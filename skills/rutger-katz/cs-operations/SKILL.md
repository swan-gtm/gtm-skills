---
name: "cs-operations"
title: Customer success operations
description: "Customer success operations for B2B SaaS. The post-sale revenue engine that prevents churn, drives expansion, and compounds customer value. Use when the user mentions customer success, CS ops, health scoring, renewal management, churn prevention, expansion playbook, expansion signals, onboarding orchestration, time to first value, QBR, customer segmentation, coverage model, high-touch, low-touch, tech-touch, CSM ratios, NPS, CSAT, save plays, red accounts, CS-Sales handoff, churn autopsy, renewal discount governance, discount sunset, renewal pricing, or save plays with pricing components. Also trigger when someone says \"we keep losing customers\" or \"our CS team is reactive\" or \"we have no idea which accounts will churn\" or \"discounts are expiring and customers are pushing back\" or \"renewal price increase resistance."
category: RevOps
---

# Customer Success Operations

You are a CS operations architect. CS Ops is the post-sale revenue engine. It sits in the ICP Value Loops layer of the revenue operating system, owning Adopt → Realise Value → Renew → Expand. Without it, you're relying on individual heroics instead of systems.

## The CS Ops Operating Model

Four pillars. Neglect any one and the system breaks.

```
PROCESS DESIGN          TECHNOLOGY & SYSTEMS
├─ Playbooks            ├─ CS Platform: Gainsight (Horizon AI, 2024+), ChurnZero,
├─ Workflows            │  Vitally; all support real-time ML scoring (2026)
├─ Escalation paths     ├─ Product analytics (Pendo, Amplitude)
├─ Governance           ├─ Support (Zendesk, Intercom)
├─ Swimlanes            ├─ Survey tools (NPS, CSAT; note: Delighted shut 30 Jun 2026)
└─ AI agents            └─ Data warehouse integration; reverse ETL (Hightouch, Census)

DATA & ANALYTICS        ENABLEMENT
├─ Health scores        ├─ CSM onboarding (2 weeks, not 2 months)
│  (ML-powered, real-time)  ├─ Playbook documentation
├─ Churn prediction     ├─ Tools training
│  (ML+NLP ensemble)    ├─ Certification on key processes
├─ Expansion scoring    ├─ Knowledge base
├─ Cohort analysis      └─ AI-assisted customer signal synthesis
└─ Team efficiency
```

## CS Maturity Model

```
┌────────────┬──────────────┬────────────────┬───────────────┬──────────────┐
│ Stage      │ Health Score │ Renewals       │ Expansion     │ Governance   │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ REACTIVE   │ None. React  │ Ad-hoc,        │ Accidental    │ CS isolated, │
│            │ to churn.    │ customer-led   │               │ no loops     │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ DEFINED    │ Manual, CSM  │ Playbook, 60d  │ Signals ID'd  │ Handoff doc  │
│            │ judgment     │ before expiry  │ inconsistently│ exists       │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ PROACTIVE  │ Composite,   │ Automated 90d  │ Scoring model │ Quarterly    │
│            │ weekly auto  │ process + save │ + targeted    │ CS-Product   │
│            │ alerts       │ playbooks      │ outreach      │ forums       │
├────────────┼──────────────┼────────────────┼───────────────┼──────────────┤
│ PREDICTIVE │ ML model,    │ Preventive     │ Expansion     │ Real-time    │
│            │ >80% churn   │ interventions, │ scoring feeds │ feedback     │
│            │ accuracy     │ <5% churn      │ Sales pipeline│ loops        │
└────────────┴──────────────┴────────────────┴───────────────┴──────────────┘
```

If you're Reactive: stop everything else and move to Defined first.

## Health Score Framework

The single most important CS Ops tool. Composite scores with weighted dimensions:

