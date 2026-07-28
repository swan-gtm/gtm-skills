---
name: persona-builder
title: Persona builder
description: |
  Use this skill when you need buyer personas for outbound off an ICP — "who do we message,"
  "build our personas," "our targeting keeps hitting the wrong titles." Given what a company
  sells and its ICPs, it returns clean, non-overlapping personas with job titles and each
  person's role in the deal.
category: Research
tags: [Research, Prospecting]
---

An agent that turns an ICP into the people you actually message. Its whole job is precision on *who* — the economic buyer, the daily user, and the champion are different people, and a targeting list that blurs them wastes outreach on the wrong titles.

## Input

- `product` — what the company sells and the pain it removes.
- `icps` — the ICP segment(s) to build personas for.

## Procedure

1. **Separate the roles in the deal:** the economic buyer (owns the budget), the daily user (feels the pain), and the champion (sells it internally). Each is its own persona.
2. **Assign titles in the person's own language,** not the company's org-chart language — how they would describe themselves, across the title variants and seniorities that ICP uses.
3. **Enforce one-title-one-persona.** A given title belongs to exactly one persona. If "Head of Growth" could sit in two, the personas are wrong — redraw them.
4. **State each persona's angle** — what they care about, which is different per role (buyer: outcome/ROI; user: friction; champion: looking good internally).

## Output

`personas[]`, each:

- `name` — the persona in plain language
- `titles` — the title variants that map here (no title repeated in another persona)
- `role_in_deal` — economic buyer / user / champion
- `in_icps` — which ICP segments this persona appears in
- `cares_about` — the one thing that moves them

## What good looks like

- **No title appears in more than one persona.** Overlapping title lists silently double-target and corrupt reply-rate reads — this is the single most common failure.
- **Titles are the person's language, not the company's.** "RevOps lead" over "Manager, Revenue Systems" if that is what they call themselves.
- **Buyer, user, and champion are distinct** — collapsing them into one "decision maker" persona hides who to actually open with.
- Good output: a targeting engine could route each title to exactly one persona with no ambiguity.

## Rules

- MUST keep every title in exactly one persona.
- MUST separate economic buyer, user, and champion into distinct personas.
- MUST use the person's self-description for titles, not internal org labels.
- NEVER create a persona without a concrete title set and a "cares about."
