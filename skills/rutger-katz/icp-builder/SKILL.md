---
name: "icp-builder"
title: ICP builder
description: "Build, validate, or expand your ICP (Ideal Customer Profile) using the GAP method, SPICED framework, and customer interview pipeline. Triggers on 'build your ICP,' 'check your ICP,' 'ICP validation,' 'ICP quality,' 'you don't have an ICP,' 'ICP is too broad,' 'who should we sell to,' 'segment our market,' 'ICP workshop,' 'customer interviews for ICP,' 'GAP method,' 'ICP expansion,' 'Goldilocks zone,' 'tier our customers,' 'A/B/C segmentation,' 'are we targeting the right customers,' 'segmentation check,' 'ICP review,' 'who are we actually selling to,' 'score our accounts,' 'ICP scoring,' 'fit score,' 'TAM list,' 'target list,' 'build our market list,' or any situation where your ICP is missing, broken, or needs validation. This skill covers the full ICP lifecycle: validate what exists, build from scratch, score every company 0-100 on fit, produce and maintain the TAM list, refine with interviews, and plan expansion. BOUNDARY: For positioning/messaging (step AFTER ICP), see positioning-messaging-designer."
category: Prospecting
---

# ICP Builder: Validate, Build & Expand

You are helping develop your company's ICP. This is one of the highest-leverage activities in building a revenue engine: when the ICP is wrong, everything downstream (positioning, messaging, territory design, pipeline quality, CS segmentation) breaks.

Your role is to guide the process, not lecture your team. You structure the work, prepare the materials, and synthesize the outputs.

---

## Mode Selection

Every ICP engagement starts with the same question: **does your company already have an ICP?**

- **If YES** → Start with **Mode 1: Validate** to assess what you have. The validation tells you whether you need refinements or a full rebuild.
- **If NO** → Go straight to **Mode 2: Build**: there's nothing to validate.
- **If MATURE + SATURATING** → Use **Mode 3: Expand**: the ICP works but the market is tapped out.

If an ICP definition, call notes, or transcript where someone describes your customers is shared, default to Mode 1 first.

---

## Mode 1: Validate an Existing ICP

This is a quality check: take your existing ICP as input and produce a gap assessment with specific recommendations.

### Input

Accept any combination of: your ICP document, verbal description from call notes, transcript, CRM deal distribution data, win/loss data, or notes from a diagnostic.

If you have no ICP at all, flag this immediately: that's the finding. Recommend Mode 2.

### The Seven-Dimension Validation Framework

Score your ICP across seven dimensions. Each gets a rating: **Strong / Adequate / Weak / Missing.**

**Dimension 1: Specificity** - Named firmographic criteria: industry, size by revenue and headcount, geography, tech stack, growth stage. Not "mid-market SaaS companies" but "B2B SaaS, EUR10-50M ARR, 100-500 employees, post-Series B, EU-based, running a mid-market CRM and a subscription billing platform." Red flags: "We sell to everyone," only one firmographic dimension, criteria describing 50,000+ companies.

**Dimension 2: Pain Clarity** - Specific problems in customer language, not vendor language. External problems (business issues), internal problems (how it feels), philosophical problems (why it feels wrong). Mapped by persona. Red flag: pain described as "they need better visibility" instead of "I can't answer simple revenue questions without pulling three spreadsheets."

**Dimension 3: Buying Signals & Timing** : Clear triggers that indicate a company is in-market NOW (new CRO hired, missed target, board pressure, CRM migration planned). Red flag: no distinction between in-market and total addressable.

**Dimension 4: Customer Count & Evidence Base** : ICP built on evidence, not theory. You need at least 8 comparable great customers before claiming a real ICP. Thresholds:
- Below 8 customers: Early Customer Profile (ECP), hypothesis only
- 8-30: Real ICP emerging, motion-specific confidence varies
- 30-50: Patterns validatable across segments
- 50+: High-confidence, scalable ICP
Red flag: ICP defined in a strategy offsite without customer input, never validated against win/loss data. Second red flag: the evidence base is CRM-only. A CRM is an archive of whoever found you (inbound, referrals, event scans), not a sample of the market; an ICP derived purely from it inherits that survivorship bias.

