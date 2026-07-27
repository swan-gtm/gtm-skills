---
name: "partner-channel-operations"
title: Partner channel operations
description: "Partner and channel operations for B2B SaaS: programme design, partner enablement, co-selling, deal registration, and ecosystem-led growth. Use when the user mentions partner programme, channel strategy, partner enablement, co-sell, deal registration, partner onboarding, partner tiers, ecosystem-led growth, partner-sourced pipeline, partner health scoring, partner QBR, ideal partner profile, IPP, referral partners, resellers, VARs, implementation partners, GSIs, MSPs, partner portal, MDF, partner attribution, partner revenue, or partner operations. Also trigger when someone says 'we need partners to scale,' 'our partner programme isn't producing,' 'how do we structure partner tiers,' 'partners aren't bringing deals,' or 'we want to build an ecosystem.' BOUNDARY: covers partner OPERATIONS (programme design, enablement, pipeline, reporting). For GTM org design and capacity, see gtm-planning. For handoff design between partner and direct, see revops-handoffs. For HubSpot implementation, see revops-hubspot."
category: RevOps
---

# Partner & Channel Operations

## The Partner Operating Model

Partner-driven revenue is becoming table stakes in B2B SaaS. The data is clear: partner-involved deals close 46% faster and are 53% more likely to close (Crossbeam State of Partner Ecosystem, 2023; 500+ GTM leaders), producing 32-60% larger deal sizes (Introw, 2024; Crossbeam case studies). Mature programmes source 25-40%+ of total revenue, and partner-involved accounts are 58% less likely to churn (Crossbeam, 2023). But most partner programmes fail. Not because of bad partners, but because of bad operations.

The operating model has five components:

```
1. PROGRAMME DESIGN: Who do we partner with? What's the structure?
2. PARTNER ENABLEMENT: How do we make partners successful?
3. CO-SELLING OPERATIONS: How do we work deals together?
4. PARTNER PIPELINE OPS: How do we track and manage partner pipeline?
5. PARTNER PERFORMANCE: How do we measure, review, and optimise?
```

---

## Partner Types & Selection

### Partner Type Decision Matrix

```
TYPE                 WHEN TO USE                                    REVENUE MODEL
-----------          -----------                                    ----------------
Referral Partner     Early-stage ecosystem. Low complexity.         10-25% of Y1 ARR
                     Partners have relationships but no sales       commission
                     resources. Quick wins.

Technology Partner   Shared ICP. Integration creates combined       Commission on co-sold
                     value. Complementary, not competitive.         deals. Revenue share.

Reseller             High-volume market. Need geographic or         30-50% margin on
                     vertical distribution fast. Partner owns       resold product
                     customer relationship.

Implementation       Solution requires setup, configuration,       Project fees to partner.
Partner              or customisation. Barrier to self-serve.       Indirect ARR uplift.

Co-Sell Partner      Two-way deal pipeline. Both orgs selling       Reciprocal referral
                     together. High alignment required.             fees or revenue share.

VAR                  Bundled solution (hw + sw + services).         35-50% discount off
                     Project-based delivery. Turnkey for customer.  list + project margin.

MSP                  Ongoing managed services. Customer prefers     40-50% wholesale +
                     outsourced operations. Recurring revenue.      managed services margin.

SI / GSI             Enterprise customers. Custom requirements.     30-40% discount +
                     Long sales cycles. Large deal sizes.           project margin.
                     GSIs: Deloitte, Accenture, IBM-class.         Requires co-investment.

Embedded/Integration Native integration partnership. Product-to-product  Revenue share
Partner              connectors, Slack/Figma/Shopify-style app      (typically 5-15%),
                     ecosystems. Partner tools are extension       referral fees on
                     of your product, not standalone solution.     co-sold deals.
                     Low friction for end-user adoption.
```

### Ideal Partner Profile (IPP)

Like ICP for customers, define your Ideal Partner Profile before recruiting.

