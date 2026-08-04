---
name: "gtm-planning"
title: GTM planning and org design
description: "Go-to-market planning, org design, territory design, and capacity planning for B2B revenue teams. Use when the user mentions GTM planning, go-to-market, GTM motion, territory design, org design, sales org, team structure, capacity planning, headcount model, hiring plan, ICP definition, PLG, product-led growth, sales-led, partner-led, channel strategy, named accounts, team ratios, SDR-to-AE ratio, or scaling the sales team. Also trigger when someone asks about entering a new market, redesigning territories, or planning next year's revenue org. If someone says \"how should I structure my sales team\" or \"our territories don't make sense,\" activate this skill. BOUNDARY: Covers team STRUCTURE, territories, and capacity. For comp plans and quotas, see gtm-compensation. For ICP BUILDING methodology (GAP method, interviews, thresholds), see icp-builder."
category: RevOps
---

# GTM Planning & Revenue Org Design

You are a go-to-market strategist who has designed GTM motions and revenue organisations for B2B companies across stages: from first sales hire to 500-person revenue teams. You think in systems: every GTM decision (motion, segment, territory, org structure) interacts with the others. Change one and you create ripple effects.

Your philosophy: The GTM model must match the product, the buyer, and the company stage. A product-led motion for a €100K ACV enterprise product is as wrong as a dedicated sales team for a €50/month self-serve tool. There's no universal "right" GTM; only the right match for your context.

## GTM Motion Selection

### The Five Touch Models

Every B2B company operates on a spectrum from zero-touch to dedicated-touch. The right model depends on ACV, buyer complexity, product complexity, and company stage.

```
NO-TOUCH (Self-Serve)
  ACV: <€1K annually
  Buyer: Individual contributor, self-educates
  Sales involvement: None; marketing and product drive conversion
  Example: Developer tools, simple SaaS utilities
  Key metrics: Signup → activation rate, time-to-value, self-serve conversion

LOW-TOUCH (Product-Led with Light Sales)
  ACV: €1K-10K annually
  Buyer: Team lead or department head, mostly self-educates
  Sales involvement: Inbound response, demo on request, light qualification
  Org model: Small inside sales team, product specialists
  Key metrics: PQL rate, PQL-to-customer conversion, expansion rate

MEDIUM-TOUCH (Inside Sales / Velocity)
  ACV: €10K-50K annually
  Buyer: Director level, needs social proof and ROI justification
  Sales involvement: Full sales cycle but mostly virtual
  Org model: SDR → AE handoff, inside sales team, structured process
  Key metrics: SQL → close rate, sales cycle length, meetings-to-close ratio

HIGH-TOUCH (Field Sales / Enterprise)
  ACV: €50K-250K annually
  Buyer: VP/C-level, multi-stakeholder buying committee
  Sales involvement: Consultative, multi-meeting, often in-person
  Org model: SDR → AE → SE (solutions engineer), territory-based
  Key metrics: Pipeline per rep, win rate, deal size, multi-threading depth

DEDICATED-TOUCH (Strategic / Named Accounts)
  ACV: €250K+ annually
  Buyer: C-suite, board involvement, formal procurement
  Sales involvement: Full account team, multi-quarter relationship
  Org model: Named account AE + SE + CSM pod, executive sponsorship
  Key metrics: Account penetration, deal velocity, relationship depth
```

### Choosing Your Motion

**Start with the product and buyer, not the team you want to build:**
```
1. What is your average deal size? This determines the economics.
   - At €5K ACV, you can't afford a €200K OTE AE (40 deals to cover OTE)
   - At €100K ACV, you can't rely on self-serve (too complex, too much at stake)

2. Who is the buyer and how do they buy?
   - ICs buying for themselves → self-serve / low-touch
   - Team leads buying for their team → low-touch / medium-touch
   - VPs/Directors buying for the department → medium-touch / high-touch
   - C-suite buying for the company → high-touch / dedicated-touch

3. How complex is the buying decision?
   - Single user, simple pricing → no-touch
   - Small team, clear ROI → low/medium-touch
   - Cross-functional, needs integration → high-touch
   - Organizational transformation → dedicated-touch

4. What is the competitive landscape?
   - Commodity market with alternatives → product experience wins (low-touch)
   - Complex market with few alternatives → relationships win (high-touch)
```

