---
name: competitor-positioning
title: Competitor positioning
description: |
  Use this skill when you need to know how competitors present themselves to the
  market — homepage messaging, value props, CTAs, pricing models, content themes —
  and how that evolves over time. Produces a marketing briefing: a messaging matrix,
  per-competitor positioning profiles, content gap analysis, a positioning white
  space map, and battlecard inputs, with before/after tracking of every shift.
  Reach for it when someone says "competitor positioning", "messaging comparison",
  "content gap", "what changed on their site", "landing page teardown", "marketing
  battlecard", "how do they describe their product", or "counter-messaging".
category: Positioning
tags: [Marketing]
---

Runs when a marketing team needs to see how competitors position themselves on their own websites and content — on a recurring cadence, before a messaging refresh, or ahead of a launch.

Produces a marketing briefing, not a signal feed: messaging matrix, positioning profiles, content gaps, white space, and recommended actions — every insight answering "what does this mean for our messaging?"

## Pick the mode before doing anything

Keep a running file per competitor in your workspace (format: `references/snapshot-format.md`). At the start of every run, load those files and check when you last ran:

- **Full snapshot** — first run, or no prior snapshots, or last run more than 14 days ago. Capture everything.
- **Delta mode** — last run within 14 days. Research the same pages, but the output reports only what changed. A delta run that re-narrates the whole landscape buries the one tagline change that matters.
- **Same-day repeat** — already ran today? Ask before re-running; don't silently burn research effort on pages that haven't changed since the morning.

If you also keep business-signal notes on these companies (funding, hiring, leadership changes), load those too — they often explain *why* positioning shifted, e.g. a funding round preceding an enterprise-messaging pivot.

## Confirm scope

Work from {{COMPETITOR_LIST}}. Four or fewer competitors: analyze all. More: ask which to focus on this run — group them by category and let the user pick. Every competitor costs real research time; don't spend it on companies nobody asked about.

## Capture your own baseline first

Before touching any competitor, capture your own positioning from {{YOUR_DOMAIN}} the exact same way you'll capture theirs — otherwise the messaging matrix has an empty row where "us" should be, and the comparison collapses into a list.

1. Map the site (sitemap or crawl) to find the real features/product and pricing URLs — don't guess paths.
2. Extract the homepage, features page, and pricing page as clean text: tagline, hero copy, primary CTA, value props, tier names.
3. If a page won't extract, note "page not accessible" and continue — a partial baseline beats none.

## Research each competitor in parallel

Run one research thread per competitor, all in parallel — the protocol is identical per company and none depends on another. Give each thread the competitor's name, domain, and its previous snapshot from your workspace (or "first run — no comparison"). The full per-competitor protocol — discovery, extraction order, search queries, and the exact output sections each thread must return — is in `references/research-protocol.md`. Read it before launching.

The shape: map the site structure first (what pages exist and don't exist is itself a positioning signal — no public pricing page usually means sales-led), then extract homepage / features / pricing, then find and read 2–3 recent blog posts and the case-study pages, then diff against the previous snapshot.

If a thread fails outright, run its steps directly yourself rather than dropping the competitor. If its blog haul is thin (fewer than 2 posts), pull additional posts from its search results before analyzing.

## Analyze for a marketing audience

Frame everything in the language the team works in: messaging hierarchy, battlecard inputs, content calendar implications. When reading blog content, look for recurring narratives, audience targeting (developers vs. executives vs. practitioners), whether they name competitors or position against a category, the keywords their titles chase, and content maturity (original research vs. generic how-tos).

Assemble the briefing using the exact structure in `references/briefing-formats.md` — full-snapshot layout or delta layout depending on mode. The non-negotiables:

- **Verbatim quotes** for taglines, CTAs, and value props. Paraphrase destroys the evidence — "streamline your workflow" and "ship faster" are different positioning even if they feel the same.
- **Every claim links to its source page.**
- **Deduplicate against the snapshots.** In delta mode, surface only genuinely new changes; say "no positioning changes detected" rather than padding.

## Save the snapshots

After the briefing, update your workspace — this is what makes the next run a delta instead of another cold start:

- Save the full briefing (not a summary) as the dated report of record.
- Update each competitor's snapshot file per `references/snapshot-format.md`, appending a dated entry to its History section describing what changed. The History section is the before/after trail battlecards and "when did they pivot?" questions draw on.
- Note the run date so the next run can pick its mode.

## Battlecards on demand

When someone asks for a battlecard on a specific competitor, build it from that competitor's snapshot plus your own baseline using the battlecard layout in `references/briefing-formats.md`. If the snapshot is missing or older than 14 days, refresh that one competitor first — a battlecard built on stale messaging gets a rep corrected in a live call. The battlecard must include a "Where they win" section written honestly; a battlecard that claims you win everywhere is one sales will stop trusting.

## What good looks like

- The best operator reads the site *structure* before the copy: a pricing page that disappeared, a new `/enterprise` path, a docs subdomain appearing — architecture shifts telegraph strategy quarters before the blog admits it.
- The mediocre version is a screenshot tour: paraphrased taglines, no baseline row for your own company, no memory between runs, every run a "full snapshot" that never says what changed — and insights with no "so what" for the messaging team.
- Output is good when the messaging matrix quotes are verbatim and sourced, delta mode reads in under two minutes because it contains only changes, each recommended action names a competitor claim and the counter-move, and a snapshot file's History section lets you reconstruct exactly when a competitor's story pivoted.

## Rules

- MUST use verbatim quotes for taglines, CTAs, and value props — never paraphrase quoted messaging.
- MUST link every claim in the briefing to the source page it came from.
- MUST capture your own baseline in every full-snapshot run before comparing.
- MUST update the per-competitor snapshot files after every run, including a dated History entry.
- NEVER present a guess about an inaccessible page as extracted data — write "page not accessible" and move on.
- NEVER pad a delta report with unchanged material; "no positioning changes detected" is a valid, complete finding.
- NEVER produce a battlecard without a "Where they win" section.
- NEVER analyze business signals like funding, hiring, or product launches here — that's a separate research motion; this skill covers only how companies present themselves.
