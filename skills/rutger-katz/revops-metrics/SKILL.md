---
name: "revops-metrics"
title: Revenue performance metrics
description: "Revenue performance measurement, funnel math, and unit economics for B2B teams. Use when the user mentions revenue metrics, conversion rates, pipeline velocity, unit economics, LTV, CAC, payback period, cohort analysis, NRR, GRR, churn rate, expansion revenue, ARR, MRR, funnel conversion, win rate, deal size, sales cycle, Rule of 40, burn multiple, T2D3, growth benchmarks, deal health scoring, deal health dimensions, conversational intelligence metrics, strategic initiative trackers, activity velocity, multi-threading score, or measuring revenue performance. Also trigger on \"our numbers are off,\" \"how do we stack up,\" \"what should our conversion rate be,\" or \"how healthy is this deal.\" BOUNDARY: This skill covers WHAT to measure. For forecasting, see revops-forecasting. For meeting cadence, see revenue-operating-cadence."
category: RevOps
---

# Revenue Performance Metrics

You are a revenue analytics specialist who has built measurement frameworks for B2B companies across stages. You think in systems of connected metrics: every number exists in a chain from activity to revenue, and your job is to find the broken link.

Your philosophy: Metrics are diagnostic tools, not scorecards. The value of a metric is in the question it prompts, not the number it displays. When revenue is off track, the answer is always in the data: but only if you measure the right things at the right granularity.

## The Revenue Math Framework

### Volume Metrics (The Funnel)

Track volume at each stage of the revenue funnel. These are your primary "what happened" metrics.

```
V1:  Website Visitors / Inbound Traffic
V2:  Leads (known contacts with intent signal)
V3:  MQLs (marketing qualified: fit + engagement threshold)
V4:  SALs (sales accepted leads: human quality gate)
V5:  SQLs (sales qualified: confirmed opportunity)
V6:  Opportunities Created (deal in pipeline)
V7:  Proposals / Demos Delivered
V8:  Negotiations (verbal intent, commercial discussion)
V9:  Closed Won (new customer)
V10: Onboarded (activated, using product)
V11: Retained (renewed or active past initial period)
V12: Expanded (upsell, cross-sell, seat expansion)
```

Not every company tracks all 12. The minimum viable funnel for a B2B company is: Leads → MQLs → SQLs → Opportunities → Closed Won → Retained → Expanded. If you can't measure these seven reliably, fix that before anything else.

### Conversion Metrics (The Diagnostic Layer)

Conversion rates between stages tell you *where* the funnel is breaking.

```
CR1: Lead → MQL rate         (is marketing attracting the right people?)
CR2: MQL → SQL rate          (is the MQL definition aligned with sales needs?)
CR3: SQL → Opportunity rate  (is qualification working?)
CR4: Opportunity → Close rate (is the sales process effective?)
CR5: Close → Onboard rate    (is implementation/onboarding working?)
CR6: Retain → Expand rate    (are customers growing with you?)
```

**Benchmark ranges for B2B SaaS:**
```
Lead → MQL:          20-25% average (Data-Mania, First Page Sage, 2026; depends heavily on lead definition and source)
MQL → SQL:           15-21% average, top performers 39-40% (Artisan Strategies, SaaS Hero, 2026)
SQL → Opportunity:   60-80% (practice-based baseline; external benchmarks limited for this stage)
Opportunity → Win:   15-30% varies by segment: enterprise 15-20%, SMB 25-35% (Pavilion, Ebsta, 2026)
Overall Lead → Win:  1-3% (composite, derived from funnel math not external benchmark)
```

### AI-Native Product Metrics

For companies where AI is the product (not just a tool in the GTM stack), the standard funnel math still applies but needs an additional measurement layer for AI product quality.

**The Four Signal Layers (Poyar, March 2026):**

| Layer | What it measures | Examples | When to use |
|-------|-----------------|----------|-------------|
| 1. Explicit | Direct user feedback | Thumbs up/down, chat feedback, survey scores | Starting point: cheap to implement, correlates with conversion (Gamma) |
| 2. Implicit | Post-output behaviour | Edit intensity, copy rate, send rate of AI drafts, time modifying output | Stronger signal: shows whether outputs are actually useful |
| 3. Adoption | Usage patterns | DAU/MAU (copilot), messages per DAU (agentic), days editing/month | Standard but interpretation shifts: depth > frequency |
| 4. Business impact | Work completed | Resolution rate, automation rate, FTEs augmented, digital capacity, time savings | Ultimate measure: is the AI completing valuable work? |

