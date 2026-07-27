---
name: "set-creator-benchmarks"
title: Set performance benchmarks
description: "Use this skill when setting pre-launch KPI targets for a B2B LinkedIn creator campaign. Calibrates to your own historical performance rather than generic industry percentiles, producing conservative / target / stretch bands per creator and a campaign rollup tied to the creator budget."
category: Influencers
---

# Set Performance Benchmarks

Give every campaign a defensible pre-launch target set, built from what your creators actually deliver, not generic influencer benchmarks. For B2B LinkedIn thought-leadership the metric that matters most is not raw reach but how much of that reach lands on the target buyer, so this skill targets both impressions and ICP reach, as **conservative / target / stretch** bands.

## Connectors for this skill

Optional. The skill runs from pasted inputs, but will use these if available:
- **Your campaign performance records** (spreadsheet, CRM, or analytics store) — to pull each creator's historical per-post metrics.
- **A LinkedIn or creator-analytics source** — to fetch demographics for estimating ICP reach.
- **A document tool** — to format the client-facing benchmark set.

If none are connected, gather the inputs manually in Step 0.

## Step 0 – Gather the inputs

Collect, asking the user for anything missing:
- The client / brand and the campaign scope (which creators, how many posts).
- The creator budget for the campaign.
- Historical performance for these creators or close comparables: per-post impressions, likes, comments, reposts, and link clicks where a CTA is used.
- The client's ideal customer profile (seniority, industries, company sizes), so ICP reach can be estimated.
- Any conversion tracking in place (lead-magnet, UTM'd link, landing page), so leads and cost-per-lead can be targeted.

Guiding rules for the whole exercise:
- **Calibrate off your own data, never industry percentiles.** For a creator you've run, the benchmark is their own median; for a new one, the nearest comparable in your history plus your proven ceilings.
- **Ranges, not points.** LinkedIn reach depends on the algorithm on the day, so commit to bands, never single guaranteed figures.
- **Commit to what you control, forecast what you don't.** Volume, draft timeliness, and go-live compliance are commitments; impressions, reach, and engagement are forecasts.

## Step 1 – Build the comparable set

Pull the history for each creator (or the nearest comparable). Compute a per-creator **median** for each metric, not a mean; medians are robust to the odd viral spike day. If you have no history at all, say so and mark the whole set lower-confidence.

## Step 2 – Estimate ICP reach

For each creator, estimate the share of impressions landing on the target buyer:

```
ICP reach = impressions × seniority-fit% × industry-fit% × company-size-fit%
```

Use the client's ICP definition and the creator's audience demographics. ICP reach is the headline number for a B2B campaign; always target it alongside raw impressions.

## Step 3 – Build the bands

Per creator, set **conservative / target / stretch** on each metric, then roll up to a campaign total. Cross-check the target band against the best results you've actually delivered on similar campaigns, so "stretch" is credible and "conservative" isn't sandbagged. Compute the implied blended efficiency (cost per 1,000 impressions, per click, per 1,000 ICP-reach) against the stated creator budget, and flag any target the budget can't fund.

## Step 4 – Frame for the client

Label the output "target range — indicative, not guaranteed". Separate controllable commitments (volume, compliance) from outcome ranges, so the client knows what's a promise and what's a projection.

## Output

```
PERFORMANCE BENCHMARKS — [Client], [campaign / quarter]
Creator budget assumed: [ ]   ·   [N] creators, [M] posts   ·   basis: [N] comparable posts (median)

PER CREATOR                Conservative   Target     Stretch
[Creator]  Impressions     [ ]            [ ]        [ ]
           ICP reach       [ ]            [ ]        [ ]
           Weighted eng.   [ ]            [ ]        [ ]
           Link clicks     [ ]            [ ]        [ ]

CAMPAIGN ROLLUP            Conservative   Target     Stretch
Impressions               [ ]            [ ]        [ ]
ICP reach                 [ ]            [ ]        [ ]
Cost / 1k impressions     [ ]            [ ]        [ ]
Cost / 1k ICP-reach       [ ]            [ ]        [ ]
Leads / CVR (if tracked)  [ ]            [ ]        [ ]

Controllable commitments: [posts live, drafts ahead of go-live, fixed go-live dates]
Framing: target range, indicative not guaranteed.
```

Use the user's own currency throughout. Keep this set: it's the yardstick a later quarterly or campaign review measures actuals against.

## What good looks like

- Every target traces to real comparable data or a stated proven ceiling.
- ICP reach is targeted, not just impressions.
- No number sits outside your historical range without a reason.
- The budget-to-efficiency maths is sound; no target needs a cost-per-impression the budget can't fund.
- Creators with no comparable data are benchmarked as estimates and clearly labelled as such.
