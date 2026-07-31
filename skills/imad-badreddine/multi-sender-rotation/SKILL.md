---
name: multi-sender-rotation
title: Multi-sender rotation
description: |
  Use this skill when one LinkedIn campaign needs more volume than a single account
  can safely send: scaling outreach across several sender accounts, sizing a sender
  pool, splitting a lead list between profiles, or reacting when one account in the
  pool gets a warning. Produces a rotation plan with per-account caps and an
  incident playbook.
category: Outreach
tags: [Sales]
---

Run this when campaign volume exceeds what one account can safely send. It produces a sender-pool plan: how many accounts, how leads are split, per-account caps, and what happens when an account degrades.

## The play

1. Size the pool from the target, not the other way around: divide required daily connection requests by 20, the safe steady-state ceiling per warmed account. A 100-invite-per-day campaign is a 5-account pool.
2. Only rotate warmed accounts. A new profile joins the pool after a full warm-up ramp, never on day one. Keep one warmed spare per five active senders: the bench rule. When an account degrades, the bench replaces it the same day.
3. Split the lead list by account, never round-robin per message. Each prospect belongs to exactly one sender for the entire relationship: the one-voice rule. Dedupe by person and by company before launch so two senders never hit the same account.
4. Stagger sending windows so the pool does not fire in one burst: each account keeps its own working hours, matched to its own timezone and history.
5. Keep per-account caps individual. An account fresh off warm-up sends less than a veteran; never apply the pool average to every profile.
6. On any warning: pull that account from rotation immediately, pause it 48-72 hours, and let the bench absorb its remaining volume. Never redistribute a paused account's leads mid-conversation; conversations wait for their owner.
7. Review the pool weekly: acceptance rate and reply rate per account. One account trending down while others hold is an account problem; all accounts trending down together is a targeting or copy problem.

## What good looks like

- Experienced operators read per-account acceptance rates as an early-warning system; the mediocre version only watches campaign totals and misses the one account quietly dying inside a healthy average.
- The common mistake is treating the pool as one big account: shared caps, shared list, leads bouncing between senders. Prospects notice a second stranger continuing a first stranger's conversation, and so does the platform.
- Done well, losing any single account costs at most one-fifth of daily volume for two days, no prospect ever hears from two different senders, and the campaign total stays flat while individual accounts rest and rotate.

## Rules

- MUST warm up every account fully before it enters rotation.
- MUST keep each prospect with one sender for the whole relationship.
- MUST pull a warned account out of rotation the same day and rest it 48-72 hours.
- NEVER round-robin messages to one prospect across accounts.
- NEVER let two senders contact the same company without a deliberate multi-threading plan.
