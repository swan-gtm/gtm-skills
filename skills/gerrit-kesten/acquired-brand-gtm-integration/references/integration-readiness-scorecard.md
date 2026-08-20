# Integration readiness scorecard

This scorecard governs a customer-facing migration, not ownership transfer. Score eight domains from 0 to 3. Maximum: 24.

## Scale

- **0, Unknown:** no trustworthy evidence or owner.
- **1, Mapped:** current state documented, but replacement or rollback is untested.
- **2, Tested:** replacement and rollback tested with approved low-risk data or users.
- **3, Verified:** production-equivalent path, owner, monitoring, and read-back evidence exist.

## Domains

| Domain | Evidence required for a 3 |
|---|---|
| Customer access | Login, reset, registration, and support paths verified by user type |
| Demand capture | High-intent pages, forms, replies, routing, and ownership read back end to end |
| Data provenance | Source brand, consent, contract entity, lifecycle, and exceptions retained |
| Commercial continuity | Pricing, packaging, billing identity, and sales promises have an approved source of truth |
| Measurement | Brand-level traffic, conversions, pipeline, and campaign attribution remain separable |
| Search and reputation | Redirects, canonicals, rankings, backlinks, reviews, and listings have mapped destinations |
| Communications | Audience, message, sender, support path, approvals, and suppression rules are ready |
| Rollback and ownership | Named operator, escalation, rollback trigger, restoration steps, and monitoring are tested |

## Go/no-go rule

Proceed only when:

- total score is at least **20 of 24**;
- customer access, demand capture, data provenance, and rollback each score **3**;
- no domain scores **0**;
- every bulk send, merge, pricing change, domain change, or retirement has explicit human approval.

A score of 20 is not a claim that the integration is finished. It means one specific migration step has enough evidence to run under monitoring.

## Stop conditions

Pause or roll back when any of these occurs:

- a known customer cannot access the expected path;
- high-intent submissions stop routing or lose ownership;
- source or consent provenance is overwritten;
- a redirect or canonical sends demand to a non-equivalent destination;
- brand-level conversions can no longer be reconstructed;
- customer communication creates commitments the operating team cannot honour;
- the observed state differs from the approved migration record.

## Read-back table

```text
Change:
Pre-change baseline:
Expected result:
Observed result:
Evidence link or report:
Exceptions:
Rollback threshold:
Owner:
Approval:
Decision: proceed | pause | roll back
```

Score each migration step independently. A successful website change does not prove CRM, email, pricing, analytics, or customer access readiness.
