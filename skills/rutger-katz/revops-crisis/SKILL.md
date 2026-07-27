---
name: "revops-crisis"
title: RevOps crisis triage
description: "Revenue crisis triage and emergency response when multiple systems break simultaneously. Use this skill when the user describes a CRISIS state: forecast missed for multiple quarters, win rate collapsing, pipeline coverage below 2.8x and falling, NRR crashed below 90%, multiple simultaneous system failures, loss of trust between functions, data that cannot be trusted, or scenarios like \"everything is broken,\" \"forecast is ±30% wrong,\" \"we are losing deals we should win,\" \"I cannot trust our data,\" \"sales blames marketing blames product,\" \"three quarters in a row we missed,\" \"board is panicking,\" or \"we need to save this quarter.\" Also trigger on \"we need emergency triage,\" \"nothing is working,\" \"where do we even start,\" or \"we are in firefighting mode.\" BOUNDARY: This is emergency response (what to fix FIRST when everything is broken). For detailed methodology after stabilisation, see revops-diagnostic and revops-four-capability-maturity-assessment. For specific domain fixes, see the relevant domain skill."
category: RevOps
---

# RevOps Crisis Triage & Emergency Response

You are a revenue operations crisis specialist. The key insight: **existing skills assume baseline functionality. They do not tell you what to do when multiple systems are broken at once.** A diagnostic session is useless if your data is garbage. A maturity assessment is academic if your teams do not talk to each other.

Your philosophy: In a crisis, speed of stabilisation beats perfection of diagnosis. Find the ONE thing that unlocks everything else, fix it, move to the next constraint. Do not try to fix six things. Focus relentlessly.

## Crisis Recognition

A crisis is not "we missed a number." A crisis is when multiple system layers break simultaneously and you can no longer trust the basic machinery.

### Threshold Triggers (Any ONE = Crisis Mode)

```
FORECAST:  ±30%+ variance for 2+ consecutive quarters (practice-based; calibrate per company stage)
WIN RATE:  Declined 5+ points over 3 quarters (e.g. 24% to 19%, below median 19% in 2026; Optifai, Clari)
PIPELINE:  Coverage below 2.8x AND falling month-over-month (below this, quota attainment falls to 52%; Clari, Fullcast, 2026)
RETENTION: NRR below 90% OR GRR below 84% (GRR median 84% in 2026, 75th percentile 91%; Optifai, 2026)
DATA:      Critical deal fields <70% complete (practice-based); CRM does not equal finance by >10%
TRUST:     Sales blames marketing blames CS blames product (3+ parties)
PEOPLE:    2+ top performers leaving in one quarter; open cynicism
```

### The Multi-System Failure Pattern

```
DATA BREAKS ──┬── PROCESS FAILS ──┬── PEOPLE FRACTURE
              │                    │
         NOBODY CAN EXECUTE RELIABLY
              │
         TRUST COLLAPSES → CRISIS MODE
```

If you see data corruption + unclear process + silent wars between functions, you're here.

## The Emergency Triage Protocol (4 Weeks)

### Week 1: DATA AUDIT. Can You Trust Your Data?

**The Rule:** If data quality <70% on critical fields, STOP. Nothing else matters.

```
EMERGENCY DATA AUDIT (sample 200 random open deals):

CRITICAL FIELDS                                   TARGET
□ Deal amounts populated?                         95%+
□ Close dates updated in last 14 days?            95%+
□ Stage assigned and makes sense?                 98%+
□ Contact role(s) assigned?                       80%+
□ Activity logged in last 30 days?                85%+
□ Next step documented?                           80%+
□ Won/lost reason populated (closed deals)?       95%+
□ Customer name matches finance system?           99%+

SCORING:
<70% at target = DATA CRISIS. Run 5-day blitz before anything else.
70-84%         = ACCEPTABLE. Proceed with caveats on all forecasts. Target is 85%+ for reliable GTM execution (practice-based).
>85%           = GOOD. Proceed with confidence (data quality directly correlates with forecast accuracy; practice-based).
```

**The 5-Day Data Blitz (if <70%):**
- Day 1: Sort deals by completeness. Find worst teams and reps. Root cause: lazy? unclear definitions? tool issue?
- Days 2-3: RevOps + CRM admin run bulk updates on objective data. Pull in worst-data reps to update their own deals. Fix validation rules.
- Days 4-5: Establish daily data standup (15 min). Weekly data audit report. Assign data owner per team.

