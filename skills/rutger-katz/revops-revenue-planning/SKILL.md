---
name: "revops-revenue-planning"
title: Revenue planning
description: "Annual and quarterly revenue plan construction, top-down vs bottoms-up reconciliation, plan versioning, stretch goal handling, and FP&A-RevOps collaboration for B2B revenue teams. Use when the user mentions annual planning, revenue targets, capacity planning, planning calendar, stretch goals, plan versions, plan of record, reforecasting triggers, FP&A collaboration, or revenue reconciliation. Also trigger on \"we need to build our plan\", \"our forecast and budget don't align\", \"how do we set targets\", \"what's our plan of record\", \"we got a stretch from finance\", \"when should we start planning\", or \"we need to reforecast\". BOUNDARY: Covers plan construction, versioning, and reconciliation. For in-quarter/weekly forecasting mechanics, see revops-forecasting. For GTM structure and capacity mechanics, see gtm-planning. For compensation and quotas, see gtm-compensation."
category: RevOps
---

# Revenue Planning

You are a revenue planning architect who has built annual and quarterly plans at B2B companies from €5M to €200M ARR. You know the gap between what salespeople tell you they can produce and what the board wants to see, and you know how to bridge that gap with rigour and transparency.

Your philosophy: Revenue planning is not a board presentation exercise. It is a commitment contract between your revenue team, your finance team, and your market. The plan of record is the single source of truth. Everything else (working plans, scenarios, stretch analysis) serves that truth. A plan that sales owns and can defend is more valuable than a perfect plan that sales does not believe in.

## Core Planning Principles

1. **Bottoms-up first, then top-down.** The team builds from current capacity and known account pipeline. Finance adds ambition. You reconcile the gap with named scenarios, not by spreading a number across teams unilaterally. Start with reality, then improve it.

2. **Separate three questions.** What can we produce? (capacity model, bottoms-up). What do we want to produce? (strategic target). What does the market allow us to produce? (market opportunity, ICP sizing). Three separate analyses; three separate answers. Conflating them creates noise, not clarity.

3. **Version control is non-negotiable.** Original bottoms-up plan, finance stretch iteration, final plan of record: all three survive in the vault. Every mid-year reforecast preserves the prior baseline. This is not bureaucracy; this is audit trail and learning.

4. **Stretch targets are scenarios, not directives.** When finance adds a target above bottoms-up, that stretch becomes a named scenario with owners and explicit assumptions (new hiring, productivity gains, expansion acceleration, churn reduction, pipeline investments). A stretch without owners is a wish disguised as a plan.

5. **Reforecasting is disciplined, not reactive.** Specific triggers (coverage below 3x, CAC payback above threshold, NRR drop below 105%, actual variance exceeds plan by 15% for two consecutive periods) drive reforecasts. The calendar blocks reforecasting windows. Continuous re-planning creates chaos and erodes ownership.

6. **FP&A and RevOps are joint decision-makers, not separate processes.** RevOps owns pipeline reality and call quality. FP&A owns financial implications. A forecast that doesn't reconcile across both functions gets revised, not approved.

## Annual Planning Calendar

Revenue planning is a backwards-timeline exercise. Fiscal close-out, budget finalisation, and board approval all anchor the schedule. Build backwards from there.

### Planning Calendar Template (12-Week Cycle)

For a calendar-year business (plan finalised Dec 31, approved Nov, in-market Jan 1):

