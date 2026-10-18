# Draft outreach

Branch of event lead ingestion. Stage a follow-up sequence from the teammate who met the person. Do not use it when they asked us to wait, or when they said memory only.

## Who sends

The person who had the conversation owns the 1:1. That overrides any default in `{{SCORING_PROCESS}}` that assigns top-tier accounts to a fixed rep's sequence, for **this contact**. The account owner still takes the meeting if it books. Do not put the account owner on a parallel cadence to the same person.

Whoever had the conversation sends, whatever their role.

Never auto-send. Build the sequence in `{{SEQUENCE_TOOL}}` staged for approval, always.

## Which outreach path

Read `{{OUTREACH_PLAYBOOK}}` before writing copy, including its writing-style rules.

Route by how you met them:

- **Booth or walking-floor 1:1 with notes** → your post-conference path, Warm unless a meeting is actually on the calendar (then Hot, with a 2-step confirmation only)
- **Dinner or same room, no booth** → your in-person event follow-up path
- **The requester already specified sender, channel and ask** (e.g. "draft from me, pleasure meeting you, ask for a proper meeting") → honor that. Still run the playbook's gates and pre-flight checks.

If a connection request from the sender is already pending, do not stage a second one, and do not add LinkedIn DMs that cannot land until they accept: email only is correct until then. If they are not connected and may not accept, put the first substantive touch on email when a verified work email exists.

## Shape

Anchor on the conversation. Their words are the hook. Never mention badge scans, lists, or that you "pulled attendees".

- No booked date → this is Warm, not Hot.
- They asked a question or sketched a model → continue that thread in the first message; do not open with a cold qualifier.
- Champion path → this person is not the closer. The cadence can book a demo with them; the reply to the requester then says who else belongs on the call.
- Persona-match the pitch using the playbook. Marketing leaders do not get a sales-team zoom-out.
- Pull demo and booking URLs from `{{LINKS_AND_RESOURCES}}`. Never hardcode them. Never wrap URLs in markdown.
- Use the booking link your routing rules assign for this sender and account (some teams split calendars by company size, or route the meeting to the account owner). Follow those rules unless the requester said otherwise.
- Check existing sequences; edit, do not duplicate.
- Record a compact `Pre-flight:` line in the sequence's reasoning or notes field. If it is missing, do not build.

Stage for approval. Confirm to the requester: contact, company, sender, step count, the hook in one line, and the sequence link.

Do not approve it yourself unless the requester explicitly says to.

After staging, the `EVENT-ATTENDEE` line should already exist from Step 6 of the main skill. If outreach is the first proof this named person is in play for the event and Step 6 somehow skipped it, write it now.

## What good looks like

The opener could only have been written by the person who stood in that conversation. A mediocre draft could have gone to anyone you scanned.

Failure modes: a second connection request while one is pending; DMs before they accept; the account owner running a parallel cadence to the 1:1; pitching in the first message; auto-send; reaching them during a wait they asked for.
