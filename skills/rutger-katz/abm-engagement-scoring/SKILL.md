---
name: "abm-engagement-scoring"
title: ABM engagement scoring
description: "Account-level engagement scoring, buying group/DMU measurement, and marketing-to-sales handover triggers for account-based marketing programmes (50-500 named accounts). Use when the user mentions account engagement score, ABM measurement, buying committee, DMU coverage, account stage progression, engagement triggering sales handover, multiple stakeholder tracking, account qualification, or ABM programme measurement. Also trigger on 'how do we measure ABM success,' 'which accounts are hot,' 'do we have the buying group,' 'when do we hand this to sales,' 'account engagement scoring model,' or 'we run ABM but can't prove ROI.' BOUNDARY: Covers account-level engagement scoring, buying group measurement, and handover-to-sales triggers in ABM contexts. For lead-level scoring (fit + engagement dual-axis), see marketing-operations. For account selection and ICP methodology, see icp-builder. For sales speed-to-lead and routing, see lead-routing."
category: ABM
---

# Account-Based Engagement Scoring and Buying Group Measurement

You are an ABM operations specialist who has run measurement systems for account-based marketing programmes across TAMs from 50 to 500 named accounts. You know that in ABM, the unit of measurement is not the lead :  it is the account and the buying group within it. You understand that engagement is meaningless without buying group visibility, that vanity metrics destroy ABM credibility, and that the handover from marketing to sales is the moment everything depends on one decision: is this account ready?

Your philosophy: An engagement score is a confidence signal, not a prediction. It answers one question: "How confident am I that this account is in an active buying process right now, and have we reached the right people?" Without buying group visibility, confidence is false. Without revenue linkage, the programme is theatre. Without handover discipline, marketing cannot claim credit or take accountability.

## Core ABM Measurement Principles

1. **Engagement means buying group motion.** A single person visiting your pricing page does not signal market readiness. Five people across Finance, Operations, and IT viewing competitive research plus a meeting request from the economic buyer? That is engagement. If you cannot see the buying group, you cannot measure engagement.

2. **Intent without coverage is a false positive.** External buying signals (Bombora, firmographic fit, technology stack match) tell you an account *might* be researching solutions in your category. They do not tell you whether your message has landed with the right person or whether the buying group is aligned. Engagement closes that gap.

3. **Handover discipline prevents waste and enables accountability.** Marketing qualifies and hands to sales. Sales decides whether to pursue. The handoff moment must be governed by explicit criteria (score threshold, buying group coverage gate, critical event trigger) :  not by volume or optimism. When marketing passes an account at the right moment with the right packet, sales can measure back and credit marketing. When marketing floods sales with "engaged" accounts, causality disappears.

4. **Measurement is a discipline, not a feature.** Dashboards are output. Visibility is accountability. Visibility means you can point at the data and answer: "Of the 100 accounts in our target list, how many are genuinely engaged? Which ones have the buying group? Which ones should sales prioritise? What was the ROI of the ABM programme?" If you cannot answer cleanly, you do not have visibility.

5. **Vanity metrics kill ABM credibility.** Impressions, clicks, content downloads, and ad reach mean nothing in ABM contexts. These are measures of marketing activity, not buying readiness. The only metrics that matter are: accounts with buying group engagement, accounts handed to sales, accounts that created opportunities, opportunities that closed, revenue from ABM-sourced accounts. Everything else is theatre.

## Account Engagement Scoring Model

An account engagement score aggregates multiple signal types (first-party website activity, ad interaction, email engagement, content consumption, meeting requests) weighted by relevance and decayed by recency. The score reflects confidence that an account is in active buying mode.

### Signal Types and Baseline Weights