**Key metric shifts for AI-native companies:**

| Traditional SaaS | AI-Native Evolution |
|-----------------|---------------------|
| Seats / licences sold | Digital capacity / FTEs augmented / work completed |
| DAU/MAU | Messages per DAU + work completed per user |
| NPS / CSAT | AI output quality score + resolution rate per interaction |
| Time-to-value (days/weeks) | Time-to-value (minutes / first session) |
| ARR per customer (stable) | Consumption per customer (expanding dynamically) |

Use these metrics when designing revenue dashboard tiles for AI-native clients. The leading indicator tile may be "AI resolution rate" or "work completed per user" instead of traditional pipeline velocity.

See also: AI-native GTM patterns reference, Section 4.

**The diagnostic power of conversion rates:** When revenue drops, don't just look at the output. Walk the funnel:
```
Revenue is down 20% this quarter. Why?

Step 1: Did we create enough pipeline? → Check opportunity volume
Step 2: If pipeline was sufficient, did we convert? → Check win rate
Step 3: If win rate was normal, did deal sizes hold? → Check avg deal size
Step 4: If everything looks normal, did velocity slow? → Check cycle length

Revenue = Opportunities × Win Rate × Average Deal Size ÷ Sales Cycle Length
```

### The Four Pipeline Velocity Levers

Pipeline velocity (sometimes called sales velocity) is the formula that connects your pipeline to revenue output:

```
Pipeline Velocity = (# Opportunities × Win Rate × Avg Deal Size) ÷ Sales Cycle Length

Example:
  100 opportunities × 25% win rate × €40K avg deal = €1M
  If sales cycle is 90 days: €1M per quarter
  If you reduce cycle to 75 days: €1.2M per quarter (20% improvement)
```

**Each lever is an optimization opportunity:**

```
LEVER 1: Opportunities (volume)
  Diagnostic: Are we generating enough qualified pipeline?
  Improve via: Inbound marketing, outbound prospecting, partnerships, PLG
  Typical action: Marketing programs, SDR hiring, channel development
  Warning: Increasing volume without quality wastes sales capacity

LEVER 2: Win Rate (conversion)
  Diagnostic: Are we closing deals at a competitive rate?
  Improve via: Better qualification, sales process, competitive positioning
  Typical action: Methodology training, demo improvement, better multi-threading
  Warning: Win rate improvements compound: 25% → 30% = 20% more revenue

LEVER 3: Average Deal Size (value)
  Diagnostic: Are we selling the full solution or leaving money on the table?
  Improve via: Multi-product selling, packaging optimization, value selling
  Typical action: Bundle offerings, train on value selling, implement pricing tiers
  Warning: Don't inflate ADS by chasing wrong-fit large deals

LEVER 4: Sales Cycle Length (speed)
  Diagnostic: Are deals moving at the expected pace?
  Improve via: Remove friction, improve handoffs, mutual action plans, exec alignment
  Typical action: Standardize process, implement champion programs, accelerate legal
  Warning: Cycle compression that skips stages reduces win rate
```

## Unit Economics

### Customer Acquisition Cost (CAC)

```
CAC = Total Sales & Marketing Spend ÷ New Customers Acquired

Fully-loaded CAC includes:
  - Sales team compensation (base + variable + benefits)
  - Marketing spend (programs, tools, headcount)
  - SDR team cost
  - Sales engineering cost
  - Revenue operations cost (allocated)
  - Sales tools and technology

Segment CAC separately:
  - Inbound CAC vs. Outbound CAC (typically 2-5x difference)
  - SMB CAC vs. Enterprise CAC
  - New business CAC vs. Expansion CAC (expansion should be 20-40% of new biz CAC)
```

### Lifetime Value (LTV)

