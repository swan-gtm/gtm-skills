---
name: market-finder
title: Market finder
description: |
  Use this skill when you need to enumerate every business of a given type in a
  geography — "find all X in Y", "build a list of", "market sizing", "account
  universe", "how many X in Y", "TAM for", "discover all", "prospect list" — or
  when you already have a list and want it checked: "audit my list", "compare
  against", "what am I missing", "gap analysis", "verify my business list".
  Produces a deduplicated, source-linked market inventory with a confidence
  score per entity; in audit mode, a three-way comparison of your list against
  fresh discovery (matched / discovered-only / reference-only) with a coverage
  score. Not for monitoring known competitors over time or deep-diving a single
  company — this play is for mapping a whole market.
category: Prospecting
tags: [Sales]
---

# Market finder

Runs when someone needs the full universe of businesses of one type in one geography — for territory planning, TAM sizing, list building, or checking an existing account list for gaps.

Produces a deduplicated entity list with per-entity strength scores and mandatory source links; in audit mode, your list categorized against fresh discovery with a coverage percentage.

## The play

### 1. Detect the mode

Two modes, and the difference is whether the user handed you a list:

| Signal | Mode |
|--------|------|
| Spreadsheet link, CSV file, or inline list of 3+ businesses | **Audit** |
| Explicit audit language ("audit my list", "compare against", "gap analysis") | **Audit** |
| No reference list | **Discovery** (default) |

If a list is present but intent is ambiguous, ask: "Want me to audit your list against fresh discovery, or use it as a starting point?" If audit language appears but no list does, ask for the list — never run an audit against an imagined reference.

### 2. Scope the request

Extract: business type (required), geography (required — except software/SaaS markets, which are not geography-bound), qualification criteria (optional: "must have a website", "10+ reviews"), and depth. If type and geography are both clear, confirm in one line and go; if not, ask one combined question — never a drip of clarifications.

Two depth modes: **quick scan** (one discovery pass over all sources, enrich only the top 5, verify only the top 5) and **comprehensive** (all sources with retries, full enrichment, verify everything). Default to quick scan unless the user signals they want the complete universe.

### 3. Load the vertical preset

Read `references/vertical-presets.md` and match the business type against preset trigger keywords (Healthcare, SaaS/Software, Restaurants, Legal/Financial, Auto/Home Services, Custom fallback). The preset tells you which sources to search, in what priority order, what query pattern to use per metro, and whether the vertical is geographic at all. A partial match gets confirmed ("This looks like Healthcare — use healthcare sources?"); no match falls through to the Custom preset with the user's own keywords.

### 4. Tile the geography

Skip for SaaS. Otherwise:

| Geography | Tiling |
|-----------|--------|
| City | Single query set |
| Metro area | Single query set per source |
| State | Top 5–10 metros in the state |
| Region | States, then top metros per state |
| Nationwide | All states, then top metros per state |

Estimate the total work before starting: `metros × discovery sources × (1 + ~0.3 enrichment ratio)`. A nationwide comprehensive run is thousands of lookups — state the estimate and get an explicit go-ahead before launching anything that large. Derive a market slug (`dentists-florida`, `hvac-nationwide`) and keep a working file per slug in your workspace; save intermediate results after each phase so a long run can resume instead of restarting, and so a repeat run can load prior entities and only chase what's new (new metros, new entrants) rather than re-discovering everything.

### 5. Discover

For each metro in the tiling plan, run the preset's discovery queries against its sources in parallel — primary source first (maps-style listings), secondary (review directories), tertiary only when the first two return fewer than ~10 combined unique results for that metro. When a structured source is unavailable or fails, fall back to a plain web search for `"{type} in {metro}"` — partial data beats none; never abort a whole run for one empty metro.

