---
name: "revops-handoffs"
title: Revenue handoff operations
description: "Revenue handoff design across the full bow-tie model; Marketing → Sales → Partner/Implementation → CS → Sales (expansion), plus lifecycle marketing and ABM loops. Use when the user mentions handoff, lead routing, speed-to-lead, MQL routing, closed-won handoff, partner handoff, CS-to-sales handback, expansion pipeline, cross-sell pipeline, upsell pipeline, renewal pipeline, territory routing, SLA between teams, transfer document, or AI handoff docs. Also trigger on \"leads fall through the cracks,\" \"CS never knows what sales promised,\" \"we lose momentum after signature,\" \"nobody owns expansion,\" or \"cross-sell has a different buying group.\" BOUNDARY: covers handoff design and SLAs between bow-tie stages. For HubSpot implementation, also consult revops-hubspot. For CS operations, see cs-operations. For SPICED, see sales-methodology."
category: RevOps
---

# Revenue Handoff Operations: Full Bow-Tie Model

You are a revenue handoff architect. Handoffs are where revenue leaks. Standardised handoff protocols improve implementation success by ~45% and cut first-year churn by 35-40%. Your job: design the SLAs, context packets, routing rules, ownership models, and automation for every transition in the bow tie.

**Reference files** (read before giving detailed implementation advice):
- `references/handoff-slas-and-benchmarks.md`: SLA targets, speed-to-lead data, metrics per handoff, leading indicators of failure, measurement dashboards
- `references/expansion-pipeline-architecture.md`: three-type expansion model, new-DMU cross-sell handling, ownership thresholds, association model, SPICED requirements
- `references/hubspot-workflows.md`: pipeline configurations, workflow specs, property catalog, Breeze AI patterns, tier requirements
- `references/ai-tooling.md`: AI handoff document generation, enrichment/scoring tools, predictive models, LLM middleware patterns, GDPR considerations

## The Five-Node Bow Tie

Most B2B SaaS orgs have four handoff points. Companies with implementation partners have five:

```
Marketing → Sales → Partner/Impl → CS → Sales (expansion)
                                         ↑
              Lifecycle marketing & ABM loops back ←──┘
```

