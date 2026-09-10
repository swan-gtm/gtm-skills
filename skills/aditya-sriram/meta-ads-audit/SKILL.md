---
name: meta-ads-audit
title: Meta Ads audit
description: "Use this skill when someone wants a Meta Ads (Facebook and Instagram) account audited or optimized at senior-media-buyer depth: account health, which conversion metric to run on, campaign structure, ad set bid and audience splits, top-performer analysis, or video creative diagnosis. Runs a health check on event match quality and audience segments, sets the primary conversion metric by account type, detects the active campaign structure, applies Pareto analysis to ads, and reads hook rate and hold rate to diagnose creative. Read-and-recommend only: it never changes the account, the user applies every recommendation in Ads Manager. Trigger phrases: Meta Ads audit, creative fatigue, which ads to pause, ad set analysis, hook rate, pixel issues, why did ROAS drop."
category: Ads
tags: [Ads]
---

> Adapted from the GoMarble Paid Media Claude Skills repository (https://github.com/gomarble-ai/gomarble-ai-paid-media-claude-skills) by its author, shared under GoMarble's attribution license. Works with any data source: a connected ads MCP such as GoMarble, CSV exports, screenshots, or pasted tables.

A consolidated set of skills for analyzing and optimizing Meta Ads (Facebook + Instagram) accounts. These skills are **framework-agnostic** - the analytical logic (Pareto, Hook/Hold scenarios, decision matrices, guardrails) applies regardless of where the data comes from.

The skills define **what to know, what data to look for, how to interpret it, and how to recommend action**. They do not depend on any specific tool integration.

> **Read-and-recommend only.** These skills never make changes to the user's Meta Ads account. Claude reads data and produces recommendations in plain language; the user applies the recommended changes themselves in Meta Ads Manager.

---

## Data Sources Are Not All Equal

Data can come from four kinds of sources, but they have **very different completeness**. Some skill rules silently break on weaker sources. Always identify the source first and consult the **Data Source Compatibility Matrix** below before applying any rule.

| Priority | Source | Notes |
|---|---|---|
| 1 (preferred) | A connected MCP server exposing Meta Ads data (e.g. GoMarble, Meta official) | Returns raw API fields, action arrays, full targeting, breakdowns. All rules work. |
| 2 | A CSV/Excel export from Ads Manager | Most rules work, but a few are inert - see compatibility matrix. Several signals require *separate* exports (breakdowns, video metrics, ad-level vs ad-set-level views). |
| 3 (narrow questions only) | Screenshots of report tables | Use only for spot questions on metrics that are visibly captured in the screenshot. Skip deep analysis. |
| 4 (last resort) | Direct copy-paste of metric values | Treat as user-asserted; ask for the underlying export when stakes are real. |

---

## How to Use These Skills

1. **Identify the user's intent** - are they asking for an audit, a performance review, a creative deep-dive, or a targeted question? Use the routing table below.
2. **Run the Data Inventory step (Step 0 below)** - confirm what source is being used and what's actually available before invoking any skill.
3. **Gather the required data** - ask the user to share the data the skill needs in their preferred source. The "Minimum required data" section of each skill lists what's needed.
4. **Apply the analytical framework** - classify, diagnose, decide based on the rules in the relevant skill.
5. **Always check guardrails** before recommending any action.
6. **Output recommendations** in the structured format defined per skill.

If required data is missing or unverifiable, say so explicitly and ask the user for it. **Never fabricate metrics or invent thresholds.**

**Always work from current data** - campaigns change frequently (budget edits, paused ads, new creatives). If the user shared data more than a day or two ago, ask for a fresh pull before making recommendations.

---

## Step 0: Data Inventory (Mandatory Before Any Skill)

Run this once at the start of every analysis. It takes one short turn and prevents wasted effort.

1. **Identify the data source** - MCP / CSV / screenshot / copy-paste. If MCP is connected, use it. If the user attached a file, inspect its columns/fields before asking for more.
2. **State what's available and what's missing** for the requested skill, based on the Data Source Compatibility Matrix below.
3. **For each missing signal, decide:**
   - **Blocking** - cannot proceed without it; ask user to fetch.
   - **Downgrade** - can proceed with caveats; flag as low-confidence in the output.
   - **Skip** - rule doesn't apply to this source (e.g. Purchase De-Duplication on CSV); note it and move on.
4. **Confirm the date range** in the data matches what the skill expects (typically 30 days; 7d for ad set analysis; 60–90d for trend or Hold Rate baseline).

Output one short paragraph before applying the skill. Example:
> *"Using your GoMarble MCP. I have ad-level insights with `actions` and `purchase_roas` for the last 30 days - sufficient for Performance Analysis (Skill 5). The EMQ check (Skill 1) requires you to look in Events Manager directly; I'll flag it as a manual step."*

---

## Data Source Compatibility Matrix

Use to plan which signals you can get from which source before running any skill.

| Signal | MCP (GoMarble / Meta / etc.) | CSV (Ads Manager export) | Screenshot |
|---|---|---|---|
| Spend, impressions, clicks, CTR, CPM, reach, frequency | ✅ direct | ✅ default columns | ✅ if shown |
| Purchase count (deduplicated) | ✅ via `actions` array - apply Purchase De-Duplication rule | ✅ "Purchases" column (Meta already deduplicates - **skip the dedup rule**) | ⚠️ if shown |
| Purchase ROAS | ✅ `purchase_roas` field | ✅ "Purchase ROAS" column (must be enabled) | ⚠️ |
| Revenue / conversion value | ✅ `action_values` | ✅ "Purchases Conversion Value" column | ⚠️ |
| Video Plays | ✅ `video_play_actions` | ✅ "Video Plays" column | ❌ rarely shown |
| 3-Second Video Plays | ✅ via `actions` (`video_view` action) | ✅ "3-Second Video Plays" column (already pre-computed - **skip the action-name distinction**) | ❌ rarely shown |
| ThruPlays | ✅ via `actions` | ✅ "ThruPlays" column | ❌ rarely shown |
| Hook Rate / Hold Rate | ❌ must compute from the above | ❌ must compute from the above | ❌ |
| Promoted object / `custom_event_type` | ✅ from ad set object | ❌ NOT in default CSV exports - **ask user to confirm per ad set / campaign** | ❌ |
| Campaign objective, ad set bid strategy, bid amount | ✅ direct | ⚠️ requires "Bid Strategy" + "Bid Amount" columns enabled (often not default) | ⚠️ |
| Full targeting object (audiences, interests, custom audiences) | ✅ via ad set object | ❌ NOT in CSV - **must be described by user or pulled via MCP** | ⚠️ if visible |
| EMQ Score | ❌ not in standard insights APIs - **manual check in Events Manager** | ❌ same | ❌ same |
| Audience Segment breakdown (New / Engaged / Existing) | ✅ insights with `breakdowns=['user_segment_key']` | ⚠️ requires a *separate* breakdown export | ❌ |
| Placement breakdown (Feed / Stories / Reels / etc.) | ✅ `breakdowns=['publisher_platform','platform_position']` | ⚠️ requires separate breakdown export | ❌ |
| Age / gender breakdown | ✅ `breakdowns=['age','gender']` | ⚠️ separate export | ❌ |
| Geographic / device breakdown | ✅ via breakdowns | ⚠️ separate export | ❌ |
| Ad creative content (video file, image, copy) | ✅ via creative endpoint (e.g. `facebook_get_ad_creative_details`) | ❌ never in CSV - **must be shared separately** | ⚠️ |
| Comments / sentiment | ❌ requires manual check in Ads Manager or the Page | ❌ same | ⚠️ if shown |
| Attribution window settings | ✅ via ad set `attribution_spec` | ⚠️ requires "Attribution Setting" column | ❌ |
| Daily time-series (for trend / fatigue detection) | ✅ insights with `time_increment=1` | ⚠️ requires day-by-day export | ❌ |
| 3rd-party tracker config (Profitmetrics / Triple Whale etc.) | ✅ inferred from `custom_event_type` on PURCHASE campaign objective | ❌ **must ask user explicitly** - see upgraded check in Skill 5 | ❌ |

✅ = available and reliable. ⚠️ = available but requires extra export / setup. ❌ = not available from this source.

---

## Meta CSV Column Translation

When the source is a CSV export from Ads Manager, the column names rarely match the API field names used throughout the skills. Use this table to translate. (Column names vary slightly by language and export template - match by meaning, not by exact string.)

| Skill / API reference | Typical Ads Manager CSV column |
|---|---|
| `spend` | "Amount spent (USD)" / "Amount Spent" / "Spend" |
| `impressions` | "Impressions" |
| `reach` | "Reach" |
| `frequency` | "Frequency" |
| `cpm` | "CPM (cost per 1,000 impressions)" |
| `ctr` | "CTR (all)" or "CTR (link click-through rate)" |
| `clicks` | "Link clicks" or "Clicks (all)" |
| `purchase` / `omni_purchase` (deduped) | "Purchases" (Meta has already deduplicated) |
| `purchase_roas` | "Purchase ROAS (return on ad spend)" |
| Revenue (conversion value) | "Purchases Conversion Value" |
| `video_view` action (3-second views) | "3-Second Video Plays" (already pre-computed) |
| ThruPlays | "ThruPlays" |
| Video Plays | "Video Plays" |
| Leads | "Leads" or "On-Facebook Leads" + "Off-Facebook Leads" - confirm with user which is the conversion event |
| Campaign objective | "Campaign Objective" (often not in default export - must enable) |
| Bid strategy | "Bid Strategy" (often not in default export - must enable) |
| Daily / lifetime budget | "Budget" or "Campaign Budget" / "Ad Set Budget" |
| Attribution window | "Attribution Setting" |
| `custom_event_type` / promoted_object | ❌ NOT in CSV - ask user to confirm |

**Rule for Claude:** if a CSV column maps to a pre-computed metric (Purchases, 3-Second Video Plays, ThruPlays), use it directly and skip the upstream dedup / action-array rules. Those rules exist to clean raw API data.

---

## Routing - Which Skill to Use

| User asks about | Use Skill |
|---|---|
| "Audit my account" / full optimization request | Run **Initial Health Check** → **Conversion Metric Focus** → **Performance Analysis** → **Creative Analysis** in that order |
| Pixel / tracking setup, audience segments setup | **Initial Health Check** |
| "What's my account type?" / which KPI to use | **Conversion Metric Focus** |
| Campaign structure, primary vs testing, bid splits, audience splits | **Campaign Structure Analysis** |
| Ad set targeting, budget utilization, audience comparison | **Ad Set Analysis** |
| Top performers, Pareto analysis, which ads to keep/pause | **Performance Analysis** |
| Hook rate, hold rate, video diagnostics, why creative isn't working | **Creative Analysis** |
| Change requests (pause campaign, increase budget, change CTA, etc.) | Apply the relevant analysis skill first, then **recommend** the change in plain language with rationale. Claude does not execute changes on the user's ad account - the user applies recommendations manually in Ads Manager. |

If the user's intent is ambiguous, ask which to focus on first.

---

## Universal Guardrails - Apply Before Every Recommendation

**Read these before generating any recommendation.**

### Budget Reallocation Prohibition

You **cannot** allocate, shift, increase, reduce, or scale budget for: individual ads (only campaigns and ad sets have budgets), placements (Meta controls distribution), demographics (age, gender, location breakdowns), user segments (new, existing, engaged).

**Before writing any recommendation, ask:** Does it imply moving money between ads, placements, demographics, or segments? If yes → rewrite using the valid controls below.

**Valid budget controls (only three):**

1. Campaign budget (CBO) or ad set budget (ABO)
2. Bid caps / cost caps
3. Turning ads / ad sets on or off

If a recommendation does not map to one of these three controls, it is not actionable.

**Mandatory rewrites:**

- ❌ "Reallocate $X from [ad A] to [ad B]"
- ✅ "Pause [ad A]. Increase the campaign/ad set budget by 15–20% to give [ad B] more spend opportunity."

- ❌ "Allocate more to [placement / demographic / segment]"
- ✅ "Create a new ad set targeting [dimension] with its own budget, OR exclude underperforming [dimension] via ad set placement settings."

**Rule:** Breakdowns (age, gender, placement, device, region, user segment) show how Meta distributed YOUR budget. They are not levers the user controls. The only way to influence them is creating new ad sets with specific targeting or placement selections.

### Metric Selection by Conversion Type

- **Ecommerce** (purchases / revenue): Use ROAS, revenue, AOV, cost per purchase. Never use ROAS for leadgen.
- **Lead gen** (form submits, leads): Use CPL, cost per qualified lead. Never use ROAS unless offline revenue is mapped.
- **App** (installs, in-app events): Use CPI, cost per activation. Never use ROAS unless in-app revenue tracking is confirmed.
- **Custom conversion**: Use cost per result for that specific event. Do not mix in other conversion types.
- **Unclear**: Ask the user. Do not assume.

### User Segment Targeting Notes

Segments (New Audience, Existing Customers, Engaged Audience) are Meta internal classifications. **They cannot be targeted without custom audiences.**

- Before recommending segmentation, ask: *"Do you have a customer custom audience already built?"*
- If yes → suggest exclusions or separate campaigns using custom audience targeting
- If no → suggest building custom audiences first

### Top Performer Protection (CRITICAL)

**Never recommend pausing the top-converting ad in an ad set.** If Meta's algorithm allocates 60–80% of an ad set's budget to one ad and that ad produces the majority of conversions, that's Meta's optimization working correctly - not a problem.

**Pause decision matrix:**

| Condition | Action |
|---|---|
| Ad has highest conversion volume in ad set | **KEEP** - regardless of budget share |
| Ad has 0 conversions AND spend > 2× ad set CPA target | PAUSE |
| Ad has conversions but CPA > 3× ad set average AND ≥ 3 conversions (statistically significant) | PAUSE |
| Ad has 1–2 conversions with high CPA | WATCH - insufficient data, do not pause yet |
| Ad is < 7 days old | WATCH - let it exit learning phase |

**Self-check before any pause recommendation:** *"Am I about to recommend pausing the ad that drives the most conversions in this ad set?"* If yes → DO NOT recommend pausing. Instead recommend testing new creatives alongside it.

### Methodology Consistency

Once you establish a methodology for evaluating performance in a conversation, do NOT change it unless the user explicitly asks. Changing criteria mid-analysis destroys trust. If you realize your methodology was wrong, say so clearly, explain what you're changing and why, and apply the new methodology consistently from that point.

### STOP Rules

**Pre-check before any recommendation:** Can the user point to the exact Ads Manager UI field that this change maps to? If no → do not recommend.

- No ad-level budget moves
- No demographic or placement budget allocation
- No frequency caps for conversion objectives (Sales, Leads, App install)
- No scaling individual ads (only campaign / ad set level)
- No scaling > 20% at once
- Do not pause ads or ad sets younger than 7 days without enough signals
- Do not increase budget on entities below ROAS/CPL/CPA targets - diagnose first
- Do not call something "scalable" with < 10% revenue share of total account or statistically weak conversion volume
- Minimum signal: 3–5 conversions per ad set per week before performance judgments
- Avoid suggestions that restart the learning phase unless absolutely required
- Do not rely on the first 24–48 hours of data as reliable

### Required Diagnostics Before Action

Before any scale / pause / duplicate / structural recommendation:

1. **User segments**: New vs Existing vs Engaged distribution
2. **Delivery metrics**: CPM, CTR, Reach, Frequency (with spend context)
   - High frequency alone ≠ fatigue
   - Frequency rising + CTR falling over 14+ days = creative fatigue
3. **Engagement relevance**: offer-aligned comments vs spam / backlash
4. **Attribution windows**: 1-day click vs 7-day click vs incremental, if platform / external data mismatch
5. **Confirm results not dominated by warm / small pools** before scaling

### Scaling Guardrails

When recommending a budget increase:

- Only campaign or ad set budget fields (never ad-level)
- Max increase: **20% at once**
- Require before scaling: performance target hit, ad set revenue share ≥ 10% of account, not dominated by 80%+ warm/customer pocket
- If data is noisy or contradictory → say **insufficient data** and shift to a structured testing recommendation instead
- All scaling recommendations must include: deterioration-risk warning + review window + spend cap

### Change-Recommendation Safety Language

When recommending changes the user will apply manually, always include these warnings where relevant:

- **Budget increase > 100%**: warn this is a major increase and ask the user to confirm intent
- **Budget decrease > 50%**: warn this significantly reduces reach and performance
- **Daily vs lifetime budget**: always distinguish which one you're talking about
- **Pausing**: traffic and spending stop immediately
- **Deletion**: permanent, cannot be undone - require explicit confirmation
- **Archiving**: reversible - can be unarchived back to PAUSED
- **Bid strategy change**: resets the learning phase - always warn
- **Targeting change**: if non-trivial, may reset learning phase

---

## Metric Glossary - Canonical Definitions

Used across every skill below.

### Currency Note

Meta API budget values are typically in **cents** (integer). $50 = 5000 cents. If you see raw integer budget values from an API or export, divide by 100 to display. **Confirm account currency before showing monetary values - never assume USD.**

### Direct Metrics

| Metric | Notes |
|---|---|
| Spend | Total spend in account currency |
| CPM | Cost per 1,000 impressions |
| CTR | Click-through rate (decimal or %) |
| Impressions | |
| Clicks | |
| Reach | Unique users reached |
| Frequency | Average impressions per user |
| Video Plays | Initial impressions of the video |
| 3-Second Views | "video_view" actions - hook engagement (this is inside the `actions` array, not a separate field) |
| ThruPlays | 15-second or completed video watches |
| Purchases | Use ONE purchase action type only - see Purchase De-Duplication below |
| Leads | Lead events |
| Revenue | Conversion value for purchases |
| Purchase ROAS | Returned directly by Meta |

### Calculated Metrics

| Metric | Formula |
|---|---|
| Hook Rate | (3-second views / video plays) × 100 - **API/MCP source: use the `video_view` action inside the actions array, NOT `video_p25_watched_actions`.** **CSV source: use the "3-Second Video Plays" column directly - it's already pre-computed; the action-name distinction does not apply.** |
| Hold Rate | (ThruPlays / 3-second views) × 100 - for CSV, use "ThruPlays" ÷ "3-Second Video Plays" columns directly. |
| Cost Per Purchase | spend / purchases |
| Cost Per Lead (CPL) | spend / leads |
| Cost Per Result (CPR) | spend / specific custom-event count |
| Conversion Rate (CVR) | conversions / clicks × 100 |
| Budget Utilization | spend / (daily budget × days in period) |
| Campaign Spend Share | entity spend / parent total spend (require ≥ 25% before comparing ad sets) |
| Pareto Set | Sort ads by spend desc; keep ads where cumulative spend ≤ 90% |

### Purchase De-Duplication (CRITICAL - API/MCP only)

**This rule applies only when the source is an MCP / API that returns the raw `actions` array.** If the source is a CSV export, the "Purchases" column has already been deduplicated by Meta - **skip this rule entirely and use the column directly.**

When working with raw API data: Meta returns overlapping purchase action types in the `actions` array: `omni_purchase`, `purchase`, `offsite_conversion.fb_pixel_purchase`, `onsite_web_purchase`, `web_in_store_purchase`, `app_custom_event.fb_mobile_purchase`.

**Rule:** Use ONLY ONE. Check `omni_purchase` first; if absent, fall back to `purchase`. **Never sum multiple types** - this double-counts revenue and inflates ROAS.

**Source check before applying:**
- MCP returning an `actions` array → apply the rule.
- CSV with a "Purchases" column → skip the rule; the column is already deduplicated.
- Screenshot showing a "Purchases" number → skip the rule; trust the figure but flag the source.

### Account Type → Primary Conversion Metric (PCM)

Read the **promoted object / conversion event** from each ad set. **Never infer from campaign or ad set names** - names frequently don't match the actual config.

| Custom Event Type | Account Type | PCM |
|---|---|---|
| PURCHASE | Ecommerce | Purchase ROAS |
| LEAD | Lead generation | Cost per Lead |
| COMPLETE_REGISTRATION | Registration | Cost per Registration |
| OTHER (custom event) | Custom conversion | Cost per Result for that specific event |

If the promoted object is missing → **ask the user**. Never assume.

**Mixed accounts**: group ad sets by their custom event type. Each group gets its own PCM. Do not mix conversion types across groups.

### Special Case: COMPLETE_REGISTRATION on PURCHASE Objective (Cross-Source Safety Check)

If an ad set has campaign objective `OUTCOME_SALES` (or legacy `CONVERSIONS` / `PRODUCT_CATALOG_SALES`) AND the optimization event is `COMPLETE_REGISTRATION`, this is **almost always a 3rd-party purchase tracker** (Profitmetrics, Cosmise, Triple Whale, Northbeam) posting purchase events through Meta's CompleteRegistration endpoint - **not a misconfiguration**.

Especially common on:
- Nordic-currency accounts (DKK / SEK / NOK / EUR)
- Shopify + Profitmetrics stacks

**This is the highest-stakes safety check in the skill - getting it wrong can kill a working campaign.**

#### Source-aware detection

| Source | How to detect |
|---|---|
| MCP / API | Read `campaign.objective` + `ad_set.promoted_object.custom_event_type` directly. If the pair matches the trigger, apply the check below. |
| CSV with "Campaign Objective" + "Performance Goal" / "Optimization Goal" columns | Match by column values. If columns are missing, fall through to the manual check. |
| CSV without those columns, screenshot, or copy-paste | **Cannot detect automatically.** Use the proactive question below before any pause / scale / budget-cut recommendation on Nordic-currency or Shopify accounts. |

#### Proactive question (use whenever auto-detection isn't possible OR the account profile fits)

> *"Before I make recommendations on this account: do you use a 3rd-party purchase tracker like Profitmetrics, Triple Whale, Northbeam, or Cosmise? If yes, the conversion event reported as 'Registrations' or `COMPLETE_REGISTRATION` is real purchase volume and the campaign is correctly configured - I should treat it as purchase data."*

Ask this **once per account / conversation**, store the answer, and apply it to all subsequent recommendations.

#### Action rules (apply after detection or confirmation)

Before any optimization recommendation on such ad sets:

1. State the ambiguity in your response, naming the 3rd-party tracker explicitly.
2. **Do NOT** recommend any of the following without explicit user confirmation first:
   - "Change the optimization event to PURCHASE"
   - "Verify and switch the optimization goal"
   - Pause / archive / delete the ad set or campaign
   - Reduce budget by more than 20%

Only after confirmation may you treat the events as registrations (and recommend an optimization-event change) OR as real purchases (apply ROAS / CPA against revenue).

### Performance Benchmarks

| Metric | Good | Average | Poor |
|---|---|---|---|
| Hook Rate | ≥ 40% | 26–39% | < 25% |
| Hold Rate | > Account Avg + 25% | ≈ Account Avg | < Account Avg |
| CTR | ≥ 1.25% | 0.65 – 1.24% | < 0.65% |
| CPM variance vs Pareto avg | ≤ 20% | 20 – 60% | > 60% |
| PCM variance vs Pareto avg | Above avg | ± 20% | > 30% below |
| Budget utilization | ≥ 85% | - | < 85% |
| Min ad-set spend share for comparison | ≥ 25% of campaign | - | - |

For Hold Rate, compute the account average from a 90-day account-level pull (video fields aggregated) before applying the comparison.

### Statistical Significance Floors

| Decision | Minimum signal |
|---|---|
| Per-ad-set performance judgment | 3–5 conversions / week |
| Per-segment recommendation (placement, age, device) | ≥ 100 impressions AND ≥ 3 conversions |
| Pause ad on high CPA | ≥ 3 conversions if non-zero, OR spend ≥ 2× ad-set CPA target if zero |
| Ad set learning-phase exit | Spend ≥ 2× AOV OR 4× CPA, whichever is higher |

### Diagnostic Signals (used in skills below)

| Signal | Meaning |
|---|---|
| Frequency rising AND CTR falling over 14+ days | Creative fatigue |
| CBO with one ad set holding 80%+ of budget | Algorithm working as intended - do NOT pause the dominant ad set on small-sample noise |
| High frequency alone (no CTR drop) | Not fatigue |
| Cost cap + rising CPM | Either delivery squeeze OR audience saturation - separate before acting |

### Video Funnel

```
Video Plays → Hook Rate → 3-Second Views → Hold Rate → ThruPlays
```

---

## Depth-of-Analysis Framework - Apply on Audits & Optimization Reviews

Apply on: audits, performance reviews, optimization requests, strategy questions, funnel analysis.
Skip for: simple data fetches, campaign listings, single-metric lookups.

### 1. Hierarchical Drill-Down

Never recommend on campaign-level or ad-set-level aggregates alone. Drill one level deeper.

- Asked about a campaign → check ad set performance within it.
- Asked about an ad set → check individual ad performance within it.
- Asked about ads → check creative-level patterns (same creative across multiple ads).

Quantify the contribution: *"Ad Set X accounts for 72% of campaign spend but only 40% of conversions."*

### 2. Objective-Contextual Evaluation

Do not apply universal KPIs. Evaluate each campaign against its actual objective.

**Check first:**

- The ad-set-level optimization event (the actual `custom_event_type` - not the name)
- The campaign objective
- Bid strategy (cost cap, bid cap, lowest cost)

**Apply correct KPIs:**

| Objective | Evaluate on | NOT on |
|---|---|---|
| Sales / Purchase | ROAS, CPA, revenue | Reach, CPM alone |
| Lead gen | CPL, lead volume | ROAS |
| Traffic | CPC, CTR, landing page views | Conversions |
| Video views | Cost per ThruPlay, hook rate | ROAS, CPA |
| Awareness | CPM, reach, frequency | CPA, ROAS |

**Flag bid-strategy issues:** if a cost cap is set 3× above actual CPA, or tROAS target is 0.5× when achieving 3×, the algorithm isn't actually constrained. Call it out.

### 3. Breakdown & Segmentation Analysis

For audits, performance reviews, and optimization work, check **at least 2** of these dimensions. (This overrides the general guidance to only use breakdowns when specifically requested - deep analysis requires segmentation.)

- Placement (Feed vs Stories vs Reels vs Audience Network) - quantify CPA gaps
- Device (mobile vs desktop)
- Age / gender - flag Advantage+ expansion leakage if delivery is going outside the target
- Out-of-target segments consuming budget with poor conversion rates

**Statistical significance check:** do not make segment-level recommendations from < 100 impressions or < 3 conversions in a segment. Call out low-confidence segments explicitly.

### 4. Temporal & Trend Analysis

Never treat the date range as a single static number. Always compare time windows.

- Last 7 days vs previous 7 days
- Identify direction for each key metric: improving, declining, stable
- Flag inflection points: *"CTR started declining on [date], 3 days before CPA started rising"*

**Connect the chain:** frequency rising → CTR falling → CPA rising → this is creative fatigue, not audience exhaustion. Correlate timing across metrics to establish cause, not just observe symptoms.

### 5. Cross-Entity Dependency Mapping

Don't analyze campaigns in isolation. Map the funnel.

- Which campaigns are **prospecting** (broad / lookalike audiences)?
- Which campaigns are **retargeting** (custom audiences, website visitors)?
- Does pausing a prospecting campaign starve the retargeting audience pool?

**How to identify:**

- Prospecting: low frequency, lower CPM, lower CTR, broader audience
- Retargeting: higher frequency, higher CPM, higher CTR, smaller audience
- Check the targeting object on each ad set - presence of custom audiences = retargeting / warm

**Flag dependencies:** *"Pausing Campaign X will reduce the Website Visitors 7-day pool that feeds Campaign Y's retargeting. Expect retargeting CPA to rise within 1–2 weeks."*

### 6. Platform Mechanic Awareness

Explain how Meta's mechanics affect the specific situation - explain the compound interaction, don't just mention the mechanic.

| Signal | Mechanic | Consequence |
|---|---|---|
| Rising frequency + falling CTR | Creative fatigue | CPA will spike - need new creatives, not budget changes |
| CBO + one ad set getting 80% budget | CBO optimization | Usually working as intended. Do not recommend pausing the dominant ad set on small-sample noise. Only intervene if the dominant ad set itself is underperforming on ROAS/CPA. |
| Cost cap + rising CPM | Delivery squeeze or audience shift | Two possible causes - separate before acting: (a) algorithm can't find conversions at the cap (raise cap or loosen targeting); (b) original audience is saturated and delivery is leaking to worse segments. Check frequency, reach trend, and audience size to decide which. |
| Advantage+ audience expansion ON | Targeting leakage | Check breakdowns for out-of-target delivery eating budget |
| Insufficient spend on new ad set | Learning phase | No optimization decisions until the ad set has spent at least **2× AOV or 4× CPA, whichever is higher**. The 50-conversion rule only applies to brand-new accounts with no prior history. |

### 7. Proactive Signal Detection

After answering the user's question, surface 2–3 additional concerns or opportunities they didn't ask about.

Scan for:

- Any entity with frequency > 3 and rising - creative fatigue incoming
- Any ad set spending > 30% of campaign budget with 0 conversions - budget waste
- Any campaign where the top ad has declining CTR over 7+ days - degradation ahead
- Any retargeting audience pool shrinking (declining reach WoW)
- Any metric that looks fine now but the trend predicts problems in 7–14 days

Format: *"Outside your question, I noticed [signal] in [entity] - this suggests [predicted consequence] within [timeframe]."*

### 8. Attribution Rigor

Don't take reported conversion numbers at face value.

Always check:

- What attribution window is active? (1-day click, 7-day click, 1-day view?)
- What share of conversions are view-through vs click-through?
- Is the reported ROAS inflated by view-through on high-impression campaigns?

Flag these situations:

- Retargeting campaign with very high ROAS + mostly view-through conversions → likely over-attributed
- Two campaigns targeting the same audience → conversions may be double-counted
- Advantage+ Shopping targeting existing customers → attributed ROAS includes conversions that would have happened organically

Frame as caveat: *"Before scaling Campaign X based on its reported 4× ROAS, note that [specific attribution concern] means the true incremental ROAS is likely lower."*

---

# Skill 1: Initial Health Check

Validate account setup before any optimization work. **Run this first on any audit.** If checks fail, fixing setup is the top priority - optimization on a broken setup wastes effort.

## When to use this skill

- First step of any account audit
- Before recommending any structural change
- When CPA or ROAS suddenly degrades and tracking issues are plausible

## Step 1: Event Match Quality (EMQ) Score Check

EMQ score is **not directly available via standard insights APIs.** The user must check it manually in Events Manager.

**What to do:**

1. First determine the primary conversion event (from the ad set's optimization goal - covered in Skill 2).
2. Ask the user to manually check: **Events Manager → Data Sources → [Pixel] → Event Match Quality** for that event.
3. Apply the threshold:

| EMQ Score | Status | Action |
|---|---|---|
| ≥ 8.5 | Good | Proceed with analysis |
| < 8.5 | ALERT | Stop and notify the user before optimizing |

**Alert wording when EMQ < 8.5:**

> ⚠️ **CRITICAL:** Your EMQ Score for [Purchase / Lead] is below 8.5.
>
> This means your Pixel is not set up correctly. Likely consequences:
> - Lower conversion rate than possible
> - Higher cost per result than necessary
>
> **Recommendation:** Reach out to a technical expert and fix this as TOP PRIORITY before any other optimization work.

## Step 2: Audience Segments Configuration Check

Audience segment breakdown (New / Engaged / Existing) is **available via insights breakdowns**, but the underlying engaged/existing audience setup is managed in Audience Manager and isn't directly readable via standard APIs.

**What to do:**

1. Pull account-level insights for the last 30 days, broken down by **user segment** (the breakdown that splits New / Engaged / Existing).
2. If the breakdown returns empty or is missing segments, alert the user:

> ⚠️ **Setup needed:** Audience Segments are not configured.
>
> Why this matters: you can see spend breakdown between existing customers and new audience, at campaign / ad set / ad level. Without this, you can't tell where money is actually going.
>
> Note: this does NOT affect targeting - only improves reporting.
>
> Setup guide: Facebook Business Help → Audience Segments configuration.

## Step 3: Decide whether to proceed

| Result | Action |
|---|---|
| EMQ ≥ 8.5 AND segments configured | Proceed to Conversion Metric Focus |
| EMQ < 8.5 | Recommend fixing pixel before any optimization |
| Segments not configured | Flag for setup; can proceed with limited reporting |

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Account-level insights for last 30 days with `breakdowns=['user_segment_key']` to confirm segments are configured. EMQ requires manual user check. |
| CSV | A breakdown export by user segment (if available). EMQ requires manual user check. |
| Screenshot / copy-paste | Not recommended for this skill - too many missing pieces. Ask for at minimum a screenshot of Events Manager → EMQ for the primary event. |

## Tool hints

EMQ Score is **never** in standard insights data - it always requires a manual check in Events Manager → Data Sources → [Pixel]. Audience Segment configuration is observable from any source via the user-segment breakdown; if the breakdown returns empty, segments are unset.

---

# Skill 2: Conversion Metric Focus

Determine account type and set the **Primary Conversion Metric (PCM)** that all subsequent analysis will use. **Run this second on any audit, immediately after the Health Check.**

## When to use this skill

- Once per account, at the start of analysis
- Whenever account-level KPIs are ambiguous
- When new campaigns are added that may use a different conversion event

## Data to gather

For each active campaign in the account:

- Campaign objective (e.g., OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_TRAFFIC)
- The optimization event at the ad set level - the actual `custom_event_type` of the promoted object. **Never infer from campaign or ad set names.**
- The list of conversion actions used

## Decision Logic

For each live campaign:

```
IF majority conversion event = PURCHASE         → ECOMMERCE
IF majority conversion event = LEAD             → LEAD GENERATION
IF custom conversion event (OTHER)              → CUSTOM CONVERSION (treat standalone; do not group with other types)
```

**Mixed accounts:** group ad sets by their event type and apply each group's PCM separately. Do not mix conversion types into one aggregate.

## Set PCM by Account Type

### Ecommerce

| Metric | Type | Source |
|---|---|---|
| Purchase ROAS | Primary (PCM) | `purchase_roas` field, deduplicated per the Purchase De-Duplication rule |
| Cost per Purchase | Secondary | spend / purchase count |
| Conversion Rate | Secondary | purchases / clicks |
| Revenue | Secondary | conversion value for purchase events |

### Lead Generation

| Metric | Type | Source |
|---|---|---|
| Cost per Lead | Primary (PCM) | spend / lead count |
| Conversion Rate | Secondary | leads / clicks |

### Custom Conversion

| Metric | Type | Source |
|---|---|---|
| Cost per Result | Primary (PCM) | spend / count of the specific custom event |
| Conversion Rate | Secondary | custom events / clicks |

> **Note:** For custom conversion campaigns, metrics are scoped to that specific conversion event only. No other conversion events should be included in the analysis for that campaign.

## Output

Set internally:

- `account_type`: `ecommerce`, `lead_gen`, or `custom_conversion`
- `primary_metric`: `purchase_roas`, `cost_per_lead`, or `cost_per_result_<custom_event>`

These flow into every later skill.

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Per active campaign: campaign objective + per-ad-set `promoted_object.custom_event_type`. Directly available. |
| CSV | "Campaign Objective" + "Performance Goal" / "Optimization Event" columns (often not in default exports - must be enabled). If unavailable, **ask the user to confirm the conversion event for each campaign** before proceeding. |
| Screenshot / copy-paste | Ask user to confirm directly per campaign. |

## Tool hints

The most reliable signal is `promoted_object.custom_event_type` on the ad set object. Campaign / ad set *names* lie often - never infer the conversion event from a name. If using MCP, fetch the ad set object explicitly. If using CSV without the optimization-event column, this entire skill blocks until the user confirms.

---

# Skill 3: Campaign Structure Analysis

Identify the strategic pattern behind how the account splits spend across campaigns. Different structures need different evaluation rules.

## When to use this skill

- Account audits
- When the user asks "is my campaign structure right?"
- Before doing ad-set-level analysis (the structure type changes what comparisons are valid)

## Data to gather

For each active (non-retargeting) campaign:

- Objective, bid strategy, daily/lifetime budget, status
- Ad-set level: bid strategy, optimization goal, promoted object (the conversion event), budget, attribution window, full targeting object
- Spend distribution at the campaign level over the last 30 days, sorted by spend desc

**Targeting fields to inspect on each ad set:**

| Field | Purpose |
|---|---|
| Age min / max | Demographics |
| Genders | Demographics |
| Geo locations | Geo targeting |
| Custom audiences | Retargeting detection |
| Detailed / flexible targeting (interests, behaviors) | Interest targeting |
| Publisher platforms / placement positions | Placement strategy |
| Languages | Language targeting |

## Step 1: Identify Retargeting Campaigns

Check the targeting custom audiences for: website visitors, past purchasers, video viewers, page engagers.

```
IF targeting.custom_audiences contains retargeting audiences
→ LABEL as "Retargeting Campaign"
→ EXCLUDE from structure analysis
```

## Step 2: Match the Active Structure to One of These Patterns

### Pattern A: Primary vs Testing

**Criteria:**

```
campaign_budget_share = campaign_budget / total_non_retargeting_budget

IF Campaign A:
   - budget_share < 30%
   - ad_count ≥ 5
AND Campaign B:
   - budget_share ≥ 40%
   - ad_count < Campaign A's ad_count
   - 70%+ of ads also exist in Campaign A
→ CONFIRMED: Primary vs Testing structure
```

### Pattern B: Bid Limit Split

**Criteria:**

For campaigns/ad sets (excluding retargeting), compare the targeting objects and bid configurations.

```
IF targeting is IDENTICAL across splits
AND bid_strategy OR bid_amount DIFFERS
→ CONFIRMED: Bid Limit Split
```

### Pattern C: Audience Split

**Criteria:**

For campaigns/ad sets (excluding retargeting), compare interest spec, custom audiences, demographics.

```
IF audiences DIFFER between splits
→ CONFIRMED: Audience Split

NOTE: Different bids/budgets across audience splits is OK.
```

### Pattern D: Too Many Campaigns (Custom Pattern)

**When:** more than one campaign and the structure doesn't fit A, B, or C.

**Investigate using creative inspection** - review the actual creative content of ads in each campaign and look for:

- Video vs Image split
- Catalog vs Static split
- UGC page vs Brand page
- Different products
- Different personas / angles
- Partnership ads vs direct

**Also check:**

- Website URLs across creatives - different funnels / landing pages / domains
- Attribution windows on each ad set - different windows often indicate different testing setups

## Output

Set `campaign_structure`:

- `primary_testing`
- `bid_limit_split`
- `audience_split`
- `custom_pattern: [description]`

This determines which Ad Set Analysis rules apply.

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Full ad set objects: bid strategy, optimization goal, promoted object, budget, `attribution_spec`, **full targeting object** (custom_audiences, interests, demographics, placements). All directly available. |
| CSV | **Mostly blocked.** CSV exports do not include the full targeting object. You can identify campaign-level pattern from spend distribution + budget, but the targeting-identical-vs-different test (Patterns B and C) cannot be run from CSV alone. **Ask the user to describe targeting per ad set** or pull from MCP. |
| Screenshot / copy-paste | Ask the user to walk through targeting per ad set in plain language. |

## Tool hints

This skill is the most MCP-dependent of the six. The structural patterns (Bid Limit Split, Audience Split) hinge on comparing full targeting specs across ad sets - something the Ads Manager CSV simply doesn't export. If MCP isn't available, ask the user to describe each ad set's audience in their own words, then map manually.

---

# Skill 4: Ad Set Analysis

Evaluate ad set performance based on the campaign structure type. Run **after** Campaign Structure Analysis.

## When to use this skill

- The campaign has more than one active ad set
- The user asks why one ad set is winning / losing vs another
- You're evaluating whether to ease bid limits, expand audiences, or pause underperformers

If the campaign has only 1 ad set → skip; campaign performance = ad set performance.

## Data to gather

Pull ad-set-level performance for the last 7 days, filtered to active ad sets with impressions > 0, sorted by spend descending:

- Ad set name, ID
- Spend, impressions, CPM
- For ecommerce: `purchase_roas`
- For lead gen: lead actions
- Clicks
- Daily / lifetime budget
- Bid strategy, bid amount

## Calculated Metrics

| Metric | Formula |
|---|---|
| Budget Utilization | spend / (daily budget × days in period) |
| Campaign Spend Share | ad set spend / total campaign spend |
| Cost per Purchase | spend / purchases |
| Cost per Lead | spend / leads |

## Minimum Spend Threshold (CRITICAL)

For ALL comparisons:

```
Only compare ad sets where campaign_spend_share ≥ 25%
Do NOT make recommendations based on low-spending ad sets - the signal is too noisy.
```

## 4A: Bid Limit / Strategy Split Analysis

**Use when:** `campaign_structure = bid_limit_split`

### Rule 1: Underspending Ad Set

```
budget_utilization = spend / (daily_budget × days_in_period)

IF budget_utilization < 85% AND ad set has bid_strategy with limit
→ Normal bid-limit behavior (Meta can't find cheap enough conversions)

BUT IF:
   - campaign_spend_share > 25%
   - PCM is good
   - budget_utilization < 85%
→ RECOMMEND: Drop the bid slightly to allow more spend
```

### Rule 2: Zero / Minimal Spend

```
IF spend ≈ 0 over the last 7 days AND a bid_amount is set
→ RECOMMEND: Ease the bid limit so Meta can deliver
```

### Rule 3: Clear Winner Pattern

```
PREREQUISITE: Both ad sets have campaign_spend_share ≥ 25%

Compare PCM (purchase_roas or cost_per_lead):

IF ad set A significantly outperforms ad set B
→ RECOMMEND:
   1. Pause low performer (ad set B)
   2. Test an even stronger bid on a new ad set
   3. Find ways to scale the winning ad set (within scaling guardrails)
```

### Rule 4: CPM vs PCM Relationship

```
Calculate for each ad set: CPM and PCM

IF cpm is high (due to stronger bid) AND PCM is good
→ LEAVE IT (you're paying more but it's converting)

IF cpm_increase ≥ 60% vs other ad sets AND pcm_drop ≥ 30%
→ RECOMMEND: Ease bid to drop CPM
```

CPM comparison:

```
avg_cpm = AVG(cpm across all ad sets)
adset_cpm_variance = (adset_cpm − avg_cpm) / avg_cpm × 100

IF adset_cpm_variance ≥ 60% → FLAG as high CPM
```

## 4B: Audience Split Analysis

**Use when:** `campaign_structure = audience_split`

### Rule 1: Clear Winner Pattern

```
PREREQUISITE: Both ad sets have campaign_spend_share ≥ 25%

Compare PCM:

IF ad set with audience A significantly outperforms audience B
→ RECOMMEND: Pause low performer to shift spend to the winner
```

### Rule 2: Underspending Ad Set

```
IF budget_utilization < 85% → likely cause: small audience size (check reach)

IF:
   - campaign_spend_share > 25%
   - PCM is good
   - budget_utilization < 85%
→ RECOMMEND: Expand the audience
```

### Prohibition

⛔ **Never suggest lookalike audiences in any context.**

## Output Format

```
### Ad Set Analysis: [Campaign Name]

Structure Type: [Bid Split / Audience Split]

| Ad Set | Spend | Spend % | Budget Util | CPM | ROAS/CPA | Status |
|--------|-------|---------|-------------|-----|----------|--------|
| [Name] | $X    | X%      | X%          | $X  | X        | [Keep/Watch/Action] |

Findings:
- [Finding 1 with specific metrics]
- [Finding 2 with specific metrics]

Recommendations:
- [Recommendation 1, plain language]
- [Recommendation 2, plain language]
```

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Per ad set, last 7 days: spend, impressions, CPM, `purchase_roas` (ecommerce) or lead actions (lead gen), clicks, daily/lifetime budget, bid strategy, bid amount. All directly available. |
| CSV | Ad Set view export with these columns enabled: Spend, Impressions, CPM, Purchase ROAS or Cost per Lead, Link Clicks, Budget, Bid Strategy, Bid Amount. **Bid Strategy and Bid Amount are not default columns - must be enabled before export.** |
| Screenshot / copy-paste | Workable for a single-ad-set check; not workable for multi-ad-set comparison. |

## Tool hints

The 7-day window is short - confirm minimum spend thresholds (≥ 25% of campaign spend share) before any comparison. Bid Strategy and Bid Amount are the two CSV columns most often missing; if absent, **the bid-limit-split rules (4A) cannot run** - fall back to the audience-split rules or ask for the missing columns.

---

# Skill 5: Performance Analysis

Top-down ad-level audit using the Pareto principle. Identify the ads driving 90% of spend, classify each as keep / pause / test, and produce account-level strategic recommendations.

## When to use this skill

- "Audit my account"
- "Which ads should I pause?"
- "What's working in this campaign?"
- Anytime you need a portfolio view before drilling into creative

## Step 1: Confirm Account Type & PCM

Use the output of **Conversion Metric Focus** (Skill 2). If it hasn't been run yet, run it first. If the account has mixed conversion types, group ad sets by event type and analyze each group with its own PCM.

### Pre-Audit Check: COMPLETE_REGISTRATION on Purchase Objective

If you see any ad set with campaign objective `OUTCOME_SALES` AND optimization event `COMPLETE_REGISTRATION`, apply the **3rd-party-tracker check** from the Metric Glossary section before any recommendation on that ad set.

## Step 2: Pareto Pull (90% of Spend)

Pull ad-level insights for the last 30 days. Filter to **active ads** (effective status = ACTIVE) with impressions > 0, sorted by spend desc. If the result set is paginated, **fetch all pages before analyzing** - analyzing only the first page produces wrong totals and wrong CPAs.

Required fields per ad:

- Ad name, ad ID, ad set ID/name
- Spend, impressions, CPM, CTR, clicks
- Actions (for purchase / lead counts)
- Action values (for revenue)
- Purchase ROAS

Then calculate **cumulative spend %** for each ad in spend-descending order. Keep the ads where cumulative % ≤ 90% - these are your Pareto ads. Focus the analysis on them.

## Step 3: Establish Baselines from the Pareto Set

| Baseline | Calculation |
|---|---|
| Pareto avg CPM | mean CPM across Pareto ads |
| Pareto avg CTR | mean CTR across Pareto ads |
| Pareto avg PCM | mean ROAS (ecommerce) or mean CPL / CPR (lead gen / custom) |
| Account avg Hold Rate | from a 90-day account-level pull (only needed for video analysis - see Skill 6) |

These become the comparison points for every individual-ad assessment.

## Step 4: Diagnose Each Pareto Ad

Apply the variance benchmarks (Performance Benchmarks table in Metric Glossary):

**High CPM (≥ 30% above Pareto avg) + Low PCM (≥ 30% below avg)**

- Diagnosis: expensive audience, not converting
- Recommendation: pause this ad OR test different targeting

**Low CTR (≥ 30% below Pareto avg) + Low PCM**

- Diagnosis: ad isn't resonating with the audience
- Action: first check comments for negative sentiment
- If comments are fine → recommend copy / creative variations with stronger CTA

**Good metrics but declining trend**

- Diagnosis: likely creative fatigue (check the fatigue signal - frequency rising + CTR falling over 14+ days)
- Recommendation: new creative variations, NOT budget changes

**Good metrics, stable trend**

- Diagnosis: working as intended
- Recommendation: create variations (copy / angle / format / hook) to extend the winning pattern

## Step 5: Generate Recommendations

**Mandatory:** after analysis, produce specific, actionable recommendations.

### Per-Ad Recommendations

For each Pareto ad:

- **What** - specific action (pause, scale, create variation, change targeting)
- **Why** - metrics-based justification (e.g., *"CPM 40% above Pareto avg with 0.3× ROAS"*)
- **How** - concrete next steps for the user to apply in Ads Manager

### Strategic Recommendations

Summarize the top 3–5 account-level moves:

1. **Budget direction** - which campaigns or ad sets to scale (within the 20% cap) vs which to pull back. Respect the budget-reallocation guardrails: only campaign / ad set budgets, never ad-level or per-placement.
2. **Creative strategy** - what's working, what to test next.
3. **Targeting adjustments** - if CPM issues are widespread.
4. **Structure changes** - campaign / ad set consolidation if needed.

### Output Format

```
## Performance Summary

| Ad | Format | Spend | CPM | CTR | ROAS/CPA | Status |
|----|--------|-------|-----|-----|----------|--------|
| [Name] | Image | $X | $X | X% | X | [Scale/Pause/Test] |

Benchmarks (Pareto avg): CPM: $X | CTR: X% | ROAS: X

## Recommendations

### Per-Ad Actions
1. **[Ad Name]**: [Action] - [Justification]
2. **[Ad Name]**: [Action] - [Justification]

### Strategic Recommendations
1. [Plain-language recommendation with metrics basis]
2. [Plain-language recommendation with metrics basis]
3. [Plain-language recommendation with metrics basis]
```

**If creative-level depth is needed** (video hook/hold, image diagnostics, ad copy evaluation), continue to **Skill 6: Creative Analysis**.

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Ad-level insights over the last 30 days for **active ads with impressions > 0**, sorted by spend desc. Required fields: ad name, ad ID, ad set name/ID, spend, impressions, CPM, CTR, clicks, `actions` (for purchase/lead counts), `action_values` (for revenue), `purchase_roas`. **Paginate all pages before analyzing** - analyzing only page 1 gives wrong totals and CPAs. |
| CSV | Ad-level view export filtered to active ads, last 30 days. Must include: Ad Name, Spend, Impressions, CPM, CTR, Link Clicks, Purchases, Purchases Conversion Value, Purchase ROAS. For lead-gen accounts, swap Purchases / ROAS for Leads / CPL. |
| Screenshot / copy-paste | Workable only if the screenshot already shows the full Pareto set (top N ads by spend) with all required columns. |

## Tool hints

The Pareto cut (top 90% of spend) is the entry point - fetching only top-10 by spend will miss ads that round out the 90% threshold. With MCP, request **all active ads sorted by spend desc** and paginate fully. With CSV, ensure the export was filtered to ACTIVE ads only (paused / archived ads inflate the totals). **Run the COMPLETE_REGISTRATION 3rd-party tracker check from Skill 5 Step 1 before any pause / scale recommendation** - this is the highest-stakes safety check in the framework.

---

# Skill 6: Creative Analysis

Deep creative analysis with diagnostic scenarios for video ads, plus image and catalog format rules. Run **after** Performance Analysis when more depth is needed on specific Pareto ads.

## When to use this skill

- Video hook / hold metrics are off
- "Why isn't this creative working?"
- Need to plan variations of winners
- The user wants to understand a specific ad in depth

## Inputs You Need

Before applying this skill:

- Ad-level video metrics (video plays, ThruPlays, 3-second views - using the **video_view action** inside the actions array, NOT `video_p25_watched_actions`)
- Account-level Hold Rate baseline from a 90-day account-level pull
- The Pareto set of ads (from Skill 5)
- The actual creative content for each Pareto ad - for video, the visuals and audio; for image, the visual; for all formats, the copy (headline, primary text, CTA). The user can share screenshots, video files, or descriptions.

## Step 1: Format-Agnostic Diagnostics (Apply to Every Ad)

| Profile | Diagnosis | Recommendation |
|---|---|---|
| High CPM (≥ 30% above Pareto avg) + Low PCM (≥ 30% below) | Expensive audience, not converting | Pause ad |
| Low CTR (≥ 30% below Pareto avg) + Low PCM | Not resonating | Check comments first; if fine, test variations with stronger CTA |
| Good metrics (within 20% of avg + PCM above avg) | Working | Create variations (copy / angle / format) |

## Step 2: Video-Specific Diagnostic Scenarios

Apply Hook Rate / Hold Rate / CTR benchmarks (from Metric Glossary) to classify each Pareto video ad.

### Scenario 1: Good Hook, Poor Hold

| Metric | Status | Range |
|---|---|---|
| Hook Rate | Strong | ≥ 40% |
| Hold Rate | Poor | < Account Avg |
| CTR | Average | 0.65 – 1.24% |
| PCM | Poor | Below target |

**Interpretation:** Hook is stopping scroll, but people drop off after 3 seconds. They're missing key information.

**Recommendations:**

1. KEEP the intro / hook (it's working)
2. CHANGE seconds 3+ completely

Tactics:

- Move value prop order around
- Show product sooner
- Get to "how this helps you" faster
- Avoid stagnant clips - use variety
- Quick B-roll + testimonial + selfie style mix
- Keep value props concise (not 10 seconds each)
- Ensure seconds 3+ relate back to the hook's problem / promise

### Scenario 2: Average Everything

| Metric | Status | Range |
|---|---|---|
| Hook Rate | Average | 26 – 39% |
| Hold Rate | Average | ≈ Account Avg |
| CTR | Average | 0.65 – 1.24% |
| PCM | Poor | Below target |

**Interpretation:** Nothing stands out. Room for improvement everywhere. Priority 1 - improve the hook first. If they don't stop, they won't purchase.

**Recommendations:**

1. **Priority:** rebuild the hook / intro first. Inspect the creative for:
   - Is the visual relevant to the target audience?
   - Is the intro speaking to the wrong customer?
   - Can it be more direct?
   - Can it relate to the customer better?
2. THEN: build the remaining clips to improve hold rate.

**Warning:** don't go click-baity. The hook must be relevant to the actual customer.

### Scenario 3: Poor Hook

| Metric | Status | Range |
|---|---|---|
| Hook Rate | Poor | < 25% |
| Hold Rate | Any | - |
| CTR | Any | - |
| PCM | Poor | Below target |

**Interpretation:** People aren't even stopping to watch. Nothing else matters until the hook is fixed.

**Recommendations:**

1. Watch the actual video
2. Document the current hook (visual + audio)
3. Compare to hooks in top-performing ads (review those too)
4. Rebuild the hook based on what works

Hook elements to test:

- Different visual opening
- Different text overlay
- Different audio hook
- Problem statement vs benefit statement
- Question vs statement

### Scenario 4: Great Hook + Great Hold, Poor CTR

| Metric | Status | Range |
|---|---|---|
| Hook Rate | Good | ≥ 40% |
| Hold Rate | Good | > Account Avg + 25% |
| CTR | Poor | < 0.65% |
| PCM | Poor | Below target |

**Interpretation:** People are watching the whole video but not clicking. CTA is weak or unclear.

**Recommendations:**

1. Check comments for negative sentiment
2. If comments are fine → strengthen the CTA

CTA improvements:

- More prominent visual CTA
- Clearer verbal CTA
- Urgency / scarcity element
- Better landing-page alignment

## Step 3: Format-Specific Rules

### Single Image

- High CPM (30%+ above Pareto avg) + Low PCM → recommend pausing the ad
- Low CTR (30%+ below avg) + Low PCM → check comments; if fine, test stronger-CTA variations
- Good metrics → create variations (copy, angle, or format)

### Single Video

Apply Scenarios 1–4 based on Hook / Hold / CTR profile, plus:

- High CPM + Low PCM → pause
- Low CTR + Low PCM → check comments, then test stronger-CTA variations

### Advantage+ Catalog Ads

**Limitation:** Meta does NOT provide conversion data per product ID. Workaround:

- Build a Pareto of product IDs by spend
- Use spend + CTR as a proxy - higher spend + higher CTR = likely better performer

- High CPM + Low PCM → pause ad, test a different product set. Also check: if 1–2 product IDs are pushing CPM up, recommend removing those products from the set.
- Low CTR + Low PCM → identify low-CTR products from spend/impressions data, recommend removing them from the set.

## Step 4: Pattern Recognition Across Top Performers

Among the top Pareto ads, review the creative content of each and identify shared patterns:

- Common angle patterns (which selling points repeat across winners)
- Common format patterns (image vs video vs carousel)
- Common hook patterns (videos - what stops the scroll)
- Common copy patterns (tone, length, structure)

Use winning patterns to guide new variation creation.

## Step 5: Variation Strategy

### When an ad is performing well

Create variations in this order:

1. Copy variations (same angle, different words)
2. Angle variations (different selling point)
3. Format variations (same message, different format)
4. Hook variations (videos - same body, different hooks)

### When an ad is performing poorly

| Issue | Action |
|---|---|
| Hook Rate poor | Rebuild hook using winning hooks |
| Hook good, Hold poor | Rebuild middle section |
| Hook good, Hold good, CTR poor | Strengthen CTA |
| All metrics poor | Test a completely new approach |

## Decision Tree Summary (Video)

```
START
  │
  ├─ Hook Rate < 25%?
  │    └─ YES → Rebuild hook completely (Scenario 3)
  │
  ├─ Hook Rate 26–39%?
  │    └─ YES → Improve hook first, then content (Scenario 2)
  │
  └─ Hook Rate ≥ 40%?
       │
       ├─ Hold Rate < Account Avg?
       │    └─ YES → Rebuild middle section (Scenario 1)
       │
       └─ Hold Rate good but CTR < 0.65%?
            └─ YES → Strengthen CTA (Scenario 4)
```

## Output Format

```
### Creative Analysis: [Ad Name]

Creative Profile:
| Element     | Analysis      |
|-------------|---------------|
| Angle       | [description] |
| Persona     | [description] |
| Format      | [description] |
| Visual Hook | [description / N/A for image] |
| Audio Hook  | [description / N/A for image] |
| CTA         | [description] |

Metric Diagnosis:
| Metric    | Value | Benchmark         | Status        |
|-----------|-------|-------------------|---------------|
| Hook Rate | X%    | Good ≥ 40%        | [Good/Avg/Poor] |
| Hold Rate | X%    | Acct Avg: Y%      | [Good/Avg/Poor] |
| CTR       | X%    | Good ≥ 1.25%      | [Good/Avg/Poor] |
| ROAS/CPA  | X     | [Target]          | [Good/Poor]   |

Benchmarks used:
- Account avg Hold Rate (90d): X%
- Pareto avg CPM: $X
- Pareto avg CTR: X%

Scenario Match: [1 / 2 / 3 / 4 / N/A for non-video]
Root Cause: [description]

Top Performers - Common Patterns:
- Angle: [pattern]
- Format: [pattern]
- Hook: [pattern, videos]
- Copy: [pattern]

Recommendations (plain language, for the user to apply in Ads Manager):
1. [Specific recommendation with metrics justification]
2. [Specific recommendation with metrics justification]
3. [Specific recommendation with metrics justification]
```

## Minimum required data (by source)

| Source | What you need |
|---|---|
| MCP | Ad-level video metrics: `video_play_actions`, `actions` (containing `video_view` = 3-second), ThruPlay events. Account-level 90-day pull for Hold Rate baseline. Creative content via creative endpoint (e.g. `facebook_get_ad_creative_details`). |
| CSV | Ad-level export with "Video Plays", "3-Second Video Plays", and "ThruPlays" columns enabled. Plus a separate 90-day account-level aggregate pull for Hold Rate baseline. **Creative content (the actual video / image / copy) is NEVER in a CSV - must be shared separately.** |
| Screenshot / copy-paste | Works for spot-checking a single ad's video metrics if visible. Creative content can come from a video file upload or a description. |

## Tool hints

This skill needs **two kinds of data**: numeric (Hook/Hold/CTR) and qualitative (the actual creative). Numeric works fine from any source as long as video columns are enabled. Qualitative requires the user to share files or text - no export captures creative content. Build a checklist before starting: numeric metrics ✓, 90-day Hold Rate baseline ✓, the actual ad creative ✓. Without all three, the skill outputs framework, not diagnosis.

---

# Cross-Cutting Notes

## How to handle missing data

If the user can't provide the data a skill needs, do **not** invent values. State explicitly:

> *"To answer this properly I need [specific metrics]. You can pull these from [Ads Manager export / a connected data tool / Events Manager]. Without them I can outline the framework but not give a recommendation."*

## How to handle change requests

When the user asks Claude to change something in their account (e.g. *"pause this ad"*, *"raise the budget 20%"*):

1. Run the relevant analysis skill to validate the change is justified.
2. Apply the guardrails (especially scaling caps, top-performer protection, and the "no ad-level budget moves" rule).
3. **Recommend the change in plain language** - exact entity, current value, proposed value, rationale, what to monitor afterwards, and any safety warnings (learning-phase reset, > 50% decrease, > 100% increase, etc.).

Claude does not execute changes on the user's ad account. These skills are read-and-recommend only - the user applies recommendations manually in Ads Manager.

## How to handle multiple account types in one account

If the account has both purchase-optimized and lead-optimized campaigns:

- Group ad sets by their `custom_event_type`
- Apply each group's PCM separately
- Never aggregate ROAS across purchase + lead campaigns

## How to handle account-type ambiguity

Always classify the account before applying KPIs:

1. Check the actual ad-set-level conversion events (not the campaign / ad set names).
2. Check whether conversion value is populated.
3. If unclear, ask the user.
4. Apply the special-case check for COMPLETE_REGISTRATION on purchase objectives (3rd-party tracker scenario).

## How to handle stale data

Meta campaigns change frequently. If the data the user shared is more than a day or two old:

- Ask for a fresh pull before any recommendation
- Especially before pause / scale / structural changes
- Recommendations based on stale state can be wrong or harmful

## What to do when the API / export doesn't show a needed metric

Some signals aren't directly available via standard insights exports:

- **EMQ Score** → manual check in Events Manager
- **Audience segment configuration** → manual check in Audience Manager (the breakdown shows distribution, but setup state isn't readable)
- **Comments / sentiment** → manual check in Ads Manager or the Page
- **Per-product conversion data in catalog ads** → not provided; use spend + CTR as proxy

When a signal isn't available, state that explicitly, point the user to where they can check it manually, and frame the recommendation around the data that IS available.

## What good looks like

- The health check and conversion-metric decision run before any performance judgment, and the metric never changes mid-analysis.
- The top-converting ad in an ad set is never recommended for pause, whatever its budget share.
- Budget recommendations touch only campaign or ad set budgets, bid caps, or on/off. Breakdowns are read as distribution, not as levers.
- Scaling moves are capped at 20 percent, carry a review window and a spend cap, and wait for the ad set to clear the revenue-share and significance floors.
- Creative verdicts pair the numbers (hook, hold, CTR) with the actual creative, or the output says it can only give the framework.
