---
title: Command reference
description: (reference)
---

The plugin's three slash commands, in the order you use them. Commands only sequence the bundled skills; the skills do the work.

## /radar-setup — one-time onboarding (checkpoint)

1. `radar-onboard`: asks whether BrightData and Notion are connected, live-tests one real call to each, detects the live MCP prefix (plugin path, desktop connector path, or UUID), and writes `radar.config.json` with your business context — name, domain, geo, tracked keywords, competitor list (capped at 8), and the three scout-depth flags (social, financials, hiring — all off by default for a lean run). Stops with connect instructions if a live test fails.
2. `radar-provision-notion`: shows the proposed Competitors and Briefings schema and asks for approval before creating anything. Idempotent — verifies existing databases instead of duplicating them.
3. Checks the agent-team prerequisites for the council (Claude Code v2.1.32+ and the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` env flag) and reports status. Gather and council are independent; `/radar` works even if the council isn't ready.

## /radar — the weekly gather (autonomous)

1. `radar-plan-targets`: reads the config, enforces the cap of 8 and waves of 8, creates the dated run directory, and emits one scout job spec per competitor.
2. Fans out one `competitor-scout` subagent per competitor, all in one message so they run in parallel. Each writes one cited JSON dossier and reports back.
3. `radar-diff-changes`: compares against last run, only across fields fresh on both sides, and produces a ranked change set.
4. `radar-merge-briefing`: writes the briefing markdown, the combined dossier JSON, and the dashboard data JSON. Every claim carries a source URL.
5. `radar-publish-notion`: upserts Competitors rows (by domain, with the Change field) and creates the Briefings page. Skipped gracefully if Notion isn't provisioned.
6. `radar-render-dashboard`: injects the data into the self-contained HTML dashboard.
7. Prints the three output locations and hints at `/radar-council`.

## /radar-council — the strategic war room (checkpoint)

1. Confirms a briefing exists, agent teams are enabled, and the user explicitly agrees to spend the tokens (each teammate is a separate Claude instance).
2. Creates one agent team and spawns the four analysts by name, each pointed at the latest briefing and dossiers with its specific lens.
3. Runs the debate: opening reads, direct challenges, defend with cited evidence or concede, converge.
4. The lead synthesizes the Strategic War Room addendum and `radar-publish-council` appends it to all three surfaces (local briefing, dashboard war-room section, Notion page with its War Room box checked).
5. Cleans up the team as soon as the addendum is written.