```
LTV = Average Revenue Per Account × Gross Margin × Average Customer Lifetime

Where:
  Average Customer Lifetime = 1 ÷ Annual Churn Rate

Example:
  ARPA = €30K | Gross Margin = 80% | Annual Churn = 10%
  LTV = €30K × 0.80 × (1 ÷ 0.10) = €240K

With expansion (more realistic for SaaS):
  LTV = ARPA × Gross Margin × (1 ÷ (1 - NRR%))
  If NRR = 115%: LTV = €30K × 0.80 × (1 ÷ (1 - 1.15)) → use NRR-adjusted model

Note: When NRR > 100%, the simple LTV formula breaks (customer lifetime is theoretically
infinite because revenue grows). Use a 5-year discounted cash flow model instead, or cap
the lifetime at a reasonable period (5-7 years for planning purposes).
```

### LTV:CAC Ratio

```
Target: 3:1 minimum (below 3:1, you're buying growth unprofitably)
Sweet spot: 3:1 to 5:1
Above 5:1: You're likely under-investing in growth: spend more to capture market

By segment:
  Enterprise: 5:1+ is common (high LTV, high CAC, but great ratio)
  Mid-Market: 3:1-4:1 (balanced)
  SMB: 2:1-3:1 (lower LTV, needs efficient acquisition)
```

### CAC Payback Period

```
CAC Payback = CAC ÷ (ARPA × Gross Margin)

Example: CAC = €45K, ARPA = €30K, GM = 80%
Payback = €45K ÷ (€30K × 0.80) = 1.875 years = ~22.5 months

Benchmarks:
  <12 months: excellent (most efficient companies)
  12-18 months: strong (healthy SaaS benchmark)
  18-24 months: acceptable (typical for enterprise motion)
  >24 months: concerning (cash-intensive growth, must have strong retention)
```

## Retention and Expansion Metrics

### Net Revenue Retention (NRR)

```
NRR = (Beginning ARR + Expansion - Contraction - Churn) ÷ Beginning ARR

Example:
  Starting ARR: €10M
  Expansion: +€1.5M
  Contraction: -€300K
  Churn: -€700K
  NRR = (€10M + €1.5M - €300K - €700K) ÷ €10M = 105%

Benchmarks:
  <90%:  Critical: the business is shrinking from within
  90-100%: Below par: growth is entirely dependent on new acquisition
  100-110%: Good: existing base is stable to growing
  110-120%: Strong: expansion engine is working
  120%+: Exceptional: each cohort grows significantly over time
```

**Why NRR matters more than growth rate:** A company growing 50% with 80% NRR needs to acquire 70% of its base in new revenue each year just to maintain growth. A company growing 30% with 120% NRR only needs to acquire 10% of its base. The second company is far more efficient and durable.

### Gross Revenue Retention (GRR)

```
GRR = (Beginning ARR - Contraction - Churn) ÷ Beginning ARR

GRR is always ≤ 100% (it excludes expansion). It tells you how much
revenue you keep before any expansion effort.

Benchmarks:
  <80%: Serious retention problem: fix before investing in growth
  80-85%: Below average for SaaS
  85-90%: Average
  90-95%: Strong
  >95%: Exceptional (typically enterprise with multi-year contracts)
```

### Revenue Composition Analysis

Break down where revenue comes from to understand the growth engine:

```
New Business ARR:     Revenue from new logos (new customers)
Expansion ARR:        Revenue from existing customers buying more
Renewal ARR:          Revenue from customers renewing at the same level
Contraction ARR:      Revenue lost from downgrades (negative)
Churned ARR:          Revenue lost from departures (negative)

Healthy composition at maturity (€25M+ ARR):
  New Business:  30-50% of gross new ARR
  Expansion:     30-50% of gross new ARR
  GRR:           >90%

If expansion is <20% of new ARR, you're leaving money on the table.
If new business is >70% of new ARR, you're too acquisition-dependent.
```

**AI-Generated Inbound and Pipeline Pollution (2026 caveat):** 70%+ of intent signals now originate from AI-research traffic (Landbase, Digital Applied, 2026). Traditional pipeline composition benchmarks (30-50% new / 30-50% expansion) predate this shift. When measuring composition, filter AI-generated research signals from genuine buying signals, or adjust thresholds upward for new business. A pipeline that appears 80% new business may actually be 60% new logos plus 20% AI-noise. Segment your composition analysis: (a) AI-research sourced pipeline, (b) human-initiated and referral pipeline. Track them separately until you can reliably distinguish them in your CRM.

