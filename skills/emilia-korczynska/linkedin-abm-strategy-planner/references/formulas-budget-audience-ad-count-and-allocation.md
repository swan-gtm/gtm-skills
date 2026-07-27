---
title: "Formulas: budget, audience, ad count and allocation"
description: Reference for the LinkedIn ABM strategy planner skill.
---

# Formulas: budget, audience, ad count and allocation

Reverse-engineered from ZenABM's [ABM Budget Calculator](https://zenabm.com/free-tools/abm-budget-calculator)
and [LinkedIn Ads Count Calculator](https://zenabm.com/free-tools/linkedin-ads-count-calculator), and verified
numerically against the live tools. Compute **per audience / campaign**.

## Inputs

| Input | Source | Default |
|---|---|---|
| `revenueTarget` | asked (annual; convert MRR→ARR ×12) | — |
| `ACV` | asked (annual; convert MRR→ARR ×12) | — |
| `qualificationRate` (demo→qualified) | asked | 0.75 |
| `closeRate` (qualified→won) | asked | 0.15 |
| `landingPageCvr` (visit→demo) | asked | 0.008 |
| `CPC` | asked, or ZenABM connector | 8 |
| `monthlyBudget` (their planned spend) | asked | — |
| `clicksPerAdPerDay` | fixed | 3 |

**Normalize first.** Keep revenue and ACV on the same basis. If the user gives MRR, multiply BOTH by 12 to get
annual before running the budget formulas (the calculator is annual). Report monthly figures by dividing by 12.
Note: the calculator's **CTR input is decorative** — it is never used. Do not ask for it here.

## Budget & funnel (run the funnel backwards)

```
dealsNeeded       = round( revenueTarget / ACV )
qualifiedDeals    = dealsNeeded / closeRate
demosNeeded       = round( qualifiedDeals / qualificationRate )
clicksNeeded      = round( demosNeeded / landingPageCvr )

accountsNeeded    = round( qualifiedDeals / qualificationRate / 0.0058 )   # 0.58% baseline account→qualified rate (hidden constant)

annualBudget      = round( CPC * clicksNeeded )
monthlyBudgetReq  = round( annualBudget / 12 )

ROAS              = round( revenueTarget / annualBudget )                  # e.g. 2 -> "2x"
pipelinePerDollar = round( (qualifiedDeals * ACV) / annualBudget )         # dollars of pipeline per $1 spend
```

Collapsed: `annualBudget = CPC × (revenueTarget / ACV) / closeRate / qualificationRate / landingPageCvr`.

**Time to run the campaign** (months to accumulate the required spend at the user's pace):

```
timeToRunMonths   = ceil( annualBudget / monthlyBudget )      # actual budget needed ÷ their stated monthly budget
```

If `monthlyBudget ≥ monthlyBudgetReq`, the plan runs within ~12 months; otherwise it stretches to `timeToRunMonths`.
Surface this honestly — a small budget against a big goal just means a longer runway.

### Defaults sanity-check (matches the live tool)
revenueTarget 800,000 · ACV 20,000 · qual 0.75 · close 0.15 · LPcvr 0.008 · CPC 8 →
40 deals → 356 demos → 44,444 clicks → **$355,556/yr, $29,630/mo**, 61,303 target accounts, **2× ROAS**, **$15** pipeline-per-$.

## Audience / impressions layer (for "target audience size needed")

The budget calculator does not expose impressions. For the audience-size line, size it up from clicks with
standard ZenABM planning defaults (state them as assumptions on the doc):

```
CTRplan        = 0.006      # ~0.6% blended plan CTR (image+TLA mix); override with connector/actual if known
frequency      = 7          # impressions per member
penetration    = 0.5        # share of the target audience you realistically reach

impressions    = round( clicksNeeded / CTRplan )
membersToReach = round( impressions / frequency )
audienceNeeded = round( membersToReach / penetration )   # LinkedIn audience size to build
```

Report **audienceNeeded** as the "target audience size needed" and **accountsNeeded** (from the funnel) as the
"number of accounts needed." If the user gave a current list size, show the gap (audience implied ÷ current list).

## Ad-count model (how many ads you can run at once)

From the LinkedIn Ads Count Calculator:

```
dailyBudget        = monthlyBudget / 30
minDailyPerAd      = max( CPC * clicksPerAdPerDay, 20 )         # hard $20/day floor
maxSimultaneousAds = max( floor( dailyBudget / minDailyPerAd ), 1 )

monthlyClicksPerAd = clicksPerAdPerDay * 30
totalMonthlyClicks = monthlyBudget / CPC
```

**Algorithm-health badge** (per-ad daily spend = `CPC × clicksPerAdPerDay`):

- `< $25/day` → **Too Thin**
- `$25–49/day` → **Watch**
- `≥ $50/day` → **Healthy**

Subtext: "LinkedIn needs ≥ $25/day per ad to optimize delivery." (The tool's math floors at $20 while its copy
says $25 — we surface $25 as the guidance threshold and note the health tiers above.)

## Format allocation (how to split the affordable ads)

`maxSimultaneousAds` = the click-driving ads you can fund at once (image · TLA · video · carousel/doc).
**Text ads are excluded from this budget** (set-CPC, ~free) and always included. Allocate like this:

Targets when budget allows (aim, per audience):

| Format | Aim | Ad-set objective | Notes |
|---|---|---|---|
| **TLAs** | 5 | Website Visits | Best value; posted from a person's profile |
| **Image ads** | 5 | Engagement | The reach workhorse |
| **Text ads** | 5 | Website Visits | Always include; set-CPC, ignore budget |
| **Video ads** | 1–2 | Website Visits | Warm/nurture; 15–30s |
| **Document / Carousel** | 1 | Brand Awareness | Storytelling / lead magnet |

Rules:

1. Always include **5 text ads** (they don't consume the click budget).
2. Spend `maxSimultaneousAds` on click-driving formats in this priority: **TLA → image → video → doc/carousel**,
   up to the aims above.
3. **If `maxSimultaneousAds < 10`** (can't fund 5 TLA + 5 image separately): **group TLAs + image ads together and
   recommend the Brand Awareness objective** for that combined set, then add video/doc as budget allows.
4. If `maxSimultaneousAds` comfortably exceeds the aims, keep the aims (5/5/1–2/1) — don't inflate; suggest raising
   `clicksPerAdPerDay` or splitting audiences instead.
5. Number of **ABM campaigns** = number of distinct target audiences the user named (1 market/ICP = 1 campaign).

Show the resulting per-format counts and objectives in the Campaign Structure section and in the flowchart.

## Budget allocation per ad set (how much $ each format gets)

Split the spend across the **click-driving** formats by ad count (equal spend per ad = delivery-safe; each ad
clears the ~$25/day floor before you add another). **Text ads are excluded** — they run on a small separate
set-CPC bid, so show them as `~$0` of this budget. Show **two columns**: one at the user's stated budget, one at
the budget required to hit the goal (`monthlyBudgetReq`).

```
clickAds        = N_TLA + N_IMAGE + N_VIDEO + N_DOC          # everything except text
shareFmt        = N_fmt / clickAds                            # per format (0 if that format has 0 ads)

# Column 1 — at the user's budget:
budgetFmtYours  = round( shareFmt * monthlyBudget )           # $/mo for that format
pctFmt          = round( shareFmt * 100 )                     # % of spend (same in both columns)

# Column 2 — at the budget needed to hit the goal:
budgetFmtRec    = round( shareFmt * monthlyBudgetReq )        # $/mo for that format
```

Render each cell as `"$X/mo · Y%"` (text ads: `"~$0 · set-CPC"`; formats with 0 ads: `"—"`). Add a **Total
(click-driving)** row that sums to `monthlyBudget` (col 1) and `monthlyBudgetReq` (col 2). The **% mix is the same
in both columns** — only the dollars change; the recommended column just funds the same mix fully so the plan
lands in ~12 months instead of stretching over `timeToRunMonths`. Note in the allocation line that at the
recommended budget the ad-count model affords more ads, so they can also un-group TLA+image and add video/doc.
