---
name: icp-matrix-builder
title: ICP matrix builder
description: |
  Use this skill when targeting needs to become a decision rule instead of a description — before
  launching outbound for a new company or product line, when refining targeting after the first
  campaign data lands, when expanding into a new vertical, or when a list is producing replies from
  people who will never buy. Produces a scored, tiered ICP matrix that a list build can be filtered
  against and that anyone on the team can apply the same way twice. Trigger phrasings: "define our
  ICP", "who should we target", "build the ICP", "tier these accounts", "score this list", "our
  leads are bad", "we're getting replies but no deals", "which segment do we go after".
category: Prospecting
---

Applies before any list gets built or bought. Produces a scored, tiered matrix that turns targeting from an opinion into a filter.

## Default-deny, not default-allow

Most ICP work starts from "who could buy this" and subtracts. That produces a large list with a fuzzy edge, and the fuzzy edge is where the budget dies.

Invert it: **an account is out until it earns its way in.** Every dimension is a gate that must pass, not a point that gets added to a total. A high score on four dimensions never rescues a fail on the fifth — a company with perfect firmographics and no budget is not a 4/5, it's a no.

Order the gates cheapest-first, so the expensive ones only ever run on survivors:

1. **Structural fit** — size band, stage, model, geography. Free or near-free to check.
2. **Problem evidence** — something observable says they have the problem you solve. Not "they could have it."
3. **Exclusions** — competitors, current clients, prior contact, people who sell what you sell. Run this early; it's cheap and it prevents the most embarrassing sends.
4. **Reachability** — can you actually get to the buyer? An unreachable perfect fit is worth zero.
5. **Deal size** — can they pay your floor? Put this gate before enrichment spend, not after.
6. **Timing signal** — is the buying window open, or is this a nurture entry?

Spend and send are the *last* gates, never the first.

## Build the matrix

For each dimension, write the gate as a binary question with a stated source, then a tier rule on top of the survivors:

- **Tier 1** — passes every gate plus an active timing signal. Worth manual research and a custom asset.
- **Tier 2** — passes every gate, no timing signal. Worth a templated, segment-level motion.
- **Tier 3** — passes structural fit only. Nurture. Never the target of paid enrichment.

Anything failing a gate is excluded with the reason recorded. The exclusion log is more useful than the include list — it's what stops the same bad accounts re-entering next quarter.

## Anchor it to closed-won, then to closed-lost

Start from the accounts that actually paid, not from the deck. Look for the attribute that the winners share and the near-misses don't. Then check it against deals you lost late — a dimension that both winners and late losers share isn't a qualifier, it's table stakes, and scoring on it just inflates everyone equally.

## What good looks like

The tell of a good operator: they can state the *disqualifier* before the qualifier. Anyone can describe a dream customer; knowing precisely who to throw away, and being willing to throw away most of the market, is the skill.

The mediocre version is a persona document — a paragraph about "innovative mid-market leaders who value efficiency" that no one can filter a list against. If two people can't independently score the same twenty accounts and land in the same tiers, it isn't a matrix, it's a mood.

Good output is falsifiable: every dimension names its data source, every gate is answerable yes or no by someone who has never met the customer, and the matrix predicts the last ten closed-won accounts as Tier 1 or 2. If it doesn't retro-predict your own wins, it won't predict the next ones.

## Rules

- MUST make every dimension a gate with a named data source, not a subjective rating.
- MUST place deal-size and exclusion gates before any paid enrichment step.
- MUST record the reason for every exclusion.
- NEVER let a strong score on one dimension override a failed gate on another.
- NEVER ship a matrix that can't be applied identically by two different people.