## Growth Benchmarks

### The Rule of 40

```
Rule of 40 = Revenue Growth Rate (%) + Profit Margin (%)

Example: 30% growth + 15% profit margin = 45 (above 40 = healthy)
Example: 60% growth + (-15%) margin = 45 (above 40 = healthy, burning for growth)
Example: 10% growth + 10% margin = 20 (below 40 = underperforming)

A company should aim for its growth rate plus profit margin to exceed 40%.
This balances growth investment against profitability.

For early-stage companies (<€25M ARR): growth rate matters more than Rule of 40.
A company growing 100% at -30% margin (Rule of 40 = 70) is doing well.
```

### Burn Multiple

```
Burn Multiple = Net Burn ÷ Net New ARR

This tells you how much you're spending to generate each euro of new ARR.

Benchmarks:
  <1x:   Exceptional efficiency (rare: company is nearly self-funding growth)
  1-1.5x: Strong: sustainable growth investment
  1.5-2x: Average: acceptable at scale-up stage
  2-3x:   Concerning: needs efficiency improvement
  >3x:    Alarming: burning cash without proportionate ARR return
```

### Growth Rate Benchmarks by Stage

```
T2D3 Framework (target growth trajectory):
  Year 1-2 post-PMF:  Triple ARR (3x year-over-year)
  Year 3-4:           Triple again, then double (3x → 2x)
  Year 5+:            Double (2x year-over-year)

More realistic benchmarks by ARR stage:
  €1-5M ARR:     100-200% YoY (fast growth expected, small base)
  €5-15M ARR:    70-120% YoY (growth at scale becomes harder)
  €15-50M ARR:   40-80% YoY (efficiency matters more)
  €50-100M ARR:  30-50% YoY (strong performance)
  €100M+ ARR:    20-40% YoY (compounding at scale is impressive)
```

## Diagnostic Frameworks

### The Revenue Diagnostic Sequence

When revenue is off track, diagnose in this order:

```
1. VOLUME DIAGNOSTIC: Is enough entering the funnel?
   Check: Leads, MQLs, SQLs, Opportunities created vs. target and trend
   If low: It's a demand generation problem. Look at marketing programs,
   SDR productivity, and inbound channel health.

2. CONVERSION DIAGNOSTIC: Is the funnel converting at expected rates?
   Check: Stage-to-stage conversion rates vs. historical and benchmarks
   If low: Identify WHICH stage is breaking. MQL→SQL = scoring/handoff.
   SQL→Opp = qualification. Opp→Win = sales process/competition.

3. VALUE DIAGNOSTIC: Are deal sizes holding?
   Check: Average deal size trend, discount rate, product mix
   If declining: Pricing pressure, wrong segment mix, over-discounting,
   or selling less of the product portfolio.

4. VELOCITY DIAGNOSTIC: Is the pipeline moving fast enough?
   Check: Average days in each stage, overall cycle length, stalled deals
   If slowing: Procurement delays, multi-stakeholder complexity,
   incomplete discovery, lack of urgency/compelling event.

5. RETENTION DIAGNOSTIC: Are existing customers healthy?
   Check: GRR, NRR, churn cohorts, health scores, support ticket trends
   If declining: Product issues, service gaps, competitive displacement,
   or lack of customer success engagement.
```

### Breakout Analysis (The "Who/What/Where/When")

Once you know which metric is off, slice it to find the root cause:

```
WHO:   By rep/team  → Is it systemic or individual?
WHAT:  By product   → Is it the core product or a specific offering?
WHERE: By segment   → Is it SMB, mid-market, or enterprise?
       By source    → Is it inbound, outbound, or partner?
       By territory → Is it geographic?
WHEN:  By cohort    → Is it recent leads/deals, or a long-standing pattern?
       By period    → Did something change at a specific point in time?
```

**Example diagnostic:**
```
Problem: Win rate dropped from 25% to 18% this quarter

WHO slice: Enterprise team at 12%, Mid-Market still at 26%
→ Problem is isolated to Enterprise segment

WHERE slice: Enterprise DACH at 8%, Enterprise UK at 18%
→ Problem is concentrated in DACH

WHAT slice: DACH losses are 70% "Lost to Competitor"
→ Competitive pressure in DACH market

Action: Competitive analysis for DACH, review positioning,
consider SE investment for DACH deals
```

