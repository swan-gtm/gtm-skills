---
name: google-ads-ppc-math
title: PPC forecasting and unit-economics math
description: |
  Use this skill when someone asks for a budget projection, a ROAS or CPA target, an
  impression-share opportunity estimate, or any paid-search math from numbers they
  already have — no live account access needed. Produces a shown-work table with a
  sensitivity check, not just a final number. Triggers: budget projection, ROAS
  calculation, CPA target, conversion forecast, impression share opportunity,
  break-even ROAS, "what would happen if."
category: Ads
---

# PPC Forecasting and Unit-Economics Math

Applies any time the question is really arithmetic wearing a strategy question's
clothes — someone wants to know what a number implies before committing spend to it.

## The play

1. Work from whatever inputs are actually given, and state which core rates you
   derived them from: CPA (spend ÷ conversions), ROAS (revenue ÷ spend), CTR (clicks
   ÷ impressions), CPC (spend ÷ clicks), CVR (conversions ÷ clicks). Every downstream
   projection is built from these five.
2. For a budget or conversion forecast, chain the rates forward explicitly: daily
   clicks from budget and CPC, daily conversions from clicks and CVR, then scale to a
   monthly figure using an average month length (roughly 30.4 days) rather than a
   flat 30 — the drift compounds over a full year of planning.
3. For a target gap (hitting a CPA or ROAS goal), show the distance three ways: where
   the account is now, what's required to hit the target, and the specific delta in
   conversions or revenue needed to close it — not just "you're below target."
4. For impression share opportunity, translate the missed share into missed clicks
   and missed conversions using the account's own CTR and conversion rate, not an
   assumed industry rate — the whole point is showing what the account's actual
   funnel would produce with more visibility.
5. Always run the sensitivity check nobody asked for: "if CPC rises 20%, your CPA
   becomes X." A single-point forecast without a stress case invites false confidence
   the moment reality drifts from the input.
6. Flag inputs that don't pass a sanity check before running them forward — a CTR
   above what's plausible for the format, or a CPA implausibly low for a non-branded
   term, will just launder into an equally implausible forecast if you don't stop and
   ask about it first.

## What good looks like

- The best version of this always shows the formula and the inputs next to the
  result — a table with just a final number invites "how did you get that" and
  erodes trust the first time someone tries to reproduce it.
- The common mistake is running a forecast on inputs that were never sanity-checked,
  producing a precise-looking number built on an impossible assumption. Catch the
  impossible input, don't just compute through it.
- Good output pairs every headline number with its sensitivity — a forecast that
  can't say what happens if one input moves 20% isn't a forecast, it's a guess with
  extra decimal places.

## Rules

- MUST show the formula and inputs alongside every calculated result, not the result
  alone.
- MUST use a full-year average (≈30.4 days/month) for monthly projections, not a
  flat 30.
- NEVER present a single-point forecast without at least one stated sensitivity case.
- NEVER silently run an implausible input through a formula — flag it and ask before
  projecting from it.
