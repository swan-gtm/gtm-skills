# Platform assumptions

This play needs six capabilities from your sequencer and seven numbers about it. Confirm each in the platform's docs or with a test before building. If one is missing, use the fallback.

## Six capabilities

| # | Capability | Why it matters | If missing |
|---|---|---|---|
| A1 | Sequences can be grouped (campaign, list, tag, folder) and listed by group | The kill sweeps one group | Keep a sheet of sequence ids per cutoff and stop by id |
| A2 | A one-time scheduled job can run at an exact time | This is the self-kill | Use an external scheduler (cron, Zapier, Make, GitHub Actions) calling the platform's API. A calendar reminder is a last resort, and it is manual: say so |
| A3 | The job can stop running sequences with no human approval | Otherwise it waits on a person and does not self-kill | Use the platform's API with a key, or pause the whole group |
| A4 | Sequences already waiting (for a connection, a queue slot or a limit) can be stopped, and search can list them | These are the ones that fire late | List by "active or pending" status and by step, not only "sending" |
| A5 | A contact who replied has already ended automatically | The kill must not touch live conversations | Filter out contacts with a reply timestamp before stopping |
| A6 | The job can notify the owner (chat, email, task) | The owner needs the reply list and any failures | Write the result to a shared sheet or doc |

## Seven numbers to look up

- **P1 Sending window**: days and hours messages may go out, and in which timezone.
- **P2 Daily limits per inbox**: emails, LinkedIn messages and connection requests.
- **P3 Steps that ignore the window**: for example waits or connection requests.
- **P4 Acceptance wait**: how long a message waits for a connection before it expires.
- **P5 Queue**: how many contacts already wait ahead of yours on each inbox.
- **P6 One active sequence per contact per inbox**: whether a second one is rejected.
- **P7 Stop semantics**: whether stop pauses (resumable) or ends permanently, and whether that depends on the sequence state.

## Worked example: one platform's values (checked October 2026)

Re-verify against the platform's current docs before relying on them.

- P1: Monday to Friday, 09:00 to 19:00, applied in the sequence's timezone.
- P2: email up to 150 a day; LinkedIn messages 40 a day, or 80 with a Sales Navigator seat; connection requests 25 a day, or 50 with Sales Navigator.
- P3: connection requests and wait steps ignore the window.
- P4: a message waits up to 14 days for acceptance; then the LinkedIn steps expire and email steps continue.
- P5: read the per-inbox queue count before building.
- P6: yes. One active sequence per contact on a shared inbox.
- P7: stopping a running sequence pauses it and it can be resumed. Stopping one that is still awaiting approval rejects and archives it permanently.
- A3: the platform's docs say scheduled runs may approve or reject sequences awaiting review. They do not state whether a scheduled run can stop already-running sequences without an approval card. Test it once before a real event.

## Test the kill once per platform

Make a group with one test sequence to a teammate, schedule the kill a few minutes ahead, and confirm three things: it stopped without anyone approving anything (A3), nothing sent afterwards, and the notification arrived (A6). Write the result beside the numbers above.
