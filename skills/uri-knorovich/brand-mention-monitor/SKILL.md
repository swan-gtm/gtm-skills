---
name: brand-mention-monitor
title: Brand mention monitor
description: |
  Use this skill when you need to know what people are saying about a brand across
  the web and social — "monitor brand mentions", "what are people saying about
  [brand] this week", "run a brand sweep", "social listening", "find high-risk
  mentions", or "how does [brand] compare to [competitor] in the conversation".
  Sweeps social platforms, news, forums, and review sites; scores every mention on
  reach, velocity, sentiment, and risk-topic match; and produces a triage report
  bucketed into Crisis / Watch / Engage / Log with a suggested owner and response
  window for each mention, so the team responds before one spirals.
category: Signals
tags: [Marketing]
---

Run this when anyone needs eyes on the brand conversation — a routine weekly sweep, a launch-week watch, or a "something feels off" check. It produces a triage report: every mention scored on four dimensions, deduped against what previous runs already found, and bucketed into Crisis / Watch / Engage / Log with an owner and a response window.

## Before the sweep — resolve, profile, confirm

Do two research steps before asking the user anything:

1. **Resolve brand variants.** Search the live web for the brand's alternate spellings, hashtags, handles, product names, and sub-brands that get mentioned independently. For common-word brand names, find the disambiguating terms (industry, founder, domain) so the sweep doesn't pull unrelated noise. Fold every confirmed variant into the query list silently — never ask the user to supply this.
2. **Profile the brand.** Establish B2B vs B2C, industry, primary geography and language, and rough audience size. This picks the source profile and calibrates scoring — "high reach" means something different for a niche B2B tool than for a consumer app with millions of users.

Replace before enabling: {{CRISIS_OWNER}} (who gets flagged on a Crisis hit) and {{ALERTS_CHANNEL}} (the team channel, if any, for Crisis/Watch pushes).

Then confirm scope in a single message: the brand as you understood it plus any competitors to track alongside, the date window (default: last 7 days), depth (quick scan vs deep sweep; default deep), and who gets flagged on a Crisis-tier hit ({{CRISIS_OWNER}} — a PR lead, legal, founder, or the marketing team by default). Skip the questions entirely when the user already provided the answers or a prior run in this workspace configured them. If the brand name is still ambiguous after research, confirm which entity is meant before running anything.

## Pick the source profile

The single most important configuration step. Do not scan all platforms equally — weight the channels where this brand's audience actually talks. B2B brands live on LinkedIn, G2, Hacker News, and trade press; consumer brands on TikTok, Instagram, YouTube, and Trustpilot; regulated industries on wire services, regulatory watchdogs, and journalist accounts; regional brands on local-language platforms. Read `references/source-playbook.md` for the five market profiles and the full per-platform query patterns before building the query list.

## Sweep

Fan out parallel searches, one stream per source group (social, news and press, review platforms, community forums), every query bounded to the confirmed date window. Run a shallow discovery pass first across all streams; extract full page or thread content only for candidates that look high-impact — that is where the scoring evidence (engagement counts, reply tone, author profile) comes from. Every pass runs three query families: broad brand queries, risk queries (lawsuit, outage, scam, recall — tuned to the industry), and opportunity queries (organic praise, purchase intent, comparison wins). If one stream fails, continue with the rest and name the gap in the report — never silently present a partial sweep as complete.

## Score every mention

Four dimensions, each 0–100: **reach** (how many people can see this), **velocity** (how fast it is gaining ground — the differentiator between "viral forming" and "stale"), **sentiment** (scored separately for risk and opportunity), and **risk-topic match** (legal, safety, outage, executive controversy, misinformation). Composite:

```
composite = reach x 0.30 + velocity x 0.30 + max(risk_sentiment, risk_topic) x 0.25 + opportunity x 0.15

Dimension scores are additive rows capped at 100 each — see the rubric for the cap rule and why the Crisis bar sits at 65.
```

Velocity has an honesty gate: hourly growth rates need two data points. On a first pass with no baseline, score only observable proxies (cross-platform pickup, press pickup of a social post, crisis-scale absolute engagement) and label the velocity `~estimated`. The full point tables, baseline rules, and the rapid re-check upgrade path are in `references/scoring-rubric.md` — read it before scoring anything.

## Dedup against brand memory

Keep a running file per brand in your workspace. On each run, load it, fingerprint every found mention as `{url, platform, published_date}` (URLs normalized), and split the feed: net-new, returning-with-score-shift, and already-known-unchanged (suppressed to Log). Lead the report with the split: `X net-new · Y returning (score changed) · Z suppressed`. After the run, persist the new fingerprints and scores. Windowing, carry-forward, and cadence rules are in `references/rerun-and-memory.md`.

## Tier and route

Assign every mention exactly one tier — teams act on tiers, not numbers.

| Tier | Score | Action | Suggested owner | Window |
|---|---|---|---|---|
| Crisis | 65+ | Route immediately | {{CRISIS_OWNER}} + legal + leadership | Respond < 2h |
| Watch | 45 up to 65 | Assign owner, monitor velocity | Marketing / comms | Respond < 24h |
| Engage | Any score, positive + high reach | Amplify, thank, share | Marketing / social team | Act within 48h |
| Log | < 45, no risk signals | None — searchable record | — | — |

Crisis mentions surface first, each as a full decision card: excerpt, all four scores, why it was flagged, who responds, by when, and a suggested draft action. If the user wants Crisis and Watch items pushed to a team channel ({{ALERTS_CHANNEL}}), post only those tiers — never the full feed.

## Write the report

Follow `references/output-format.md` exactly: TL;DR up top, then the triage sections in fixed order, closing with a "What this means" section carrying one to three recommended actions, each tied to a tier and an owner. On a first run, note that a second pass in a few days establishes the velocity baseline and trend lines.

## What good looks like

- The best operator reads velocity before volume — a 40-minute-old post already at thousands of reposts outranks last week's big thread every time — and picks the source profile before writing a single query, because B2B risk hides in G2 review clusters while a generic sweep is busy reading consumer social noise.
- The mediocre version is a flat list sorted by follower count: every platform weighted equally, velocity "scored" on a single snapshot with no baseline, homepages pasted as source links, and re-runs that re-report everything last week's run already surfaced.
- Output is good when every Crisis card is actionable in 60 seconds (excerpt, exact link, reason, owner, window, draft action), the dedup summary line proves the run only surfaced what is new, and any mention can be re-found from its exact URL a month later.

## Rules

- MUST link every mention to the exact post/article/thread URL — never a platform homepage.
- MUST label first-pass velocity scores `~estimated`; hourly-rate points require a prior measurement.
- MUST bound every query to the confirmed date window and state that window in the report header.
- MUST persist mention fingerprints after every run and carry Crisis and Watch items forward until the user marks them handled.
- NEVER fabricate engagement counts, follower numbers, or sentiment — when a value can't be verified from the page, say so on the card.
- NEVER publish, post, or send any response on the brand's behalf — suggested actions are drafts that require explicit human approval.
- NEVER suppress a returning mention as a duplicate when its composite score moved 10+ points — a score shift is news.
