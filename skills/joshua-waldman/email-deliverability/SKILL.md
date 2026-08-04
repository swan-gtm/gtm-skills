---
name: email-deliverability
title: Email deliverability audit and rescue
description: |
  Use this skill when emails hit spam, open rates drop, a domain or IP gets
  blocklisted, or a sender wants a deliverability audit before scaling volume.
  Triggers: "why are we going to spam", "audit my email setup", "open rates
  dropped", "we got blocklisted", "warm up this domain", "check my
  deliverability". Produces a severity-ranked audit or a root-cause diagnosis
  with a recovery plan and the thresholds to monitor.
category: Newsletters
tags: [Marketing, RevOps]
---

Run this when email performance breaks, or before it gets the chance to. It produces either a severity-ranked audit of the sending setup or a root-cause diagnosis with a dated recovery plan.

## The play

1. Pick the mode. Proactive review → audit the setup top to bottom. Active fire ("we're in spam") → diagnose.
2. Scope first. Pull send volume, open rates by mailbox provider, shared vs dedicated IPs, and what changed right before the drop. An open rate below 10% at any provider confirms a deliverability problem, whatever anyone thinks of open tracking accuracy.
3. Walk the four pillars, in order:
   - Infrastructure. SPF, DKIM, DMARC present and verified recently — whole zone files disappear during migrations. The server's HELO announcement must match the IP's reverse DNS; a mismatch is an automatic blocklisting.
   - Data. Hard bounces above 0.5% mean stop and clean. Soft bounces above 2% mean investigate before removing anything: Microsoft graylists legitimate senders heavily and ProofPoint soft-bounces on send rate, so both inflate the number with no list-quality problem behind it. Retry soft bounces three times across 72 hours, then treat what still fails as hard. After an ESP migration, check whether old bounces were accidentally re-imported.
   - Content. Ask: how is this email distinguishable from a scam? Missing branding, HTML-only sends, bloated code, and mismatched sender identity all read as scam patterns to filters.
   - Traffic shape. The big one — solving it at the pipe solves most of the problem. Throttle per provider, never raise volume more than 50% week over week, and spread large sends across 3-4 days.
4. Classify and prescribe. Blocklisted → delist, but fix the root cause first or the listing comes back. Content filtered → pause that provider for 24-48 hours, fix, retest on an engaged segment. Broken authentication → fix DNS, wait for propagation before resuming. New or damaged sender → run the ramp in references/warmup-playbook.md.
5. Define monitoring. Set thresholds that trigger a pause, not a postmortem: bounce spikes, complaint rate above 0.3%, one provider dropping while the others hold.

When the work goes deep, read references/warmup-playbook.md (week-by-week recovery ramp with per-provider volumes), references/shared-pool-management.md (pool contamination, compliance rails, high-risk verticals), and references/provider-specific-tactics.md (Gmail, Microsoft, Yahoo, iCloud, ProofPoint).

## What good looks like

- The best operators diagnose by provider, not in aggregate. A Gmail-only drop and an everywhere drop are different diseases with different cures.
- The mediocre version blames "spam trigger words" and rewrites subject lines. Content is the least common root cause; infrastructure, data quality, and traffic shape break far more often.
- A real diagnosis names the broken pillar and the change that broke it, with a date. "Improve engagement" is not a diagnosis.
- Honesty beats comfort. A sender at 2-4% opens needs to hear that recovery takes weeks and may cost 10-20% of the list. Fully inboxing typically returns 10x the engagement, so frame the pause as an investment.
- The output is good when the plan has dates, per-provider daily ceilings, and explicit stop conditions.

## Rules

- MUST report audit findings by severity: critical (causing spam placement or blocks right now), warning (fix this week), improvement (fix when able).
- MUST check open rates by mailbox provider before proposing any fix.
- MUST fix the root cause before resuming volume on any IP, new or old — a fresh IP with the same practices just burns the fresh IP.
- NEVER exceed 4x the previous day's opens at a provider whose opens you can trust — Gmail, Microsoft, Yahoo. Apple Mail Privacy Protection pre-fetches images and inflates iCloud opens, so ramp Apple on a fixed schedule and read delivery and bounce signals there instead.
- NEVER recommend purchased lists or mailing contacts who never opted in.
- NEVER let a damaged sender blast a full list in one day — spread it or stop it.