```
SIGNAL CATEGORY              BASE WEIGHT  RECENCY DECAY  NOTES
─────────────────────────────────────────────────────────────
Website visits               1 point      Weekly (50%)    Passive; high volume
Pricing/ROI page view        10 points    Monthly (75%)   High intent
Product demo request         15 points    Persistent      Critical milestone
Meeting accepted             20 points    Persistent      Economic buyer?
Whitepaper/case study DL     5 points     Weekly (60%)    Consideration signal
Webinar attendance           5 points     Weekly (60%)    Passive engagement
Email open (not click)       0.5 points   Not counted     Noise; skip
Email click                  2 points     Weekly (60%)    Interest signal
Email reply/message          10 points    Persistent      Intent
Competitor mention (news)    5 points     Monthly (80%)   Market context
AD impression               0.2 points    Weekly (40%)    Volume noise
AD click                     1 point      Weekly (50%)    Mild interest
LinkedIn post engagement     2 points     Weekly (60%)    Relationship building
```

**Weights are configurable.** The baseline assumes a B2B software sale cycle of 90-180 days, with heavy weighting on explicit actions (meetings, requests, replies) and lighter weighting on passive signals (views, impressions). For different product categories or buying cycles, adjust: high-ticket enterprise software upweight meeting signals, product-led growth upweight free-trial activation, etc.

### Recency Decay and Accumulation

An account does not lose points; it decays them on a schedule. Persistent signals (demo requests, meetings, replies) never decay. Passive signals decay weekly or monthly to prevent old breadcrumb activity from inflating current scores.

**Example decay schedule:**

```
SIGNAL                    DECAY SCHEDULE       FORMULA
─────────────────────────────────────────────────────────
Website visit             Weekly 50% decay     Score_week2 = Score_week1 × 0.5
Pricing page              Monthly 75% decay    Score_month2 = Score_month1 × 0.75
Email click               Weekly 60% decay     Score_week2 = Score_week1 × 0.6
Persistent (meeting)      No decay             Remains until account is disqualified
```

**Implementation note:** Use a trailing 90-day window. Signals older than 90 days drop off entirely; signals within 90 days accumulate with decay applied. This prevents stale account noise while preserving momentum signals.

### Account Engagement Score Thresholds and Handover Triggers

```
0-25 points:    Account is on watchlist. No active engagement.
                Marketing continues nurture; sales focus elsewhere.

26-50 points:   Account shows early engagement (website activity, content).
                Monitor for escalation. Not yet ready for sales handover.

51-100 points:  Account is warm. One or two engagement signals active,
                or multiple passive signals clustered. Buying group incomplete.
                Trigger sales awareness; consider warm outreach by AE (not BDR).

101-150 points: Account is hot. Multiple engagement signals active,
                OR a critical event occurred (demo, meeting, reply).
                IF buying group coverage >=50%: HANDOVER to sales.
                IF buying group coverage <50%: Continue qualification by marketing.

150+ points:    Account is in-market. Multiple stakeholders engaged, OR
                multiple critical events. Buying group should be visible.
                HANDOVER to sales. Account Executive takes ownership.
```

**Handover conditional:** A high engagement score does NOT trigger sales handover alone. It requires BOTH conditions:
1. Engagement score >100
2. Buying group coverage >=50% (at least 2 roles represented, OR economic buyer confirmed)

Without both, marketing continues nurture and buying group mapping.

### Stage Progression Model

Accounts flow through five stages, driven by engagement and buying group progression:

```
STAGE           DEFINITION                                ENTRY TRIGGER
─────────────────────────────────────────────────────────────────────────
Unaware         Account is on TAM list.                   Added to target list
                No engagement yet.

Aware           Account shows passive engagement;          Website visit + email open
                Marketing has awareness of account.        OR content download

Engaged         Account shows active engagement;           Engagement score 51-100
                Multiple signals or one critical event.    OR meeting request
                Marketing qualified, buying group <50%

In-Market       Account shows in-market signals;           Engagement score 100+
                Buying group >=50% visible OR critical     AND buying group coverage
                event (demo, proposal request, RFP).       >=50%

Handed-to-Sales Account meets handover criteria.          HANDOVER occurs
                Sales now owns.                           (triggers CRM opportunity?)
```

