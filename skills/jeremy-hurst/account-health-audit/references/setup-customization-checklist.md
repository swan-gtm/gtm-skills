---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Data access

The audit is only as good as Step 1. Before the first run, confirm the
agent can actually pull each source:

- [ ] `{{USAGE_DATA_SOURCE}}` — workflows/automations with execution counts
      and enabled state, connected senders and integrations, registered
      users with last-login dates, and feature-level usage/spend for the
      past `{{LOOKBACK_DAYS}}` days. If you can't get execution counts,
      Section 1's dead-workflow check degrades to guesswork — fix access
      first.
- [ ] `{{CRM}}` — company activity feed: notes, calls, emails, deal stage
      history.
- [ ] `{{CALL_LIBRARY}}` — transcript search by account domain. Optional
      but strongly recommended; it anchors "what are they solving for."
- [ ] Account notes/memory — wherever your team records goals and context.

## 2. Placeholders

- [ ] `{{USAGE_DATA_SOURCE}}`, `{{CRM}}`, `{{CALL_LIBRARY}}`,
      `{{TIER_LABELS}}`, `{{ALERT_DESTINATIONS}}`, `{{SCORING_WORKFLOW}}`,
      `{{VOICE_GOVERNANCE}}`, `{{STALE_DAYS}}`, `{{LOOKBACK_DAYS}}` — all
      filled.
- [ ] Map `{{TIER_LABELS}}` to your actual tier names. The 3-tier minimum
      in Section 2 is the judgment rule; the labels are cosmetic.
- [ ] Set `{{STALE_DAYS}}` to match your product's activity rhythm. Default
      5 assumes daily-cadence workflows; weekly-cadence products should use
      10–14 or every audit will cry wolf.
- [ ] Point `{{SCORING_WORKFLOW}}` and `{{VOICE_GOVERNANCE}}` at the
      *account's* central workflows, not your org's — the audit inspects
      the customer's configuration.

## 3. Policy decisions

- [ ] **Character caps** (750 / 1,000 / 500 per section) — these are the
      skill's core discipline, forcing signal over narrative. Adjust only
      if your team consistently needs more; never remove them.
- [ ] **The 30-account cross-reference before flagging spend waste** —
      decide your sample size (30+ is the tested floor). Flagging waste
      from raw spend percentages is the most common false alarm this rule
      exists to prevent.
- [ ] **Interventions in Section 6** — review the failure-to-intervention
      map and swap in your own playbook actions (e.g., your onboarding
      session format, your champion check-in motion) while keeping the
      one-intervention-per-flag rule.
- [ ] Decide who receives the report and where it lands (doc, channel,
      CRM note). The skill produces the report; routing is yours.

## 4. Behavioral invariants (do not remove)

- All Step 1 data gathered **before** any section is written — sections
  produced from partial data are worthless.
- No "likely," "probably," or "seems" anywhere in the output.
- Tier persistence checked by **comparing two counts** (tagged vs.
  sequenced), never by eyeballing tags alone — partial persistence is the
  failure mode this catches.
- Spend flagged as waste only after the per-account cross-reference, or
  when no qualification gate exists at all.
- Messaging judged from workflow instructions read word-for-word — never
  from titles, descriptions, or usage counts.
- Section 3 stops at notification coverage; sequence/outreach state
  belongs to Section 4. Scope bleed is how audits balloon.
- Zero saved message examples for a connected sender is a hard flag.
- Every flagged finding in Section 6 pairs with exactly one concrete
  intervention.
