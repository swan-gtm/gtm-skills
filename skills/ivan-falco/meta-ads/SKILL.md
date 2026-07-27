---
name: "meta-ads"
title: Meta ads management
description: |
  Use this skill when managing Meta (Facebook/Instagram) ads for B2B — audience strategy, campaign structure, creative-as-targeting, CAPI and conversion tracking, creative testing, fatigue detection, and lead form optimization for B2B SaaS on Meta's platform.

  Triggers: Meta Ads, Facebook Ads, Instagram Ads, Meta campaign, Facebook lead gen, Meta lead forms, Facebook retargeting, Meta remarketing, Facebook lookalike, Meta audience, Advantage Plus, Meta B2B.
category: Ads
---

# Meta Ads Management for B2B

Orchestrator for all Meta Ads (Facebook/Instagram) tasks. Meta Ads for B2B can deliver half the cost per lead and lower cost per qualified opportunity compared to LinkedIn - but only when audience data quality is right and creative does the targeting work.

## Methodology

This skill implements the Ivan Falco B2B demand generation methodology for Meta - a data-first, creative-as-targeting approach that leverages Meta's algorithm (Andromeda + Gem) with high-quality audience inputs and systematic creative testing.

## Core Philosophy

**On Meta, your data is everything. Your creative is your targeting.**

Meta's native targeting can't match LinkedIn's B2B precision (no job title, company, seniority filters). The way to make Meta work for B2B is to bring your own high-quality audience data (CRM, third-party providers) and use creative specificity to filter for ICP. The algorithm (Andromeda + Gem) does the rest.

## Routing Logic

### Always Load First

**Any Meta work starts here:**

| Intent | File | Priority |
|--------|------|----------|
| **Scaling qualified B2B pipeline end to end** (the goal is SQLs / qualified pipeline, not lead volume) | [scale-b2b-qualified-pipeline.md](/skill/scale-b2b-qualified-pipeline) | LOAD FIRST when the goal is qualified pipeline. The 6-step spine (map market -> audiences -> funnel events/CAPI -> creative -> segments -> SQL reporting) that ties the audience, CAPI, creative, and reporting files together. |
| **ANY operational decision** (pause, scale, graduate, budget, creative count) | [meta-ads-operating-system.md](/skill/meta-ads-operating-system) | ALWAYS LOAD FIRST. This is THE decision framework. All formulas, thresholds, and actions live here. |
| **Auditing an account** (pull data, classify ads, produce recommendations) | Load the OS file above + run `scripts/get_active_ads_copy.py` | Pull active ads, classify by OS rules, produce recommendations. |
| **Creative production decisions** (what to build, when to iterate, cadence, formats) | [creative-cadence-operating-system.md](/skill/creative-cadence-operating-system) | Iteration hierarchy, concept sourcing, format playbook, testing cadence, fatigue detection, quality scoring. |

### Deeper Context (Load When Needed)

These files provide detailed methodology on specific topics. The OS drives decisions; these explain the deeper why and how.

