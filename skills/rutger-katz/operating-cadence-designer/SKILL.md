---
name: "operating-cadence-designer"
title: Operating cadence designer
description: "Design and install the operating cadence for a client: the calendar that makes the revenue operating system real. Connects the strategy scorecard (strategy), the revenue dashboard (visibility), and weekly/monthly rituals (execution). Use whenever the user mentions 'operating cadence,' 'cadence design,' 'meeting architecture,' 'install the cadence,' 'ritual design,' 'revenue meetings,' '5P meetings,' 'breach rhythm,' 'WIP limits,' 'decision cadence,' 'signal trigger action,' 'decision rules,' or any engagement where meetings need restructuring. Also trigger on 'our meetings are status updates,' 'nobody makes decisions,' 'nothing gets done,' 'the board keeps getting surprised,' or 'we need a rhythm.' Also trigger on 'forecast calls,' 'pipeline review,' 'QBR,' 'board meeting,' 'board deck,' 'monthly business review,' 'sales standup,' or 'deal review.' BOUNDARY: For the revenue dashboard build itself, see pipeline-visibility."
category: RevOps
---

# Operating Cadence Designer

## Purpose

This skill helps design and install the operating cadence for clients. The cadence is the calendar that makes the revenue operating system real. It connects strategy (strategy scorecard), visibility (revenue dashboard), and execution (weekly/monthly rituals).

Without a cadence, leaders waste time in meetings that produce no decisions. With a cadence, every ritual has a clear purpose, owner, and output. This skill walks through the design and installation process.

---

## When This Skill Activates

Use this skill in three main situations:

### 1. No existing cadence
Client has no consistent rhythm for revenue decisions. Meetings happen ad hoc. Leadership time is fragmented across email, Slack threads, and back-channel conversations. There is no single source of truth for the week's agenda or the month's priorities.

**Design task:** Build a complete weekly, biweekly, monthly, and quarterly rhythm from scratch. Start with the simplest version (7 weekly rituals + 1 biweekly + 2 monthly + 1 quarterly) and adapt to client size and stage.

### 2. Broken or inconsistent cadence
Client has some rituals, but they're inconsistent: some happen on schedule, some get cancelled or rescheduled. No one knows which meetings are mandatory. There is no clear escalation path from a signal to a decision.

**Design task:** Audit existing rituals, apply the 5P gate, consolidate into a clean calendar, and install decision rules that tell people when to escalate.

### 3. Cadence exists but no decision rules
Client has the calendar but no signal-based decision rules. Meetings happen, data is reviewed, nods happen, but nothing actually changes. Decision latency is long. Experiment kill rate is low. The cadence is status theatre, not a control system.

**Design task:** Install signal-based decision rules on top of the existing calendar. Define 8-12 key signals, set thresholds, route triggers to rituals, and train people on escalation.

---

## The 5P Standard

Every meeting must pass the 5P gate. This is the non-negotiable foundation. If any P is missing or fuzzy, the meeting should be cancelled or rescheduled.

### The 5Ps

1. **Purpose**: One clear sentence: "By the end of this meeting, we will...". This must finish with a concrete outcome (decision, list, design, changed plan), not an activity (discuss, review, understand).

2. **Product**: A tangible artifact that proves the meeting was worth the time.
   - Examples: 3 decisions in the Decision Log with IDs and owners; prioritised problem list; A3 draft; updated experiment backlog; changed forecast or strategy scorecard tile.
   - Not: "discuss pipeline" or "update everyone" (these are verbs, not products).

3. **People**: The smallest set of roles that can create the product and own the actions.
   - No spectators. Everyone must bring proof, make decisions, or leave with actions.
   - Invite by role, not just by name. Example: "one VP Sales" instead of "everyone from Sales".

4. **Process**: How the time will be used.
   - 2-5 bullet agenda with explicit timeboxes.
   - Which panels in the revenue dashboard (if applicable).
   - Who facilitates, who decides, who takes notes, how the close happens.

5. **Proof**: The facts and pre-work needed so time is spent deciding, not discovering.
   - Bowtie metrics, GRR/NRR, customer quotes, win/loss summaries, A3 snippets.
   - Pre-reads sent at least one working day in advance for decision sessions.
   - Clear baseline so you can measure later if the decision worked.

**5P gate rule:** If any P is missing or fuzzy, cancel the meeting or replace it with an async update. A healthy cadence has a non-zero cancel rate (5-15% typical; practice-based).