```
HEALTH SCORE = Weighted average of 5 dimensions

PRODUCT USAGE (35%)
  Login frequency, feature adoption, depth of use, usage trend
  Weight rationale: usage is the strongest churn predictor

RELATIONSHIP (25%)
  Executive sponsor engaged, NPS response, meeting cadence, org adoption %
  Weight rationale: champions save accounts

SUPPORT (18%)
  Ticket volume trend, severity, resolution time, CSAT
  Weight rationale: pain signals churn

COMMERCIAL (17%)
  Contract value trend, payment history, expansion conversations
  Weight rationale: money doesn't lie

OUTCOMES (5%)
  Achieving stated goals, ROI realization, milestone completion
  Weight rationale: data often incomplete early on
```

### Traffic Light System

```
GREEN (80+):  Expand. Growth partner posture. 2-5% churn risk (practice-based).
YELLOW (40-79): Intervene. Increase touchpoints. 15-30% churn risk (practice-based).
RED (<40):    Save mode. Executive intervention. 60%+ churn risk (practice-based).
```

### Health Score Anti-Patterns

```
Binary scores ("healthy" vs "at risk")  → Use 0-100 scale with thresholds
Usage-only scores                       → Composite with multiple signals
Manual, updated quarterly               → Automated, real-time or weekly minimum
Score says green but they churn          → Calibrate against actual outcomes
Nobody acts on red accounts              → CS Manager reviews reds weekly
```

**EU Data Governance Note (GDPR Article 22):** Health scores incorporate personal data (NPS responses, engagement metrics from personal profiles). If automated scoring drives material customer-facing decisions (e.g., renewal discounting, reduced support tier) without human review, you must establish documented lawful basis and provide individuals with the right to human review per Article 22. Recommended: reserve automated action for internal escalation only; require CSM/manager review before any customer-visible decision.

## Segmentation & Coverage Models

```
┌──────────────┬─────────────────┬─────────────────┬────────────────────┐
│ Segment      │ Criteria        │ Coverage Model   │ CSM Ratio          │
├──────────────┼─────────────────┼─────────────────┼────────────────────┤
│ HIGH-TOUCH   │ >€50K ARR       │ Named CSM        │ 1:10-50            │
│ (Strategic)  │ Complex product │ Quarterly EBRs   │ (ChurnZero, 2026)  │
│              │ High expansion  │ Dedicated onboard│ AI-assisted: +25-50%│
├──────────────┼─────────────────┼─────────────────┼────────────────────┤
│ MID-TOUCH    │ €10-50K ARR     │ Pooled CSM       │ 1:100-200          │
│ (Scaled)     │ Moderate complex│ Templated touches│ (ChurnZero, 2026)  │
│              │ Growth potential│ Triggered playbks│ AI-assisted tools  │
├──────────────┼─────────────────┼─────────────────┼────────────────────┤
│ TECH-TOUCH   │ <€10K ARR       │ Automated        │ 1:500-1000         │
│ (Digital-led)│ Self-serve      │ In-app guidance  │ (ChurnZero, 2026)  │
│              │ Simple use case │ Community/webinar│ AI agents primary  │
└──────────────┴─────────────────┴─────────────────┴────────────────────┘
```

Reassess tiers quarterly based on usage growth, health, and expansion potential.

## Renewal Management

Start 120 days before contract end. Not 30. Starting at T-30 is too late for anything except discounting. This is the single canonical renewal timeline.

```
T-120 days: PREP
  Renewal flag auto-created in CRM
  CSM reviews health, usage, and expansion signals; Finance pulls contract
  terms; Product flags blockers
  If health < 40 (Red): escalate immediately, don't wait for T-90
  Output: Renewal strategy (standard / at-risk save play / expansion)

T-90 days: HEALTH CHECK / KICKOFF
  QBR conducted, executive alignment, pulse on value delivery
  CSM prepares ROI / value-delivered summary
  Internal alignment: any pricing changes, product updates?
  If discount expiring: begin value-led conversation (see Renewal Discount Governance)
  Score: Likely / At-risk / Needs work

T-60 days: PROPOSAL / CONVERSATION
  Standard: Renewal proposal sent. Present value delivered, roadmap alignment, terms
  At-risk: Executive sponsor conversation, barrier removal; activate save playbook
  Expanding: Sales/CSM joint upsell conversation, present expansion proposal alongside renewal

T-30 days: NEGOTIATION
  Contract sent; handle objections, escalate to CS leader if not signed
  If discount negotiation: use graduated step-up (see Renewal Discount Governance)
  Daily tracking of renewal pipeline

T-0: CLOSE
  Contract signed or churned. Revenue booked, post-renewal thank you, reset for next cycle
  If churned: initiate churn autopsy within 7 days
  Feed learnings to Product

T+7: POST-RENEWAL CHECK-IN
  Confirm satisfaction with terms, document win/loss reason
  Set next QBR date, update health score
```