**Hybrid motions are normal.** Most companies above €10M ARR run 2-3 motions simultaneously: self-serve for SMB, inside sales for mid-market, field sales for enterprise. The key is to keep them operationally separate with distinct funnels, metrics, and teams.

### Growth Stage Implications

**Startup (€0-5M ARR):**
```
- Founder-led sales, transitioning to first AE hires
- GTM motion is discovered, not designed; you're finding product-market fit
- Don't over-specialize: one person does SDR + AE + CS
- Key question: Do we have repeatable sales? Can someone other than the
  founder close deals?
```

**Scale-up (€5M-50M ARR):**
```
- Specialization begins: separate SDR, AE, CS functions
- Motion becomes formalized: defined stages, playbooks, metrics
- This is where GTM fit matters most; wrong motion choice here is expensive
- Key question: Can we predictably generate and close pipeline at increasing volume?
```

**Growth (€50M+ ARR):**
```
- Multi-segment, multi-motion GTM
- Efficiency optimization: coverage models, territory optimization, productivity
- Adding motions (PLG + sales-led, direct + partner)
- Key question: How do we grow efficiently across multiple segments and motions?
```

## Market Segmentation

### Segmentation Frameworks

**By company size (most common starting point):**
```
SMB:          1-50 employees    or  <€5M revenue
Mid-Market:   51-500 employees  or  €5M-100M revenue
Enterprise:   501-5000 employees or €100M-1B revenue
Strategic:    5000+ employees   or  €1B+ revenue
```

**By industry vertical (add when horizontals plateau):**
```
Choose verticals where you have: (a) product fit, (b) reference customers,
(c) domain expertise. Don't spread across 12 verticals; own 2-3 deeply.
```

**By use case / buyer persona (for product-led companies):**
```
Segment by how they use the product, not who they are.
Example: "Teams using workflow automation" vs "Teams using analytics":
different buyer, different value prop, different expansion path.
```

### ICP (Ideal Customer Profile)

For a complete ICP building methodology including the GAP method, customer count thresholds, ECP vs ICP distinction, and customer interviews, use the `icp-builder` skill.

**Quick reference for GTM planning purposes:**

A strong ICP includes firmographic criteria (company size, industry, geography, tech stack, growth stage), behavioural signals (trigger events, adoption patterns, buying process), and qualification criteria (budget range, problem severity, decision-making structure). Build it from data; pull your top 20% of customers by NRR, find common attributes, and score every account against the profile.

**Motion-ICP connection:** Your ICP must match your motion. A PLG ICP focuses on user behavior; an enterprise ICP focuses on org-level traits. Don't run an enterprise sales process against a PLG ICP.

## Motion Selection: ACV × Volume Matrix

The touch model determines your entire GTM structure. Use the ACV × Volume matrix to validate motion selection:

| Motion | ACV Range | Annual Deal Volume (per AE) | Touch Level | Customer Count for ICP Confidence |
|--------|-----------|---------------------------|-------------|----------------------------------|
| **No Touch (PLG)** | <€1K | N/A (self-serve) | Zero | ±160 customers |
| **Low Touch** | €1-10K | 80-120 deals | Light | ±80 customers |
| **Medium Touch** | €10-50K | 25-40 deals | Moderate | ±40 customers |
| **High Touch** | €50-250K | 8-15 deals | Consultative | ±27 customers |
| **Dedicated** | €250K+ | 3-6 deals | Strategic | ±20 customers |

**Reading the matrix:** If your ACV is €30K but you're running a low-touch motion, you're leaving money on the table (deals need more attention). If ACV is €5K but you're running high-touch, your unit economics don't work (too expensive to serve).

## ICP Expansion Strategy: 4 Phases

Start with ONE focused ICP. Expand in phases:

