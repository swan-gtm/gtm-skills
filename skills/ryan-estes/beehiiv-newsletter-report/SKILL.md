---
name: "beehiiv-newsletter-report"
title: Beehiiv newsletter performance report
description: "Use this skill when building a sponsor or client performance report on top of a Beehiiv publication, or when designing a Beehiiv MCP tool or integration that needs to expose the same metrics. It covers audience growth, open and click rate analysis (including the click-to-open trap in Beehiiv's own API), audience segmentation, month-over-month synopsis, an engaged-reader export, per-issue KPIs, and a pattern for keeping the report refreshed automatically without the narrative drifting."
category: Newsletters
---

## Purpose

Turn raw Beehiiv publication data into a report a non-technical stakeholder (a sponsor, a
client, a newsletter owner) can read in under a minute and still trust the numbers in.
This skill generalizes a report built for a real newsletter sponsorship client, stripped of
any client-specific branding or copy, so the same structure can be reused for any Beehiiv
publication or wired into an MCP server that answers questions like "how did last month's
issues perform."

## When to use this skill

Use it when asked to build, extend, or automate a newsletter/sponsor performance report
backed by Beehiiv, or when exposing Beehiiv metrics through an MCP tool, API, or chatbot and
needing the correct formulas and section structure rather than reinventing them.

## Prerequisites

- A Beehiiv publication ID and an API key (Bearer token) with read access to that publication.
- Base URL: `https://api.beehiiv.com/v2/publications/{pub_id}/...`
- All Beehiiv field mappings, formulas, and pagination details live in
  `references/beehiiv-api-reference.md`. Read it before implementing any of the sections below;
  several of Beehiiv's own fields are misleading (see Pitfalls) and getting them wrong produces
  a report that contradicts what the client sees on their own Beehiiv dashboard.

## Report anatomy

A complete report has nine sections. Build them in roughly this order, since later sections
depend on data assembled for earlier ones.

1. **Hero stats**: total growth since launch, current audience size, average open rate over a
   recent window (e.g. trailing several months). Three numbers, no chart, at the very top.
2. **Website / lead magnet links**: a short list of outbound links relevant to the newsletter
   itself (its homepage) and any sponsor/lead-magnet destination being tracked (e.g. a landing
   page a sponsor cares about). Plain outbound links, not chart data.
3. **Audience growth chart**: one time series of subscriber count, spanning the newsletter's
   full history to date.
4. **Open rate analysis**: a per-issue open-rate bar chart plus a short structured narrative
   (a question, an answer/verdict, supporting points, one forward-looking opportunity).
5. **Click rate analysis**: the same narrative structure as open rate analysis, charting clicks
   or click rate per issue instead.
6. **Audience insights**: an engagement segmentation (how loyal is the audience, by lifetime
   open rate) and a list-health breakdown (active / inactive / invalid).
7. **Month-over-month tabs**: one tab per calendar month, each with a synopsis (headline,
   highlights, opportunities), that month's rollup stats, and every issue published that month.
8. **Engaged-reader export**: for reports tracking clicks to a specific sponsor/partner link,
   a table of who clicked, exportable as CSV, with a searchable full-list view and a breakdown
   by company/industry category.
9. **Per-issue KPI cards**: nested inside each month tab: recipients, delivered, open rate,
   click rate, unsubscribes, spam reports, per individual issue.

Full data shapes and exact chart/card content for each section are in
`references/report-sections.md`.

## Workflow to build one

1. Confirm credentials and the publication ID; verify a single `GET /posts?limit=1` call
   succeeds before building anything else.
2. Fetch confirmed posts with stats (`expand[]=stats`, `status=confirmed`, ordered by publish
   date ascending). This one call powers sections 4, 5, 7, and 9.
3. Compute per-issue fields and per-month rollups using the formulas in
   `references/beehiiv-api-reference.md` (do not trust Beehiiv's `click_rate` field at face
   value; see Pitfalls).
4. Build the audience growth series (section 3). Decide the growth mode up front: `per-issue`
   (derived from posts) or `subscriber-timeline` (a hand-curated periodic snapshot). See
   `references/beehiiv-api-reference.md` for when each applies.
5. Fetch the full subscriber list with `expand[]=stats`, cursor-paginating to completion, and
   compute the engagement segments and list-health split for section 6.