| User Intent | Knowledge Base File | When to Use |
|-------------|-------------------|-------------|
| Full Meta B2B overview, algorithm, strategy | [meta-b2b-overview.md](/skill/meta-b2b-overview) | Andromeda + Gem, strategy, "what works" - overview and quick reference |
| Pixel, tracking, first campaign setup | [meta-setup-and-tracking.md](/skill/meta-setup-and-tracking) | Installing the pixel, Events Manager, domain verification, CAPI, pre-launch |
| CAPI, conversion events, HubSpot vs n8n | [meta-capi-and-events.md](/skill/meta-capi-and-events) | Conversions API, event hierarchy, CRM to CAPI, deduplication, Event Match Quality |
| Webinar/event, third-party conversion | [meta-third-party-conversion-tracking.md](/skill/meta-third-party-conversion-tracking) | Off-domain conversion (Luma, etc.), pixel in platform vs thank-you page |
| Audience targeting, data strategy, lookalikes | [audience-strategy.md](/skill/meta-audience-strategy) | Building audiences, data sources, audience validation, third-party tools |
| Detailed campaign structure, phases, roadmap | [campaign-structure.md](/skill/meta-campaign-structure) | Phase 1/2/3 deep dive, naming conventions, campaign architecture, month-by-month roadmap |
| Creative concepts, copy, formats | [creative-strategy.md](/skill/meta-creative-strategy) | Creative development, concept testing, placement optimization, creative-as-targeting |
| Creative fatigue detection, rotation system | [creative-fatigue-detection.md](/skill/creative-fatigue-detection) | Full fatigue workflow, rotation cadence, pipeline management, format-specific notes |
| Advantage+ setup and details | [advantage-plus.md](/skill/advantage-plus) | When to use Advantage+, setup steps, budget requirements, ABM considerations |
| Optimization playbook, benchmarks | [optimization-playbook.md](/skill/meta-optimization-playbook) | Decision trees, B2B benchmarks, seasonal patterns, weekly cadence, scaling protocol |
| Ad quality scoring, message validation | [message-validation.md](/skill/message-validation) | Scoring ads against revenue quality, winner scaling pattern, validation process |
| Lead forms, conversion optimization | [lead-form-optimization.md](/skill/lead-form-optimization) | Lead form setup, work email validation, custom questions, social amnesia |
| ABM on Meta | [abm-on-meta.md](/skill/abm-on-meta) | ABM targeting, Advantage+ conflicts, manual vs hybrid approach |
| Offer strategy by funnel stage | [offer-strategy.md](/skill/meta-offer-strategy) | What offers to run at each funnel stage |
| **Creating campaigns, ads, audiences** (the full build chain) | [creating-campaigns-ads-audiences.md](/skill/creating-campaigns-ads-audiences) | End-to-end: audience -> campaign -> ad set -> creative -> ad. Endpoints, scripts, PAUSED-by-default rules. |
| **Reporting / dashboards** | use the `meta-reporting` skill | Performance analysis + a branded HTML dashboard with your logo. |

## Scripts (execution layer)

Python scripts live in `scripts/` and hit the Meta Marketing API (v22.0) through
the shared `scripts/client.py` (credentials from `.env`). Full index, key args,
and examples: [scripts/README.md](scripts/README.md). **Every create defaults to
`PAUSED`.** Budgets are in cents. Any script accepts `--account-id act_XXXXXXXXX`
to override the default account.

**Analyze / Report**

| Script | Use when you need to... |
|--------|------------------------|
| `account_overview.py` | Pull an account-level metrics dashboard (with optional period comparison) |
| `list_campaigns.py` / `list_ad_sets.py` / `list_ads.py` | List objects with status, budget, targeting, and 30-day metrics |
| `get_campaign_performance.py` | Get detailed campaign analytics with date presets / daily breakdown |
| `get_active_ads_copy.py` | Dump full creative and copy of every active ad (audits) |
| `top_ads.py` | Rank ads by spend or cost per lead to find winners |

**Create (default PAUSED)**

| Script | Use when you need to... |
|--------|------------------------|
| `create_campaign.py` | Create a campaign |
| `create_ad_set.py` | Create an ad set (targeting, optimization goal, pixel/page promoted object) |
| `create_ad.py` | Create a single-image or video ad (creative + ad) |
| `create_dco_ad.py` | Create a dynamic/flexible creative (DCO) ad from multiple assets |

**Manage**

| Script | Use when you need to... |
|--------|------------------------|
| `update_campaign.py` | Change a campaign's status, budget, or name |
| `duplicate_ad.py` | Duplicate an ad (optionally into another ad set, N copies) |
| `ad_scheduler.py` | Schedule automatic ad pauses (e.g. webinar ads), run from cron |

**Audiences**