```
PHASE 1: DATA & RETROSPECTIVE (Weeks 1-2, August)
  Week 1 (Aug 5-9):    Retrospective inputs pulled (prior year close-out, current-year variance)
  Week 2 (Aug 12-16):  Team input window opens (sales capacities, market intel, customer feedback)

PHASE 2: BOTTOMS-UP BUILD (Weeks 3-5, mid-August through early Sept)
  Week 3 (Aug 19-23):  Account planning by segment (current ARR + known expansion + new business pipeline)
  Week 4 (Aug 26-30):  Capacity model: new hires, ramp periods, retention assumptions
  Week 5 (Sep 2-6):    Segment totals rolled up; bottoms-up revenue plan drafted

PHASE 3: TOP-DOWN & RECONCILIATION (Weeks 6-8, mid-September)
  Week 6 (Sep 9-13):   Finance top-down model shared; comparison against bottoms-up
  Week 7 (Sep 16-20):  Reconciliation meeting(s): gap analysis, named scenarios, stretch owners assigned
  Week 8 (Sep 23-27):  Revised plan incorporating scenarios; finance models impact (hiring, spend, working capital)

PHASE 4: VALIDATION & FINALISATION (Weeks 9-10, early October)
  Week 9 (Sep 30-Oct 4):   Executive alignment; SPICED assumptions validated against pipeline
  Week 10 (Oct 7-11):      Plan of Record locked; FP&A sensitivity analysis; board narrative drafted

PHASE 5: BOARD & APPROVAL (Weeks 11-12, mid-October)
  Week 11 (Oct 14-18):     Board materials finalised; executive alignment on narrative
  Week 12 (Oct 21-25):     Board presentation; plan approved; budget allocation to departments begins

BUFFER: (Oct 28-Nov 1)     Post-approval implementation; sales enablement; quota setting; incentive finalisation
```

**Key dates to set first:** Board approval date (locked), then work backwards. This calendar assumes 12 weeks. Compressed cycles (8-10 weeks) compress data gathering or validation; they should not compress reconciliation.

For a fiscal-year business (e.g. April 1 start), shift the calendar backwards by the month delta (e.g. April plan = start 4 January, board approval early March).

See `references/planning-calendar-checklist.md` for guardrails per phase and a template for customisation to your fiscal year.

## The Bottoms-Up Build Process

Bottoms-up planning is not a line-by-line forecast. It is a capacity-grounded estimate of what the team should produce given known constraints and opportunities.

### Step 1: Account Segmentation and Current ARR Baseline

Segment accounts by tier (SMB / Mid-Market / Enterprise) and revenue type (New Business / Expansion / Renewal). Baseline current ARR or bookings by segment.

```
Segment          Current ARR    % of Total
-------------------------------------------
New Business     €2.5M           40%
Expansion        €2.2M           35%
Renewal          €1.3M           21%
  Total          €6.0M          100%
```

### Step 2: Capacity Model (per gtm-planning reference)

The capacity model calculates what a team should produce from headcount, ramp, quota, and productivity assumptions. The formula:

```
Annual Bookings Target = (Available Full-Time Reps) × (Ramp Factor) × (Annual Quota)

EXAMPLE:
  7 FTE Account Executives
  Average ramp: 3 new hires × 80% (ramping) + 4 tenured × 100% = 6.4 effective FTE
  Annual quota per AE: €850K
  Annual bookings capacity = 6.4 × €850K = €5.44M

Adjust by:
  + Expansion ARR from existing customer base (typically 15-20% incremental)
  + Inbound/self-sourced pipeline (typically 10-30% pipeline contribution)
  = Total revenue capacity
```

For the full capacity-model calculator (including SDR ratios, territory balance, retention assumptions), see `references/bottoms-up-build-recipe.md`.

### Step 3: Known Opportunity Pipeline Overlay

Audit CRM for booked/named deals at or above threshold (e.g. >€50K ACV). These deals have confirmed timelines and advance/close probabilities higher than blended averages.

```
Named Pipeline Analysis (next 6 months):
  Deal A (SMB inbound):        €45K, 70% probability, Sep close
  Deal B (Enterprise):         €180K, 50% probability, Oct close
  Deal C (Expansion):          €120K, 85% probability, Aug close
  ---
  Total named pipeline:        €345K
  Expected close (prob-weighted): €243K
```

Overlay this against bottoms-up. If named pipeline significantly exceeds capacity-model expectations, document the delta and source. If named pipeline falls short, that is your pipeline-generation gap for the year.

### Step 4: Segment-Specific Growth Assumptions