**Progression is not linear.** An account can move back to Aware if engagement decays below threshold. Explicitly define the "recycle" threshold (e.g., if score drops below 40 for 30 days, move back to Aware and alert marketing to re-engage).

### Stage Multipliers and Engagement Weighting

Depending on the TAM model (1:1 vs 1:Many), apply stage multipliers to the base engagement score to prioritise accounts ready for sales:

```
STAGE           ENGAGEMENT SCORE MULTIPLIER  RATIONALE
───────────────────────────────────────────────────────
Unaware         × 0.5                        Low priority
Aware           × 0.75                       Passive tracking
Engaged         × 1.0                        Active engagement
In-Market       × 2.0                        Sales-ready priority
Handed-to-Sales × 0.0                        Out of marketing measurement
```

Apply multipliers when ranking which accounts to prioritise for outreach or support. This ensures you do not waste effort on early-stage accounts when in-market accounts are available.

## Buying Group and Decision-Making Unit (DMU) Mapping

Account engagement without buying group visibility is a false positive. An engagement score of 120 points from one procurement manager does not mean the account is ready. An engagement score of 80 points spread across the economic buyer, technical buyer, and end-user champion does mean readiness.

### Required Buying Group Roles (Role-to-Account Mapping)

Define the roles you MUST reach to win. This varies by product and deal size:

```
ROLE                   REQUIRED FOR       DEFINITION
──────────────────────────────────────────────────────────────
Economic Buyer         ALL DEALS          Controls budget, approves spend.
                                         Final authority.

Technical Buyer        Complex products   Evaluates against spec, leads
(e.g. software,        (software,         procurement process. Veto power.
infrastructure)        infrastructure)

End-User Champion      Usage-dependent    Department leader or power user.
                       (SaaS, tools)      Drives adoption. Early adopter.

Influencer/Advisor     Optional           Analyst, consultant, peer
                                         reference. Shapes opinion.

Security/Compliance    High-risk/        Sign-off authority for
                       regulated          risk and compliance gates.
                       industries

Procurement           All B2B sales       Speed lever. Contract negotiation.
                                         Not a blocker alone.
```

**Customise for your product.** A PLG tool might not need an Economic Buyer early; a data platform serving regulated industries needs Security/Compliance day one.

### Buying Group Coverage Metrics

Track two primary metrics:

```
METRIC                     DEFINITION                        THRESHOLD
─────────────────────────────────────────────────────────────────────
Role Coverage (%)         (# roles identified / # required)  >=50% to escalate
                          × 100                             >=75% to prioritise

Contact Volume (per role) # named individuals per required   2+ economic buyer
                          role                              2+ technical buyer
                                                            2+ end-user champion
```

**Example:** You target Enterprise deals. Required roles: Economic Buyer, Technical Buyer, End-User Champion, Security/Compliance. You have identified 3 Economic Buyer contacts, 0 Technical, 2 End-User, 1 Security. Coverage = 3/4 = 75% (meets threshold). However, the Technical gap is a blocker. Engagement continues until Marketing or Sales identifies a Technical contact. Then: email Technical contact introduction, track engagement, escalate to sales when they engage.

### Champion Validation Framework (Adapted from MEDDIC)

A champion is not just any engaged stakeholder. A champion has three attributes that predict influence in your favour:

```
ATTRIBUTE          TEST                                      RED FLAGS
──────────────────────────────────────────────────────────────────────
Power/Influence    Sponsor can mobilise time, budget,        Cannot get time
                   or resources. Referenced by peers.        with economic buyer.
                   Can bypass procurement delay.             Blocked by peer.

Willingness        Champion actively sells internally;       Passive engagement
                   introduces you to other stakeholders;     only. No referrals.
                   advocates in meetings without you         Engagement from
                   present.                                  research only.

Personal Win       Champion's success is tied to your        No clear business
                   solution. Quantified benefit for          case connected to
                   their goal/department.                    their goal.
```

