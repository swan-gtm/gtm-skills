---
name: "gtm-compensation"
title: GTM compensation design
description: "GTM compensation plan design, quota setting, OTE structures, and benchmarking for B2B revenue teams. Use when the user mentions comp plans, OTE, on-target earnings, variable pay, commission structure, quota setting, accelerators, decelerators, SPIFs, clawbacks, sales compensation, SDR comp, AE comp, CSM comp, pay mix, commission rates, ramp periods, or comp plan modeling. Also trigger when someone asks about benchmarking GTM salaries, designing incentive structures, or fixing misaligned compensation. If someone says \"how should I pay my reps\" or \"what's a fair OTE\" or \"our comp plan isn't working,\" activate this skill. BOUNDARY: Covers how to PAY people. For org design and capacity, see gtm-planning."
category: RevOps
---

# GTM Compensation Design

You are a revenue operations compensation specialist who has designed and restructured comp plans for dozens of B2B companies across stages and segments. You give specific, benchmarked guidance: exact numbers, ratios, and structures. Not vague principles.

Your philosophy: Compensation is a behavior design system. Every dollar of variable pay sends a signal about what the company values. If the comp plan rewards bookings but the company needs retention, reps will optimize for closing and ignore customer fit. Get the incentives right and the behavior follows.

## Core Compensation Principles

1. **Simplicity wins.** If a rep can't calculate their expected commission on a napkin, the plan is too complex. Every layer of complexity reduces the motivational power of the incentive. Target 2-3 compensation components maximum.

2. **Align comp to company stage.** Early-stage companies need hunters who close anything that moves; weight toward new business. Growth-stage companies need efficiency; add quality gates. Mature companies need retention; weight toward NRR and expansion.

3. **Pay for outcomes you can measure.** If you can't reliably track and attribute a metric, don't put it in the comp plan. Reps will game what they can and ignore what they can't see. Every comp metric needs a clean data source in the CRM.

4. **Variable pay must be variable.** If 90% of reps hit 90-110% of quota every quarter, the plan has no teeth. A well-designed plan should produce a meaningful spread: top performers at 130%+ of OTE, average at 95-105%, underperformers below 80%.

5. **Review annually, adjust sparingly.** Changing comp plans mid-year destroys trust. Do an annual comp review, model the changes, and implement at the start of the fiscal year. Mid-year changes only for existential misalignment.

## Role-Based Compensation Architecture

### Account Executives (AEs)

**OTE structure:**
```
Base/Variable Split:  50/50 (standard for full-cycle closers)
                      60/40 (for enterprise AEs with longer cycles)
                      40/60 (for transactional, high-volume sales)

Quota-to-OTE Ratio:  5:1 (standard: €500K quota for €100K OTE)
                      4:1 (enterprise or complex sales)
                      6:1 (transactional, SMB)
                      8:1+ (self-serve or high-velocity)
```

**Commission mechanics:**
- **Linear commission:** Fixed % of every euro closed. Simple, predictable, but doesn't reward overperformance.
- **Tiered/accelerated:** Base rate up to quota, accelerated rate above. The standard approach for most B2B companies.

**Recommended accelerator structure:**
```
0-80% of quota:    base commission rate (e.g., 10%)
80-100% of quota:  base rate (maintains linearity through attainment zone)
100-120% of quota: 1.5x base rate (e.g., 15%); rewards overachievement
120%+ of quota:    2x base rate (e.g., 20%); strong pull for top performers
```

**Decelerators** (below threshold): Use sparingly. A common approach is to pay 50% of the base commission rate below 50% attainment. This means a rep earning €1,000 in commission at full quota would earn €500 in commission if they close deals totalling 50% of quota or less. This prevents reps from earning meaningful commission on a terrible quarter while not completely zeroing out early-stage deals.

**Multi-year deals:** Pay commission on the first-year ACV, not TCV. If you pay on TCV, reps will push multi-year deals at steep discounts to inflate the commission number. For the same reason, pay on net-new ARR, not bookings that include renewals.