Build distinct assumptions per revenue type:

**New Business:** Most variable. Bottoms-up = capacity model × historical attach rate per AE. Adjust for known customer losses (churn from prior year) and new market entries.

**Expansion:** More predictable. Bottoms-up = current expansion ARR × (1 - churn rate) × (1 + expansion rate). Example: €2.2M expansion ARR × 92% retention × 1.12 growth = €2.87M.

**Renewal:** Most predictable. Bottoms-up = current renewal ARR × gross-retention rate. Example: €1.3M renewal ARR × 97% = €1.26M.

Sum segment bottoms-up for company total.

### Step 5: Document All Assumptions in a Shared Sheet

Create a single source of truth for assumptions so finance can validate and challenge:

```
Assumption                          Value       Source/Owner         Confidence
------------------------------------------------------------------------
Renewal GRR                         97%         CS retention data     HIGH
Expansion growth rate               12%         prior 3-year trend    MEDIUM
New biz AE capacity                 €850K       quota × ramp model    MEDIUM
SDR pipeline contribution           35%         current pipeline mix  MEDIUM
Inbound:Outbound mix                40:60       sales sourcing audit  LOW
New hires (net)                     2           hiring plan approved  HIGH
CAC payback expected                13 months   prior year actuals    MEDIUM
```

This sheet is the contract between Revenue and Finance. For the template, see `references/planning-assumptions-template.md`.

## Top-Down Forecasting and Reconciliation

Finance typically builds a top-down target derived from company growth strategy, board expectations, or fundraising narratives. The reconciliation meeting compares bottoms-up against top-down and closes the gap.

### The Reconciliation Meeting Playbook

**Pre-meeting (Finance prepares):**
- Top-down target (e.g. "We need €8.5M in new bookings")
- High-level drivers ("20% YoY growth, 10% market expansion, 5% win-rate improvement")
- Sensitivity analysis (what if growth is 15%? 25%?)

**Meeting structure (90 min):**

1. **Set the frame (5 min).** This is not a negotiation. This is a diagnostic. We have two independent analyses. Where they converge, we have high confidence. Where they diverge, something is true we need to learn.

2. **Present bottoms-up (20 min).** Segment-by-segment breakdown. Capacity model with assumptions highlighted. Named pipeline overlay. Total: €7.8M.

3. **Present top-down (10 min).** Strategic target. Drivers. Sensitivity. Total: €8.5M.

4. **Close the gap (40 min).** Gap = €700K (€8.5M - €7.8M). Work through scenarios:
   - **Scenario A: Additional hiring.** If we hire 2 net new AEs in Q1 (6-month ramp), capacity adds ~€350K. Owner assigned.
   - **Scenario B: Expansion acceleration.** If we invest €150K in customer success and expand faster, uplift +€250K. CS + GTM owners assigned.
   - **Scenario C: Pipeline generation investment.** If we dedicate additional ABM spend, create +€100K in new-business pipeline. Marketing owner assigned.
   - **Total uplift: €350K + €250K + €100K = €700K.** Closes gap.

5. **Lock plan of record (10 min).** €8.5M plan now has:
   - €7.8M base (bottoms-up capacity)
   - €0.7M stretch (Scenario A/B/C with named owners and dependencies)

6. **Document scenarios and owners (5 min).** Creates accountability. If hiring slips, the plan adjusts. If CS expansion doesn't materialise, the plan adjusts.

**Post-meeting:** Distribute Plan of Record to entire revenue organisation. Every rep, manager, and CFO knows the single agreed number.

For the full playbook (including conflict resolution patterns, what to do if the gap cannot close, and how to handle a stretch the team believes is unrealistic), see `references/reconciliation-playbook.md`.

## Plan Versioning and Governance

Three versions must exist and persist:

**Version 1: Bottoms-Up Original (BO)**
- Drafted by Revenue in Weeks 3-5
- File path: `annual-plan-2026-bottoms-up-original.md`
- Status: Locked after reconciliation; never overwritten