---

## Cadence Design Workflow

Follow this sequence when designing a cadence for a client:

### Phase 1: Assess Current State (Week 1)

1. **Map existing meetings.** What meetings happen now? List them with owner, frequency, duration, attendees, and stated purpose. Include 1:1s, team standups, leadership syncs, and functional reviews.

2. **Run the 5P audit.** For each meeting, can the owner write down all 5Ps clearly? Where are the gaps? Common failures: no clear Purpose, no Product (just "discuss"), no defined attendees, no pre-work or proof.

3. **Identify decision gaps.** Where are decisions made today? In the meetings, or in side channels and follow-ups? Is there a Decision Log? How long does it take from insight to decision?

4. **Assess data readiness.** Is there a revenue dashboard with live dashboards? Can people answer the key questions (pipeline health, GRR/NRR, constraint wall, experiment portfolio status) in minutes?

5. **Interview key roles.** Ask CRO, CEO, CMO, VP Sales, Head of CS: What decisions are you struggling to make? What meetings feel like waste? Where do you spend time that creates no value? What surprises you about the current system?

**Output:** A 1-page "Current State" document with audit findings, three pain points ranked by impact, and a rough sketch of what meetings should exist.

### Phase 2: Design the Calendar (Week 2-3)

Use the operating cadence template. Adapt the rhythm to client size and stage.

#### Weekly (7 rituals); 4.5 hours total

1. **Revenue Dashboard: Pipeline and Decisions** (75 min)
   - Owner: CRO
   - Purpose: Review bowtie, pipeline health, constraints, then make at most 3 decisions or A3 assignments
   - Product: Decisions logged with IDs, owners, due dates
   - Panels: Bowtie and segment views, pipeline by stage, constraint wall, experiment portfolio

2. **Marketing Demand and Efficiency Loop** (45 min)
   - Owner: CMO or Head of Growth
   - Purpose: Improve demand quality and SDR efficiency
   - Product: Adjusted campaign focus, new experiments with stop rules

3. **Sales Pipeline and Efficiency Loop** (45 min)
   - Owner: VP Sales
   - Purpose: Improve pipeline health and sales efficiency
   - Product: Clean pipeline, surfaced stuck items, problems framed as A3s

4. **CS Value and Efficiency Loop** (45 min)
   - Owner: Head of CS
   - Purpose: Improve retention and expansion
   - Product: Account attention list, new countermeasures

5. **Coaching and Revenue Craft Loop** (45 min)
   - Owner: Sales and CS leaders
   - Purpose: Turn customer conversations into better plays
   - Product: Coaching actions with check-in dates, playbook updates

6. **Breach and Incident Huddle** (30 min)
   - Owner: RevOps on call
   - Purpose: Catch and contain SLO breaches
   - Product: Owner and containment plan for each breach

7. **AI and Automation Integration** (45 min, starting Week 3)
   - Owner: RevOps and Platform lead
   - Purpose: Embed AI into the revenue system at four levels: L1 (signal tagging and automation triggers), L2 (breach detection agents that alert decision-makers), L3 (experiment idea generation and analysis), L4 (autonomous agents making decisions within guardrails)
   - Product: Prioritised automation experiments with cost-benefit, execution plan, and kill rules. Monthly AI rhythm advancement (L1 to L2, L2 to L3, etc.)
   - Integration: Connects to the Breach Huddle (L2 agents feed incident alerts) and Demo and Retro (L3 and L4 results reviewed monthly)

#### Bi-weekly (1 ritual); 60 min

1. **Demo and Retro** (60 min)
   - Owner: Rotating facilitator
   - Purpose: Show shipped experiments and countermeasures, decide keep/kill/scale
   - Product: Keep/kill/scale decisions logged in Decision Log

#### Monthly (2 rituals); 150 min

1. **Strategy and Lever Review** (90 min)
   - Owner: CEO and CRO
   - Purpose: Review strategy scorecard, choose levers, adjust WIP and SLOs
   - Product: Updated WIP caps, next quarter lever list

2. **Data Spine and Definition Review** (60 min)
   - Owner: RevOps and Data lead
   - Purpose: Check data freshness, completeness, and activation. Ensure decision-to-execution loops close via reverse ETL (data changes trigger CRM updates, audience sync, and alert routing).
   - Product: Data health status, definition change log, reverse ETL activation status (which signals route to which systems: Salesforce, email platforms, messaging tools)
   - Integration: Validates that the revenue system feeds real-time data to decision-makers and that decisions propagate back to the stack (via Hightouch, Census, Segment, or native reverse ETL)

