---
name: campaign-launch-preflight
title: Campaign launch preflight
description: |
  Use this skill when an outbound campaign is about to be scored, approved, pushed to a sending platform, or started, and someone needs to know it will send what everyone thinks it will send. Runs a gated preflight across six stages (scoring context, sendable pool, approval count, sending infrastructure, rendered copy, post-launch verification), returns a go or hold verdict per gate with the evidence each one rests on, and then runs a daily sending health check for as long as the campaign sends. Reach for it when someone says "launch the campaign", "are we ready to send", "pre-launch checklist", "why did the campaign send to nobody", "why did only half the leads load", "qualification rate looks wrong", "check before we push", or "is deliverability OK to start".
category: Outreach
tags: [Sales, Demand Gen, RevOps]
---

Applies the moment a campaign moves from building to sending: before scoring, before approval, before the push, before the start button, and every sending day after. Produces a gate-by-gate verdict (go, hold, or not checked) with the evidence behind each line, and a launch record that names which system each fact was read from.

Most failed launches do not fail at the copy. They fail in the plumbing between systems: a list scored against the wrong buyer, a "ready" campaign holding zero approved leads, a push that loaded 60 of 78, a mailbox nobody reconnected. Each of these looks like success on the dashboard that caused it. This preflight's core rule: **a launch fact counts only when it was read from the system that will act on it, with its denominator.**

## The six gates

Run them in order. A later gate cannot rescue an earlier one; a campaign scored against the wrong buyer stays wrong however clean its copy is.

1. **Scoring context.** Before any lead is scored, the campaign carries its own written buyer definition: who it targets, which signals count, what disqualifies. A blank campaign context does not fail loudly; scoring falls back to the account-level ICP, and a campaign aimed at security buyers gets graded against an operations ICP. Write industry as a weighting, never a gate, and rank a verified technology or platform footprint above industry. Settle every context before the first scoring run, because scoring runs cost money and a re-score usually does not re-qualify on its own. The context template and the failure it prevents are in `references/gate-checklist.md`.
2. **Sendable pool.** Count only leads with a verified work email (or a verified channel handle for a social-first sequence), a first name, and a company. Personal mailboxes, unverified and catch-all addresses stay out. If the sequence is email-first, confirm the leads actually hold email before quoting a number.
3. **Approval count.** Count leads in the approved state, per campaign, before quoting any push number. "Contactable", "ready to launch" and "enriched" are not approved, and a push sends only approved leads. Confirm the campaign is in the state the push requires, and never start an empty campaign.
4. **Sending infrastructure.** Per mailbox: authentication records published and passing on sent mail, daily cap at or below the mailbox provider's ceiling, warm-up running, schedule set to the recipient's business hours and time zone, open and click tracking off. A status badge is a symptom; open the panel and name the failing line. The full infrastructure gate is in `references/deliverability-gate.md`.
5. **Rendered copy.** Read every step of the sequence, rendered, for up to three leads per campaign: subject, body, every merge field resolved, the right sender name and no other sender's name, an opt-out line on every email step, and real content in steps that might be empty shells. If two systems hold the sequence, make them agree on step count and sender before any push, because a push writes one over the other.
6. **Post-launch verification.** After the push, the lead count on the sending platform must equal the approved count you pushed. A shortfall is a failure to investigate before reporting the launch. Read launch state on the sending platform, never in the system that requested it, and record which source you read.

Then hand the campaign to the daily sending health check in `references/daily-health-check.md`, which runs every sending day and for two sending days after the campaign stops.

## What good looks like

- **What the best operator notices first:** the denominator. "240 contactable" and "0 approved" can describe the same campaign on the same afternoon. The expert asks "of how many, in which system, read when?" before believing any launch number.
- **The common mistake:** checking step 1 and assuming the rest. Unresolved placeholders, a previous rep's signature and empty template shells live in steps 2 through 6, where a first-step check never looks. A close second: trusting a "running" status, which a partial push also shows.
- **The quiet failure:** qualification rates that look merely low. A campaign qualifying 2% of a hand-built list is usually not a bad list; it is a list scored against the wrong buyer. Read the scoring context before blaming the data. Worked cases, including that one, are in `references/worked-examples.md`.
- **How you know the output is good:** every gate line names its evidence and its source system; every count carries its denominator; the push count reconciles exactly; and anyone reading the launch record could tell what was checked and what was not.

## Rules

- MUST read every count from the system that acts on it, with its denominator, and record the source.
- MUST hold the launch on any failed gate; report "not checked" as distinct from "passed".
- MUST get explicit human approval before scoring a batch, pushing leads, starting or resuming a campaign, or raising a send limit. This skill prepares and verifies those actions; a person takes them.
- NEVER re-score a list to fix a qualification problem without first fixing the context that caused it.
- NEVER raise a mailbox above its provider's daily ceiling, and never start a campaign whose sending platform holds zero leads.
- NEVER pause or resume a campaign without recording who did it and why.
