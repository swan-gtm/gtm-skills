---
name: sales-hire-readiness
title: Sales hire readiness
description: |
  Use this skill when a founder, CEO or first revenue leader is deciding whether to make their first sales hires, and who to hire. Tests "we need a salesperson" against evidence from the CRM, billing and sales materials: retention, founder repeatability, a written motion, pipeline supply, runway through ramp, and founder coaching time. Returns one of four verdicts (Not yet, Hire two pioneers, Hire a player-coach, Build pipeline first) with the numbers behind it, the exact profile to hire, and a 90-day leading-indicator test that shows by month three whether the hire is working. Rules out a VP of Sales as a first hire and explains why. Ends with one Yes/No decision for a human. Triggers on "should we hire a salesperson", "first sales hire", "hire a VP of Sales", "are we ready to hire sales", "I need someone to take sales off my plate", "founder-led sales", "when do we hire AEs", "who should our first rep be", "can we afford a sales hire".
category: Hiring
tags: [Sales, Leadership]
---

# Sales hire readiness

Runs when a founder says "I need to hire a salesperson." Produces a readiness card and a Yes/No decision, never a job post or a candidate contact.

**The prime rule: hire to scale a motion, never to find one.** A salesperson can run a motion the founder has proven. They cannot discover one on a quota. Fewer than half of quota-carrying reps hit their number in a normal year, so one new rep missing tells you almost nothing about whether the rep or the motion failed. If the motion is not proven, the answer is "Not yet", with the one gap to close and a date to re-run.

## Template placeholders

Replace every `{{...}}` before enabling. The setup checklist in `references/setup-customization-checklist.md` covers each one.

- `{{CRM}}`: deals, owners, stage dates and deal sources
- `{{BILLING}}`: customers, contract values and churn
- `{{PRODUCT_ANALYTICS}}`: the value event each customer reaches, if tracked
- `{{DOCS}}`: where the sales materials live
- `{{REVIEW_CHANNEL}}`: where the card is posted
- `{{FOUNDER}}`: who owns the decision
- `{{CURRENCY}}`: currency for pay, deal values and cash

## Trial mode (recommended for the first run)

Run the gates and post the card to `{{REVIEW_CHANNEL}}` marked TRIAL. Do not treat the verdict as a decision until `{{FOUNDER}}` has checked every number against what they know. A founder who disagrees with a gate usually has data the systems do not hold. Add it and re-run.

## Diagnostic questions (before the first run)

1. How many deals have you closed yourself, and how many did anyone else close?
2. What does a customer do in the product that tells you they will renew?
3. If a new rep started Monday, what would you hand them on day one?
4. Where will next quarter's first meetings come from, by source?
5. How many hours a week will you give a new rep for the first six months?

## Step 1. Pull the evidence

Search before asking. Read `references/readiness-gates.md` for exactly what to pull and how to measure each item.

- From `{{CRM}}`: closed-won and closed-lost deals, the owner on each, stage dates, first meetings per month, and the source of each deal.
- From `{{BILLING}}` or `{{PRODUCT_ANALYTICS}}`: retention by customer cohort, and the share of customers reaching the value event.
- From `{{DOCS}}`: the sales materials, checked against the written-motion list.
- From `{{FOUNDER}}`, only what the systems cannot answer: cash, monthly burn, the pay they expect to offer, and coaching hours.

Every number on the card names its source. Missing data is named, never estimated.

## Step 2. Run the gates in order

Stop at the first hard fail. Thresholds and the fix for each failure are in `references/readiness-gates.md`.

1. **Retention (hard).** P% of customers reach the value event E within T days. Bookings without retention are an infomercial, not product-market fit.
2. **Founder repeatability (hard).** 10 to 30 founder-closed deals, a first-meeting-to-close rate that holds month to month, and a cycle length the founder can predict.
3. **Written motion (hard).** ICP, discovery questions, deck, demo script, top objections with answers, and why deals were lost. If it is not written, it cannot be handed over.
4. **Pipeline supply (routes the verdict).** Enough first meetings, by source, to feed two reps once ramped.
5. **Runway (hard).** Two hires through ramp plus an evaluation window, against cash, using `references/evidence-and-benchmarks.md` for pay when the founder has no number.
6. **Founder capacity (soft).** Weekly coaching time through ramp. Low capacity does not block a verdict, but the card says the hire will likely fail and why.