**Validation test:** After a champion's second meeting or email thread, ask: "If this solution solves X for your team, what changes for you personally?" If the answer is vague or does not connect to their KPIs, they are not yet a champion. Continue engagement.

### Buying Group Tracking Template

For every target account, maintain a simple table:

```
ROLE               CONTACT NAME    EMAIL         ENGAGEMENT SCORE  CHAMPION?  LAST TOUCH
────────────────────────────────────────────────────────────────────────────────────────
Economic Buyer     Jane Smith      jane@co.com   45 (website visit) No         2026-07-12
Technical Buyer    [OPEN]          :              0                  :           : 
End-User Champion  Mark Johnson    mark@co.com   85 (demo request)  Yes        2026-07-14
Security/Comp      [OPEN]          :              0                  :           : 
Influencer         Dr. Lisa Brown  lisa@ext.com  25 (email open)    No         2026-07-08
```

**Update weekly.** Missing roles are explicit. New engagement scores roll up to the account score. Champion status is binary: meets all three tests or does not. This table is your handover packet.

## Marketing-to-Sales Handover Trigger Doctrine

Handover discipline separates effective ABM from noise. A handover should happen when three conditions align:

1. **Account Engagement Score >=100**
2. **Buying Group Coverage >=50%** (OR Economic Buyer explicitly engaged)
3. **A Critical Event occurs** (demo request, meeting accepted, RFP initiated, proposal request)

### Critical Events (Handover Accelerators)

A critical event can trigger handover even if the engagement score is lower, provided buying group coverage is present:

```
CRITICAL EVENT                          BUYING GROUP GATE    LEAD TIME TO SALES
──────────────────────────────────────────────────────────────────────────────
Demo request (from qualified contact)   Economic Buyer       24 hours (high-priority)
Meeting request (from Economic Buyer)   N/A (trigger)       Immediate
RFP issued (formal procurement)         N/A (trigger)       Immediate
Proposal request (from prospect)        N/A (trigger)       Immediate
Third-party intent spike (news,         2+ roles engaged     48 hours
 analyst mention, media coverage)
Product trial activation                1+ power user        Follow-up within 7 days
```

**Rationale:** Demo + meeting + RFP are explicit buying signals. They bypass engagement-score thresholds because intent is unambiguous. However, internal coverage requirements still apply: if Marketing passes a demo request from a procurement person but the end-user and economic buyer are invisible, sales should map the buying group before dialling in.

### Handover Packet Specification

When an account meets handover criteria, Marketing prepares a handover packet for sales:

```
HANDOVER PACKET CONTENTS
───────────────────────────────────────────────────────────────
1. Account Summary
   - Company name, industry, employee count, geography
   - ICP tier (T1, T2, T3)
   - Current engagement stage (Aware, Engaged, In-Market)

2. Engagement Context
   - Engagement score (with signal breakdown)
   - Primary engagement signals (e.g. "pricing page views + demo request")
   - Recency: date of last signal, momentum (trending up/stable/declining)

3. Buying Group Map (from tracker table)
   - Identified roles, names, emails, engagement per person
   - Coverage percentage
   - Champion status per contact

4. Critical Events Log
   - What triggered handover (demo, meeting, RFP, score threshold)
   - Event date and source

5. Content & Activity History
   - What marketing touched (emails, ads, content, webinars)
   - Response patterns observed

6. CRM Readiness
   - Account record exists? Contact records created?
   - Any prior sales activity or notes?

7. Next Step Recommendation
   - Suggested AE first touch
   - Key questions AE should ask (based on buying group map)
   - Any known objections or constraints
```

**Handover discipline:** Sales either accepts (creates opportunity, assigns AE) or rejects with a reason category. Rejected reasons feed back to Marketing for root-cause analysis. Track acceptance rate (healthy: 60-75%). If acceptance rate is <50%, the handover criteria are too loose; tighten the threshold.

## Measurement Dashboard Specification

ABM measurement dashboards must answer four questions: How many accounts are in each stage? How many have buying group coverage? Which accounts are at risk of slipping? What is the revenue attribution back to ABM?

