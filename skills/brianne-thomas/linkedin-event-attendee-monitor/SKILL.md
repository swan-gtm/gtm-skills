---
name: "linkedin-event-attendee-monitor"
title: LinkedIn event attendee monitor
description: "Use this skill when scanning LinkedIn for people or companies posting about attending an upcoming event. Builds a company watchlist of attendees, alerts account owners when their customers or open deals are going, and flags ICP-fit people for human LinkedIn outreach with a ready-to-use comment and coffee-ask connection note. Never likes, comments, or connects on its own."
category: Events
---

## Template placeholders

- `{{EVENT_NAME}}` - The event you are monitoring, by its full public name.
- `{{EVENT_SEARCH_QUERIES}}` - The phrases and hashtags people use when posting about it (event name, short name, hashtags, "<event> <city>").
- `{{DEDUP_RECORD}}` - A record your workspace can write to on every run, used to store already-processed post URLs (e.g. your own company's account record).
- `{{ATTENDEE_TAG}}` - The tag applied to companies found attending (e.g. "<event> attendee").
- `{{ALERT_CHANNEL}}` - The Slack channel where alerts and drafted copy land.
- `{{ALERT_OWNER}}` - The person tagged on ICP-fit alerts, who owns the LinkedIn follow-up.
- `{{ICP_DEFINITION}}` - Your ICP segments, their revenue/employee thresholds, and the buying-committee personas for each.

### Purpose

Find people and companies publicly posting on LinkedIn that they are attending {{EVENT_NAME}}. Companies go on a running watchlist. People get checked against your full ICP bar. Fits are routed to a human rep to like, comment, and send a connection request, because the agent cannot perform any of those three actions itself.

### Step 1: Search for new posts

Run the `harvestapi/linkedin-post-search` Apify actor (actorId: `harvestapi/linkedin-post-search`) with:
- `searchQueries`: all of {{EVENT_SEARCH_QUERIES}}, run together in one call.
- `postedLimit`: "3months" is too wide. Use `postedLimitDate` if narrowing further is possible, otherwise use `postedLimit: "week"` and rely on dedup (below) to avoid reprocessing. If the trigger is running every 3 days, "week" gives enough overlap to not miss posts between runs.
- `sortBy`: "date"
- `maxPosts`: 40 per query (adjust up only if volume clearly exceeds this)

### Step 2: Dedupe

Store the running list of already-processed post URLs in {{DEDUP_RECORD}}. Pick a record this workflow can reliably write to on every run (org-level memory is often admin-only and not available to a scheduled run).

Use a clearly labeled section, e.g. "### {{EVENT_NAME}} - Processed Posts", with one line per processed post: date + URL. Before acting on any post returned by the search, skip it if its URL is already listed there. After processing a batch, append the newly processed post URLs (with date) to that section. Prune entries older than 14 days on each write, since the search window looks back one week and runs happen every 3 days. There is no need to retain more than that, and this keeps the note from eating into the record's memory budget.

### Step 3: Classify the author

For each new post:

- **If the author is a LinkedIn Company Page** - this is a company posting (e.g. a company account sharing that it will be attending or exhibiting). Look up the company in your workspace by domain/name. If it doesn't exist, create it. Add the tag {{ATTENDEE_TAG}}. Log the post URL and post date in that company's account memory as a running note of the source post.
  - If the company's funnel stage is Customer or Opportunity, also post a short FYI to {{ALERT_CHANNEL}} noting the existing relationship, the recorded owner, and the post URL, so the account owner knows their account is publicly attending. No coffee-ask copy, no "prospecting" framing, this is an FYI only.
  - No further action beyond that. No outreach, no ICP re-check.

- **If the author is a person** - resolve their current employer (from their profile/headline in the scraped data, enrich further if needed). Look up that employer in your workspace first.
  - If the employer's funnel stage is Customer or Opportunity, do not run the ICP prospecting flow. Instead, post a short FYI to {{ALERT_CHANNEL}}: person's name/title, employer, funnel stage, recorded owner (if any), the post URL, and the person's LinkedIn profile URL. Do not draft "grab coffee" connection-request copy for someone already at a customer or active deal. Treat this as a relationship signal for the account owner, not a new-logo prospecting opportunity. Stop here.
  - If the employer is not an existing Customer/Opportunity (Target, Aware, Hand Raiser, Closed Lost, Competitor/Partner, or not yet in your workspace), run your full standard ICP check against {{ICP_DEFINITION}}: does the employer match one of your ICP segments, meet the segment's revenue/employee thresholds, and does the person's title match one of that segment's buying-committee personas (decision maker, technical buyer, influencer, champion, or user roles)? Use the same qualification logic you use everywhere else. Do not loosen the bar for this play.
    - **Not ICP fit** → no action, no message, no log needed beyond dedup.
    - **ICP fit** → go to Step 4.

### Step 4: Draft copy and alert a human (ICP-fit people only)

Draft two pieces of copy, following your org's humanizing and voice rules (for example: no em dashes, never abbreviate your company name, no "angle" language, no "no agenda" language):

1. **Comment** - casual, "see you there" style, personalized with the person's first name. Rotate across variants like:
   - "Looking forward to connecting in person, {first name}!"
   - "See you there, {first name}!"
   - "Fantastic, looking forward to seeing you there!"
   Do not write a comment that reacts to post content or invents a fake shared detail. Keep it to the fact that we'll both be at the event.

2. **Connection request note** - includes the coffee-meetup ask, e.g.: "Hey {first name}, saw your post about {{EVENT_NAME}}. I'll be there too, would love to grab coffee if you're open to it." Note this only actually sends if the connecting LinkedIn sender has Sales Navigator. Flag this caveat every time.

Then post to {{ALERT_CHANNEL}}, tagging {{ALERT_OWNER}}, with:
- Post URL
- Author name, title, company
- The author's LinkedIn profile URL
- One-line reason they clear ICP (segment + persona match)
- The chosen comment
- The connection request note (with the Sales Navigator caveat)
- Note that the LinkedIn sender for this play is still TBD. Do not assign one; just flag the copy is ready whenever a sender is chosen.

Batch all ICP-fit people found in a single run into one Slack message (or one message per person if the batch is large and a single message would be unwieldy. Use judgment, but keep it to as few messages as reasonably possible per run).

### What NOT to do

- Never attempt to like, comment, or send a connection request/DM directly. The agent has no tool for this and must not claim it happened.
- Never build or send an outreach sequence for this play until a sender is explicitly assigned. That's a future upgrade, not part of this flow.
- Never lower the ICP bar to include non-buying-committee attendees just because the event is a local networking event. The full ICP bar applies.
