---
title: "Metric definitions and the ad-count model"
description: "Reference for the LinkedIn ads & ABM audit skill."
---

# Metric definitions and the ad-count model

All metrics come from the ZenABM connector fields: `impressions`, `clicks`, `landingPageClicks`, `cost` (USD),
`engagements` (and video fields). Compute per format and per ad; roll up for the account.

## Core rates

```
CTR                    = clicks / impressions
CPC                    = cost / clicks
CPM                    = cost / impressions * 1000
effectiveCTRtoLP       = landingPageClicks / impressions
effectiveCPCtoLP       = cost / landingPageClicks          # n/a when landingPageClicks == 0
engagementRate         = engagements / impressions
```

- **Effective CTR to LP** is the honest "did this ad actually send someone to the site" rate — it strips out
  likes, comments, profile clicks and other non-LP clicks. For a plain image/carousel/video ad it usually equals
  CTR; for TLAs it is much lower than CTR because most TLA "clicks" are profile/expand clicks, not link clicks.
- **Effective CPC to LP** is what each real landing-page visit cost. This is the number that matters for pipeline,
  and it is where TLAs win big ($3.06 vs $13+ for image).
- If `landingPageClicks == 0`, report effective CPC to LP as **n/a** (no link / no LP traffic), never as $0 or
  infinity.

> **RULE — grade image ads (and any link-driving format) on effective CPC to LP, not raw CPC.** Raw CPC bills for
> every click including likes, reactions, profile and expand clicks that never reach the site. The honest cost of
> an image ad is `cost / landingPageClicks` (effective CPC to LP), compared to the **$13.23** image benchmark.
> Lead with that number in the scorecard, the benchmark grade and the reallocation for Single Image, Carousel and
> Video. Raw CPC can be shown alongside as secondary, but the pass/fail call and any "this format is too
> expensive" verdict must be driven by effective CPC to LP. (TLAs are the one format where raw CPC and effective
> CPC to LP diverge hugely in the other direction — always report both for TLAs too.)

## TLA effective metrics (called out in the report)

For Thought Leader Ads specifically, from the engagement/creative data:

```
TLA effectiveCTR   = landingPageClicks / impressions
TLA effectiveSpend = cost / landingPageClicks        # "effective cost per LP click"
```

Only TLAs that carry a link produce landing-page clicks. A TLA with no link has `landingPageClicks == 0` and
therefore no effective metric — say "no link, so no landing-page metric," don't score it as a zero.

## Deltas (period over period)

For any metric `m`, with `cur` = this 30 days and `prev` = the previous 30 days:

```
deltaPct = (cur - prev) / prev * 100        # guard prev == 0 → report "new" instead of a %
```

Report direction words plainly: impressions/engagements/clicks **up** is good; spend **down** with output flat or
up is **increasing efficiency**; spend **up** with output flat or down is **decreasing efficiency**. Always pair a
volume delta with a cost delta so the verdict is honest (e.g. "clicks +18% while spend -6% — you got more for
less, efficiency is improving").

## Ad-count model (are you running the right number of ads?)

Reverse-engineered from ZenABM's LinkedIn Ads Count Calculator. For the audit, use the user's **last-30-days
spend** as the budget and their **actual CPC** (not an assumption):

```
monthlyBudget      = last30DaysSpend
CPC                = actual account CPC (cost / clicks over the window)
clicksPerAdPerDay  = 3                                   # ZenABM planning default
dailyBudget        = monthlyBudget / 30
minDailyPerAd      = max(CPC * clicksPerAdPerDay, 20)    # hard $20/day floor
affordableAds      = max(floor(dailyBudget / minDailyPerAd), 1)
```

`affordableAds` is the number of click-driving ads this budget can fund at healthy delivery **at once**. Compare
to the **actual number of currently-serving ads** (`list_creatives`, servingOnly). Text ads run on set-CPC and
don't consume this budget — exclude them from the "actual" count for a fair comparison.

**Verdict:**

- `actualAds > affordableAds` by a meaningful margin → **too many** — the budget is spread too thin, each ad is
  starved below the delivery floor and LinkedIn can't optimize any of them. Recommend consolidating to
  ~`affordableAds` and pausing the weakest.
- `actualAds < affordableAds` by a meaningful margin → **too few** — there's headroom to launch more creatives /
  formats (lead with TLAs) and give the algorithm more to optimize.
- within ~20% either way → **about right**.

**Per-ad delivery health** (per-ad daily spend = `monthlyBudget / 30 / actualAds`, or `CPC * clicksPerAdPerDay`
for a single ad's planned spend):

- `< $25/day` → **Too Thin** (LinkedIn can't optimize)
- `$25-49/day` → **Watch**
- `≥ $50/day` → **Healthy**

Surface the tier next to the count so the "too many / too few" verdict is grounded in delivery, not just a ratio.

## Allocation (reallocate the budget)

1. Current split = spend share per format (spend_format / total_spend).
2. Rank formats by value: primarily **effective CPC to LP** (lower is better) and **deal influence** (if CRM),
   with TLAs as the default value leader.
3. Recommend moving budget from the worst effective-CPC-to-LP / lowest-influence formats into the best ones. Give
   an actual dollar move ("shift ~$X/mo from Video into TLAs"), not just "do more TLAs." Keep at least a small
   always-on presence in reach formats (image) unless the data screams otherwise.
