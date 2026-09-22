---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. When it runs

On demand, in chat. Reference invocation:

```
Prep me for [EVENT_NAME] meetings. [DATE]: [time or TBD] [Company] with
[Attendee names]; [time or TBD] [Company] with [Attendee names]. Send the
link to [names].
```

- [ ] Enrichment (photo, title, LinkedIn URL) is available to the agent.
- [ ] {{CRM}} read access covers companies, deals, and the deal fields
      named in the placeholders.
- [ ] The agent can save a file to {{OUTPUT_FOLDER}} and create a public
      share link for it. If it cannot, it returns the HTML for you to host.

## 2. Placeholders

- [ ] `{{CARD_OWNER}}` - one person; run one instance per seller if several
      people walk the floor with different books.
- [ ] `{{CRM}}` field names for amount, stage, next step, close date, and
      `{{STAGE_LABELS}}` mapping raw stage identifiers to printable labels.
      Unknown identifiers print as "Unknown (id)"; do not let the agent
      guess a label.
- [ ] `{{MEETING_NOTES_TOOL}}` and `{{NEXT_STEP_LOOKBACK_DAYS}}` (default 60).
- [ ] `{{FULL_BRIEF_SKILL}}` - the skill this one is *not*. Point it at your
      pre-call brief so the agent picks the right one.
- [ ] `{{DESIGN_TOKENS}}` - optional. The day-card template reference ships
      with a neutral palette you can keep.
- [ ] `{{OUTPUT_FOLDER}}`, `{{MAX_BULLETS}}` (default 6),
      `{{BULLET_CHAR_CAP}}` (default 150), `{{EVENT_TEAM}}`.

## 3. Policy decisions

- [ ] **Six bullets, 150 characters each.** This is a card read while
      walking, not a brief. Raising either number turns it back into a
      brief.
- [ ] **Never invent a CRM number.** A no-deal meeting gets a labeled ACV
      estimate or nothing. Confirm your team is fine seeing "No open deal"
      on a card.
- [ ] **No calendar scraping by default.** The owner lists the meetings.
      Flip this only if your calendar is clean enough to trust.
- [ ] **Share link before DM, and the link is gated.** The owner confirms
      before anything is published, the link is unguessable and expiring,
      and the DM carries only the link and a count, never the card contents,
      so deal amounts and risks never land in a shared channel.
- [ ] **Ask who is at the event.** Recipients are per event; the agent
      asks rather than DMing a default list.

## 4. Behavioral invariants (do not remove)

- Enrichment miss means initials and "verify details", never an invented
  title.
- Bullet order is fixed; empty bullets are skipped, not padded.
- One HTML file per calendar day, self-contained, printable one meeting
  per page.
- The agent returns a file path and a one-line takeaway in chat, and never
  recaps the cards.
