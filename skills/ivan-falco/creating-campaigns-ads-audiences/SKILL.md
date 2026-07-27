---
name: "creating-campaigns-ads-audiences"
title: "Create Meta campaigns & audiences"
description: "Use this skill when creating campaigns, ad sets, ads, or audiences on Meta — the build chain and the settings that matter, step by step."
category: Ads
---

# Creating Campaigns, Ads, and Audiences on Meta

The full build chain, end to end. Meta's structure is strict and nested:

```
Campaign (objective, budget if CBO)
  -> Ad Set (audience, placement, budget if ABO, optimization goal, schedule)
    -> Ad (references a creative + an ad set)
      -> Ad Creative (media, copy, CTA, link, url_tags)
Custom / Lookalike Audiences (built at the account level, referenced by ad sets)
```

**Golden rules (always):**
- **Everything is created PAUSED.** Never set a campaign, ad set, or ad to `ACTIVE` without explicit user confirmation. Spend only starts when the user says go.
- **Budgets are in cents.** `5000` = $50.00.
- **Build order:** audiences first (ad sets reference them) -> campaign -> ad set -> creative -> ad.
- Full field-level schemas (every param, every enum) are in [../api-reference.md](../api-reference.md). This guide is the flow; the api-reference is the dictionary.

---

## 1. Audiences

**Custom audience** (from a customer list, pixel traffic, engagement) - use the script:
```bash
python create_custom_audience.py --name "CRM - Closed Won" --type CUSTOM --subtype CRM
```
For B2B, follow the data hierarchy in [audience-strategy.md](audience-strategy.md): CRM lookalikes (Tier 1) -> third-party data (Tier 2) -> broad (Tier 3). Validate audience quality before scaling creative.

**Lookalike** - create the source custom audience first, then create a lookalike from it (`subtype=LOOKALIKE`, with `origin_audience_id` and country/ratio). See api-reference.md for the lookalike spec.

---

## 2. Campaign

Use the script:
```bash
python create_campaign.py --name "Q2 Leads" --objective OUTCOME_LEADS --daily-budget 5000
```
- `OUTCOME_LEADS` for lead gen. Objectives are listed in `create_campaign.py`.
- Add `is_adset_budget_sharing_enabled: "true"` for CBO (budget on the campaign) or `"false"` for ABO (budget on each ad set). ABO is the default for audience testing - one ad set per audience source, same ads across all.
- Starts PAUSED. The script prints the `campaign_id` for the next step.

---

## 3. Ad Set

**Endpoint:** `POST /{account_id}/adsets` (see api-reference.md "Ad Set Schema" for all fields). Create with `api_post` from `client.py`. Key fields:
- `campaign_id` (from step 2), `name`, `status: "PAUSED"`
- `optimization_goal` (e.g. `OFFSITE_CONVERSIONS`, `LEAD_GENERATION`), `billing_event`, `bid_strategy`
- `targeting` (JSON): the audience - `custom_audiences`, `geo_locations`, `age`, plus `flexible_spec` for interests if broad. For B2B, lean on your custom/lookalike audiences and let creative do the ICP filtering (see [meta-ads-operating-system.md](meta-ads-operating-system.md)).
- `daily_budget` (cents) only if ABO.
- `promoted_object` when optimizing for conversions/leads (pixel + custom event, or the lead form / page).

Validate the audience before scaling: one ad set per audience source, same ads across all, audit lead quality by job title and company.

---

## 4. Ad Creative

**Endpoint:** `POST /{account_id}/adcreatives` (see api-reference.md "Ad Creative Schema"). The creative holds the actual content via `object_story_spec` (page id + link data: image/video, message, headline, description, CTA, link). Notes:
- `url_tags` (UTMs) are set at creative-creation time and cannot be edited later - get them right up front.
- **Creative IS targeting on Meta.** The copy must call out who the ad is for. On broad audiences the creative does the filtering (see [creative-strategy.md](creative-strategy.md)).
- Never invent ad copy. Use exactly the headline / body / description / CTA the user provides.

---

## 5. Ad

**Endpoint:** `POST /{account_id}/ads`. Fields: `name`, `adset_id` (step 3), `creative: {creative_id}` (step 4), `status: "PAUSED"`. That wires the creative into the ad set.

---

## 6. Go live

When the user confirms, flip status to ACTIVE (campaign, ad set, and ad all need to be ACTIVE to spend):
```bash
python update_campaign.py --campaign-id <id> --status ACTIVE
```
Confirm the budget and audience one more time before enabling spend. Maintain 4-6 unique creative concepts per campaign so the algorithm has diversity to learn from.