```
IPP CRITERIA:                              SCORING (1-5)

STRATEGIC FIT
  Shared ICP overlap                       ___
  Complementary (not competitive) offering ___
  Aligned go-to-market motion              ___
  Geographic/vertical alignment            ___

OPERATIONAL READINESS
  Dedicated partner/sales team             ___
  CRM and deal tracking in place           ___
  Existing customer base to cross-sell     ___
  Marketing capability (content, events)   ___

COMMITMENT SIGNALS
  Executive sponsor identified             ___
  Willing to invest in enablement          ___
  Has referred deals before (informally)   ___
  Strategic motivation beyond commission   ___

SCORING: 36-60 = Tier 1 (strategic). 24-35 = Tier 2 (growth). 12-23 = Tier 3 (referral). <12 = not ready.
```

---

## Programme Design

### Tiering Structure

```
TIER 1: STRATEGIC PARTNERS (3-5 partners max)
  Requirements:
    - IPP score 36+
    - Dedicated partner manager assigned
    - Joint GTM plan signed
    - Minimum pipeline commitment (e.g., €500K/year)
    - Co-marketing investment
  Benefits:
    - Highest commission rates (20-25%)
    - Joint marketing funds (MDF)
    - Priority deal registration
    - Exec-to-exec alignment
    - Quarterly business reviews
    - Early access to product roadmap

TIER 2: GROWTH PARTNERS (10-20 partners)
  Requirements:
    - IPP score 24-35
    - Completed certification programme
    - Minimum 2 deals/quarter registered
    - Active in partner portal
  Benefits:
    - Standard commission rates (15-20%)
    - Access to co-marketing resources
    - Monthly partner check-ins
    - Lead sharing

TIER 3: REFERRAL PARTNERS (unlimited)
  Requirements:
    - IPP score 12-23
    - Signed partner agreement
    - Basic product training completed
  Benefits:
    - Referral commission (10-15%)
    - Access to partner portal and collateral
    - Quarterly webinars and updates
```

### Deal Registration

```
REGISTRATION PROCESS:
  1. Partner submits deal via portal/form (account name, contact, est. value, timeline)
  2. Auto-check: Is account already in pipeline? (CRM lookup)
     - If yes → conflict resolution (see below)
     - If no → register and assign
  3. Partner manager reviews within 24 hours
  4. Deal registered for [60/90/120] days (varies by deal size)
  5. If deal doesn't progress → registration expires, can be re-registered

CONFLICT RESOLUTION:
  - First to register wins (if within 7 days)
  - If account already has open opportunity → direct sales owns
    UNLESS partner can demonstrate prior relationship (evidence required)
  - If both partner and direct are engaged → co-sell (split commission)
  - Escalation: Partner manager + Sales manager resolve within 48 hours
  - Executive escalation if unresolved in 48 hours

CRM IMPLEMENTATION:
  Required properties on Deal/Opportunity:
    partner_sourced           (boolean)
    partner_influenced        (boolean)
    partner_name              (lookup to Partner record)
    partner_contact           (text: who at the partner is involved)
    deal_registration_id      (auto-generated)
    deal_registration_date    (date)
    deal_registration_expiry  (date: auto-calculated)
    partner_commission_%      (number: from tier)
    partner_commission_€      (formula: deal value × commission %)
    partner_tier              (dropdown: T1/T2/T3)
```

---

## Partner Enablement

### Onboarding Process (New Partner)

```
WEEK 1: WELCOME & ORIENTATION
  - Welcome call with partner manager
  - Partner agreement signed
  - Portal access granted
  - Product overview training (self-paced or live)

WEEK 2-3: PRODUCT CERTIFICATION
  - Technical product training
  - ICP and buyer persona training
  - Competitive positioning training
  - Certification exam (if applicable)

WEEK 4: GTM ALIGNMENT
  - Joint account mapping session (Crossbeam/Reveal or manual)
  - Identify first 5-10 target accounts
  - Define co-selling motion
  - Create 90-day partner plan

WEEK 5-6: FIRST DEAL ACTIVATION
  - Support partner on first deal registration
  - Joint call or co-sell support if needed
  - Weekly check-ins during ramp

RAMP METRICS:
  Time to first deal registration    Target: <60 days (Crossbeam composite; aligned with mature-stage benchmark)
  Time to first closed deal          Target: <120 days
  Certification completion rate      Target: >80% within 30 days
  Partner activation rate            Target: >60% active within 90 days (Crossbeam composite; growth-stage benchmark)
```

