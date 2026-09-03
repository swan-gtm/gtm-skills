---
name: google-ads-audit
title: Google Ads audit
description: "Use this skill when someone wants a Google Ads account audited or optimized at senior-media-buyer depth: Search campaigns, search terms and keywords, Shopping and product feeds, Performance Max, or keyword research. Classifies search terms into five intent tiers, separates rank pressure from budget pressure, grades Shopping SKUs (kill, downgrade, promote), gates PMax changes on maturity and asset labels, and compares PMax against Search on ROAS. Read-and-recommend only: it never changes the account, the user applies every recommendation in the Google Ads UI. Trigger phrases: Google Ads audit, wasted spend, search term report, PMax review, Shopping feed, keyword research, why is my CPC rising."
category: Ads
tags: [Ads]
---

> Adapted from the GoMarble Paid Media Claude Skills repository (https://github.com/gomarble-ai/gomarble-ai-paid-media-claude-skills) by its author, shared under GoMarble's attribution license. Works with any data source: a connected ads MCP such as GoMarble, CSV exports, screenshots, or pasted tables.

A consolidated set of skills for analyzing and optimizing Google Ads accounts. These skills are **framework-agnostic** - the analytical logic (Q1–Q5 query tiers, auction-pressure diagnosis, PMax maturity gates, item classification) applies regardless of where the data comes from.

The skills define **what to know, what data to look for, how to interpret it, and how to recommend action**. They do not depend on any specific tool integration.

> **Read-and-recommend only.** These skills never make changes to the user's Google Ads account. Claude reads data and produces recommendations in plain language; the user applies the recommended changes themselves in the Google Ads UI.

---

## Data Sources Are Not All Equal

Data can come from four kinds of sources, but they have **very different completeness**. Some skill rules silently break on weaker sources - most notably, PMax asset performance labels and PMax search term insights are NOT in default Google Ads CSV exports. Always identify the source first and consult the **Data Source Compatibility Matrix** below before applying any rule.

| Priority | Source | Notes |
|---|---|---|
| 1 (preferred) | A connected MCP server exposing Google Ads data (e.g. GoMarble) with GAQL access | All rules work. Query each Google Ads resource via GAQL. |
| 2 | CSV / Excel exports from Google Ads UI | Most basic rules work, but PMax assets, PMax search insights, and Quality Score components require *separate UI reports* the user often doesn't realise they need. |
| 3 (narrow questions only) | Screenshots of report tables | Use only for spot questions on metrics visible in the screenshot. Skip deep analysis. |
| 4 (last resort) | Direct copy-paste of metric values | Treat as user-asserted; ask for the underlying export when stakes are real. |

---

## How to Use These Skills

1. **Identify the user's intent** - are they asking about Search, Shopping, Performance Max, or keyword research? Use the routing table below.
2. **Run the Data Inventory step (Step 0 below)** - confirm what source is being used and what's actually available before invoking any skill.
3. **Gather the required data** - ask the user to share the data the skill needs. The "Minimum required data" section of each skill lists what's needed.
4. **Apply the analytical framework** - classify, diagnose, decide based on the rules in the relevant skill.
5. **Always check guardrails** before recommending any action.
6. **Output recommendations** in the structured format defined per skill.

If required data is missing or unverifiable, say so explicitly and ask the user for it. **Never fabricate metrics or invent thresholds.**

---

## Step 0: Data Inventory (Mandatory Before Any Skill)

Run this once at the start of every analysis. It takes one short turn and prevents wasted effort - especially for PMax, where users often share a campaign CSV without realising they're missing the Asset Group Asset and Search Term Insights reports.

1. **Identify the data source** - MCP / CSV / screenshot / copy-paste. If MCP with GAQL access is connected, use it. If the user attached a file, inspect its columns/fields before asking for more.
2. **State what's available and what's missing** for the requested skill, based on the Data Source Compatibility Matrix below.
3. **For each missing signal, decide:**
   - **Blocking** - cannot proceed without it; ask user to fetch (e.g. Asset Group Asset report for PMax).
   - **Downgrade** - can proceed with caveats; flag as low-confidence in the output.
   - **Skip** - rule doesn't apply to this source (e.g. micros conversion on CSV data already in account currency); note it and move on.
4. **Confirm account currency** before showing any monetary value - never assume USD.
5. **Confirm the date range** in the data matches what the skill expects (30 days for Search; 14d or 30d for Shopping depending on volume; 30d for PMax with optional 60d for trend).

Output one short paragraph before applying the skill. Example:
> *"Using your GoMarble MCP via GAQL. For the PMax audit (Skill 3), I'll pull (1) campaign performance, (2) `asset_group_asset` for performance labels, (3) `campaign_search_term_insight` for PMax categories, (4) device + geo segments. Account currency confirmed as USD."*

---

## Data Source Compatibility Matrix

Use to plan which signals you can get from which source before running any skill.

| Signal | MCP (GoMarble etc. with GAQL) | CSV (Google Ads UI exports) | Screenshot |
|---|---|---|---|
| Campaign performance (cost, conversions, conversion value, clicks, impressions, CTR, avg CPC) | ✅ via standard `metrics.*` fields | ✅ default Campaign report | ✅ if shown |
| Cost in account currency | ✅ but `cost_micros` returned by API - **divide by 1,000,000** | ✅ already in account currency - **skip the micros rule** | ✅ |
| Average CPC | ✅ in account currency (no conversion) | ✅ in account currency | ✅ |
| Search Impression Share, IS Lost (Rank), IS Lost (Budget) | ✅ via `metrics.search_impression_share`, `search_rank_lost_impression_share`, `search_budget_lost_impression_share` | ✅ but column names vary ("Search lost IS (rank)" / "Impr. share lost (rank)") - match by meaning | ⚠️ |
| Top of Page Rate / Absolute Top of Page Rate | ✅ via `metrics.top_impression_percentage`, `absolute_top_impression_percentage` | ✅ default Search columns | ⚠️ |
| Search term report | ✅ via `search_term_view` resource | ✅ separate "Search Terms" report - **not in the Campaigns export** | ❌ |
| Keyword-level performance | ✅ via `keyword_view` resource | ✅ separate "Keywords" report | ⚠️ |
| Quality Score components (Expected CTR / Ad Relevance / Landing Page) | ✅ via `ad_group_criterion.quality_info.*` | ⚠️ requires Quality Score columns enabled in the Keywords report | ❌ |
| Bid strategy + target | ✅ via `campaign.bidding_strategy_type` + `target_cpa.target_cpa_micros` / `target_roas.target_roas` | ⚠️ requires Bid Strategy + Target columns enabled (often not default) | ⚠️ |
| Daily budget utilization | ✅ via `segments.date` aggregation | ⚠️ requires day-by-day segmented export | ❌ |
| Shopping item-level performance | ✅ via `shopping_performance_view` | ✅ separate "Products" report | ❌ |
| Merchant Center approval rate | ❌ requires manual check in Merchant Center | ❌ same | ❌ same |
| PMax asset performance labels (BEST / GOOD / LOW / PENDING / UNSPECIFIED) | ✅ via GAQL on `asset_group_asset` with `performance_label` | ❌ **NOT in default exports** - requires Asset Report (separate UI report) | ❌ |
| PMax search term insights (aggregated categories) | ✅ via GAQL on `campaign_search_term_insight` | ❌ **NOT in default exports** - requires Search Terms Insights from the PMax campaign page | ❌ |
| PMax asset group structure (asset group ID, name, status) | ✅ via `asset_group` | ⚠️ partial - visible in PMax campaign page but not always in exports | ⚠️ |
| Device performance | ✅ via `segments.device` | ✅ separate "Devices" segment export | ⚠️ |
| Geographic performance | ✅ via `geographic_view` | ✅ separate "Locations" report | ⚠️ |
| Time-of-day / day-of-week | ✅ via `segments.day_of_week` / `hour` | ✅ separate "Time" segment export | ⚠️ |
| Auction Insights (competitor share) | ⚠️ limited via API (`auction_insight_domain`) | ✅ separate "Auction Insights" UI report | ⚠️ |
| Conversion type / value source | ✅ via `conversion_action` resource + `segments.conversion_action_category` | ⚠️ requires "Conversion action" segment + "All conv. value" enabled | ❌ |
| Keyword Planner data (volume, top-of-page bid, competition) | ✅ via `google_ads_keyword_discover` / `google_ads_keyword_metrics` (GoMarble) | ✅ via Keyword Planner export | ❌ |

✅ = available and reliable. ⚠️ = available but requires extra export / column / segment enabled. ❌ = not available from this source.

---

## Google Ads CSV Column Translation

When the source is a CSV export from the Google Ads UI, column names rarely match the API field names used throughout the skills. Use this table to translate. Column names vary slightly by language, account version, and export template - **match by meaning, not exact string**.

| Skill / API reference | Typical Google Ads CSV column |
|---|---|
| `metrics.cost_micros` | "Cost" (already in account currency in CSV - micros rule does not apply) |
| `metrics.conversions` | "Conversions" |
| `metrics.conversions_value` | "Conv. value" or "All conv. value" |
| `metrics.clicks` | "Clicks" |
| `metrics.impressions` | "Impr." |
| `metrics.ctr` | "CTR" |
| `metrics.average_cpc` | "Avg. CPC" |
| `metrics.search_impression_share` | "Search impr. share" |
| `metrics.search_rank_lost_impression_share` | "Search lost IS (rank)" / "Impr. share lost (rank)" |
| `metrics.search_budget_lost_impression_share` | "Search lost IS (budget)" / "Impr. share lost (budget)" |
| `metrics.top_impression_percentage` | "Top impr. rate" / "Search top IS" |
| `metrics.absolute_top_impression_percentage` | "Abs. top impr. rate" / "Search abs. top IS" |
| `metrics.value_per_conversion` (ROAS = this / cost) | "Conv. value / cost" or compute as Conv. value ÷ Cost |
| `campaign.bidding_strategy_type` | "Bid strategy type" (must enable) |
| `target_cpa.target_cpa_micros` | "Target CPA" |
| `target_roas.target_roas` | "Target ROAS" |
| `campaign.budget_amount_micros` | "Budget" or "Daily budget" |
| `ad_group_criterion.quality_info.quality_score` | "Quality Score" (must enable in Keywords report) |
| `ad_group_criterion.quality_info.creative_quality_score` | "Ad relevance" (must enable) |
| `ad_group_criterion.quality_info.post_click_quality_score` | "Landing page experience" (must enable) |
| `ad_group_criterion.quality_info.search_predicted_ctr` | "Expected CTR" (must enable) |
| `asset_group_asset.performance_label` | ❌ NOT in standard CSV - requires Asset Report from the PMax campaign |
| `campaign_search_term_insight.*` | ❌ NOT in standard CSV - requires Search Terms Insights from PMax campaign page |

**Rule for Claude:** if the source is CSV, **costs are already in account currency** - never apply the divide-by-1,000,000 rule. That rule only fires on raw API/MCP data.

---

## Routing - Which Skill to Use

| User asks about | Use Skill |
|---|---|
| Search campaigns, keywords, RSAs, text ads, search terms | **Search Optimization** |
| Shopping campaigns, product feed, Merchant Center, SKUs | **Shopping Optimization** |
| Performance Max, PMax, asset groups | **PMax Optimization** |
| Keyword research, new keyword ideas, search volume, CPC estimates, market expansion | **Keyword Research** |
| Change requests (create campaign, add keyword, change bid, pause, etc.) | Apply the relevant analysis skill first, then **recommend** the change in plain language with rationale. Claude does not execute changes on the user's ad account - the user applies recommendations manually in the Google Ads UI. |

If the user's intent is ambiguous or spans multiple campaign types, ask which to focus on first.

---

## Universal Guardrails - Apply Before Every Recommendation

These rules apply across every skill below. **Read them before generating any recommendation.**

### Budget Reallocation Prohibition

You **cannot** allocate, shift, increase, reduce, or "optimize" budget for: keywords, search terms, match types, devices (unless via bid adjustments in Search), locations (unless via bid adjustments or exclusions), audiences (unless via bid modifiers), asset groups (PMax has no per-asset-group budgets).

**Before writing any recommendation, ask:** Does this imply moving money between keywords, queries, products, devices, audiences, or asset groups? If yes → rewrite using the valid controls below.

**Valid budget controls:**

| Campaign Type | Valid Controls |
|---|---|
| Search / Shopping | Campaign daily budget, bid strategy targets (tCPA / tROAS / max CPC), pause or enable campaigns or ad groups |
| Performance Max | Campaign daily budget, bid strategy targets (tCPA / tROAS), pause asset groups or campaign |

**Mandatory rewrites:**

- ❌ "Shift budget from keyword A to keyword B"
- ✅ "Pause keyword A. Increase campaign daily budget by 10–20% to give keyword B more eligible demand."

- ❌ "Allocate more to [placement / device / demographic / product / asset group]"
- ✅ "Create a new campaign targeting [dimension] with its own budget, or use bid adjustments / exclusions."

### Metric Selection

First infer the account's conversion type:

- **Ecommerce**: Use ROAS, conversion value, cost per purchase. Never use CPA alone for revenue decisions.
- **Lead gen**: Use CPA, cost per lead. Never use ROAS unless offline revenue is imported.
- **Footfall / awareness / local-service**: Replace CPA/ROAS with cost per footfall action, cost per call, cost per direction, CPM, reach, frequency. State explicitly that purchase-derived CPA/ROAS do not apply.
- **Unclear**: Ask the user. Do not assume.

### Scaling Limits

- Max budget increase: **20% per move** for Search/Shopping; up to **50% per move** for mature PMax.
- Never scale if: CPA > target, ROAS < target, or query / search term hygiene not done.
- Never scale based on: impression share alone, CPC alone, or early data (< 7 days).
- Frame scaling as: "incremental test with downside risk."

### Learning & Stability

- Do not stack changes (budget + bids + structure simultaneously).
- Do not judge performance on: < 30 conversions for Search, < 50 conversions for PMax/Shopping.
- Avoid changes that reset learning unless absolutely required.

### Immediate STOP Triggers

Halt any recommendation that attempts:

- "Scale keywords / products / asset groups"
- "Reallocate spend between queries"
- "Optimize placements in PMax"
- "Increase bids and budget at the same time"
- "Scale > 20% in one step"
- "Fix low impression share by increasing budget blindly"

### Required Diagnostics Before Any Action

Before any scale/pause/restructure suggestion, confirm you know:

1. Search term quality (presence of Q4 / Q5 queries - defined in the Search skill)
2. CPA / ROAS vs target
3. IS Lost split: Rank vs Budget
4. CPC trend direction
5. Conversion volume sufficiency
6. Bidding strategy compatibility

If diagnostics are incomplete → say **insufficient data**, ask for what's missing, and do not recommend.

---

## Metric Glossary - Canonical Definitions

Used across every skill below.

### Currency Note: Micros (API/MCP only)

**This rule applies only to raw API / MCP data.** If the source is a CSV export from the Google Ads UI, costs are already shown in account currency - **skip this rule.**

When data is pulled from API exports (MCP / GAQL), cost and bid fields are often returned in **micros** (1,000,000 micros = 1 unit of account currency). If you see fields named `cost_micros`, `cpc_bid_micros`, or `amount_micros`, divide by 1,000,000. `average_cpc` is typically already in account currency.

**Source check before applying:**
- MCP returning `*_micros` fields → divide by 1,000,000.
- CSV with a "Cost" or "Avg. CPC" column → already in account currency; do nothing.
- Screenshot showing a currency symbol → already converted; trust it.

**Always confirm account currency before showing monetary values - never assume USD.**

### Direct Metrics

| Metric | Notes |
|---|---|
| Cost | Total spend in account currency |
| Conversions | Includes all configured conversion actions unless filtered |
| Conversion value | Revenue for value-based conversions |
| Clicks | |
| Impressions | |
| Average CPC | Already in account currency |
| CTR | Decimal (0.05 = 5%) |
| Search IS | Search impression share |
| IS Lost (Rank) | Share of impressions lost due to ad rank (quality + bid) |
| IS Lost (Budget) | Share of impressions lost because campaign hit daily budget |
| Top of Page Rate | Share of impressions appearing above organic results |
| Absolute Top Rate | Share of impressions appearing as the first ad |

### Calculated Metrics

| Metric | Formula |
|---|---|
| CPA | cost / conversions |
| ROAS | conversion value / cost (decimal multiple, e.g. 3.5 = 3.5×) |
| CVR | conversions / clicks × 100 |
| AOV | total conversion value / total conversions |
| CPC trend WoW | (this_week_cpc − last_week_cpc) / last_week_cpc × 100 |
| CPC trend MoM | (this_month_cpc − last_month_cpc) / last_month_cpc × 100 |
| Spend share | entity_cost / total_cost × 100 |

### Account-Type Inference

If the user hasn't stated account type, infer from data:

- **Ecommerce**: Purchase conversion actions present AND non-zero conversion value → use ROAS, AOV, CPA.
- **Lead gen**: Conversions present AND conversion value = 0 → use CPA only; ROAS unreliable unless offline conversion import is configured.
- **Mixed**: Group campaigns by primary conversion action and apply each group's metrics separately.
- **Unclear**: Ask the user. Don't default.

### Maturity & Statistical-Significance Gates

| Gate | Threshold | Rationale |
|---|---|---|
| Smart Bidding minimum (Search) | ≥ 30 conversions / 30 days | Below this, tCPA/tROAS lacks signal |
| Smart Bidding minimum (PMax / Shopping) | ≥ 50 conversions / 30 days | Wider channel mix needs more signal |
| PMax maturity gate | Age ≥ 30 days (ideally 60) OR conversions ≥ 50 | Required before any PMax optimization |
| Segment-level recommendation | ≥ 50 clicks AND ≥ 5 conversions | Below this → flag as low-confidence |
| Scaling step cap | ≤ 20% per move (Search/Shopping); ≤ 50% per move on mature PMax | |
| Lookback for Shopping | 14 days if ≥ 100 purchases/month, else 30 days | |

### PMax vs Search ROAS Comparison

Apply only after the PMax maturity gate passes.

| PMax ROAS Ratio | Assessment | Default Action |
|---|---|---|
| < 0.5× Search ROAS | Poor | Monitor closely; consider pausing if not improving |
| 0.5 – 0.9× Search ROAS | Below par | Optimize assets and negatives before any scaling |
| ≥ 0.9× Search ROAS | Healthy | Optimize; eligible for scaling |
| > Search ROAS | Outperforming | Prioritize scaling |

### PMax Asset Performance Labels

Google labels each PMax asset (it does NOT expose cost/conversion data per asset).

| Label | Interpretation | Default Action |
|---|---|---|
| BEST | Top performer in its asset group | Create variations with similar style |
| GOOD | Acceptable | Keep, monitor |
| LOW | Underperforming | Remove; replace with BEST variations |
| PENDING / UNSPECIFIED | Insufficient data | Wait 14+ days |

### Shopping Item Classification (used in the Shopping skill)

| Classification | Trigger |
|---|---|
| KILL | cost ≥ 2× AOV AND conversions = 0 |
| DOWNGRADE | ROAS < 0.7× target AND cost ≥ 0.5× AOV |
| PROMOTE | conversions ≥ 2 AND ROAS ≥ target |

### Quality Score Components (when CPC is high)

Decompose Quality Score into:

- Expected CTR
- Ad relevance
- Landing page experience

Identify which component is dragging and recommend fixes for that component. **Do not recommend bid changes alone to compensate for low Quality Score.**

---

## Depth-of-Analysis Framework - Apply on Audits & Optimization Reviews

Apply on: audits, performance reviews, optimization requests, strategy questions, account restructuring.
Skip for: simple data fetches, campaign listings, single-metric lookups.

### 1. Hierarchical Drill-Down

Never recommend on campaign-level aggregates alone. Drill deeper:

- Asked about a campaign → check ad group performance within it.
- Asked about an ad group → check keyword + search term performance within it.
- Asked about PMax → check asset group performance, search term categories, URL expansion config.

Quantify the driver: "Ad Group X accounts for 65% of campaign spend but CPA is 2× the campaign average."

### 2. Objective-Contextual Evaluation

Evaluate each campaign against its bid strategy target, not just absolute performance.

| Bid Strategy | Evaluate against | Red flag |
|---|---|---|
| tCPA | Actual CPA vs target CPA | CPA 30%+ above target |
| tROAS | Actual ROAS vs target ROAS | ROAS 30%+ below target |
| Maximize Conversions (no target) | CPA trend direction | Rising CPA with no constraint |
| Manual CPC | CPC vs Quality Score implied CPC | Paying premium due to low QS |

**Flag unconstrained strategies:** if tROAS target is 0.5× on a campaign achieving 3×, the algorithm isn't actually constrained. If tCPA is 3× above actual CPA, same problem. Call it out.

### 3. Breakdown & Segmentation Analysis

Before concluding, check at least 2 of these dimensions:

- Device performance (mobile vs desktop CPA gap)
- Search Partners conversion rate vs Search network (quantify the gap)
- Geographic variations (regions with high spend and poor CVR)
- Day-of-week patterns
- Cross-reference bid adjustments against actual segment performance

**Statistical significance:** Do not make segment-level recommendations from < 50 clicks or < 5 conversions. Flag as low-confidence.

### 4. Temporal & Trend Analysis

Never treat the date range as a single number. Compare:

- Last 7 days vs previous 7 days (WoW)
- Separate day-of-week seasonality from structural trends
- Identify direction for each key metric: improving, declining, stable

**Distinguish:** "metric is bad" vs "metric is getting worse" - direction matters more than absolute value.

**Connect the chain:** impression share declining → CPC increasing → competitive pressure, not quality degradation.

### 5. Cross-Entity Dependency Recognition

- **Brand Search ↔ PMax overlap**: Is PMax capturing brand terms? Check PMax search term categories.
- **Non-brand Search → Remarketing**: Does non-brand search activity feed remarketing lists?
- **Shopping ↔ Search overlap**: Same products advertised in both? Check for cannibalization.

**Flag dependencies:** "PMax and Brand Search are both converting on brand terms. Total reported conversions across both campaigns likely exceed actual unique conversions. Before scaling PMax based on its ROAS, factor in cannibalization from Brand Search."

### 6. Platform Mechanic Awareness

| Signal | Mechanic | Consequence |
|---|---|---|
| Broad match + rising CPC | Query expansion | Algorithm widens to less relevant queries → QS drops → CPC rises → tCPA struggles |
| Low QS + high CPC | Ad relevance | Paying premium for same position - fix relevance, not just bid |
| tCPA + low conversion volume | Smart Bidding data | Insufficient signal - consider Manual CPC |
| PMax + declining Brand Search IS | Brand cannibalization | PMax claiming brand conversions → inflated PMax ROAS |
| Maximize Conversions + no target | Unconstrained spend | Algorithm spends full budget at any CPA - add a tCPA target |

### 7. Proactive Signal Detection

After answering the user's question, surface 2–3 additional concerns or opportunities they didn't ask about.

Format: *"Outside your question, I noticed [signal] in [entity] - this suggests [predicted consequence] within [timeframe]."*

### 8. Attribution & Measurement Rigor

Don't take reported conversion numbers at face value.

Always check:

- Attribution model in use (last click, data-driven, etc.)
- Conversion lag - are recent days' conversions still incomplete?
- Share of conversions that are estimated (modeled) vs observed
- Mix of micro- vs macro-conversions

**Frame as caveat:** *"Before scaling based on the reported 5× ROAS, note that [attribution concern] means the true incremental ROAS is likely lower."*

---

# Skill 1: Search Campaign Optimization

A systematic approach to Google Ads Search via query classification, auction-pressure diagnosis, and rule-based decision logic.

**Workflow:** Data → Classification → Pressure Analysis → Decision → Action.

## When to use this skill

- Audit or optimize a Search campaign
- Diagnose why CPA / ROAS / impression share is changing
- Decide whether to scale, hold, or cut a Search campaign
- Identify wasted spend in search terms

## Data to gather

Ask the user to share - or pull from whatever data source is available - the following for the relevant Search campaigns over the **last 30 days**, filtered to ENABLED campaigns only.

**Campaign-level auction metrics:**

- Search impression share
- IS Lost (Rank)
- IS Lost (Budget)
- Top of Page Rate
- Absolute Top of Page Rate
- Average CPC
- Cost, conversions, conversion value, clicks, impressions

**Search-term report:** Each search term with impressions, clicks, cost, conversions, conversion value, sorted by cost descending (top 200 by spend).

**Keyword-level data:** Keyword text, match type, keyword impression share, IS Lost (Rank), avg CPC, conversions, cost.

**CPC trend:** Average CPC for the last 7 days AND the prior 7 days, so WoW change can be calculated.

**User inputs to request (if not already known):**

- Target CPA (or target ROAS for ecommerce). Default: historical 30-day average.
- Brand name (so brand vs non-brand terms can be classified)
- Competitor names (optional)
- Priority geographies (optional)

## Step 1: Classify Each Search Term (Q1 – Q5)

| Tier | Name | Condition |
|---|---|---|
| **Q1** | Profitable | Conversions ≥ 2, OR CPA ≤ target, OR ROAS ≥ target |
| **Q2** | Promising | Conversions = 0 AND cost < 0.5× target CPA AND no Q5 signals |
| **Q3** | Unproven | Conversions = 0 AND cost between 0.5×–1× target CPA |
| **Q4** | Losing | Cost ≥ 1× target CPA with 0 conversions, OR CPA ≥ 1.5× target, OR ROAS ≤ 0.7× target |
| **Q5** | Invalid | Query contains: free, cheap, diy, how to, job, salary, course, pdf, meaning, used, repair |

**Q5 terms are eliminated regardless of cost.** Calculate spend share per tier.

**Intent signal patterns** (for classifying Q1 vs Q5 when ambiguous):

- **High intent (→ Q1):** buy, purchase, order, pricing, price, cost, near me, delivery, shipping, discount, coupon, subscribe, sign up, get started, demo, trial, quote, consultation, book, schedule
- **Mid intent (→ Q2 / Q3):** best, top, review, vs, versus, compare, alternative, recommendation, worth it
- **Low intent (→ Q4 / Q5):** what is, how to, tutorial, guide, learn, definition, meaning, example
- **Negative intent (→ Q5):** free, diy, repair, fix, used, second hand, jobs, career, salary, template, sample

## Step 2: Classify Auction Pressure

### Rank Pressure

| Rank Pressure = HIGH if **any** true |
|---|
| IS Lost (Rank) ≥ 30% |
| Search IS ≤ 50% AND IS Lost (Rank) > IS Lost (Budget) |
| Top of Page Rate ≤ 60% on Q1 queries |
| Absolute Top ≤ 20% on Q1 queries |

| Rank Pressure = LOW if **all** true |
|---|
| IS Lost (Rank) ≤ 20% |
| Top of Page Rate ≥ 70% |
| Absolute Top ≥ 30% on Q1 queries |

### Budget Pressure

| Budget Pressure = HIGH if **all** true |
|---|
| IS Lost (Budget) ≥ 20% |
| IS Lost (Budget) > IS Lost (Rank) |
| CPA ≤ target CPA |
| ≥ 60% of spend from Q1–Q3 |

| Budget Pressure = LOW if **any** true |
|---|
| IS Lost (Budget) < 10% |
| CPA > target CPA |
| Q4 + Q5 spend ≥ 25% |

## Step 3: Decision Matrix

| Query Mix | Rank Pressure | Budget Pressure | Action |
|---|---|---|---|
| Q1-heavy | Low | High | Increase budget 10–20% |
| Q1-heavy | High | Low | Increase bids 5–10% OR improve ad relevance |
| Q1-heavy | High | High | Fix rank first, then budget |
| Q1-heavy | Low | Low | Hold - no changes needed |
| Q2–Q3 heavy | Low | High | Limited budget test |
| Q4+ present | High | Any | Cap or cut spend |
| Q5 present | Any | Any | Negate immediately |

**Search IS alone:** Low Search IS means nothing on its own. Only act when Q1 share ≥ 50% AND IS Lost (Rank or Budget) explains it.

**IS Lost (Rank) logic:**
- If majority Q1, CPA ≤ target, Rank Pressure HIGH → increase bids 5–10% **or** improve ad relevance.
- If CPA > target → do NOT raise bids. Instead tighten queries: promote Q1 to Exact, kill Q3/Q4 leakage.

**IS Lost (Budget) logic:**
- If CPA stable, Q1–Q3 share ≥ 60%, Budget Pressure HIGH → increase budget 10–20%.
- Otherwise fix queries first.

**Top / Absolute Top:**
- Use only on Q1 queries.
- If CVR at Top ≥ 1.15× rest → defend the position.
- No CVR delta = ego tax. Ignore.

## Step 4: CPC Inflation Diagnosis

When CPC is rising WoW:

| Symptom | Root Cause | Action |
|---|---|---|
| CPC ↑ AND IS Lost (Rank) ↑ | Competition increased | Bid increase allowed ONLY if CPA ≤ target |
| CPC ↑ AND new Q4/Q5 terms appearing | Match type leakage | Add negatives, tighten match types |
| CPC ↑ AND CTR ↓ | Ad relevance degraded | Improve ad copy, NOT bids |

**Only competition justifies bid increases.** Cases 2 and 3 require query or creative fixes.

## Step 5: Scaling Prerequisites

Scale ONLY if **all** true:

- Q1 queries isolated (Exact or tight Phrase match)
- CPA stable or improving over 14+ days
- IS Lost (Budget) ≥ 20%
- CPC WoW% increase < CVR WoW% increase (efficiency improving faster than costs)

If CPC rising faster than CVR → false scale signal. Do not increase budget.

## Step 6: Brand & Competitor Logic

**Brand defense** (when brand CPC ↑, Absolute Top ↓, competitor overlap ↑):

- Raise bids only on exact-match brand terms
- Tighten match types on brand campaigns
- Add competitor terms as negatives in non-brand campaigns

**Competitor campaigns:** Default state is OFF. Enable only if CPA ≤ 1.2× target AND Rank Pressure = LOW. Otherwise pause.

## Recommendations to Make

When the user is ready to act, recommend the change in plain terms. The recommendation itself is the deliverable - the user applies the change manually in the Google Ads UI. Examples:

- *"Increase the daily budget on Campaign X from $Y to $Y × 1.15 (15% increase). Hold here for 14 days and re-evaluate."*
- *"Raise the keyword-level max CPC on these 5 Q1 keywords by 5–10%. Keep the other keywords' bids unchanged."*
- *"Add the following terms to the campaign's negative keyword list: free, diy, how to, repair, [...]"*
- *"Create a new ad group containing the top 8 Q1 search terms as Exact-match keywords. Add those same terms as negatives in the original ad group to prevent overlap."*

## Weekly Execution Order (immutable)

1. Prune Q4/Q5 queries
2. Reclassify remaining queries
3. Recompute auction pressure
4. Make bid / budget moves
5. Fix ad relevance

## Prohibitions

- Never increase budget to fix low IS without classifying queries first
- Never increase bids with Q4/Q5 terms present
- Never chase Absolute Top without CVR proof
- Never let Broad match dominate auction signals
- Never increase bids AND budget simultaneously

## Output Format

```
### Current State
- Total spend: $X over 30 days
- Query distribution: Q1 (X%), Q2–Q3 (Y%), Q4–Q5 (Z%)
- CPA: $XX (Target: $XX) - [XX% over/under target]
- Rank Pressure: HIGH / LOW
  - IS Lost (Rank): X%
  - Top of Page Rate: X%
  - Absolute Top: X%
- Budget Pressure: HIGH / LOW
  - IS Lost (Budget): X%
  - CPA vs Target: [status]
  - Q1–Q3 spend: X%

### Query Classification Summary
- Q1 (X% of spend): top profitable terms
- Q2–Q3 (Y% of spend): top promising/unproven terms
- Q4–Q5 (Z% of spend): terms to negate; estimated savings $X/day

### CPC Inflation Analysis
- Current CPC: $X
- Prior period CPC: $X
- Change: X% WoW
- Diagnosis: [Case 1 / 2 / 3]
- Root cause: [...]

### Recommended Action (from decision matrix)
Execution order:
  1. ...
  2. ...
  3. ...

Tactical moves:
  - Bid/budget adjustments with entity references
  - Negatives to add (list)
  - Isolation recommendations

### Expected Outcomes (7-day horizon)
- CPA: $XX → $XX
- IS Lost (Rank): X% → X%
- IS Lost (Budget): X% → X%
- Q1 spend share: X% → X%
```

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Last 30 days, filtered to ENABLED Search campaigns: (1) campaign-level metrics (cost, conversions, conv. value, clicks, impressions, search IS, IS Lost Rank/Budget, Top of Page Rate, Abs Top Rate, avg CPC) via the `campaign` resource; (2) search-term performance via `search_term_view` (top 200 by cost); (3) keyword-level via `keyword_view`; (4) CPC trend by segmenting last 7d vs prior 7d. |
| CSV | **Requires three separate exports** from the Google Ads UI: (1) Campaign Performance report with auction metrics columns enabled; (2) Search Terms report (top 200 by cost); (3) Keywords report. Plus a week-over-week breakdown if not in the campaign export. |
| Screenshot / copy-paste | Workable only for a quick sanity-check on one campaign. The Q1–Q5 classification needs the full search-term list. |

## Tool hints

The Q1–Q5 classification engine needs the **full search-term list, not just top performers**. With MCP, query `search_term_view` and paginate to 200 rows by cost desc. With CSV, the user must run a separate Search Terms export - not the Campaigns export. Auction metrics (Search IS, IS Lost Rank/Budget, Top of Page Rate, Abs Top Rate) are in the Campaigns export but require the auction columns to be enabled - many users miss this and share a CSV with only spend / conversions.

---

# Skill 2: Shopping Campaign Optimization

Product-led optimization: validate feed → classify items → manage structure → scale or cut.

## When to use this skill

- Audit or optimize Shopping / Performance Max for Retail campaigns
- Identify wasted spend at the SKU level
- Decide which products to promote, downgrade, or kill
- Diagnose why Shopping ROAS is below target

## Step 0: Feed Health (BLOCKING)

Before any optimization, verify:

- ≥ 80% of products approved in Merchant Center
- Purchase conversion tracking is active (conversion value > 0 in data)
- Prices and availability are accurate (requires Merchant Center check or manual verification)

**If any check fails → STOP all optimization. Fix the feed first.** Ask the user to confirm Merchant Center status before continuing.

## Data to gather

Lookback window: **14 days** if the account has ≥ 100 purchases/month, otherwise **30 days**.

Ask the user to share - or pull from whatever data source is available:

**Account-level AOV:** total conversion value ÷ total conversions over the lookback window.

**Item-level performance:** Per product: product ID, product title, brand, cost, conversions, conversion value, clicks, impressions. Sort by cost descending (top 200).

**Campaign-level:** Campaign ID, name, status, daily budget, cost, conversions, conversion value, filtered to Shopping campaigns and ENABLED status.

**Search terms:** Search term, cost, clicks, conversions for the Shopping campaigns (top 200 by cost).

**Daily budget utilization:** Daily cost over the last 14 days for each Shopping campaign.

**Ask for target ROAS.** Default: historical 30-day ROAS.

## Step 1: Item-Level Classification

Sort items by cost (highest first). For each item:

| Classification | Condition | Action |
|---|---|---|
| **KILL** | Cost ≥ 2× AOV AND conversions = 0 | Exclude item ID immediately. No learning window. |
| **DOWNGRADE** | ROAS < 0.7× target AND cost ≥ 0.5× AOV | Lower bid or exclude. Spending but underperforming. |
| **PROMOTE** | Conversions ≥ 2 AND ROAS ≥ target | Isolate into its own product group / campaign to protect budget. |

Items not matching any rule: monitor, no action needed.

## Step 2: Product Group Structure

- Maximum 3 product groups per campaign.
- Split ONLY when economics differ (different margins, price bands, seasonal risk).
- If groups don't have meaningfully different ROAS targets → consolidate.

## Step 3: Search Term Negatives

Add negatives ONLY for wrong-intent terms:

- **Price objection:** free, cheap, budget, discount code, coupon
- **DIY / repair:** diy, repair, fix, how to, tutorial
- **Used / second-hand:** used, second hand, refurbished, pre-owned
- **Products not in feed:** compare search terms to product titles; negate terms for products you don't sell
- **Irrelevant attributes:** colors / sizes not offered

**Do NOT negate high-intent commercial terms even if they haven't converted yet.**

## Step 4: Budget & Bid Decisions

### SCALE (increase budget 10–20%)

**All** must be true:

- Campaign ROAS ≥ target
- Budget utilization ≥ 90% on 10+ of the last 14 days
- Top 20% of SKUs by conversions account for ≥ 60% of spend (winners are getting the budget)

### CUT / CAP (reduce budget or exclude SKUs)

**Any** true:

- Campaign ROAS < target
- SKUs with ROAS < 0.7× target receiving increasing spend share WoW

→ Reduce budget OR exclude underperforming SKUs first, then reassess.

## Step 5: Device & Location (last)

Only analyze if segment spend ≥ 2× AOV (enough data to judge).

- Exclude device/location ONLY if ROAS ≤ 0.6× account average AND no operational explanation (e.g. mobile site is broken).
- Check for technical issues before excluding (site speed, checkout flow).

## Step 6: Campaign Kill Conditions

Pause the Shopping campaign if:

- ROAS < 0.6× target after total spend ≥ 2× AOV
- Shopping ROAS consistently worse than Search ROAS over 30+ days

## Prohibitions

- Never optimize by CTR alone - Shopping is ROAS-driven.
- Never let cheap, low-converting SKUs dominate spend.
- Never scale without confirming winners are getting the budget.

## Output Format

```
### Feed Health
- Merchant Center approval rate: X%
- Conversion tracking: [active / inactive]
- Status: [OK to proceed / blocked]

### Item Classification Summary
- KILL: N items, $X estimated monthly savings
- DOWNGRADE: N items, $X estimated savings
- PROMOTE: N items, suggested isolation strategy
- Monitor: N items

### Search Term Negatives
- Recommended additions: [list]
- Estimated savings: $X/day

### Budget Recommendation
- Current: $X/day
- Recommended: $X/day (+/- X%)
- Rationale: [SCALE / CUT / HOLD with reasons]

### Expected 7-day ROAS Impact
- Current ROAS: X.XX (Target: X.XX)
- Projected ROAS after kills/negatives: X.XX
```

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | (1) Account-level AOV (total conv. value / total conversions over lookback). (2) Item-level performance via `shopping_performance_view` (top 200 by cost). (3) Campaign-level Shopping metrics filtered to ENABLED. (4) Search terms for Shopping campaigns. (5) Daily cost segmentation for last 14 days via `segments.date`. (6) Merchant Center approval rate - **manual user check**, not in MCP. |
| CSV | Three separate exports: (1) Campaign Performance for Shopping campaigns; (2) **Products report** for item-level performance; (3) Search Terms report for Shopping. Plus a daily-segmented export for budget utilization. Merchant Center approval rate is a manual check the user must do in Merchant Center. |
| Screenshot / copy-paste | Not workable for full Shopping audit - too many entity-level joins required. |

## Tool hints

The feed-health gate (Step 0) **blocks all optimization** if Merchant Center approval rate is unknown. This is never in MCP or CSV - always ask the user to confirm. The Products report at item level is the second most-missed export (after PMax assets) - many users share a Campaigns export and ask for product-level recommendations that can't be made from it.

---

# Skill 3: Performance Max (PMax) Optimization

PMax is machine-learning-led: multi-channel (Search, Display, YouTube, Gmail, Discover), asset-driven, with limited granular control. It requires maturity before optimization.

## When to use this skill

- Audit or optimize an existing PMax campaign
- Decide whether PMax is worth keeping vs. shifting spend to Search/Shopping
- Plan scaling for a profitable PMax campaign
- Diagnose why PMax ROAS is below Search ROAS

## Maturity Gate (BLOCKING)

Campaign must meet **one** of:

- Age ≥ 30 days (ideally 60)
- Total conversions ≥ 50

**If neither met → WAIT. Do not optimize.** ML has not stabilized.

**Exception:** if the campaign is clearly burning money (ROAS < 0.3× target after spend ≥ 3× AOV), recommend pausing - even pre-maturity.

## Data to gather

Ask the user to share - or pull from whatever data source is available - over the **last 30 days** (use 60 days for trend analysis):

**Campaign performance:** Campaign ID, name, status, start date, impressions, clicks, CTR, cost, conversions, conversion value. Filter to PMax campaigns.

**Asset group details:** Campaign ID, asset group ID, name, status.

**Asset performance labels:** For each asset (image, video, headline, description) within each asset group, the performance label: BEST / GOOD / LOW / PENDING / UNSPECIFIED.

**Device performance:** Cost, conversions, conversion value, clicks, impressions per device (mobile / desktop / tablet) for each PMax campaign.

**Geographic performance:** Cost, conversions, conversion value per location (top 200 by cost).

**Time series:** Daily cost, conversions, conversion value over the last 60 days for trend analysis.

**Search term insights (PMax-aggregated):** Category labels, clicks, impressions, conversions, cost. Note: PMax provides aggregated categories only, not individual terms.

**PMax vs Search comparison:** Cost, conversions, conversion value for both PMax AND Search campaigns over the same window.

**Ask for:** Target ROAS, target CPA, initial budget (for scaling caps), priority locations.

## Phase 1 - Evaluate Performance

### Step 1: PMax vs Search Comparison

Calculate ROAS for each channel type and compare:

| PMax ROAS Ratio | Assessment | Action |
|---|---|---|
| < 0.5× Search ROAS | Poor | Monitor closely; consider pausing if not improving |
| 0.5 – 0.9× Search ROAS | Below par | Optimize assets and negatives before any scaling |
| ≥ 0.9× Search ROAS | Healthy | Proceed with optimization; eligible for scaling |
| > Search ROAS | Outperforming | Prioritize scaling |

**Also check for brand cannibalization:** review PMax search term categories. If brand terms appear, correlate PMax conversion growth with Brand Search impression share decline over the same window. Flag inflated PMax ROAS.

### Step 2: Asset Performance Analysis

Group by asset type (images, videos, headlines, descriptions). For each asset:

| Label | Action |
|---|---|
| **BEST** | Create variations with similar style/messaging. This is working - make more like it. |
| **GOOD** | Keep, monitor. No changes needed. |
| **LOW** | Remove from asset group. Replace with variations of BEST performers. |
| **PENDING / UNSPECIFIED** | Wait for more data (typically 14+ days). |

### Step 3: Device & Location

**Device:**

| Device CPA vs Account | Action |
|---|---|
| > 1.5× account CPA | Check site/funnel usability on that device first. If no issues → consider -50% bid adjustment or exclusion. |
| > 2× account CPA | Strong candidate for exclusion after confirming no technical issues. |
| CVR < 0.5× account CVR | Check landing page experience on that device. |

**Location:**

| Location CPA vs Account | Action |
|---|---|
| > 1.5× account CPA | Consider excluding |
| > 2× account CPA | Exclude |
| Spend but 0 conversions | Wait for more data, OR exclude if spend ≥ 2× AOV |

**Always check for technical/usability issues before excluding a device or location.**

### Insights Tab Review (qualitative)

If the user has access to the PMax Insights tab in the Google Ads UI:

- **Audience Insights:** which audience types are getting majority of clicks (cannot see conversion performance directly - infer by click volume).
- **Asset Insights:** overlap of assets and audiences. Use this to plan new asset groups for high-performing segments.

## Phase 2 - Scale (only if Phase 1 confirms profitability)

### Scaling Prerequisites

**All** must be true before scaling:

- Campaign profitable for 14–30 consecutive days
- ROAS ≥ target (default 300% if not specified)
- CPA ≤ target
- Performance trends stable or improving WoW

### Budget Scaling

Increase daily budget by **20–50%** every 14–30 days.

| Scenario | Action |
|---|---|
| Profitable 14+ days, trends stable | Increase 20–50% |
| Post-scaling CPA > 1.2× target | PAUSE scaling, optimize assets/negatives, reassess after 30 days |
| Post-scaling ROAS < 0.8× target | PAUSE scaling, optimize, reassess after 30 days |
| Consistently profitable 90+ days | Can exceed 2–3× initial budget cap |

**Hard cap:** do not exceed 2–3× initial monthly budget until 90+ days of consistent profitability.

### Location Expansion

- Only after core locations profitable for 30+ days.
- Expand to similar / adjacent markets.
- Create separate asset groups for new locations if targeting differs.
- Monitor new locations independently for 30 days before further expansion.

### Audience Expansion

- Start with **Observation** mode for new audience signals.
- Monitor performance for 14+ days.
- Switch to **Targeting** mode only if performance holds.
- Do NOT force audience preferences without data.

### Asset Expansion

Based on BEST-performing assets from evaluation:

| Asset Type | Expansion Rule |
|---|---|
| Images | Add 5–10 total, similar style to BEST, different angles/contexts |
| Headlines | Variations of BEST - same theme, different wording. Test different CTAs. |
| Descriptions | Variations of BEST - same value props, different framing |
| Videos | Test 30-second formats if shorter videos are BEST |
| New asset groups | For high-performing audience segments identified in Insights |

## PMax Limitations (do NOT recommend these)

- No keyword targeting
- No budget per asset group
- No placement control
- No demographic control
- No channel-level budget control
- Search term data is aggregated categories only, not individual terms

## Prohibitions

- Never optimize before 30 days OR 50 conversions (unless burning money)
- Never scale before 14 days of profitability
- Never increase budget > 50% in one step
- Never scale beyond 2–3× initial budget before 90 days of profitability
- Never continue scaling if CPA > 1.2× target OR ROAS < 0.8× target
- Never remove BEST or GOOD performing assets
- Never force device/location exclusions without checking for technical issues first

## Output Format

```
### Current State
- Campaign age: X days (Ready: Yes/No)
- Total conversions: X (Minimum met: Yes/No)
- Status: [Ready for optimization / Still stabilizing]

### Performance vs Search
- PMax ROAS: X.XX (Target: X.XX)
- Search ROAS: X.XX
- Ratio: X.XX (PMax is XX% of Search performance)
- Assessment: [Outperforming / Acceptable / Underperforming / Poor]

### Asset Group Analysis
- BEST assets: [list with action - create variations]
- GOOD assets: [list - keep, monitor]
- LOW assets: [list - remove and replace]
- PENDING assets: [list - wait]

### Device Performance
- Per-device CPA vs account; flagged exclusion candidates

### Location Performance
- Top locations by spend; flagged exclusion candidates

### Scaling Recommendation
- Days profitable: X
- Recommendation: [SCALE / OPTIMIZE FIRST / PAUSE]
- If SCALE: current $X/day → recommended $X/day (+X%); cap at $X/month
- If OPTIMIZE FIRST: reason and required fixes
- If PAUSE: reason

### Expansion Opportunities (if applicable)
- Locations, audiences, asset variations to test

### Expected Outcomes (30-day horizon)
- CPA: $X → $X
- ROAS: X.XX → X.XX
- Monitoring priorities
```

## Minimum required data (by source)

PMax has the **largest data-source gap** of any skill. Many users share a campaign-level export and ask for asset and search-term recommendations that simply cannot be made from it.

| Source | What you need |
|---|---|
| MCP (with GAQL) | (1) Campaign performance over 30d (60d for trend) via `campaign`; (2) **Asset group structure** via `asset_group`; (3) **Asset performance labels** via GAQL on `asset_group_asset` with `performance_label` field; (4) **Search term insights** via GAQL on `campaign_search_term_insight`; (5) Device segment via `segments.device`; (6) Geographic segment via `geographic_view`; (7) PMax vs Search comparison - pull both with same date range. |
| CSV | **Requires four to five separate exports** that users frequently miss: (a) Campaign Performance for PMax campaigns; (b) **Asset Report from the PMax campaign page** (gives BEST / GOOD / LOW labels); (c) **Search Terms Insights from the PMax campaign page** (gives aggregated categories - NOT the regular Search Terms report); (d) Devices segment; (e) Locations segment. Plus a Search-campaigns export with same window for the PMax vs Search ROAS comparison. |
| Screenshot / copy-paste | Not workable for full PMax audit. Possibly workable for a single yes/no question (e.g. "is my PMax mature enough to optimize?"). |

**Before running this skill on CSV data**, explicitly check whether the user has the Asset Report and Search Term Insights. If they don't, ask them to pull both before continuing - or fall back to the MCP path.

## Tool hints

PMax's "limitations" cut both ways: the platform exposes less, but Google Ads API still has the resources Claude needs. The two resources that turn an incomplete PMax audit into a complete one are `asset_group_asset` (for performance labels) and `campaign_search_term_insight` (for the aggregated category data). Both require GAQL. If the connected MCP supports arbitrary GAQL (e.g. GoMarble's `google_ads_run_gaql`), use it. The CSV alternative - running two separate UI reports from the PMax campaign page - is the most common point of friction in PMax audits and worth flagging early in the conversation.