#### Quarterly (1 ritual); 180 min

1. **Quarterly Reset** (2-3 hours)
   - Owner: CEO
   - Purpose: Refresh strategy scorecard, confirm cadence, align next quarter targets and SLOs
   - Product: Updated strategy scorecard, confirmed cadence changes, new SLOs

**Key design rules:**
- Keep weekly rituals short and focused. No meeting longer than 75 minutes.
- Most rituals feed the same revenue dashboard. No parallel streams.
- Reduce, never add. If you're tempted to add a meeting, cancel an existing one first.
- Schedule decision sessions early in the week. Leave space for countermeasures and follow-up.

**Output:** Colour-coded calendar showing all rituals, owners, attendees, duration, and which revenue dashboard panels they use.

### Phase 3: Build Ritual Cards (Week 3-4)

For each ritual, create a one-pager (the "ritual card") that shows:
- Purpose statement
- Inputs (which dashboards or documents are needed)
- Outputs (what gets decided or changed)
- RACI (Driver, Approver, Contributors, Informed)
- Tollgates (what has to be true for the meeting to happen)
- Cancel rule (when to cancel or shorten)
- Pre-work and proof checklist

Adapt owner names and timings to the client. Print and laminate them. Put them in the revenue dashboard room so facilitators can see the standard at a glance.

### Phase 4: Install Signal-Based Decision Rules (Week 8-10)

Once the calendar is stable and people are attending, layer in signal-based decision rules. This is Phase 2 of the 90-day rollout (see below).

1. **Week 8:** Choose 8-12 key signals from the four capability streams (Customer Insights, Revenue Motions, Enablement, Governance). Start with signals where you already have data.

2. **Week 9:** Set thresholds using 6 months of historical data. When a signal crosses a threshold, it becomes a trigger (something has changed enough that we need to act).

3. **Week 10:** Route each trigger to a specific ritual in the cadence. For example:
   - Pipeline coverage SMB <2.5x for 3 weeks -> escalate to Marketing Demand Loop
   - Win rate drops >5pp -> open A3 in Sales Pipeline Loop
   - Decision latency >14 days -> escalate to Strategy and Lever Review
   - 5P cancel rate 0% for 4 weeks -> challenge in Strategy and Lever Review

Print the signal map and post it in the revenue dashboard room. No new meetings. Just clearer escalation rules.

**Output:** Signal-based decision rules matrix with 8-12 signals, thresholds, and routing rules.

### Phase 5: Transfer Ownership (Week 11-12)

In the final weeks of the 90-day programme, transfer operational ownership of the cadence to the client team. The Cadence Owner (usually the CRO or RevOps lead) becomes accountable for:

- Keeping the calendar on track
- Enforcing the 5P gate at the start of each meeting
- Logging decisions and actions in the Decision Log
- Monitoring cadence health KPIs
- Proposing cadence changes only in the Quarterly Reset

Run a "Cadence Keeper" workshop where the Cadence Owner and RevOps lead practice facilitating rituals, handling the 5P gate, and routing signals to the right forum.

---

## 90-Day Installation Programme

The cadence installs in a 12-week programme with clear phases and handoff points.

### Phase 1: Stand-up (Weeks 1-2)

**Goal:** Assess the current state and design the ideal cadence.

- Audit existing meetings and run 5P gate
- Interview key roles (CRO, CEO, CMO, VP Sales, Head of CS)
- Map decision gaps and data readiness
- Design the calendar (weekly, biweekly, monthly, quarterly)
- Prepare ritual cards
- Brief the leadership team on the design

**Output:** Signed-off calendar, ritual cards, current state assessment

### Phase 2: Co-host (Weeks 3-6)

**Goal:** Launch the cadence with the consultant as co-facilitator. Build the habit.

- Run all 7 weekly rituals with the consultant co-hosting or observing
- Apply the 5P gate strictly. Cancel or shorten any meeting that fails.
- Log all decisions and actions in the Decision Log
- Build or update the revenue dashboard (if not already done)
- Run the first Demo and Retro (biweekly)
- Run the first Strategy and Lever Review (monthly)
- Observe and coach the CRO on ownership

**Output:** Live cadence with 4 weeks of decisions logged, habits forming, revenue dashboard live