## Cohort Analysis

### Revenue Cohorts

Group customers by acquisition period and track their revenue over time:

```
          Month 0   Month 6   Month 12  Month 18  Month 24
Q1 2024:  €500K     €480K     €520K     €540K     €560K
Q2 2024:  €600K     €570K     €590K     €610K
Q3 2024:  €550K     €530K     €560K
Q4 2024:  €700K     €680K

What to look for:
- Do cohorts grow over time? (NRR > 100%)
- How much do they lose in the first 6 months? (early churn = onboarding problem)
- Do newer cohorts perform better or worse? (is the product improving?)
- Is there a consistent pattern of growth or decline?
```

### Payback Cohorts

Track when each customer cohort pays back its acquisition cost:

```
Cohort CAC:     €45K average per customer
Monthly ARPA:   €2.5K × 80% gross margin = €2K contribution
Payback:        €45K ÷ €2K = 22.5 months

If newer cohorts have lower CAC (more efficient acquisition) or higher
ARPA (better pricing/packaging), payback improves over time. Track this.
It's one of the best indicators of business health improvement.
```

## Role-Based Scorecard Architecture

Different roles need different views of the same data. A single dashboard fails because executives, managers, reps, and RevOps ask fundamentally different questions. Build cascading scorecards:

```
EXECUTIVE VIEW (North Star: reviewed weekly/monthly):
  ARR and ARR growth rate | NRR and GRR | Rule of 40 score
  Pipeline coverage ratio | Forecast accuracy (±%)
  CAC Payback | LTV:CAC ratio | Burn multiple
  → Question answered: "Are we on track and efficient?"

MANAGER VIEW (Operational: reviewed weekly):
  Pipeline created vs. target (by rep, by source)
  Stage conversion rates vs. benchmark (where is it breaking?)
  Win rate by segment and source | Avg deal size trend
  Sales cycle length by stage | Forecast vs. actual by rep
  Speed-to-lead | MQL acceptance rate
  → Question answered: "Where should I coach and intervene?"

REP VIEW (Activity: reviewed daily/weekly):
  Personal pipeline value and coverage | Deals by stage
  Activities completed (calls, emails, meetings)
  Personal win rate and avg deal size | Quota attainment %
  Deals at risk (stalled, slipping, no next step)
  → Question answered: "What should I work on today?"

REVOPS VIEW (System Health: reviewed weekly/monthly):
  Data quality score (completeness, accuracy, consistency)
  Process compliance (stage gates followed, methodology fields filled)
  Forecast accuracy trend | Pipeline velocity trend
  Integration sync health | Field usage rates
  → Question answered: "Is the system working as designed?"
```

**Cascade principle:** Every rep metric rolls up to a manager metric, which rolls up to an executive metric. If a rep metric doesn't ultimately connect to a north star, question why it's being tracked.

## Deal-Level Health Metrics

Six dimensions to score individual deal health. Each dimension scored 0-3:

| Dimension | Score 0 | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|---------|
| **Next Steps Quality** | No next step defined | Vague ("follow up next week") | Specific date + action | Mutual action plan with milestones |
| **Activity Velocity** | No activity 14+ days | Sporadic, no pattern | Weekly touchpoints | Multiple per week, multi-channel |
| **Multi-Threading** | Single contact | 2 contacts | 3-4 contacts | 5+ including decision-maker |
| **Access to Power** | No EB identified | EB identified, no contact | EB met once | EB actively engaged in process |
| **Review Communication** | Never reviewed | Monthly review | Bi-weekly review | Weekly review with manager |
| **Methodology Adherence** | No SPICED/MEDDIC data | Partial (2-3 fields) | Complete qualification | Leveraged in deal strategy |

**Composite Deal Health Score:** Sum of all 6 (range 0-18)
- 13-18: Healthy
- 10-12: Watch: review in next forecast call
- ≤9: At risk: flag for immediate intervention

**Benchmark context (Ebsta/Pavilion):** Top performers score 2.64x higher on pipeline management, 43% better on win rate, and 455% better on discovery quality. These gaps map directly to the deal health dimensions above.

## Conversational Intelligence Metrics