---

# Skill 4: Keyword Research

When a decision depends on search volume, CPC (top-of-page bid), or competition, real keyword data is required. **Without that data, do not estimate volume or CPC - say insufficient data and ask the user to share it.**

## When to use this skill

| Trigger | Action |
|---|---|
| "Do keyword research" / "Suggest keywords" / "Find buyer keywords" | Discover new keyword ideas + validate |
| "Are these keywords good?" / "Which should I keep?" | Validate against volume + CPC |
| "Which keyword is better?" / "Prioritize these" | Compare metrics across candidates |
| "Create a new search campaign" / "Launch Google Search ads" | Research → validate BEFORE proposing structure |
| "Expand to a new country" / "International Google Ads" | Pull metrics with the new geo + language |
| "Can we scale?" / "What CPCs should we expect?" | Pull top-of-page bid forecasts |

## When NOT to use this skill

Keyword Planner data is NOT required for:

- Creative work (RSA headlines, descriptions, ad strength)
- Structure work (match type explanations, campaign naming, account audits)
- Post-performance analysis (CPA / ROAS analysis, search-term-report mining for existing campaigns)

## Data to gather

For each candidate keyword, the user needs to provide (or pull from any keyword-research tool - Keyword Planner, third-party tools, etc.):

- **Search volume** (monthly searches in the target geo + language)
- **Top-of-page bid range** (Low / Medium / High, or explicit min–max CPC)
- **Competition** (Low / Medium / High - used only as a tie-breaker)