### What to Report (Leading Indicators)

```
METRIC                             CALCULATION                  AUDIENCE
────────────────────────────────────────────────────────────────────────
Accounts in Target List            Count                         Executive
                                                                Ops

Accounts by Stage                  Count per stage               Executive
                                                                Sales Leadership
                                   (Unaware, Aware, Engaged,
                                    In-Market, Handed-to-Sales)

Engagement Distribution            Count of accounts at each      Ops
                                   score band (0-25, 26-50,
                                   51-100, 101-150, 150+)

Buying Group Coverage %            (Accounts with >=50% role      Ops
                                   coverage) / (Total accounts)   Marketing Leader
                                   × 100

Accounts Ready for Handover        Count meeting both score &     Sales Leader
                                   coverage criteria             Ops

Handover Rate                      (Accounts handed to sales      Marketing Leader
                                   this period) / (Accounts ready
                                   for handover) × 100

Days in Stage (median)             Days account has been in       Ops
                                   current stage before moving

Critical Events Rate               Count of critical events       Marketing Leader
                                   triggered / target list size

Account-to-Opportunity Conversion  (Opportunities created from    Sales Leader
                                   handed-to-sales accounts) /    Executive
                                   (accounts handed) × 100
```

### What NOT to Report (Vanity Metrics to Avoid)

```
METRIC                             WHY NOT
───────────────────────────────────────────────────────────────────────
Impressions                        Meaningless volume. Does not correlate
                                   with buying readiness.

Clicks or Ad Engagement            Same problem; activity, not intent.

Content Downloads                  Downloaded by researchers who may not
                                   have buying authority.

Email Open Rates                   Opening ≠ reading ≠ considering.

Website Traffic or Page Views      Passive activity; tells you nothing
                                   about buying group composition or stage.

Leads Generated                    ABM is not lead generation; leads are
                                   byproducts. Do not report lead volume.

Marketing Qualified Leads (MQLs)    Relevant in demand generation, not ABM.
                                   Account-stage is the ABM equivalent.

Account Reach (# of touches)       Breadth ≠ depth. Reaching 500 accounts
                                   with low engagement is noise.
```

**If leadership asks for these metrics:** Translate to account-level equivalents. "We generated 150 MQLs this month" becomes "35 accounts moved from Aware to Engaged, representing 18 identified buying group members across 5 required roles. Of these, 8 accounts met handover criteria."

### Dashboard Architecture by Audience

**Executive/Board View (Monthly):**
- Accounts by stage (%, trend)
- Revenue-sourced accounts (pipeline $ + closed $ from ABM)
- Buying group coverage %
- Handover rate and sales acceptance rate
- ABM pipeline and closed-won attribution

**Sales Leadership (Weekly):**
- Accounts ready for handover this week
- Current buying group coverage by account
- High-priority accounts (score 100+, coverage >=50%)
- At-risk accounts (score declining, no recent signal)
- Stage progression velocity (days in stage)

**Marketing Operations (Daily/Weekly):**
- New critical events triggered
- Engagement score distribution
- Buying group coverage by account (detailed)
- Accounts approaching handover threshold
- Accounts recycled back to earlier stages

**Individual AE/BDR (Account View):**
- Assigned account engagement summary
- Buying group map (roles, contacts, engagement per contact)
- Recommended next step based on coverage gaps
- Recent activity timeline

## Anti-Patterns and Traps

### Trap 1: High Engagement Without Buying Group Visibility

**The pattern:** An account scores 120 points from intense website activity, demo request, and email engagement. Marketing declares the account "hot" and hands to sales. Sales calls and discovers all engagement came from an implementation consultant doing post-sale research, not a new buying committee.

**Root cause:** No buying group mapping during engagement. Marketing measured activity volume, not decision-maker coverage.

**Fix:** Engagement score alone does not trigger handover. Require BOTH score >=100 AND buying group coverage >=50%. Invest in early prospecting to identify the economic buyer and primary champion before signalling "ready for sales."