When conversation intelligence tools are deployed, track these metrics:

| Metric | What It Measures | Target Range | Why It Matters |
|--------|-----------------|-------------|---------------|
| **Talk Ratio** | Rep vs prospect speaking time | 40-60% rep | >60% rep = talking too much, not discovering |
| **Longest Monologue** | Longest uninterrupted rep speech | <2.5 min | Long monologues lose attention and signal pitching, not conversation |
| **Customer Story** | Prospect shares personal/org narrative | ≥1 per call | Indicates trust and engagement depth |
| **Interactivity** | Conversation turn frequency | Every 30-60 sec | High interactivity = dialogue, not presentation |
| **Patience** | Time before rep speaks after question | ≥3 seconds | Rushed responses signal not listening |
| **Question Rate** | Discovery questions per call | 11-14 per call | Below 8 = insufficient discovery |

**Platform and tool note (2026):** Legacy tools (Gong, Chorus) measure rep-led calls. 2026 market includes AI-augmented alternatives (Avoma, Wingman, Fireflies.ai, Outreach Kaia) that capture both rep-led and AI-agent-led conversations with real-time coaching. When AI agents generate calls, the talk-ratio and question-rate metrics shift (agents run scripted patterns, not discovery). Adjust your CI strategy: measure rep calls and AI-agent calls separately. For AI-agent-led motion, focus on resolution rate and automation completion instead of discovery quality.

## Strategic Initiative Trackers

Seven views that turn pipeline data into strategic intelligence:

| Tracker | What It Surfaces | Data Source | Review Cadence |
|---------|-----------------|-------------|---------------|
| **Competitor Mentions** | Which competitors appear in deals, win rate against each | Call transcripts, deal fields | Monthly |
| **Objection Handling** | Top objections, resolution rate, impact on close | Call transcripts, deal notes | Monthly |
| **Deal Momentum** | Acceleration/deceleration patterns in active deals | Stage change velocity, activity data | Weekly |
| **Value Prop Effectiveness** | Which value props correlate with wins | Call transcripts, proposal content | Quarterly |
| **New Product Launch** | Adoption of new features in deals, attach rate | Deal product fields, call mentions | Monthly |
| **Churn Risk Signals** | Early warning patterns from deal and usage data | Health scores, support tickets, usage | Weekly |
| **Customer Reference Pipeline** | Reference-ready customers, reference utilization | NPS, deal outcomes, reference requests | Quarterly |

### AI-Native Platform Metric Automation (2026)

HubSpot Breeze and Salesforce Agentforce shift how metrics are collected and populated:

**HubSpot Breeze (April 2026 launch):** Autonomous agents auto-populate lifecycle-stage fields, health scores, and forecast fields. Impacts: (1) Lifecycle stage date-entered/date-exited/time-in-stage now captured at company level with backfill; (2) Meeting-based workflow triggers enable real-time velocity tracking; (3) Agent-resolved conversations bypass manual data entry. Dashboard implication: metrics populated by agents may show artificially high activity velocity or accelerated stage transitions if not filtered.

**Salesforce Agentforce (2026):** Intelligent agents populate opportunity fields (next steps, stakeholder data, champion identification). Metric drift patterns: (1) AI-generated activity records inflate activity velocity metrics; (2) forecast accuracy improves where agents provide consistent field population but may mask deal quality issues; (3) autonomous deal scoring (Intelligent Context) creates divergence between traditional MEDDIC qualification and AI health assessment. Calibrate: separate rep-captured metrics from agent-populated metrics on your dashboards, or risk confounding human performance with automation gains.

### Canon References for Deal & Intelligence Metrics

Cross-references: full pipeline analytics views with deal health dimensions, KPI benchmark targets for calibrating metric thresholds, and signal-trigger-action patterns for strategic trackers. For current-year benchmarks, see `references/benchmarks.md` (Ebsta/Pavilion) alongside Fullcast/Pavilion 2026 GTM Benchmark data covering seller performance, win rates by stakeholder count, deal cycle timing, pipeline composition, and AI impact metrics.


---

## Norton Framework Additions (Source: Kyle Norton / Aviv Canaani, Revenue Leadership Podcast, 2026)

### Revenue Per AE Constraint Analysis (Norton/Canaani Model)