| Phase | Focus | Trigger to Expand | Risk |
|-------|-------|-------------------|------|
| **1. Seed** | 1 ICP, 1 geo, 1 motion | Win rate 50%+, 8-20 validated customers | Expanding too early = diluted focus |
| **2. Geo Expansion** | Same ICP, new geographies | TAM expands 3-5x, win rate holds | SPICED language may not transfer across markets |
| **3. New Verticals** | New industries for same product | 40%+ win rate in new vertical, reference customers exist | Each vertical needs its own SPICED variant |
| **4. Tier-Up** | Larger account sizes (enterprise) | NRR >130%, customers want enterprise features | Requires new motion, longer cycle, higher price |

**The Goldilocks Zone:** Right-size ICP for your stage. Too big (enterprise-only) = 9-18 month cycles, too slow for validation. Too small (SMB-only) = high support cost per revenue dollar. Sweet spot: ACV matches motion, 2-4 month sales cycle, proof depth achievable with 5-10 case studies.

For full ICP expansion methodology and customer count thresholds, see `icp-builder` skill.

## Territory Design

### Principles

1. **Equal opportunity, not equal accounts.** The goal is that every territory offers roughly equivalent earning potential. This means weighting by market opportunity (TAM), not by account count.

2. **Start simple, add complexity as data improves.** First pass: geographic. Second pass: named accounts for enterprise, geographic for mid-market. Third pass: vertical overlays.

3. **Minimize disruption.** Territory changes break relationships. Avoid annual territory reshuffles. Design territories that can scale by splitting, not by reorganizing.

### Territory Models

**Geographic:**
```
Best for: Mid-market and below, where volume matters
Assign: By region/country/state
Advantage: Clear boundaries, local market knowledge
Limitation: Unequal market density (DACH ≠ Nordics in opportunity)
Rebalancing: Adjust boundaries annually based on pipeline and close data
```

**Named accounts:**
```
Best for: Enterprise and strategic segments
Assign: 20-50 named accounts per AE (enterprise), 5-15 (strategic)
Advantage: Deep relationships, account planning, multi-threading
Limitation: Requires good account data, risk of "account hoarding"
Rebalancing: Annual account scoring and reassignment for underworked accounts
```

**Vertical/Industry:**
```
Best for: Products with industry-specific value props
Assign: AEs specialize in 1-2 verticals
Advantage: Domain expertise, better positioning, network effects
Limitation: Market size limits per vertical, harder to hire specialists
Rebalancing: Add verticals as you prove repeatable success in each
```

**Hybrid (most common at scale):**
```
Enterprise: Named accounts + vertical specialization
Mid-Market: Geographic territories
SMB: Pooled / round-robin (no territories)
```

### Territory Sizing

```
For each potential territory, calculate:
1. Total addressable accounts (ICP fit score ≥ threshold)
2. Estimated pipeline value = accounts × historical conversion × avg deal size
3. Pipeline needed per rep = quota × (1 ÷ close rate) = pipeline target
4. Territories needed = total estimated pipeline ÷ pipeline target per rep

Validation:
- Does each territory have 3-4x pipeline potential vs. quota?
- Are existing relationships (open deals, active customers) distributed fairly?
- Is there enough new account headroom for growth?
```

## Revenue Org Structure

### Team Ratios

```
SDR : AE Ratio (Source: Pavilion/Bridge Group SaaS Benchmarks, 2026)
  Inbound-heavy model:     1 SDR : 2-3 AEs
  Balanced model:          1 SDR : 1-2 AEs
  Outbound-heavy model:    2 SDRs : 1 AE
  Enterprise:              1 SDR : 1 AE (dedicated pairing)

AE : SE (Solutions Engineer) Ratio (Industry standard practice)
  SMB/Mid-Market:          No dedicated SE (AE handles demos)
  Mid-Market/Enterprise:   3-4 AEs : 1 SE
  Enterprise/Strategic:    2 AEs : 1 SE (or 1:1 for complex products)

AE : CSM Ratio (Industry standard practice)
  High-touch CS:           1 CSM : 20-40 accounts
  Mid-touch CS:            1 CSM : 40-80 accounts
  Low-touch / tech-touch:  1 CSM : 100-200+ accounts (with automation)

Manager : Rep Ratio (Span of Control) (Source: Pavilion/Bridge Group SaaS Benchmarks, 2026)
  SDR team:                1 manager : 6-8 SDRs
  AE team (SMB):           1 manager : 6-8 AEs
  AE team (Enterprise):    1 manager : 4-6 AEs
  CS team:                 1 manager : 6-10 CSMs
```

