---
name: competitor-monitoring
title: Competitor monitoring
description: |
  Use this skill when you need to know what rival companies are doing — "what are
  my competitors doing", "competitor update", "competitor news", "competitive
  landscape", "market intel", "what's new with [company]", "track [company]",
  "competitor briefing", "who's making moves", "we keep losing deals to
  [company]" — or before a board meeting, battlecard refresh, or strategy session
  that needs competitive context. Produces a structured intelligence briefing —
  funding, M&A, leadership moves, product launches, hiring waves, partnerships —
  with every signal date-verified against its primary source and deduped against
  a running memory file per competitor, so each run surfaces only what is new.
category: Research
tags: [Sales, Marketing]
---

# Competitor monitoring

Runs whenever someone needs a current read on the competitive landscape — on a cadence, before a strategy conversation, or the moment a rival's name comes up in a lost deal. Produces a dated, source-linked intelligence briefing of genuinely new competitor moves, plus an updated running memory per competitor so the next run starts where this one ended.

The failure mode this skill exists to prevent: a briefing that confidently reports last quarter's funding round as this week's news because a recap article was published yesterday. Everything below is built around one distinction — **when a page was published vs. when the event actually happened** — and a memory that remembers what you already reported.

## Set up the profile (first run only)

1. Ask for the company's website domain, then search the live web for the domain to confirm you have the right company. Confirm with the user before proceeding.
2. Build the competitor list one of two ways: the user names them, or you propose them — run three parallel searches ("[Company] competitors", "[Company] vs", "[Company] alternatives"), synthesize a candidate list, and get explicit confirmation. Never research a competitor list the user hasn't approved.
3. For each confirmed competitor, capture name, domain, and category (direct, adjacent, incumbent). Also capture 2–3 industry keywords for trend searches.
4. Save all of this to a profile file in your workspace, alongside a `competitors/` directory that will hold one running memory file per competitor and a `briefings/` directory for saved runs.

## Pick the run mode

Check the profile's last-run date before searching anything:

- **Full mode** — first run, or last run more than 14 days ago. Search window: the past 14 days. Output: the full briefing.
- **Quick refresh** — last run within 14 days. Search window: since the last run, but never narrower than 7 days (too-narrow windows return empty results and read as false quiet). Output: the short delta format.
- **Same-day repeat** — a report already exists for today. Ask before re-running: "Already ran today — run again for fresh data?" Never silently re-run; it burns effort to produce a near-identical report.

## Load memory before searching

Read each competitor's running memory file and collect the signals already reported. These known signals are the dedup baseline: anything you find that matches one is not news, no matter how fresh the article covering it looks. Pass the known-signal list into each research thread so it can skip them at the source.

## Fan out the research

Research each competitor in parallel — one thread per competitor if your setup supports parallel work, sequentially otherwise. Per competitor, run the five-query fan-out: news, funding/M&A/hiring, their own changelog or release-notes page, real-time social announcements, and review-site movement. Read `references/query-patterns.md` for the exact query shapes, the changelog-extraction step, fallbacks for thin results, and scope caps.

In the same pass, run two industry-trend searches from the profile's keywords, and two searches on the user's own company (site-restricted product updates + news) so the briefing can contrast "them" with "you."

## Validate every signal before it enters the report

This is the gate that separates intelligence from noise. For each candidate signal, record both dates — article date and event date — classify its source type, assign a priority (P1: M&A, leadership changes, major funding, direct product competition; P2: launches, partnerships, hiring waves; P3: blog posts, comparison articles, minor hires), then classify it NEW, UPDATED, STALE, or UNCERTAIN. Only NEW and UPDATED survive. Any P1 signal sourced only from derivative coverage must be corroborated against a primary source before it can appear — this is a hard gate, not a preference. Read `references/signal-validation.md` for the date-extraction rules, source hierarchy, freshness table, verification budget, and the per-signal record format.

Extract the full page (not just the search snippet) for every P1 signal and for any signal whose date you can't pin down from the snippet. Determine the event date from the article body — datelines, "last September", "today announces" — not the page header.

## Build the briefing

Full mode gets the structured briefing (TL;DR of 3–5 P1 signals, per-competitor sections with a "where they win vs. where you win" read, industry trends, your-company update, cross-competitor patterns, strategic implications). Quick refresh gets the short delta: new signals, explicit "nothing new" list, action items only if something demands attention. Read `references/briefing-format.md` for the section-by-section spec of both formats.

If a competitor produced nothing new, say exactly that. "Nothing notable this period" is a valid, valuable finding; padding it with stale context destroys the reader's trust in every future briefing.

## Save and remember

Persist only signals that passed validation — STALE and UNCERTAIN signals never enter memory, or they'd pollute every future dedup. Save the full briefing to `briefings/`, append validated signals to each competitor's memory file in the entry format from `references/briefing-format.md`, and update the profile's last-run date. When this run covered 3+ competitors, also refresh the cross-competitor landscape synthesis described there.

Offer to share the briefing wherever the team reads updates — but only send it after the user explicitly approves the destination.

## Follow-ups

Go deeper on one competitor (focused searches on the thread that mattered), add a competitor (update the profile, create a memory stub), or skip one going forward (record the preference in the profile).

## What good looks like

- The best operator's first move on any exciting headline is to find the event date, not to write the bullet. A syndicated article published yesterday about a funding round from March is the single most common way competitor briefings lie — and the first thing an expert screens out.
- The mediocre version is a pasted list of search-result headlines: undated, unsourced, half of them repeats of last month's report, padded with "competitor X continues to invest in AI" filler. If the reader can't tell what's actually new since last time, the run failed.
- A good briefing passes three checks: every TL;DR item carries a verified event date and a clickable source; a reader who saw the previous report finds zero repeated signals; and quiet competitors are explicitly listed as quiet rather than inflated with background context.
- A good quick refresh is short. Shrinking output when nothing happened is the skill working, not the skill failing.

## Rules

- MUST verify the event date of every reported signal from page content — never trust the article's publication date alone.
- MUST corroborate every P1 signal that is only derivative-sourced against a primary source (company blog, press release, official filing) before reporting it. No corroboration → drop it.
- MUST dedup against per-competitor memory and surface only NEW or UPDATED signals.
- MUST get explicit user confirmation of the competitor list before the first research run, and explicit approval before distributing a briefing anywhere.
- NEVER include STALE or UNCERTAIN signals in a report or in memory — not as footnotes, not as "background context."
- NEVER pad a quiet period. Better to miss a real signal than to report a stale one as new — trust is the product.
