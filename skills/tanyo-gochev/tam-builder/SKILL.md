---
name: tam-builder
title: TAM builder
description: |
  Use this skill when the target market needs to become an actual enumerated list of companies —
  every organisation that could plausibly buy, with a verified size band, exact geography, and fit
  classification, deduplicated to one row per company. Companies only; contacts and email
  verification are a separate, later stage. Produces the company universe plus an honest coverage
  report. Trigger phrasings: "map the TAM", "build the TAM", "total addressable market", "pull
  every company", "target account universe", "who could buy this", "size the market", "list every
  company that", "refresh the TAM".
category: Prospecting
---

Applies before any contact-level work. Produces one row per company with provenance on every field, plus a statement of what the build missed.

## Companies now, contacts later

Keep these stages apart. A TAM build that drifts into finding contacts and verifying emails produces a half-finished universe and a large bill, because enrichment and verification are priced per contact and you're paying for them on companies you haven't qualified yet.

Stage one answers one question: **which companies could buy this?** Nothing else.

## Retrieve, don't infer

Every field comes from a source that actually knows it, and every field carries provenance — where it came from and how confident it is. The temptation is to infer employee count from a website's feel, or geography from a top-level domain. Inferred fields look identical to retrieved ones in a spreadsheet and quietly corrupt every downstream filter.

Deduplicate on the root domain, not the company name. Names vary by legal entity, trading style, and punctuation; domains don't.

## Build to saturation, not to a number

The completeness guarantee doesn't come from hitting a target count. It comes from running additional queries and sources until the yield of *new* domains per query goes to near zero.

Log that curve. If the run was capped — top-N per source, a budget ceiling, a rate limit — say so explicitly in the output. A truncated universe presented as complete is the single most damaging thing this process can produce, because every strategic decision downstream inherits the gap without knowing it exists.

## Report coverage honestly

Enrichment never resolves everything. On smaller or non-standard companies, a large share will come back with no verified size band. Those are **not** disqualified — they're a lower-confidence pool, kept and flagged. Deepen them only when a specific cohort needs the verified band before it's activated.

Report the verified core and the unknown tier as separate numbers. Presenting the verified count as "the market" understates it; merging the two overstates confidence. Both are wrong in ways that matter.

## What good looks like

The tell of a good operator: they know their own coverage rate on this kind of company before quoting a market size, and they state it unprompted. Anyone can produce a big number; knowing what fraction of it is verified is the actual skill.

The mediocre version is a single-source export presented as the total addressable market — clean, confident, and missing the entire long tail of companies that source doesn't index. It looks more authoritative than the honest version, which is why it survives.

Good output can be filtered directly into a campaign without further cleaning: one row per company, deduplicated on domain, every field sourced, the unknown tier separated and labelled, and a saturation log showing where the yield went dry. If a reader can't tell which numbers are verified and which are inferred, it isn't finished.

## Rules

- MUST deduplicate on root domain.
- MUST record provenance for every field.
- MUST report the verified count and the unknown-size tier separately.
- MUST state any cap or truncation in the output.
- NEVER infer a field that can be retrieved.
- NEVER run contact-level enrichment or email verification at this stage.