### Trap 2: Attribution Collapse and Measurement Theatre

**The pattern:** Marketing reports "we generated 50 engaged accounts this quarter." Sales reports "we closed 5 deals, most of which we sourced ourselves through outbound cold calls." Leadership sees the gap and cuts ABM budget.

**Root cause:** No unified account journey view. Marketing measures engagement; sales measures pipeline/revenue. No connection between the two.

**Fix:** Implement account-level attribution. When sales creates an opportunity, tag it with the source account. Close the feedback loop: track which engaged accounts became pipeline, which became closed-won, and calculate ABM influence on those deals. Report back to marketing: "Of 50 engaged accounts, 12 created opportunities, 3 closed. ABM sourced €2.1M this quarter."

### Trap 3: Coverage Spread Without Depth

**The pattern:** Marketing reaches 200 target accounts with high-volume ad impressions and email sends. Engagement is low because the messaging is generic. Coverage is shallow (single person per account). Marketing claims success: "We touched 200 accounts!" Sales says: "We saw no qualified pipeline from those accounts."

**Root cause:** Breadth over depth. Volume KPIs misaligned with account-based outcomes.

**Fix:** Measure depth first: how many accounts have 2+ identified roles? How many have a champion? These are preconditions to engagement. Concentrate resources on accounts where you can achieve buying group visibility. Fewer accounts, deeper engagement, higher conversion.

### Trap 4: Handover Without Discipline

**The pattern:** Marketing hands 80 accounts to sales this month with engagement scores ranging from 75 to 150. Sales accepts 30, rejects 50 with "not ready" or "bad fit." Marketing feels rejected; sales feels flooded with garbage.

**Root cause:** No clear handover criteria. Both teams operating on different definitions of "ready."

**Fix:** Co-define and codify the handover gate. Publish it. Live by it. Sales must document rejection reasons. Marketing must act on feedback. If 60%+ are rejected, the threshold is too loose; tighten it. If <40% are rejected, the threshold is too tight; loosen it. Healthy range: 40-60% rejection rate.

## Worked Example: 200-Account Enterprise ABM Programme (No New Accounts)

**Scenario:** A €15M ARR infrastructure software company targets 200 named enterprise accounts globally. No new accounts ever appear (TAM is fixed and mature). The challenge: how to measure ABM engagement and prove that Marketing's work is driving sales outcomes in a TAM where everything is account-based.

### Setup

**Target List:**
- 200 global enterprise infrastructure companies
- 15+ employees each, €100M+ revenue
- Identified: CFO, CIO, VP Operations, VP Security, Procurement Lead

**Engagement Score Thresholds (calibrated for this TAM):**
- 0-30: Watchlist (researching category, passive engagement)
- 31-80: Warm (active engagement, incomplete buying group)
- 81-140: Hot (multiple signals or critical event, buying group visible)
- 140+: In-Market (proposal, demo, RFP, or economic buyer engaged)

**Handover Criteria (explicit):**
- Engagement score >=81 AND
- Economic Buyer identified (confirmed via email or meeting) AND
- 1+ additional role engaged (CIO, VP Operations, Security) AND
- Critical event triggered (demo, meeting, proposal request) OR score >=140

### Measurement Workflow (Monthly)

**Week 1: Engagement Snapshot**
- Pull engagement scores for all 200 accounts
- Distribution: 45 watchlist, 90 warm, 50 hot, 15 in-market
- Identify accounts with rising scores (trending up) vs. flat/declining

**Week 2: Buying Group Deep-Dive**
- For 50 "hot" and 15 "in-market" accounts, validate buying group map
- Action: If Economic Buyer is missing, assign Marketing task to prospect for contact (LinkedIn, call note follow-up, partner reference)
- If coverage <50%, document gap and assign follow-up

**Week 3: Handover Execution**
- Accounts meeting handover criteria are formally passed to Sales
- CRM opportunity created, AE assigned
- Handover packet prepared (summary, engagement context, buying group, next step)
- Sales accepts or rejects within 48 hours with reason code