### Phase 3: Hand-off (Weeks 7-10)

**Goal:** The client team leads the cadence. The consultant coaches and observes.

- The CRO leads all weekly rituals
- The consultant observes and coaches on facilitation, decision quality, and escalation
- Install signal-based decision rules (Week 8-10)
- Run Demo and Retro (biweekly)
- Run Quarterly Reset if applicable
- Coach the RevOps or Cadence Owner on decision logging and cadence health

**Output:** Client team running cadence independently; decision latency improving; kill rate and 5P cancel rate visible

### Phase 4: Certification (Weeks 11-12)

**Goal:** Certify that the cadence is stable and the client team owns it.

- Client team runs all rituals without the consultant present
- The consultant spot-checks decisions and cadence health KPIs
- Hold final "Cadence Keeper" workshop with CRO, RevOps, and CEO
- Transfer the Cadence Owner role formally
- Schedule quarterly cadence reviews (tuning only in Quarterly Reset)
- Document any customisations or deviations from the standard

**Output:** Certified cadence; client team owns the calendar and decision log; cadence health KPIs in place

---

## Cadence Health KPIs

Track these metrics to see if the cadence itself is working:

1. **Decision latency**: Time from insight (data signal) to logged decision, and from logged decision to live countermeasure. Target: <7 days for most decisions.

2. **5P cancel rate**: Share of scheduled meetings that are cancelled because they lack Purpose, Product, People, Process, or Proof. A healthy cadence has 5-15% cancel rate (practice-based). Zero cancel rate means the gate is not enforced; >20% means the calendar is overloaded.

3. **SLO hit rate**: Share of weeks where key handover p95 SLOs (lead to first touch, MQL to SQL, etc.) are met. Target: >80% (practice-based).

4. **Freshness attainment**: Share of weekly Data Spine checks that pass (data is current, complete, accurate). Target: >95% (practice-based).

5. **Forecast accuracy**: Share of periods where actual revenue sits within forecast bands. Target: >70% (practice-based).

6. **Kill rate**: Share of experiments killed by stop rule per quarter. Target: 20%+ per quarter. Kill rate <10% suggests experiments don't have real stop rules.

7. **Coaching uptake**: Share of reps and teams that complete agreed coaching actions within the target timeframe. Target: >80% (practice-based).

Review these KPIs monthly in the Strategy and Lever Review. Tune the cadence only in the Quarterly Reset.

---

## Revenue Cadence: Meeting Architecture & Ceremony Agendas

### The Core Principle: Data Pyramid

Every decision flows from clean data. Every data input flows from activity. The pyramid collapses if the base is dirty.

```
          +-----------------+
          |    BOARD        |
          |  (Quarterly)    |
          |  Narrative+KPIs |
          +--------+--------+
                   |
          +--------v--------+
          |  LEADERSHIP     |
          | (Monthly/QBR)   |
          | Trends+Decisions|
          +--------+--------+
                   |
          +--------v--------+
          |      TEAM       |
          |   (Weekly)      |
          |Pipeline+Forecast|
          +--------+--------+
                   |
          +--------v--------+
          |   ACTIVITY      |
          |    (Daily)      |
          | Calls/Deals/Logs|
          +-----------------+
```

If activity is garbage -> pipeline data lies -> forecasts fail -> board gets surprises.

### The 7-Question Meeting Architecture

Before scheduling any revenue meeting, answer these:

| Element | Question | Bad Answer | Good Answer |
|---------|----------|-----------|-------------|
| **Purpose** | What decision does this produce? | "Check on things" | "Lock forecast by Friday noon" |
| **Frequency** | How often? | "Weekly because that's what we do" | "Weekly for accountability, monthly for trends" |
| **Participants** | Who MUST be here? | "The whole team" | "Sales managers + CRO only (RevOps attends async)" |
| **Inputs** | What prep is required? | People wing it | Pre-built forecast model + deal aging report |
| **Agenda** | How do we spend the time? | Meandering | 15 min data review, 30 min decisions, 5 min actions |
| **Outputs** | What leaves the room? | "We'll figure it out" | Logged forecast, deal actions with owners |
| **Accountability** | Who owns follow-through? | Nobody | Action log with due dates + owner names |

**Rule:** If a meeting doesn't produce decisions or logged actions, send an email instead.

### Core Ceremony Agendas