**Version 2: Finance Stretch Iteration (FS)**
- Top-down target plus assumptions
- File path: `annual-plan-2026-finance-stretch.md`
- Status: Locked after reconciliation; used as comparison baseline for reforecasts

**Version 3: Plan of Record (POR)**
- Final agreed plan with scenarios documented
- File path: `annual-plan-2026-plan-of-record.md`
- Status: Single source of truth; all teams execute against this number

**Reforecasts (monthly or quarterly):**
- File path: `annual-plan-2026-reforecast-M5.md` (Month 5) or `annual-plan-2026-reforecast-Q2.md`
- Status: Compares current projection against POR and original BO
- Preserved permanently for audit trail

**Example comparison during M5 reforecast:**
```
Plan of Record (POR):        €8.5M
Bottoms-Up Original (BO):    €7.8M
Current Forecast (M5):       €7.9M
Variance from POR:           -€0.6M (down 7%)
```

This structure enables learning: why is the forecast down? Did pipeline generation miss? Did deals slip? Did assumptions break?

For the full governance template (access controls, approval gates, version-numbering conventions), see `references/plan-versioning-governance.md`.

## Reforecasting: Triggers, Cadence, and Constraints

Reforecasting is not continuous re-planning. It is disciplined re-evaluation on a fixed schedule or when specific triggers fire.

### Standard Cadence

**Monthly:** Lightweight review (1 hour). Compare current forecast vs Plan of Record. Flag material variances (>±10% from POR) for deeper analysis.

**Quarterly:** Full reforecast (4 hours). Update all assumptions; recalculate segment forecasts; reconcile across Revenue and Finance; document scenario changes.

**On trigger:** Full reforecast within one week of trigger firing.

### Reforecasting Triggers

A trigger fires when a business condition changes materially. At that point, the planning team (Revenue + Finance) has 5 business days to reforecast and update the Plan of Record.

**Revenue-side triggers:**
- Pipeline coverage falls below 2.5x (leading indicator of revenue miss)
- Month-end close rate drops below 60% of plan (execution signal)
- Forecast accuracy variance exceeds ±20% for two consecutive months (process signal)
- Named-deal slippage exceeds 50% (pipeline health signal)

**Unit-economics triggers:**
- NRR drops below 105% (retention signal)
- CAC payback period exceeds 14 months (acquisition economics signal)
- Gross margin erodes below plan by >3% (delivery signal)

**Execution triggers:**
- Actual revenue variance from plan exceeds 15% for two consecutive periods
- Headcount hiring plan slips (capacity constrained)
- Major customer churn event (€500K+ ARR loss)

**External triggers:**
- Competitor disruption affecting win rate
- Macro economic condition change with material impact (recession, credit freeze)
- Product release delay affecting pipeline (6+ week slip)

See `references/reforecasting-triggers.md` for the full matrix, examples, and the specific reforecast process per trigger type.

### What May NOT Change Mid-Year

**Locked parameters (never reforecast):**
- Quota targets (change only at annual reset)
- Headcount plan (hiring pace committed to board; changes only with board discussion)
- Compensation structure (changes create rep chaos; reserve for annual refresh)
- Strategic positioning or ICP definition (changes only with GTM strategy refresh, not in-year)

**Flexible parameters (reforecast freely):**
- Revenue target (adjusted up or down based on actual vs plan)
- Pipeline assumptions (conversion rates, velocity, mix)
- Stretch scenario owners (reassigned if dependencies shift)
- Reforecast cadence itself (can adjust from monthly to quarterly if business stabilises)

Mixing locked and flexible parameters is the primary cause of reforecasting chaos.

## Benchmarks: When to Trigger a Full Reforecast

**Pipeline Coverage Benchmarks:**
- Below 2.5x: Critical; reforecast immediately
- 2.5x to 3.0x: At-risk; escalate and plan pipeline generation response
- 3.0x to 3.5x: Healthy baseline
- 3.5x+: Strong (banding is a practice-based threshold informed by Ebsta slippage data: 36% deals slip quarterly, 50% best-case close rate)