**Track:** On-time renewal rate, early renewal rate, save rate (red accounts renewed), renewal velocity.

## Expansion Playbooks

Expansion is a process, not an event. Most expansion dies because nobody owns the handoff from CS to Sales or because the signal was visible but nobody acted on it.

### Expansion Signals

```
USAGE:        Hitting seat limits, new feature adoption, DAU increasing,
              usage approaching plan limits (>80% utilisation)
RELATIONSHIP: Champion promoted, new stakeholder/exec sponsor engaged, positive NPS,
              new departments/teams using the product
COMMERCIAL:   Org headcount growth, new budget cycle, cross-functional interest,
              feature requests for premium-tier functionality
OUTCOMES:     Value achieved ahead of schedule, ROI exceeded, new use cases,
              positive health trend (score increasing 3+ months), referral/case study
```

### Expansion Ownership Model

```
Small expansion (<20% ACV):  CS owns end-to-end
Medium expansion (20-50%):   CS identifies, Sales closes
Large expansion (>50% ACV):  Sales owns, CS supports
```

CS-to-Sales handoff: CS prepares customer context, decision-maker, timeline, needs. Sales accepts or declines. If accepted, CS introduces Sales to champion and stays involved through close. Expansion motion: CS documents the signal in CRM → warm intro from CSM to AE/expansion AE → AE runs the commercial conversation while CSM provides context and stays on early calls → post-expansion, CS implements the expanded scope and tracks value on the new commitment.

For the 0-100 expansion scoring model (usage/stakeholder/feature/health/headroom weights), score-based ownership thresholds, account readiness triggers, and whitespace analysis, see `references/expansion-scoring-model.md`.

## Onboarding Orchestration

The handoff is where retention is won or lost. A weak handoff creates context loss, broken promises, and a customer who feels like they're starting over. For the step-by-step Sales → CS handoff process and checklist, see the summary under "Sales → CS Handoff" below and `references/sales-cs-handoff-template.md`. This is the single canonical onboarding model.

```
DAY 1-7: ACTIVATION / KICKOFF
  Welcome email (within 2 hours), license activation, kickoff scheduled
  Kickoff call with key stakeholders; assign customer-side project owner
  Success criteria and timeline confirmed: "What does success look like?"
  (Use SPICED Impact as baseline)

DAY 8-30: IMPLEMENTATION / TECHNICAL SETUP
  Configuration / environment setup, data migration, integration setup
  Admin training, user training, weekly status calls, blocker resolution
  Document known issues or customisation needs
  Milestone: Go-live readiness confirmed

DAY 31-60: STABILIZATION / USER ENABLEMENT
  Go-live, first-week support surge (daily check-ins)
  End-user training sessions, internal documentation/guides
  Identify power users / internal champions, validate adoption metrics
  Usage monitoring, issue resolution, user adoption tracking
  First value delivered: "Here's the impact you're seeing"

DAY 61-90: OPTIMIZATION / FIRST VALUE
  Confirm first value milestone achieved; capture success story (even informal)
  Performance vs. success criteria, advanced feature rollout
  Executive check-in, health score baseline set, first QBR/check-in scheduled
  Transition to business-as-usual CSM cadence
```

**Automation triggers:** No kickoff by day 3 → reminder. Not go-live by day 30 → alert manager. Usage <20% by day 60 → intervention. Health <50 by day 90 → yellow playbook.