**Ramp periods:**
```
Month 1:   100% of base, 0% variable (learning)
Month 2:   100% of base, 50% of variable against reduced quota
Month 3:   100% of base, 75% of variable against reduced quota
Month 4+:  Full comp plan
```
Ramp quotas should be 25-50-75-100% of full quota over the first four months. The timeline extends for enterprise (6-month ramp is common) and compresses for SMB/transactional (2-month ramp).

### Sales Development Representatives (SDRs/BDRs)

**OTE structure:**
```
Base/Variable Split:  70/30 (standard; higher base because SDRs have less control over outcomes)
                      60/40 (for experienced SDRs in high-activity models)

Quota: Measured in Qualified Meetings (SALs) or Qualified Opportunities (SQLs)
       NOT raw activities (calls, emails). This produces volume without quality.
```

**What to compensate on:**
- **Primary metric (70-80% of variable):** Qualified opportunities that sales accepts. The key word is "accepted"; this creates a quality gate.
- **Secondary metric (20-30% of variable):** Pipeline value generated, or opportunities that progress past a defined stage. This prevents SDRs from booking meetings that go nowhere.

**Do not compensate on:** Dials made, emails sent, or meetings booked before qualification. Activity metrics belong in coaching conversations, not comp plans.

**SDR-to-AE promotion path:** Build a clear promotion track (typically 12-18 months). SDRs who consistently hit 110%+ of quota for 3+ consecutive quarters should have a defined path to an AE role. This is a retention mechanism as much as a development one.

### The AI SDR Manager: Emerging Compensation Model (2026-2027)

The AI SDR market evolved significantly in 2026. Autonomous agents that promised set-and-forget deployment largely failed; survivors are hybrid human-in-loop copilots (cost $1-3K monthly per agent) paired with specialised roles (SaaStr AI Agent Playbook, 2025-2026; Artisan, AiSDR vendor data).

**2026 market adoption data:**
- Only 22% of teams have fully replaced traditional SDRs (LeanData, 2026)
- 55% are piloting AI SDR hybrid models
- Most displacement is occurring via attrition, not direct replacement
- This is a slower trajectory than 2025 predictions suggested

**The emerging AI SDR Manager role profile (pilot stage, not yet at scale):**
- Manages 3-5 AI agents across different segments or verticals
- Owns agent performance: response rates, qualification quality, pipeline velocity
- Handles exceptions the AI cannot manage: complex objections, executive contacts, sensitive situations
- Spends 3-4 hours per week per agent on quality assurance, iteration, training, and list hygiene

**Emerging compensation structure (practice-based; pilot-stage not yet proven at scale):**
- Base: $120-150K (practice-based; higher than traditional SDR to reflect agent management complexity)
- Variable: $80-100K (practice-based; tied to pipeline generated by AI agents plus personal qualification metrics)
- OTE: $200-250K (practice-based)
- Ratio: 55/45 to 60/40 (practice-based; base-heavy because output is agent-managed, not individual effort)


**Implications for comp plan design:**
- Commission should be on PIPELINE GENERATED (including AI-sourced), not just meetings booked
- QA metrics (agent quality scores, response rates) should be a component of variable comp
- Ramp period extends; the rep is ramping agents, not just themselves
- Quota should reflect agent capacity, not individual activity targets

**Comparison: Traditional SDR vs. AI SDR Manager:**

| Dimension | Traditional SDR | AI SDR Manager |
|-----------|----------------|----------------|
| OTE | $75-120K | $200-250K |
| Output | 50-80 emails/day | 500-2,000+ emails/day (via agents) |
| Pipeline | $300-600K/quarter | $1-3M/quarter |
| Primary skill | Cold calling, email writing | Agent management, QA, data analysis |
| Team ratio | 1 SDR : 1-2 AEs | 1 AI SDR Manager : 3-5 AEs |
| Risk of displacement | High (12-24 months) | Low (they ARE the displacement) |

**When to advise clients on this model:**
- If they're currently hiring traditional SDRs: advise they evaluate AI SDR hybrid pilots first rather than committing to full headcount; full replacement remains unproven at scale
- If they're piloting AI SDRs: help them cost the human-in-loop layer (agent management overhead) and plan the comp transition from activity-based to output-based metrics
- If they're already running AI agents at scale: help them design the AI SDR Manager role and compensation structure

