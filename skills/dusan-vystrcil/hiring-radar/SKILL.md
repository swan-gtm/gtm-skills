---
name: hiring-radar
title: Hiring radar
description: |
  Use this skill when job postings should be watched as buying signals —
  continuously, with no outreach. Runs daily over watched accounts plus job
  descriptions matching tracked queries, keeps only the hiring patterns that
  matter to your GTM (hiring spree, buyer-persona hire, build-vs-buy,
  competitor tool in JD), and lands each signal on the account record with a
  per-signal alert and a reconciled digest. Built for inbound, PLG, and
  relationship-led motions. Detection and classification only — it never
  drafts or sends outreach.
category: Signals
tags: [Sales]
---

Run when target accounts' job postings should work as buying signals. Produces
classified signals with dated evidence, a per-signal alert, and a reconciled
digest — detection only, never outreach.

Run this daily to keep a live picture of who is building what across your
target accounts. Hiring is budget made visible: a team being built today is a
tooling decision being made this quarter.

**Setup state.** Not yet configured for this org. Before scheduling,
configure: the account watchlist (tier-A daily, rest weekly), the mention-scan
queries (competitor and own products, watched role titles), the signals
channel, and your own-domain exclusions. Maintain the configuration of connectors from job-board-sourcing-and-actor-schemas.md here. After setup, rewrite this paragraph
to describe the current configuration.

## Step 1 — Pull fresh postings (two scans, never conflated)

**Watchlist scan**: jobs posted BY watched accounts — company-filtered.

**Mention scan**: jobs at ANY company matching a tracked query — a role title
("data engineer"), a technology in the JD ("SharePoint"), or both
("administrator" + your platform). A JD that mentions a watched company is
NOT that company's hiring signal. Pull everything since the last run,
paginated to the end. Drop your own postings — a query on your own product
returns your own ads. LinkedIn only through native
integration, never a third-party scraper; other boards one vetted, test-run
scraper each — schemas and the vetting protocol are in
[references/job-board-sourcing-and-actor-schemas.md](references/job-board-sourcing-and-actor-schemas.md).

## Step 2 — Keep only GTM-relevant patterns (the threshold)

Tune to your GTM; everything else is log-only:

- **Hiring spree** — 3+ fresh roles, same team → tooling decisions being made
  now
- **Buyer-persona hire** — "first" / "Head of" the persona you sell to → a new
  owner with a 90-day agenda
- **Build-vs-buy tell** — JD describes building what you sell → funded,
  unstaffed, still open
- **Executive hire** in your buying committee → their first quarter decides
  what stays
- **Competitor tool required in a JD** → displacement intel
- **Your product required in a JD** → a customer signal for the CS owner


Single postings, category-term-only mentions, evergreen and reposted listings drop — a pattern is only real if the posted dates are.

## Step 3 — Resolve and gate

Resolve the true employer behind agency-posted listings, or drop them. Then
gate mention-scan finds to ICP: non-ICP dies here as a log entry, never an
alert.

## Step 4 — Dedup and suppression ledger

Check account memory for `Last hiring signal: YYYY-MM-DD (pattern)`. The same pattern within 30 days doesn't re-alert — new postings attach as evidence. An active deal never re-alerts as new: flag as "warm signal on active deal" for the deal owner. **Write the ledger note for every account processed or skipped, with the reason.**

## Step 5 — Read, log, alert

Read the surviving JDs — named tools, team-size hints, reporting line, pain
language — and log those words to the account record with scan of origin,
class, roles, posted dates, and links. Then one per-signal message to the
signals channel: the account, the pattern with dated links, who likely owns
the consequence, and one line on what it means. **One pattern = one alert**, however many postings feed it, and only within 14 days of the posted dates — older hiring is context, not news.

## Step 6 — Digest

Close each run with a single summary: X postings pulled → Y patterns
classified → Z alerts → skipped with reasons. Zero postings across ALL
watched accounts on three consecutive runs is a sourcing failure until
verified — never report it as market silence.

## What good looks like

A great run reads like a radar sweep: dead postings die at the threshold,
agency listings are resolved or dropped, and each real pattern lands once,
with dated links and a one-liner on why it matters. The digest reconciles, and a quiet run says "quiet, verified" rather than nothing.

Mediocre looks like: five alerts for one spree, congratulating a staffing
agency, evergreen reposts counted as ramps, a mention hit alerted as a watched account's own hiring, or — worst — a silent zero nobody checked.

## Tighten over time

After 3–6 weeks, read the ledger and digests: signals per week, share acted on within the 14-day window, share on unowned net-new accounts. Prune pattern classes and queries nobody acts on, suggest widening the setup phrases/sources. If alerts outrun rep capacity and net-new share is high, extend step 5 with a draft-for-review branch — the radar still never sends.

## Rules

- MUST pull LinkedIn postings only through native integration; every other board through one vetted, test-run apify scraper.
- NEVER draft, queue, or send outreach — this play detects, classifies, and
  alerts, and stops there.
