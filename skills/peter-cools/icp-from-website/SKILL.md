---
name: icp-from-website
title: ICP from website
description: |
  Use this skill when you need to define or tighten an ICP from a company's website —
  "who should we actually target," "build our ICP," "our ICP is too broad." Given a domain,
  it returns a small set of sharp, evidence-backed ICP segments (company type, industries,
  size bands, geographies), each ranked by fit and reachability.
category: Research
tags: [Research, Prospecting]
---

An agent that turns a company's website into a short set of ICP segments precise enough to build a target list from. It works backward from what the product sells and who is shown buying it — never a generic "mid-market B2B" label.

## Input

- `website_url` — the company whose ICP you are defining.
- *(optional)* `constraints` — known limits (geo, size, industry, compliance) to respect.

## Procedure

1. **Read what the product does** and, crucially, *who it is shown serving* — customer logos, case studies, testimonials, pricing tiers, industry pages. Evidence beats assertion.
2. **Cluster the buyers** into segments that share a buying reason, not just a firmographic label. A segment is real when the members would buy for the *same* why.
3. **Bound each segment** — company type, industries, employee-size bands, geographies. Tight enough that two people would build the same list from it.
4. **Rank by fit × reachability** — a perfect-fit segment you cannot find at volume is a worse ICP than a good-fit one you can.

Label any segment inferred (not evidenced on the site) as an **Assumption**.

## Output

`icps[]` — 2 to 5 items, each:

- `name` — the segment in plain language
- `company_type`, `industries`, `size_bands`, `geos`
- `buying_reason` — the shared why that makes it one segment
- `evidence` — what on the site supports it (or "Assumption")
- `rank` — 1-5 (fit × reachability)

## What good looks like

- **Sharp and few.** Two to five segments a rep could each build a list from — not a paragraph that means "anyone."
- **Evidence-backed.** Every segment points at something real on the site; inferred ones are labeled.
- **Segmented by why, not just size.** The mediocre version splits by headcount alone and misses that two same-size companies buy for opposite reasons.
- Good output: you could hand any segment to a list-builder and get a coherent set of accounts back.

## Rules

- MUST return a small set (2-5), never one catch-all ICP.
- MUST tie each segment to on-site evidence or label it an Assumption.
- MUST bound each segment concretely enough to build a list from.
- NEVER define an ICP by firmographics alone — always include the buying reason.
