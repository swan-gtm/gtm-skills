# Follow-up and handoff matrix

Timing starts when the underlying signal becomes available and reliable, not merely when the webinar ends.

## Default matrix

| Segment | Default timing | Content | Sales action |
|---|---|---|---|
| Priority score with decision signal | Same business day review | Reflect exact problem or question | Named owner reviews and approves personal follow-up |
| Review score | Within one business day | Verify fit and relationship first | Accept, reject with reason, or return for research |
| Attended, relevant, below sales threshold | Within one business day | Session takeaway or answer tied to attended topic | No sales task unless another signal appears |
| Replay viewer with new intent | Within one business day of replay signal | Continue the topic they watched | Re-score; create review only if gates are met |
| No-show | Within one business day of event end | Replay or concise summary | No sales task from no-show alone |
| Existing customer | Same business day routing when signal is material | Customer-relevant context | Route to customer owner |
| Active opportunity | Same business day routing | Add question and engagement to deal context | Route to opportunity owner |
| Meeting booked | Immediate state update | Only meeting logistics and useful preparation | Stop booking nurture; prepare handoff |
| Unsubscribed or disqualified | No marketing follow-up | None | Apply suppression and retain reason |

These timings are operating defaults. If platform data arrives late or changes, use the verified state rather than sending against stale data.

## Sales handoff packet

Every accepted handoff should contain:

```text
Person and account:
Role and fit evidence:
Original source and campaign:
Webinar and session/topic:
Live/replay/no-show evidence:
Exact registration answer or question:
Fit score / Engagement score / Intent score:
Existing customer, opportunity, or prior conversation:
Recommended conversation angle:
Reason to act now:
Owner:
Approval state:
```

The handoff should take less than a minute to understand. Link to source evidence rather than pasting unnecessary personal data into multiple systems.

## Approval gates

Require explicit human approval before:

- sending an individual sales message;
- launching or changing a bulk follow-up;
- enrolling anyone in a sales or marketing sequence;
- merging uncertain identities;
- overriding an unsubscribe, customer owner, opportunity owner, or disqualification;
- making product, pricing, legal, compliance, security, or timing promises.

Automatic internal updates are acceptable when they are idempotent, reversible, and monitored: recording events, calculating scores, adding suppression, creating review tasks, and attaching source context.

## Message rules

- Reference the topic or exact question, not generic attendance.
- Do not claim someone attended when only registration is known.
- Do not say “sorry we missed you” unless no-show state is verified.
- Do not manufacture scarcity or urgency.
- Use one clear next step.
- A replay link is value delivery, not permission for an unrelated sales sequence.
- If a personal message is approved, read back the final recipient, text, and send result. An ambiguous result is investigated, not retried automatically.