### Enablement Content Matrix

```
CONTENT TYPE              PURPOSE                          FORMAT
────────────              ───────                          ──────
Product one-pager         Quick reference for partner      PDF, portal
ICP & persona guide       Who to target                    PDF, training
Battlecard vs competitors How to position against others   PDF, portal
Demo environment          Partner can show product         Login credentials
Co-branded slide deck     For joint customer presentations PPTX template
Case studies              Proof points for partner         PDF, portal
ROI calculator            Quantify value for prospects     Excel/web tool
Partner playbook          How to sell, step-by-step        PDF/Notion doc
Objection handling guide  Common objections + responses    PDF, portal
Pricing guide             How to price/quote               PDF (restricted)
```

---

## Co-Selling Operations

### Co-Sell Motion Design

```
MOTION 1: PARTNER-SOURCED (partner finds the deal)
  Partner identifies opportunity → registers deal → introduces your team
  Your team runs discovery + solution → partner supports relationship
  Attribution: partner-sourced. Full commission.

MOTION 2: PARTNER-INFLUENCED (your team found the deal, partner helps close)
  Your team identifies opportunity → invites partner for expertise/credibility
  Partner joins calls, provides implementation perspective, builds trust
  Attribution: partner-influenced. Reduced commission (typically 50%).

MOTION 3: CO-SELL (both teams work deal together)
  Joint account mapping identifies shared target accounts
  Both teams coordinate outreach and selling
  Joint proposals and presentations
  Attribution: co-sell. Agreed revenue share.

RULES:
  - Every co-sell deal must have ONE designated "lead" (your team or partner)
  - Weekly sync between your AE and partner contact on active deals
  - Shared deal notes in CRM (both sides update)
  - Escalation path if deal stalls (partner manager + sales manager)
```

---

## Partner Pipeline & Reporting

### Partner Dashboards

**Executive Dashboard:**
```
  Partner-sourced pipeline (€ and % of total)
  Partner-influenced pipeline (€ and % of total)
  Partner-sourced revenue (€ and % of total, trailing 12 months)
  Active partners (% of total partners producing pipeline)
  Top 5 partners by pipeline contribution
  Deal registration volume and conversion rate
  Partner programme ROI (revenue ÷ programme cost)
```

**Operational Dashboard:**
```
  Deal registrations this month (by partner, by tier)
  Registration → Closed Won conversion rate
  Average deal size (partner vs direct)
  Average sales cycle (partner vs direct)
  Win rate (partner-sourced vs direct)
  Partner activity: portal logins, content downloads, certifications
  Partner pipeline by stage (funnel view)
```

**Partner-Facing Dashboard (in portal):**
```
  My registered deals and status
  My commission earned (paid and pending)
  My certification status
  My tier status and progress to next tier
  Shared account mapping results
  Upcoming partner events and training
```

### Attribution Model

```
PARTNER-SOURCED:    Partner registered the deal AND the first meeting was
                    originated by the partner. Full commission applies.

PARTNER-INFLUENCED: Direct team originated the deal, but partner was
                    actively involved in the sales process (joined calls,
                    provided references, supported evaluation).
                    Reduced commission applies.

MEASUREMENT:
  Track both sourced and influenced. Report separately.
  Total partner contribution = sourced + influenced.
  Influenced is harder to track; requires rep to tag deals.
  Enforce tagging in deal review cadence.
```

---

## Partner Health Scoring

```
DIMENSION                  WEIGHT    METRICS
-----------                ------    -------
Pipeline Activity (35%)    35%       Deal registrations/quarter
                                     Pipeline value created
                                     Deals progressing through stages

Revenue Production (25%)   25%       Closed-won revenue (trailing 12m)
                                     Win rate on registered deals
                                     Average deal size

Engagement (20%)           20%       Portal activity (logins, content)
                                     Training/certification completion
                                     Event attendance
                                     Responsiveness to comms

Relationship (15%)         15%       Exec sponsor engaged
                                     QBR attendance
                                     Joint planning completed
                                     Escalation frequency (lower = better)

Strategic Fit (5%)         5%        ICP overlap score
                                     Product roadmap alignment
                                     Market momentum

SCORING: 0-100.
  80+  = Healthy (green). Invest more.
  50-79 = Watch (yellow). Diagnose and coach.
  <50  = At risk (red). Intervention or exit.

REVIEW: Quarterly for T1, semi-annually for T2, annually for T3.
```

