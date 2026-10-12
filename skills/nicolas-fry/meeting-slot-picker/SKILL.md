---
name: meeting-slot-picker
title: Meeting slot picker
description: |
  Use this skill when the user hands over someone else's booking link or scheduling link and
  wants the meeting placed well, not just placed. Reads the user's calendar for the window,
  classifies the meeting as revenue-facing or internal, and picks the slot that serves it:
  revenue conversations land where the prospect, customer, partner or investor has runway
  (first slot after their lunch, first hour of their day), internal and low-stakes meetings
  get clustered against existing commitments so the longest free block survives. Produces a
  booked slot with a one-line reason, the day's resulting meeting count, and a drafted
  confirmation message held for approval. Triggers: "book time with her", "grab time on my
  calendar", "here's his booking link", "what time should I take this call", "find a slot
  that works for both sides", "book Monday afternoon with the prospect", or a pasted booking
  page URL with no other instruction. Different from setting up your own booking links or
  triaging inbound demo requests: this is the user booking onto a counterparty's page.
category: Sales
tags: [Sales]
---

Applies when the user books onto a counterparty's booking page. Produces one well-placed booking and a confirmation draft held for approval.

When a meeting sits changes what comes out of it and what the rest of the day is worth. Two objectives:

- **Revenue-facing** (prospect, customer, partner, investor): optimize for the counterparty's state of mind. Put them where they have room to keep talking.
- **Everything else** (internal, vendor, admin, networking): optimize for the user's focus, protecting contiguous work time.

When a rule does not fit, reason from the objective.

## 1. Gather and classify

Get the link, who the meeting is with, and the topic. If the link arrived in a thread, read it for the topic, day constraints and tone. A window the user names ("Monday", "before Thursday") is the search space; these heuristics only pick within it.

State the classification in one line before slot hunting ("Treating this as revenue-facing: she leads a channel partner"), so a misread is cheap to correct. When ambiguous, read the ambiguous case in `references/worked-examples.md` before asking.

## 2. Pin both timezones

The most damaging error in this play. Take the user's timezone from their calendar settings, the counterparty's from their city, signature or company location. A booking page's timezone selector reflects the viewer's browser, not the host, unless the page explicitly labels it as the host's. If the counterparty's timezone cannot be determined with confidence, ask.

## 3. Read the calendar, then the page

Read the user's calendar for the whole candidate window, not just the obvious day: the booking page only knows the host is free. Count two things separately:

- **Meeting load**: real meetings with other people. Reminders and self-created task blocks are not meetings.
- **Time occupancy**: everything, solo blocks included. A 30-minute self-block fragments a morning as much as a meeting.

Then extract the page's slots per candidate day as structured data (day, start, displayed timezone). Read `references/booking-page-patterns.md` first: stale reads, scrolling slot lists and routing forms cause most bad bookings.

## 4. Score and pick

Score every candidate with `references/slot-scoring-rubric.md`. Revenue mode scores in the counterparty's clock: the 45 minutes after their lunch and their first hour rank best; the hour before lunch and their last 90 minutes rank weak, because they have a wall in front of them. Focus mode scores in the user's clock: pick the slot that leaves the longest unbroken free block standing. Explain the pick with a reason ("1:15 PM, first slot after her lunch"), not a bare score.

If the pick makes a third meeting that day, say so in one line and name a lighter nearby day, then proceed: a revenue meeting is what a busy day is for.

## 5. Ask only at a real fork

Ask when the top two score close on different days, when it is a weak slot this week against a strong one next week, when classification or timezone is unresolved, or when a non-revenue meeting would crowd a day. Offer two or three options with the tradeoff named. Recurring forks are in `references/edge-case-playbook.md`.

## 6. Book, confirm, report

Book the slot and verify the page shows an explicit confirmation state. Draft a two-to-three sentence confirmation for the originating thread (day, date, time, timezone, the thread's tone, no scheduling rationale) and wait for a yes. Report the booked time, a one-line reason, and the day's meeting count.

## What good looks like

- The confirmed time is right in both timezones, and the summary states both.
- A revenue call sits in the counterparty's post-lunch or first-hour window, with no hard stop on the user's side within 30 minutes after it.
- An internal sync sits against an existing meeting or the edge of the day, and the user's longest free block is the same length, or close, after booking.
- The expert's tell: separating reminders from real meetings. Counting "REMINDER: send proposal" as a meeting makes a light day look full and pushes a prospect out a week.
- The mediocre version: the first open slot, revenue windows applied to an internal sync, or a 4:45 PM call because a timezone was assumed.

## Rules

- MUST read the user's calendar before booking. If no calendar is readable, ask the user to paste the day's commitments. NEVER book blind.
- MUST respect any day or window the user states, over every heuristic.
- MUST stop and ask when a routing or qualification form asks something not already known. NEVER guess an answer.
- MUST enter only the user's name and email, on the page the user supplied. NEVER add guests, change duration, or fill optional fields the user did not mention.
- MUST show the drafted confirmation and wait for an explicit yes before sending. Approval of one message is not approval of the next.
- NEVER place a revenue meeting outside the user's own working hours, even when it scores well in the counterparty's clock.