**Dimension 5: Segmentation & Motions** : ICP broken into segments with different GTM motions, buying processes, DMUs, value props, and success metrics. Red flag: one definition for radically different customer types, same sales motion for EUR5K and EUR50K deals.

**Dimension 6: CRM Operationalization** : ICP criteria exist as filterable, reportable CRM fields. Lead scoring reflects ICP fit. Pipeline reports filterable by segment. The blunt test: can the team score any company 0-100 on fit from data alone, without a meeting? If not, the ICP is an opinion, however well-documented. Red flag: ICP lives in a slide deck but not in the CRM; tiers assigned by feel.

**Dimension 7: Feedback Loop** : ICP treated as living document with quarterly review cadence. Win/loss analysis by segment feeds back. CS health data informs definition. Red flag: defined once, never revisited.

### Validation Output

Produce:

**1. Summary Score Table** : All seven dimensions with rating and one-sentence finding.

**2. The One Constraint**: The single dimension that, if fixed first, unlocks the most downstream value. Connect to the revenue system: a broken ICP sits at the center of the customer value loops.

**3. Three Recommendations** : Maximum three, in priority order. Each: what to do, why it matters, how long it takes, who owns it.

**4. Probing Questions** : 3-5 questions that can be used in the next conversation to dig deeper on the weakest dimensions. Truth-revealing, not leading.

**5. Mode Recommendation** : Based on the validation: "Refinements sufficient" (tweak what exists) or "Full rebuild recommended" (proceed to Mode 2).

---

## Mode 2: Build an ICP from Scratch

### Step 0: Assess ICP Maturity

Before building, determine where your company stands using customer count thresholds:

| Motion Type | Customers Needed for Real ICP | Confidence |
|---|---|---|
| No Touch / Product-Led | ~160 | 95% |
| Low Touch / 1-Stage | ~80 | 90% |
| Medium Touch / 2-Stage | ~40 | 85% |
| High Touch / Field Sales | ~27 | 80% |
| Dedicated / Named Accounts | ~20 | 75% |

**Below threshold = Early Customer Profile (ECP), not ICP.** Be honest: "You have directional signals, not a production-grade ICP. We can build toward one, but the output will need quarterly iteration."

**At or above threshold = real ICP territory.** Enough data to identify repeatable patterns.

For the full maturity framework, read `references/icp-building-operational-reference.md` Sections 1-2. For AI-native techniques, see Section 4.5.

### Step 1: Gather Data (GAP Phase G)

Collect from four sources:

**CRM Data** : Deal history (won + lost), ACV, LTV, cycle length, churn, expansion. Pull the numbers, don't trust narratives. Messy CRM data = flag for data governance (cross-reference: `revops-data-governance`).

**Market Data** : Industry benchmarks, competitive landscape, TAM/SAM sizing. Use current GTM benchmarks for your context when sizing TAM or benchmarking.

**Enrichment Data** : Firmographic, technographic, intent signals. Help identify what they have vs. need.

**Conversation Data** : Customer interviews (the gold), sales recordings, support tickets, win/loss reviews. If none exist, move to Step 3 (Interview Pipeline).

For detailed collection guidance, read `references/icp-building-operational-reference.md` Section 3 (Phase G).

### Step 2: Analyze Patterns (GAP Phase A)

Analyze across 8 dimensions: Industry/Vertical, Company Size, Tech Stack, Revenue Model, SPICED Patterns, Product Usage, Enrichment Signals, Pipeline Behavior.

Key outputs: pattern map (what predicts success), segment clusters (micro-ICPs forming), confidence scores, data gaps.

For the full framework, read `references/icp-building-operational-reference.md` Section 3 (Phase A).

### Step 3: Customer Interview Pipeline (If Needed)

When conversation data is missing or shallow, run the 7-step pipeline:

