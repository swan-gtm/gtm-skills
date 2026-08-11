---
name: leaked-demand-recovery
title: Leaked demand recovery
description: |
  Use this skill when demand may have leaked between systems: a chat or form lead who never
  completed a booking, a demo request with no meeting, a call held with no follow-up sent, an
  inbound reply never answered, a trial that ended quietly, a deal closed lost on a blocker that
  has since changed. Produces a list of confirmed drops with the evidence attached and one drafted
  recovery message each, queued for a human to send. Fires on "did they ever book", "who fell
  through the cracks", "what did we drop", "who never got a follow-up", "unworked inbound", "leads
  that went nowhere", "recover lost inbound", and before any re-engagement send.
category: RevOps
tags: [Sales, RevOps]
---

The cheapest pipeline in any organisation is demand already paid for and then lost in the gap
between two systems. This finds it, proves the drop is real before anyone touches it, and drafts
the recovery.

## The play

1. **Scope the sweep.** Choose the seams to work and the window: about a month for active leaks,
   six to twelve months for closed-lost revival. Confirm the window if one was specified.

2. **Build the candidate list from the capture systems, not the CRM.** The CRM holds what someone
   remembered to log. The mailbox, the calendar, the call recorder and the lead-capture channel
   hold what actually happened. Take the union, deduplicate by person and by company, and include
   people with no CRM record at all: they are the largest silent category and the entire reason to
   build the list this way. `references/leak-map.md` lists the seams worth working and what each is
   verified against.

3. **Verify every candidate against two independent systems. This is a hard gate.** The record
   saying someone was dropped is frequently wrong, and the cost is asymmetric: a missed recovery
   forfeits one opportunity, while messaging someone who already booked or already replied costs the
   relationship. Read `references/verification-gate.md` before running this step. Candidates that
   fail the gate leave the list with a one-line note. Never soften a failed gate into a light touch
   anyway.

4. **Establish history before choosing a voice.** A recovered hand-raiser is usually not new. No
   history: fresh first touch. Prior conversation: re-engagement voice that references the context
   honestly. Existing or churned customer: route to the account owner and stop drafting. Open deal
   owned by a colleague: flag the owner and stop, because a parallel message collides with a live
   motion. Closed lost: carry the stated reason into the framing, and proceed only if the blocker
   has genuinely changed.

5. **Apply hard disqualifiers before scoring fit.** Geography, regulatory coverage, segment.
   Serviceability is binary and cheap; fit scoring is expensive and pointless on an account that
   cannot be served. Verify thin enrichment rather than trusting it, since poor records under-report
   company size. Keep the disqualifier list in one place, or a stale gate rejects markets since
   opened and admits ones since dropped.

6. **Draft one message per confirmed drop**, personalised on what they asked about or the exact point
   the last conversation reached. The recovery framing does the work; generic re-engagement copy
   wastes the advantage of knowing precisely where they fell. Where the drop was an internal failure,
   acknowledge it in a clause and move on. One unambiguous next step.

7. **Present for approval.** Per confirmed drop: person and company, leak type, evidence checked,
   history, suggested action. Then the drafts. Keep failed-gate candidates visible at one line each
   so the verification work is auditable and a bad call can be spotted. On a scheduled sweep that
   finds nothing, end silently.

## What good looks like

- The tell: the best operator distrusts the field claiming nothing happened more than the one
  claiming something did. Absence of evidence is nearly always a query problem, not a cold prospect.
  An empty result is a hypothesis about the search, not a finding about the person.
- The mediocre version filters the CRM for "no activity in 30 days" and mails the list. It produces
  volume, a few confused replies from people already mid-conversation, and a reputation cost nobody
  measures because no system reports it.
- The output is good when it leads with what was confirmed dropped rather than how many records were
  scanned, and every claim carries its evidence. "Not booked" is not a finding. "No forward-dated
  event under their name or domain, no meeting on the contact record, still in initial status" is.

## Rules

- **MUST** confirm every drop against two independent systems before it advances.
- **MUST** resolve the contact record and search by address and domain before concluding no activity.
- **MUST** let the system closest to the event win when systems disagree: the calendar beats the CRM
  on bookings, the mailbox beats the CRM on last contact, the recorder beats the calendar on
  attendance.
- **NEVER** treat one system's field as proof of contact or of non-contact.
- **NEVER** treat a chat transcript, a bot's promise, or an auto-applied status as evidence that a
  booking exists or a call was held.
- **NEVER** send or post anything automatically. This verifies and drafts; a human decides.
- **NEVER** message into an account a colleague is working without flagging it first.
- **NEVER** re-engage a prior contact in fresh-inbound voice. It reads as institutional amnesia and
  is worse than sending nothing.
- **NEVER** recover a lead outside serviceable coverage. Flag it and stop.
