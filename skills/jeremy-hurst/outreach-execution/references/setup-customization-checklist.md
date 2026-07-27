---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Senders and channels

- [ ] Fill `{{SENDER_ROSTER}}` — every person who can send, with which channels each has connected (email, LinkedIn). A sender without a healthy LinkedIn connection cannot carry LinkedIn steps; the skill stops rather than improvises.
- [ ] Assign `{{AWARENESS_SENDER}}` — a senior exec (founder/CxO) with an active LinkedIn presence. Their Stage 1 job is blank connection requests + one casual DM to decision makers: no pitch, no product mention. If no exec posts content regularly, skip Stage 1 rather than faking it.
- [ ] Assign `{{HIGH_TIER_SENDER}}` and `{{LOW_TIER_SENDER}}` per your `{{TIER_MODEL}}`. The point of the split is protecting the senior sender's reply rates and calendar — keep the boundary strict in both directions.
- [ ] Connect `{{VOICE_SOURCE}}` — per-sender voice guides and/or a library of past approved messages. If you have neither yet, run the first few sequences fully manually and save the approved versions; the skill drafts from approved copy, never from generic templates.

## 2. Placeholders

- [ ] `{{CRM}}`, `{{SENDER_ROSTER}}`, `{{AWARENESS_SENDER}}`, `{{HIGH_TIER_SENDER}}`, `{{LOW_TIER_SENDER}}`, `{{TIER_MODEL}}`, `{{APPROVAL_OWNER}}`, `{{MULTITHREAD_THRESHOLD}}`, `{{LARGE_COMPANY_THRESHOLD}}`, `{{VOICE_SOURCE}}`, `{{RESOURCE_LIBRARY}}`, `{{AUTO_APPROVE_CARVEOUT}}` — all filled.
- [ ] Map `{{TIER_MODEL}}` to your actual tiering scheme. The skill references tier *semantics* (high vs low), not names — any two-band split works.
- [ ] Build `{{RESOURCE_LIBRARY}}` as one page or doc: booking links, demo video, trust/security docs, DPA, one-pagers. It is the single source of truth — the skill never hardcodes a URL, so a moved link only needs fixing in one place.

## 3. Policy decisions

- [ ] **Default `{{AUTO_APPROVE_CARVEOUT}}` to none.** Everything queues for {{APPROVAL_OWNER}}. Only after weeks of clean approvals should you consider the narrow carveout in Step 4 (signed-up user, lifecycle trigger, ≤4 steps, not a senior exec at a large company) — and even then, all four conditions, no partial credit.
- [ ] **The executive hard rule is not configurable downward.** Sequences to C-level/VP/Head-of/Director contacts at companies above `{{LARGE_COMPANY_THRESHOLD}}` always require human approval, no matter what trigger fired. You may tighten the threshold, never loosen it.
- [ ] Set `{{MULTITHREAD_THRESHOLD}}` (default >200 employees). Below it, single-thread; above it, an exec multi-thread from `{{AWARENESS_SENDER}}` spawns automatically with every primary sequence — and always queues for approval.
- [ ] Decide whether low-tier accounts may auto-send at all. If your brand risk tolerance is low, queue everything — the skill works identically, just with more human clicks.
- [ ] Confirm the LinkedIn-active rule (10,000+ followers or visibly active → LinkedIn-only by default) matches your motion.

## 4. Behavioral invariants (do not remove)

- No hook, no send — generic "stay top of mind" requests get pushed back, not drafted.
- Never mention the signal directly — signals inform the angle, they are never quoted at the prospect.
- Scenario always wins over channel.
- Prior-relationship check before every pre-conversion play — replied outreach, past meetings, and closed-lost deals make it warm; unanswered sequences and anonymous visits do not.
- LinkedIn connection requests are always blank.
- Duplicate check before every new sequence — edit or archive, never stack.
- Written outreach rationale on every staged sequence — the approver should never have to reconstruct the "why."
- Plain-text URLs only in outreach copy — outreach channels don't render markdown.
- No attachments, ever — links from `{{RESOURCE_LIBRARY}}` instead.
- Approved messages get saved back to `{{VOICE_SOURCE}}`; unapproved drafts never do.
