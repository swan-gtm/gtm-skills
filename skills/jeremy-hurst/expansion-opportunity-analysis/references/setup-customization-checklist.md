---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Data sources

- [ ] `{{CRM}}` — confirm closed-won deals carry a close date and amount, and
      that upsells appear as additional deals (or map to however your CRM
      records plan changes).
- [ ] `{{BILLING_SOURCE}}` — the skill must be able to read the **live** plan
      definition (base fee, included allocation, per-unit rate) and the raw
      charge history. If your plan metadata lives inside the billing object
      (e.g. price metadata), point the skill there explicitly — never at a
      static mapping table.
- [ ] `{{USAGE_SOURCE}}` — monthly consumption by account, active users with
      roles, and which capabilities are configured. If overage purchases are
      merged into a single balance field, note where the *plan* allocation
      lives so 2.2 doesn't double-count.
- [ ] `{{USAGE_UNIT}}` — one word, used consistently in every table.

## 2. Tunable defaults

All thresholds ship as defaults — tune them to your pricing, then leave them
alone so analyses stay comparable across accounts.

- [ ] `{{CONSERVATIVE_FACTOR}}` (0.90) and `{{GROWTH_FACTOR}}` (1.50) —
      multipliers on the trailing 3-month average for the two proposals.
      Widen the gap if your customers' usage is spiky; narrow it if steady.
- [ ] `{{COMMIT_DISCOUNT}}` (10%) — the per-unit discount the growth option
      earns. Must match what you can actually honor.
- [ ] `{{OVERAGE_MULTIPLIER}}` (2.0×) — your on-demand rate vs. committed
      rate. This ratio is the engine of most volume plays; if yours is lower,
      the "repeated overage" pattern fires less often and that's correct.
- [ ] `{{HIGH_UTILIZATION_THRESHOLD}}` (90%) — what counts as "at the
      ceiling."
- [ ] `{{INACTIVITY_WINDOW}}` (30 days) — the churn-risk gate. Shorten for
      daily-use products, lengthen for monthly-cadence ones.
- [ ] Rounding boundary for proposal volumes — "nearest natural tier" should
      map to your plan tiers (nearest 1,000 units, nearest seat band, etc.).

## 3. Policy decisions

- [ ] `{{EXPANSION_OWNER}}` — one named person. They approve every play,
      receive every no-reply escalation, and can override proposal volumes
      by fiat.
- [ ] **Never auto-send** — the strongest invariant. The skill drafts copy
      and queues sequences; a human sends everything. If you want pure
      analysis with no drafts, delete section 3.4 and stop at the timing
      call.
- [ ] Decide your commitment-averse framing: if you sell "bulk purchase /
      draw-down" instead of "annual contract," keep the language rule in 2.6;
      otherwise delete it and say "annual" plainly.
- [ ] Relationship-led plays require confirming the champion + stakeholder
      list with {{EXPANSION_OWNER}} **before** any sequence exists — keep
      this gate; multi-threading the wrong exec burns real relationships.
- [ ] Map the role-to-gap guidance in 3.2 to your product: write down, for
      each buyer role you sell to, the one adoption gap that most concerns
      them. The skill fills in specifics per account, but the role framing
      is yours.

## 4. Behavioral invariants (do not remove)

- Base fee and consumption fee reported **separately** — the whole invoice is
  never "platform fee."
- Included allocation always read from the plan definition, never from a
  balance field.
- Proposals sized from the three most recently **completed** months — the
  current partial month never enters the average.
- The inactivity gate ends the analysis at Part 1 — no expansion play on a
  silent account.
- Every analysis lands on a matched pattern or an explicit new-pattern
  proposal — never a shrug, never a forced match.
- No placeholder numbers in copy intended to send.
- One active expansion play per account at a time — tag on launch, clear on
  reply or close.
- No-reply escalations go to {{EXPANSION_OWNER}} internally — never another
  touch to the customer.