**Daily: Sales Pipeline Pulse (15 min)**
Purpose: Surface blockers. Coordinate same-day wins. RevOps not in the room; pre-built CRM views make this self-serve.

**Weekly: Pipeline Review (45 min, Sales Manager + team)**
Pre-meeting packet: stage movement (last 7 days), deal aging by stage, forecast accuracy vs. prior week, win/loss summary.

| Time | Owner | Output |
|------|-------|--------|
| 0-5 min | Sales Manager | Context (priorities this week) |
| 5-35 min | Team | Review deals >7 days old + red-flag risks |
| 35-40 min | Sales Manager | Commit vs. best case for the week |
| 40-45 min | All | Logged actions: who's doing what by when? |

Key questions: Which deals moved stage? What's stalled? What's the gap to plan?

**Weekly: Forecast Roll-up (30 min, CRO + Sales Managers + RevOps)**
Pre-meeting: consolidated forecast, variance to plan, confidence % by deal stage, top 10 at-risk deals.

| What | Time | Owner |
|------|------|-------|
| Review company forecast vs. target | 10 min | RevOps |
| Identify gap-closing actions | 15 min | CRO + managers |
| Log decisions & owners | 5 min | All |

Output: Locked company forecast. Gap-closing action log.

**Bi-weekly: Funnel Review (60 min, Marketing + Sales + CS + RevOps)**
Pre-meeting: conversion rates by stage, lead-to-opportunity velocity, MQL quality, bottleneck analysis, win rate by segment.

| Section | Time | Owner |
|---------|------|-------|
| MQL quality & lead flow | 15 min | Marketing |
| Lead-to-opp conversion | 10 min | Sales |
| Opportunity velocity & close rates | 15 min | RevOps |
| Retention & expansion | 10 min | CS |
| Cross-functional actions | 10 min | All |

**Monthly: Business Review (90 min, Leadership + RevOps + Finance)**
Pre-meeting deck (8-10 slides): revenue vs. plan, pipeline health, efficiency metrics (CAC/payback/LTV:CAC), retention & expansion, GTM performance, risks, asks. Rule: max 1 chart per slide.

**Quarterly: QBR (Half-day)**
Morning: revenue health, GTM performance, pipeline confidence, customer & retention, what's working/not, steers.
Afternoon: board deck dry-run, key narratives, board asks.

**Quarterly: Board Meeting (2-3 hours)**
Board deck structure (8-10 slides): Executive Summary + Asks -> Revenue Performance vs. Plan -> Pipeline & Forecast -> Efficiency Metrics -> Retention & Expansion -> GTM Update -> Strategic Initiatives -> Asks & Decisions Needed. Golden rules: lead with narrative, show trends not snapshots, max 3 metrics per slide.

### Anti-Patterns

| Anti-pattern | Cost | Fix |
|---|---|---|
| **Meetings without pre-read** | 15 mins wasted reading slides | Require slide delivery 24h before |
| **Reviews without actions** | Decisions forgotten by Wednesday | Log every action: owner, due date, success metric |
| **Forecast as negotiation** | Forecasts become useless | Make forecast analytical, not emotional |
| **Dashboard theater** | 40 metrics shown, 5 matter | Max 3-5 metrics per meeting; every number connects to a decision |
| **Cadence without accountability** | Actions slip | Name the owner. Publish the due date. Review at next meeting. |
| **Activity data not validated** | Everything above pyramid is garbage | Monthly CRM audit: who's logging? Are stage changes real? |

### Norton Framework Additions

**Closed-Loop Feedback System**
Upward Flow: Activity -> Team Metrics -> Leadership Review -> Board.
Downward Flow: Board decisions -> Strategy adjustments -> Manager coaching priorities -> Rep behavior change.

Decision authority: Daily (rep self-manages) -> Weekly pipeline (manager) -> Weekly forecast (director) -> Monthly (VP) -> Quarterly (CRO/Board). Coaching doesn't happen separately; it happens DURING reviews. The cadence IS the coaching system.

**Discipline as AI Prerequisite**
The #1 differentiator between top performers and average performers using AI is NOT which tools they use. It's operating discipline. Jeremy Donovan (Insight Partners) on The Revenue Leadership Podcast, E61: "If I could only run one play: incredibly disciplined weekly deal reviews." Before any AI investment conversation, ask: "How tight is your operating rhythm?" (The Revenue Leadership Podcast, Kyle Norton; Episode 61, "GTM Strategy: 5 Insights from 500 B2B SaaS Orgs"; January 30, 2026).