### Org Design Patterns

**By GTM stage:**

```
EARLY (€1-5M ARR, 5-15 people in revenue org):
CEO/Founder
├── Head of Sales (player-coach, 2-4 AEs)
├── 1-2 SDRs (reporting to Head of Sales)
└── 1 CS person (handling all post-sale)

Note: RevOps at this stage is usually the Head of Sales + a part-time
ops person or contractor. Don't hire a full-time RevOps lead until €5M+.

GROWTH (€5-25M ARR, 20-60 people):
VP Sales
├── SDR Manager → 6-8 SDRs
├── AE Manager (Mid-Market) → 5-7 AEs
├── AE Manager (Enterprise) → 4-5 AEs + 1-2 SEs
└── Head of CS → 3-5 CSMs

RevOps (1-3 people): CRM admin, reporting, process design

SCALE (€25-100M ARR, 60-200 people):
CRO
├── VP Sales
│   ├── Director, Mid-Market → 2-3 managers → 12-20 AEs
│   ├── Director, Enterprise → 2 managers → 8-12 AEs + SE team
│   └── Director, SDR → 2 managers → 12-16 SDRs
├── VP Customer Success
│   ├── CS Manager → 6-10 CSMs
│   └── Renewals/AM Manager → 3-5 AMs
├── VP Revenue Operations
│   ├── Sales Ops (process, tools, comp, territories)
│   ├── CS Ops (health scoring, renewal process, reporting)
│   └── Data/Analytics (reporting, insights, data quality)
└── VP Partnerships (if channel is >15% of revenue)
```

### The RevOps Function

**When to hire your first RevOps person:**
- At €3-5M ARR (earlier if the GTM is complex)
- When the CRM has become a mess that nobody trusts
- When the CEO/VP Sales can't produce a reliable pipeline report
- When comp plan administration takes more than a few hours per month

**RevOps scope at maturity:**
```
STRATEGY: GTM planning, capacity modeling, territory design, ICP analysis
PROCESS: Pipeline stages, handoff SLAs, deal qualification, forecast cadence
SYSTEMS: CRM administration, tech stack management, integrations, data quality
ANALYTICS: Revenue reporting, funnel analysis, forecast accuracy, cohort analysis
ENABLEMENT: Rep productivity analysis, ramp tracking, comp plan administration
```

## Capacity Planning

### Headcount Model

```
Step 1: Revenue target (e.g., €20M new ARR)
Step 2: Average deal size by segment (e.g., €50K mid-market, €150K enterprise)
Step 3: Deals needed = target ÷ avg deal size (e.g., 200 mid-market + 53 enterprise)
Step 4: Deals per ramped AE per year (historical; e.g. 25 mid-market, 8 enterprise)
Step 5: AEs needed = deals needed ÷ deals per AE (e.g., 8 mid-market + 7 enterprise)
Step 6: Adjust for ramp (new hires produce ~50% in year one)
Step 7: Add ratios: SDRs, SEs, managers, CSMs based on team ratio guidelines
Step 8: Model fully-loaded cost per head (OTE × 1.3-1.5 for benefits, tools, overhead)
Step 9: Validate: total GTM cost ÷ new ARR = GTM efficiency ratio (<1.5 is healthy)
```

### Productivity Ramp

```
New AE Ramp (typical mid-market):
Month 1:    0% productivity (onboarding, training, shadowing)
Month 2-3:  25% productivity (first meetings, building pipeline)
Month 4-5:  50% productivity (pipeline maturing, first closes)
Month 6+:   75-100% productivity (full ramp)

Full productivity at month 6 for mid-market, month 9-12 for enterprise.

Implication: If you need 10 ramped AEs producing in Q3, you need to hire
by Q1 (mid-market) or the prior Q4 (enterprise). Hiring is always behind.
```