### Week 1-2: CASH DIAGNOSIS. What's the Immediate Revenue Risk?

**The Rule:** In a crisis, protect cash first. Assign senior people to the top 10 at-risk deals.

```
THE 2-HOUR CASH DIAGNOSIS:

1. Pull all open deals closing in 30-60 days + renewals due in 30-90 days
2. Stack rank by € amount
3. Flag at-risk: no recent activity, no champion, competitive threat,
   economic buyer not engaged
4. Top 10 at-risk = your downside exposure number for leadership
5. Assign executive owner to each (CRO or VP level, not deal owner)
6. Define next tangible action + deadline (this week, not "soon")
```

**Start the Daily Cash Standup (Monday of Week 2):**
15 minutes. Every day. CRO, VP Sales, VP CS, RevOps.
One line per deal: status, next action, owner, date. This is a war room. Run for 60 days.

### Week 2-3: ROOT CAUSE. Six Stages of Check in FAST Mode

Reference: For full methodology, see revops-diagnostic skill. For maturity assessment after stabilisation, see revops-four-capability-maturity-assessment.

```
DAY 1: PURPOSE    . Clear, agreed definition of success? Target conflict?
DAY 2: DEMAND     . Real market demand? Right ICP? Problem still urgent?
DAY 3: CAPABILITY . Skills, tools, structure match the motion we are running?
DAY 4: FLOW       . Pick 20 random deals. Where do they stall? Bottleneck?
DAY 5: SYSTEM CONDITIONS & THINKING
       Data trusted? Stage exit criteria defined? Leadership mental model
       matches reality?
```

**Output: One-Page Root Cause Summary**

```
CRISIS:     [One-line description with numbers]
EVIDENCE:   [Data that proves it is real]
ROOT CAUSE: □ Purpose □ Demand □ Capability □ Flow □ System □ Thinking
IMMEDIATE FIX: [The ONE thing that unblocks everything else]
OWNER:      [Name]
TIMELINE:   [1-3 weeks]
```

### Week 3-4: CONSTRAINT IDENTIFICATION

Reference: For full framework, see revops-four-capability-maturity-assessment.

Score each 1-2 (crisis mode; nuance comes later):

```
GOVERNANCE:       Decisions being made? Steering mechanism exists?
ENABLEMENT:       Data/process/tool stack working?
REVENUE ENGINE:   Sales/CS engine producing?
CUSTOMER INSIGHT: Understand ICP and why you're winning/losing?

Emergency constraint = the ONE scoring 1 when others are at 2.
All four at 1? Start with Governance (you need a steering mechanism first).
```

**Constraint Unlock Logic:**

```
Governance = 1:  Install daily standup. Assign decision driver (CRO).
                 Unlock: Everything clearer because leadership knows what matters.

Enablement = 1:  Data audit (done Week 1) plus define 3 non-negotiable processes.
                 Unlock: Teams can execute consistently.

Revenue = 1:     Win rate analysis. Talk to 5 lost deals fast.
                 Unlock: Know where to focus (discovery? closing? multi-threading?)

Insight = 1:     Pull top 5 wins and 5 losses. Pattern-match.
                 Unlock: Stop guessing about ICP.
```

## The 30-60-90 Crisis Response Plan

### Days 1-30: STABILISE

```
□ Data quality audit complete; blitz if needed (target: 85%+)
□ Top 10 at-risk deals identified with exec sponsors
□ Daily cash standup running
□ Root cause identified (which Six Stage is broken)
□ First structural fix in place (stage criteria, validation rules, or governance)
□ One quick win executed (visible improvement, however small)
□ All non-essential projects halted
```

### Days 31-60: DIAGNOSE & FIX

```
□ Full IFA diagnostic complete (reference revops-diagnostic)
□ Capability maturity assessed (reference revops-four-capability-maturity-assessment)
□ Fix roadmap drafted: 3 initiatives max, prioritised by constraint unlock
□ First major structural change: design complete, stakeholders mapped
□ Change management started (reference revops-change-management)
□ Weekly leadership update: "Here is what broke. Here is how we fix it."
□ Measure Day 1 baseline vs. now (data quality, forecast accuracy, win rate)
```

### Days 61-90: REBUILD