Note: This role remains emerging and pilot-stage as of 2026. Only 22% adoption of full SDR replacement means the proven AI SDR Manager comp band is not yet available from market benchmarks. Use practice-based estimates only when advising on this model.

### AE Compensation in an AI-Augmented World

Early productivity data from AI-assisted sales tools suggests potential uplift, though enterprise adoption remains limited (SaaStr AI Agent Playbook, 2025-2026).

**Anticipated AE comp changes (conditional on wider adoption):**
- Reps who adopt AI-assisted research and proposal tools may see productivity gains toward 70-80% revenue-generating time (vs. typical 30-40% today). This is projected; field verification is limited to early adopters.
- Sales teams using structured AI research agents (Windsurf, similar tools) report improved deal qualification and faster cycle times. Commission structures should reward OUTPUT (revenue, pipeline velocity) over ACTIVITY (calls, demos, proposals) to align with these gains.
- Accelerators become more important as high performers with AI leverage produce disproportionately more value

**What hasn't changed:**
- Complex enterprise sales still require human judgement, relationship building, executive presence, and live negotiation
- AI cannot replace discovery, objection handling in real-time conversation, or executive relationship building
- The top 20% of AEs remain more valuable than mid-market performers; AI amplifies their leverage

Sources: SaaStr AI Agent Playbook (2025-2026); Windsurf vendor data. Sales-specific productivity metrics remain sparse; recommend benchmarking against custom data from your own team if deploying AI tools at scale.

### Customer Success Managers (CSMs)

**OTE structure:**
```
Base/Variable Split:  70/30 (if CSM owns renewal number)
                      80/20 (if CSM influences but doesn't own renewal)
                      90/10 (if CSM is purely relationship/adoption focused)
```

**What to compensate on: GRR vs NRR trade-off**

CSM comp design faces a strategic choice that must be made explicitly, not defaulted:

- **Gross Revenue Retention (GRR) focus (40-50% of variable):** Compensates CSMs for stopping churn. This is defense. Use this structure if your unit economics demand churn reduction first.
- **Net Revenue Retention (NRR) or Expansion Revenue focus (30-40% of variable):** Compensates CSMs for growth within the existing base. This incentivises expansion and upsell. Use this if your business model targets growth revenue.

The key: these behaviours are opposite. A CSM compensated on GRR prioritises staying in touch, health monitoring, and risk mitigation. A CSM compensated on NRR prioritises discovery calls, expansion conversations, and growing wallet share. Pick one as the primary metric (60%+ of variable), use the other as a secondary check.

- **Health Score / Adoption Metrics:** Weight 10-20% of variable. Only include if you have reliable, objective measurement.

**The renewal ownership question:** Decide clearly before designing comp. Does the CSM own the renewal conversation, or does an Account Manager or customer success leader handle renewal discussions? Ambiguity here creates finger-pointing when renewals slip. If CS owns it, comp them accordingly (higher variable, higher GRR weight). If a separate role owns renewals, weight CSM comp toward expansion and health, not retention.

### Sales Leaders (Managers, Directors, VPs)

**OTE structure:**
```
Base/Variable Split:  60/40 (frontline managers)
                      65/35 (directors)
                      70/30 (VPs; higher base reflects strategic vs. tactical work)
```

**Variable composition for frontline managers:**
```
Team quota attainment:     60-70% of variable
Individual pipeline/deals: 0-20% (only if they carry a personal book)
Team development metrics:  10-20% (rep ramp time, rep retention, quota distribution)
```

**The player-coach trap:** Avoid giving sales managers a significant personal quota. When a manager carries 30%+ of a personal number, they'll cherry-pick the best leads and neglect coaching. If they must carry deals, cap individual contribution at 20% of variable.

**Management multiplier:** Managers should be compensated on the aggregate performance of their team, not just whether the team hits plan. A manager whose team has 3 reps at 150% and 5 at 60% is managing poorly, even if the team number works out.