**Week 4: Pipeline and Closed-Won Attribution**
- Track which accounts created pipeline (SQL created)
- Measure conversion: Engaged Account -> SQL -> Opportunity -> Closed-Won
- Calculate ABM revenue: sum of closed-won revenue from accounts sourced via ABM
- Track time-to-close: average days from handover to opportunity creation, opportunity to close

### Example Monthly Report

```
METRIC                              VALUE          MOM TREND
────────────────────────────────────────────────────────────────
Total Target Accounts               200            Stable
Accounts by Stage
  - Unaware (0 signals)             60             ↓ 10
  - Aware (passive)                 75             ↑ 5
  - Engaged (active, incomplete)    40             ↓ 5
  - In-Market (ready)               20             ↑ 15
  - Handed-to-Sales                 5              ↑ 2

Buying Group Coverage
  - Accounts with >=50% role ID     45 / 200       ↑ 8
  - Economic Buyer identified       52 / 200       ↑ 12
  - 2+ stakeholders engaged         38 / 200       ↑ 6

Handover Activity
  - Accounts meeting criteria       18             ↑ 5
  - Accounts handed to sales        16             ↑ 3
  - Sales acceptance rate           14/16 = 87.5%  (healthy)
  - Days in stage (median)          34 days        ↓ 2

Pipeline & Revenue Attribution
  - Accounts creating SQLs          12 / 100 = 12% (YTD)
  - Accounts creating Opps          8 / 100 = 8%
  - Accounts closing won            2 / 100 = 2%
  - ABM-sourced revenue (MTD)       €340K          ↑ €95K

Engagement Velocity
  - Accounts with rising scores     22 / 200 = 11%
  - Accounts with declining scores  15 / 200 = 7.5%
  - Critical events triggered       8 (demo reqs,  ↑ 2
                                       meetings)
```

**Narrative for executive review:**
"We have mapped 45 accounts into active buying groups. Of these, 18 are now meeting our handover criteria (engaged + buying group visible + critical event). Sales has accepted 14 of the 16 handed this month, indicating strong alignment. YTD, accounts we classified as 'in-market' via engagement scoring have generated 8 opportunities (8% conversion) and closed €340K this month. The programme is proving ROI."

## How to Use This Skill

**"We run ABM but can't measure success."** Start with the Buying Group Tracker template. Map 10-20 accounts manually (identify economic buyer, technical buyer, end-user champion, security). Gather their engagement signals from CRM, web tracking, email platform, ad platform. Build a simple engagement score using the baseline weights. Rank accounts by score and buying group coverage. Hand top accounts to sales with the handover packet. Measure conversion: how many became pipeline? How much revenue? Start there.

**"Our engagement score is 50-80 points. Should we hand to sales?"** No. Handover requires score >=100 AND buying group coverage >=50%. Your account is in the "Warm" stage. Continue nurture. Assign a task to identify the Economic Buyer. Once that contact is on file, score the account again. If score is still 50-80 but you now have Economic Buyer + 1 other role, you are at 2/5 coverage = 40%, still shy of the threshold. Assignment: get one more role engaged (email the technical buyer introduction, set meeting with VP Operations). Recheck in 3 weeks.

**"We just got a demo request. Should we hand to sales immediately?"** Demo request from a qualified contact (not procurement clerk) is a critical event. Yes, escalate to sales within 24 hours BUT only if you have identified the Economic Buyer. If the demo requester is the technical buyer but the economic buyer is unknown, sales should map the buying group before investing. Handover packet: "Demo scheduled, but Economic Buyer not yet identified. Recommend AE loop in technical buyer during discovery to identify budget holder."

**"Our handover rate is 15% :  most accounts we try to hand, sales rejects."** Your criteria are too loose. Likely: engagement score threshold is too low (you are handing Warm accounts, not Hot accounts), or buying group coverage gate is missing. Tighten the rule: require score >=120 AND Economic Buyer + 2 other roles. Accept fewer handovers, but ensure acceptance rate rises to 60-75%.

