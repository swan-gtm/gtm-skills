---
name: seo-intel
title: SEO intel
description: |
  Use this skill when you need SEO answers grounded in live data instead of a tool's
  guessed metrics: keyword research, rank checks, a technical site audit, content gap
  analysis against competitors, reverse-engineering a competitor's on-page strategy, or
  an AI-visibility audit of how often AI assistants mention and cite your brand.
  Produces an evidence-backed report per play — every keyword, gap, finding, and score
  traceable to a real search result or extracted page. Covers "what should we rank
  for", "why did rankings move", "SEO audit", "technical SEO", "keyword difficulty",
  "topic clusters", "content gap", "competitor keywords", "SERP analysis", "AI
  visibility", "AI citation audit", "AEO", "GEO", and "do AI Overviews mention us".
category: SEO
tags: [Marketing]
---

# SEO intel

Runs whenever an SEO question needs a live-data answer: what to rank for, what is technically broken, what competitors cover that you don't, whether AI assistants cite you. Produces one report per play, with every claim tied to an observed search result or extracted page.

## Ground rules

- **Only observed evidence.** Every difficulty score, gap, and finding must trace to a real search result or a page you actually extracted. Never quote search volume, domain authority, or traffic numbers you did not measure — if a metric is unavailable, say "not measurable" instead of inventing it.
- **Source URL on every row.** Every keyword opportunity, content gap, and AI citation in a report carries the URL that proves it.
- **Partial data is reported as partial.** If a platform was unreachable or a crawl came back incomplete, score from what returned and state the coverage gap. Never backfill.

## Route the request

| The user wants | Play | Read first |
|---|---|---|
| Keywords to target, topic clusters, difficulty | Keyword research | `references/serp-and-keywords.md` |
| Current positions, ranking movement | Rank check | `references/serp-and-keywords.md` |
| Technical/on-page health, "SEO audit" | Site audit | `references/site-audit-checks.md` |
| Topics competitors cover that they don't | Content gap | `references/content-gaps.md` |
| A competitor's on-page playbook at scale | Competitor reverse-engineering | `references/content-gaps.md` |
| Brand presence in AI answers, AEO/GEO | AI visibility | `references/ai-visibility.md` |

If the request is generic ("help me with SEO"), ask which of these they need — don't guess. After finishing one play, suggest the natural next one (audit → keyword research → content gap → rank check), carrying forward the domains, keyword lists, and crawl data already gathered instead of re-collecting.

## Running memory and delta modes

Keep a running file per domain (and per brand, for AI visibility) in your workspace: audit findings, rank snapshots, gap lists, AI-citation snapshots — dated, structured, append-only. On every run, load the prior snapshot first and pick a mode:

- **Full mode** — first run, or the last run is more than 14 days old. Report the whole landscape as a baseline.
- **Delta mode** — a snapshot exists from the last 14 days. Diff against it and lead with what changed: new gaps, resolved findings, position movers, citations gained or lost. Unchanged items go to an appendix, not the summary.
- **Same-day repeat** — a report from today already exists. Ask before re-running; don't silently burn a second pass on identical data.

Delta framing is the discipline that keeps repeat reports readable: the executive summary carries only NEW and WORSENED items, resolved items are noted as wins, and everything else stays in the breakdown sections.

## The plays

**Keyword research.** Expand the user's topic into 15–25 seed variations (modifiers, long-tail questions, commercial variants, adjacent concepts), sweep the live results page for each, and score what you actually see: who ranks, how deep their content is, which result-page features appear. Classify intent and AI-surface type from the result-page composition — not intuition — then cluster into pillars and rank by `(relevance x intent value) / difficulty` into Quick Wins, Growth Targets, and Moonshots. Rubrics, formulas, and the report format are in `references/serp-and-keywords.md`.