## Step 3. Pick the verdict and the profile

Read `references/profile-picker.md`. Four verdicts only:

| Verdict | When |
|---|---|
| **Not yet** | Retention, repeatability, written motion or runway fails |
| **Hire two pioneers** | All hard gates pass, pipeline is enough, the founder is still the best seller |
| **Hire a player-coach** | Two sellers already perform near founder win rates |
| **Build pipeline first** | The founder closes well, but there are not enough first meetings to feed a rep |

A VP of Sales is never a first-hire verdict. The card says why, with the tenure and cost evidence.

## Step 4. Attach the 90-day test

Every hire verdict carries the month-by-month leading indicators from `references/ninety-day-test.md`, set from the founder's own funnel, with a kill or keep date. Founders lose a year waiting for bookings that ramp makes impossible before month six.

## Step 5. Post the card and stop

```
[Company] / Sales hire readiness / [date]
Verdict: [Not yet / Hire two pioneers / Hire a player-coach / Build pipeline first]
Retention: [P% reach E within T days, cohort, source] | Pass/Fail
Repeatability: [n founder-closed] | first meeting to close [x%] over [months] | cycle [days] | Pass/Fail
Written motion: [present] | Missing: [items] | Pass/Fail
Pipeline: [first meetings a month by source] vs [needed for two reps] | Enough? Yes/No
Runway: two hires through ramp + evaluation = [cost] | months left after = [n] | Pass/Fail
Founder capacity: [hours a week] | Risk: [low/high]
Profile: [one line: price point sold at, stage worked at, self-sourced share]
90-day test: M1 [ ] | M2 [ ] | M3 [ ] | Kill/keep by [date]
Why not a VP of Sales: [one line, with the numbers]
Decision: Open the role(s) as written? Yes / No
          Or fix [top gap] and re-run on [date]? Yes / No
```

After a human answers, log the card and the decision in `{{CRM}}` or `{{DOCS}}`, read the write back, and post a visible warning if it failed. Write failures never block the card.

## Handoffs

The skill works on its own. When other parts of the hiring process exist, it feeds them:

- **After a hire verdict:** carry the profile line and the 90-day test into the interview scorecard. The profile tells interviewers what motion to test for.
- **After a Not yet:** schedule the re-run on the date on the card, and re-run only the failed gate and everything after it.

## What good looks like

- The verdict is one of four, with a number behind every gate. "We feel ready" is not a gate.
- A founder who wanted a VP of Sales leaves with a reason they can repeat to their board: one hire of that size costs about the same as two pioneers through ramp, and gives one reading instead of two.
- A Not yet names one gap, how to measure it, and a date. It is a plan, not a no.
- The pipeline number is computed from the founder's own deal size and close rate, not a benchmark.
- The 90-day test is agreed before anyone is hired, so the kill or keep conversation is about numbers both sides signed.
- The best operators look at retention before bookings. Strong sales numbers with weak retention is the most expensive time to add a rep.

## Anti-patterns

- **The VP of Sales as hire one.** A leader hired to build a team with no motion to scale spends their tenure doing the founder's job.
- **One rep as the experiment.** When most reps miss quota anyway, a single miss is noise.
- **The quota from a spreadsheet.** A quota the founder's own history cannot reach is fiction on day one.
- **Hiring to escape selling.** The founder's learning in deals is the asset. A hire buys back time on execution, never on discovery.
- **Judging at month nine on bookings.** By then the runway is spent. Judge leading indicators at month three.

## Rules

- MUST pass retention and repeatability before any hire verdict.
- MUST recommend two hires, never one, for any first-seller verdict.
- MUST attach the 90-day test to every hire verdict.
- MUST name the source of every number. Missing data is named, never estimated.
- MUST compute pipeline need from the founder's own deal size and close rate.
- NEVER recommend a VP of Sales as a first sales hire.
- NEVER use the unsupported statistics listed in `references/evidence-and-benchmarks.md`.
- NEVER open a role, post a job or contact a candidate. A human decides.