Each node has: an **owner**, a **context packet** (what must transfer), an **SLA** (time + quality), a **trigger** (what fires the handoff), and **measurement** (how you know it's working or failing).

## 1. Marketing to Sales

The most studied, most frequently broken transition. Speed kills competitors; delay kills deals.

### Speed-to-Lead (the non-negotiables)

| Lead Type | Response SLA | Evidence |
|---|---|---|
| Hand-raisers (demo, pricing) | < 5 minutes | 21× more likely to qualify vs 30 min (Dr. James Oldroyd, MIT Sloan, 2007; foundational research, predates AI automation and channel saturation; 15,000+ leads across 6 companies) |
| Paid ads | < 3 minutes | Highest cost-per-lead, hottest intent |
| Partner referral | < 30 minutes | Warm but relationship-dependent |
| Organic inbound | < 10 minutes | Moderate intent |
| Content / webinar | 3-4 days (nurture first) | Premature outreach damages trust |

Reality check (historical baseline, 2011): average B2B response is 42 hours, 23% never get a reply. Modern context (2025): instant booking converts 66.7% of qualified submissions vs ~30% industry average (Chili Piper, 4M submissions); <5-minute response closes at 32% rate (Optifai Pipeline Study, 939 companies).

### Lead Tiers

**Hand-raisers**: bypass scoring, route directly to sales. 5-minute SLA.
**MQLs**: firmographic fit + behavioural intent + third-party intent. Common starting split: 40/40/20 (operational template; optimise through conversion analysis against your closed-won data). Route to SDR/AE by territory. Scoring drives 39-40% MQL-to-SQL vs 15-21% without (Forrester/SiriusDecisions Demand Waterfall).
**PQLs** (hybrid PLG): usage-based triggers. Convert at 15-30%.

### Context Packet

Firmographic context, full engagement history, lead score breakdown (fit vs intent), buying group context (other contacts from same account), qualification data (SPICED/BANT if SDR-qualified). Auto-enrich before routing to eliminate research delay.

### Marketing-Sales SLA

Marketing: X qualified MQLs, pipeline contribution at 4x coverage. Sales: respond within SLA, 5-10 follow-up attempts, CRM disposition within deadline. Enforce: auto-escalation, auto-reassignment at 24h, weekly compliance reporting.

### Routing Models

Round-robin (early stage), territory-based (scale), capacity-based (mature). **Account-based override is non-negotiable**: leads from known accounts route to account owner, never rotation. For EU: route by language of form submission as first-pass filter: DACH, Nordics, UK/IE, Western Europe, Southern Europe, CEE.

→ For detailed benchmarks and metrics: read `references/handoff-slas-and-benchmarks.md`

## 2. Sales to Partner/Implementation

Customer excitement peaks at signature then collapses if nothing happens ("Trough of Disillusionment").

### Context Packet (7 elements)

1. Deal history and origin
2. Customer goals with **measurable** success criteria (specific, not assumed)
3. Full stakeholder map (champion, economic buyer, end users, detractors)
4. Every commitment the AE made (explicit and implicit)
5. Known risks and internal politics
6. Technical requirements (integrations, migration, compliance)
7. Customer timeline including critical events from SPICED

### SLAs

| Milestone | Target |
|---|---|
| Internal AE to Impl briefing | 24-48 hours post-signature |
| Customer introduction email | Within first week |
| Kickoff scheduled | 48-72 hours post-signing |
| First implementation meeting | 2-7 days (2 best, 7 standard) |

### Partner-Specific

Partner receives: full SPICED brief + technical requirements + stakeholder map + timeline + promises log. AE attends partner kickoff. Partner reports milestones to vendor CRM. Hypercare (2-4 weeks post go-live) bridges to CS.

### Sales Involvement Model

**Warm overlay** (default): AE at kickoff, introductions, steps back, CC'd 2 weeks.
**Pre-sale CS** (enterprise >€50K ACV): CSM in late-stage calls.
**Clean break** (SMB <€10K): automated handoff.

## 3. Implementation to CS

Least standardised, most consequential. Early value realisation (within first 30 days) correlates with higher CLV.

### Context Packet

Scope/configuration details, training completion status and gaps, outstanding issues with workarounds, customer sentiment during implementation, updated stakeholder map, initial adoption metrics, lessons learned.

### Go-Live Readiness (5 conditions, all true)

Tasks work end-to-end. People trained. Data migrated. Support plan in place. Rollback plan exists.

### Health Scoring Starts Here

Don't wait for steady-state. Track: milestone completion rate, stakeholder engagement, customer responsiveness, admin login frequency, training attendance.

## 4. CS to Sales (Expansion)

Expansion costs $0.27/$1 ACV vs $1.16 new (Pacific Crest, 2016, historical baseline); modern data shows 50-60% of new ARR from expansion sourced from existing customers (OpenView 2023, KeyBanc 2024), up from historical 35-40%.

### Three Expansion Types: Critical

| Type | DMU | Pipeline | Discovery |
|---|---|---|---|
| **Upsell** | Same champion, same budget | Short: Identified → Proposal → Won | SPICED refresh |
| **Cross-sell (warm)** | Partial overlap, champion introduces | Standard: Identified → Needs Assessment → Proposal → Negotiation → Won | Partial new SPICED |
| **Cross-sell (new DMU)** | Completely new buying group | Full discovery stages added | Full new SPICED mandatory |

A cross-sell with a completely new DMU is a **new-logo sale inside a known company**. Trust is with the account, not the buying group. Forcing it into the short pipeline poisons win rate and velocity data.

**Litmus test**: "Would losing the contract in BU-A affect closing in BU-B?" If no → new logo with customer referral source.

### Ownership

| ACV | Owner | CS role |
|---|---|---|
| <€10K | CSM closes | End-to-end |
| €10K-50K | AM/AE + CSM | Context, stays in meetings |
| >€50K | AE full cycle | Introduces, advisory |

Define thresholds in governance. Ambiguity = nobody closes.

### Expansion Signals

Usage: 80%+ seat limits, new feature adoption, DAU increasing.
Relationship: champion promoted, new stakeholder, positive NPS.
Commercial: org headcount growth, new budget cycle, cross-functional interest.
Outcomes: value ahead of schedule, ROI exceeded, new use cases.

### CS to Sales Handback Process

CSM flags signal → workflow creates deal → assigns to AE → CSM prepares brief (health, usage, stakeholders, whitespace) → joint meeting → clear rules of engagement from there.

→ For new-DMU detail, association model, and reporting payoff: read `references/expansion-pipeline-architecture.md`

## 5. Lifecycle Marketing and ABM Loops

### Five-Stage Post-Sale Marketing

1. **Onboarding**: role-based education, setup guides, in-app messaging
2. **Adoption**: feature spotlights, best practices, certifications
3. **Retention**: ROI reports, QBR materials, NPS surveys
4. **Expansion**: usage-based trigger emails, cross-sell content, feature nudges
5. **Advocacy**: case studies, review campaigns (G2, Capterra), advisory boards

### ABM for Existing Customers

Churn prevention ABM (competitor intent signals to executive engagement), cross-sell ABM (content clustering to product nurture), multi-threading ABM (new departments via LinkedIn + role-specific content), renewal ABM (customer-specific ROI reports 90-120 days pre-renewal), usage-based expansion ABM (in-app + email on product signals).

## 6. AI-Enabled Handoffs

Read `references/ai-tooling.md` for the full stack. Summary:

**Production-ready now**: AskElephant ($99/mo) for auto-generated SPICED handoff docs. Clay ($149-800/mo) for enrichment + scoring. HubSpot Breeze for native intent scoring. Gong/Avoma for conversation intelligence.

**LLM middleware pattern**: deal stage change → pull CRM data + transcripts → structured prompt → output to CRM/workspace. Works with GPT-4 or Claude via Zapier/Make/n8n.

**Predictive**: Pendo Predict, ChurnZero for churn/expansion. Best models hit 85-92% accuracy 60-90 days pre-churn.

**GDPR non-negotiables**: data residency, model training opt-out, consent management, EU Data Act switching requirements.

## 7. HubSpot Implementation

Read `references/hubspot-workflows.md` for detailed specs. Architecture summary:

**Three pipelines**: New Business, Expansion (with `expansion_type` driving conditional stages), Renewals (auto-created on Closed Won).

**Deal-to-deal associations** (Professional+) link expansion → original deal for lineage and Δt7 measurement.

**Key workflows**: MQL routing (5-min SLA, Breeze AI summary, Slack notify, 24h escalation), Closed-Won handoff (validate completeness → create onboarding ticket + renewal deal), expansion signal (company property → auto-create deal → assign + notify), renewal automation (date-triggered at T-90).

**Speed-to-lead tracking**: custom `first_connection_date` property + calculated `speed_to_lead_hours`. HubSpot lacks this natively.

## Measurement Framework

### Metrics by Handoff

| Handoff | Key Metrics | Targets |
|---|---|---|
| Mktg to Sales | Speed-to-lead, MQL-to-SQL conversion, unworked rate | <5 min (hand-raisers), 25-35% conversion, <5% unworked |
| Sales to Impl | Time-to-kickoff, info completeness, quality score | <7 days, >90%, ≥4.0/5 |
| Impl to CS | TTFV, go-live rate, onboarding churn | Segment-dependent, >85%, <3% |
| CS to Sales | Expansion pipeline from CS, handoff time, expansion win rate, NRR | Growing QoQ, <48h, >40% upsell / >20% new-DMU, 110-130%+ |

### Leading Indicators of Failure

Rising unworked leads (>10%) signals SDR overload/routing failure. MQL rejection rising signals ICP misalignment. Time-to-kickoff >14d signals sales-CS bottleneck. Declining onboarding completion signals capacity/complexity issue. Shrinking expansion pipeline signals CS not surfacing signals.

### Quality Scorecard

Receiving team rates each handoff 1-5 across: information completeness, promise alignment, customer sentiment continuity, context transfer quality, stakeholder mapping. Review weekly in operating cadence.

## How to Use This Skill

**"Leads fall through the cracks"**: Speed-to-lead + routing rules. Read benchmarks reference.
**"CS never knows what sales promised"**: SPICED-to-handoff pipeline. Gate Closed Won on completeness. Read AI tooling reference.
**"We lose momentum after signature"**: Sales to Impl SLA. Auto-trigger on Closed Won. Read workflows reference.
**"Nobody owns expansion"**: Ownership model + expansion pipeline. Read expansion architecture reference.
**"Cross-sell has a different buying group"**: Three-type model. Read expansion architecture reference.
**"How do we involve the partner?"**: Partner context packet + AE-at-kickoff + hypercare bridge.
**"Design handoffs from scratch"**: Audit each point against SLA framework. Instrument leading indicators. Start with biggest revenue leak.

---

## References

- Dr. James Oldroyd, MIT Sloan (2007). Lead Response Management study. 15,000+ leads across 6 companies. Published via InsideSales.com.
- Velocify (circa 2012). Responding within 1 minute increases conversion by 391%.
- HBR (2011). "The Short Life of Online Sales Leads." 2,241 companies tested. Average B2B response: 42 hours. 23% never responded.
- Workato (2024). Speed-to-lead study: 114 B2B companies. Only 1 sent personalised email within 5 min. Average personalised response: 11h 54m.
- Chili Piper (2025). 2025 Benchmark Report: ~4M form submissions. Instant booking converts 66.7% vs ~30% industry average.
- Justin Norris, RevOps FM (2025). "A Complete Guide to Speed-to-Lead." 10-min hand-raiser SLA to 40% conversion lift.
- Optifai Pipeline Study (Q2 2025-Q1 2026, 939 companies). <5 min response = 32% close rate, 2.6x higher than 24+ hours.
- Pacific Crest / David Skok & Matrix Partners (2016). SaaS Survey: expansion costs $0.27 per $1 ACV vs $1.16 new logos.
- OpenView Partners (2023). SaaS Benchmarks (700+ companies): 50-60% of new ARR from expansion (best-in-class).
- KeyBanc (2024). Expansion = 52% of new ARR.
- Rework (2025). "Deal Handoff Protocol: Standardizing Post-Close Transitions." 45% implementation improvement, 35-40% churn reduction.
- Forrester/SiriusDecisions. Demand Waterfall: MQL→SQL 39-40% with scoring vs 15-21% without.

> Built by [Neon Triforce](https://neontriforce.com)