**Rank check.** Normalize each keyword, search it, and match the target domain against the top 20 organic results by root domain — recording the first (highest) match. Snapshot every run; on re-runs compute deltas and classify moves (major / notable / stable / new entry / drop-out). For unranked keywords, still record which result-page features appeared and who holds the top spots. Query normalization, domain-matching, feature taxonomy, and delta thresholds are in `references/serp-and-keywords.md`.

**Site audit.** Map the site (sitemap included, so orphans surface), sample pages representatively — homepage, primary landing pages, a cross-section per section, paginated pages, a few sitemap-only orphans — and extract each page's head metadata and body content, escalating to JS rendering when extraction comes back empty. Run the seven check categories (meta tags, headings, schema, internal links, content quality, technical foundations, observational Core Web Vitals), tag each finding with a severity and a confidence tier, dedup against the prior audit, and grade overall health A–F. The full rule set with thresholds lives in `references/site-audit-checks.md` — run the checks from that page, not from memory.

**Content gap.** Map your site and 1–3 competitor sites in parallel, extract every page's topics, and build a coverage matrix: topic clusters as rows, domains as columns. A gap is a topic where a competitor has pages and you have none — or your coverage is under 30% of their depth. Then validate each gap against live search results before recommending it: a competitor page that doesn't rank is a much weaker signal than one in the top 10. Score by `(rank strength x relevance) / effort` and bucket into Quick Wins, Strategic Bets, Nice-to-Have. Full logic in `references/content-gaps.md`.

**Competitor reverse-engineering.** Crawl a competitor's site at scale and read their strategy out of the on-page elements: keyword themes from titles/H1s/H2s, hub-and-spoke structures from body-only internal anchors, title formulas, publishing velocity, meta-description CTAs. The filtering rules that keep this honest (boilerplate H2 and anchor stripping, exact-URL hub matching) are in `references/content-gaps.md`.

**AI visibility.** Build 20–40 queries a buyer would actually ask an AI assistant, run each against the AI platforms you can reach (asked as natural questions, not keyword strings), and analyze each answer for brand mentions, domain citations, sentiment, and competitor presence — with a false-positive guard for common-word brand names. Compute visibility score, share of AI voice, and citation rate; the competitor-visible-you-absent queries are the priority list. Then recommend fixes from the measured GEO methods (citations, statistics, quotations lead) and check that AI crawlers aren't blocked in robots.txt — if bots can't crawl, nothing else matters. Detection rules, scoring formulas, per-platform profiles, and the GEO playbook are in `references/ai-visibility.md`.

## What good looks like

- The best operator reads the results page before scoring anything: difficulty comes from who actually ranks and how deep their content is; intent comes from what kind of pages Google chose to show; a gap only counts after the competitor's page was seen ranking. The evidence chain never breaks.
- The best operator notices structure others miss: an AI Overview on a keyword changes the content recommendation; a competitor's hub page changes the effort estimate; a "brand mention" that's really a common English noun gets caught by the proximity check.
- The mediocre version quotes difficulty scores and search volumes from nowhere, treats every competitor page as a gap without checking whether it ranks, re-reports the same 40 audit findings every run with no delta, and counts navigation links as internal-linking strategy.
- Output is good when a stranger can verify any row of the report by opening its source URL, when a repeat run's summary contains only what changed, and when every recommendation names the specific page or query it came from.

## Rules

- MUST tie every reported keyword, gap, finding, and citation to a source URL or extracted page.
- MUST load the prior snapshot before a repeat run and lead the report with deltas, not a re-baseline.
- MUST state coverage honestly: pages that failed extraction, platforms that were unreachable, gaps that went unvalidated — all named in the report.
- MUST ask before re-running a play already run the same day for the same target.
- NEVER fabricate or estimate metrics you did not measure — no invented search volumes, authority scores, or traffic figures.
- NEVER score from a stale snapshot as if it were fresh — data older than the run's window is background, not evidence.
- NEVER let one failed extraction or unreachable platform abort a run — skip, note it, and complete the rest.
