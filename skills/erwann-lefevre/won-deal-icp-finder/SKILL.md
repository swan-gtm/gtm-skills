---
name: won-deal-icp-finder
title: Won-deal ICP finder
description: |
  Use this skill when someone wants to know who actually pays them — auditing closed-won deals to
  derive a proven ideal customer profile instead of an aspirational one, then building a look-alike
  target list from it. Produces a revenue-ranked deal table, two to four named ICP archetypes with
  searchable criteria, and a ranking of the acquisition sources that produced the money. Trigger
  phrasings: "audit my biggest deals", "which customers made us the most money", "analyse my
  closed-won", "what's my real ICP", "find more customers like my best ones", "look-alike accounts",
  "revenue by account", "which channel produced our best deals", "ICP refresh before planning".
category: Prospecting
tags: [RevOps, Sales]
---

Applies when the ICP on the slide was written before the revenue arrived. Produces a proven profile, derived from deals that closed, plus the search criteria to find more of them.

## Most stated ICPs are aspirational

Teams write their ICP at the start, from the market they want. Then they close deals, and the deals quietly disagree — smaller, in an adjacent vertical, in a country nobody targeted. Nobody rewrites the slide, so prospecting keeps aiming at the market that never paid. This skill re-derives the profile from the ledger instead of the plan.

## Select on money, not on stage names

The first move is picking which deals count, and it is where this play usually breaks.

The obvious approach — filter on a "Closed Won" stage — assumes a stage that a surprising number of pipelines don't have, or don't use consistently, or spell in another language. When it silently matches nothing, the fallback is worse: pull the most recent deals instead, which are the newest and emptiest ones, and the analysis runs on rows with no value in them.

Select on **deal value being populated**, over the last twelve months. A won signal, where one genuinely exists, is a filter you add on top — not the thing you rely on. Read the CRM's own conventions before pulling anything: which field actually holds value (the standard amount field is often abandoned in favour of a custom ARR or ACV one), and whether a won status exists at all. If you can't tell, ask one specific question and stop. Guessing here doesn't produce a slightly-off answer, it produces a confident answer about empty rows. See `references/deal-data-extraction.md` for the field-discovery sequence, the CSV fallback, and how to keep the pull bounded.

## Do the arithmetic in code

Sums, revenue shares, concentration ratios, and frequency rankings across a hundred-odd deals are exactly the work a language model gets quietly and unfixably wrong — and a wrong ranking sends a team after the wrong accounts for a quarter.

`scripts/analyze.py` does the counting. It parses both European and US amount formats, applies the window, excludes lost deals always, detects a won signal when present, aggregates revenue per company, and returns segments and source rankings as JSON. Run it, then reason over what it returns. It refuses rather than improvises when it can't find a value field, a company, or any deal in the window — a refusal is a question for the user, not a problem to code around. `references/analysis-engine.md` covers the flags, the output schema, and how to read each block.

The judgment — which companies form a coherent archetype, whether a source ranking can be trusted, what to flag — is the part that stays yours.

## Cluster on revenue, not on logos

Group the companies behind the top deals into **two to four** named archetypes, built by intersecting the revenue-dominant industry, size and geography segments: "mid-market FinTech in FR/DE", not "B2B in Europe". Each needs objective criteria a search can consume — one or two values per dimension, a typical deal size, and how many won companies fit.

Read revenue share, never deal count. Three large deals in one vertical beat twenty small ones in another, and counting logos rewards whichever segment is cheapest to sell to. Above roughly a quarter of revenue in a single account, you have a whale rather than a pattern — say so plainly instead of building an archetype around one customer.

Before promoting any segment to an archetype, count the distinct companies inside it. A segment can sit third on the revenue table and consist entirely of one customer who renewed; the table makes it look like a market and it isn't. Fewer than two companies means concentration to report, not a profile to search. Past four archetypes you are slicing noise; collapse the thin ones. The clustering rubric, the anti-pattern table and a worked example are in `references/archetype-clustering.md`.

## Then say where they came from

Rank the acquisition sources behind these deals by frequency, with the revenue attached. Report the coverage alongside the ranking: below about 70% of deals carrying a source, the ranking is a sample, and should be described as one.

Most CRMs carry the channel but not the campaign — you learn that outbound worked, not which sequence worked. That gap is worth naming explicitly, because it's the difference between knowing a channel pays and being able to scale the thing inside it that paid.

## What good looks like

The tell of a good operator: before touching the data they ask how this team marks a won deal, and they don't assume the answer is a stage. They know their own pipeline has three abandoned value fields and one real one, and they check which is which — because everything downstream inherits that choice.

The mediocre version ranks accounts by deal count, produces five or six archetypes that are really just a list of the biggest customers with the serial numbers filed off, and quotes a channel ranking built from the 40% of deals that happened to have a source filled in. It reads as rigorous and points at the wrong market.

Good output is falsifiable. Every archetype names the companies it was built from and how many there were, every rate carries its denominator, and anything inferred rather than observed — a buyer persona the CRM never recorded — is labelled as inferred. If the profile can't be handed to someone building a prospecting list and used without further interpretation, it isn't finished.

## Rules

- MUST select deals on a populated value field, never on the assumption that a won stage exists.
- MUST run the aggregations in code and reason over the result, never total revenue by reading rows.
- MUST state the selection basis when no won status was found, and confirm it maps to what the team calls won.
- MUST report source coverage next to any acquisition ranking, and label inferred attributes as inferred.
- MUST count the distinct companies behind a segment before turning it into an archetype.
- NEVER rank or cluster by deal count.
- NEVER build an archetype from firmographics the data didn't carry — an absent dimension is a gap to flag, not a blank to fill.
- NEVER present a single dominant account as a repeatable profile.
