---
name: company-deep-dive
title: Company deep dive
description: |
  Use this skill when the ask is about one specific company: "tell me about
  [company]", "research [company]", "what does [company] do", "who is
  [company]", "look up [company]", "company deep dive", "due diligence on
  [company]", "background on [company]", "dig into [company]", "analyze
  [company]" — or when evaluating a company as a sales target, partner, or
  investment. Research the live web instead of answering from memory: funding,
  leadership changes, and product launches move faster than any knowledge base,
  so run it even for well-known companies. Produces a sourced 360-degree
  report covering funding, leadership, product and technology, market position,
  news, and strategic outlook — with a date and URL on every claim.
category: Research
tags: [Sales]
---

Runs when someone needs real, current intelligence on one specific company — not a vibe from stale general knowledge.

Produces a 360-degree company report: quick assessment up top, then funding, leadership, product, market position, and news, closed by a strategic outlook — every factual claim carrying a date and a source URL.

## Scope the run

Three decisions before any research:

1. **Which company, exactly.** If the name is unambiguous ("research Stripe"), run two quick web searches — `"[Company] official site"` and `"[Company] company overview"` — to lock the legal name and primary domain, and confirm in one line: "Researching **[Company]** ([domain])". If the name collides ("research Mercury" — bank? auto brand?), ask one clarifying question with the top candidates. If no company was named, ask which one.
2. **Full or quick.** Default to the full deep dive. If the ask says "quick overview", "brief", or "summary", run quick mode: search-snippet research only, skip the deep-extraction step, produce a shorter report.
3. **First run or refresh.** Keep a running file per company in your workspace (format in `references/company-memory.md`). If a file for this company exists, load it and run in **refresh mode**: tell the reader "I have prior research on [Company] from [date] — refreshing with what's new", pass the known facts into every research thread so they hunt only for new signals, and lead the report with a "What's new since [date]" section. No file → full mode across all dimensions.

## The play

### 1. Research five dimensions in parallel

Fan out one research thread per dimension — run them concurrently, not sequentially; a deep dive is five narrow investigations, not one broad search:

| Dimension | Hunting for |
|---|---|
| **Funding & financials** | Rounds, total raised, valuation, revenue signals, investors, IPO chatter |
| **Product & technology** | Core products, launches, tech-stack signals, engineering blog, open source |
| **Leadership & team** | Founders, C-suite, key hires and departures, headcount, culture signals, executive interviews |
| **News & events** | Press coverage, partnerships, acquisitions, awards, conferences, social chatter |
| **Market position** | Competitors, market share, analyst coverage, customer reviews, case studies |

The per-dimension query patterns — including which queries to date-filter, which to run against the company's own domain, and which review and analyst sources to target — are in `references/dimension-queries.md`. Read it before fanning out.

Two searches run outside the fan-out, first, to frame everything: an "about" search restricted to the company's own domain, and a search for the company's profile on the major business registries (Wikipedia, Crunchbase, Pitchbook). These give founding date, HQ, headcount, and mission — the skeleton the dimensional findings hang on.

Every finding comes back as a structured signal — description, article date, event date, source URL, source type — not prose. The distinction between when a page was published and when the event actually happened is where most research goes wrong; the dating rules, source-quality hierarchy, and the drop rules for stale or unverifiable signals are in `references/signal-dating.md`. Read it before recording the first signal.

If a research thread fails or comes back empty, rerun its queries directly — never leave a dimension blank without trying twice.

### 2. Extract the pages that matter

From all findings, pick the **5–8 most informative URLs** and extract each full page (in parallel). Prioritize, in order: funding announcements with specific amounts; official product or feature pages; executive interviews, podcasts, or conference talks; in-depth analyst or journalist profiles; the company's own about/team page. Full pages yield the numbers, direct quotes, and context that snippets flatten.

Quick mode skips this step entirely and reports from snippets.

### 3. Synthesize the report

Assemble the 360-degree report — exact section order, per-section content rules, and the refresh-mode variant are in `references/report-format.md`. The non-negotiables:

- Lead with a 2–3 sentence **Quick Assessment** — what the company is, where it stands, the one thing that matters most right now. Most readers stop there; make it earn the stop.
- Every claim dated and sourced. A dimension with nothing found says "no public data found" — never speculation dressed as findings.
- Confirmed facts and inferred signals are labeled differently.
- Direct executive quotes (from interviews, earnings calls, talks) beat paraphrase wherever found.

### 4. Update memory and offer next steps

Write the full report to your workspace, and update (or create) the company's running memory file: structured key facts plus dated signal entries, so the next run dedups against it instead of re-reporting old news. Format and dedup rules in `references/company-memory.md`.

Then offer the natural follow-ups: go deeper on one dimension, compare side-by-side with another company, set the company up for ongoing tracking over time, or research the specific people ahead of a meeting.

## What this is not

- **Not multi-company monitoring.** This goes deep on ONE company; tracking a set of competitors over time is a different, recurring motion.
- **Not people research.** It profiles companies, not the individuals attending your next meeting.
- **Not investment advice.** It is intelligence gathering from public sources — say so if asked.
- **Not live monitoring.** The report is point-in-time; rerun it (in refresh mode) when currency matters.

## What good looks like

- The best operators check the **event date, not the article date**, before calling anything new — a syndicated recap published this week about a funding round from last year is the single most common way a "fresh" report embarrasses its author.
- The second tell: single-sourcing a big claim from an aggregator. Funding amounts, M&A, and leadership changes get corroborated against a primary or wire source before they appear — every time.
- The mediocre version is a Wikipedia-shaped summary: undated claims, no URLs, "recent developments" that are neither, dimensions padded with speculation where the search came up empty, and a refresh that re-reports everything already known instead of only what changed.
- Good output test: a reader can click through any claim to its source, the Quick Assessment could stand alone as a briefing, and a refresh run reads like a changelog — short, dated, only genuinely new or updated signals.

## Rules

- MUST research the live web — never answer about a specific company purely from prior general knowledge, however famous the company.
- MUST attach a date and source URL to every factual claim in the report.
- MUST corroborate funding, M&A, and leadership-change claims sourced from derivative or aggregator sites against a primary or major source before reporting them (see `references/signal-dating.md`).
- MUST write "no public data found" for an empty dimension — NEVER fill the gap with speculation.
- MUST dedup against the company's memory file in refresh mode and surface only NEW or UPDATED signals.
- NEVER include a signal whose event date cannot be established — dropped means dropped, not footnoted as "background".
- NEVER present an estimate or inference with the same confidence as a confirmed fact — label which is which.