---

## Partner Review Cadence

```
WEEKLY:   Partner manager reviews deal registration pipeline (15 min)
          Sync with sales on active co-sell deals

MONTHLY:  Partner activity review (all tiers)
          Identify inactive partners → outreach or exit
          Review new partner onboarding pipeline

QUARTERLY (T1 Partners): Partner QBR
  Agenda:
    1. Revenue review: sourced + influenced, vs plan
    2. Pipeline review: active deals, stuck deals, new registrations
    3. Programme feedback: what's working, what's not
    4. Joint account mapping refresh
    5. Next quarter plan: target accounts, co-marketing, enablement needs
    6. Exec alignment: strategic direction, product roadmap

ANNUALLY: Programme review
  - Tier reassignment based on performance
  - Commission structure review
  - Programme ROI analysis
  - Strategic partner planning for next year
```

---

## Maturity Model: Partner Operations

```
LEVEL 1. FUNDAMENTALS (Month 0-6):
  Investment: Low (1 FTE + tools)
  Partners: 3-5 initial partners recruited
  Revenue: 0-5% partner-sourced
  What to build:
    [ ] Ideal Partner Profile defined
    [ ] Partner GTM process documented
    [ ] Deal registration process defined
    [ ] Basic partner agreement template
    [ ] Partner onboarding process created
    [ ] CRM partner tracking implemented
    [ ] First 3-5 partners recruited and enabled

LEVEL 2. ADOPTION (Month 6-18):
  Investment: Growing (1-2 FTEs + portal)
  Partners: 15-25 active partners
  Revenue: 10-20% partner-sourced
  What to build:
    [ ] Tiering structure implemented
    [ ] Partner portal launched
    [ ] Enablement content library complete
    [ ] Reporting and dashboards live
    [ ] Regular management review cadence
    [ ] Deal registration process running smoothly
    [ ] Partner health scoring implemented

LEVEL 3. OPTIMIZATION (Month 18-36):
  Investment: Dedicated team (3-5 FTEs)
  Partners: 30-50 active partners
  Revenue: 20-35% partner-sourced
  What to build:
    [ ] Partner insights driving programme decisions
    [ ] A/B testing partner messaging and enablement
    [ ] GTM Council reviewing partner performance
    [ ] Account mapping technology (Crossbeam/Reveal)
    [ ] Partner marketing programmes (MDF, co-marketing)
    [ ] Attribution model refined and trusted
    [ ] AI-driven partner health scoring (emerging: real-time pipeline analysis, deal sentiment, activity velocity)
    [ ] Automated deal registration categorisation and conflict flagging

LEVEL 4. ACCELERATION (Month 36+):
  Investment: Full partner org
  Partners: 50-100+ active partners
  Revenue: 35-60% partner-sourced
  What to build:
    [ ] LLM-powered partner agents (deal summarisation, auto-generated battlecards, qualification scoring)
    [ ] AI-driven account research for partner mapping (enterprise-scale waterfall enrichment)
    [ ] Predictive partner health scoring (ensemble ML plus NLP on unstructured signals)
    [ ] Automated trigger-based partner sequences with AI personalization
    [ ] Self-service partner onboarding at scale (multi-language, multi-product)
    [ ] Ecosystem-led growth motions (embedding partners in product, network effects)
```

---

## Common Pitfalls

