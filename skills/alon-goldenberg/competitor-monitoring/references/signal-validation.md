# Signal validation — dates, sources, priorities

The rules that decide whether a candidate finding may appear in a briefing. Apply them to every signal, every run. The core problem they solve: syndicated and recap content carries fresh publication dates on old events, and a briefing that misses this reports history as news.

## Priority tiers

Assign every signal exactly one priority. Priority drives the verification budget and the report's ordering.

| Priority | Signal types | Why it matters |
|---|---|---|
| **P1** | M&A, leadership changes (C-suite/VP in or out), major funding (>$10M), a launch that competes directly with your product | Changes the competitive landscape; a rep or exec may act on it same-day |
| **P2** | Product launches, strategic partnerships, major hiring waves, pricing changes | Shapes positioning and battlecards |
| **P3** | Blog posts, comparison articles, minor hires, event appearances, opinion pieces, review-site movement | Context; mention briefly or omit when the report runs long |

## Article date vs. event date

Every signal carries two dates:

| | What it is |
|---|---|
| **Article date** | When the page was published |
| **Event date** | When the underlying event actually happened |

A signal is "new" only if its **event date** falls inside the run's freshness window. The article date is never sufficient — syndication, regulatory recaps, and industry roundups routinely publish weeks or months after the event.

### Extracting the event date from content

1. **Explicit past reference** — "launched in Q3", "appointed last October" → event date is in the past, regardless of article date.
2. **Temporal language** — "last quarter", "months ago", "earlier this year" → resolve relative to the article date.
3. **Present-tense announcement** — "today announces", "is launching" → event date ≈ article date.
4. **Dateline** — "NEW YORK, March 15 —" → event date = the dateline date.
5. **Still ambiguous from the snippet** — extract the full page and read the body; check the on-page date, not the search result's date.

## Source-type hierarchy

When the same event appears in multiple places, classify each source and prefer the one closest to the event:

1. **PRIMARY** — the company's own domain, official press release, regulatory filing
2. **WIRE** — AP, Reuters, Bloomberg
3. **MAJOR** — original reporting with a byline at a major outlet
4. **DERIVATIVE** — syndicated copies, aggregators, recap articles, anything that attributes its facts to another source

If the *only* source for a signal is DERIVATIVE, it cannot be reported as-is — corroborate it (below) or drop it.

## Freshness classification

After the event date is determined and memory has been checked:

| Classification | Meaning | Action |
|---|---|---|
| **NEW** | Event date inside the window, not in memory | Include |
| **UPDATED** | Known event with genuinely new information | Include, marked as an update |
| **STALE** | Old event under a fresh article | **Drop entirely** |
| **UNCERTAIN** | Event date can't be determined even after extracting the page | **Drop, with a one-line note if P1** |

**Hard rule:** only NEW and UPDATED signals may appear in reports or be written to memory. STALE and UNCERTAIN are dropped entirely — not downgraded, not footnoted, not smuggled in as "background context." A signal that can't be verified as genuinely recent does not exist as far as the report is concerned.

## Verification budget

Full-page extraction costs time; spend it by priority:

| Priority | Verification |
|---|---|
| **P1** | Always extract the page AND corroborate (below) — no exceptions |
| **P2** | Extract when the date is uncertain or the only source is derivative |
| **P3** | Trust a plausible date; drop if obviously stale. Never spend an extraction on a P3 |

## P1 corroboration (mandatory gate)

Any P1 signal that is derivative-only sourced, or whose date confidence is low, must be corroborated before it can enter the report:

1. Search the live web for "[Company] [event summary]".
2. Look for the primary source — company blog, press release, official or regulatory filing.
3. **Primary source dates the event inside the window** → NEW, include.
4. **Primary source dates it outside the window** → reclassify STALE, drop.
5. **No primary source found** → reclassify UNCERTAIN, drop.

Never report a P1 that fails corroboration. Better to miss a real signal than to report a stale one as new.

## Per-signal record format

Have every research thread return signals in this exact shape — free-form prose can't be validated, deduped, or filed to memory:

```
SIGNAL: [one-line description]
ARTICLE_DATE: [YYYY-MM-DD or ~YYYY-MM]
EVENT_DATE: [YYYY-MM-DD or ~YYYY-MM]
URL: [source url]
SOURCE_TYPE: [PRIMARY|WIRE|MAJOR|DERIVATIVE]
DATE_CONFIDENCE: [HIGH|MEDIUM|LOW]
NEEDS_CORROBORATION: [true|false]
TYPE: [news|product|funding|hiring|partnership|review]
PRIORITY: [P1|P2|P3]
```

`NEEDS_CORROBORATION` is true when: PRIORITY is P1 AND (SOURCE_TYPE is DERIVATIVE OR DATE_CONFIDENCE is LOW) AND no primary source has been found yet.

## Deduplicating the same event across sources

Within one run, the same event often arrives from several queries and outlets. Merge before classifying: match on the event (company + event type + approximate date), keep the highest-ranked source as the record's URL, and count the distinct sources — multi-source signals are higher confidence. Dedup against *memory* (events already reported in previous runs) happens separately and turns would-be NEW signals into UPDATED or drops them.