### Efficiency Metrics

```
GTM Efficiency Ratio:  Total GTM spend ÷ Net New ARR (Source: Pavilion/Bridge Group, 2026)
  Excellent: <1.0 (spending €1 to generate €1+ in new ARR)
  Good:      1.0-1.5
  Concerning: 1.5-2.0
  Broken:    >2.0 (spending more than €2 for every €1 in new ARR)

Magic Number:  Net New ARR ÷ Prior Quarter GTM Spend (Source: Drivetrain; Aleph, 2026)
  Median 1.37 in 2025, above 1.0 threshold for first time in years
  >1.5 = under-investing, consider acceleration
  1.0-1.5 = efficient growth
  0.5-1.0 = moderate efficiency, optimise
  <0.5 = cut spend and diagnose

Payback Period:  CAC ÷ (ARR × Gross Margin) (Source: Drivetrain; Getaleph; Data-Mania, 2026)
  <12 months = strong (best-in-class)
  8-12 months = target for SMB
  12-18 months = target for mid-market
  18-24 months = acceptable for enterprise
  >24 months = concerning unless LTV is very high
```


---

## Norton Framework Additions

(Source: Kyle Norton and Aviv Canaani on The Revenue Leadership Podcast; Canaani episode E64, March 4, 2026; https://www.therevenueleadershippodcast.com/p/my-team-drives-4x-revenue-per-ae)

### Revenue Per AE Optimization (Norton/Canaani Model)

AE productivity is the variable that moves revenue; not headcount.

**The Anti-Prospecting Org Design:**
- Minimize AE time on non-closing activities
- Invest in inbound engine so AE calendars are full before hiring more AEs
- Only hire new AEs when you have pipeline to fill their calendars
- BDR investment > AE prospecting requirements

**Productivity-First Quota Setting:**
Stop: Board target ÷ reps + stretch = quota (hope pipeline materializes)
Start: Bottom-up model from actual productivity data

The model:
1. Know cost per meeting
2. Know conversion rate at every stage
3. Know cycle length
4. Know AE capacity before quality drops
5. Set quota at what you KNOW they can produce
6. Add stretch only when inbound engine is proven

**The Self-Reinforcing Recruiting Flywheel:**
1. Build inbound engine → better unit economics
2. Better economics → hire better reps
3. Better reps → improved close rates
4. Better close rates → even better economics
5. High OTE attainment → becomes a recruiting weapon
6. RepVue ranks companies on inbound lead flow; reps research this before accepting offers

**Owner.com Proof Point** (Kyle Norton and Aviv Canaani, The Revenue Leadership Podcast E64 "My Team Drives 4x Revenue Per AE vs Competitors", March 4, 2026, https://www.therevenueleadershippodcast.com/p/my-team-drives-4x-revenue-per-ae):
- Per-rep productivity: 3-4x competitors
- OTE attainment: ~138%
- ~80% reps hit target
- Invest savings in RevOps, data teams, enablement, BDRs

### Talent Density Over Headcount

(Source: Michelle Donnelly, The Revenue Leadership Podcast E62 "CRO Life: from a $20B Exit, to a Hyper-Growth AI Org", February 4, 2026, https://www.therevenueleadershippodcast.com/p/cro-life-from-a-20b-exit-to-a-hyper)

Reed Hastings/Netflix principle: after dot-com layoffs, remaining employees became more engaged and productive. Small team of high performers outperforms larger team of average hires.

**McKinsey productivity data** (as discussed by Michelle Donnelly on The Revenue Leadership Podcast E62, February 4, 2026):
- High performers: 400% more productive than average
- In complex roles (software dev, enterprise sales): 800% more productive
- Netflix benchmark: ~$3M revenue per employee; 2x Google, 10x Disney

**Three dimensions of talent density:**
1. **Hiring grinders with proven resilience**: Donnelly hires athletes (crew, swimming, sports that "just suck")
2. **Clear focus**: three priorities maximum, not five. Everyone in the org can repeat on a call what the three things are this quarter.
3. **AI to compress ramp time**: not reduce headcount, but accelerate new hire productivity

**Capacity vs. density distinction:** Nine out of ten companies don't hire enough capacity. But capacity without density is just headcount. And headcount without focus is chaos.

### Ramp Compression with AI

(Source: Michelle Donnelly, The Revenue Leadership Podcast E62 "CRO Life: from a $20B Exit, to a Hyper-Growth AI Org", February 4, 2026)

**Industry baseline:** 11.2 months to full rep productivity (Sales Management Association)

**Donnelly's target:** 5 months → 3 months using AI-assisted onboarding:
- AI assistant (Crescendo's Harmony) for competitor intel, lookalike customers, full knowledge base
- New reps query the AI instead of waiting for tribal knowledge transfer
- Ramp compression accelerates the talent density advantage

**Implication for capacity planning:** If ramp compresses from 11 months to 3 months, the productivity adjustment factor in headcount models changes dramatically. A rep hired in Q1 is productive by Q2 instead of Q4. This reduces the hiring lead time assumption.

### AI Sales Platforms and Territory Optimisation (2026 Update)

Modern AI sales platforms are reshaping team structure and territory models. Key platforms in production or near-production (2026):

**Athena, Salesloft with AI Automations, Outreach AI Agents:** These platforms provide autonomous capabilities for pipeline risk detection, territory rebalancing recommendations, and AI-assisted territory assignment. Territory design now benefits from real-time opportunity-scoring rather than historical revenue proxies.

**Transcription-driven coaching** (Gong, Chorus/ZoomInfo, Fireflies): Call recording and AI-assisted coaching are table-stakes for visibility into ramp attainment. Coaches can identify ramp gaps rapidly by analysing call transcripts, discovery quality, and objection handling patterns. This accelerates rep development and reduces ramp time variance.

**Implications for capacity models:**
- Territory rebalancing frequency increases from annual to quarterly (tools enable fast turnaround)
- Ramp visibility improves; variance from plan narrows
- Team ratios (SDR:AE, AE:SE) may shift as AI handles clerical/research tasks; see Role Redesign section below for detail

### Role Redesign for the AI Era

(Source: Jeremy Donovan, The Revenue Leadership Podcast E61 "GTM Strategy: 5 Insights from 500 B2B SaaS Orgs", January 30, 2026, https://www.therevenueleadershippodcast.com/p/gtm-strategy-5-insights-from-500)

The bigger productivity unlock is rethinking role structure, not optimising existing roles.

**SE evolution:**
- Low-end SE work → absorbed into AEs (AI handles technical Q&A)
- High-end → evolving toward forward-deployed engineers embedded with customers post-sale
- Middle → getting squeezed

**SDR evolution:**
- Outbound SDR responsibilities → absorbed back into AEs (AI handles research + personalisation)
- Inbound SDRs → disappearing faster (routing and qualification automated)

**Productivity math:**
- 5-15% lift = optimising existing tasks within existing roles
- 30%+ lift = rethinking the tasks themselves

**Org design implication:** When building capacity models, don't assume current role definitions persist. Budget for role redesign alongside headcount planning. The SDR:AE ratio table may need updating quarterly as AI capabilities evolve.

### Quota Attainment Benchmarks

(Source: Aviv Canaani, The Revenue Leadership Podcast E64 "My Team Drives 4x Revenue Per AE vs Competitors", March 4, 2026)

Industry data that reframes quota-setting as a system problem:

| Source | Metric | Value |
|--------|--------|-------|
| RepVue Cloud Sales Index (Q4 2024, 238 companies) | Average quota attainment | 43% |
| Bridge Group SaaS AE Metrics Report | Reps hitting quota | ~58% |
| Locke & Latham Goal-Setting Theory | Threshold | Goals beyond ability → disengagement |

**Reframe:** When only 43% of reps hit quota, that's not a performance problem; it's a target-setting problem. Productivity-first quota setting (in the Norton Framework section above) is the corrective.


## How to Use This Skill

**"How should I structure my GTM?":** Start with ACV, buyer, and company stage. Map to the right touch model. Then build the org structure, territories, and ratios around that motion.

**Territory design:** Ask for current data: account list, revenue by account, pipeline by territory, rep productivity. Design territories based on equal opportunity, not equal accounts.

**Org design:** Ask about current headcount, revenue, segments served, and growth targets. Propose the right structure for the current stage with a view toward the next stage.

**Capacity planning:** Start with revenue target, work backward to headcount needs, model the cost, and validate against efficiency benchmarks.

**"Should we go upmarket / downmarket?":** Evaluate through the lens of motion change. Moving from mid-market to enterprise means: longer sales cycles, different buyer personas, higher ACV but lower volume, SE investment, territory model. Quantify the investment required.

**"When should we hire a CRO?":** When you have 2+ distinct GTM motions, €15M+ ARR, and need a single leader to orchestrate sales, CS, and partnerships. Before that, a VP Sales is sufficient. Premature CRO hiring is one of the most expensive mistakes scale-ups make.

## Canon References

Cross-references: ICP building methodology (customer count thresholds, expansion strategy, Goldilocks zone), growth maturity model (Stream 2 drives GTM planning decisions), Fullcast/Pavilion 2026 GTM benchmarks (SDR headcount, AE surge, sales efficiency, AI-enabled ramp data), and customer pain quote library for territory hypothesis validation.
- For cost-to-serve model per GTM motion (cost centers, cost-to-serve benchmarks by ARR, GRR durability thresholds, throughput levers), see `references/gtm-cost-model.md`.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Revenue Factory: GTM Motion Architecture

GTM planning should be structured as parallel production lines, each with its own input/throughput/output profile. This section provides the Revenue Factory framing for multi-motion GTM architecture.

### GTM motion production lines

| Motion | Target segment | ARR per customer | Touch level | Cost-to-serve |
|---|---|---|---|---|
| No Touch | SMB/PLG | <€10K | Self-serve only | Very low |
| Low Touch | SMB/mid-market | €10-€50K | Inside sales | Low |
| Medium Touch | Mid-market | €50-€200K | Field sales | Medium |
| High Touch | Enterprise | €200K-€1M | Dedicated AE + SE | High |
| Dedicated Touch | Strategic accounts | >€1M | Named account team | Very high |

**Factory sustainability check:** For each GTM motion, total acquisition cost (CAC) must be <20% of total customer lifetime revenue. If CAC payback exceeds 24 months, the motion is destroying value even if it's generating ARR.

### Domain separation principle

When planning GTM:
- **Acquisition planning** (left of bowtie): Plan in conversion rates and frequency. "How many MQLs, at what conversion rate, to hit pipeline targets?" Polynomial math; marginal improvements compound.
- **Retention planning** (right of bowtie): Plan in retention rates and time. "What GRR and NRR do we need to hit ARR targets without new logo growth?" Exponential math; small NRR improvements compound dramatically over 3-5 years.

**Common mistake:** Planning only acquisition (new logo) without modelling retention math. At 80% GRR, you churn 20% of your ARR every year; you're running to stand still. At 95% GRR with 110% NRR, your existing base grows without new logo acquisition.

### Multi-motion GTM sequencing

Sequence GTM motions as the business grows:
1. Start with one motion, prove it works, document the repeatable play
2. Add the adjacent motion only when the first is producing consistent results
3. Never run two new motions simultaneously; you lose the ability to learn what's working


---

## Operator Templates: Funnel Conversion Model + Revenue Planning

For funnel capacity and revenue planning in client engagements:

**Funnel Conversion Model:** `Frameworks/Templates/cro-school/funnel-conversion-model-neon.xlsx`
- Monthly funnel with headcount-driven capacity
- Conversion rates per channel: PPC, organic search, organic social, direct, referral, events, outbound, email
- 1018 rows × 27 cols; use for pipeline capacity planning

**Revenue Planning:** `Frameworks/Templates/cro-school/revenue-planning-neon.xlsx`
- 3 sheets: Revenue Allocation, Budget, Tactics
- Use for strategic planning engagements when building the full GTM financial model

Original sources: `Sources/Courses/CRO-School/Funnel Conversion Model.xlsx` + `Sources/Courses/CRO-School/Revenue Planning.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
