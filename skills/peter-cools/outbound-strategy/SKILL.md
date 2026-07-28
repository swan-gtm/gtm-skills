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

An agent that turns a single domain into the targeting half of an outbound strategy: who to go after, why they buy, and which intent signals reach them while they are in-market. It stops at foundations plus signals — messaging and campaigns are separate steps. It composes the ICP, persona, value-prop, and signal agents; run those standalone for one section, or this for the whole foundation.

## Input

- `website_url` — the company the strategy is for.
- *(optional)* `market_geo`, `acv_range`, `sales_motion` (PLG / sales-led / hybrid), `icp_constraints`.

## Procedure

1. **What they sell** — category, top use cases, who it is for, pricing and motion clues. Prefer the site, docs, pricing, case studies, reviews.
2. **Who buys** — economic buyer vs. daily user; which teams feel the pain; industries named or implied.
3. **Competitors and alternatives** — direct rivals, plus the "do nothing / build in-house / spreadsheet / incumbent" alternatives, and the switching trigger.
4. **Translate to targeting** — derive ICPs, personas, pains, value props (each mapped to a pain), and the intent signals detectable in outbound.
5. **Shortlist signals** — 3-5 detectable signals, each with a why-now.

Label anything you cannot verify from public sources as an **Assumption** and keep it plausible.

## Output

- `icps[]` — `{name, company_type, industries, size_bands, geos}`
- `personas[]` — `{name, titles, in_icps}`
- `pains[]` — `{name, description}`
- `value_props[]` — `{name, resolves_pains}`
- `signals[]` — `{signal, why_now, detect_in, target, rank}` (3-5)

## What good looks like

- **Every value prop links back to a pain; every persona to an ICP.** A strategy whose pieces do not connect is decoration.
- **The intents are actually detectable in outbound** — not inbound wishes dressed up as signals.
- **Assumptions are labeled, not hidden** — a reader can see what is verified vs. inferred.
- Good output is *narrow*: a few sharp ICPs and 3-5 signals someone could act on Monday, not twelve of everything.

## Rules

- MUST map every value prop to a pain and every persona to an ICP.
- MUST label unverified claims as Assumption.
- MUST keep the signal shortlist to 3-5 detectable-in-outbound signals.
- NEVER pad ICPs or personas for coverage — precision over breadth.
