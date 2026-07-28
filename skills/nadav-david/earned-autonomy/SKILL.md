---
name: earned-autonomy
title: Earned autonomy
description: |
  Use this skill when deciding how much a GTM agent may do without a human looking, when a
  workflow is ready to run on a schedule, when outreach should stop requiring per-item approval,
  and when something has gone wrong and autonomy needs pulling back. Produces a level per task
  with the evidence required to move up and the triggers that drop it automatically. Trigger
  phrasings: "can I let the agent send", "when do I stop reviewing every draft", "how much should
  I automate", "the agent made a mistake, now what", "is this workflow ready to run unattended".
category: RevOps
---

Produces a level per task, the evidence needed to raise it, and the triggers that lower it without asking.

## The one-line law

Autonomy is granted per task, not per agent, and only against logged evidence. New tasks start at full review.

One agent can be trusted to qualify accounts unattended while its enrichment is still spot-checked. Granting autonomy to an agent rather than a task is how a good record on the easy work buys freedom on the risky work.

## The four levels

| Level | What ships | What reaches the human |
|---|---|---|
| **L0 Draft** | nothing with wording in it | every worded item, before it goes |
| **L1 Spot-check** | items that passed the quality gate | a random sample, plus every low-confidence item |
| **L2 Exception-only** | items that passed the gate | flagged, edge and high-risk items only |
| **L3 Auto** | runs on schedule, ships on gate pass | a periodic digest, plus any guardrail trip |

The distinction that keeps L0 honest is copy risk versus click risk. Wordless actions carrying no claim, a connection request with no note, a profile visit, can move at L0 inside their rate limits, because nothing in them can misstate, leak, or embarrass. Anything with words waits.

## Promotion needs evidence, not confidence

Set your own numbers; these are the defaults worth starting from. Full criteria in `references/promotion-evidence.md`.

- **L0 to L1:** at least 30 items reviewed, human edit or reject rate under 10%.
- **L1 to L2:** at least 50 items at L1, sampled gate-pass rate at or above 95%, no guardrail breach in the window.
- **L2 to L3:** the task's outcome metric holds at or above target for four consecutive weeks, zero breaches.

Two rules matter more than the thresholds.

**Judgment steps are trusted separately, and a credibility-costing miss resets the count to zero.** Clearing "picked a good angle" does not clear "picked the right person." Within each, a weak-but-harmless output costs nothing, while a miss that advertises you did no homework sends the count back to zero. The gate guards against embarrassing misses, not stylistic ones.

**No refusal in the window means hold the promotion.** The evidence has to include at least one logged case where the agent declined or flagged something inside its own authority because it looked wrong. An agent that has never refused anything has demonstrated obedience, not judgment, and autonomy is a grant of judgment. This is a hold rather than a demotion, and a manufactured refusal ticked to clear the gate is itself a breach.

## Demotion is automatic

No approval needed to pull back. Any one of these drops the task:

- gate pass rate falls below 90% over the trailing 20 items,
- the outcome metric misses target two weeks running,
- any guardrail breach, which drops the task straight to L0 with a notification.

## Guardrails no level crosses

These bind an L3 task exactly as hard as an L0 one. Autonomy buys you out of review, never out of the rubric.

- **Volume limits.** Every channel's caps hold regardless of level.
- **Suppression.** Never contact anyone on the no-contact list, however good the lead looks.
- **Claims.** No unverified or stale claim ships. Anything needing legal or compliance sign-off routes to a human first.
- **Quality rules.** The automatic-fail rules of your review rubric apply at every level.
- **A kill switch.** Any task, or everything, freezes to L0 instantly.
- **The live-reply floor.** Responding to a live inbound conversation never runs above L0, whatever the task has earned. No agent free-types a reply to a real person unattended. On a reply, the sequence stops and routes to a human.

## What good looks like

Two failure modes, opposite directions, equally common.

The cautious one leaves everything at L0 forever because no promotion gate was written down, so autonomy becomes a mood rather than a decision and the system never gets faster however well it performs.

The reckless one promotes on a good feeling after a strong week, outcome metric unmeasured, and finds out at scale. Promoting on volume alone is the specific trap: a task can hit its item count while producing a disproportionate share of risky output, which is why risk is logged per item and read at promotion rather than averaged away.

It is working when you can name every task's current level, point at the evidence behind it, and show a demotion that fired without anyone deciding to allow it. If nothing has ever been demoted automatically, the triggers are decoration.

## Rules

- MUST record the level per task, with the evidence, where the next reviewer will read it.
- MUST start new tasks at L0 and let evidence move them, never a launch decision.
- MUST demote on trigger without waiting for approval.
- NEVER promote a task on volume alone, or on a window containing no logged refusal.
- NEVER let an earned level cross a guardrail, and never let a live conversation run unattended.
