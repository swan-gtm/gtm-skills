---
name: inbox-warm-up-ramp
title: Warm up a sending inbox before you need it
description: |
  Use this skill when a new mailbox, domain or seat is about to start cold outreach, or when
  replies and deliverability drop after volume was raised. Produces a per-inbox daily send
  ceiling that rises on a schedule, the rules that keep it rising, and the honest way to tell a
  user why today's limit is low.
category: Outreach
tags: [Sales, RevOps]
---

A new mailbox at full volume is a spam complaint with a countdown. This sets
the ceiling, per inbox, and the conditions to raise it.

## The play

1. **Ramp by the age of the inbox, not the age of the campaign.** Week one at
   a handful of sends a day; roughly double each week; reach full volume at
   about four weeks. Every seat runs its own clock — a new person joining a
   mature team starts at week one.
2. **Get volume from more inboxes, never from one working harder.** Two or
   three mailboxes on a domain, more domains when you need more volume. A
   single inbox pushed past its ceiling is the failure everyone repeats.
3. **Send inside the recipient's working hours, on working days.** Mail
   arriving at 3am local time reads as automation to a person and to a filter.
4. **Keep the first touch plain.** No links, no images, no tracking pixel, no
   attachment. Add them once a thread has a human in it.
5. **Watch the three numbers that end a ramp**: hard bounces (stop and clean
   the list well before 3%), spam complaints (any is a lot), and the share of
   sends that reach zero engagement over a week. A ramp is paused by evidence,
   not by feel.
6. **Never warm up on the account you cannot lose.** If cold volume must grow,
   put it on a separate sending domain and keep the primary one for real
   conversation.
7. **Tell the user why the cap is low, in their words.** A silent limit reads
   as a broken tool, and the person will raise it blindly to make the silence
   stop. Say the number, say the schedule, and if you offer a skip, spell out
   what it risks before they choose it.

## What good looks like

- The tell: reputation is per *sending identity*, and it is earned by
  behaviour that looks like a person's — modest volume, replies coming back,
  activity inside a working day. Volume without replies is the pattern
  filters are built to catch, which is why the ramp exists at all and why a
  sequence that gets answers can climb faster than one that does not.
- The mediocre version warms up by mailing seed accounts in a warming network
  and calls the inbox ready on day three. The metric moves; the reputation
  does not. Nothing detectable happens until real volume starts landing in
  spam, and by then the domain is spent.
- You know the output is good when raising the cap changes nothing except the
  count — same bounce rate, same complaint rate, same reply rate. If replies
  fall as volume rises, the ceiling was already correct.

## Rules

- **MUST** hold a per-inbox daily cap that increases with that inbox's own
  sending age.
- **MUST** pause the ramp on rising bounces or any complaint, and clean the
  list before resuming.
- **MUST** show the current cap and its reason wherever the user sees the
  send happening.
- **NEVER** run cold volume from the domain your business depends on.
- **NEVER** raise a cap silently, and never raise it without stating what a
  cold inbox at full volume risks.
- **NEVER** treat a warming-network score as evidence that a real list can be
  mailed.
