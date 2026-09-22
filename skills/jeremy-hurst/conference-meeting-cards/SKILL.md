---
name: "conference-meeting-cards"
title: "Conference meeting cards"
description: "Use this skill before a conference, roadshow, or any day of back-to-back in-person meetings when the person walking the floor needs one phone-ready screen per meeting, not a chat brief. For each meeting it enriches the attendees (photo, title, LinkedIn), pulls the live deal amount, stage, and next step from your CRM, and writes at most six short deal-context bullets in a fixed order: what they do, amount, stage plus next step, use cases, the people who matter, relationship context, and an optional key risk. It renders one self-contained HTML file per day, printable to PDF with one meeting per page, and DMs a share link to the teammates who are at the event."
category: Events
---

# Conference meeting cards

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{CARD_OWNER}}` - The person the cards are written for (usually the seller walking the floor)
- `{{CRM}}` - Your CRM (e.g. HubSpot, Attio, Salesforce) and the field names for deal amount, stage, next step, and close date
- `{{STAGE_LABELS}}` - Your CRM stage identifiers mapped to the human labels that should print on a card
- `{{MEETING_NOTES_TOOL}}` - Your meeting-notes or call-recording tool (e.g. Circleback, Gong, Fireflies), used as the next-step fallback
- `{{NEXT_STEP_LOOKBACK_DAYS}}` - How far back to search meeting notes for a next step when the CRM field is empty (default: 60)
- `{{FULL_BRIEF_SKILL}}` - Your full pre-call meeting-prep skill. This skill is the walking-floor card, not that brief.
- `{{DESIGN_TOKENS}}` - Your brand colors and type, if you have a design reference the template should follow
- `{{OUTPUT_FOLDER}}` - Where day files are saved (default: `events/{event-slug}/meeting-cards/{YYYY-MM-DD}.html`)
- `{{MAX_BULLETS}}` - Deal-context bullets per card (default: 6, optional 7th for a real key risk)
- `{{BULLET_CHAR_CAP}}` - Characters per bullet (default: 150)
- `{{EVENT_TEAM}}` - Who receives the share link by DM for this event (a per-event list, asked for if not given)

---

### Instructions

Load this skill when the ask is a walking-floor card, not a chat meeting-prep brief. For a full pre-call brief, use {{FULL_BRIEF_SKILL}} instead.

Voice is sales-first. One screen per meeting. No fluff.

### Input required before research

You need the event name, the date or dates, and per meeting: time (or TBD), company (domain preferred), and attendee names. Location is optional. Recipients for the DM are a per-event list; ask who is attending this conference before sending. Do not scrape {{CARD_OWNER}}'s calendar unless they say to.

### Procedure

1. Normalize the event slug and the meeting list. Group by date. Keep {{CARD_OWNER}}'s order when times are TBD.

2. Per company: read the account record and account memory (and the key-account folder if memory points there). Search {{CRM}} for the company and associated deals. Fetch amount, stage, next step, deal name, and close date. An open deal is associated and not closed-won or closed-lost. If several, use the most recently modified. Print stage labels from {{STAGE_LABELS}}; for an unknown stage identifier write "Unknown (id)" rather than guessing.

3. Per attendee: enrich for photo, title, and LinkedIn URL. Apply your enrichment-failure and LinkedIn-employer-mismatch checks (the ones from {{FULL_BRIEF_SKILL}}). No web search for emails or phones. The photo comes from enrichment or a LinkedIn profile fetch. Initials fallback if the image fails.

4. If the CRM next-step field is empty: use the latest forecast next move in account memory, else search {{MEETING_NOTES_TOOL}} for that domain in the last {{NEXT_STEP_LOOKBACK_DAYS}} days (the latest concrete next step or action item, not a transcript dump). Else omit the next-step clause.

5. Write the deal-context bullets in the order below. Enforce the {{BULLET_CHAR_CAP}}-character cap (truncate with an ellipsis). Skip any bullet with nothing true to say.

6. Load {{DESIGN_TOKENS}} if set (otherwise keep the template's default palette) and the day-card template reference. Fill one self-contained HTML file per day. Re-read before delivering.

7. Save to {{OUTPUT_FOLDER}}. Create the event folder if needed.

8. Confirm with {{CARD_OWNER}} before publishing, then create an unguessable, expiring share link for that day's HTML so phones can open it without a workspace login. The cards carry deal amounts, champions, and risks: DM the link to named people only, never post it in a shared channel. Ask who should get the DM if not already named. DM each person in {{EVENT_TEAM}}: event, date, meeting count, share link. No card contents in the DM. If {{CARD_OWNER}} asked in chat, also return the file path plus a one-line takeaway (meeting count + verify flags). Do not recap cards.

Enrichment costs roughly one lookup per attendee, plus a LinkedIn profile fetch for photos when enrichment has none. Batch. Skip people already verified in this run.

### Card anatomy

**Header.** Time plus location if known; omit location rather than invent it. If time is unknown, show "Time TBD". The company name is the only large headline. A tiny generated-date line.

**Attendees.** Photo, name, title. The name is the LinkedIn link (large tap target). A visible `linkedin.com/in/...` under the name so the PDF still works. On an enrichment miss: initials only, no invented title, and a "verify details" flag.

**Deal context.** Short bullets. Default max {{MAX_BULLETS}}. Each at most {{BULLET_CHAR_CAP}} characters. Optional 7th only for a real key risk.

1. **What they do.** One sentence a college junior in business could understand. From the account record, their site, or memory. Plain English, not pitch language.
2. **Amount.** The {{CRM}} amount if an open deal exists. Else a short ACV assessment, clearly labeled as an estimate. Never invent a CRM number.
3. **Stage + next step.** Open deal: the stage label plus the next-step field (or the fallback from step 4). No open deal: a one-line conversation stage (e.g. "first live discussion after pre-event outreach").
4. **Use cases.** Only if there is an active deal. Skip if none known.
5. **Important people.** Champion, budget, blocker for this conversation. Not a roster dump.
6. **Relationship context.** Only if meaningful (customer or investor referral, prior meeting, mutual connection, champion who moved). Skip if none.
7. **Key risk (optional).** Only if memory holds a real risk (prefer the latest forecast note's key risk). Skip if none.

### Day file

One file per calendar day. Meetings stacked chronologically, or in list order if times are TBD.

Sticky top bar: event name, weekday and date, meeting count, jump links. Attendee chips wrap. Deal context is a tight bullet list under them. Print: one meeting per page, card backgrounds print, no sticky chrome. Light mode only. Snapshot HTML, not a live app. Export: browser Print, Save as PDF, backgrounds on.

Visual language follows {{DESIGN_TOKENS}}: circular photos, initials fallback. Time is the spine between meetings. No placeholder copy in filled files.

## What good looks like

{{CARD_OWNER}} can open the PDF on their phone between sessions and know who is in front of them, what the deal is worth, and the one thing not to get wrong, without scrolling a chat brief.

Spot first: an empty CRM next step, a missing photo, a LinkedIn employer mismatch, and optional bullets that should have been skipped.

Overlooked: inventing a title after enrichment failed; repeating amount and stage in extra cells; stuffing five "important people" who are not in this conversation; sending the DM before asking who is at the event.

Failure modes: a dashboard of identical cards; a fake CRM amount on a no-deal meeting; a transcript pasted into the next step; a DM body that recites the cards.

Success: one HTML per day, real photos, real CRM numbers, skipped empty bullets, and a share link DMed to the people {{CARD_OWNER}} named.
