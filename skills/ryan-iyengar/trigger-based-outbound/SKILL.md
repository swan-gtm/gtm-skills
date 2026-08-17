---
name: trigger-based-outbound
title: Trigger-based outbound
description: |
  Use this skill to qualify one already-detected account event for an outreach decision; use abm-signal-watchlist to operate persistent monitoring across a fixed account list. Produces a ranked send, nurture, or skip decision, a verified contact target, a trigger-grounded opener, and an outcome record that improves future signal selection.
category: Signals
tags: [Sales, Demand Gen]
---

Use this when a fresh account change may create a credible reason to start or resume a conversation. Produce a ranked decision and a reviewable message task; do not treat a detected event as automatic permission to send.

## Qualify the trigger

1. Capture the event, source, observed date, account, and exact evidence. Prefer primary evidence over summaries.
2. Verify freshness against the date the event occurred, not the date an aggregator surfaced it.
3. Translate the event into a plausible operational implication. A job posting matters only when the role, seniority, volume, or language connects to the problem being solved.
4. Compare the account with the ICP and exclusion rules. Record why the signal changes priority now.
5. Check recent activity, open opportunities, suppression rules, customer status, and previous replies before deciding to engage.

Score the event using [references/signal-rubric.md](references/signal-rubric.md). A high event score cannot rescue poor fit or missing contact access.

## Resolve the person

Start with the account, then identify the person whose responsibility is closest to the observed change. Confirm that the contact belongs to the account and that the role evidence is current. Prefer an existing relationship or known stakeholder over a newly found senior title.

If the signal exists only at domain level and no appropriate person is verified, return “acquire or research contact” rather than drafting a send. If several stakeholders are relevant, name a primary contact and a distinct reason for involving each additional contact. Do not send the same message to an entire buying group.

## Decide send, nurture, or skip

- **Send:** strong fit, material and fresh trigger, verified person, no suppression, and a specific implication.
- **Nurture:** credible fit but the trigger is weak, early, ambiguous, or lacks a reachable stakeholder.
- **Skip:** poor fit, stale or generic evidence, active conflict, recent negative reply, customer-sensitive context, or no defensible connection.

Record the decision and the strongest counterargument. This exposes weak enthusiasm disguised as scoring.

## Draft the opener

Write one opener around the observed change, its likely implication, and a low-friction question. State only what the evidence supports. The trigger should explain why this account and why now; it should not be used as surveillance theater.

Keep the first message focused on one hypothesis. Do not lead with congratulations unless the event is genuinely celebratory. Do not pretend to know internal priorities. Read [references/worked-signals.md](references/worked-signals.md) for send, nurture, and skip examples.

Before creating a send task, show the account, contact, evidence, recent-touch check, message, and channel to a human reviewer. Sending remains a separate approved action.

## Learn from outcomes

Record delivered, replied, positive reply, meeting, disqualified, and negative feedback against the account, contact, trigger type, and message hypothesis. Evaluate trigger types over a meaningful sample; do not rewrite weights after one win.

Review both precision and coverage. A signal program that never makes mistakes because it selects almost nothing is not necessarily useful. Preserve negative outcomes so future ranking does not repeat avoidable touches.

## What good looks like

- The exact evidence, event date, and source are inspectable.
- The contact’s responsibility makes the hypothesis credible.
- The opener would still make sense if the recipient knew exactly how the event was found.
- “Skip” and “nurture” remain common, legitimate outputs.
- Recent conversations and customer context suppress inappropriate outreach.
- Outcome history changes priorities only after enough observations to distinguish a pattern from noise.

The mediocre version alerts on every funding story or job post, targets the most senior available title, produces generic congratulations, and measures messages sent rather than useful conversations.

## Rules

- MUST verify the event date, account identity, contact identity, and recent-touch history.
- MUST keep drafting and sending as separate actions with human approval before send.
- NEVER fabricate an implication, quote, relationship, or internal initiative.
- NEVER contact a domain-only target without resolving an appropriate person.
- NEVER evade suppression, consent, or channel-policy requirements.
