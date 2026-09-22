---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. When it runs

This play is invoked on demand, not on a schedule: an attendee-list upload
for a named conference, or an explicit "run pre-conference outreach on these
people". Reference invocation:

```
Run the <Pre-conference outreach> play on the attached attendee list for
[EVENT_NAME] ([EVENT_CITY], [EVENT_DATES]). Side events: [EXEC_SIDE_EVENT] and
[PRACTITIONER_SIDE_EVENT]. Stage everything for approval.
```

- [ ] The three senders' email and LinkedIn accounts are connected to the
      workspace.
- [ ] The attendee list has, per row: name, company or domain, title, and
      a LinkedIn URL where available. Rows without a resolvable LinkedIn URL
      run email-only and get flagged.

## 2. Placeholders

- [ ] `{{EVENT_NAME}}`, `{{EVENT_CITY}}`, `{{EVENT_DATES}}` - refresh per
      conference. The M3 line names the event, so a stale name is a
      visible mistake.
- [ ] `{{EXEC_SIDE_EVENT}}`, `{{PRACTITIONER_SIDE_EVENT}}` - written as they
      read inside a sentence ("an exec dinner on Tuesday night"). If you only
      run one side event, point both placeholders at it and note that
      Scenario 1 and 2 then differ only by sender.
- [ ] `{{EXEC_SENDER}}`, `{{SALES_LEADER_SENDER}}`, `{{PRACTITIONER_SENDER}}` -
      one person each. If one person covers two lenses, name them twice; the
      mandate rules still decide the angle.
- [ ] `{{EXEC_SENDER_MIN_ORG_SIZE}}` - default 100. This is the line below
      which a founder or exec sender is overkill and the sales leader gets the
      exec-persona contact instead.
- [ ] `{{CRM}}`, `{{ATTENDEE_TAG}}`, `{{M1_CHAR_CAP}}` (default 250),
      `{{SIGNAL_LIBRARY}}` (optional), `{{VOICE_GUIDE}}` (optional).

## 3. Policy decisions

- [ ] **Everyone on the file gets sequenced.** Scoring tier does not skip
      anyone here; only the standard gates (customer, live thread, booked
      meeting, engaged owner) remove a row. If you want tier-based skipping,
      you are running a different play.
- [ ] **Queued for approval, always.** The original internal version of this
      play never auto-sends either. Keep it that way for the first few conferences at
      minimum.
- [ ] **The exec size gate** - confirm 100 matches where your exec sender's
      time stops being worth it. Raise it if your exec should only touch
      enterprise.
- [ ] **The practitioner never contacts sellers.** Decide whether that rule
      holds for your practitioner sender; it exists because a hands-on
      operator DMing a VP Sales reads as off-lens.
- [ ] **Side-event links are offered, never pasted.** The reply asking for
      the link is the engagement you want.
- [ ] Decide what your "closed-lost research procedure" is and where it
      lives. This play calls it whenever a prior deal exists and does not
      define it.

## 4. Behavioral invariants (do not remove)

- Research line (`research: ... ; prior deal: ...`) on every row before a
  draft exists. No line, no build.
- M1 under the cap, counting the full body including the name.
- M2 and M3 verbatim, nameless; only the this-week / next-week timing on
  M3 changes.
- Blank connection requests: no note text.
- The attendee list is never named as the source.
- Attendee line written to memory and tag applied after staging, for
  sequenced and connection-only rows alike, one per person per event.
