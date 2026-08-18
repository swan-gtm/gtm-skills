# Company memory and differential analysis

Keep one running file per researched company in your workspace (e.g. `memory/companies/[company-slug].md`), plus the full timestamped report per run (e.g. `memory/reports/company-deep-dive-[company-slug]-[YYYY-MM-DD].md`). The memory file is what makes the second run on a company worth more than the first: it turns a repeat deep dive into a changelog.

## Company profile format

Structured key facts up top, dated signal entries below — newest first:

```markdown
# Target Corp

## Overview
- Industry: Enterprise SaaS | Founded: 2015 | HQ: Austin, TX | ~500 employees
- Domain: targetcorp.com
- Last researched: [date of most recent run]

## Financials
- Last funding: Series B ($30M, Sep 2025) | Revenue: est. $40M ARR (inferred)

## Leadership
- CEO: [name] | Notable: [key hires/departures with dates]

## Products
- [core products, one line each]

## Signals
### [YYYY-MM-DD]
- [signal] — [source URL]
### [YYYY-MM-DD]
- [signal] — [source URL]
```

Keep cross-references to related entities you also track — key people, competitors in the same space — so adjacent research can load the connected context.

## Dedup lifecycle

Memory is loaded at two points in every run:

1. **Before research:** load the company's file and pass its known facts to every dimension thread, so threads hunt only for what is not already known.
2. **Before writing the report:** final dedup pass — compare every finding against memory. Only signals classified NEW or UPDATED (per the freshness rules in the signal-dating reference) make it into the report.

## What "new" means

- "Raised a Series C" is **noise** if it is already in memory.
- "Just hired a new CTO" is a **new** signal worth surfacing.
- "Raised a Series C" with a detail memory lacks (amount, lead investor) is an **update** — surface only the new detail.

## After each run

- Append the run's NEW/UPDATED signals to the profile's Signals section (dated).
- Update the structured key facts where they changed (headcount, last funding, leadership).
- Save the complete report — the full text, not a summary — to the reports location.
- When the reader corrects a fact ("that ARR figure is wrong"), fix the memory file immediately and confirm the correction — memory errors compound across every future run.
