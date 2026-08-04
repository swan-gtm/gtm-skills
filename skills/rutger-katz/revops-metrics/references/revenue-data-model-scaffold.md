# Revenue Data Model Reference

*Supporting reference for revops-metrics, revenue-operating-cadence, expansion-revenue-architect, cs-operations, and revops-handoffs skills.*

---

## Understanding Your Measurement Architecture

When you build a revenue operations dashboard, you're trying to answer four connected questions:

1. **Are enough prospects entering the system?** (volume)
2. **Are they moving through the stages at expected rates?** (conversion)
3. **How fast are they moving?** (velocity)
4. **How do different customer segments or go-to-market motions compare?** (segmentation)

The framework below helps you structure these answers for three distinct go-to-market patterns: inside sales (rapid iteration, high volume), enterprise sales (long cycles, multi-stakeholder), and product-led growth (self-serve acquisition).

---

## Volume, Conversion, and Velocity Framework

Every stage of your revenue funnel can be measured across three dimensions: the count of things in that stage (volume), what percentage advance to the next stage (conversion), and how many days they spend there (velocity).

### Inside Sales Architecture

Inside sales models work when your sales cycle is short (30-90 days), your deal size is repeatable, and your process is standardized.

| Stage | What to count | Conversion to watch | Velocity to target |
|-------|---|---|---|
| **Awareness** | Visitor count or inbound inquiries | % who become known leads | Days from first touch to inquiry |
| **Education** | Marketing-qualified leads (MQLs) | % who are sales-accepted | Days from MQL to SAL handoff |
| **Qualification** | Sales-accepted leads (SALs) or SQLs | % who become opportunities | Days to opportunity creation |
| **Pitch** | Opportunities in pipeline | % who advance to proposal/demo | Days from opp creation to first demo |
| **Decision** | Proposals or active negotiations | % who close won | Days in active negotiation |
| **Adoption** | New customers | % who reach activation milestone | Days from contract to first value |
| **Retention** | Active customers | % who retain past initial period | Days to first expansion signal |
| **Growth** | Customers eligible for expansion | % who buy more | Days from signal to expansion close |

Not every company measures all eight stages. A minimum viable measurement set for inside sales: leads → sales-accepted → opportunities → closed won → retained → expanded.

### Enterprise Sales Architecture

Enterprise sales requires different measurement logic. Deals move slower, involve many stakeholders, and often follow different qualification criteria.

| Stage | What to measure | Conversion point | Velocity pattern |
|-------|---|---|---|
| **Account awareness** | Accounts touched or with intent signal | % who become marketing-qualified accounts | Days from outreach to first engagement |
| **Engagement** | Qualified accounts in nurture | % who book discovery meeting | Days from qualification to first meeting |
| **Qualification** | Active opportunities | % who complete full qualification | Days to qualification completion |
| **Proposal** | Qualified opportunities | % who move to closed won | Days from qualification to contract |
| **Onboarding + expansion** | Same as inside sales above | Same conversion logic | Same velocity framework |

The key difference: enterprise measurement starts with accounts, not individuals. Multiple people within the same account may progress at different rates, and the buying committee itself is a metric.

### Product-Led Growth Architecture

PLG companies measure from first free usage through to paid conversion and then into expansion.

| Stage | What to count | Conversion logic | Velocity to track |
|-------|---|---|---|
| **Awareness** | Free trial sign-ups or freemium registrations | % who become active trial users | Days from sign-up to first real usage |
| **Education** | Active product users | % who trigger hand-raise signal (request demo, upgrade) | Days from first login to hand-raise |
| **Sales** | Product-qualified leads (PQLs) | % who become sales-accepted or convert directly | Days from PQL signal to sales contact |
| **Monetization** | PQLs engaged by sales | % who convert to paid | Days from sales engagement to first payment |
| **Retention + expansion** | Same as inside sales | Same logic | Same framework |

The shift in PLG is that conversion from trial to paid often happens without sales involvement, but your measurement structure remains the same.

### Mixed Motion Scenarios

Most companies run two or three motions in parallel: inside sales handles SMB, enterprise handles large accounts, and product-led handles self-serve evaluation. When you blend these, your funnel numbers lie. **Always measure inside sales, enterprise, and PLG tracks separately.** A blended funnel masks which track is failing.

Example: Your aggregate MQL→SQL rate appears normal at 18%, but when you split it:
- Inside sales SMB: 28% (strong)
- Enterprise: 12% (broken)
- PLG hand-raises: 22% (ok)

The enterprise motion is your actual problem, not a broad "conversion" issue.

---

## Expansion and Retention Logic

After the initial sale, there are four distinct patterns of how revenue grows from existing customers. Understanding which pattern applies to your business shapes how you measure and run expansion.

### The Four Expansion Types

Think of expansion on two axes: Is the customer buying the same thing or something new? And is the person making the decision the same person or someone new?

**Renewal** happens when the same customer, same use case, and same buyer want to continue. It's the lowest-risk expansion because the relationship and value are proven. Your metric: days between contract end and renewal conversation. Earlier is healthier; it means your customer already knows they want to stay.

**Upsell** happens when the same buyer wants to do more with what they already have: more users, more volume, higher tier, or more features within the same use case. This is high-probability expansion and typically triggered by a usage milestone or expansion signal from the customer success team. Your metric: time from expansion signal to close.

**Cross-sell** is when you introduce a completely different product or use case to a different person within the same account. Because the buyer is new, you essentially restart the qualification process. Treat cross-sell as a new enterprise opportunity, complete with SPICED qualification. Your metric: similar to new opportunity close rate, but watch it separately because the attachment rate is typically lower than your core motion.