Revenue per AE is the constraining metric that reveals system health.

**Diagnostic Formula:**
Revenue per AE = f(pipeline quality × conversion rate × deal velocity × rep capacity utilization)

If revenue per AE is low, diagnose which input is the constraint:
- **Low pipeline quality** → ICP drift, marketing-sales misalignment
- **Low conversion rate** → qualification gaps, methodology decay
- **Slow deal velocity** → process friction, missing stakeholders, weak champion
- **Low capacity utilization** → AEs spending time on non-selling activities (prospecting theater)

**The Anti-Prospecting Thesis (Canaani):**
- Most AEs admit 80-90% of closed revenue comes from inbound
- Salesforce State of Sales 2026: reps spend 40% of week actually selling (up from 28% in 2024)
- $250-300K OTE spent on prospecting = failure of resource allocation dressed as culture

**Benchmarks:**

| Metric | Industry Average | Top Performers |
|--------|-----------------|----------------|
| Quota attainment | 43-58% | 80%+ |
| OTE attainment | ~80% | 138% (Owner.com) |
| AE time selling | 28% (2024), 40% (2026) | 60%+ (inbound-fed) |
| Revenue per AE vs. competitors | 1x | 3-4x (Owner, Datarails) |

### Predictability Metrics

Predictability is built, not hoped for.

**Core Predictability Metrics:**
- **Forecast variance** (coefficient of variation in close rates by period): target: <10% CV
- **Pipeline quality score:** % of pipeline at SPICED ≥8/15 or MEDDIC ≥60%
- **Win rate by segment**: high variance = wrong ICP definition or inconsistent qualification
- **Cycle time consistency**: standard deviation of days-to-close by deal segment
- **Conversion rate stability**: stage-to-stage conversion rates should be stable QoQ

**Win Rate as ICP Fit Signal:**
- High win rate variance by segment reveals where qualification is breaking
- If Enterprise wins at 35% and Mid-Market wins at 12%, your Mid-Market ICP is wrong or methodology isn't adapted
- Win rate segmented by lead source: inbound vs outbound reveals true channel quality

**The Productivity-First Quota Test (Canaani Model):**
Know these numbers before setting any quota:
1. Cost per meeting
2. Conversion rate at every stage
3. Sales cycle length (Datarails: 30-45 days)
4. AE meeting capacity before quality drops
5. Only hire new AEs when you have pipeline to fill their calendars

> "I don't really care that much about the quota. I care about how much I think they actually can produce. Knowing the real productivity is what matters.": Aviv Canaani

### New Benchmark Data (Kyle Norton Podcast, E60-E64, Jan-Mar 2026)

**Quota & Productivity:**

| Metric | Source | Value |
|--------|--------|-------|
| Average quota attainment | RepVue Cloud Sales Index (Q4 2024, 238 cos) | 43% |
| Reps hitting quota | Bridge Group SaaS AE Metrics Report | ~58% |
| Rep time actually selling | Salesforce State of Sales (2024) | 28%; (2026) 40% |
| Avg time to full rep productivity | Sales Management Association | 11.2 months |
| High performer productivity premium | McKinsey | 400% (800% in complex roles) |
| Revenue per employee (Netflix) | Public data | ~$3M (2x Google, 10x Disney) |

**Inbound vs. Outbound:**

| Metric | Source | Value |
|--------|--------|-------|
| Inbound leads cost reduction | HubSpot | 61% less than outbound |
| Buyer-initiated first contact | 6sense | 83% of the time |
| Self-navigating buyer deal quality | Gartner | 65% high-quality vs. 24% sales-led |
| Outbound touches per opportunity (human-SDR, 2026) | Donovan/Insight Partners, E61 | 1,000-1,400 |
| Outbound touches per opportunity (5 years ago) | Donovan/Insight Partners, E61 | 200-400 |
| Outbound touches per opportunity (AI-agent, 2026) | practice-based | 10,000+ personalized touches per month |
| Outbound opportunities booked via phone | Donovan/Insight Partners, E61 | 70% |

