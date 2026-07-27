---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Trigger setup

This skill is designed to fire on **account signal events** — website visits, registrations, trial starts, usage milestones, meeting completions, outreach replies, LinkedIn engagement — and to be callable on demand ("score this account"). Reference trigger instructions:

```
An account signal fired: [event type] for [company / domain].

Load and follow the <Account tier scoring> skill in full.

Context for this run:
- Triggering event: [type + payload summary]
- Named individual (if any): [name, title]
```

- [ ] Wire your signal sources (web analytics/identification, product events, CRM activity, LinkedIn engagement feed) to invoke the skill with the event context.
- [ ] Pass the **event type** through — several rules branch on it (the partner-check exception, the self-artifact guard, agency flagging all key off signup/trial events).
- [ ] Account memory must persist between runs — the methodology scores the **running signal stack**, not single events. Without durable memory, stacking rules and repeat-view escalation cannot work.

## 2. Placeholders

- [ ] `{{CRM}}`, `{{ALERTS_CHANNEL}}`, `{{ACTIVE_DEALS_CHANNEL}}`, `{{SALES_OWNER}}`, `{{PARTNERSHIPS_OWNER}}`, `{{SOCIAL_SELLER}}`, `{{SELF_SERVE_THRESHOLD}}`, `{{ENTERPRISE_THRESHOLD}}`, `{{BUYER_PERSONA_LIST}}`, `{{DISQUALIFIED_MARKETS}}` — all filled (or the optional ones deliberately deleted).
- [ ] Map the lifecycle references to **your** funnel stage names: closed won, trial, closed lost, self-serve, unqualified, potential partner. The skill references stage *semantics*, not stage names.
- [ ] Create the tags in your workspace: the four tier tags, the three ACV tags, `self-serve`, `expansion target`, and confirm your vendor/partner labels match what Step 0a checks.
- [ ] Create the lead-score field in {{CRM}} that Step 4 syncs to, with the four tier values.
- [ ] Tier names: Bronze/Silver/Gold/Diamond is the default ladder — rename freely, but keep four levels or re-map every rule that names a tier.
- [ ] If you have no LinkedIn signal feed, delete the {{SOCIAL_SELLER}} signal rows and the LinkedIn routing caps — do not leave them referencing a feed that doesn't exist.

## 3. Policy decisions

- [ ] **Start in EVAL mode.** Run 1–2 weeks with CRM writes disabled and review the would-have-written tags in the alert posts before going live.
- [ ] **All numeric thresholds are tuned defaults, not laws**: the self-serve floor (<50 employees AND ≤$10M funding), the enterprise gate (1,000+), the <3-sellers cap and its overrides (>$5M revenue founder signup; >$10M funding), the fresh-trial window (14 days), the inactivity window (30 days), the funding bands in the ACV assessment. Recalibrate each to your price point and sales-touch economics — then leave them stable so tiers stay comparable over time.
- [ ] The **Silver→Gold tiebreaker** (default to visibility on genuinely mixed signals) — confirm {{SALES_OWNER}} actually wants the extra review volume; flip the default if your alert channel is drowning.
- [ ] The **prior-relationship Gold floor** — decide what counts as a "genuine prior evaluation" in your CRM (deal object, logged meeting, trial record) and confirm the verification signals exist in your data.
- [ ] The **ACV assessment dimensions** are written for a GTM/sales product ("dedicated sellers", "RevOps hires"). Substitute the team and ops function *your* product serves in dimensions 2, 3, and 6.
- [ ] Alert format: Gold/Diamond posts use your team's **standard lead-scoring alert format** — point Step 7 at that spec; never let this skill invent a second layout for the same channel.

## 4. Behavioral invariants (do not remove)

- The self-serve gate runs **before everything** and is a hard stop — no signal strength overrides headcount.
- Near the self-serve threshold, headcount is **verified against LinkedIn**, taking the lower of the two counts — enrichment ranges are never trusted alone in the risk band.
- Exactly **one tier tag and one ACV tag** per account — old tags removed on every write.
- Every tag write is **verified by re-reading the record**, retried once, and reported honestly — an alert never claims a write that didn't land (`TIER_TAG_STATUS`).
- **Bronze and Silver never alert.** Zero-signal accounts never alert.
- Anonymous signals never score Gold; post-engagement-only never scores Gold; a lone profile view caps at Silver.
- A weak new signal **never demotes** an existing tier — demotion only via explicit gates or deliberate review.
- The **self-artifact guard**: objects created by the current run never count as evidence a rep is already engaged.
- Auto-created onboarding objects never count as product depth.
- All outreach produced by this skill is **queued for human approval — never auto-sent**, at any tier.
- Memory snapshots **prepend, never overwrite** — the running signal stack is the scoring substrate.