```
□ First structural change at 70%+ adoption
□ Initiatives #2-3 in design (NOT launched yet; don't launch 3 at once)
□ Operating cadence established (reference revenue-operating-cadence skill):
  Weekly ops review (30 min), monthly deep-dive (90 min), quarterly reset
□ Forecast rebuilt with proper methodology (reference revops-forecasting)
□ Metrics dashboard live and trusted (reference revops-metrics)
□ Team sentiment: pulse survey shows improved trust
□ Hand off to revops-diagnostic and revops-four-capability-maturity-assessment for deeper work
```

## AI & Automation for Crisis Response (2026)

**The efficiency gap:** Manual crisis response (spreadsheets, daily calls, human analysis) is fast, but reactive. 2026 crisis response augments humans with AI for speed and pattern detection.

### Real-Time Data Monitoring & Alerting

**Replace daily manual forecast calculations with automated flagging:**
- **Streaming data pipelines:** Supabase or similar warehouse ingests CRM changes in real-time. Fivetran syncs from Salesforce, HubSpot, finance systems continuously.
- **Anomaly detection:** ML model flags when forecast variance exceeds thresholds (e.g. 3+ deals slip in one day; deal values drop 20%+; win rate shifts >2 points).
- **Slack alerts:** War room receives notifications when anomalies trigger, not when humans remember to check.
- **Outcome:** Detect crises 3-5 days earlier than manual weekly reviews.

### AI-Driven Root Cause Analysis

**Instead of humans debating root cause for 2 weeks:**
- **Claude API integration:** Feed war room data (deal activity, stage transitions, person changes, win-loss reasons, forecast variance trends) into Claude for structured root cause analysis.
- **Pattern extraction:** Claude identifies what changed (e.g. "discovery duration extended from 18 to 31 days in the last 6 weeks"; "win rate collapsed specifically on deals with no C-suite contact").
- **Constraint mapping:** Maps findings to Governance / Enablement / Revenue / Insight framework automatically.
- **Outcome:** Root cause analysis moves from "opinions" to "data-driven facts" in 1 week instead of 2-3.

### Predictive Health Scoring

**Forecast deal health before it fails:**
- **Model inputs:** Deal age, stage duration, activity cadence, champion engagement, competitive signals, budget confirmation status.
- **Real-time scoring:** Every deal in pipeline scored continuously. War room sees Red (high risk), Yellow (watch), Green.
- **Automate actions:** CRM workflow triggers outreach when deals fall to Red; escalates to rep manager if no response in 24 hours.
- **Outcome:** Identify at-risk deals on Day 1 of risk, not Day 20.

### War Room Tech Stack (2026)

**Minimum stack for crisis war room:**
- **Real-time dashboard:** Supabase-backed analytics (Metabase or Superset) showing live pipeline coverage, forecast variance, deal health scores, top 20 deals by status. Refresh every 15 minutes, not daily.
- **Slack as command centre:** War room receives alerts from data pipelines. Decisions logged as Slack threads (timestamped, searchable, shared context).
- **Shared CRM view:** Large screen or shared tab showing live Salesforce/HubSpot pipeline for deal-level discussions.
- **Action tracking:** Asana, Linear, or simple spreadsheet for action items; automated reminders every 6 hours for overdue actions.

**Avoid:** Spreadsheet-only tracking. By Day 3, spreadsheets diverge from reality. Centralise data in warehouse; surface via dashboard.

---

## Four Crisis-Specific Playbooks

### A: THE FORECAST CRISIS . "Missed 3 quarters in a row"

```
ROOT CAUSE PATTERNS:
1. Bad data (amounts missing, close dates stale, wrong stages)
2. Sandbagging (reps entering deals late, hiding pipeline)
3. Pipeline inflation (stalled deals still counted, no stage exit criteria)
4. Wrong methodology (rep confidence instead of data-driven)

EMERGENCY FIX (Week 1-2):
• Build shadow forecast from scratch (CRM data multiplied by finance validation)
• Compare to current forecast. Variance greater than 15% equals data problem.
• Run 3 methods: rep probability, historical conversion, high-confidence only
• Take the lowest number. That is your realistic forecast.
• Daily: "How many deals closed that were or were not in forecast?"

STRUCTURAL FIX (Week 3-8): reference revops-forecasting skill
• Define stage exit criteria (what moves a deal forward)
• Choose forecast method (start Conservative, move to Blended after 2Q)
• Weekly deal inspection (manager validates every deal in qualified stages)
• Monthly accuracy measurement: target +/- 10% (achievable within 2-3 quarters; AI-driven forecasting teams report variance reduction from 30-40% to under 10%; Forrester, 2026)
```

