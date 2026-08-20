# Lifecycle states and suppression

A webinar record needs one current state plus its event history. Do not overwrite the history when the state advances.

## State precedence

Highest state wins for routing:

1. unsubscribed or disqualified;
2. customer or active opportunity;
3. meeting booked;
4. sales review accepted;
5. priority sales review pending;
6. attended live or watched replay;
7. no-show;
8. registered, event pending.

Unsubscribed and disqualified are communication stops, not deletion instructions. Retain only the data that the organisation is permitted or required to keep.

## State definitions

| State | Required evidence | Allowed next action |
|---|---|---|
| Registered, pending | Valid registration for a future event | Event confirmation and permitted reminder |
| Attended live | Verified event attendance | Score engagement and questions |
| Watched replay | Verified replay event | Score replay and any later intent |
| No-show | Registered; event ended; no verified live/replay activity | Replay or summary, subject to permission |
| Sales review pending | Score and gates met; no hard suppression | Human checks fit, identity, relationship, and next step |
| Sales review accepted | Named owner accepted the handoff | Personalised sales action with approval |
| Meeting booked | Confirmed active meeting matched to the person | Stop lower-level booking nurture; prepare sales context |
| Customer | Verified current customer relationship | Route to customer owner; treat as adoption or expansion context |
| Active opportunity | Verified open opportunity | Route to opportunity owner; do not create a duplicate lead motion |
| Unsubscribed | Valid opt-out or objection | Suppress external marketing and sales nurture |
| Disqualified | Documented reason | Suppress or route according to the reason |

## Hard stops

Stop booking and qualification nurture when:

- a meeting is confirmed;
- the contact unsubscribes or objects;
- sales disqualifies the record;
- an active opportunity or customer relationship requires a different owner;
- the event or registration is cancelled;
- identity cannot be resolved safely.

A cancelled or rescheduled meeting is not the same as a no-show. Re-open the correct state only after reading the current meeting status.

## Conflict resolution

Use this order:

1. read current relationship and suppression state;
2. verify identity and event;
3. apply the latest harder state;
4. retain earlier events as history;
5. calculate the permitted next action;
6. confirm that competing sequences or owners will not act simultaneously.

## Reconciliation table

```text
Person/account:
Original source:
Event:
Registration state:
Attendance/replay evidence:
Current relationship:
Current lifecycle state:
Suppression reason:
Owner:
Last permitted action:
Next permitted action:
Evidence checked at:
```

Reconcile event records against the customer system and meeting system after each webinar. A webinar platform can prove registration or viewing; it cannot by itself prove customer status, opportunity ownership, or a valid meeting.
