---
title: Setup and customization checklist
description: Trigger setup, placeholders, policy decisions and the behaviour that must never be removed.
---

# Setup and customization checklist

## 1. Trigger setup

On demand, when a founder or leader asks about a first sales hire, and on the re-run date from any Not yet card. Reference triggers:

```
[Founder] wants to hire their first salesperson.

Load and follow the <Sales hire readiness> skill.

Context for this run:
- Company: [name]
- CRM workspace: [link or ID]
- Founder: [name]
```

```
A sales hire readiness card dated [date] returned Not yet on [gate].
The re-run date is today.

Load and follow the <Sales hire readiness> skill, starting at [gate].
```

- [ ] `{{CRM}}` returns deal owner, first meeting date, close date and source on every deal. If first meetings are not logged, start logging them now. The repeatability and pipeline gates depend on them.
- [ ] `{{BILLING}}` or `{{PRODUCT_ANALYTICS}}` can show retention by cohort.
- [ ] `{{REVIEW_CHANNEL}}` exists and `{{FOUNDER}}` reads it.

## 2. Placeholders

- [ ] `{{CRM}}`, `{{BILLING}}`, `{{PRODUCT_ANALYTICS}}`, `{{DOCS}}`, `{{REVIEW_CHANNEL}}`, `{{FOUNDER}}`, `{{CURRENCY}}` all filled, or the optional ones deleted.
- [ ] If the company is outside the US, add a local pay table to `references/evidence-and-benchmarks.md` with source and year, and use it before the US table.

## 3. Policy decisions

- [ ] **Start in trial mode** for the first run.
- [ ] **Value event.** Agree with product which event defines retention before the first run.
- [ ] **Repeatability floor.** Default 10 founder-closed deals. Raise it for long, complex enterprise cycles. Lower it only with a written reason.
- [ ] **Runway buffer.** Default six months left after ramp plus evaluation, at full guaranteed commission.
- [ ] **Load factor.** The multiplier on pay for employer costs, tools and recruiting.
- [ ] **Coaching floor.** Default four hours a week per new rep through ramp.
- [ ] **Benchmark refresh.** Put a yearly date in the calendar to update the evidence file.

## 4. Behaviour that must never be removed

- Retention and repeatability are checked before any hire verdict.
- Two hires, never one, for a first-seller verdict.
- A VP of Sales is never a first-hire verdict.
- Every hire verdict carries the 90-day test and a kill or keep date.
- Pipeline need is computed from the founder's own numbers.
- Every number names its source. Missing data is named, never estimated.
- The unsupported statistics in the evidence file are never used.
- No role is opened, no job posted and no candidate contacted without a human Yes.
- Every write is read back, and failures are reported on the card.