**Forecast Accuracy Benchmarks (Monthly Actuals vs Month-Start Forecast):**
- ±5%: Elite (only 7% of companies reach 90%+ accuracy; Gartner via ORM Technologies, 2025)
- ±10%: Strong; ±15-20%: Normal; ±25%+: Process broken, structural fix required (practice-based banding, informed by the Ebsta 2025 accuracy distribution)

**Quota Attainment Benchmarks (Rep-Level Performance):**
- Healthy: 70-80% of reps hit quota (aspirational target)
- Median market: 46% of reps hit quota in 2025, down from 52% in 2024 (Ebsta 2025 GTM Benchmarks Report)
- Signal: If below 50% organisation-wide, quota-setting process is flawed (Canaani, Revenue Leadership Podcast E64, 2026)

**Reforecasting Frequency Boundaries:**
- Minimum: Quarterly (prevents total disconnect between plan and reality)
- Maximum: Weekly (creates organisational paralysis; FP&A overhead becomes unsustainable)
- Standard: Monthly operational reviews + quarterly full reforecasts (Fincome, 2025)

See `references/reforecasting-benchmarks.md` for the full matrix and when each trigger fires.

## FP&A and RevOps Collaboration Model

The strongest revenue organisations operate with joint FP&A and RevOps ownership of the forecast and plan.

**RevOps role:** Pipeline operator. Owns deal inspection, forecast categories, stage accuracy, pipeline health, sandbagging detection, and the weekly forecast call.

**FP&A role:** Financial modeller. Owns cash implications, working capital, burn forecasts, expense budgets, and board narrative.

**Joint decisions:**
- Plan of Record: both sign off
- Reforecasts: both validate triggers and scenarios
- Stretch scenarios: RevOps owns feasibility, FP&A owns financial modelling
- Headcount plan: RevOps owns capacity math, FP&A owns cost allocation

**Weekly sync (30 min):** Any material forecast change or pipeline signal gets flagged immediately. Prevents surprise reforecasts. Builds trust.

**Reconciliation meeting (quarterly):** Full top-down vs bottoms-up recalibration. Both functions debate assumptions openly. Resolution via data, not politics.

For the full collaboration charter (including conflict-resolution protocols, escalation triggers, and the meeting templates), see `references/fpa-revops-collaboration-charter.md`.

## AI-Native Revenue Planning (2026)

As of 2026, AI forecasting and deal scoring are table-stakes for mature RevOps practices. Organisations that embed AI into planning see variance reduction from 30-40% to under 10% (Forrester, 2026). Plan integration points:

**AI Forecasting Platforms:**
- Gong Forecast integrates CRM automation and AI deal-health assessment; feeds directly into plan variance triggers
- Salesforce Agentforce Revenue Management (successor to CPQ) includes predictive forecasting and pipeline shaping
- HubSpot Revenue Intelligence (native to Operations Hub) surfaces deal risk and close probability by deal stage
- These platforms replace manual rep calibration; their outputs should inform your reforecasting triggers

**Operational pattern:** Monthly forecast call structure changes when AI is active. Instead of rep-by-rep challenge, the agenda becomes: "Which deals flagged by AI need RevOps intervention?" AI surfaces outliers; humans diagnose and escalate. Expected outcome: 15-25% reduction in forecast surprise (deals slipping unexpectedly).

**CRM Automation for Plan Execution:**
- Reverse ETL platforms (Hightouch, Census) enable automated pipeline snapshots to feed your planning models. Example: Every morning at 05:00, deal stage, probability, close date, and deal age sync to a planning sheet. RevOps sees velocity drift within 24 hours, not 30 days later.
- Automated trigger detection: Workflow rules flagging stale deals (>45 days in same stage), coverage drops (pipeline below 2.5x), close-rate signals (forecast variance >20% month-to-date). These fire immediate escalations to RevOps, shortening diagnostic cycle from 5 days to hours.

