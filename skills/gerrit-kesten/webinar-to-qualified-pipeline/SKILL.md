---
name: webinar-to-qualified-pipeline
title: Webinar to qualified pipeline
description: |
  Use this skill after a B2B webinar has registrations or engagement data but before treating
  every registrant as a sales lead. Produces reconciled lifecycle states, fit and intent scores,
  a prioritised sales-review queue, segment-specific follow-up, and a measurable handoff from
  webinar registration to qualified pipeline and booked meetings.
category: Events
tags: [Sales, Demand Gen, RevOps]
---

Use this when a webinar has produced names but the revenue team cannot tell who deserves sales attention, useful follow-up, or no action. It turns verified engagement and fit into a controlled pipeline process.

## Define the commercial job

Write one sentence that names the audience, the problem taught, and the next buying step. A webinar for awareness, customer education, partner enablement, and opportunity acceleration cannot share one qualification rule.

Define the conversion ladder:

1. registration;
2. attended live, watched replay, or no-show;
3. meaningful engagement;
4. sales review accepted;
5. meeting booked;
6. qualified opportunity created.

Keep every rung separate. Registration is a content conversion, not pipeline. Attendance still does not prove fit, authority, a current problem, or willingness to buy.

## Reconcile identities and states

Create one record per person and preserve source, campaign, event, answers, permission, company, role, and existing relationship. Resolve duplicates conservatively. Uncertain identity matches go to review instead of merging.

Assign one current state using `references/lifecycle-states-and-suppression.md`. A later, harder state overrules an earlier one. A confirmed meeting ends booking nurture. Customers and open opportunities route to their existing owner.

## Score fit and intent separately

Do not let watch time rescue a poor-fit account. Score three dimensions:

- **Fit, 0–40:** account, persona, market, and use-case match.
- **Engagement, 0–30:** attendance depth, replay, questions, polls, and calls to action.
- **Buying intent, 0–30:** stated problem, decision-stage question, high-intent page visit, reply, or meeting request.

Use `references/qualification-scorecard.md` for the rubric and these starting bands:

- **0–24:** record only or low-frequency nurture;
- **25–49:** relevant nurture, no sales task;
- **50–69:** human sales review;
- **70–100:** priority sales review and handoff.

A score of 70 qualifies for handoff only when Fit is at least 20 and Buying Intent at least 10. Booked meetings move to sales. Suppression and existing relationships override scoring.

## Use questions as buying evidence

Separate educational questions from workflow and decision questions. Decision questions reveal commercial, rollout, integration, compliance, approval, timing, or capacity constraints.

Preserve the buyer's wording. “Can we plan monthly target hours and see utilisation?” carries more context than “interested in workforce planning.” Aggregate repeated questions to find messaging and demo gaps without treating every questioner as sales-ready.

## Route the next action

Build the next step from state, score, and relationship. Priority records receive a context-rich handoff. Review-band records require human verification. Relevant but unqualified attendees receive topic-specific value. No-shows receive a replay or summary without manufactured urgency. Existing relationships route to their owner; suppressed contacts receive no nurture.

Use `references/follow-up-and-handoff-matrix.md` for timing and approval. Individual sales messages, bulk sends, sequence enrolment, and ambiguous merges require explicit human approval.

## Measure the complete funnel

Report each rung by source, audience, and event topic:

```text
registrations → live/replay engagement → sales reviews accepted
→ meetings booked → qualified opportunities → sourced or influenced revenue
```

Do not report registration as a lead, a sales task as pipeline, or a processed conversion event as revenue. Track source, duplicates, suppression, owner acceptance, rejection reasons, and whether meetings exited lower-level nurture. Compare cohorts only when definitions match.

See `references/worked-webinar-case.md` for an anonymised operating pattern built from real B2B webinar question types.

## What good looks like

- The operator notices the gap between attendance and buying intent before celebrating registration volume.
- Sales receives a short queue with account fit, exact engagement, buyer wording, source, existing relationship, and recommended next step.
- No-show, attendee, replay viewer, customer, open opportunity, and booked meeting never receive the same treatment.
- Every qualified handoff can be traced back to source evidence and every rejected handoff has a reason.
- The weak version sends the same “thanks for attending, book a demo” email to everyone. The strong version protects trust, routes real intent quickly, and leaves low-signal contacts out of sales sequences.
- Funnel reporting distinguishes sourced pipeline from influenced pipeline and preserves the difference between meeting and opportunity.

## Rules

- MUST keep registration, engagement, meeting, opportunity, and revenue as separate funnel events.
- MUST score account fit independently from engagement and buying intent.
- MUST preserve buyer wording, source, permission, and existing relationship in every handoff.
- MUST stop booking nurture after a confirmed meeting and reroute customers or active opportunities to their owner.
- NEVER infer marketing permission, buying intent, or qualification from attendance alone.
- NEVER auto-send individual sales outreach, run bulk follow-up, merge uncertain identities, or enrol sequences without explicit human approval.
- NEVER invent attendance, watch time, questions, attribution, or revenue when the event platform does not provide it.