```
PITFALL                              FIX
-------                              ---
"We recruited 50 partners but        Focus on activation, not recruitment.
 none are producing."                10 active partners > 50 dormant ones.
                                     Measure activation rate, not partner count.

"Sales and partners fight over       Clear deal registration rules. First to
 the same accounts."                 register wins. Conflict resolution process.
                                     Make commission worth it for both sides.

"Partners don't understand           Invest in enablement. Certification.
 our product well enough."           Demo environments. Regular training.
                                     Don't expect partners to self-serve.

"We can't track partner              Implement CRM properties. Enforce
 revenue accurately."                tagging in deal reviews. Track both
                                     sourced AND influenced.

"We invest equally in all            Tier your partners. Invest most in T1.
 partners and get uneven results."   Auto-serve T3. Kill non-producers after
                                     2 quarters of inactivity.

"Partners bring bad-fit leads."      Define qualification criteria for
                                     partner-registered deals. Reject deals
                                     that don't meet ICP threshold. Train
                                     partners on ICP.

"Our partner programme is            Partner ops is a long game. Expect
 not producing ROI yet."             6-12 months to first meaningful revenue.
                                     Track leading indicators (registrations,
                                     pipeline) before lagging (revenue).
```

---

## Benchmarks (Sourced)

### Partner Revenue by Programme Maturity

| Metric | Early (<18 months) | Growth (18-36 months) | Mature (36+ months) | Source |
|--------|--------------------|-----------------------|---------------------|--------|
| Partner-sourced revenue (% total) | 5-10% | 15-25% | 25-40%+ | Crossbeam composite, 2023 |
| Partner-influenced revenue (% total) | 5-15% | 15-25% | 20-30% | Crossbeam composite, 2023 |
| Partner-influenced ARR (2025 median) | | | 26-28% | SaaS Hero, 2025 |

### Deal Performance (Partner vs Direct)

| Metric | Value | Source |
|--------|-------|--------|
| Win rate uplift (avg, all ecosystem sizes) | **+11.7%** | Crossbeam Partner Impact Analysis, 2024 |
| Win rate uplift (1-5 partners) | +9.4% | Crossbeam, 2024 |
| Win rate uplift (50+ partners) | +37.1% | Crossbeam, 2024 |
| Win rate multiplier (partner-involved) | **2.8x** | Introw, 2024 |
| ELG deals; closure probability | **53% more likely** | Crossbeam, 2023 (500+ GTM leaders) |
| Sales cycle acceleration | **46% faster** | Crossbeam, 2023 |
| Deal size uplift | **32-60% larger** | Introw (32%); SaaS Hero (60%); Crossbeam cases (34-40%) |
| Pipeline increase from account mapping | **+44%** | Introw, 2024 |
| Pipeline from 10+ partner signal sharing | **+291%** | Reveal, 2024 |
| Churn reduction (partner-involved) | **58% less likely** | Crossbeam, 2023 |
| EQL conversion vs outbound | **53% faster** | Crossbeam, 2024 |

### Unit Economics

| Metric | Value | Source |
|--------|-------|--------|
| Avg B2B SaaS CAC (all channels) | $1,200 | SaaS Hero, 2026 |
| Partner/referral programme CAC | ~$150 (lowest across all channels) | Genesys Growth, 2026 |
| Partner LTV:CAC ratio | 3:1+ (vs ~2.5:1 direct) | SaaS Hero, 2025 |
| Programme ROI (3-year, Forrester-validated) | **296%** | Impartner/Forrester TEI, 2024 |
| Partner-sourced deal increase (Forrester) | Up to **+50%** | Impartner/Forrester TEI, 2024 |

### Programme Operations

| Metric | Early | Growth | Mature | Source |
|--------|-------|--------|--------|--------|
| Partner activation rate (active <90 days) | 40-60% | 60-75% | 75-85% | Crossbeam composite |
| Deal registration → closed-won conversion | 20-35% | | | Industry composite |
| Time to first deal (new partner) | 90-120 days | 60-90 days | 30-60 days | Crossbeam composite |
| Partner retention rate | 70-85% annually | | | Industry composite |
| Programmes with <50 partners | 56% of all programmes | | | Rewardful, 2025 |
| Programmes scaling beyond 1,000 | Only 10% | | | Rewardful, 2025 |