**Planning for AI-Native Go-to-Market Models:**
- AI SDRs (hybrid human-in-loop, production-ready in 2026: AiSDR, Artisan, Amplemarket) shift pipeline-generation assumptions. Cost per AI SDR: EUR 1-3K monthly vs EUR 7.5-10.8K human (2026; cost parity case-dependent on list quality and ICP fit). Traditional capacity models assume X SDR:AE ratios; hybrid models should cost-model both motions and assume AI SDRs at 15-35% of human salary cost. Update your headcount plan to reflect blended human and AI pipeline generation.
- Agent-assisted reps (autonomous deal scoring, next-best-action recommendations) increase quota attainment in mid-market. Budget for sales enablement tools (Salesforce Data 360, HubSpot Segment Analytics) in your GTM efficiency line.

---

## Diagnostic: 10 Questions That Expose Broken Planning Processes

Walk through these 10 questions. If you answer "No" or "Unknown" to any, that function is a process risk.

1. **Do you have a formal planning calendar with locked dates for each phase (bottoms-up, reconciliation, board approval)?**
   - No = Planning happens ad-hoc; reforecasts are reactive

2. **Can you produce the bottoms-up plan without Finance input, using only capacity and pipeline data?**
   - No = You don't know what the team can actually produce independent of aspirations

3. **Do you preserve three versions of the plan: original bottoms-up, finance stretch, and plan of record?**
   - No = You cannot diagnose variance or learn from plan misses

4. **Can you explain every €1 of stretch target with a named scenario, an owner, and explicit assumptions?**
   - No = The stretch is a wish, not a plan

5. **Does every reforecast compare current projection against Plan of Record AND against the original bottoms-up?**
   - No = You cannot see if you missed capacity or if execution slipped

6. **Have you documented what may NOT change mid-year (quota, headcount plan, comp structure)?**
   - No = Reforecasting will cascade into chaos and erode team ownership

7. **Do FP&A and RevOps jointly review every material forecast change together, in real time?**
   - No = One function surprises the other; plans get unravelled mid-quarter

8. **Can you articulate the specific triggers that would force a reforecast (coverage drop, CAC payback, NRR decline, variance threshold)?**
   - No = You reforecast reactively or continuously; no discipline

9. **Do your reps know the plan of record and understand their segment targets and expansion opportunities?**
   - No = The plan exists for the board, not to drive behaviour

10. **When the plan misses, can you trace the miss to a specific assumption (retention, deal size, pipeline generation, productivity) rather than blaming execution or market?**
    - No = You are not learning from misses; next year's plan will repeat the errors

**Scoring:** 8-10 Yes answers: Strong planning discipline. 5-7: Process gaps exist; tackle them in the next planning cycle. Fewer than 5: Plan the planning process itself before tackling revenue targets.

See `references/planning-diagnostic-full.md` for the detailed interpretation guide and remediation playbook per question.

---

## How to Use This Skill

**"We need to build our annual plan from scratch."** Start with the planning calendar (backwards from board approval date). Then run the bottoms-up build (Sections 2.1-2.4). Overlay capacity model from gtm-planning. Then reconcile against top-down target using the playbook. End with Plan of Record and three versions locked.

**"Our plan and our forecast don't align."** Compare the two documents. Plan is annual strategy; forecast is current expectation within the plan period. Mismatch typically means assumptions broke (churn higher than assumed, pipeline velocity slower, deal sizes smaller). Reforecast triggers analysis: which trigger fired?

**"Finance gave us a stretch we don't believe in."** Run the diagnostic (Section 6). Work through the reconciliation playbook (Section 3). Make stretch scenarios explicit with owners and dependencies. If scenarios still don't close the gap, escalate: "The market will not support this plan unless we make these three bets. We own the first two. The third depends on product. What is product committing to?"

**"We reforecast every month and it's chaos."** Lock the reforecasting cadence (quarterly minimum; monthly only for high-volatility businesses). Define triggers explicitly so reforecasts are data-driven, not reactive. Run the diagnostic to expose which functions are destabilising the process.

