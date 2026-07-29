---
name: outbound-strategy
title: Outbound strategy from intent
description: |
  Use this skill when you need an outbound targeting strategy from just a company's website —
  "build our outbound strategy," "who do we target and why now." Given a domain, it returns a
  structured foundation: ICPs, personas, pains, value propositions, and a ranked shortlist of
  intent signals to run — each signal tied to a why-now.
category: Signals
tags: [Signals, Prospecting, Research]
---

An agent that turns a single domain into the targeting half of an outbound strategy: who to go after, why they buy, and which intent signals reach them while they are in-market. It stops at foundations plus signals — messaging and campaigns are separate steps.

## Input

- `website_url` — the company the strategy is for.
- *(optional)* `market_geo`, `acv_range`, `sales_motion` (PLG / sales-led / hybrid), `icp_constraints`.

## Procedure

1. **What they sell** — category, top use cases, who it is for, pricing and motion clues. Prefer the site, docs, pricing, case studies, reviews.
2. **Who buys** — economic buyer vs. daily user; which teams feel the pain; industries named or implied.
3. **Competitors and alternatives** — direct rivals, plus the "do nothing / build in-house / spreadsheet / incumbent" alternatives, and the switching trigger.
4. **Segment into ICPs by shared buying reason**, not by firmographic label. A segment is real when its members would buy for the *same why*. Bound each one — company type, industries, employee-size bands, geographies — tightly enough that two people would build the same list from it. Rank by **fit × reachability**: a perfect-fit segment you cannot find at volume is a worse ICP than a good-fit one you can.
5. **Draw personas, one title to one persona.** Assign titles in the person's own language, not the company's org-chart language. A given title belongs to exactly one persona — if "Head of Growth" could sit in two, the personas are wrong; redraw them. Keep economic buyer, daily user, and champion distinct, and state what each cares about (buyer: outcome/ROI; user: friction; champion: looking good internally).
6. **Map value props to pains.** Take the pains in the buyer's words, and for each write the value prop that resolves it — the outcome the buyer gets, phrased as a change in their world, not a feature name. A value prop with no pain behind it is a feature: drop it or find its pain. Where a metric, customer, or result backs a claim, cite it; where none exists, mark it unproven rather than dressing it up.
7. **Shortlist signals** — 3-5 detectable signals, each with a why-now.

Label anything you cannot verify from public sources as an **Assumption** and keep it plausible.

## Output

- `icps[]` — `{name, buying_reason, company_type, industries, size_bands, geos, evidence, rank}`
  - `buying_reason` — the shared why that makes it one segment
  - `evidence` — what on the site supports it, or `"Assumption"`
  - `rank` — 1-5 (fit × reachability)
- `personas[]` — `{name, titles, role_in_deal, in_icps, cares_about}`
  - `titles` — the variants that map here; **no title repeated in another persona**
  - `role_in_deal` — economic buyer / user / champion
  - `cares_about` — the one thing that moves them
- `pains[]` — `{name, description}`
- `value_props[]` — `{name, outcome, resolves_pains, proof}`
  - `outcome` — the change the buyer experiences
  - `proof` — the metric/customer/result, or `"unproven"`
- `signals[]` — `{signal, why_now, detect_in, target, rank}` (3-5)

## What good looks like

- **Every value prop links back to a pain; every persona to an ICP.** A strategy whose pieces do not connect is decoration.
- **ICPs are segments, not filters.** Firmographics alone describe a list; the buying reason explains why that list converts.
- **No title appears in more than one persona.** Overlapping title lists silently double-target and corrupt reply-rate reads — the most common failure in practice. Good output: a targeting engine could route each title to exactly one persona with no ambiguity.
- **Titles are the person's language, not the company's.** "RevOps lead" over "Manager, Revenue Systems" if that is what they call themselves.
- **Outcomes, not features.** "Cut ramp time in half," not "onboarding module." One cited result outweighs three superlatives.
- **The intents are actually detectable in outbound** — not inbound wishes dressed up as signals.
- **Assumptions are labeled, not hidden** — a reader can see what is verified vs. inferred.
- Good output is *narrow*: a few sharp ICPs and 3-5 signals someone could act on Monday, not twelve of everything.

## Rules

- MUST give every ICP a buying reason; NEVER define one by firmographics alone.
- MUST keep every title in exactly one persona, and separate economic buyer, user, and champion.
- MUST use the person's self-description for titles, not internal org labels.
- MUST map every value prop to a pain and every persona to an ICP.
- MUST phrase value props as buyer outcomes, not features.
- MUST label unverified claims as Assumption and unbacked results as unproven; NEVER invent a metric or customer.
- MUST keep the signal shortlist to 3-5 detectable-in-outbound signals.
- NEVER pad ICPs or personas for coverage — precision over breadth.
