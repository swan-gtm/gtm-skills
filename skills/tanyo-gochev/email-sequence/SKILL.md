---
name: email-sequence
title: Email sequence
description: |
  Use this skill when designing or fixing an automated multi-email flow for people who already know
  you — welcome and onboarding series, lead nurture, trial conversion, re-engagement, post-purchase,
  or any behaviour-triggered drip. Produces the sequence spec: entry trigger, touch count, timing,
  per-email job, exit conditions, and what to measure. Trigger phrasings: "email sequence", "drip
  campaign", "nurture flow", "welcome series", "onboarding emails", "re-engagement emails",
  "lifecycle emails", "what emails should we send", "our nurture isn't converting".
category: RevOps
---

Applies to automated flows for known contacts, not cold outreach. Produces a buildable spec, not just copy.

## Trigger on behaviour, not on a clock

A fixed drip sends the same day-three email to someone who logged in twice yesterday and someone who has never logged in at all. Both get the wrong message, and the engaged one gets taught to ignore you.

Start from **the core action and its natural frequency**: the single behaviour that delivers value, and how often a satisfied person would do it. A "we miss you" email on day three to a monthly-frequency product is noise. Every trigger, delay, and exit condition keys off that frequency.

## One email, one job

Each email does exactly one thing and asks for exactly one thing. The instinct to bundle — a tip, a case study, a webinar, and an upgrade nudge in one send — is what makes sequences feel like newsletters and perform like them.

Write the *job* of each touch before writing a word of copy. If two adjacent emails have the same job, one of them shouldn't exist.

## Sequence shapes

| Sequence | Length | Entry | The one thing it must do |
|---|---|---|---|
| Welcome | 3–7 over ~2 weeks | Signup | Get them to first real value, fast |
| Onboarding | 5–7 | Account created | Complete the setup steps that predict retention |
| Lead nurture | 6–8 over 2–3 weeks | Asset downloaded | Earn the right to make an offer |
| Trial conversion | 4–6 | Trial start | Reach the aha moment before the trial ends |
| Re-engagement | 3–5 | Inactive at their natural frequency | Restart the habit, or learn why it stopped |
| Post-purchase | 3–5 | Purchase | Make the decision feel correct, then expand |

Lengths are starting points. Sales cycle, product complexity, and relationship stage move them.

## Exits, and the one that shouldn't exist

Every sequence needs explicit exit conditions — took the action, replied, converted, or unsubscribed. Without them people sit in two flows at once and receive contradictory messages in the same hour.

But **inactivity is not an exit.** The "last email — we'll stop messaging you" send at the end of a re-engagement flow is a self-inflicted wound: it announces the demotion and converts a dormant contact into a lost one. End the sequence by dropping the cadence instead — to monthly, then quarterly, indefinitely. The list never shrinks, only the frequency does. The only true exits are an explicit request to stop, or a hard unsubscribe.

## What good looks like

The tell of a good operator: they can state the entry trigger, the exit condition, and the single job of every email before any copy exists — and they check what data actually exists before designing a flow that depends on it. Most broken lifecycle programs are broken at the data layer, not the copy layer; the event the sequence keys off simply isn't being tracked.

The mediocre version is a time-based drip with escalating urgency and no behavioural gate — technically live, quietly training a whole list to ignore the sender.

Good output is buildable by someone who wasn't in the conversation: trigger, delay, audience condition, and exit stated for every touch, plus the measurement plan. If it can't be built without asking follow-up questions, it isn't finished.

## Rules

- MUST define the entry trigger and every exit condition before writing copy.
- MUST verify that the events and attributes the flow depends on are actually populated.
- MUST give every email one job and one ask.
- NEVER end a sequence with a message announcing that you'll stop contacting them.
- NEVER run two sequences that can send to the same person on the same day.
