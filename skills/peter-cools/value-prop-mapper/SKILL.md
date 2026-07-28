---
name: value-prop-mapper
title: Value prop mapper
description: |
  Use this skill when you need value propositions tied to real pains — "map our value props,"
  "our messaging lists features, not value," "which benefit answers which pain." Given what a
  company sells and its buyer pains, it returns value propositions each explicitly linked to
  the pain it resolves, with the proof that backs it.
category: Research
tags: [Research, Outreach]
---

An agent that turns pains and product capabilities into value propositions that actually answer a pain — not a feature list. Every value prop must point at a specific pain it removes, or it does not ship.

## Input

- `product` — what the company sells (capabilities, outcomes).
- `pains` — the buyer pains to answer. *(If none are supplied, derive them from the product first.)*
- *(optional)* `proof` — case studies, metrics, testimonials available to cite.

## Procedure

1. **List the pains** (or derive them) in the buyer's words, not the vendor's.
2. **For each pain, write the value prop that resolves it** — the outcome the buyer gets, phrased as a change in their world, not a feature name.
3. **Link explicitly.** Each value prop names the pain(s) it answers. Any value prop with no pain behind it is a feature — drop it or find its pain.
4. **Attach proof.** Where a metric, customer, or result backs the claim, cite it; where none exists, mark the claim unproven rather than dressing it up.

## Output

`value_props[]`, each:

- `name` — the value prop in one line
- `outcome` — the change the buyer experiences
- `resolves_pains` — the specific pain(s) it answers
- `proof` — the metric/customer/result, or "unproven"

Plus `pains[]` if they were derived rather than supplied.

## What good looks like

- **Every value prop maps to a named pain.** The mediocre version is a feature list where nothing points at a problem — impressive to the vendor, invisible to the buyer.
- **Outcomes, not features.** "Cut ramp time in half," not "onboarding module."
- **Proof beats adjectives.** One cited result outweighs three superlatives; unproven claims are labeled, not disguised.
- Good output: a rep could pick any buyer pain and instantly find the one value prop that answers it.

## Rules

- MUST link every value prop to at least one pain — no orphan value props.
- MUST phrase value props as buyer outcomes, not features.
- MUST label unproven claims as unproven; NEVER invent a metric or customer.
