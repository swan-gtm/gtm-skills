---
name: "forecast-creator-pipeline"
title: Forecast pipeline from creator spend
description: "Use this skill when creator budget needs a defensible forecast — \"what will €10K of creator spend produce,\" \"build the pipeline model for the creator channel,\" \"what ARR can we commit to from this program.\" A five-input model (budget, cost per qualified click, click→opportunity rate, win rate, ACV) with a worked example and the sensitivity insight that decides where tuning effort goes."
category: Influencers
---

Use when the creator channel needs a forward number leadership can hold you to. Produces a pipeline forecast from five inputs — all observable, none hand-waved.

## The five inputs

1. **budget (B)** — the quarter's spend
2. **cost per qualified click (C)** — from your own campaign history; network baseline ~€2.30–2.40
3. **click → opportunity rate (O)** — planning band 3–6% for a well-defined ICP audience
4. **opportunity → close rate (W)** — your actual sales win rate, from the CRM
5. **ACV** — real average contract value, from the CRM

Qualified click means tracked AND ≥30 seconds on-site — the behavioral definition is what makes the whole model honest.

## The model

qualified clicks = B ÷ C → opportunities = clicks × O → deals = opportunities × W → new ARR = deals × ACV → return = ARR ÷ B

Worked example at €10,000: 4,167 clicks → 167 opportunities (4%) → 33 deals (20% win) → €200K ARR at €6K ACV → 20× gross return. Run the conservative case too: at 3% and 15% the same budget returns €67.5K (6.75×). Present both — the range is the forecast.

## Where the leverage is

The opportunity rate dominates. Doubling it from 3% to 6% doubles pipeline; a ±30% swing in effective CPC moves the model by roughly a third. So tuning effort goes to audience-ICP fit and post quality (what moves O) before rate negotiations (what moves C). Sanity-check the downstream half against reality: click→SQL composites run ~3.4% in network data — a model implying far more should be challenged.

## What good looks like

A great forecast shows the formula, sources every input (own history where it exists, network baselines labeled as baselines where it doesn't), and presents a base and conservative case. A mediocre one multiplies best-case everything into a single big number. The overlooked failure: forecasting from CPL with a mushy lead definition — qualified-click-based models survive CFO scrutiny because the unit is behavioral, not declared.

MUST source W and ACV from the actual CRM, never from aspiration. MUST present a conservative case alongside the base. NEVER present a single-point forecast.
