---
title: Agent roster
description: (reference)
---

Five agent definitions ship with the plugin: one gather worker and four war-room analysts. The distinction is deliberate — subagents for gathering (workers that only report back), an agent team for the debate (teammates that message and challenge each other) — and the plugin never swaps them.

## competitor-scout (subagent, one per competitor)

An amnesiac single-competitor gatherer. Researches exactly one competitor via BrightData and returns exactly one cited JSON dossier: SERP rank for the tracked keywords, pricing and positioning from the competitor's own pages, fresh news, and — only when the depth flags are on — social sentiment, financials, and hiring signals. Prefers batch tools, falls back to the expensive scraping browser only for blocked or JS-heavy pages, and records `not_found` or `blocked` honestly instead of inventing values. Never messages another agent.

## The four council analysts (agent-team teammates)

All four read the latest briefing and dossiers, may make one or two light BrightData spot-checks to test a specific claim, cite every external claim, and debate each other by name until the moves converge. They are read-only; the team lead synthesizes and publishes.

- **pricing-analyst** — pricing and packaging. Where is each rival's price relative to yours, who changed packaging, where are you exposed or advantaged, and what concrete pricing move follows: a new tier, a repackage, a price test.
- **product-gap-analyst** — product, features, and positioning. What rivals emphasize and ship, where one is clearly ahead, where a gap nobody covers could be owned, with hiring signals read as a leading indicator of product direction.
- **threat-sentiment-analyst** — competitive threat and market sentiment. Ranks the rising danger of the week from SERP momentum, funding, news, hiring, and mood shifts; separates a single bad review from a pattern.
- **devils-advocate** — the skeptic. Doesn't propose the plan; stresses it. Attacks the weakest link in each analyst's read, hunts for anchoring on the first plausible story, flags any move resting on a stale or missing source, and surfaces the move nobody proposed because it was uncomfortable. A move that can't survive its challenge gets cut or downgraded.
