---
name: gtm-command-center
title: GTM command center
description: |
  Use this skill when a GTM operator is losing time hopping between tools to see their own work - the task board in one tab, the outreach queue in another, research in a third, the content calendar in a fourth. Produces one personal operating surface that aggregates those lanes, plus a single daily "what needs me now" roll-up. Reach for it when someone says "I'm drowning in tabs", "I need one place to work from", "build me a dashboard", "a command center", "a morning operating view", or "I keep missing things across my tools".
category: RevOps
tags: [RevOps]
---

Applies when one operator's work is scattered across many tools and nothing shows the whole day in one place. Produces a single personal operating surface - the lanes that matter, refreshed on a cadence - and one daily roll-up of only what needs that person today.

A command center is not another tool to maintain. It is a read-mostly mirror: it pulls the current state of each lane you already work in and lays it on one screen, so you stop tab-hopping to reconstruct your own day. The discipline that makes it work is subtractive - what you leave off matters more than what you put on.

## Build it

1. **List the lanes, then cut half.** Write down every surface you check in a normal day. Keep only the lanes where you personally take action - the task board, the outreach queue, the research digest, the content/publishing queue, the events or presence lane, a pipeline snapshot. Drop anything you only monitor. The lane catalogue and the data contract each lane needs are in `references/lanes.md`.
2. **One source of truth per lane.** Each lane points at exactly one system of record and mirrors it. Never let a lane hold state that also lives somewhere else - the moment two places disagree, you stop trusting the surface and go back to the tabs. The build patterns (read-mostly aggregation, refresh cadence, single-source rule) are in `references/build-guide.md`.
3. **Keep it read-mostly.** The surface shows and links out; it does not become the place you edit everything. A dashboard that turns into another editing tool is just one more thing to keep in sync. Allow only the few low-friction actions that keep you on the surface (mark done, add a note); everything heavier links back to the system of record.
4. **Wall off anything teammate-facing.** If any part of this surface is ever shown to teammates, a boss, or clients, it must carry none of your private working notes, raw scores, or internal labels. The clean-room separation - private working surface vs shareable view - is in `references/clean-room.md`.

## Run it daily

The payoff is one morning read that answers a single question: what needs me today. Assemble the roll-up across lanes, rank by what only you can move and what has a clock on it, and suppress everything that is merely in progress. The assembly method, the ranking rule, and what to surface vs suppress are in `references/morning-rollup.md`.

## What good looks like

- **What the best operator notices first:** the value is in what the surface leaves off. A command center that shows everything is a second inbox - you scan it once, feel behind, and go back to your tools. The skill is ruthless triage: only lanes you act in, only items that need you, only today. If a section never changes what you do, cut it.
- **The common mistake:** building a dashboard that becomes another place to maintain. Two failure shapes - a lane that holds its own copy of state and drifts out of sync with the real system, and a surface that slowly turns into a full editing tool with its own stale data. Both end the same way: you stop trusting it. Read-mostly, one source of truth per lane, or it dies in a month.
- **How you know it worked:** for a week, you start the day on this one surface instead of opening five tabs, and you stop being surprised by things you owned. The morning roll-up is short enough to read in under two minutes and every item on it is genuinely yours to move. If it is long, or full of other people's work, the triage is too loose.

## Rules

- MUST include only lanes where the operator personally takes action; monitoring-only surfaces stay off.
- MUST point each lane at exactly one system of record and mirror it, never hold a second copy of state.
- MUST keep the surface read-mostly - show and link out, do not rebuild every tool inside it.
- MUST separate the private working surface from any teammate-facing view; internal notes, scores, and labels never appear on a shared version.
- The daily roll-up MUST carry only items that need this person and have a reason to act now; in-progress work stays off it.
- NEVER let the command center become the system of record for work that lives elsewhere.
