---
name: launch-monitor
title: Launch monitor
description: |
  Use this skill when a product launch is live and you need to know what press, social,
  and developer communities are saying — and what to do about it. Produces a response
  war room report: a triaged signal feed with urgency levels and action badges, a
  mischaracterization tracker with copy-ready corrections, a competitor response panel,
  and a sentiment velocity read. Reach for it when someone says "monitor this launch",
  "track the launch", "what's being said about the launch", "what's the reaction to the
  announcement", "flag any mischaracterizations", "check press coverage for the launch",
  "post-launch coverage", or "how are competitors responding to our launch". Not for
  steady-state brand monitoring outside a launch window.
category: Signals
tags: [Marketing]
---

Applies from the moment a launch is public until the coverage wave dies — typically two to four weeks. Produces a triaged response war room report where every signal carries an urgency level, an action badge, and an exact source link, so the team knows what to respond to, correct, amplify, or escalate — in that order.

Replace before enabling: `{{ALERTS_CHANNEL}}` — where act-now items get flagged to the team; `{{COMMS_OWNER}}` — who receives escalations (comms, legal, or leadership).

## Before the first sweep

Do two research steps before asking the user anything:

1. **Resolve alternate names silently.** Search the live web for the product's codenames, former names, version names, API/SDK/repo names, and model identifiers — they are often different from the marketing name, and coverage splits across all of them. Fold every confirmed variant into your query list without showing the user this step. Query patterns are in `references/sources.md`.
2. **Confirm the launch date from evidence.** Search for when the product actually launched. Present what you found for confirmation; if announcement date and general availability differ, surface both and ask which window matters.

Then confirm in a single message: launch date, lookback window (default: launch to now), depth (quick scan vs deep sweep — default deep), and competitors to prioritize or exclude (default: on, identified automatically). If the user says "just run it", take every default. If the product name is ambiguous after research, disambiguate before spending a single search on the wrong product.

**Profile the product before querying.** Answer five questions from the announcement and a quick search: What category is it? What ecosystem does it live in? Who is the audience? What are the key launch claims? And — most important — what would a mischaracterization look like: wrong category, wrong price, wrong capability, wrong comparison? This profile decides which communities you sweep, and you cannot flag a mischaracterization without knowing what "correct" looks like.

## The sweep

Run parallel searches across four fronts — press, community, social, competitors — highest-reach sources first, because that is where a wrong claim does the most damage before you catch it. The full tiered source list, per-platform query patterns, and consumer-launch additions are in `references/sources.md`; read it before the first sweep of any launch.

Alongside the discovery queries, run the **mischaracterization hunt** every pass: targeted queries built from the context profile — the wrong claim you fear, the price, the wrong category, the capability it does not have, the wrong competitor comparison. Wrong information rarely surfaces in a generic sweep; you find it by searching for the specific error.

Use shallow, fast searches for discovery; extract the full page only for signals that survive triage and need exact quotes or reach estimates.

## Triage

Every signal gets four labels: an urgency level (act now / monitor / good signal / noise), an action badge (RESPOND, CORRECT, AMPLIFY, ESCALATE, WATCH, IGNORE), a signal type, and the **exact URL** of the article, thread, or post — never a homepage, never fabricated. The full rubric — urgency definitions, badge semantics, reach heuristics, and the materiality threshold that filters noise — is in `references/triage.md`; apply it to every signal, every run.

For each piece of coverage that gets something wrong, extract the six-field mischaracterization record (claim, source and reach, what's wrong, correct version, spread risk, suggested one-sentence correction) per the same reference — including a secondary search to see whether other outlets are already citing the wrong claim. Spread status (SPREADING / CONTAINED / CORRECTED) decides urgency more than the original outlet's size does.

## Sentiment velocity

Break the window into intervals — hourly for the first 24 hours, daily after — and count positive, negative, and neutral signals per interval. Identify the inflection point (when did sentiment peak or flip?) and flag any velocity spike, positive or negative: a sudden surge in mentions is itself a signal even before you read a single post.

## Memory and re-runs

Keep a running file per launch in your workspace. On every run, load it and dedup before writing output: fingerprint each signal as `{url, signal_type, published_date}` with URLs normalized (strip query params and trailing slashes). Already-known and unchanged → suppress from the main feed (appendix only, on request). Returning with changed urgency → keep in the feed, marked as returning. Lead the report with the honesty line: `X net-new · Y returning (urgency changed) · Z suppressed`. After the run, append the new fingerprints and carry forward every unresolved mischaracterization and open action item — a wrong claim is not done until its status is CORRECTED.

Re-run cadence: every 1–2 hours for the first 6 hours post-launch, every 3–4 hours until hour 24, then once or twice daily until momentum dies. On a re-run, sweep only since the last run timestamp and surface only what is new.

## The report

One format, every run: TL;DR first (sentiment read, act-now count, single most urgent item), the war room body in fixed section order, "What this means" last (trajectory read plus the one action to take now). The full section-by-section format spec — card fields, mischaracterization tracker layout, competitor panel, source index, and tone rules — is in `references/report-format.md`; follow it exactly.

After the report is delivered, flag act-now items to `{{ALERTS_CHANNEL}}` and route ESCALATE items to `{{COMMS_OWNER}}` — only after the user approves what gets posted. Suggested responses and corrections are always drafts for a human to send, never sent by you.

## What good looks like

- The best operator hunts for what's *wrong*, not what's *said*: the mischaracterization queries built from the context profile find the "it's just an X reskin" thread hours before it hits press, and the spread-risk search shows whether it is one Reddit comment or three outlets already citing each other.
- The mediocre version is a clipping service: a flat list of links, no urgency, no suggested action, homepage URLs, positive and negative mixed together — the user still has to do all the thinking. Or worse: a re-run that re-reports Tuesday's signals as if they were news.
- Output is good when the user can act in sixty seconds: the TL;DR names the single most urgent item, every act-now card carries a specific suggested action ("reply in the HN thread with the pricing page link", not "consider responding"), every correction is copy-ready, and every source link lands on the exact thread.

## Rules

- MUST include the exact article/thread/post URL for every signal, as returned by search. NEVER a homepage. NEVER a fabricated or reconstructed URL.
- MUST run the mischaracterization hunt on every pass, not just the first.
- MUST dedup against the launch's running file before output and lead with the net-new/returning/suppressed counts.
- MUST keep suggested responses and corrections as drafts — NEVER post, reply, comment, or send anything publicly or to a channel without explicit human approval.
- NEVER report a claim as spreading, or attach a reach number, without evidence found in the sweep — say "unverified" when it is.
- NEVER treat accurate neutral coverage as a problem to fix; flag it, don't prioritize it.
- NEVER count syndicated wire copy as multiple signals.