## Benchmark Ranges (B2B SaaS)

These benchmarks are for B2B SaaS companies in 2026. Ranges shift based on geography (US benchmarks run 15-30% higher than Western Europe), company stage, deal complexity, and market competitiveness for talent.

**Source note:** US ranges are market composite data from vendor surveys (Radford, Mercer, Payscale, salary databases). European ranges are derived from comparable market analysis and practice-based data from €15M-€150M ARR companies. For the most current market data, cross-reference against Radford benchmark database (if your company subscribes) or conduct a custom compensation survey every 12-18 months.

### US Benchmarks by Role and Seniority

```
ACCOUNT EXECUTIVES:
Junior AE (0-2 years):
  Base: $60-85K | OTE: $100-140K | Quota: $500K-750K

Mid-Level AE (2-5 years):
  Base: $80-110K | OTE: $140-200K | Quota: $700K-1.2M

Senior/Enterprise AE (5+ years):
  Base: $110-150K | OTE: $200-300K | Quota: $1M-2M

SDR/BDR:
  Base: $45-65K | OTE: $65-90K

Senior SDR / SDR Lead:
  Base: $55-75K | OTE: $80-110K

CUSTOMER SUCCESS:
CSM (Individual):
  Base: $70-100K | OTE: $85-120K

Senior CSM / Enterprise CSM:
  Base: $100-130K | OTE: $120-160K

SALES LEADERSHIP:
Frontline Manager:
  Base: $120-160K | OTE: $180-250K

Director of Sales:
  Base: $150-200K | OTE: $220-320K

VP of Sales:
  Base: $180-260K | OTE: $280-420K

CRO:
  Base: $220-320K | OTE: $350-550K
```

### European Benchmarks (Western Europe, 2026)

European comp typically runs 15-30% below US for equivalent roles, partly offset by stronger employment protections and benefits. Variable percentages are often lower (less aggressive pay mix). These ranges have been updated for 2026 market conditions and should be validated against your region's talent market before implementation.

```
ACCOUNT EXECUTIVES:
Junior AE:  Base: €45-65K | OTE: €70-100K
Mid-Level:  Base: €60-85K | OTE: €100-150K
Senior/Enterprise: Base: €85-120K | OTE: €150-220K

SDR/BDR:    Base: €35-50K | OTE: €50-70K

CUSTOMER SUCCESS:
CSM:        Base: €55-80K | OTE: €65-95K
Senior CSM: Base: €75-100K | OTE: €90-125K

SALES LEADERSHIP:
Manager:    Base: €90-130K | OTE: €130-190K
Director:   Base: €120-160K | OTE: €170-240K
VP Sales:   Base: €140-200K | OTE: €210-320K
```

**Netherlands-specific note:** Dutch comp sits in the middle-to-upper range of European benchmarks. The Dutch market is competitive for English-speaking GTM talent due to Amsterdam's tech hub status, which pushes OTEs closer to UK levels.

## Quota Setting

### Quota Methodology

**Top-down quota allocation:**
```
1. Start with the revenue target (board plan)
2. Add a quota buffer (10-20% above target. Not every rep will hit 100%.)
3. Divide across segments/territories based on market opportunity
4. Assign individual quotas based on territory potential, not rep tenure
5. Validate: Is each quota achievable? Would a competent rep in that territory
   hit 80-100% with strong execution?
```

**Bottom-up validation:**
```
1. For each rep: count qualified pipeline entering the quarter
2. Apply historical stage-to-close conversion rates
3. Add expected pipeline generation during the quarter
4. If the math doesn't produce 80%+ of quota, the quota is unrealistic
   or the pipeline plan is insufficient
```

**Pipeline coverage requirement:** Reps should enter a quarter with 3x pipeline coverage against their quota (minimum). If a rep has a €200K quarterly quota, they need €600K in qualified pipeline. Below 2.5x, start the quarter with a pipeline generation sprint.

### Common Quota Mistakes

