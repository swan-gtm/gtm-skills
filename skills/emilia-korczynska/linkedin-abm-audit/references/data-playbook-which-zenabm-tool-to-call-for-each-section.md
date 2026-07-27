---
title: "Data playbook: which ZenABM tool to call for each section"
description: "Reference for the LinkedIn ads & ABM audit skill."
---

# Data playbook: which ZenABM tool to call for each section

Tool names below are shown unprefixed (e.g. `get_creative_performance`). At runtime they carry the ZenABM
connector's server prefix — match by the trailing name. Two windows matter everywhere: **cur** = last 30 days,
**prev** = the 30 days before that. Pass explicit `startDate`/`endDate` (YYYY-MM-DD) so "previous period" is
unambiguous, rather than relying on `period` for the comparison window.

Probe first: call `get_linkedin_metrics` for the last 30 days. If it errors or is empty, the connector isn't ready
— stop and help the user finish connecting their LinkedIn ads account in ZenABM. Never invent numbers.

## 1. Account scorecard (spend, ads, CPC, CPM, CTR, eff-CPC-to-LP)
- `get_linkedin_metrics` for cur and prev → impressions, clicks, engagements, cost. Derive CPC, CPM, CTR (see the
  metrics reference).
- `get_ad_spend` for cur → `summary.costInUsd`, `adSetCount`, and `byAdSet` for the spend breakdown.
- Landing-page clicks come from `get_creative_performance` (sum `landingPageClicks`) → account effective CTR/CPC
  to LP.

## 2. Are you running the right number of ads?
- `list_creatives` with `pageSize: 100`, paginate via `nextCursor`; count **currently serving** ads (serving
  state), and note format of each. Exclude TEXT_AD from the click-budget count.
- Feed cur spend + account CPC into the **ad-count model** in the metrics reference. Classify too few / about
  right / too many and compute per-ad daily spend + health tier.

## 3. Where your budget goes (format mix + spend share)
- `get_creative_performance` with `groupBy: "format"`, cur window → one row per format with summed impressions,
  clicks, landingPageClicks, cost, engagements. Spend share = format cost / total cost. Ad counts per format come
  from the `list_creatives` catalog in step 2.

> **RULE — classify every ad by its `adFormat` / `format` field, never by campaign or ad-set NAME.** Users name
> campaigns freely, so a campaign called "TLA" can be full of Single Image ads and a "Bootcamp" campaign can be
> TLAs. Always read the actual `adFormat` (`TLA`, `STANDARD_UPDATE`=Single Image, `SINGLE_VIDEO`, `CAROUSEL`,
> `SPONSORED_UPDATE_NATIVE_DOCUMENT`=Document, `TEXT_AD`, `SPOTLIGHT`) from the creative/format data. If you
> mention a campaign in the report, state the format its ads actually are, not what its name implies.

## 4. What's influencing your deals (needs CRM/HubSpot)
- `list_deals` with `influenceFilter` / `abmCampaigns` to get influenced deals and amounts. If deals return with
  the influencing campaigns/ad sets, map those to formats (via `list_creatives` / `get_creative_performance`) to
  attribute deals→format. `get_company_deals` can confirm which ads touched a given account's deal.
- If `list_deals` is empty or CRM isn't connected: **skip this section** and note that connecting the CRM in
  ZenABM unlocks it. Don't guess influence without deal data.

> **RULE — quarantine test / sandbox deals; never count them as pipeline.** CRM connections often include a
> developer or sandbox org seeded with fake opportunities, and these are usually the *largest* amounts, so they
> silently dominate "influenced pipeline." Treat a deal as test data (exclude it from headline pipeline, or show
> it clearly labelled "test/demo") when any of these hold: the `externalUrl` points at a sandbox/dev host
> (contains `develop.my.salesforce.com`, `sandbox`, `--dev`, `orgfarm`, `test`, or similar); the deal or company
> name is an obvious placeholder (`Acme`, `Test`, `OPPORTUNITY TEST`, `Demo`, `Example`); the company on the deal
> doesn't match the account it's filed under (e.g. an opp named "Acme Robotics" attached to company
> "GrowthMentor"); or a round, outsized amount ($25k/$30k/$40k) sits on an account with only a handful of real
> impressions. When in doubt, keep the deal in the report but flag it as likely test data and base the verdict on
> the real, production-CRM deals. Prefer HubSpot production deals over Salesforce dev-org rows when they conflict.

## 5. Benchmark grade by format
- Reuse the `groupBy: "format"` result from step 3 for cur. Compute CTR, CPC, effective CTR to LP, effective CPC
  to LP, CPM (+ dwell if present) per format and grade each against the benchmarks reference.

## 6. Reallocate the budget
- Derived from steps 3 + 5 (+ 4 if CRM). No new calls.

## 7. Campaign trends
- `list_campaigns` for cur and prev → per-campaign impressions, clicks, engagements, cost, CPC, CTR; compute
  deltas and the efficiency verdict.
- `list_abm_campaigns` + `get_abm_campaign_overview` → ABM campaign performance; combine with `list_deals`
  (`abmCampaigns`) to find the **top ABM campaign by pipeline/deals**.
- Best campaigns / best campaign types = rank the `list_campaigns` rows by clicks/CTR/efficiency.
- **CTR spike/drop explained:** when a campaign's CTR jumps or craters vs prev, pull its ads with
  `get_creative_performance` (`campaignUrn` filter, sort by clicks/impressions) and name the specific ad(s)
  driving it.

## 8. Ad insights
- Best/worst ads by clicks: `get_creative_performance` cur, `sortBy: "clicks"`, `sortOrder` DESCENDING then
  ASCENDING.
- Best/worst formats: the `groupBy: "format"` result.
- TLA effective CTR + effective spend: `get_creative_performance` with `adFormat: "TLA"` → per-TLA
  landingPageClicks/impressions and cost/landingPageClicks. Flag TLAs with no link (0 LP clicks) as n/a.
- **Decaying ads (needs weekly series):** call `get_creative_performance` for ~4 consecutive **weekly** windows
  (e.g. last 4 Sundays) and track each ad's weekly CTR. Flag any ad whose CTR fell three weeks running, or that is
  below its format's pause threshold (see the benchmarks reference) after 1,000+ impressions. `list_companies`
  with `includeWeekly: true` also returns weekly buckets if you need account-level weekly trend.

## 9. Accounts to go after (company trends)
- Top engaged: `list_companies` cur, `sortBy` engagements/clicks DESCENDING.
- Surging: `list_companies` with `includeWeekly: true` — compare each company's latest week vs prior weeks; rank
  the biggest positive jumps in clicks/engagements.
- Newly reached: companies present in cur with no prior-period activity (diff cur vs prev company lists).
- Moved to **Interested**: `list_abm_stages` to find the "Interested" stage id, then
  `get_abm_stage_companies_entering` with that id + cur window. Link the reader to the filtered stage view in
  ZenABM if you can.
- Impression hogs: `list_companies` cur, `sortBy` impressions DESCENDING. Only recommend impression-capping /
  excluding a company when its impression share is lopsided versus the rest (e.g. one account eating a large
  multiple of the median). Otherwise just list them.

## Pagination & efficiency
- Prefer `groupBy: "format"` and account-level tools over looping per-ad where possible — fewer calls, cleaner
  totals. Only drill to per-ad/per-campaign detail for the specific spike/decay/best-worst callouts.
- Respect page sizes (max 100). Paginate `list_creatives` by cursor; paginate `list_companies`/`list_deals` by
  page. Stop once you have enough for the top-N lists — you don't need every row.