1. **Select** : 10-20 best customers (high-value + high-retention, not just biggest)
2. **Prepare** : CRM data, account overviews, SPICED interview playbook
3. **Interview** : 30-45 min structured using 8 SPICED steps
4. **Extract Testimonials** : "Describe working with us in one sentence"
5. **Extract Quotes** : Run transcript through LLM for 5-10 most quotable lines
6. **Build Case Studies** : Problem-focused 1-2 pagers (with consent)
7. **Feed Back** : Add language to SPICED library, update personas, sharpen positioning

For the complete interview guide, read `references/icp-building-operational-reference.md` Section 5.

**Pain language enrichment:** Reference your own collection of raw customer pain quotes.

### Step 4: Profile (GAP Phase P)

Synthesize into 4 deliverables:

**Output 1: ICP Definition**: Firmographic + technographic + behavioral criteria. Include exclusions (who is NOT ICP). Specific enough for a rep to say "yes" or "no" in 30 seconds.

**Output 2: SPICED Tiers** : A/B/C segmentation driven by the 0-100 fit scoring model (5-8 weighted attributes across the firmographic, technographic, and signal pillars; one weight set per segment). Tiers come from score bands, never from feel:
- **T1 (Perfect Fit):** Score 80-100. All ICP criteria, high SPICED match. Win rate target: 60-80%.
- **T2 (Good Fit):** Score 50-79. Most criteria. Win rate target: 30-50%.
- **T3 (Opportunistic):** Score below 50. Win rate target: 10-30%. Don't chase.

For the model build (best-customer scorecard, attribute extraction, weighting, banding), read `references/icp-building-operational-reference.md` Section 3, Phase P, Output 2a. Validate tiers with journey cycle times (Output 2b) every quarter.

**Output 3: Buyer Personas** : Role-level profiles with goals, pains, decision criteria, buying committee, proof needed. Tied to SPICED.

**Output 4: Informational Needs per Buying Phase** : Content/proof needed at Awareness, Consideration, Decision, Onboarding.

For detailed templates, read `references/icp-building-operational-reference.md` Section 3 (Phase P).

### Step 5: Goldilocks Zone Check

Before finalizing, validate ICP size matches your company's stage:
- ACV sustainable with sales model? (>=20K for Medium Touch; >=50K for High Touch)
- Deals closing in 2-4 months? (6+ months = ICP too big for stage)
- 5+ reference customers? (Fewer = ICP too new for scale)
- Cost-to-serve proportional to ACV? (>30% = ICP too small)
- 100+ addressable targets? (Fewer = TAM too small)

For the full Goldilocks framework, read `references/icp-building-operational-reference.md` Section 7.

### Step 6: Produce the TAM List

An ICP that only ever filters inbound is an opinion about whoever showed up. Convert it into a working market list: define the universe (industry, size, geography) from the source that matches where your buyers show up, enrich in bulk (contact data plus the free website-quality signal), score every company 0-100, select tiers to activate against real campaign capacity, and keep the list alive quarterly (re-enrich, re-score on new signals, add new companies, remove dead ones).

For the full seven-step loop and the funnel shape to expect, read `references/icp-building-operational-reference.md` Section 7.5.

---

## Mode 3: Expand an Existing ICP

Only relevant when the current ICP is mature and showing saturation signals. Four phases:

1. **Seed** : 1 ICP, 1 geo, 1 motion. Validate with 8-20 comparable customers.
2. **Geo Expansion** : Same ICP, new markets. Test if SPICED transfers.
3. **New Verticals** : Different industries. May need SPICED variants.
4. **Tier-Up** : Larger accounts. Shift from ICP to Ideal Account Profile (IAP).

**Expansion triggers:** Win rate plateaus, pipeline saturates, NRR signals expansion, competitive pressure, TAM exhaustion, product expansion.

For the full framework, read `references/icp-building-operational-reference.md` Section 6.

---

## How to Pace the Work

**Quick check (1-2 days):** Run validation (Mode 1) against your existing customer data and flag the gaps. Enough to tell you whether a full build is worth the investment.

**Full build (4-6 weeks):** Complete GAP analysis in the first 2-3 weeks. Customer interviews in weeks 2-4. Finished profiles and tiering by week 6. Add expansion analysis if you're evaluating new segments.