**Track:** Time to kickoff (<3d), time to first login (<7d), time to first value (TTFV) (<30d), go-live on schedule (90%+), onboarding completion rate (>90%), onboarding CSAT (90%+ top performers; recommended), feature adoption at T+30 (>3 core features).

### Sales → CS Handoff

When a deal hits Closed Won, an automated notification routes the account to the assigned CSM with a CRM record containing the SPICED summary, stakeholders, contractual commitments, known risks, product/tier config, and any discount terms with expiry dates. The CSM reviews it, runs a short internal handoff call with the AE (what was promised, who's the champion/blocker, what success looks like, landmines), then sends the welcome email and schedules kickoff. A handoff quality check confirms the SPICED summary is complete, all stakeholders are in CRM, and discount terms are documented with expiry. For the full step-by-step timeline, Sales pre-handoff responsibilities, the three-way handoff meeting, and checklist, see `references/sales-cs-handoff-template.md`.

## Event-Based Playbooks

```
USAGE DROP (WAU drops >30% week-over-week)
  Action: CSM outreach within 24 hours
  Root cause: Change, vacations, budget freeze, support issue?

NPS DETRACTOR (Score <6)
  Action: Call within 48 hours
  Document specific complaint, not generic dissatisfaction

CHAMPION DEPARTURE
  Action: Identify new stakeholder within 1 week
  Risk mitigation: Involve next-level executive immediately

SUPPORT ESCALATION (Sev-1 OR 3+ tickets in 7 days)
  Action: Triage within 2 hours, CS + Support Manager
```

## Renewal Discount Governance

The #1 cause of contentious renewals is a discount that was never documented to expire. At renewal, the customer anchors on what they paid, not what the product is worth. This is a structural governance failure: every discounted deal must carry a `Discount_Expiry_Date` in CRM, the T-120 workflow must flag expiring discounts automatically, and the CSM must prepare value justification before the conversation. The conversation framework leads with value (T-90), frames the step-up (T-60), and offers a graduated step-up only as a save play (T-30). GPO/consortium accounts get coordinated tier/volume validation from T-120 through T-30 with Deal Desk.

For the full discount sunset problem, the pricing conversation framework, the save-plays-with-pricing table, and GPO renewal coordination, see `references/renewal-discount-governance.md`. For discount governance policy (approval matrices, ACV tiers), see pricing-strategy skill.

## CS-Product Feedback Loop

Install the structural mechanisms that turn customer signal into product action: a quarterly advisory board (3-5 customer execs + Product VP), churn autopsies on 100% of churned accounts (CS Manager + Product Manager), feature request tagging with ARR/use case/competitive/expansion/blocker fields, and a monthly adoption blocker log feeding a dedicated Product queue.

For the full feedback loop architecture (owners, questions, outputs, and review cadence for each mechanism), see `references/cs-product-feedback-architecture.md`.

## Key Metrics

```
REVENUE                          TARGETS
  GRR                            84% median (75th %ile 91%+; Optifai, 2026)
  NRR                            106% median (top performers >130%; Optifai, 2026)
  Logo retention rate            80-90% (aspirational; industry median 70-80%)
  Expansion rate (% ARR growth)  40% of new ARR from expansion (ZoomInfo, 2026)

OPERATIONAL
  Time to first value            <30 days (recommended)
  Health score distribution      >70% green (recommended)
  QBR completion (high-touch)    100% (recommended)
  Renewal on-time rate           >90% (recommended)
  Save rate (red accounts)       >40% (practice-based)

EFFICIENCY
  Accounts per CSM (by tier)     See coverage model (sourced, 2026)
  Admin time (% of total)        <30% (recommended)
  CSM attrition rate             <15%/year (recommended)

LEADING INDICATORS
  Accounts with declining usage  Track weekly (recommended)
  Accounts without exec sponsor  <5% (recommended)
  Days to complete renewal       <60 days (recommended)
  Core feature adoption rate     >70% (recommended)
```

## AI and Automation in CS Ops (2026)

Real-time health scoring, autonomous churn prediction, and AI-assisted signal synthesis are now standard in modern CS platforms. This is not "future state"; it's operational today.

### Real-Time Predictive Scoring

Modern platforms (Gainsight Horizon AI, ChurnZero, Vitally) update health scores in real time rather than batch weekly. Triggers are now event-driven: usage cliff detected → CSM alert; NPS detractor submitted → auto-flag; champion departure → relationship score drops immediately. Churn prediction with ensemble ML plus NLP on unstructured signals (call transcripts, support tickets, email sentiment) cuts churn 15-30% within 12 months (2026 vendor research).

### Autonomous Agents and Workflow

Renewal and expansion processes no longer require manual CSM review at every step. Autonomous agents monitor thresholds (usage >80% of plan, score drop >15pts), initiate escalation workflows, and in some cases send templated outreach. The CSM remains accountable but the agent handles routine hygiene: flag at-risk accounts, surface expansion candidates, suggest playbook actions. This frees CSMs to focus on high-touch strategy and executive relationships.

### Dynamic Segmentation

Static ARR tiers are outdated. Modern platforms segment dynamically by usage trajectory, health trends, and expansion readiness. A sub-€10K account with 200% month-over-month growth and executive sponsor engagement moves into a higher-touch coverage tier automatically. Weekly re-segmentation based on behavioural signals means coverage shifts to where the opportunity is.

### AI-Assisted Churn Autopsy and Insight Synthesis

Gainsight Horizon AI (2024+) and peers now offer automated call transcription, sentiment analysis, and account summary synthesis. Rather than manual CSM + PM churn autopsies, the system ingests call recordings, extracts decision-driver signals, compares against similar accounts, and surfaces likely product gaps. QBR prep no longer requires manual data gathering; AI-generated benchmarking insights ("You are 40% below similar customers in feature X") are delivered automatically to both CSM and customer.

**Implementation rule:** Deploy gradually. Start with real-time scoring; add autonomous escalation after 2 weeks; enable dynamic segmentation once you have clean usage data feeding the platform. Full AI adoption (transcription, synthesis, autonomous agents) requires data quality baseline of 80%+ field population.

## Diagnostic Assessment

Score your CS Ops maturity. Count YES answers:

```
PROCESS:     Documented playbooks? Defined renewal timeline? Health scoring
             framework? Escalation paths? QBRs for all high-touch?
TECHNOLOGY:  Dedicated CS platform? Integrates with product analytics?
             Automated health scoring? Usage data visible to CSMs?
DATA:        Can forecast churn 30+ days out? Health dashboards? Track
             expansion signals? Segment by tier? Measure team efficiency?
ENABLEMENT:  Structured CSM onboarding? Accessible playbooks? Process
             certification? Monthly training?
GOVERNANCE:  CS-Product feedback loop? CS-Sales handoff process? Exec
             reviews CS metrics monthly? Churn autopsies? Expansion
             ownership clear? Discount sunset tracking in place?

0-6 YES  = Reactive.  Fix: Define playbooks, build basic health scoring
7-13 YES = Defined.   Fix: Integrate tech, automate playbooks
14-19 YES = Proactive. Fix: Build predictive models, optimize coverage
20-25 YES = Predictive. Fix: AI-assisted coaching, autonomous workflows
```

## Process Operating Cadence

Health scoring and renewal frameworks answer "who is at risk?" and "how do we retain them?" They depend on a structured review cadence and escalation discipline. A health score without a review cadence is a dashboard no one acts on. The cadence is the operating system; the score is the signal.

**Manual review cadence (foundation for all tiers):**

- **Weekly:** CSM reviews accounts with a score drop >10pts; flag any Green→Yellow or Yellow→Red (CSM + CS Lead).
- **Monthly:** Full health score review of all accounts; any Red account reviewed with CS Lead + AE; scores updated on new data.
- **Quarterly:** Portfolio health review, QBR prep for T1 accounts, Red account recovery planning.

**Event-driven automation (2026+, layered on top):**

Modern CS platforms trigger actions in real time on usage cliffs (WAU drop >30%), NPS detractors, champion departures, and score transitions. Autonomous agents notify CSMs of threshold breaches and recommend escalation. This does not replace the manual cadence; it augments it. The CSM still owns accountability and strategy, but routine monitoring is automated.

**Red accounts: escalate within 24h.** When a customer turns Red, the CSM (or automated alert) notifies the CS Lead, who reviews the health breakdown and jointly decides with the AE between rescue mode (>90 days to renewal) and renewal risk mode (<90 days; activate the renewal process immediately, don't wait for T-90). For the full Red Account Playbook (rescue mode, renewal risk mode, commercial options) and the complete health monitoring cadence table, see `references/red-account-playbook.md`.

QBRs are the highest-leverage CS touchpoint for T1 accounts and most fail by looking backwards rather than forwards. For the 45-60 minute agenda structure and cadence-by-tier guidance, see `references/qbr-process-template.md`.

---

## How to Use This Skill

**"We keep losing customers but don't know why":** Start with health scoring. Build the 5-dimension composite score. You'll see patterns within 4 weeks.

**"Our CS team is drowning":** Segmentation problem. Build the 3-tier coverage model. Most teams try to high-touch everyone. That doesn't scale past 50 accounts.

**"Expansion is left on the table":** Build expansion signals and scoring. Define the CS-Sales handoff. Most expansion dies because nobody owns the handoff.

**"Product doesn't listen to CS":** Install the feedback loop: churn autopsies, feature request tagging with ARR impact, quarterly advisory board. Product responds to revenue data.

**"We need to build CS Ops from scratch":** Run the diagnostic. Score your maturity. Fix the weakest pillar first. Month 1: playbooks + basic health scoring. Month 2: renewal process. Month 3: automation.

**"Discounts are expiring and customers are pushing back":** Install the renewal discount governance framework. Document every discount with an expiry date. Lead with value at T-90, frame the step-up at T-60, and have graduated step-up as a save play only at T-30. For discount governance policy (approval matrices, ACV tiers), see pricing-strategy skill.

**"GPO/consortium accounts coming up for renewal":** Check GPO master record. Validate actual vs. committed volume. Coordinate with Deal Desk. No ad-hoc terms outside the GPO framework.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Reference Files

| File | When to read | What's inside |
|------|-------------|---------------|
| `references/renewal-discount-governance.md` | Discount expiring / contentious renewal pricing | Discount sunset problem, pricing conversation framework, save-plays-with-pricing table, GPO renewal coordination |
| `references/expansion-scoring-model.md` | Quantifying/prioritising expansion | 0-100 scoring model, score-based ownership thresholds, readiness triggers, whitespace analysis |
| `references/sales-cs-handoff-template.md` | Designing the Closed-Won → CS handoff | Step-by-step T+0 to T+5 timeline, Sales pre-handoff duties, handoff meeting, quality checklist |
| `references/red-account-playbook.md` | A customer turns Red | Rescue mode, renewal risk mode, commercial options, full health monitoring cadence table |
| `references/qbr-process-template.md` | Designing or running a QBR | 45-60 min agenda structure, cadence by tier |
| `references/cs-product-feedback-architecture.md` | Building the CS-Product loop | Advisory board, churn autopsy, feature request tagging, adoption blocker log |
| `references/customer-lifecycle-plays.md` | Choosing the right CS action for an account's phase | Four-phase classification, health interpretation per phase, trigger plays, expansion timing rule |

---

## Operator Templates: Forecasting Worksheet (Renewals Tab)

The Renewals tab of the forecasting worksheet is specifically useful for CS operations modelling:
`Frameworks/Templates/cro-school/forecasting-worksheet-neon.xlsx`

Use the Renewals tab to model: renewal cohort sizing, churn impact on ARR, expansion uplift scenarios.

Original source: `Sources/Courses/CRO-School/Forecasting Worksheet _ Class #4_ Forecasting and Financial Modeling.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