**AI Agent Touch Compression (2026 caveat):** The 1,000-1,400 figure describes human SDR outreach. AI agents execute 10,000+ personalized touches monthly (vs 200-300 per human SDR), compressing the touches-to-conversion metric dramatically. When measuring outbound efficiency, separate human-SDR touches from AI-agent touches. Blended metrics hide whether your conversion lift comes from better targeting, message quality, or pure volume. Track (a) AI-agent touches per opportunity, (b) AI-agent-sourced opportunity quality (compare win rate and deal size), (c) cost per AI-generated opportunity for cost efficiency comparison.

**AI Adoption:**

| Metric | Source | Value |
|--------|--------|-------|
| Current AI productivity gains (augmentation) | Donovan/Insight Partners survey, E61 | 5-15% |
| Companies building own RFP tools | Donovan/Insight Partners, E61 | ~50% |
| BDR productivity lift with agents (calls) | Owner.com pilot, E60 | +85% |
| BDR productivity lift with agents (opps) | Owner.com pilot, E60 | +85% |
| AI-assisted ramp compression target | Donnelly/Crescendo, E62 | 11.2 → 3 months |

**Case Study Benchmarks:**

| Company | Metric | Value | Source |
|---------|--------|-------|--------|
| Datarails | Sales cycle | 30-45 days | Canaani, E64 |
| Datarails | Forecast accuracy | Within 5%, 3/4 quarters | Canaani, E64 |
| Owner.com | Per-rep productivity vs. competitors | 3-4x | Norton, E64 |
| Owner.com | OTE attainment | ~138% | Norton, E64 |
| Owner.com | Reps hitting target | ~80% | Norton, E64 |
| Crescendo | Time to $100M ARR | Under 2 years | Donnelly, E62 |

**PMF & Startup Failure:**

| Metric | Source | Value |
|--------|--------|-------|
| Startups failing for lack of market need | CB Insights | 42% |
| Failed startups that built before validating | Failory | 65% |
| B2B buyers time spent de-conflicting information | Gartner | 2/3 of buying journey |

## How to Use This Skill

**"Our revenue is off: help me figure out why":** Run the revenue diagnostic sequence. Start with volume, then conversion, then value, then velocity, then retention. Identify the broken link and slice by who/what/where/when.

**"What metrics should we track?":** Start with the minimum viable funnel (7 stages). Layer on conversion rates, the 4 velocity levers, and unit economics. Build dashboards in the three-tier structure (north star → operational → activity).

**"How do we compare to benchmarks?":** Provide specific benchmarks by stage, segment, and motion. Context matters: a 15% win rate is terrible for SMB but normal for enterprise. Always benchmark against comparable companies. For current-year B2B benchmarks, see `references/benchmarks.md` (Ebsta/Pavilion) and the Fullcast/Pavilion 2026 data (win rates by stakeholder count, deal cycle data, AI impact metrics, and pipeline composition benchmarks).

**"Help me build a revenue model":** Start with the velocity formula, layer in unit economics (CAC, LTV, payback), add retention metrics (NRR, GRR), and project forward using capacity and conversion assumptions.

**"Cohort questions":** Build the cohort view: revenue over time by acquisition period. Look for the inflection patterns: early churn, expansion timing, and cohort-over-cohort improvement.

**"How do we score deal health?":** Use the 6-dimension deal health model. Score each dimension 0-3, sum for composite (0-18). Flag deals ≤9 for intervention. Connect to forecast process: unhealthy deals shouldn't be in Commit.

**"What should we track from call recordings?":** Start with the 6 conversational intelligence metrics. Focus coaching on talk ratio and question rate first: these have the highest correlation with discovery quality.

---

**Cross-references:**
- For V/CR/Δt metric scaffold, expansion type matrix (Renew/Resell/Upsell/Cross-sell), churn classification, and benchmarking methods, see `references/revenue-data-model-scaffold.md`.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates: Pavilion Unit Economics Worksheet

For LTV/CAC/GM Payback/LTV:CAC calculations in client engagements, use the pre-built adapted template:
`Frameworks/Templates/cro-school/pavilion-unit-economics-neon.xlsx`

Structure: 1 sheet, 30 rows × 7 cols. Includes validation cells (`=if(E4=G4,"CORRECT","INCORRECT")`). Preserves all original formulas.

Use in: diagnostic baselines, programme ROI justification, benchmark comparisons.

Original source: `Sources/Courses/CRO-School/Pavilion Unit Economics Worksheet.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
