---
name: google-ads-budget-portfolio-reallocation
title: Portfolio-style budget reallocation across campaigns
description: |
  Use this skill when deciding where to shift ad budget across an existing account —
  some campaigns capped by budget, others past their efficient point, or a seasonal
  peak coming up. Produces a reallocation plan sized to a total spend envelope instead
  of an even split. Triggers: budget optimization, budget pacing, impression share
  lost to budget, shared budgets, seasonal budget planning, where to cut spend.
category: Ads
---

# Portfolio-Style Budget Reallocation Across Campaigns

Applies to an account with enough live history to compare campaigns against each
other, not to a brand-new build with no data yet.

## The play

1. Model the account as one budget envelope, not a set of independent silos. The
   question isn't "does this campaign deserve more budget" in isolation — it's
   "given a fixed total, which campaign returns more for the next dollar."
2. Read impression share lost to budget as the primary signal for underfunded
   campaigns — it directly shows demand the account is missing because the budget
   cap, not the auction, is the limit. Pair it with each campaign's marginal
   cost-per-conversion at current spend, not just its average, since averages hide
   campaigns that are efficient at low spend and expensive at the margin.
3. Cap any single reallocation at roughly 20-30% of a campaign's budget per move.
   Bigger single jumps outrun what Smart Bidding can absorb cleanly and create a
   fresh learning period right when you need stable data to judge the change.
4. Keep protected minimums outside the optimization — brand campaigns and any
   geography or line of business with a standing floor get funded first, regardless
   of where they'd rank on pure marginal return.
5. For a known short-term demand spike (a launch, a flash sale, a 1-7 day event), separate
   two different levers and don't conflate them: raising the budget cap can start
   several days early so there's headroom once demand shows up, but a conversion-rate
   seasonality adjustment should start exactly when the shift begins — never days in
   advance "to be safe" — and always carry a hard end date matched to when the event
   ends.
6. Consolidate campaigns running too little volume for reliable signal before
   optimizing across them; a marginal-return comparison built on thin data is a guess
   wearing a spreadsheet.

## What good looks like

- The best reallocation plans move budget toward impression-share-limited campaigns
  before they move budget away from anything — funding real missed demand beats
  cutting a campaign that merely looks less efficient on average.
- The common mistake is starting a seasonality bid adjustment early "just to be
  safe." That pays inflated costs for normal-intent traffic during the run-up and is
  functionally the same error as forgetting to set an end date — both quietly burn
  budget outside the window that actually mattered.
- A good plan states the size of each shift as a percentage, the signal that
  justified it, and what happens to protected minimums — a plan that just says "move
  budget to the winners" hasn't done the portfolio work.

## Rules

- MUST treat impression share lost to budget as the primary underfunded-campaign
  signal, not raw ROAS ranking alone.
- MUST cap individual budget shifts to roughly 20-30% per adjustment period.
- NEVER start a conversion-rate seasonality adjustment before the actual demand
  shift begins, and never leave one running without a hard end date.
- NEVER compare marginal return across campaigns with too little conversion volume
  for the numbers to mean anything — consolidate or wait for data first.
