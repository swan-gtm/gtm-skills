# Setup and customization checklist

Work through this before the first run.

## Placeholders

- [ ] `{{CRM}}` and `{{CRM_UPDATE_RULES}}`: how companies and contacts are found, created and associated, and which fields must never be overwritten (a good current email is never replaced by a blank or an old-employer address).
- [ ] `{{ACCOUNT_MEMORY}}`: one place per account where the conversation block and the `EVENT-ATTENDEE` line are written and can be searched later.
- [ ] `{{COMPETITOR_LIST}}`: domains and names. A match stops every lead-style write.
- [ ] `{{SCORING_PROCESS}}` and `{{TIER_NAMES}}`: the scoring this skill runs in full, including the self-serve gate and whatever alerts or MQL posts it owns.
- [ ] `{{CONTACT_MAPPING_PROCESS}}` (optional): used only to fill a thin buying committee after scoring.
- [ ] `{{CLOSED_LOST_REACTIVATION}}` (optional): used when a closed-lost account shows renewed interest.
- [ ] `{{STAGE_SYNC}}`: how a real stage move reaches `{{CRM}}`. Skip if your CRM is the only stage store.
- [ ] `{{EVENT_CALENDAR}}`: one page per event with name, dates and attendee tag (plus any extra series tag).
- [ ] `{{EVENT_TAG_FORMAT}}`: the attendee tag convention used when an event has no tag yet.
- [ ] `{{OUTREACH_PLAYBOOK}}`: routing paths (booth 1:1 vs dinner), pre-flight gates, persona pitches, writing style.
- [ ] `{{SEQUENCE_TOOL}}`: must support staging a sequence without sending it.
- [ ] `{{LINKS_AND_RESOURCES}}`: current demo and booking URLs, plus any rule for which calendar a given sender or account size uses.
- [ ] `{{TASK_TOOL}}`, `{{REMINDER_TOOL}}` and `{{PRIVATE_NOTIFY}}`: a personal task, a one-time scheduled reminder, and a private ping to the requester.

## Decisions to make

- [ ] **Closed-lost deal reuse window.** Default: open a new deal when a closed-lost account books again, unless the old deal closed lost under 30 days ago.
- [ ] **Default reminder time.** Default: 10:00 AM ET when the requester names no time.
- [ ] **Who takes the meeting.** Default: the person who had the conversation sends; the account owner takes the meeting if it books.
- [ ] **Tier names** that count as "in play" for the no-new-MQL rule.

## Behaviour that should not change

- Missing intake facts are asked for once, never invented. "We should follow up" is not a booked demo.
- The four hard gates (competitor, existing customer, self-serve, already engaged) run before any write.
- LinkedIn is the employment truth; personal email domains are never the employer.
- Relationship history is read before scoring.
- Every live, non-competitor run writes CRM, memory and the event tag, including the person-level `EVENT-ATTENDEE` line, before branching.
- A wait the lead named is a promise: no sequence reaches them during it.
- The person who met them sends. No parallel cadence from anyone else.
- Outreach is always staged for approval, never auto-sent.
- No second connection request while one is pending, and no DMs until it is accepted.