6. Write the narrative content for sections 4, 5, and 7 (the only genuinely generated prose in
   the report). Keep it short, specific to the actual numbers, and free of hedging.
7. If the report needs section 8, treat it as a periodic manual/semi-automated step, not a live
   API call. See Pitfalls.
8. Render nothing for any section whose backing data is empty or absent (no polls, no audience
   data yet, no engaged-reader export configured) rather than showing an empty or placeholder
   state. This lets sections be added to a report incrementally as data becomes available.

## Automating a refresh

Once a report exists, keep it current on a schedule (e.g. weekly) rather than hand-updating it.
The refresh should treat "recompute deterministic numbers" and "regenerate narrative" as two
different jobs with two different reliability bars. See `references/automation-pipeline.md` for
the full pattern, including a multi-tenant registry design for running the same pipeline across
several publications/clients at once.

## Pitfalls

These are the mistakes most likely to produce a report that looks fine but is wrong:

- **Beehiiv's `click_rate` field is click-to-open (clicks / opens), not clicks-per-delivered.**
  If the report is meant to show "what fraction of the send resulted in a click," compute
  `unique_clicks / delivered` yourself. Consider displaying whichever of the two figures is
  larger, since that is usually the number the client already sees emphasized on their own
  Beehiiv dashboard, and a report showing a smaller number reads as wrong even when it is
  arguably more correct.
- **The poll `poll_responses` expand on a poll's GET endpoint is capped at 10 responses and
  cannot paginate.** Any poll with more than 10 responses will silently under-report through
  that path. Get accurate per-choice counts by cursor-paginating
  `/polls/{id}/responses` and tallying `poll_choice_id` client-side instead.
- **Beehiiv exposes no subscriber location data.** Do not build or fake a geographic view; it
  does not exist in the API and any resemblance to one will be pure invention.
- **Compute engagement segments only over subscribers who have received enough issues to have
  a meaningful lifetime open rate** (e.g. at least 3). Otherwise a batch of freshly imported
  subscribers who have only seen one issue distorts the segmentation, since anyone who has not
  opened yet reads identically to someone who never will.
- **A "who clicked this specific sponsor link" export is generally not a clean, documented,
  single API call.** Beehiiv's own dashboard supports building a subscriber segment from click
  behavior and exporting it as CSV; the practical path is to pull that CSV periodically and
  enrich it yourself (e.g. classify each subscriber's email domain into a company/industry
  category with a lightweight heuristic or an LLM pass), rather than trying to reproduce it as
  a live query inside an automated refresh.
- **A publication's early history may predate structured per-issue tracking or was migrated
  from a different platform.** For that period, a hand-curated subscriber-count timeline (which
  can rise or fall) is more honest than deriving growth from per-issue recipient counts, which
  is roughly monotonic by construction and will paper over real churn.
- **Never regenerate all narrative sections wholesale on every refresh.** Update only the month
  or analysis affected by new data, and preserve the tone, length, and untouched prose from
  prior periods; wholesale regeneration produces visible tonal drift and makes diffs impossible
  to review.

## For MCP tool / integration builders

If exposing this as MCP tools or an API instead of (or in addition to) a rendered report page,
map each section to its own tool so a client can compose them conversationally or a UI can call
them independently:

- `get_publication_summary` → hero stats (section 1)
- `get_audience_growth` → growth series (section 3)
- `get_rate_analysis` (parameterized by `open` or `click`) → sections 4 and 5
- `get_audience_segments` → engagement segmentation and list health (section 6)
- `get_monthly_report` (parameterized by month) → that month's synopsis, rollups, and issues
  (section 7)
- `export_engaged_subscribers` → section 8, backed by the periodic CSV/enrichment pipeline, not
  a live Beehiiv call
- `get_issue_kpis` (parameterized by post ID or date range) → section 9

Cache subscriber-list pagination results where possible; a full engagement-segment computation
requires walking the entire subscriber list, which can be thousands of paginated records, on
every call otherwise.

## What good looks like

A report a non-technical stakeholder can read in under a minute and still trust the numbers in — click rates that match what the client sees on their own Beehiiv dashboard, poll tallies from full pagination rather than the capped expand, engagement segments that exclude subscribers too new to have a meaningful lifetime open rate, and narrative that changes only where the numbers did. The failure modes: a click rate that contradicts the client's dashboard, a silently under-reported poll, an invented geographic view, or wholesale-regenerated prose drifting in tone between refreshes.
