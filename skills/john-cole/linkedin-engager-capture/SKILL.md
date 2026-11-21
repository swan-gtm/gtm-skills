---
name: linkedin-engager-capture
title: LinkedIn engager capture
description: |
  Use this skill when a tracked creator or customer champion posts about your product
  on LinkedIn and you want ICP-fit engagers as scored leads. It verifies the post is
  about you, collects the full engager list, resolves person to company, gates on ICP,
  scores, and posts a digest. Detection and scoring only — no outreach. Trigger phrases:
  "capture engagers from this LinkedIn post", "who engaged with that influencer post",
  "pull reactors and commenters into the pipeline".
category: Signals
tags: [Sales, Demand Gen]
---

When a tracked creator publishes a company-focused LinkedIn post, produce a deduped
list of ICP-fit engagers with company, persona fit, and lead tier — then a short digest
for the signals channel. No outreach from this skill.

## Template placeholders

Replace every `{{...}}` before enabling. Full wiring options live in
[references/apify-opt-in.md](references/apify-opt-in.md).

- `{{COMPANY}}` — product/company name as it appears in posts
- `{{INTERNAL_DOMAINS}}` — your company domain(s)
- `{{TEAM_MEMBERS}}` — full names of teammates to exclude
- `{{SIGNALS_CHANNEL}}` — channel for per-lead alerts and the digest
- `{{ICP_SEGMENTS}}` — concrete segment names plus obvious exclusions
- `{{TIER_SCALE}}` — lead tiers low→high (default Bronze / Silver / Gold / Diamond)

## The play

### 1. Verify the post is about {{COMPANY}}

Read the post. Proceed only when {{COMPANY}} is the primary subject (review, demo,
sponsored mention, or clear recommendation). Stop when {{COMPANY}} is a list item,
a tangential mention, or a competitor post.

### 2. Collect every engager

Do not trust a streaming trigger list alone — it is almost always incomplete. Fetch
the post's full comment and reaction list with your post-engagement scraper (optional
Actor wiring and field map:
[references/apify-opt-in.md](references/apify-opt-in.md)). Paginate until coverage is
complete. Extract name, profile URL, and headline. Deduplicate against prior runs on
the same post.

Skip: company pages, the post author, {{TEAM_MEMBERS}}, anyone at {{INTERNAL_DOMAINS}}.

### 3. Resolve person → company

Resolve each remaining profile to a current employer with your profile/enrichment
tools. Never invent a company from a headline alone. Drop rows you cannot resolve
after one paid enrichment attempt.

### 4. ICP gate before scoring

Keep only companies that match {{ICP_SEGMENTS}}. This is where most engagers should
die. When unsure, drop — false positives burn AE time.

### 5. Score and digest

Score remaining accounts on your usual lead rubric. Cap the digest at the top 25 by
tier, then engagement recency. Post one digest to {{SIGNALS_CHANNEL}} with: post URL,
engager count kept/dropped, and a table of name / company / tier / why kept. Route
outreach downstream — this skill never sends messages.

## What good looks like

- The first filter is topical honesty: if the post is not really about {{COMPANY}},
  you stop with zero engagers processed.
- The engager list matches the public post, not the subset the trigger streamed.
- ICP kills the majority of names before scoring; a digest that keeps everyone is wrong.
- Every kept row has a resolved company and a one-line reason tied to {{ICP_SEGMENTS}}.
- Common failure: scoring headline keywords as ICP, or re-processing the same commenters
  on every trigger fire for the same post.

## Rules

- MUST confirm cost and schema before any paid scrape or enrichment run.
- MUST dedupe engagers against prior runs on the same post URL.
- NEVER invent employers from headlines.
- NEVER send outreach, connection requests, or CRM bulk writes from this skill.
- NEVER hardcode secrets or send reader data to endpoints they do not own.