**Resell** is the one most teams miss. It happens when the champion who approved the original purchase leaves the company or changes roles, and a new person must re-justify the investment. The product is still working, but the commercial relationship resets. Resell is the highest-risk expansion type because it often silently becomes churn within 90 days of the champion's departure if you don't intervene. Your metric: days from champion departure to re-engagement with the new stakeholder. Target: first introductory meeting within 14 days of departure.

**Why this matters for your measurement:** Conflating these four types produces the wrong action. If your expansion rate is low because you have a resell problem, adding CSM resources for upsell activities doesn't help. You need a champion-departure playbook.

---

## Churn Patterns and Diagnostic Logic

Not all churn is the same, and treating it generically wastes resources.

### Early Churn (0-90 days)

Early churn is a sales problem, not a product problem. The customer bought a promise (often made during sales) that the product hasn't yet delivered. This could be a slow time-to-first-value, unmet expectations from the demo, or a bad handoff from sales to customer success.

**Diagnostic question:** Did the customer reach their activation milestone within 30 days of contract start?
- If no: Early churn risk. The problem is in your sales handoff or onboarding.
- If yes but they still churned: Your sales team promised something the product doesn't deliver.

**Fix:** Repair the sales-to-success handoff. Ensure customer success receives full SPICED qualification context when the customer onboards. Compress your time-to-first-value. Calibrate what sales promises during the demo.

### Late Churn (90+ days)

Late churn is typically a lack-of-impact problem. The customer is not achieving the business outcome they expected, or they're using the product wrong, or the fit was wrong from the start. It usually surfaces at renewal.

**Diagnostic question:** Is the customer actively using the product AND demonstrating measurable business outcomes?
- If no to either: Late churn risk. The problem is adoption or fit.

**Fix:** Tighten your health scoring to catch usage problems early. Run proactive usage reviews with customers. Validate that the customer actually solved the pain they bought you to solve. If customers of a certain segment consistently show late churn, your ICP is wrong.

**Why this distinction matters:** Throwing CSMs at early churn doesn't fix a broken sales handoff. Adding onboarding steps doesn't fix late churn from a poor initial fit. Measure and diagnose separately.

---

## Benchmarking Your Metrics

Once you have your own metrics, the question is: are we good? Benchmarking helps you answer that, but only if you use it correctly.

### The Three Levels of Comparison

**Level 1: Direction Setting (Industry Benchmarks)**

Published benchmarks from large datasets (like OpenView's SaaS Index or Bessemer) tell you if you're in the right ballpark. Use these to spot if you're massively off: a 5% win rate when the benchmark is 25% is a signal something's broken. But never use broad benchmarks to set targets. A PLG company at $5M ARR will look broken against an enterprise benchmark at $100M ARR because the underlying business is completely different.

**Level 2: Peer Comparison (Stage and Motion Matched)**

The most useful benchmark is from companies with the same go-to-market motion, same ARR stage, and same ACV. A $10M ARR inside-sales company has more in common with another $10M ARR inside-sales company than with a $10M ARR enterprise company. This requires normalized data, which is hard to find. Proxy: use investor portfolio benchmarks or look for industry reports broken down by ARR and motion.

**Level 3: Trend Analysis (Your Own Data)**

The most actionable benchmark is your own 12-month trend. Are your conversion rates improving, stable, or degrading? What changed when you made a process change? A metric trending up is more important than a metric that matches a published benchmark. Track your own control charts: plot your metrics over time, mark special causes (a sales team change, a new marketing program, a product release), and watch whether metrics regress or improve. A metric that's stable and predictable tells you the system is working as designed.

### Performance Matrices

Single metrics can be misleading. Combine two metrics into a 2×2 matrix to surface real problems:

**Pipeline coverage vs. Win rate:**
- High coverage + high win rate = doing well, consider investing more in growth
- High coverage + low win rate = problem in deal execution or qualification
- Low coverage + high win rate = demand generation is the constraint
- Low coverage + low win rate = multiple problems, start with demand

**NRR vs. GRR:**
- High NRR + low GRR = expansion hiding churn (fragile growth)
- High NRR + high GRR = the ideal (sticky and growing)
- Low NRR + high GRR = stable but not growing (missed expansion opportunity)
- Low NRR + low GRR = systemic churn problem

**CAC payback vs. NRR:**
- Long payback + high NRR = investment case is sound but cash-intensive
- Short payback + low NRR = efficient at acquisition but retention leak destroys lifetime value

These 2×2s force you to think about two forces at once and prevent optimizing one metric at the expense of another.

---

## Practical Architecture Example

If you're building a dashboard for a $15M ARR inside-sales SaaS company with SMB and mid-market segments, here's how to structure it:

**By motion:** Separate inside-sales pipeline from any inbound/PLG volume.

**By segment:** Run parallel conversion and velocity tracks for SMB and mid-market. They have different benchmarks, different buying committees (even if smaller), and different cycle times.

**By source:** Track inbound-sourced opportunities separately from outbound. They typically have different win rates and cycle times, and conflating them masks whether one channel is degrading.

**Core tiles:**
- Volume (opportunities created this period vs. target and trend)
- Conversion (stage-to-stage rate for each segment, vs. benchmark and trend)
- Velocity (average days in each stage, vs. target and trend)
- Unit economics (CAC, payback, LTV:CAC, ARR per AE)
- Retention (GRR, NRR, churn rate, cohort curves)

**Expansion view:**
- Renewal rate by cohort
- Expansion rate (upsell + cross-sell) by segment
- Resell pipeline (customers with recent champion departure)
- Expansion ARR as % of new business ARR

This structure keeps signal separate from noise and makes it obvious which lever to pull.

---

For stage-specific targets and AI impact metrics, see the peer-reviewed benchmarks in the sibling file `benchmarks.md`.