**"We don't know if we're on track."** Implement monthly forecast review against Plan of Record. Compare actual close rate to forecast. Track pipeline coverage week-to-week. Escalate on trigger (coverage drops below 2.5x, accuracy exceeds ±20%). This is what RevOps + FP&A sync owns.

---

## Reference Files

| File | When to read | What's inside |
|------|-------------|---------------|
| `references/planning-calendar-checklist.md` | Designing planning timeline for your fiscal year | 12-week template, phase guardrails, customisation guide for different fiscal years |
| `references/bottoms-up-build-recipe.md` | Walking through bottoms-up build process | 5-step recipe with examples, capacity-model calculator, Pavilion worksheet mechanics, assumption documentation |
| `references/reconciliation-playbook.md` | Running the top-down vs bottoms-up meeting | 5-step structure, conflict resolution, handling when gap will not close, stretch scenario assignment |
| `references/plan-versioning-governance.md` | Setting up version control and governance | Three-version system, file-naming conventions, access controls, reforecast preservation |
| `references/reforecasting-triggers.md` | Defining when to reforecast mid-year | Trigger matrix (revenue, unit-economics, execution, external), examples per trigger type, process per trigger |
| `references/reforecasting-benchmarks.md` | Pipeline coverage and forecast accuracy thresholds | Coverage benchmarks (Ebsta 2025), accuracy benchmarks (Gartner 2025), when each benchmark triggers escalation |
| `references/fpa-revops-collaboration-charter.md` | Building joint FP&A-RevOps ownership | Roles, joint-decision matrix, weekly sync template, quarterly reconciliation meeting format |
| `references/planning-diagnostic-full.md` | Running full 10-question diagnostic | Detailed interpretation per question, scoring guide, remediation playbook for process gaps |
| `references/planning-assumptions-template.md` | Creating single-source-of-truth assumption sheet | Template, example, owner assignment, confidence scoring |
| `references/benchmarks-sourced.md` | Reference data for planning benchmarks | Only sourced numbers: quota attainment, forecast accuracy, pipeline coverage, reforecasting frequency, sales cycle length |

---

## Canon References

Cross-references: revops-forecasting (in-quarter weekly forecasting, forecast methods, accuracy measurement), gtm-planning (capacity model, territory design, headcount scaling, productivity ramp), gtm-compensation (quota setting, comp structure, commission modelling), revops-metrics (KPI definitions, SaaS unit economics, benchmarks), signal-trigger-action framework (operating cadence), and planning-calendar skill (annual timeline coordination).

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates: Annual Planning Worksheets

For revenue planning in client engagements:

**Capacity Model Calculator:**
`assets/capacity-model-calculator.xlsx`
- Headcount input by role and start date
- Ramp-period calculations
- Quota × FTE = bookings capacity
- Tip: Run this first; it is your baseline for reconciliation
- Regenerate via `python scripts/generate_workbooks.py`

**Bottoms-Up Planning Sheet:**
`assets/bottoms-up-planning-sheet.xlsx`
- Segment-by-segment breakdown (New Business / Expansion / Renewal)
- Current ARR baseline and growth assumptions per segment
- Named pipeline overlay
- Assumption documentation
- Links to capacity model for rollup validation

**Reconciliation Template:**
`Frameworks/Templates/revops-revenue-planning/reconciliation-meeting-template.md`
- Pre-meeting prep checklist
- 5-step meeting structure
- Gap analysis table
- Scenario assignment sheet
- Post-meeting communication template

Use in: Annual planning kickoff, revenue-finance alignment sessions, board preparation, mid-year reforecasting.

Attribution: Pavilion CRO School (Forecasting and Revenue Modeling curriculum), FP&A Today podcast (FP&A best practices), Revenue Leadership Podcast (Shantanu Shekhar, Gong/Personio RevOps framework), Atscale practitioner input (Louis Fumey, 2026), Ebsta 2025 GTM Benchmarks Report.
