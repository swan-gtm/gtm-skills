---
name: google-ads-write-safety
title: Write safety for AI agents on Google Ads accounts
description: |
  Use this skill when an AI agent or automation is about to make a write change to a
  live Google Ads account — pausing something, moving a bid, adding negatives, editing
  a budget, launching a campaign. Produces a change that's previewed, confirmed, and
  provably executed, instead of a plausible-sounding claim. Triggers: agent making
  Google Ads changes, autonomous bidding, automated negative keywords, AI campaign
  management, bulk account edits, "did that actually run."
category: Ads
tags: [RevOps]
---

# Write Safety for AI Agents on Google Ads Accounts

Applies the moment an agent moves from reading an account to writing to it. The
account is real money and the advertiser's livelihood — a hallucinated success
message isn't a rough edge, it's a trust catastrophe the first time it happens.

## The play

1. Classify the request by blast radius before touching anything: read-only,
   low-risk (a single keyword, negative, or bid move within a tight band), or
   account-level (budget swings, conversion tracking, campaign creation or deletion).
2. Default to propose-only — pull data, calculate, recommend, but execute nothing
   without an explicit go-ahead. An authorization covers the specific action just
   approved, never the rest of the session.
3. Keep the low-risk band actually low-risk: bid moves within roughly ±20%, negatives
   only against clear waste (spend with zero conversions), no whole-campaign pauses,
   no budget swings past ~20%, and never touch conversion actions or billing without
   a separate, explicit approval.
4. Before executing, show a preview — current value, proposed value, and what
   triggered it (the search term, the CPA, the pacing). New campaigns and new ads
   get created paused, full stop, so a human reviews before spend starts.
5. Require an explicit confirmation tied to that specific preview. "Go ahead," "do
   it," "approved" counts; a related-but-different message, or silence, does not.
   Batch operations still get one itemized preview — never a blanket yes for a list
   the human hasn't actually read.
6. Execute, then produce a receipt: the operation, the exact resource changed, the
   before/after state, and how to reverse it. If nothing else survives, the receipt
   should.
7. If the write failed, partially applied, or the tool was never called, say so in
   plain language immediately. Never generate a receipt for something that didn't
   happen, and never imply full success when only part of a batch went through.

## What good looks like

- The best operators catch the gap between "the tool ran" and "the tool returned no
  resource name" — a receipt without a real, traceable ID is worthless and should
  never ship. Every resource name or ID in an output must trace back to an actual
  tool result, never to what a successful version of that action usually looks like.
- The common failure mode is an agent narrating success from pattern-matching, not
  verification — writing "paused 14 keywords" because that's what the confirmation
  step is supposed to produce, not because it checked the response. Catch this before
  it ships, not after the advertiser notices their account didn't change.
- Good output names the account explicitly when more than one is in play, states its
  confidence on anything inferred, and gives the human enough in the receipt to undo
  the change without opening a support ticket.

## Rules

- MUST get an explicit confirmation, tied to the specific preview shown, before any
  write beyond pure read/propose mode.
- MUST create new campaigns and ads in a paused state.
- MUST tie every resource ID or name in output to an actual tool result.
- NEVER report a write as done, or partially summarize a batch as fully done, if the
  underlying call failed or wasn't made.
- NEVER let one authorized action expand into standing authorization for the rest of
  the session.