### B: THE PIPELINE CRISIS . "Coverage at 2.1x and falling"

```
ROOT CAUSE PATTERNS:
1. Top-of-funnel dried up (lead volume down, channels underperforming)
2. ICP drift (selling to wrong people; lots of leads, few convert)
3. AEs not prospecting (no pipeline generation from existing accounts)
4. Qualification too strict (over-screening legitimate opportunities)
5. Slow velocity (deals stuck in early stages, capacity full of Discovery)

EMERGENCY FIX (Week 1-2):
• Pipeline audit: coverage, composition by source, velocity check
• IF top-of-funnel: Activate dormant prospects, refocus SDRs to outbound
• IF ICP drift: Pull win and loss for 10 deals, identify winning attributes
• IF AEs passive: Pull high-usage existing customers, create upsell list
• IF qualification wrong: Blinded test with 20 rejected leads
• IF velocity slow: Manager sweep of 60+ day stalled deals

STRUCTURAL FIX (Week 3-8): reference gtm-planning plus revops-metrics skills
• Pipeline generation plan with source owners and weekly accountability
• ICP enforcement: score every lead, only greater than or equal to 60% accepted as SQL
• Velocity targets by stage (Discovery 21-35 days, Proposal 14-21 days; practice-based; adjust by stage funnel exit rates)
• Quarterly pipeline planning: [target divided by win rate times 1.3; practice-based] equals pipeline needed (coverage rule: reps at 3.2x+ weighted coverage hit quota 89% of the time; below 2.8x, 52%; Clari, Fullcast, 2026)
```

### C: THE CHURN CRISIS . "NRR crashed to 85%"

```
ROOT CAUSE PATTERNS:
1. Product-market fit erosion (competitor better, market shifted)
2. CS under-resourced (bad onboarding, no health checks, slow support)
3. No health scoring (cannot identify at-risk accounts, surprise churn)
4. Renewal process broken (starts too late, single-threaded)
5. Acquisition quality (winning wrong-fit customers, over-promising)

EMERGENCY FIX (Week 1-2):
• Churn diagnosis: rate by cohort, timing, reason, segment
• At-risk identification: all renewals due in 90 days, flag 2+ risk indicators
  (no activity 30d, usage declining, unresolved tickets, no contact 60d)
• Executive save calls on greater than EUR50K ARR at-risk accounts (CRO and VP, not CSM)
• Quick fix based on pattern:
  CS under-resourced. Senior CSM on highest-risk accounts
  No health scoring. Build simple score this week (5-7 indicators)
  Renewal process. Start renewals 120 days out, not 30 days (practice-based)
  Acquisition quality. Pre-flight check before deal close

STRUCTURAL FIX (Week 3-8): reference cs-operations skill
• Health scoring system with escalation rules
• Renewal calendar visible 120 days in advance
• CS coverage model by segment with right ratios
• Expansion sourcing: monthly identification of growth signals
```

### D: THE TRUST CRISIS . "Sales blames marketing, CS blames product"

```
ROOT CAUSE: No shared metrics, no shared cadence, no shared accountability.
Functions optimise independently. Metrics conflict. Blame cycle follows.

EMERGENCY FIX (Week 1-2):
• ONE shared dashboard all functions see daily (ARR, pipeline, churn, CAC)
• Shared definitions: Get all VPs in a room. "What is a qualified lead?"
  Agree on ONE definition per handoff. Make it rule.
• ONE weekly meeting: CRO, VP Sales, VP Marketing, VP CS, RevOps.
  45 min fixed time. Metrics. Issues. Last week actions. Next actions.
• Break finger-pointing: 1-on-1 with loudest voices. "What would need to be true
  for you to trust this team?" Fix the specific gap, not the politics.
• Quick win: Fix ONE handoff visibly (e.g. lead scoring with Sales input)

STRUCTURAL FIX (Week 3-8): reference revenue-operating-cadence skill
• Shared metrics dashboard (RevOps owns, all functions see)
• Shared definitions document (one-pager per major concept)
• Weekly governance meeting with decision log
• Cross-functional playbooks for major motions
```

## People & Leadership During Crisis

**The psychology of crisis:** When multiple systems fail simultaneously, people enter blame mode, confidence collapses, and senior leadership fractures. Technical fixes mean nothing if the team does not trust each other or leadership.

### Managing the Blame Cycle

**What happens:** Sales says "Marketing gave us garbage leads." Marketing says "Sales did not follow up." CS says "Product is broken." Product says "Sales over-promised."

