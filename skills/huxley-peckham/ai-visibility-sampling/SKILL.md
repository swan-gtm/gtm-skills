---
name: ai-visibility-sampling
title: AI visibility sampling
description: |
  Use this skill when an AI-visibility number needs to be trusted, defended, or compared
  over time — "is this score real," "the engine said something different an hour later,"
  "did our AI visibility actually move this week." Re-asks every question multiple times
  per engine, majority-votes presence, and keeps the verbatim answers as receipts, so
  every claim traces to evidence.
category: AEO
tags: [Marketing]
---

Use when brand presence in AI answers is being scored, compared, or reported over time. Produces a per-question presence verdict with vote counts, backed by the full answer text as evidence.

## Sample before scoring

Answer engines are stochastic: the same question, asked twice in the same hour, returns different answers with different names in them. A score built from one ask per question is noise wearing a number. Ask every question at least three times per engine, capture each full answer verbatim, and let a majority vote decide presence. Keep the vote visible in the output — a question won three-of-three is a different fact from two-of-three, and the margin is where next month's movement shows first.

## Define what counts as present

Three different events hide inside "the brand showed up": named as a recommendation (the engine offers the brand as an answer to the buyer's question), mentioned in passing (the name appears without endorsement), and cited as a source (the brand's site fed the answer). Decide the tiers before scoring and apply them mechanically. The strictest tier — named as a recommendation — is the one that predicts buyers arriving; report it separately, never blended.

## Score questions, not brands

One aggregate score hides everything an operator can act on. Build the readout as a grid: question by engine, vote count in each cell. The aggregate can sit on top, but the grid is the product — it shows which questions are won, which are contested, and which engine disagrees with the rest.

## Read movement honestly

Re-measure the same question set on a fixed cadence. A flip from zero-of-three to three-of-three is movement; a wobble at the margin is weather. When the question set has to change because the buyer's language moved, mark a break in the series and restate the baseline. Splicing old and new sets into one line manufactures trends that never happened.

## What good looks like

The best operators read variance before they read the score: an unstable answer means the engine is undecided, and undecided questions are the winnable ones — that instability list is the work queue. The mediocre version is a single-shot scan producing one aggregate number, no raw text kept, and a question set that quietly changes between measurements, so nothing can be traced or compared. Good output lets a skeptic pick any cell in the grid and be shown the dated, verbatim answers behind it in one step.

## Rules

- MUST keep the full verbatim text of every sampled answer, dated.
- MUST show vote counts, never just the verdict.
- NEVER score from a single ask per question.
- NEVER splice measurements across a changed question set without marking the break.