If targeting a specific geography or language, confirm the metrics are scoped to that region.

## Step 1: Generate Candidate Keywords

Generate using buyer-intent patterns only.

**Approved patterns:**

- [service] + agency
- [service] + management
- [service] + pricing
- [service] + cost
- [service] + consultant
- [software] + for + [industry]
- [competitor] + alternative

**Disallowed patterns:**

- how to
- what is
- guide
- tips
- tutorial
- free
- examples

## Step 2: Evaluate Each Keyword

| Criterion | Rule |
|---|---|
| **Intent** | Buyer intent must be explicit in the keyword text. Unclear → REJECT. |
| **Search Volume** | Volume < 50 → REJECT. Volume ≥ 50 → PASS. |
| **Top-of-Page Bid** | High → STRONG APPROVE. Medium → APPROVE. Low → APPROVE only if intent is very strong. Zero / Missing → REJECT. |
| **Competition** | Tie-breaker only. Never reject solely due to high competition. |

## Step 3: Final Decision Rule

```
IF
  buyer intent = YES
  AND volume ≥ 50
  AND top-of-page bid ≠ Low / Zero
THEN
  APPROVE
ELSE
  REJECT
```

## Step 4: Match Type Assignment

For approved keywords only:

| Match Type | When to Use |
|---|---|
| Exact | Very strong intent, specific wording |
| Phrase | Core scalable keywords |
| Broad | Do NOT suggest by default |