| Script | Use when you need to... |
|--------|------------------------|
| `create_custom_audience.py` | Create a custom audience from a hashed CSV |
| `update_custom_audience.py` | Add or remove hashed members in an existing audience |
| `upload_lookalike.py` | Create lookalike audiences from a source audience (one per country) |

## Core Rules

1. **Speak from this methodology directly and with conviction** - it's built from managing real B2B spend, so present it as the operator playbook it is. Don't pad with generic "best practices."

2. **Data quality determines Meta success for B2B.** Always follow the data hierarchy: CRM lookalikes (Tier 1) -> Third-party data (Tier 2) -> Broad targeting (Tier 3). Never skip to broad without testing data-driven audiences first.

3. **Validate audience quality before scaling creative.** Use ABO (ad set budget) campaigns with one ad set per audience source and the same ads across all. Audit lead quality by job title and company. Only scale winning audiences with CBO.

4. **Creative concept testing, not micro-variations.** Test dramatically different concepts (UGC vs before/after vs meme vs product demo), not minor tweaks (blue vs green button). The algorithm needs creative diversity to learn.

5. **Creative IS targeting on Meta.** Your ad copy must explicitly call out who the ad is for. When running broader audiences, the creative does the filtering work - it should act as "mosquito repellent" for non-ICP.

6. **Lead forms need intentional friction for B2B.** Always require work email validation. Add 1-3 custom qualification questions. Use Higher Intent form type. This combats social amnesia and improves lead quality.

7. **Build in this order: Remarketing -> Prospecting -> Acceleration.** Start with remarketing (lowest risk, highest ROI, creates omnipresence). Layer prospecting once remarketing is running. Add acceleration for open pipeline if applicable.

8. **Cross-channel remarketing is a superpower.** Create Meta retargeting audiences from LinkedIn/Google traffic using UTM parameters. You retarget validated audiences on Meta at a fraction of the cost.

9. **Broad targeting only works for large TAM.** If you're doing ABM or targeting niche enterprise, broad will not work - stick to Tier 1 and Tier 2 data sources. Broad is for SMB/lower mid-market with massive addressable markets.

10. **Meta's algorithm (Andromeda + Gem) needs creative volume.** Maintain 4-6 unique creative concepts per campaign. The algorithm processes ads to learn what works - more diverse inputs = better optimization.

## Key Differences from LinkedIn

| Aspect | Meta | LinkedIn |
|--------|------|----------|
| Native B2B targeting | Weak - bring your own data | Strong - job title, company, seniority |
| Cost per lead | ~50% of LinkedIn | Higher but more precise |
| Algorithm role | Heavy - drives targeting through creative signals | Light - advertiser controls targeting |
| Creative volume needed | High (4-6+ unique concepts) | Moderate (4-6 per campaign) |
| Remarketing strength | Excellent - cheap, cross-platform omnipresence | Good but more expensive |
| Lead form quality | Requires friction management (social amnesia risk) | Higher quality by default (work email auto-fill) |
| Best for | Large TAM, SMB/mid-market, remarketing, pipeline acceleration | Enterprise, ABM, precise ICP targeting |

## Output Standards

- Campaign plans -> Use docx skill for professional Word documents
- Performance reports -> Use xlsx skill for data-driven spreadsheets
- Creative briefs -> Structured concept descriptions with placement specs
- All documents -> Professional, client-ready quality. No source citations.

## When to Combine with LinkedIn

Meta and LinkedIn are not competitors - they're complementary channels:

- **LinkedIn for precision prospecting** (right person, right company) + **Meta for cheap remarketing** (stay top of mind across platforms)
- **LinkedIn for ABM** (company-level targeting) + **Meta for ABM extension** (via third-party tools like Primer/Metadata.io)
- **LinkedIn for enterprise** (where precision justifies the cost) + **Meta for mid-market/SMB** (where volume and cost efficiency matter more)
- Use cross-channel UTM remarketing to bridge the two platforms