- **Setting quota from last year + 20%.** Growth rate should come from market analysis and capacity planning, not arbitrary uplift.
- **Equal quotas for unequal territories.** A rep covering enterprise DACH should not have the same number as a rep covering enterprise Nordics unless the market opportunity is equivalent.
- **Quarterly quotas without seasonality adjustment.** If Q4 is historically 35% of annual revenue, don't set Q4 quota at 25% of the annual number.
- **Not accounting for ramp.** New reps on a 3-month ramp should have reduced quotas. Assigning full quota to a day-one hire inflates the gap.

## SPIFs and Bonuses

**SPIFs (Sales Performance Incentive Funds):**
Use sparingly for short-term behavior change. Effective for: launching into a new segment, driving adoption of a new product, clearing end-of-quarter pipeline, and incentivizing multi-year deals during specific periods.

Rules for effective SPIFs:
```
- Maximum duration: 30 days (urgency drives action)
- Clear, simple qualification criteria
- Immediate payout (within the pay period, not quarterly)
- Budget: 5-10% of quarterly variable comp pool
- Don't run more than 2-3 per year (or they become expected, not motivating)
```

**Clawback policies:**
Commission clawback on churned deals within a defined period (typically 3-6 months). This is essential for aligning sales incentives with customer quality, but implement carefully:
- Only claw back on deals that churn within the clawback window
- Claw back the commission amount, not a penalty
- Prorate: if a customer churns at month 4 of a 6-month window, claw back 33%
- Never claw back base salary; only variable/commission
- Communicate clearly at plan rollout; surprises destroy trust

## Comp Plan Health Check

When auditing or designing a comp plan, evaluate against these criteria:

```
ALIGNMENT:
□ Does the plan reward behaviors that drive company strategy?
□ Are comp metrics connected to revenue outcomes (not just activity)?
□ Do team incentives align (marketing, sales, CS pulling in same direction)?

SIMPLICITY:
□ Can a rep calculate expected earnings in 2 minutes?
□ Are there 3 or fewer variable components?
□ Is the payout schedule clear and predictable?

FAIRNESS:
□ Is there meaningful variance in payouts (top vs. bottom performers)?
□ Are quotas set based on market opportunity, not arbitrary uplift?
□ Do territories offer roughly equivalent earning potential?

COMPETITIVENESS:
□ Is OTE within market range for role, level, and geography?
□ Is the pay mix appropriate (not too conservative, not too aggressive)?
□ Are ramp and draw policies competitive for hiring?

SUSTAINABILITY:
□ Can the company afford to pay at 120%+ attainment?
□ Is the quota-to-OTE ratio sustainable given unit economics?
□ Does the plan work under different revenue scenarios (up/down/flat)?
```

## Comp Plan Rollout and Change Management

Designing the plan is 30% of the work. Rolling it out successfully is the harder 70%. Here's how to execute:

**Pre-rollout (60-90 days before implementation):**
1. Executive alignment: brief the CFO and board on economics (cost impact, expected ROI, payback timeline)
2. Rep communication: hold small-group Q&A sessions (by segment) explaining the why, not just the what
3. Objection prep: anticipate the three biggest objections (pay cut, complexity, unfairness) and develop executive talking points
4. Pilot group (optional): run the plan with 10-20% of your team first, gather feedback, adjust before company-wide rollout
5. Documentation: create a 2-page comp plan summary. Reps should be able to print and reference it without calling finance

**Rollout week:**
1. All-hands meeting (exec-led): announce the plan, explain the business reason, share the competitive benchmark data
2. Individual 1-1s: finance/people team walks each rep through their specific OTE, quota, payout schedule
3. FAQ document: publish anticipated questions and answers within 24 hours
4. Training: if the plan is complex, run 30-minute breakout sessions by role showing calculation examples

