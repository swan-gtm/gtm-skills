# Signal dating, source hierarchy, and verification

High-quality intelligence requires distinguishing between when a **page was published** and when the **underlying event occurred**. Syndicated and republished content carries a different publication date than the original; secondary coverage (regulatory filings, recap articles, industry roundups) reports on events weeks or months after they happened. Treating article dates as event dates is how a report calls a year-old funding round "news".

## Article date vs event date

Every signal carries two dates:

| | What it is |
|---|---|
| **Article date** | When the page was published |
| **Event date** | When the underlying event actually happened |

A signal is "new" only if its **event date** falls within the freshness window.

## Event-date extraction rules

Determine the event date from the content itself, in this order:

1. **Explicit past reference** — "launched in Q3", "appointed last October" → the event date is in the past, regardless of the article date.
2. **Temporal language** — "last quarter", "months ago", "earlier this year" → resolve relative to the article date.
3. **Present-tense announcement** — "today announces", "is launching" → event date ≈ article date.
4. **Dateline** — "NEW YORK, March 15 —" → event date = the dateline date.
5. **Still ambiguous** → extract the source page and check the on-page date.

Date filters on search queries reduce noise, but they filter by article date — always validate the event date from content. For news queries, consider a parallel undated query to surface the original source alongside the fresh coverage.

## Source-type hierarchy

When the same event appears in multiple sources, prefer the one closest to the event:

1. **PRIMARY** — the company's own domain, official press release, regulatory filing
2. **Wire service** — AP, Reuters, Bloomberg (record as MAJOR)
3. **MAJOR** — original reporting with bylines at a major outlet
4. **DERIVATIVE** — syndicated copies, aggregator sites, recap articles, anything that attributes its information to another source

If the only source for a signal is derivative, corroborate against a primary or major source before reporting it.

## Freshness classification

After determining the event date, classify each signal:

| Classification | Meaning | Action |
|---|---|---|
| **NEW** | Event date within the freshness window, not in company memory | Include in report |
| **UPDATED** | Known event with genuinely new information (amount, lead investor, a named exec) | Include as an update |
| **STALE** | Old event covered by a fresh article | **DROP — do not include** |
| **UNCERTAIN** | Event date undeterminable from the snippet | Extract the page to verify; still uncertain → **DROP** |

**Hard rule:** only NEW and UPDATED signals may appear in reports. STALE and UNCERTAIN signals are dropped entirely — not downgraded, not footnoted, not kept as "background context". If a signal can't be verified as genuinely current, it doesn't exist as far as the report is concerned.

## Verification budget

Not every signal deserves a full-page extraction. Budget verification by impact:

| Priority | Signal types | Verification |
|---|---|---|
| **P1** (high impact) | Funding, M&A, leadership changes | Always extract the page AND corroborate |
| **P2** (medium impact) | Product launches, partnerships, major hires | Extract if the date is UNCERTAIN or the source is DERIVATIVE |
| **P3** (low impact) | Blog posts, minor hires, event appearances | Trust a plausible date; drop if obviously stale |

## P1 corroboration (mandatory)

Any P1 signal sourced from a derivative or aggregator site **must** be corroborated before it appears in a report. This is a hard gate, not a suggestion. Run a fresh search on `[Company] [event summary]`, and accept the signal only when a PRIMARY or MAJOR source confirms it. If corroboration fails, the signal is UNCERTAIN — drop it.
