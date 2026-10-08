---
title: Setup and customization checklist
description: Trigger setup, placeholders, policy decisions and the behaviour that must never be removed.
---

# Setup and customization checklist

## 1. Trigger setup

The skill fires when a candidate moves to an offer stage, or on demand ("build the close for [candidate]"). Reference trigger:

```
[Candidate] has moved to offer stage for [role].

Load and follow the <Sales hire offer close> skill in full.

Context for this run:
- Candidate and role: [ATS link or ID]
- Approved ceiling and approver: [figure, name], or "not yet approved"
- Who holds the candidate relationship: [name]
- Target start date, if known: [date]
```

- [ ] `{{ATS}}` returns interview and debrief notes, not only stage changes. The motive check depends on the notes.
- [ ] `{{COMP_APPROVER}}` is named per role, and knows they are asked for a ceiling before the offer, not a sign-off after.
- [ ] `{{CALENDAR}}` can create events or tasks for `{{OFFER_OWNER}}`.
- [ ] `{{REVIEW_CHANNEL}}` exists and the hiring manager reads it.

## 2. Placeholders

- [ ] `{{ATS}}`, `{{COMP_APPROVER}}`, `{{REVIEW_CHANNEL}}`, `{{CALENDAR}}`, `{{OFFER_OWNER}}`, `{{CURRENCY}}`, `{{PACKAGE_BASIS}}` all filled.
- [ ] `{{PACKAGE_BASIS}}` written out in one line, including how equity is valued. Without it, two people compare different numbers.

## 3. Policy decisions

- [ ] **Start in trial mode** for the first three offers.
- [ ] **What flexes without a new approval.** Sign-on, equity, start date, title, review date. Write it down.
- [ ] **Sign-on clawback terms.** Decide them now, not during the close.
- [ ] **Commission disclosure.** Decide what you will show a candidate about how the last cohort was actually paid. If the honest answer is uncomfortable, fix the plan before hiring into it.
- [ ] **Your own gap thresholds.** The defaults in `offer-structures.md` are practice-based. Replace them with your own once you have ten offers of data.

## 4. Behaviour that must never be removed

- The close-ready gate runs first, and a failed check stops the plan.
- No figure is estimated. Every number is confirmed by the candidate or the approver.
- Every structure is priced on cost, signal and risk.
- The counter-offer rating cites its evidence.
- Statistics are used only with their source, year and population.
- No pressure tactics, guilt or exploding deadlines.
- Protected attributes are never inputs.
- No offer is made, changed or recorded as accepted without a human.
- Every write is read back, and failures are reported on the card.
