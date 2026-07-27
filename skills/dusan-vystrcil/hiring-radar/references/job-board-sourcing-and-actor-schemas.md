---
title: "Job board sourcing — actor schemas and the vetting protocol"
description: Reference for the Hiring radar skill.
---

# Job board sourcing — actor schemas and the vetting protocol

The skill's sourcing rule: **LinkedIn only through your platform's native
LinkedIn integration** — LinkedIn scraping actors exist, and none of them are
permitted here. **Every other board runs through exactly one vetted, test-run
scraper per board; a board without one is skipped, not improvised.**

Each actor below is documented as a schema — what it takes, what it filters
on, what it returns — followed by what a real test run proved. The **Returns**
list is also the schema canary: when an actor's field set changes, the vendor
changed something, so re-run the vetting protocol before trusting the next
scheduled pull.

Read this as a worked set, not a closed list. The documented actors cover the
common boards; for any source that isn't here — a regional board, a niche
vertical site, a market you're adding — the last two sections are the method:
find a candidate, then put it through the same vetting protocol before it
feeds a scheduled run. An undocumented board is sourced the same way as a
documented one, just by you.

## Query types

The radar searches three ways; check the actor exposes the ones you need:

- **Role title** — the persona being hired ("data engineer", "mechanical
  engineer"). Needs a title-level search field.
- **Technology / product in the JD** — a tracked tool ("SharePoint", a
  competitor product). Needs full-text description search.
- **Role × technology combo** — the sharpest displacement query
  ("administrator" + a specific platform). Needs both fields in one call.

## The actors

Two are **load-bearing**: the career-site index covers the mention scan and
most of the watchlist, and the direct-ATS actor covers watched accounts the
index misses. The rest are supplementary or regional — losing one costs
coverage, not the play.

### `fantastic-jobs/career-site-job-listing-api` — career sites & ATS · load-bearing

- **Serves:** watchlist scan and mention scan — the workhorse
- **Query fields:** `organizationSearch`, `titleSearch`, `descriptionSearch`,
  `domainFilter`, each with an exclusion twin; combinable in one call. Every
  term needs the `:*` suffix (`"Google:*"`, `"administrator:*"`) — copy the
  syntax verbatim, plain words produce silent 0-result returns.
- **Freshness:** `timeRange` = `1h` | `24h` | `7d` | `6m`
- **Cap:** `limit`, 10–5 000
- **Returns:** `date_posted` (ISO), `organization`, `description_text` (full),
  `url` (direct ATS link), `source` (ATS name), `ai_key_skills`
- **Verified:** all three query types, including the role × technology combo;
  rows inside the requested window; employer is the career-site owner
- **Watch out:** coverage is index-bound — a major enterprise on its own
  career portal returned zero while indexed companies worked, so run check 7
  on every watched account. Sibling `fantastic-jobs/career-site-job-listing-feed`
  shares the index at a lower per-job cost but forces `limit >= 200`; the
  volume option once the watchlist grows, not test-run.

### `bujhmml/ats-jobs-scraper` — Greenhouse / Lever / Ashby, direct APIs · load-bearing

- **Serves:** watchlist scan, one watched account per call
- **Query fields:** `sources` — `{ats, company}` slug pairs, pasted board
  URLs, or bare slugs with ATS auto-detect. Unbilled pre-filters:
  `titleKeyword`, `locationKeyword`, `department`, `remoteOnly`.
- **Freshness:** none — filter by date on ingest
- **Cap:** `maxItems`, **global across boards** — the first board can starve
  the rest, so keep it one account per call
- **Returns:** `source_ats`, `company`, `title`, `posted_at`, `created_at`,
  `description` + `description_html`, `url`, `apply_url`, `department`,
  `employment_type`
- **Verified:** all three ATS paths; Ashby and Lever carry precise per-job
  ISO dates (an evergreen listing showed its true multi-year-old date —
  exactly what the evergreen rule needs); employer is fixed by the slug and
  URLs point at the company's own careers page
- **Watch out:** **Greenhouse `posted_at` is a board-level publish timestamp,
  identical across every job — use `created_at` for Greenhouse rows or the
  whole board reads as a same-day spree.** Markedly cheaper per job than the
  workhorse and immune to its index gaps. Low store usage, but it calls
  documented public ATS APIs directly.

### `borderline/indeed-scraper` — Indeed

- **Serves:** mention scan (`query`); watchlist only via company `urls`
- **Freshness:** `fromDays`
- **Cap:** `maxRows`
- **Returns:** `datePublished`, `companyName`, `descriptionText` (full),
  `jobUrl` (absolute), plus company firmographics
- **Verified:** window respected, full descriptions, employer field present
- **Watch out:** heavy staffing-agency tail — the skill's employer resolution
  does real work on this source

### `valig/glassdoor-jobs-scraper` — Glassdoor

- **Serves:** mention scan (`keywords`)
- **Freshness:** `daysOld`, echoed back as `ageInDays`
- **Cap:** `limit`
- **Returns:** `title`, `employer.name`, `ageInDays`, `description` (HTML),
  `url` (absolute)
- **Watch out:** `location` must be city-level — a country name produced a
  silent 0-result return, a city returned a full page. No reliable company
  filter, so never force it into the watchlist scan.

### `johnvc/Google-Jobs-Scraper` — Google Jobs aggregator · backstop only

- **Serves:** mention scan backstop for boards you don't cover directly
- **Query fields:** `query`, `location`, `country`
- **Freshness:** none — filter dates on ingest
- **Cap:** `num_results`, `max_pagination` — pagination is the billing lever,
  it charges per results page
- **Returns:** `title`, `company_name`, `description` (full),
  `via` (originating board), `detected_extensions.posted_at` (relative string,
  sometimes absent), `share_link` (a Google URL, not the employer's page)
- **Watch out:** a charge cap below the per-page fee makes the run refuse to
  fetch and return zero rows with a SUCCEEDED status. Expect duplicates of
  Indeed/ATS finds. Weakest dates in the set — backstop, never a primary.

### `memo23/stepstone-search-cheerio-ppr` — StepStone DACH/BE (Totaljobs UK via sister actor) · regional

- **Serves:** mention scan, regional
- **Query fields:** `keyword`, `country` (`de`/`at`/`be`), `location`,
  `category`; `startUrls` for a second pass over specific postings
- **Freshness:** `postedWithin` = `1` | `3` | `7` days — verified, a 3-day
  window returned only in-window rows
- **Cap:** `maxItems`
- **Returns:** `title`, `companyName`, `datePosted` (ISO), `url`
  (site-relative — prefix the board's domain), `textSnippet` (~300 chars only)
- **Watch out:** keep `includeRelatedJobs` off, or sparse queries get padded
  with non-matching "recommended" rows. Full JD text needs the second pass via
  `startUrls`. Ignore its "No results found" status message when rows are
  present — it fires even on full result sets. Swap for the boards your market
  actually uses.

### Rejected

- `bovi/google-jobs-scraper` — better on paper than the backstop above (a real
  `datePosted` filter, full descriptions, per-result pricing) but returned
  zero rows on two query phrasings while the incumbent filled a page on the
  same query. Kept here as the reason the protocol exists.

**Dedup across sources.** If two boards return the same posting — aggregators
will — the key is employer + title + posted date, and the canonical link is
the one closest to the employer: career site > board > aggregator.

## Finding an actor for a source that isn't listed

When an actor dies, a board changes, or you need a source this page doesn't
document:

1. **Search the store** for `<board> jobs`, `job listings`, and `job postings`
   — broad platform words first, then narrow. This shortlist came from exactly
   those three searches.
2. **Shortlist on schema fit, not on marketing copy**: does it expose the
   query types above, and does it return the fields checks 1–4 need? An actor
   missing posted dates is unusable no matter how good it looks.
3. **Treat store stats as a gate, never a decision.** High usage and success
   rate did not guarantee rows — the rejected Google Jobs actor showed 98%
   success and returned nothing, twice. Low usage did not disqualify — the
   direct-ATS actor has the smallest user count and the cleanest data in this
   set. The test run decides, both ways.
4. **One actor per board.** Coverage compounds across *sources*, not across
   queries: one source reaches roughly 60% of the postings that exist, two
   ~85%, three ~92%. The same actor with different queries is not a second
   source.
5. **Skip "hiring intent lead" actors** that bundle contact enrichment.
   Classification stays in this play, and the radar does no outreach.
6. **Run the protocol below before scheduling** — and again whenever the
   Returns field set shifts.

## Vetting protocol — run once per actor before scheduling

Run the actor on a small sample (one watched account, one query; cap results
≤ 25) and check the output against what the skill's steps consume:

1. **Posted date present and real** (`postedAt` / `datePosted` / `posted_at`).
   No posted dates → the spree threshold and the 14-day rule can't work → the
   board is unusable, skip it. Relative dates ("3 days ago") must be converted
   on ingest. Watch for board-level timestamps masquerading as per-job dates.
2. **Employer field is the employer**, not a staffing agency or the board's
   own name. Spot-check three listings against the company's career site.
3. **Description is full text**, not a teaser — the mention scan and the JD
   read both die on truncated descriptions.
4. **Stable posting URL** a rep can open without login, ideally the employer's
   own page.
5. **Freshness filter works** — set it to the run cadence and confirm every
   row falls inside the window. No filter field → filter on ingest and say so
   in the Setup state paragraph.
6. **Caps, both layers.** A charge cap below the actor's fixed first-step fees
   (start fee, per-page fee) produces a silent zero, not an error. And a run
   returning exactly its item cap is an INCOMPLETE pull — re-run higher, never
   count it as the full picture, or a truncated spree misclassifies and the
   digest lies.
7. **Watchlist coverage** — for a company-filtered actor, run each watched
   account once. An account returning zero rows is not covered by that source
   and needs another board, or its zeros will read as silence.
8. **Negative control** — run a query that must return nothing (a nonsense
   company slug, an excluded own-domain term). Rows coming back mean the
   filters aren't applied. This is what makes a zero provable: without it you
   cannot tell a real quiet week from a silently broken source — and the
   skill's zero-check depends on that difference.

Record the pass in the skill's Setup state paragraph: board, actor, query
types verified. A board that fails any check is skipped.