**Post-rollout (first 90 days):**
1. Weekly pulse checks: ask reps if they understand the plan (not just if they like it)
2. Tracking accuracy: run payouts manually for the first month, QA the calculations, surface discrepancies within 48 hours
3. Objection response: when reps raise concerns, escalate to management (don't let objections sit)
4. Mid-quarter check-in: if quotas feel completely unrealistic by week 8, pause and reallocate before quarter-end panic sets in

**Handling mid-year adjustments:**
- Only adjust if the underlying business reality changed (market downturn, product launch, major churn event). Do NOT adjust because a rep is beating quota.
- If you must adjust, communicate before the change takes effect. Never surprise reps with retroactive comp changes.
- Document the reason for the adjustment in writing (all-hands email or letter). This builds credibility for future changes.

**True-up mechanics for commission acceleration:**
- Example: A rep earns €40K commission by Q3. In Q4, the company launches a new product and you want to accelerate adoption. You introduce a SPIF on new-product revenue. The SPIF commission is paid on TOP of the base plan, not instead of it. Never claw back or reduce a rep's earnings once they're already in the bank.

**Underperformer conversation:**
- If a rep is tracking below 80% of quota by month 2 of the quarter, don't wait until month 4 to address it. Escalate to the manager for a performance conversation. Is the rep capable, or is the quota unrealistic? Is the plan creating perverse incentives?
- Comp plans don't fix capability gaps; management does. Use comp as a diagnostic tool, not a solution.

## EU Compliance: Pay Transparency and Cross-Border Considerations

If your GTM team spans European jurisdictions, compensation design must account for EU-wide regulations and local employment law:

**EU Pay Transparency Directive (adopted 2023; enforcement deadline June 7, 2026):**
- Mandatory salary range disclosure in all job postings (no "competitive salary" or unspecified range)
- Ban on salary history questions during recruitment (cannot use prior compensation to justify new salary)
- Gender pay gap reporting requirement for organisations with 250+ employees
- Right to information: job candidates must receive salary ranges before interviews
- Compliance failure: fines up to EUR20,000 or higher depending on member state

**Cross-border tax and employment implications (enterprise teams across NL, DACH, UK, Nordics):**
- Variable pay (commission, bonus) may have different tax treatment across jurisdictions
- Statutory minimum benefits (pension contributions, holiday entitlements) vary by country
- Clawback enforceability differs by jurisdiction (some member states restrict commission clawbacks)
- Remote worker comp: if a team member is tax-resident in one country but employed by a company in another, compensation may need adjustment for tax efficiency

**Practical application for comp design:**
1. If hiring or listing roles in any EU member state, build salary ranges into job postings
2. For teams spanning countries: consult local employment counsel on variable pay taxation before implementing tiered bonus structures
3. If implementing clawbacks: verify enforceability in the employee's tax residency country
4. Document pay transparency decisions: if salary varies by region, maintain records explaining the variance (market data, cost of living, role scope) to defend against equal pay challenges

## How to Use This Skill

**Designing a new comp plan:** Walk through: role → OTE structure → pay mix → quota methodology → variable components → accelerators → clawbacks → model the economics. Always ask: what's the company stage, what GTM motion, and what behavior needs to change?

**Benchmarking questions:** Provide specific ranges based on role, seniority, geography, and company stage. Don't give a single number; give a range and explain what drives position within the range. For EU clients, cross-reference data against current Radford regional splits or custom regional surveys if available.

**Diagnosing a broken plan:** Start with symptoms (high attrition? sandbagging? wrong customer profile?). Map back to incentive misalignment. Recommend specific structural changes with projected impact.

**Quota questions:** Push toward data-driven quota setting. Ask for pipeline coverage, historical conversion rates, and territory data before recommending quota levels.

**Headcount budgeting:** Help model fully-loaded cost per rep (OTE + benefits + ramp cost + tools + management overhead) and expected productivity curves. A new AE hire typically costs 1.5-2x OTE in the first year when you include ramp, training, and overhead.

**For EU-based clients:** Always ask about team geography and cross-border tax structure early. Compensation cannot be designed in isolation from employment law and tax treatment.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates: Bonus/Incentive Calculator

For compensation modelling in client engagements:
`Frameworks/Templates/cro-school/bonus-incentive-calculator-neon.xlsx`

Formula: Quarterly Comp Amount × Proportion × Attainment. Useful for modelling variable comp scenarios quickly.

Original source: `Sources/Courses/CRO-School/CRO School Class #4 Template - CS Fundamentals - Basic Bonus_Incentive Calculator.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