## Output Format (per keyword)

```
Keyword:
Match Type:
Volume:
Top of Page Bid:
Competition:
Decision: APPROVE / REJECT
Reason:
```

**Example:**

```
Keyword: google ads agency for ecommerce
Match Type: Phrase
Volume: 90
Top of Page Bid: High
Competition: Medium
Decision: APPROVE
Reason: Clear buyer intent + active advertiser bidding
```

## Core Principles

1. Intent > Volume (always)
2. Top-of-page bid = strongest commercial signal
3. Informational keywords = auto-reject
4. Fewer correct keywords > many random ones

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Per candidate keyword (scoped to target geo + language): monthly search volume, top-of-page bid range (low / high), competition level. Via tools like `google_ads_keyword_discover` (seed → ideas) and `google_ads_keyword_metrics` (validate specific keywords). |
| CSV | A Keyword Planner export covering the target geo + language. Standard Planner CSV columns map directly: "Avg. monthly searches" → volume; "Top of page bid (low range)" / "(high range)" → top-of-page bid; "Competition" → competition. |
| Screenshot / copy-paste | Workable if the user pastes the Planner table directly with all three signals. |

## Tool hints

This skill cannot run on guesses - never estimate volume or CPC from training data. If MCP keyword tools are available, they're the cleanest source. If only a CSV export is available, confirm it's scoped to the target geo and language before applying the decision rule (a US-scoped Planner export gives the wrong CPCs for a UK launch).

