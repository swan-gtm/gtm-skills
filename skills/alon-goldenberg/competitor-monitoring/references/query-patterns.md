# Query patterns — the research fan-out

How to structure the searches for each run. All of this is tool-agnostic: run these with whatever live-web search and page-extraction capability you have. Where your tool supports date filters, domain restriction, or a news focus, use them as noted; where it doesn't, put the constraint in the query text ("since [date]", "site:[domain]").

## Per-competitor fan-out (five queries, run in parallel)

For each competitor, run all five simultaneously. Each query hunts a different signal class — skipping one leaves a blind spot.

| # | Query | What it catches | Notes |
|---|---|---|---|
| 1 | "[Competitor] news" — news-focused, scoped to the run's date window | Press coverage: funding, M&A, launches | The workhorse. ~10 results. |
| 2 | "[Competitor] funding OR acquisition OR hiring" — scoped to the date window | P1 events that miss generic news queries | ~5 results. |
| 3 | "release notes OR changelog OR what's new" — restricted to the competitor's own domain | Their changelog / release-notes page | See changelog extraction below. |
| 4 | "[Competitor]" — restricted to x.com and linkedin.com, past week only | Real-time announcements | Social posts land days before press articles. Keep the window tight or it's all noise. |
| 5 | "[Competitor] reviews G2 OR Capterra" | Review-site movement, positioning shifts, customer sentiment | ~5 results; usually P3. |

**Changelog extraction (the highest-signal move in the fan-out).** If query 3 returns a URL that looks like the competitor's own changelog (`example.com/changelog`, `docs.example.com/release-notes`, `/whats-new`), extract that page's full content as text. It yields dated feature releases straight from the primary source — no date verification needed, no derivative-source risk. This is the cheapest primary-source signal you will get all run.

**Fallback for thin results.** If queries 1–2 together return fewer than 3 results, re-run them without the date filter, then apply the date discipline manually — the filter sometimes hides original sources that recent coverage points back to.

**Scope cap.** Keep each competitor to roughly 8 research actions (searches + extractions) per run. Beyond that you're deep-diving one company, which is a different job — note it as a follow-up instead of blowing the budget mid-run.

## Parallelizing across competitors

- One research thread per competitor; if running threads in parallel, batch them (about 4 at a time) rather than launching all at once.
- Give each thread the competitor's name, domain, the run's date window, and the **known-signals list from that competitor's memory file** so it skips already-reported items at the source instead of returning them for you to dedup later.
- Require each thread to return signals in the per-signal record format from the signal-validation reference — free-form prose answers can't be validated or deduped.

## Own-company queries (two, run alongside)

The briefing should contrast competitor moves with your own — run these on the user's company:

1. "product updates OR changelog OR releases" — restricted to the company's own domain, scoped to the date window
2. "[Company] news" — news-focused, scoped to the date window

Fallback if under 3 results: search "blog" restricted to the company domain, undated.

## Industry-trend queries (two, run alongside)

Using the profile's industry keywords:

1. "[industry keyword] AI agents OR automation" — news-focused, date-scoped
2. "[industry keyword] regulation OR compliance OR pricing" — news-focused, date-scoped

Swap the OR-terms for whatever axes actually move this market (adjust once in the profile, not per run).

## Query construction tips

- **Domain-restrict when the name is ambiguous.** For competitors with generic names ("Notion", "Monday", "Attio" vs "Atrio"), restrict to their domain or add the category to the query — otherwise half the results are noise.
- **Discovery searches stay lightweight.** Use your tool's cheapest/fastest search tier for the fan-out; reserve full-content extraction for the signals that earn it under the verification budget.
- **Date filters reduce noise but never establish truth.** A date-filtered search returns pages by *publication* date, which include fresh articles about old events. The event date always comes from the page content (see the signal-validation reference).
- **Inline concrete dates** ("since [YYYY-MM-DD]") rather than relative language ("last two weeks") wherever a query accepts text — relative phrasing is interpreted inconsistently across tools.