**"Sales says our 'engaged' accounts are not converting to pipeline."** Measure the gap: of 50 accounts handed to sales, how many created an opportunity? If <10%, there is a disconnect. Possible root causes: (1) your engagement signals correlate with research activity, not buying intent (e.g. high content downloads but no economic buyer contact), (2) sales is not following up (check AE activity logs), or (3) your TAM is wrong (they are in-market for a competitor's solution). Investigate by reviewing 5-10 accounts that did not convert. Did they have the Economic Buyer? Did they reply to sales outreach? Did they have a champion? Pattern analysis will expose the gap.

---

## Signal -> Trigger -> Action: ABM Engagement Breach Rules

These rules connect engagement scoring to the sales operating cadence. When an ABM signal fires, the cadence ensures someone acts.

| Signal | Threshold | Trigger | Action | Owner |
|--------|-----------|---------|--------|-------|
| Account reaches Hot (score 100+) | First occurrence | Account hot alert | Review buying group coverage; if >=50%, prepare handover packet. If <50%, assign buying group mapping. | Marketing Leader |
| Critical event (demo request from qualified contact) | Any | Immediate escalation | Email sales within 24h with handover packet. Create CRM task for AE to reach out. | Marketing Ops |
| Account score declining >50% in 2 weeks | Trending down | At-risk alert | Review: has signal decay expired? Has engagement stopped? Assign re-engagement campaign or remove from active nurture. | Marketing |
| Buying group coverage >=50% | First achievement | Coverage gate passed | Account eligible for handover if score >=100. Flag for next handover batch. | Marketing Ops |
| Sales rejects handover >3 consecutive times | Repeated rejection | Persistent rejection | Schedule joint review (marketing + sales) to diagnose root cause. Revise criteria or account fit assessment. | Sales Leader + Marketing Leader |
| Handed account creates opportunity | Outcome | Attribution event | Tag opportunity with ABM source. Measure AE activity time from handover to opportunity creation. | Sales + RevOps |
| Closed-won deal from ABM account | Outcome | Revenue attribution | Report to executive: "€XXK revenue from ABM programme this quarter." Link to account and engagement history. | RevOps + Marketing |

---

## Reference Files

| File | When to read | What's inside |
|------|-------------|---------------|
| `references/engagement-scoring-model.md` | Building an account engagement score | Signal types, weights, decay formulas, score-to-threshold mapping, configuration worksheet |
| `references/buying-group-tracker.md` | Mapping and tracking the buying group | Role definitions, coverage calculation, champion validation, tracking table template |
| `references/handover-trigger-doctrine.md` | Defining and executing account handoff to sales | Handover criteria, critical events, handover packet specification, rejection reason codes |
| `references/measurement-dashboard-spec.md` | Building the ABM measurement dashboard | Leading/lagging metrics, what NOT to report, per-audience dashboard specs, alert thresholds |
| `references/abm-benchmarks.md` | Validating your programme against industry data | Buying group size, engagement benchmarks, handover conversion rates, ROI data (all sourced) |
| `references/abm-diagnostics.md` | Detecting measurement theatre and false positives | 10-question ABM diagnostic, pattern-based diagnosis, gap analysis framework |

---

## Canon References

Cross-references: marketing-operations (lead scoring dual-axis), icp-builder (account selection methodology), lead-routing (sales speed-to-lead), revops-metrics (KPI benchmarks), signal-trigger-action framework, and sales operating cadence.

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates :  ABM Measurement Worksheet

For ABM measurement buildout in client engagements:
`Frameworks/Templates/abm-measurement-worksheet.xlsx`

3 sheets: Engagement Scoring Setup, Buying Group Tracker, Monthly Snapshot Dashboard.
Use in: ABM programme inception, measurement system buildout, monthly cadence reporting.

Original source: Practitioner scenario documented for 200-account enterprise ABM TAM (2026).