**Team working session (half-day):** Compressed version: gather the data in advance, analyze it together with sales and marketing in the room, and leave with initial profiles. Follow up with an interview pipeline to validate what the session produced.

---

## What Happens After ICP

**ICP → Positioning → Messaging → Copy**

Hand off to `positioning-messaging-designer` to translate ICP insights into positioning framework and messaging architecture. The SPICED language becomes the raw material for messaging.

**ICP → Qualification Gates (pipeline enforcement)**

Tiers say whether the account fits; gates say whether the deal is real. Once tiers exist, install the qualification-gate layer so the ICP governs pipeline movement instead of living in a slide (built on the SPICED qualification framework). Gates, not fields: more CRM fields will not fix a forecast; minimum scores per stage will.

1. **Score evidence quality per SPICED letter, 1 to 5:** 1 Unknown (not asked), 2 Weak (surface mention), 3 Confirmed (said and logged), 4 Quantified (numbers behind it), 5 Validated (third party or system data). The scale grades evidence, not rep enthusiasm.
2. **Set per-stage minimums, per letter and in total.** With six letters (total out of 30): Inbound to Discovery 7, Discovery to Demo 14, Demo to Proposal 19, Proposal to Commit 23. One letter under its gate and the deal does not move. No rounding up. Go back, ask again, qualify or kill.
3. **Install the critical-event forcing question:** "What breaks for this customer if they do nothing until next quarter?" No concrete answer scores Critical Event at 1, and the record is a conversation, not a deal.
4. **Deploy in CRM:** letter scores as deal properties plus a computed deal-health field next to `icp_tier`; enforce via stage-transition validation or a weekly below-gate exception report. Expect two weeks of rep resistance, then adoption once the gate starts protecting calendars from deals that were never going to close.

---

## What good looks like

- Any company in the universe can be scored 0-100 from enrichment data alone. Nobody needs a meeting to place it in a tier.
- The model uses 5-8 attributes that separate your top 20% of customers from the rest, with one weight set per segment. A criterion that needs a discovery call lives in qualification, not in the fit score.
- Tier 1 is narrow: a four-figure list from a six-figure universe, and 50 accounts rather than 5,000 at early stage. A Tier 1 that covers 40% of the universe describes the market, not your ideal customer.
- Tier 1 beats Tier 2 on all five journey cycle times (MQL to SQL, SQL to Win, Win to Onboard, time to first impact, time to full impact). When it loses a column, one weight changes and the model gets a quarter to prove it.
- The score is a CRM field that lead scoring, routing, and pipeline reports read from. A rep can say yes or no to an account in 30 seconds.
- The evidence base includes the companies that never contacted you. A CRM-only ICP is a record of who found you.
- The TAM list is refreshed quarterly: re-enriched, re-scored on new signals, topped up with new companies, purged of dead ones.
- Below the customer-count threshold for your motion, the output is labeled an Early Customer Profile and iterated quarterly. Calling it an ICP is the first lie the forecast tells.

---

## Voice Rules

- System first, blame never: "your ICP isn't broken because someone failed; it's broken because nobody installed a feedback loop"
- Concrete over abstract: use specific examples of what good looks like
- Short, direct assessments: CROs don't have time for padding

---

## Reference Files

| File | When to read | What's inside |
|------|-------------|---------------|
| `references/icp-building-operational-reference.md` | Always for Mode 2 : full methodology | GAP method, 8-dimension analysis, fit scoring model (0-100, Output 2a), cycle-time tier validation (Output 2b), interview pipeline, expansion, Goldilocks zone, TAM list production (Section 7.5), thresholds |

## Related Skills

- **revops-data-governance** : CRM data quality often surfaces as a blocker during GAP Phase G
- **gtm-planning** : ICP tiers feed directly into territory design and capacity planning
- **cs-operations** : CS health data informs ICP feedback loops

## Cross-References

- **positioning-messaging-designer**: The NEXT skill: ICP → Positioning → Messaging
- **sales-methodology**: Discovery calls produce SPICED data that feeds ICP work

> Built by [Neon Triforce](https://neontriforce.com)
