---
name: website-to-signals
title: Website to signals
description: |
  Use this skill when you have a company's website and need a shortlist of intent signals
  worth running for them — "which buying signals fit this business," "turn this URL into a
  signal plan." Given a website, it returns 3-5 detectable intent signals, each tied to a
  concrete why-now, with where to detect it and who to target.
category: Signals
tags: [Signals, Prospecting]
---

An agent that turns a company's website into a short, operable set of intent signals. It reasons from what the company sells to what has to change in a buyer's world for them to need it now, then keeps only the changes it can actually observe in public data.

## Input

- `website_url` — the company to plan signals for (read the homepage, product, pricing, customers, blog).
- `icp_constraints` *(optional)* — known segment / geo / size limits.
- `sales_motion` *(optional)* — PLG / sales-led / hybrid; shifts which signals matter.

## Procedure

1. **Extract three things from the site:** what they sell, who buys (economic buyer vs. daily user), and — the pivot — what has to become true in an account for them to need this *now*.
2. **Turn each why-now into an observable proxy.** A trigger is a signal only if it is visible in public data. "Just hired their first RevOps lead" is observable; "frustrated with their tool" is not. Keep the observable ones.
3. **Map to signal families:** people moves (job changes, new leadership, hiring a role), company moves (funding, expansion, new market or entity), competitive engagement (evaluating an alternative), social and behavioral (posting or reacting on the problem), technographic (a tool added or dropped).
4. **Rank and cut to 3-5** by fit × intent strength × volume. Drop anything undetectable, low-volume, or really inbound.

## Output

`signals[]` — 3 to 5 items, each:

- `signal` — the observable event
- `why_this_company` — one line linking it to what they sell / who buys
- `detect_in` — where it is observed in public data
- `target` — the persona + firmographic filter to apply
- `rank` — 1-5 (fit × intent × volume)

## What good looks like

- **Starts from the buyer's why-now, never a signal menu.** The weak version: a dozen signal types picked because they sound good, half inbound-only or unobservable.
- **Detectability is the gate** — every item passes "can I see this in public data, at volume, today?"
- **Intent strength beats novelty** — a boring signal that reliably precedes a purchase beats a clever one that rarely does.
- Good output: each signal has a concrete why-now, and you could pull fifty matching accounts this afternoon.

## Rules

- MUST return 3-5 signals, never a long menu.
- MUST tie each signal to a specific trigger for *this* business.
- NEVER include a signal you cannot detect from public data at volume, or one that is really inbound.
