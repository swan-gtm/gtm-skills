---
name: post-event-roi-report
title: Post-event ROI report
description: Use this skill when a GTM team needs to show what one or more events produced, at 30 and 60 days, by joining an event lead list with CRM deals. Covers attribution, excluding pre-existing pipeline, funnel counts, pipeline and closed-won math, checkpoints, breakdowns and follow-up health.
category: Events
tags: [Events, RevOps]
---

# Post-event ROI report

Build a view that answers one question for the review meeting: what did {{EVENT_NAMES}} produce, and what is stuck? The lead list says who we met. The CRM says what became pipeline. When they disagree, the CRM wins.

## Template placeholders

Replace every `{{...}}` before running.

- `{{EVENT_NAMES}}`: the events being measured, exactly as they appear in the lead list's Event column
- `{{EVENT_START_DATE}}`: the first day of the first event; the cutoff for new versus pre-existing pipeline
- `{{DAY_30_DATE}}`, `{{DAY_60_DATE}}`: the two checkpoint dates
- `{{SPREADSHEET}}`: where the event lead list lives
- `{{ICP_FLOOR}}`: the minimum employee count that counts toward the totals
- `{{CURRENCY}}`: currency for spend and pipeline
- `{{TIER_LIST}}`: your account tiers
- `{{STALL_DEMO_DAYS}}`, `{{STALL_STAGE_DAYS}}`: stall thresholds (for example 10 and 14)
- `{{SPECIALIST_TEAM}}`: a team follow-ups often wait on, such as RevOps

## Inputs

**Event lead list** ({{SPREADSHEET}}, re-read on every load, never hardcoded). One row per account. Several people at one account stay on one row and count once. Columns used:
- Company, Person, Title, Employees, Tier, Owner, Priority
- Event (must match one of {{EVENT_NAMES}} or "Both")
- Meeting status, Demo held (date), Opp created (date), Opp amount, Opp stage
- Next step, Follow up by (date), Notes

**Side tabs.** Partners, community and investors go in their own section and stay out of every total. Accounts under {{ICP_FLOOR}} employees stay out of the totals and appear only as a count in a footnote.

**CRM deals.** Name, amount, stage, create date, close date, date entered current stage, closed-won and closed-lost flags. Fetch every deal created in the last year and match in code. Do not query one account at a time.

**Manual input.** Event spend in {{CURRENCY}}. The list does not hold it. Store it, and leave the ratios blank until someone enters it.

## Attribution rules

1. An account counts only if Event names one of {{EVENT_NAMES}} or "Both". Rows marked "Not an event lead" or "Unknown" go to a separate "Other leads needing a reply" list. They do not count toward ROI.
2. Match accounts to deals by normalized company name (lowercase, letters and digits only). Handle parenthetical aliases. Accept a prefix match only when both names are six or more characters. Report unmatched event accounts so a person can check them.
3. **Exclude pre-existing pipeline.** A deal created before {{EVENT_START_DATE}} is not event pipeline. Use the CRM create date first. Fall back to a note such as "already in pipeline before the events" or a status of "Existing deal". Show these accounts as "Influenced (existing pipeline)", with the reason, outside the headline.
4. An account with both an old deal and a new deal created on or after the start date counts on the new deal.

## Funnel stages

- **Accounts engaged:** attributed accounts, minus influenced accounts.
- **Meeting booked:** status contains held, booked or rescheduling, and is not "not booked". Declined and no-response do not count.
- **Demo held:** the demo column holds a date.
- **Opp created:** a CRM deal exists with a create date on or after {{EVENT_START_DATE}}, or the list has an opp date on or after it.
- Show each stage as a number with the conversion percentage from the previous stage.

## Money

- **Pipeline:** sum of CRM amounts for event opps. Exclude closed-lost deals.
- **Opp, no amount yet:** count the opp, add $0, and flag it by name. Never impute an amount.
- **Closed won:** CRM stage is closed won and the deal was created on or after {{EVENT_START_DATE}}. A closed-won deal that predates the event is influence, not revenue produced.
- **Ratios:** pipeline to spend and closed-won to spend, recalculated live from the spend input.
- **Expected to land by Day 60:** pipeline whose CRM close date is on or before {{DAY_60_DATE}}.

## CRM-wins conflict rule

If the list and the CRM differ on amount or stage, show the CRM value and flag the row "list differs from CRM", with both values. Never average or pick the larger. If an opp exists only in the list, count it, mark "no CRM deal found", and ask the owner to create the deal.

## Checkpoints

Show Today, Day 30 ({{DAY_30_DATE}}) and Day 60 ({{DAY_60_DATE}}) side by side, with the same metrics in each. Freeze each snapshot once its date passes, and store the freeze timestamp with it. If freezing depends on someone opening the report, label the real freeze date on the card. A scheduled job that writes the snapshot on the exact date is better.

## Breakdowns

- By event: each event name, and "Both".
- By owner: split shared owners evenly, or show them as "Shared". Pick one and say which.
- By tier: {{TIER_LIST}}, plus "other" for blanks.
- Each breakdown shows accounts, meetings, demos, opps, pipeline and closed won.

## Account table

One row per attributed account: company, person and title, employees, tier, owner, event, meeting status, demo date, CRM amount, CRM stage, next step, follow-up date. Make it sortable. Filter by owner, event and stage. Default sort is pipeline high to low, then priority.

## Follow-up health

- **Overdue:** follow-up date is before today and no meeting is booked. Group by owner.
- **Stalled:** a demo was held {{STALL_DEMO_DAYS}} or more days ago with no opp, or an opp has had no stage change for {{STALL_STAGE_DAYS}} or more days. Use the date entered the current stage, not the last modified date.
- **Waiting on {{SPECIALIST_TEAM}}:** notes or next step mention it. Flag these so that team can be looped in.

## Known limits

- Reads happen on open or on a manual refresh. Nothing updates in the background.
- Name matching to deals is approximate. Check unmatched and multi-match accounts by hand.
- Stage names depend on a mapping of CRM stage IDs, which differs per CRM account. Unknown IDs should show raw, not be guessed.
- Meeting status and demo dates are typed by people. The report is only as current as the list.
- Attribution is by the Event column. It shows association with the event, not proof that the event caused the deal.

## What good looks like

**Sanity-check the headline before anyone sees it.** An expert has a reference number from the team, such as the pipeline figure quoted in the debrief. They compute it by hand from the list and CRM, then confirm the report lands within a few percent. If it does not, the attribution logic is wrong, and the fix comes before any design work.

**Protect the credibility of the total.** The mediocre version counts every deal at an event account, including a renewal opened two weeks before the event. The first skeptical finance person finds it, and the whole report is discredited. The expert shows influenced pipeline separately and says so on the page.

**Treat the CRM as the only source for money.** The mediocre version trusts the typed amount and stage in the list. The expert reads both, shows the CRM, and uses the mismatch list as a to-do for owners.

**Report what is missing instead of filling it.** Opps without amounts, accounts without a CRM deal and unmatched names appear as named items. A silent zero hides the work that still needs doing.

**Make the checkpoints honest.** The mediocre version shows live numbers labeled "Day 30". The expert freezes the snapshot with a timestamp, so Day 60 can be compared with Day 30 without argument.

**Keep follow-up health actionable.** A count of overdue leads changes nothing. A list grouped by owner, with the next step and days overdue, gets read in the meeting. Cap each list so a person can act on it.

**Do not over-build.** Add the breakdowns and filters the review needs. A pie chart per column makes the page harder to scan and adds no decision.