**Primary sources:** Crossbeam State of Partner Ecosystem 2023 (500+ GTM leaders); Crossbeam Partner Impact Analysis 2024 (continuous dataset, thousands of companies); PartnerStack Research Lab 2024 ($500M+ in transaction data, 106K+ active partners); Impartner/Forrester Total Economic Impact 2024; Introw 2024; SaaS Hero / Genesys Growth 2025-2026.

---

## Partner Technology Stack

### Tool Selection by Stage

| Stage | Recommended Stack | Investment |
|-------|------------------|------------|
| <€5M ARR | No dedicated tooling. Track in CRM (HubSpot/Salesforce). | €0 |
| €5-15M ARR | **Kiflo** (SMB PRM, $5-15K/yr) or **Introw** (EU, $329-579+/mo) + CRM native tracking | €5-15K/yr |
| €15-50M ARR | **PartnerStack** ($15K+/yr) or **Introw** + **Crossbeam** for account mapping | €25-40K/yr |
| €50-150M ARR | **Impartner** ($20-50K+/yr) or **Channeltivity** ($22-26K/yr) + **Crossbeam** + cloud marketplace tools (if relevant) | €50-100K/yr |
| >€150M ARR | **Impartner** / **Salesforce PRM** ($165K+/yr) + **Crossbeam** + **Tackle.io/Clazar** (marketplace) + **Seismic** (enablement) | €150K+/yr |

### Key Tools by Category

**Account Mapping & Ecosystem Intelligence:**
- **Crossbeam** (merged with Reveal, June 2024): 25,000+ companies. Dominant account overlap platform. Philadelphia + Paris HQ.
- **Introw** (Ghent, Belgium): EU-native, ISO27001, GDPR. CRM-first with AI partner agent. Best option for EU compliance requirements.

**Partner Relationship Management (PRM):**
- **PartnerStack**: Purpose-built for B2B SaaS. 80K+ partner marketplace. Automated payouts.
- **Impartner**: Number one for global mature programmes. Forrester-validated 296% ROI. End-to-end partner lifecycle.
- **ZINFI**: IDC MarketScape Leader 2025. Enterprise-scale channel automation. Competes with Impartner at €150M+ ARR scale.
- **Kiflo**: Lightweight starter PRM for early-stage programmes.
- **Allbound/Channelscaler**: Mid-market. Strong deal registration and governance. Merged with Channel Mechanics.
- **Channeltivity**: 18+ years in market. High customisation, strong CRM integrations.
- **Mindmatrix**: Enterprise PRM with marketing collateral, training, and alliance management.

**Cloud Marketplace Distribution:**
- **Tackle.io** (acquired by AppDirect, Dec 2025): $20B+ in marketplace transactions. AWS, Azure, GCP.
- **Clazar**: Days-to-list marketplace acceleration. CRM-driven private offers.
- **Market context:** Cloud marketplace GMV ~$30B in 2024, projected $160B by 2030. 89% of companies transact on 1+ marketplace, but only 22% drive meaningful revenue (Clazar, 2025).

**Vertical SaaS Marketplaces (Primary Distribution Channels):**
- **Salesforce AppExchange**: 7,000+ apps. 40%+ of Salesforce expansion revenue flows through ecosystem. Co-sell with Salesforce partners.
- **HubSpot App Marketplace**: 1,700+ apps. Highest-converting distribution channel for HubSpot ecosystem plays. Native integration revenue stream.
- **Atlassian Marketplace**: 3,000+ apps across Jira, Confluence, Trello, Bitbucket. Strong for integration and extension partners.
- **Slack App Directory**: 4,000+ apps. Native integration model; "must-have" for workflow tools and data connectors.
- **Shopify App Store**: 6,000+ apps. Commerce-first ecosystem; highest per-app revenue of any vertical marketplace.
- **Why this matters.** Vertical marketplace revenue often outperforms cloud marketplace for B2B SaaS. Reasons: higher intent buyers, shorter sales cycle, lower CAC. Partners should prioritise 1-2 vertical marketplaces matching their customer base over generic cloud marketplaces.

**Sales & Partner Enablement:**
- **Seismic** (merging with Highspot, Feb 2026): Enterprise sales enablement with partner features.
- **HubSpot** (partner tools): Built-in partner management. EU data residency available.
- **Salesforce PRM** (Partner Cloud): Native CRM partner management. EU data residency option.

