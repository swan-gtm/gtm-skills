---
name: call-followup-sweep
title: Call follow-up sweep
description: |
  Use this skill when a day or a week of customer calls has piled up and the
  follow-through is owed but unwritten. Trigger on "review my calls this week",
  "draft my follow-ups", "what do I owe people", "what did I promise on these
  calls", "catch me up on yesterday's calls", "did anything fall through this
  week". Asks which window to sweep, reads every call in it, extracts the
  commitments — especially the ones you made — and returns one drafted email per
  account that earns one, the list of calls that earn none and why, and the
  promises still open from earlier sweeps. Produces drafts only; it never sends.
category: Deals
tags: [Sales, Customer Success]
contributors: []
---

Applies when a batch of customer calls has happened and the follow-through is
owed. Produces a per-account draft for the calls that earn one, a no-email list
with reasons for the calls that don't, and an aging report of commitments still
open from prior sweeps. Nothing is ever sent.

## The sweep

1. **Ask the window before anything else.** Day or week — never guess, and never
   default to "all recent calls". The window changes the output: a day sweep is
   mostly fresh drafts while the call is still warm; a week sweep is mostly an
   aging and pattern report with fewer, denser drafts. If the answer is "week",
   confirm whether it means the trailing five business days or the calendar week
   — on a Wednesday those differ by half a book.
2. **Pull every call in the window** from wherever calls are recorded —
   transcripts, recordings, or the user's own notes. Capture account, attendees,
   date, and duration for each. A scheduled call with no recording is a finding,
   not a gap: list it as unverified rather than dropping it silently.
3. **Extract commitments, not summary.** Read
   `references/commitment-extraction.md` before the first call. Four things get
   pulled from every transcript — what you committed to, what they committed to,
   the question you didn't answer, and any date that was named out loud. The
   first category is the one that loses deals and the one reps skip.
4. **Triage which calls earn an email.** Read `references/triage-rubric.md`.
   Most calls in a given week do not. The value of a sweep is subtraction — a
   run that drafts an email for every call has done nothing a calendar couldn't.
5. **Dedupe by account, not by call.** Three calls with one account in one week
   is one email to that account, built from all three. Separate drafts to the
   same company arriving the same morning read as an unmanaged vendor.
6. **Draft to the call's shape.** Read `references/draft-patterns.md` — the
   email a stalled renewal needs is not the email a first discovery needs. Cap
   every draft at 150 words and three visible action items; overflow goes to a
   named next call, not a longer email.
7. **Report the sweep, don't just dump drafts.** Lead with commitments aged past
   three business days, then the drafts, then the no-email list with a one-line
   reason each, then any pattern that showed up across calls — the same
   objection landing three times in a week is worth more than any single draft.

## What good looks like

- The best operator extracts their own promises first. Reps instinctively
  mirror the customer's pain back at them, because that is what the transcript
  is loudest about — but the thing that actually rots a deal is the seller's
  unshipped "I'll get you the security doc by Thursday". A sweep that surfaces
  customer pain and misses two of the user's own open promises has failed at
  its only irreplaceable job.
- The common mistake is the recap email. Both people were on the call; a
  narration of it is filler that buys nothing. The follow-up exists to date the
  commitments, put in writing the one thing that would otherwise be disputed
  later, and hand the champion something forwardable to people who weren't
  there. If a draft would still make sense with the account name swapped out,
  it is a template, not a follow-up.
- Good output is auditable and mostly negative space: every action item carries
  a named owner and a date, the no-email list is typically longer than the draft
  list, aging commitments appear above fresh drafts, and the user can see at a
  glance which calls were read and which could not be.

## Rules

- MUST ask whether the window is a day or a week before reading anything.
- MUST produce drafts only. NEVER send, schedule, or queue a message, and never
  write to the CRM as part of a sweep — the user reviews and sends by hand.
- MUST attach a named owner and an explicit date to every action item, or state
  plainly that the call never produced one.
- MUST list calls that were skipped or unreadable, with the reason, rather than
  returning a clean report over partial coverage.
- NEVER invent a commitment, a date, or a number that was not said on the call;
  quote or flag the absence.
- NEVER write in a register the user has not used — a draft that has to be
  rewritten for voice is worse than no draft.