**The Predictability Playbook**
Prerequisites: Directors/VPs must build predictable models with conversion rates, capacity constraints, and cost per output. Growth owns top-of-funnel math. RevOps owns instrumentation. Sales knows exactly how many meetings they're getting and what they need to convert. Aviv Canaani (Datarails CRO) on The Revenue Leadership Podcast, E64: "The real productivity is what matters." (The Revenue Leadership Podcast, Kyle Norton; Episode 64, "My Team Drives 4x Revenue Per AE vs Competitors"; March 4, 2026).

**Operating Rhythm Assessment**

| Dimension | Score 1 (Weak) | Score 3 (Adequate) | Score 5 (Strong) |
|-----------|---------------|-------------------|-----------------|
| Deal review frequency | Ad-hoc or monthly | Weekly but inconsistent | Weekly, never missed, structured |
| Pre-meeting data | None | Some data pulled manually | Automated packet 24h before |
| Decision logging | No actions recorded | Actions noted but not tracked | Actions logged, owned, reviewed next meeting |
| Forecast accuracy | +/-25%+ | +/-15-20% | +/-5-10% |
| Cross-functional sync | Teams don't talk | Monthly alignment meeting | Bi-weekly funnel review with shared metrics |
| Coaching integration | Coaching separate | Some coaching in reviews | Pipeline review IS the coaching system |

Scoring: 24-30 = ready for AI investment. 15-23 = fix cadence first. <15 = cadence rebuild required.

### The 10-Minute Board Defence

A structured alternative to the 40-slide board deck.

**The 5 Questions:**
1. **Are we on track?** Current quarter vs plan. One number, one trend line. No spin.
2. **Why?** Win rate by segment and motion. What's converting, what isn't. Name top 3 loss reasons.
3. **What changed?** Actions taken this quarter based on data. Experiment results, process changes, measured impact.
4. **What do we need?** Resource asks with projected ROI tied to specific conversion gaps.
5. **What's the risk?** Top 3 risks to hitting plan. Be specific.

Anti-pattern: 40-slide deck -> 2 hours to prepare -> board skips to bad news -> trust erodes.
The framework: 10-minute defence -> 30 minutes to prepare -> board gets answers immediately -> trust compounds.

---

## Implementation Notes

**Voice rules:**
- System first, blame never. The cadence is a tool, not a personality test.
- Use British spelling (organisation, centre, realise).
- Concrete over abstract. Always give examples. Never just say "good governance".
- Name the roles (CRO, VP Sales, Head of CS) and the forums (revenue dashboard, Demo and Retro).

**Boundary calls:**
- For the revenue dashboard build itself (panels, dashboards, data integration), see pipeline-visibility.
- Meeting architecture, ceremony agendas, and data pyramid are covered in the Revenue Cadence Reference section above.
- For client diagnostic and maturity assessment, see revops-diagnostic.

---

## Quick Reference: Ritual Triggers

Use this table to match a client situation to the ritual they need:

| Client situation | Ritual to run | Why |
| --- | --- | --- |
| No meetings at all | Start with Weekly Revenue Dashboard | This is the hub. Everything else feeds it. |
| Meetings happen but no decisions are made | Run 5P audit on existing meetings | The gateway. If a meeting fails 5P, cancel it. |
| No one knows when to escalate | Install signal-based decision rules | Gives people explicit rules: when a signal fires, escalate here. |
| Experiments never get killed | Demo and Retro + Decision Log | Kill rate is a visible health metric. Celebrate kills. |
| Strategy is unclear, disconnected from tactics | Strategy and Lever Review + strategy scorecard | This ritual connects the dots between quarterly strategy and weekly countermeasures. |
| Data is always outdated by decision time | Data Spine and Definition Review | Make data freshness a first-class ritual. If data fails, it's an incident. |
| Rituals keep getting cancelled or rescheduled | Reduce the calendar. Apply 5P strictly. | Keep only the rituals that produce decisions. |

---

## Related Skills

- **revenue-operating-cadence**: Core meeting architecture and ceremony agendas
- **pipeline-visibility**: Revenue dashboard build (panels, dashboards, data integration)
- **revops-strategy**: Strategic advisory and pipeline architecture
- **revops-forecasting**: Forecast methodology and breach rules
- **revops-metrics**: What metrics belong in which ritual

> Built by [Neon Triforce](https://neontriforce.com)