SaaS discovery is different: two parallel search passes, no geography. Pass 1 finds the players (software review directories, "best {vertical} software" roundups, launch platforms, open-source repos); pass 2 finds the money (funding databases, funding news, market-landscape pieces). Pass 2 is not optional — without it, funding and traction data will be missing or wrong.

Then deduplicate in strict key order: place identifier → root domain → fuzzy name + city. Merge fields across sources into one record per entity and track `source_count` — how many independent sources found it. That count is the backbone of scoring.

### 6. Enrich and verify

Enrich highest-`source_count` entities first, using the preset's enrichment targets (review volume, accreditation, complaint history, funding profile). Skip entities missing the identifier the enrichment source needs.

For SaaS, run a financial verification pass on top entities: search `"{company} funding raised series"` and use only sourced amounts and dates. **No source found → report "Undisclosed."** Never guess "early stage" or "bootstrapped" — an unverified funding label is worse than an honest blank.

### 7. Score

Strength is earned by independent corroboration, not by any single listing:

Geographic verticals — **High:** 3+ sources, or 2+ sources with >50 reviews. **Medium:** 2 sources, or 1 source with >10 reviews. **Low:** 1 source, few/no reviews.

SaaS — **High:** verified funding >$10M, or 3+ directory sources, or 1000+ reviews on a major software directory. **Medium:** verified funding <$10M, or 2 sources, or 100+ reviews. **Low:** 1 source, no verified funding.

### 8. Audit comparison (audit mode only)

Read `references/audit-mode.md` for the full parsing rules, normalization, and matching algorithm. In short: normalize every reference record to `{name, domain, city, state, phone}`, then match in three layers — exact root-domain, fuzzy name + same city at an 80% word-overlap threshold, then normalized phone. First match wins; record which layer matched. Categorize everything as `matched`, `discovered_only` (expansion candidates), or `reference_only` (coverage gaps), and compute the coverage score: `matched / reference_count × 100`. A 0% score is a valid, informative result — report it, don't retry until it looks better.

### 9. Report

Follow `references/output-formats.md` — discovery format, SaaS tier-grouped variant, and audit variant. Non-negotiable: **every entity carries at least one clickable source URL.** Save the report and the structured entity data to the market slug's workspace files, then offer natural follow-ups: filter, expand geography, export the discovered-only set for outreach, or investigate reference-only gaps to see who closed, moved, or rebranded.

## What good looks like

- The best operator scopes cost before spending it: the nationwide estimate is on the table before the first query fires, and the user chose comprehensive knowingly. The mediocre version discovers halfway through that the job is 10× bigger than anyone wanted.
- Strength scores mean something: a High entity was independently confirmed by multiple sources, not enthusiastically listed once. If most of your list is single-source Low, say so in "What's missing" instead of dressing it up.
- SaaS funding claims all trace to a source or read "Undisclosed". The mediocre version copies a stale directory figure and labels a Series C company "early stage".
- In audit mode, the interpretation earns the run: "82% coverage; your gaps cluster in Orlando; three reference-only entries appear to have closed" — not just three tables.
- Dedup held: no business appears twice under name variants, because domain matching ran before fuzzy names and suffixes ("LLC", "Associates", "DDS") were stripped before comparing.
- A repeat run surfaces the delta — new metros, new entrants — instead of re-presenting last month's list as fresh discovery.

## Rules

- MUST attach at least one source URL per entity in every output. An entity nobody can verify doesn't ship.
- MUST get explicit approval before launching a large run (nationwide or multi-state comprehensive), and before any bulk export intended for outreach.
- MUST deduplicate in key order (place identifier → domain → fuzzy name+city) before scoring — scores on a duplicated list are fiction.
- MUST report unverifiable funding as "Undisclosed". NEVER fabricate or infer a funding stage.
- NEVER run audit mode without an actual reference list in hand.
- NEVER abort an entire discovery run because one metro or one source returned nothing — log the gap and continue.
- NEVER present a stale prior run as fresh discovery; either refresh it or label its date.