**Why it happens:** When outcomes are bad, people protect their turf. Blame is cheap and feels like control.

**What to do:**
- **Frame it as system, not person.** In your first all-hands or leader meeting, explicitly say: "We did not miss forecast because Sales is lazy. We missed because our data is bad and our process is unclear. That is on all of us."
- **Show the data.** Display the audit results. Make the problem visible and objective. "Look: 30% of deals are missing close dates. That is not laziness. That is a process gap."
- **Redirect blame to constraint.** "We are in this crisis because our demand gen fell short AND sales velocity slowed AND churn spiked. That is three independent things. We fix them together, not by blaming each other."
- **Assign ONE decision maker per crisis phase.** CRO owns forecast crisis. VP CS owns churn crisis. Removes ambiguity about who is accountable. Everyone else executes.

### Rebuilding Confidence

**How crisis erodes confidence:** People see forecasts miss. They watch the board worry. They worry about job security. Top performers start interviewing at competitors.

**What to do:**
- **Show progress daily.** In the daily standup, call out the smallest wins. "We recovered 3 deals yesterday." "Data quality improved 2 points." Momentum matters more than magnitude.
- **Communicate the plan visibly.** Share the 30-60-90 plan with the full team. Remove mystery. "Here is what we are fixing. Here is the order. Here is where we are in the roadmap." People believe in plans they can see.
- **Senior leader involvement on deals.** When the CRO or CEO calls a customer personally, reps feel supported. This is not optional in crisis; it is your top confidence lever.
- **Celebrate structural wins.** When you ship new stage exit criteria or activate a new pipeline source, call it out. "We just reduced discovery time by 4 days on this cohort. That is structural progress."

### Difficult Conversations

**When to have them:**
- A rep is underperforming and the team knows. Address it in Week 2, not Week 6. Ambiguity kills morale.
- A manager is contributing to the crisis (e.g. hoarding deals, not coaching reps). Address it 1-on-1 immediately.
- A function is blocking progress (e.g. Product refuses to unblock an integration; Finance delays data access). Escalate the constraint to the CEO, not the person.

**How to run them:**
- **Focus on the constraint, not the person.** "You are a great manager, but we need real-time deal visibility in the next 2 days. What do you need from RevOps to make that happen?" vs. "You are not giving us transparency."
- **Make it binary.** "Do you commit to delivering X by this date?" Yes or no. No "maybe" or "I will try." In a crisis, maybes kill timelines.
- **Escalate quickly if resistance.** If someone refuses to execute on a crisis priority, loop in their boss or the CEO. Crisis mode is not time for consensus building.

---

## What NOT To Do In A Crisis

```
✗ Change comp plans mid-quarter. Adds chaos on chaos. Lock it; announce next Q.
✗ Fire the VP Sales immediately. Most of the time it is a system problem, not a person problem (Deming).
  Do the diagnostic first. If it IS a person problem, you will know in 2 weeks.
✗ Buy a new tool. Technology does not fix broken processes. Fix process first.
✗ Launch 10 initiatives. Scattered focus amplifies crisis. Fix ONE thing hard.
✗ Hide numbers from the board. They will find out. Show the bad numbers plus the plan.
✗ Blame external factors. "Market is down" explains variance but does not fix revenue.
✗ Skip the daily standup. It IS your information gathering. Commit for 60 days.
✗ Fix data plus process plus people simultaneously. Pick ONE. Usually: data first,
  then process (now you have clean data), then people (trust rebuilds when
  data plus process work).
```

## How to Use This Skill

**"Everything is broken":** Start with Crisis Recognition followed by Emergency Triage (4 weeks) followed by 30-60-90 plan.

**"Forecast is unreliable":** Playbook A. Shadow forecast followed by pattern identification followed by structural fix.

**"Not enough pipeline":** Playbook B. Audit composition followed by root cause followed by targeted activation.

**"Losing customers":** Playbook C. At-risk identification followed by executive save calls followed by structural CS fix.

**"Teams do not trust each other":** Playbook D. Shared dashboard followed by shared definitions followed by weekly meeting.

**"Data is garbage":** Run the Data Quality Checklist first. Nothing else works until data is clean.

**After Day 90:** Hand off to revops-diagnostic and revops-four-capability-maturity-assessment for the deeper work. Crisis mode is about stabilisation. Long-term improvement is a different skill set.

> Built by [Neon Triforce](https://neontriforce.com)
