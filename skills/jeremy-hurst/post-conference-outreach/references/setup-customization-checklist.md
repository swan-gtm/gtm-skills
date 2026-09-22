---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. When it runs

Invoked on demand: a booth or badge-scan export after a conference, or a
chat ask naming the scans to follow up. Reference invocation:

```
Run the <Post-conference outreach> play on the attached badge-scan export
from [EVENT_NAME]. Notes start with scanner initials. Stage everything for
approval.
```

- [ ] Every teammate who worked the booth has email and LinkedIn connected
      to the workspace, so they can be the sender of their own scans.
- [ ] The scan export has, per row: name, company or domain, title, notes,
      and (ideally) a temperature column. Ask the team to prefix notes with
      their initials while scanning; that one habit is what makes the
      sender rule work.

## 2. Placeholders

- [ ] `{{SCANNER_INITIALS_MAP}}` - every person who scans, including
      non-sales teammates. Unknown initials should be flagged, not guessed.
- [ ] `{{EXEC_SENDER}}`, `{{SALES_LEADER_SENDER}}`, `{{PRACTITIONER_SENDER}}`,
      `{{EXEC_SENDER_MIN_ORG_SIZE}}` (default 100) - used only on the persona
      fallback when nobody can tell who had the conversation.
- [ ] `{{ELEVATOR_PITCH}}` - one pitch variant per persona (seller,
      RevOps/GTM eng, marketing, exec). M2 pulls from here, never inline.
- [ ] `{{DEMO_LIBRARY}}` - demo URLs keyed by use case. DM1 picks one and
      records why.
- [ ] `{{LEAVE_BEHIND_RESOURCE}}` - something genuinely useful to a person
      who never buys. The original internal version uses a public skills
      library; a playbook, template pack, or free tool works the same way.
- [ ] `{{CALENDAR_LINKS}}` - per-sender booking links, plus the rule for a
      non-sales sender (default: drop {{SALES_LEADER_SENDER}}'s intro calendar
      as the handoff) and for the exec sender (default: their own calendar
      only at 200+ employees).
- [ ] `{{EVENT_NAME}}`, `{{PRODUCT}}`, `{{CRM}}`, `{{ATTENDEE_TAG}}`,
      `{{M1_CHAR_CAP}}` (default 250), `{{VOICE_GUIDE}}` (optional).

## 3. Policy decisions

- [ ] **Hot means a date on the calendar.** "Let's find time" is Warm.
      Confirm the team agrees before the first run, or every enthusiastic
      scan will be mislabeled Hot.
- [ ] **Account-max temperature.** One booked meeting makes every scan at
      that company Hot. This is deliberate: a colleague of someone you are
      about to meet should be invited in, not nurtured separately.
- [ ] **The Hot exception to your booked-meeting gate.** Most outreach
      systems refuse to sequence anyone with a meeting on the calendar. This
      play needs a scoped exception for Scenario 1 only. Add it to your gate
      logic explicitly; do not disable the gate.
- [ ] **Queued for approval, always.** The original internal version never
      auto-sends on this play either.
- [ ] **The +25% cap bump** exists only for a real prior thread woven into
      M1. Decide whether you want it at all; without it the cap is simply
      {{M1_CHAR_CAP}}.
- [ ] **Partner conversations stay partner conversations.** If a
      partnerships teammate scanned someone, do not let the sequence drift
      into a customer pitch and calendar drop.

## 4. Behavioral invariants (do not remove)

- Initials win over the persona rubric, every time.
- Research line (`research: ... ; prior deal: ... ; history: ...`) on every
  row before a draft exists.
- Temperature from facts, then account-max, then scenario.
- Scenario 1 is two steps and never pitches. Scenario 2's later DMs are
  unevenly spaced on purpose (days 7, 12, 19, 27).
- Booth notes are stripped of initials before they reach the email.
- Pitch, demo, and calendar URLs are pulled from references, never typed
  into the sequence.
- The scan or list is never named as the source.
- Attendee line written to memory and tag applied after staging, one per
  person per event.
