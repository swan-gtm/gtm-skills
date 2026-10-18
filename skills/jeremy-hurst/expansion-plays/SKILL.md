---
name: expansion-plays
title: Expansion plays
description: |
  Use this skill when writing outreach to grow an existing paying customer: a plan upgrade, a new use case or a deeper rollout. It picks one of five plays from the signal behind the conversation (repeated top-ups, the customer asking for more, a history of upgrades, a usage ceiling plus an in-product signal, or a good relationship with low value realized), and writes a short sequence hooked on what the customer is doing in the product or said on a call, never a cold pitch. Every sequence waits for approval and ends with an internal alert to the account owner, not a sixth pitch. Also answers "upsell email", "write expansion outreach", "how do I pitch an upgrade to a customer".
category: Deals
tags: [Sales]
---

Applies when a customer is already paying and there is a reason to talk about growing the account. Produces one sequence per contact, built on their own usage or their own words.

They already know you. The fastest way to stall an expansion is to pitch a customer as if they were a prospect. Every play here starts from evidence they will recognize: their usage, their top-ups, something they said on a call.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference.

- `{{PRODUCT}}`: Your product name
- `{{CALL_NOTES}}`: Where call notes and transcripts live (e.g. Gong, Circleback, Fathom)
- `{{USAGE_SOURCE}}`: Where product usage lives (e.g. your product database, a usage dashboard)
- `{{USAGE_UNIT}}`: What customers consume (e.g. credits, seats, API calls)
- `{{ACCOUNT_OWNER}}`: The person who owns the customer relationship and approves every send
- `{{OWNER_ALERT_CHANNEL}}`: Where the internal no-reply alert goes (e.g. a Slack DM to `{{ACCOUNT_OWNER}}`)
- `{{NO_REPLY_DAYS}}`: Days after the last customer touch before the internal alert (default: 10)

## When to use, and when not

**Use** for a paying customer and a conversation about a plan upgrade, a new use case or a deeper integration.

**Do not use** for:
- Accounts still in a trial. Converting a trial is a different conversation.
- Closed-lost or churned accounts coming back. That is a win-back, not an expansion.

## Shared rules

1. **Paying customers only.**
2. **The hook is their usage or their words.** Read `{{CALL_NOTES}}` and `{{USAGE_SOURCE}}` before writing anything. Write each message fresh from that evidence; never paste a previous customer's email.
3. **No cold pitch.** Do not re-explain what `{{PRODUCT}}` does. They know.
4. **One sequence per contact.** To reach someone else at the account, start a separate sequence for a different stakeholder.
5. **The last customer-facing message is never "just checking in."** It carries a specific reason or a specific ask.
6. **The last step is internal.** If there is no reply `{{NO_REPLY_DAYS}}` days after the last customer touch, alert `{{ACCOUNT_OWNER}}` in `{{OWNER_ALERT_CHANNEL}}`. That alert is not a customer-facing step, and it is never another pitch.
7. **Nothing sends on its own.** Every message is queued for `{{ACCOUNT_OWNER}}` to approve, and nothing reaches a customer executive without the owner's sign-off.

## The five plays

Pick the play from the signal behind the conversation.

### 1. Recurring top-ups in quick succession
- **Signal:** they have bought extra `{{USAGE_UNIT}}` several times in a short window.
- **Angle:** their usage is the proof. Show the math: the next plan up costs less than they are paying in top-ups.
- **Sequence:** email, LinkedIn message, reply on the email thread, then the internal alert.

### 2. The customer asked for more
- **Signal:** they asked for more `{{USAGE_UNIT}}`, more seats, or about upgrading.
- **Angle:** they asked, so deliver a path. Do not prospect: answer the request with the options and a recommendation.
- **Sequence:** email, reply on the thread, LinkedIn message, then the internal alert.

### 3. Several upgrades plus heavy top-ups
- **Signal:** they have moved up plans before and are still topping up aggressively.
- **Angle:** a stronger commercial conversation than a single upgrade (for example, the plan that fits where they are heading, or a longer commitment).
- **Sequence:** email, LinkedIn connection request, LinkedIn message, email, then the internal alert.

### 4. Usage ceiling plus a signal from inside the product
- **Signal:** they are near their plan's ceiling, and something in a recent session shows where they want to go next (a new use case, a new team using it, a feature they tried).
- **Angle:** hook the session, not the meter. "Your team started using X last week" lands; a lecture about their usage numbers does not.
- **Sequence:** the same five steps as play 3.

### 5. Good relationship, low value realized
- **Signal:** the relationship is warm, but they are getting little out of `{{PRODUCT}}`.
- **Confirm first.** Before writing anything, check: are they actually getting little value, or are they just quiet? Look at usage trends and the last calls. Do not start a sequence until this check passes; pitching an upgrade to a quiet, happy customer reads as tone-deaf.
- **Angle:** value before upgrade. The champion and the executive get different proof (for example, what their team could do next for the champion, the business outcome for the executive).
- **Sequence:** a longer six steps, ending with the internal alert.

## What good looks like

- The first line of every message is something the customer did or said, recognizable to them.
- Plays 1 to 3 show numbers the customer can check: their top-ups, their plan, the cheaper path.
- Play 5 never starts without the confirmation check, and the champion and executive get different proof.
- No message explains the product from scratch, and none ends with "just checking in."
- Every sequence ends with the internal alert, and nothing went out without the owner's approval.
