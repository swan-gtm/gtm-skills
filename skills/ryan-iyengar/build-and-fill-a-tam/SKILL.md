---
name: build-and-fill-a-tam
title: Build and fill a TAM
description: |
  Use this skill when a team needs a defensible total addressable market and a governed plan to cover it over time. Produces a sourced account estimate, revenue model, contact target, CRM coverage baseline, and measured population plan.
category: Prospecting
tags: [Sales, RevOps, Leadership]
---

Use this when the team needs to size a market and turn that estimate into an executable account-coverage program. Produce labeled assumptions, real account counts where possible, and a burn-up plan that never confuses loaded records with valid TAM coverage.

## Freeze the ICP definition

Write the account inclusion and exclusion rules before counting. Specify industry, company size, geography, business model, technology or operating conditions, and disqualifiers. Separate required filters from preferences and mark which filters can actually be measured by each source.

Define the unit of analysis. Count companies, not people, when estimating account TAM. Decide how subsidiaries, franchises, agencies, parent companies, and multi-brand groups are treated. Preserve one canonical domain per operating account and document exceptions.

## Estimate the account universe

Prefer a bottom-up count from a source capable of returning the matching companies. Record the source, query date, applied filters, omitted filters, caps, sampling, and estimated duplication. If the source exposes only a count, label the result as a count estimate rather than a verified account list.

Cross-check with a second method: industry registry, known-account sample, CRM classification, or another data source. Investigate large differences instead of averaging incompatible populations. A provider cap is a floor, not the size of the market.

Use [references/tam-model.md](references/tam-model.md) for the calculation and uncertainty bands.

## Add revenue and contact targets

Use a real annual contract value: the median or trimmed mean of comparable closed-won deals, annualized from the recorded contract period. Do not substitute a price-page maximum or an unlabeled band.

Calculate:

- account TAM = eligible accounts;
- revenue TAM = eligible accounts × annual contract value;
- contact target = eligible accounts × required buying roles per account.

Report the sources for each number independently. CRM presence can measure coverage; it does not establish annual contract value unless closed-won data is explicitly used.

## Measure current coverage

Classify CRM accounts as in-TAM, out-of-TAM, or unknown against the same ICP. Only in-TAM accounts count toward coverage. Unknown records expose missing data; out-of-TAM records are not progress merely because they exist.

Deduplicate accounts by stable identity before measuring. Report account coverage, contact coverage, and role coverage separately. An account with one irrelevant contact is not fully covered.

If verified in-TAM accounts already exceed the estimated universe, treat the estimate as a floor and revise it upward. Do not force the CRM count down to preserve the original story.

## Fill the gap in governed batches

Prioritize uncovered accounts by ICP strength and evidence quality. Resolve identity before creating records. Every proposed account should include source, domain, fit evidence, owner, and acquisition cost where applicable. Every proposed contact should link to a resolved account and required buying role.

Plan small batches, review cost and sample quality before acquisition, and require approval before records are created. Track attempted, resolved, created, rejected, and ambiguous records. Schedule research and planning freely; keep creation and spend gated.

Read [references/worked-tam.md](references/worked-tam.md) for a model that is revised when CRM evidence exceeds an initial capped estimate.

## Track burn-up honestly

Save dated coverage snapshots using the same definitions. Calculate net new verified in-TAM accounts per period and project time to target only after at least three comparable observations. Show losses from deduplication, disqualification, and stale contacts.

## What good looks like

- Every number names its source, date, unit, and major limitation.
- Account, revenue, contact, and role coverage are not conflated.
- The CRM is classified against the ICP instead of counted wholesale.
- Provider caps and missing filters appear as uncertainty, not false precision.
- Population batches are deduplicated, owner-stamped, costed, and approved.
- The estimate changes when stronger bottom-up evidence contradicts it.

The mediocre version multiplies an arbitrary database count by aspirational pricing, calls every CRM account covered TAM, and buys a large list without resolving identities or measuring role depth.

## Rules

- MUST define the ICP and counting unit before estimating.
- MUST use a confirmed annual contract value and label every source.
- MUST resolve records and review spend before acquisition or creation.
- NEVER treat a capped result as the full universe.
- NEVER count unknown or out-of-TAM CRM records as coverage.
- NEVER project an ETA from fewer than three comparable snapshots.
