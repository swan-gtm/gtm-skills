---
name: event-lead-ingestion
title: Event lead ingestion
description: |
  Use this skill when a teammate pastes a LinkedIn URL or work email for someone they just met at a booth, dinner or conference hallway and wants that lead captured the same way every time. It resolves the person and company, checks relationship history before scoring, writes the CRM record and a structured conversation note, tags the event at both the company and the person level, then either drafts outreach from the person who had the conversation, schedules a reminder for the wait the lead asked for, or stops at memory only. Built for ONE named person from a real conversation, where the notes are the whole advantage; badge-scan exports, attendee lists and registration lists are different plays. Also answers "I just met someone at the booth", "log this conference contact", "remind me to follow up with her after the event".
category: Events
tags: [Sales, Marketing]
---

Applies when someone on the team pastes a LinkedIn URL or work email from an in-person event conversation and wants the lead captured consistently: CRM, account memory, event tag, then the right next step.

This is not a list-upload play. It handles one named person (or a short named list in one message) from a real conversation. Badge-scan CSVs, dinner or registration lists, and web form submissions belong to your list-based post-event processes.

Preferred input is a LinkedIn URL. A work email is enough. A name plus company is the last resort.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full list and the decisions behind each.

- `{{CRM}}`: Your CRM (e.g. HubSpot, Salesforce, Attio)
- `{{CRM_UPDATE_RULES}}`: Your rules for creating and updating companies and contacts in `{{CRM}}` (dedupe, required fields, which fields never get overwritten)
- `{{ACCOUNT_MEMORY}}`: Where durable account notes live (e.g. your agent's account memory, a CRM notes field, a shared doc per account)
- `{{COMPETITOR_LIST}}`: Your competitor watchlist (domains and company names)
- `{{SCORING_PROCESS}}`: Your account scoring process: tiers, persona gates, the employee and funding gate that marks self-serve accounts, and any alerts or MQL posts it owns
- `{{TIER_NAMES}}`: Your top account tiers (default: Gold and Diamond)
- `{{CONTACT_MAPPING_PROCESS}}`: Optional: how you find more people in the buying committee at an account
- `{{CLOSED_LOST_REACTIVATION}}`: Optional: your process for re-engaging closed-lost accounts
- `{{STAGE_SYNC}}`: How account stage moves get pushed from your agent or scoring system into `{{CRM}}`, if they are separate
- `{{EVENT_CALENDAR}}`: Where each event you attend has a page with its name, dates and attendee tag (e.g. a shared doc, a Notion database)
- `{{EVENT_TAG_FORMAT}}`: Your event attendee tag convention (default: `evt:[slug]-[mmm-yy]`)
- `{{OUTREACH_PLAYBOOK}}`: Your outreach rules: routing paths, pre-flight gates, pitch by persona, writing style
- `{{SEQUENCE_TOOL}}`: Where sequences are built and staged (e.g. Outreach, Salesloft, Apollo, your agent's sequence builder)
- `{{LINKS_AND_RESOURCES}}`: Where current demo and booking URLs live
- `{{TASK_TOOL}}`: Where personal tasks are created (e.g. your CRM tasks, Asana, your agent's task desk)
- `{{REMINDER_TOOL}}`: How a one-time scheduled reminder is created (e.g. a scheduled agent run, a CRM task with a due date)
- `{{PRIVATE_NOTIFY}}`: How the requester is pinged privately (e.g. a Slack DM)

## Intake: do not invent these

If any of these are missing, ask once. Do not guess the conversation.

1. **Person:** LinkedIn URL preferred; else work email; else name plus company.
2. **Event:** name and date. If omitted and one of your events is live or just ended, read its page in `{{EVENT_CALENDAR}}` and use that event. Do not invent a different conference.
3. **Who met them:** the teammate in the room. Default to the person who sent the message.
4. **What was said:** pain, stack, interest, champion vs buyer, the next step they asked for. Use their words. Do not upgrade "we should follow up" into a booked demo.
5. **Preferred outcome:** draft outreach now, schedule a follow-up, or memory only. If they named one, that wins. If they did not:
   - They named a wait ("next week", "in 2 weeks", "after their own event") → schedule a follow-up.
   - They asked to draft, sequence, email or DM → draft outreach.
   - They said "no actions needed, just note it" → stop after CRM, memory and tags.
   - Unclear, and they just had a real 1:1 → default to drafting outreach from the person who met them.

## Hard gates (before any write)

Check `{{COMPETITOR_LIST}}` and your existing-customer records first.

- **Competitor:** memory and watchlist only. No CRM prospect writes, no tags that treat them as a lead, no alerts, no task, no outreach, no reminder.
- **Existing customer** (closed-won in your system or in `{{CRM}}`, including alias domains): log on the canonical customer record. Tag the event. Do not score as a new MQL. Do not cold-frame or trial-frame. Follow-up is expansion, not pipeline generation.
- **Self-serve:** still enrich, still write memory, still tag the event. Do not route to MQL or a sales sequence. `{{SCORING_PROCESS}}` owns the employee and funding gate.
- **Live thread or already engaged:** if someone on the team already has an unanswered inbound or a booked meeting with this person, do not stage a parallel cadence. Capture the conversation and hand off to that owner.

Check existing status before treating anyone as a net-new prospect. Enrichment tells you size, not relationship.

## Step 1: Resolve the person

Clean tracking junk off LinkedIn URLs (`utm_source`, `share_via` and the like). Keep `linkedin.com/in/{slug}`.

Fetch the live profile. Current employer and title on the live experience section win over enrichment data, `{{CRM}}`, and what the teammate remembered. If they said "she works at X" and LinkedIn says otherwise, record both and use LinkedIn as the employment truth.

You need: full name, current title, current company, LinkedIn URL, location from the current role.

## Step 2: Resolve the company

Use the work-email domain when it is not a free or personal provider. Otherwise use the current employer on the live profile. Never treat gmail, outlook, hotmail, yahoo, icloud or proton as the employer.

Find the account by domain, then the `{{CRM}}` company by domain, name, website and LinkedIn company URL. Alias and sibling domains belong on the canonical account.

Enrich firmographics enough to score: LinkedIn employee count (LinkedIn wins), funding, industry, what they sell, geography.

## Step 3: Relationship history before scoring

Read `{{ACCOUNT_MEMORY}}`, the `{{CRM}}` company and every associated contact (notes, emails, meetings, deals), and any existing sequences for this person. Open the sequence messages themselves. Do not trust a summary "replied" flag.

Capture in one pass:

- Already a customer, in a trial, closed-lost, or self-serve?
- Who owns the account?
- Unanswered asks on other contacts at the same company (do not mix those into this person's follow-up)
- Stale emails (an old employer's domain): keep LinkedIn as the follow-up channel until a current work email is verified
- Closed-lost with a prior deal: if they later book, open a **new** deal. Do not reuse the old one unless it closed lost recently (default: under 30 days)

If the account is closed-lost and this conversation looks like renewed interest, also follow `{{CLOSED_LOST_REACTIVATION}}`. Low-dollar losses over pricing friction still do not become MQLs.

## Step 4: Enrich and write the CRM

Follow `{{CRM_UPDATE_RULES}}`.

Find or create the company and the contact. Associate them. Write LinkedIn URLs on both. Set the contact's city from the LinkedIn current-position location. Enrich the work email when it is missing; never overwrite a good current email with a blank or an old-employer address.

Add a note associated to both contact and company:

- **Title:** `{Event name}: {booth | dinner | 1:1} with {Person}`
- **Body:** bullets only: who met them, where, what they said, champion vs buyer, the next step they asked for, the wait window if any

Do not invent a deal from a booth chat. A deal already closed-lost stays closed-lost until a real meeting is on the calendar.

## Step 5: Score

Run `{{SCORING_PROCESS}}` in full. The in-person conversation is a first-party intent signal: treat it as intent scoring, not as a website visit.

- Already in `{{TIER_NAMES}}` with an owner working it → scoring may reconfirm. Do not post a net-new MQL. Route it like an in-play account.
- A champion or non-buyer at a large account can still land in a top tier if the account clears your persona gates. Do not pretend the champion is the closer.
- `{{SCORING_PROCESS}}` owns any alerts, MQL posts, buying-committee enrichment and completion checks. This skill does not invent a second MQL post.
- After scoring, if the buying committee is still thin for a top-tier account, use `{{CONTACT_MAPPING_PROCESS}}` only for the gap. Do not duplicate what scoring already did.

Push a stage change to `{{CRM}}` through `{{STAGE_SYNC}}` only when scoring (or a real stage change from this conversation) actually moved the stage. Never move an existing customer backward.

## Step 6: Account memory

Write durable facts to `{{ACCOUNT_MEMORY}}`, not a transcript dump.

Must include:

- One searchable `EVENT-ATTENDEE` line per person per event:

```
EVENT-ATTENDEE | {YYYY-MM-DD} | {Person} | {Event name} | {event dates} | Event lead ingestion | {sender} | {event tag}
```

  If the line already exists, do not duplicate it; append the play or sender only if new.

- **Conversation block:** date, who met them, setting (booth, dinner, hallway), what they said in their words, stack and pain, champion vs decision-maker, the next step they asked for, the wait window
- **Relationship change:** already connected, connection request pending, first meeting, personal connection formed
- **Account landmines:** prior trial, declined demo, unanswered thread on a colleague, stale email, closed-lost reason
- **Next play** in one line (demo then multi-thread; memory only; wait until DATE)

Do not cold-frame an in-play account.

## Step 7: Tag the event

Read the event's page in `{{EVENT_CALENDAR}}` and use that page's attendee tag. If the tag does not exist yet, create it in `{{EVENT_TAG_FORMAT}}` and record it on the event page before applying it.

Apply the attendee tag to the company. Do not strip other tags. Also apply any extra tag the event page names (some events carry a series tag alongside the attendee tag). Use the live tag name as written, not a guess at its spelling.

Mark the `{{CRM}}` contact as an event attendee the same way your event attendance tracking requires. A company tag is not proof this named person was there; the `EVENT-ATTENDEE` line is.

## Step 8: Branch on the preferred outcome

Do CRM, memory and tags on every live, non-competitor run before this branch.

- **Memory only:** stop. Tell the requester what was written. No sequence, no reminder.
- **Schedule a follow-up:** follow the schedule-follow-up reference.
- **Draft outreach:** follow the draft-outreach reference.

If they asked for both ("draft something and also remind me next week"), the reminder is the system of record for the wait. Only stage outreach if they also want something to send *now*. Never stage a cadence that would reach them during a wait they requested.

## Reply to the requester

Short. What was captured, the score, champion vs buyer, landmines, and what happens next (staged sequence, reminder date, or memory only). Call out the stale-email, unanswered-colleague-thread and closed-lost-reuse traps when they exist.

## What good looks like

Spot first: is this a real 1:1 with notes, or a scan with no conversation? Notes are the whole advantage. Then: did they ask us to wait? A wait beats a sequence.

What gets overlooked:

- Treating "follow up sometime" as a booked meeting. No date on a calendar is not Hot.
- Scoring a champion as the buyer, then pitching them as if they can sign.
- Opening a second cadence to the person who just met us, from a different sender.
- Reusing a closed-lost deal when a new meeting appears.
- Writing the company event tag and skipping the person-level `EVENT-ATTENDEE` line.
- Mixing a colleague's unanswered thread into this person's follow-up.
- Emailing an old-employer address because the CRM still has it.

Failure modes:

- Running a list-based post-event play on a single pasted LinkedIn URL from a booth chat (this skill first; those plays own lists).
- Cold or trial framing an existing customer or an in-play top-tier account.
- Surfacing a competitor as a lead.
- Staging outreach during an explicit wait window.
- Auto-sending anything, above all to a senior executive at a 100+ employee company.
- Inventing pain the teammate did not report.

Success: the next teammate can open the account and see who we met, what was said, which event they belong to, and either a staged follow-up in the voice of the person who met them or a reminder that fires on the date they asked for, without re-prompting anyone.
