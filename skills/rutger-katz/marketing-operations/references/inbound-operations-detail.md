# End-to-End Inbound Process: Operational Detail

On-demand reference for the marketing-operations skill.

**Source:** Adapted from Union Square Consulting's Inbound Pyramid. This skill applies it as the process layer beneath the scoring mechanics. The lead scoring and attribution sections of the skill cover the mechanics; this is the operational process: the step-by-step flow from first touch to qualified pipeline. The customer journey map and inbound conversion metrics by stage live in the skill body; the routing process, follow-up cadences, speed-to-lead SLAs, and ABM reporting depth live here.

## Speed-to-Lead SLA

Research consistently shows that response time is the single biggest lever in inbound conversion. After 5 minutes, contact rates drop by 10x (practice-based; Blazeo formal 15-minute SLAs hit target 54.9% vs 29.5% without, 2026). Response speed is the single highest-leverage lever for inbound conversion.

```
TIER     RESPONSE SLA     ESCALATION
────     ────────────     ──────────
T1 MQL   < 5 minutes      If no response in 5 min → escalate to sales manager
                           If no response in 15 min → re-route to backup rep
T2 MQL   < 30 minutes     If no response in 30 min → escalate
                           If no response in 2 hours → re-route
T3 MQL   < 4 hours        If no response in 4 hours → auto-nurture sequence

MEASUREMENT:
  - Track: time from MQL creation to first rep outreach (call/email)
  - Target: median < 10 minutes for T1
  - Report: weekly, by rep and by lead source
  - Enforce: include in rep performance metrics
```

Alternative SLA framing by fit × intent (report weekly; if T1 SLA miss rate >10%, escalate immediately. This is a revenue leak, not a process problem):

```
LEAD TYPE                     TARGET RESPONSE SLA     CHANNEL
──────────                    ───────────────────     ───────
T1 (High Fit + High Intent)   < 5 minutes             Phone + email
T2 (High Fit + Medium Intent) < 1 hour                Email sequence + phone attempt
T3 (Medium Fit)               < 4 hours               Email sequence
Nurture (Low Fit or Intent)   < 24 hours              Automated nurture sequence only
```

## Lead Routing Rules

Routing rules determine which leads go where. Without defined rules, leads route by accident (whoever picks up first, whoever is online, whoever is the default owner).

```
RULE TYPE         LOGIC                                   IMPLEMENTATION
─────────         ─────                                   ──────────────
Geographic        Route by country/region/timezone         MAP workflow → CRM owner
Named Account     If account in named list → assigned rep  MAP lookup → CRM account owner
Round Robin       Equal distribution within territory      MAP rotation + weighted by capacity
Segment-Based     Route by ICP tier (T1 → senior rep)     MAP scoring → routing workflow
Product-Based     Route by product interest signal         MAP form field / page visit → workflow

CONFLICT RESOLUTION:
  Named Account always wins over Round Robin.
  If account has existing open opportunity → route to opp owner.
  If account has existing CSM → notify CSM + route to sales.
  If no match → round robin within territory.
```

**Routing logic hierarchy:**
1. **Geography/territory**: route by region or country first
2. **Account ownership**: if the lead's company has an existing CRM owner, route to that owner
3. **Segment/tier**: route T1 leads to senior reps; T3 leads to SDRs or nurture
4. **Round-robin**: within a qualified pool, distribute evenly to prevent cherry-picking
5. **Capacity cap**: prevent routing to reps above their daily/weekly lead cap

Document routing rules in CRM as explicit automation, not as "the team knows." For operational depth on routing design, see lead-routing.

## Lead Follow-Up Sequence

Inbound leads are not self-converting. Even high-intent demo requests require structured follow-up.

```
DAY 0 (within SLA):  Phone call attempt + personalized email
                     Reference: specific content consumed, company context
DAY 1:               Second phone attempt (different time of day)
DAY 2:               Email with relevant case study or resource
DAY 3:               Phone attempt #3 + LinkedIn connection request
DAY 5:               Email with value-add (not "just checking in")
DAY 7:               Final attempt email: "Should I close this out?"
DAY 10:              If no response → recycle to nurture. Set re-engagement trigger.

RULES:
  - Never send "just following up" emails. Every touch adds value.
  - Personalize first email based on lead source + content consumed.
  - Log all attempts in CRM. No dark pipeline.
  - If lead responds but isn't ready → set task for 30/60/90 day follow-up.
```

Tier-specific inbound cadence variant (calibrate cadence length and steps against your industry and ACV. High-ACV B2B sales with longer cycles tolerate longer cadences):

```
T1 LEAD FOLLOW-UP (High Fit + High Intent)
Day 0:   Phone call (within 5 min) + confirmation email
Day 1:   Follow-up email with case study or relevant social proof
Day 3:   Phone attempt + personalized value email (reference their use case)
Day 5:   "Break-up" email: sets expectation this is final attempt
Day 7:   Move to nurture if no response

T2 LEAD FOLLOW-UP
Day 0:   Confirmation email + 4-hour phone attempt
Day 2:   Follow-up email
Day 5:   Final follow-up
Day 7:   Move to nurture
```

## ABM Reporting (When Running Allbound/ABM Motion)

```
ACCOUNT COVERAGE REPORTING:
  - % of target accounts with active engagement (content, ads, outreach)
  - Average touches per account per month (by channel)
  - Account penetration depth (contacts engaged per account)

ACCOUNT GENERATION REPORTING:
  - New accounts entering pipeline from ABM programs
  - ABM-sourced vs ABM-influenced pipeline split
  - Time from ABM activation to first meeting (by tier)

PIPELINE GENERATION REPORTING:
  - ABM pipeline value vs direct inbound pipeline value
  - Conversion rates by ABM tier (T1 named vs T2 programmatic)
  - ABM deal velocity vs non-ABM deal velocity

ABM/INBOUND REVENUE REPORTING:
  - Closed revenue by motion (ABM, inbound, outbound, partner)
  - Blended CAC by motion
  - LTV by acquisition motion (do ABM customers retain better?)
```

**Account-level inbound reporting:** For accounts in your ABM program, supplement lead-level reporting with account-level coverage and pipeline metrics. Key ABM inbound metrics:
- **Coverage:** % of target accounts with at least one identified contact (by tier)
- **Engagement:** % of target accounts with activity in last 30/60/90 days
- **Account-level MQL:** at least one T1/T2 lead from a target account in active research
- **Pipeline by ABM tier:** Tier 1 accounts should generate disproportionate pipeline relative to their count

Report ABM inbound at the account level in the monthly Marketing review. Individual lead metrics miss the signal when multiple contacts from one account engage across different channels. For full pipeline reporting architecture, see pipeline-visibility.
