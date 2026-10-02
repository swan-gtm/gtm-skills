# Operating numbers, experiment gates and economics

These are the adopted operating limits for a pre-first-client solo operator. They are ceilings and decision rules, not benchmarks or conversion predictions.

## Volume ceilings (not quotas)

| Limit | Value |
|---|---|
| Marketplace proposals | max 5 per day |
| Warm asks | max 2 per day |
| Follow-ups | max 1 per recipient, after 5 business days |
| Acquisition spend | $50 total per round, including bid credits and fees; no paid boosts |

A day with zero qualified postings is a day with zero proposals. Never lower the rubric thresholds to fill the ceiling.

## Capacity caps

| Queue | Cap | When full |
|---|---|---|
| Drafts awaiting human review | 8 | Stop sourcing and drafting until reviewed |
| Live prospect conversations | 4 | HOLD new KEEPs; do not start new threads |
| Delivery | 1 paid diagnostic, then 1 implementation at a time | Decline or schedule; never overlap two uncertain builds |

Unreviewed drafts are not pipeline. A full review queue pauses production rather than turning drafts into automatic sends.

## Review gate: every 10 sent attempts

Count per channel, with denominators. Only observed events: sent, reply, qualified conversation (passed the rubric after talking), paid diagnostic, paid implementation.

| Result after 10 sent | Read it as | Next |
|---|---|---|
| 0 meaningful replies | Channel, proof or eligibility problem. Not "no demand" | Review targeting, proof shown and proposal shape; check deliverability where relevant; change one thing |
| Replies but no qualified conversation | Scope, budget or trust mismatch | Tighten hard stops and the first screen |
| 2 qualified conversations or 1 paid pilot | Signal worth another round | Run another bounded round at the same caps |
| Demand present, price failing | Offer problem | Change scope, buyer size or channel; never promise more to close |

Never raise price automatically from a reply rate. An empty denominator is N/A, not 0%. A blocked or unsent round is not a failed round.

## Economics

Contribution per hour = (collected price − platform fee − acquisition cost − vendor costs − refund allowance) ÷ all hours (acquisition, scoping, delivery, learning, support).

- Floor: $50/hour contribution, before tax.
- Re-scope after two consecutive pilots below the floor.
- Set the support reserve explicitly in every quote; never let it silently be zero.
- Count each benefit to the buyer once. Capacity freed is not cash saved.

## Pricing

No public price menu. Quote each bounded scope individually, after scope, fees and support reserve are known. Uncertain scope gets a paid diagnostic first; the diagnostic is a standalone deliverable, not a free discovery call.
