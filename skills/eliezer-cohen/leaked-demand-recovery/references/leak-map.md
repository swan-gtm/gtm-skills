# Where demand leaks

Read this at step 2, when building the candidate list. Each row is a seam where two systems hand off
and neither owns the failure, which is why the loss is silent.

| Leak | Signal | Verify against |
|---|---|---|
| Booking never completed | Lead shared contact details through chat or a form, no meeting exists | Calendar AND CRM meetings |
| Meeting booked, never held | Event on the calendar, no recording or notes | Call recorder AND calendar |
| Call held, follow-up never sent | Recording exists, a commitment was logged, no outbound message | Complete sent history AND targeted per-domain search |
| Inbound reply never answered | The last message in the thread is theirs | The full thread, not search snippets |
| Live conversation with no record | A real thread in the mailbox, nothing in the CRM | The mailbox as source of truth |
| Closed lost on a blocker that changed | Loss reason was timing, coverage, a missing capability, or a departed champion | Loss reason AND current product and coverage state |
| Trial or pilot that ended quietly | Usage stopped, no close-out conversation | Product usage AND the mailbox |

## Which seams pay

The last two rows are the highest-yield and the most neglected, because neither generates an inbound
signal to remind anyone it exists. Everything above them is triggered by something arriving; a
closed-lost record whose blocker quietly expired, and a pilot that faded rather than ended, produce
no event at all. Nobody is reminded, so nobody looks.

Work them on a slower cycle than the active leaks, six to twelve months back, and re-check the loss
reason against what has actually shipped or opened since. A revival message that claims something
changed when nothing did is worse than silence, because it burns the one reason they would have
taken the call.

## Prioritising within a sweep

Rank confirmed drops by the strength of the original intent, not by how recent they are. Someone who
completed a form and sat through a call outranks someone who abandoned a chat widget, even if the
chat lead is fresher. Intent that survived several steps is the scarcer signal.