---

# Cross-Cutting Notes

## How to handle missing data

If the user can't provide the data a skill needs, do **not** invent values. State explicitly:

> *"To answer this properly I need [specific metrics]. You can pull these from [Google Ads UI report / a CSV export / a connected data tool]. Without them I can outline the framework but not give a recommendation."*

## How to handle change requests

When the user asks Claude to change something in their account (e.g. "raise the bid", "pause the campaign"):

1. Run the relevant analysis skill to validate the change is justified.
2. Apply the guardrails (especially scaling caps and the "no simultaneous bid + budget" rule).
3. **Recommend the change in plain language** with the exact entity, the current value, the proposed value, the rationale, and what to monitor afterwards.

Claude does not execute changes on the user's ad account. These skills are read-and-recommend only - the user applies recommendations manually in the Google Ads UI.

## How to handle multiple campaign types in one account

If the user's account has Search + Shopping + PMax all active, ask which to focus on first. Don't analyze all three at once unless explicitly requested - it dilutes the recommendation quality.

## How to handle account-type ambiguity

Always classify the account before applying KPIs:

1. Check the conversion actions present (purchase / lead / store visit / call).
2. Check whether conversion value is populated.
3. If unclear, ask the user.

If the account is footfall / awareness / local-service, **replace CPA/ROAS in headline metrics** with: cost per footfall action, cost per call, cost per direction, CPM, reach, frequency. State explicitly that purchase-derived CPA/ROAS do not apply.

## What good looks like

- The data source is named first, and every rule that the source cannot support is skipped out loud instead of guessed.
- Each recommendation maps to a control that exists in the Google Ads UI: campaign budget, bid strategy target, pause or enable. No budget is "shifted" between keywords, devices or asset groups.
- Nothing scales until search-term hygiene is done, CPA or ROAS is on target, and conversion volume clears the significance floor.
- Auction pressure is diagnosed as rank or budget before anyone touches bids or budgets.
- When diagnostics are incomplete the output says insufficient data and asks for the missing report, rather than recommending.
