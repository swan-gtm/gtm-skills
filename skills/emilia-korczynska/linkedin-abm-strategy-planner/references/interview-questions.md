---
title: Interview questions
description: Reference for the LinkedIn ABM strategy planner skill.
---

# Interview questions

Ask in small batches. Offer defaults as selectable options so the user can accept with one tap. Numeric answers
only where possible. If the ZenABM connector is available, prefill CPC/CTR, prior spend and audience size and skip
those asks.

## A. Company (1 — you research the rest)
- **What's your company website?** → you fetch it and draft product, use cases, personas, ICP and jobs-to-be-done.
  The user only confirms/edits. *(Also grab the company name for the title.)*

## B. Goals & deal economics (drives the math)
1. **What's your ABM revenue goal, and is it monthly (MRR) or annual (ARR)?** (per audience if more than one)
2. **Average contract value (ACV)?** — total contract value or MRR (state which).
3. **Close rate** (qualified → closed-won)? — *default 15%*
4. **Qualification rate** (demo → qualified)? — *default 75%*
5. **Landing-page conversion rate** (visit → booked demo/form)? — *default 0.8%*

## C. Budget & metrics
6. **Average LinkedIn CPC?** — *default $8; skip if the ZenABM connector is available (pull real CPC)*
7. **Planned monthly LinkedIn ads budget?**

## D. Audiences & content
8. **Which target audiences / markets are in scope?** (geo + industry) — sets the number of campaigns. Seed from
   the website research and have them confirm the list.
9. **Top jobs-to-be-done / use cases per audience, and the core problem you solve?** — pre-fill from research; edit.

## Defaults not asked (advanced only)
Clicks/ad/day = 3 · frequency = 7 impressions/member · audience penetration = 50% · account→qualified baseline
= 0.58% · plan CTR ≈ 0.6%. Per-format CTR/CPC/CPM benchmarks come from ZenABM's 2026 report (see the Best
Practices reference).

## If the ZenABM connector is available
Call `get_linkedin_metrics` (CPC, CTR, spend), `get_ad_spend`, and `list_companies` / audience tools to prefill
CPC, prior spend and current list size. Tell the user which numbers you pulled vs. assumed.
