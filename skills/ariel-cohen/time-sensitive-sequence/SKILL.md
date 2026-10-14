---
name: time-sensitive-sequence
title: Time-sensitive sequence
description: |
  Use this skill when outreach is only worth sending until a moment passes and must stop by itself, with nobody remembering to stop it: pre-event meeting outreach, a dinner that needs same-day attendees after cancellations, a webinar invite, a closing offer. Produces one group of sequences per event, copy that stays true until the cutoff, and a scheduled kill job that stops everything left in the group at the cutoff. Also answers "self-killing sequence", "sequence that expires", "stop outreach after the event date", "last-minute dinner invites", "pre-event outreach".
category: Outreach
tags: [Sales, Marketing]
---

Applies when a message becomes wrong or useless after a specific moment. Produces sequences plus a scheduled kill that ends them at that moment.

A sequence has no end date. Steps run on waits, and a LinkedIn message can sit for days waiting for a connection to be accepted. Left alone, a pre-event sequence sends "let's meet next week" during event week, and a dinner invite lands after the dinner. The cure has two halves: plan the cadence backwards from the cutoff, and schedule a kill that catches whatever is still alive at the cutoff.

## The play

1. **Set the cutoff.** The cutoff is the earlier of two moments: when the copy stops being true, and the last moment an invite is still useful for this kind of event. Read `references/cutoff-rules.md` for the rules by copy phrase and event type. State the cutoff as a date, time and timezone.
2. **Check what the platform can do.** Confirm the six capabilities and look up the seven numbers in `references/platform-assumptions.md`. If a capability is missing, use its fallback there, not a guess.
3. **Check feasibility.** Work out when the first message can go out and when the last step can run inside the sending window. Divide contacts by daily limits per inbox and add what already waits in the queue. If the list cannot clear before the cutoff, cut the list or add an inbox. Do not build sequences that mostly die in the queue.
4. **Choose channels.** Use both LinkedIn and email when there is time, because they reach different people. Drop LinkedIn when the cutoff is too close for a connection to be accepted and a message to follow. Drop email for people who only respond on LinkedIn. Decide per event and per list, and say why.
5. **Plan the cadence backwards.** Place the last step at least one sending window before the cutoff, with short waits of one to two days. Write copy that is true right up to the cutoff: real dates and times, never "next week" or "this Thursday" unless the cutoff rules say it is safe. Read `references/copy-examples.md` for real event copy and which phrases in it go stale.
6. **Make one group per event.** Three dinners means three groups, three cutoffs, three kill jobs. Never mix cutoffs in one group, because the kill stops the whole group. Put the cutoff in the group's description.
7. **Build the sequences** in the group, in the event's timezone. Leave them for approval unless the owner explicitly said to send automatically.
8. **Arm the kill job before you call it done.** Read `references/kill-job.md` for the schedule and the hand-off instructions. If you cannot arm it, say so first and do not approve or send.
9. **Report** the group, number of sequences, last planned send, cutoff in the owner's timezone and in UTC, and what the kill will and will not touch.

## What good looks like

- **The best operators write the cutoff down before the copy.** They pick the kill time first, then write backwards. The mediocre version writes a good sequence and adds a stop date as an afterthought, so the copy still says "next week".
- **The kill is a sweep, not a list.** It finds whatever is alive in the group at the cutoff, including contacts added after the job was created and people stuck waiting for a connection. A kill built from a fixed list of ids misses them.
- **Judgment at the real moment beats the rule.** Cutoffs for a dinner or a webinar are starting points. On the day, if the dinner moves or fills, the owner moves the cutoff or stops the group now.
- **Replies are left alone.** Someone who answered is in a live conversation. The kill never touches them, and the report lists them first, because they need a human reply.
- **You can tell it worked** by re-listing the group after the cutoff: nothing is running, nothing sent after the cutoff, every replier was told to the owner.

## Rules

- MUST set the cutoff before writing copy, and MUST state it with date, time and timezone.
- MUST use one group and one kill job per cutoff.
- MUST arm the kill job before approving or sending anything.
- MUST leave contacts who replied untouched and report them to the owner.
- MUST check the cutoff against the copy: any relative time phrase ("next week", "tomorrow", "tonight") needs a cutoff that keeps it true.
- NEVER build when the cutoff has passed or is too close to clear the queue. Suggest a direct message instead.
- NEVER let the kill job create, send or edit outreach. It only stops, re-checks and reports.
- NEVER hard-code a list of sequences into the kill job. It sweeps the group at run time.
