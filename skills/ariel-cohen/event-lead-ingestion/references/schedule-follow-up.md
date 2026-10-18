# Schedule follow-up

Branch of event lead ingestion. Set a personal reminder and a task when the lead asked you to wait. Do not sequence during the wait.

Use it when they asked you to wait, or the next play is "remind me to book or ping them on DATE".

Do not stage a sequence that would reach them during the wait. Do not send anything now unless the requester separately asked for a same-day note.

## When this is the right branch

Typical cases: "follow up in 2 to 2.5 weeks, I'm on vacation and then at another vendor's event"; "remind me next week, after this conference ends, to book her demo".

A wait they named is a promise. Breaking it with a "quick hello" sequence is worse than silence.

## What to create

1. **A task** in `{{TASK_TOOL}}` for the person who met them (the requester). The title names the person, the company and the action (book the demo, ping on LinkedIn). The body has the LinkedIn URL, the wait reason, the score, champion vs buyer, and the landmines. Do not notify them now unless they asked to be pinged immediately.
2. **A reminder:** a one-time scheduled run in `{{REMINDER_TOOL}}`, personal to the requester. Call it a reminder in anything you say to them. Convert their local time into whatever time zone the scheduler uses (default 10:00 AM ET if they did not name a time).

The reminder's instructions must tell the future run to:

- Ping the requester privately through `{{PRIVATE_NOTIFY}}` (not a public channel)
- Include the LinkedIn URL, the company, and the conversation facts from account memory
- Draft the follow-up in the requester's voice (do not send)
- Put the draft in that private thread
- Not start a new sequence unless the requester asks for one in that later thread
- Not cold-frame or trial-frame the account

## Date math

Use the wait they named, not a rounder number you prefer. "2.5 weeks" from September 30 is mid-October, not "sometime next month". If they said "next week, after we finish this event", pick the first weekday after the event ends.

If the wait is "after DATE" because they are at another event, do not fire during that event.

## What not to do

- Do not enroll them in a post-conference sequence "just in case".
- Do not also email them today.
- Do not assign the reminder to the account owner when someone else had the conversation. The account owner belongs in the later demo, not the wait.
- Do not create a team-wide reminder for a personal follow-up; keep it on the requester.

## What good looks like

The reminder fires on the date they asked for, with enough context that the requester can send without re-briefing anyone. The lead is not touched in the meantime.

Failure modes: sequencing during the wait; rounding 2.5 weeks into "next month"; posting the reminder to a public channel; handing the account owner a wait that belongs to the person who had the conversation.
