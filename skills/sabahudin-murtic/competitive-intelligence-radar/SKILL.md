---
name: "competitive-intelligence-radar"
title: Competitive intelligence radar
description: "Use this skill when you want a standing weekly watch on your competitors — pricing, SERP rank, positioning, news, sentiment, funding, and hiring — with a source URL on every single claim, plus an on-demand strategic war room that debates the findings and converges on ranked moves. A Claude Code plugin that fans out one research scout per competitor in parallel over live web data (BrightData MCP), diffs against last week, and publishes to a local folder, Notion, and a self-contained HTML dashboard."
category: Research
---

This is a Claude Code plugin by Sabahudin Murtic. Install it from his repo — https://github.com/sabahudin-web/competitive-intelligence-radar — which bundles the commands, agents, skills, and rules described here. It needs a BrightData API token (live web data) and a Notion connection (publishing), and the optional war room uses Claude Code's experimental agent-teams feature.

## The three commands

- `/radar-setup` — one-time onboarding. Asks whether BrightData and Notion are connected and live-tests one real call to each (it never assumes), collects your business context (domain, tracked keywords, competitor list, geo), shows the proposed Notion schema and creates the databases only after you approve, and checks the agent-team prerequisites for the council.
- `/radar` — the weekly gather. Runs autonomously end to end.
- `/radar-council` — the on-demand strategic war room. Token heavy; always asks before it runs.

## The weekly gather (/radar)

One scout subagent per competitor, all fanned out in parallel (capped at 8 per run). Each scout independently gathers a cited JSON dossier: SERP rank for your tracked keywords, pricing and positioning scraped from the competitor's own pages, and fresh news — plus opt-in deep sources (social sentiment, financials, hiring) only when enabled. Scouts never talk to each other; they gather, cite, and report back.

Every dossier field is an object of `value`, `source_url`, `fetched_at`, and `status`. If a value can't be found it is `null` with `status: not_found`; a blocked page is recorded as `blocked`. Never a guess, never a URL that wasn't fetched this run — model knowledge is not a source.

The orchestrator then diffs against last week's run, comparing only fields fresh on both sides (pricing and SERP re-fetched every run; news, sentiment, and hiring within 30 days; funding within 90). Changes are classified — Rising, Falling, Price, News, New — ranked by materiality, and merged into one briefing where every claim carries its source and fetch date, headed by a "what changed" digest and a three-item focus list.

## The war room (/radar-council)

Where the gather uses subagents (workers that only report back), the council uses a real experimental agent team — four analyst teammates that read the briefing and debate each other directly: a pricing analyst, a product-gap analyst, a threat-and-sentiment analyst, and a devil's advocate whose whole job is to disprove the others. They post opening reads, challenge each other by name, defend with cited evidence or concede, and converge. The lead then synthesizes a Strategic War Room addendum: a consensus summary, the top recommended moves each with a one-line rationale and its supporting source or dossier field, and a dissents-and-risks list for anything still disputed. The plugin never swaps the two parallelism primitives: subagents for the gather, an agent team for the debate.

## Three output surfaces, every run

1. A local `outputs/` folder: the briefing markdown, the combined raw dossier JSON, and the war-room addendum.
2. Notion: a Competitors database upserted by domain with week-over-week Change tracking, and a Briefings page per run.
3. A self-contained local HTML dashboard — inline CSS and JS, no dependencies, no network — you open in any browser.

## Rules in force

- No fabrication: every factual claim carries a real source URL fetched this run. A single invented number destroys the product promise.
- Freshness: stale data is labeled "as of <date>", never presented as current.
- Cost control: batch tools over per-URL calls, competitors capped at 8, lean scout depth by default, the expensive scraping browser only as a fallback for blocked pages.
- Checkpoints: Notion database creation and the token-heavy council always ask for an explicit yes first; the gather runs autonomously.

## What good looks like

A briefing where every claim links to a page actually fetched that run; anything unverifiable says not-found or blocked instead of guessing; the focus list is three ranked items, not a wall of data; and the council's moves each survive a devil's-advocate challenge with a citation attached. The owner reads it in five minutes and knows exactly where to look this week.
