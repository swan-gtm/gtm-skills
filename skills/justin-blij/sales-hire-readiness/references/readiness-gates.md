---
title: Readiness gates
description: For each of the six gates, what to pull from the systems, how to measure it, the pass bar, and the fix that goes on the card when it fails.
---

# Readiness gates

Run the gates in order and stop at the first hard fail. A later gate measured on top of a failed earlier one gives a false sense of progress. Every pass bar below is a default. Thresholds marked "practice default" come from operator experience, not a study. Change them in setup if your evidence says otherwise, and write down why.

## Gate 1. Retention (hard)

**Why it comes first.** Bookings without retention are an infomercial. Adding a rep to a product customers quietly leave buys churn faster.

**Pull.** From `{{PRODUCT_ANALYTICS}}`: the event that best predicts renewal (first report shared, first workflow automated, third active seat). From `{{BILLING}}`: logo and revenue retention by monthly or quarterly cohort.

**Measure.** State it as P% of customers reach value event E within T days, for the last two or three cohorts. If no value event is tracked, fall back to logo retention at the first renewal point.

**Pass.** The founder can name the value event, and the share reaching it is flat or rising across the last cohorts. Practice default for a first hire: at least half of new customers reach it within the window the founder sets, and no cohort shows retention falling for two periods in a row.

**Fail, and the fix on the card.** "Not yet. Define the value event, track it for two cohorts, and re-run on [date]." If retention is falling while bookings rise, the card says so in those words.

## Gate 2. Founder repeatability (hard)

**Why.** A motion is repeatable when the founder can predict it. A rep inherits the founder's numbers only if there are numbers to inherit.

**Pull.** From `{{CRM}}`: every closed-won and closed-lost deal with the owner, created date, first meeting date and close date.

**Measure.**

- Founder-closed deals, and deals closed by anyone else.
- First-meeting-to-close rate by month or quarter. Use first meeting as the denominator, not lead, so inbound noise does not distort it.
- Median sales cycle, and the spread between the fastest and slowest quartile.

**Pass.** 10 to 30 founder-closed deals (Lemkin's floor of 10 to 20, Kazanjy's 10 to 30). A first-meeting-to-close rate in roughly the 15% to 25% range that holds within a few points period to period. A cycle the founder can predict within a month.

**Fail, and the fix.** Under 10 deals: "Not yet. Close [10 minus n] more yourself and re-run." A volatile close rate: "Not yet. The rate swings from x% to y%. Find what the wins share, write it down, and re-run when two periods agree."

## Gate 3. Written motion (hard)

**Why.** A new rep cannot inherit what lives in the founder's head. Kazanjy's test: before blaming a rep, check for a deck, a discovery question list and a demo script. Without them, nobody succeeds.

**Pull.** From `{{DOCS}}`, look for each item:

| Item | Bar |
|---|---|
| ICP | One paragraph a stranger could use to disqualify a prospect |
| Discovery questions | Written, in order, with what a good answer sounds like |
| Deck | The one the founder actually uses |
| Demo script | The path through the product, and the moment buyers lean in |
| Objections | The top five with the answers that work |
| Loss reasons | Why the last ten losses were lost, in the buyer's words |

**Pass.** All six present and current.

**Fail, and the fix.** List the missing items. Writing them is usually a week of founder time, so the re-run date is close. A first hire hired to "write the playbook" is a discovery hire, and the card says so.

## Gate 4. Pipeline supply (routes the verdict)

**Why.** A rep with no first meetings is a researcher on a quota. Lemkin's rough line: below about $1M ARR, most startups lack the 50 or so qualified leads a month one rep needs.

**Pull.** From `{{CRM}}`: first meetings per month for the last six months, by source (inbound, founder network, outbound, partners).

**Measure, from the founder's own numbers, not a benchmark.**

```
deals each rep must close a year  = annual quota / average deal value
first meetings each rep needs     = deals a year / first-meeting-to-close rate / 12
needed for two reps (ramped)      = 2 x first meetings each rep needs
```

Example: quota $760k, average deal $38k, close rate 21%. 20 deals a year, about 95 first meetings a year, about 8 a month per rep, 16 for two.

**Pass.** Current monthly first meetings, minus the ones the founder keeps, cover two ramped reps, or a dated plan shows supply reaching that level by the end of ramp.

**Fail.** Routes to **Build pipeline first**, not to Not yet. The founder can close. The constraint is supply, and the card shows the gap in first meetings a month.

## Gate 5. Runway (hard)

**Why.** The first sales hire costs a year of runway, not a salary. Ramp averages about six months before any evaluation is fair.

**Pull.** From `{{FOUNDER}}`: cash, monthly burn, and the pay they expect to offer. If there is no pay number, use the US medians for the segment in `references/evidence-and-benchmarks.md`, or local data outside the US, and say so on the card.

**Measure.**

```
window            = ramp (default 6 months) + evaluation (default 3 months)
floor cost        = 2 x base x window in years x load factor
ceiling cost      = 2 x OTE x window in years x load factor   (commission guaranteed through ramp)
new monthly burn  = current burn + ceiling cost / window in months
months left after = cash / new monthly burn - window in months
```

The load factor covers employer costs, tools and recruiting. Ask the founder for theirs. Never assume one silently.

**Pass.** Practice default: at least six months of runway left after the window closes, at the ceiling cost. A company that runs out of money the month it learns the answer has not learned anything it can use.

**Fail, and the fix.** "Not yet. Two hires through evaluation cost [x]. You would have [n] months left. Raise, cut burn, or re-run when [condition]." Never "hire one instead". One hire costs less but tells you less.

## Gate 6. Founder capacity (soft)

**Why.** Every operator source assumes the founder keeps selling and coaches through ramp. Without that, the new rep inherits a motion with nobody to teach it.

**Pull.** From `{{FOUNDER}}`: hours a week they will give for six months to ride-alongs, deal reviews and call reviews, and whether they will keep their own deals.

**Measure.** Practice default: four hours a week per new rep through ramp.

**Low capacity.** Does not change the verdict, but sets founder capacity risk to high, and the card says: "At [n] hours a week, expect the hire to fail on handover, not on talent."

## Re-runs

On a Not yet, re-run only the failed gate and the gates after it. Earlier passes stand unless the data behind them has changed by more than a period.