### EU Compliance Tiers

| Grade | Tools |
|-------|-------|
| **A+ (EU-native)** | Introw (Belgium: ISO27001, GDPR, EU data residency) |
| **A (EU data residency available)** | Crossbeam/Reveal (Paris office), Salesforce (EU DC), HubSpot (EU DC) |
| **B+ (GDPR-aware, US-hosted)** | PartnerStack, Impartner, Impact.com, Channeltivity, ZINFI |

### Recent Market Moves (Track for Client Conversations)

- **Crossbeam + Reveal merger** (June 2024): All-stock transaction. Creates single dominant account mapping platform. 25,000+ companies, 135 employees.
- **Tackle.io acquired by AppDirect** (Dec 2025): Cloud marketplace management consolidating.
- **Highspot + Seismic merger** (Feb 2026): Sales/partner enablement consolidating into single platform. Unified pricing timeline and product roadmap still under development; recommend deferring tool selection until post-close clarity (Q3 2026).
- **Azure flat 3% marketplace fee** (Azure Marketplace Pricing, 2025): Dramatically improves partner economics on Azure Marketplace. Compare to AWS (3% on select products) and GCP (variable by category).

---

## ELG Market Context (2025-2026)

Key data points for framing partner strategy conversations:

- **60%** of SaaS leaders are investing in ecosystem-led growth (Pavilion, 2024)
- **67%** of partner ecosystem decision-makers plan for indirect revenue to grow >30% YoY (Forrester, 2025)
- **89%** of sellers use partners daily; **84%** of sellers who hit quota credit partners (Highspot, 2025)
- **75%** of partner ecosystem marketing decision-makers increasing technology investment (Forrester, 2026)
- Partners per customer rising from **7 to 17** by 2026 (driven by modular products, embedded AI, and compliance localisation; Jay McBain, Omdia/Canalys)
- Channel market forecast FY2026: **$63.7 billion**, +11.7% growth (Canalys Channel Index)
- AI becoming essential for ecosystem management at scale (87% of revenue teams used AI in 2025, 96% expect to in 2026; Highspot)

---

## How to Use This Skill

**"We want to build a partner programme":** Start with the Ideal Partner Profile. Don't recruit before you define who you're looking for. Then build the minimum viable programme: partner agreement, onboarding process, deal registration, basic CRM tracking. Recruit 3-5 partners. Get to first revenue. Then scale.

**"Partners aren't bringing deals":** Diagnose the layer. Is it Fundamentals (partners don't know how to sell your product)? Adoption (partners aren't executing the process)? Optimization (process exists but isn't producing results)? Usually it's enablement; partners need more support than you think.

**"How do we structure partner tiers?":** Use the three-tier model. T1 strategic (3-5 partners, highest investment, highest return). T2 growth (10-20, standard programme). T3 referral (unlimited, low-touch). Promote based on performance, not tenure.

**"Sales and partners are fighting over accounts":** Install deal registration with clear conflict resolution. First to register wins. Co-sell when both are engaged. Make the economics work for both sides. Escalation path that resolves in 48 hours.

**"How do we measure partner programme ROI?":** Track partner-sourced and partner-influenced pipeline and revenue separately. Compare deal metrics (win rate, cycle time, deal size, LTV) between partner and direct. Total programme cost ÷ total partner-attributed revenue = ROI. Expect 6-12 months before ROI turns positive.

**"We need to scale from 5 to 50 partners":** You're moving from Fundamentals to Adoption/Optimization. Invest in: partner portal, tiered structure, account mapping technology (Crossbeam/Reveal), dedicated partner team (3+ FTEs), and partner marketing (MDF, co-marketing). Don't scale what isn't working at small scale.

## Canon References

- **revops-handoffs**: Handoff design between partner and direct sales
- **gtm-planning**: GTM motion design including partner/channel capacity planning
- **sales-methodology**: Qualification frameworks for partner-registered deals
- **revops-hubspot**: CRM implementation for partner objects

> Built by [Neon Triforce](https://neontriforce.com)
