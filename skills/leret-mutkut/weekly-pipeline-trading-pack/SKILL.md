---
name: weekly-pipeline-trading-pack
title: Weekly pipeline trading pack
description: |
  Use this skill when someone needs the weekly pipeline pack, trading pack, pipeline review or weekly commercial readout — the recurring read on whether the week traded green, what moved in the funnel week on week, and when current pipeline is expected to convert to orders and billing.
  Produces an editable KPI-and-commentary pack from a CRM opportunity export plus orders and target figures. Use it for phrases like "build this week's trading pack", "how did pipeline move this week", "are we still at 3x cover", "did we trade green", "when does this pipeline land as orders", "which sector is underperforming", "pipeline slide for the trading call".
category: RevOps
tags: [RevOps]
---

Runs weekly, on the trading cycle, for commercial trading, planning, performance and CVM teams working from a pipeline snapshot.

Produces an editable pack: headline verdict, KPIs across a chosen cut, and written commentary.

## Establish the inputs

Ask for what you need and accept it in whatever form the user has it — typed figures, pasted text, an uploaded file, or a live connection to the source. Do not insist on a format. Say what you need in plain commercial terms and let the user map their columns once.

Required:

- **Open opportunities**, one line per opportunity: identifier, account, value, stage or status, expected billing date, product, sector, segment, owner.
- **Orders booked and the orders target** for the period. These usually come from finance rather than the CRM. Raw numbers are fine.

Strongly wanted:

- **The previous week's opportunity snapshot.** Movement is the point of this pack. Without it, run a point-in-time read and state plainly that week-on-week movement could not be assessed.

Never guess a target or an orders figure. Ask.

## Ask before analysing

The story changes weekly, so confirm three things — offer defaults and proceed if the user skips them:

1. **Which cut leads** — sector, public/private/SMB, or product. Default: sector.
2. **The angle** — a single large deal, comparative sector performance, or who is behind on target. Default: comparative performance.
3. **Commentary length.** Default: short.

## Read the week

- **Orders against target.** This is the headline and the only thing that decides green. Pipeline growth never decides it.
- **Pipeline cover** — open pipeline against target, measured against 3x. Check whether one large deal is carrying it before reporting it as healthy.
- **Movement** week on week and month on month: what was added, what converted, what slipped, what disappeared without being closed out.
- **Top five won and top five lost.**
- **ARPU and win rate** across the chosen cut.
- **Billing expectation profile** — when the current pipeline is expected to land, read from the expected billing date rather than inferred.

## Build the pack

Output an editable KPI pack with commentary against each number. HTML by default, since it edits and converts cleanly to PDF or image. Lead with the green/not-green verdict in the first line.

Where a segment underperforms, name the owner covering it so the reader knows who to ask. This is a pointer, not an individual scorecard.

## What good looks like

The first line answers whether the week traded green, and the rest earns its place by explaining movement rather than restating the export. A weak version reports the whole pipeline back at the reader; the volume is exactly what the reader was trying to escape.

The most common error is treating pipeline growth as good news. Cover inflated by deals with distant or missing billing dates is not cover. The quality bar for pipeline is conversion to orders, not size.

Commentary should tell the reader what changed and what it means for hitting target, in the fewest words that survive scrutiny on the call.

## Rules

- MUST state the as-of date of every input on the pack.
- MUST state what could not be assessed when an input was unavailable.
- MUST check whether pipeline cover depends on a single large deal before calling it healthy.
- NEVER declare a green week on pipeline movement alone.
- NEVER fabricate orders, targets or billing dates.
- NEVER present the pack in a form the user cannot edit.
