---
name: acquired-brand-gtm-integration
title: Acquired-brand GTM integration
description: |
  Use this skill immediately after acquiring a product or brand, before combining websites,
  customer data, pipelines, messaging, analytics, or campaigns. Produces a staged GTM
  integration plan that preserves active demand and customer access while defining what to
  retain, endorse, consolidate, or retire.
category: RevOps
tags: [Leadership, RevOps, Marketing]
---

Use this when an acquisition creates pressure to integrate before demand, customer journeys, permissions, and systems are understood. It produces a decision record, risk map, and reversible sequence of GTM changes.

## Establish the integration boundary

1. Name the acquisition thesis in one sentence: distribution, product expansion, market entry, customer access, talent, or brand equity. Reject activities that do not support it.
2. Inventory the demand system before changing it: domains, search and direct demand, forms, account paths, communications, pricing, records, attribution, partners, reviews, and campaigns.
3. For every asset, record the current owner, system of record, audience, business value, failure impact, permission basis, and rollback path. Unknown is a valid status; assumed is not.

Do not treat legal ownership as proof that identities, consent, contracts, or customer expectations can be merged. The first integration output is a map of boundaries, not a rebrand plan.

## Choose a brand posture

Assign one posture to each customer-facing surface:

- **Retain:** the acquired identity carries demand or trust worth protecting.
- **Endorse:** keep the identity but clarify the parent-company relationship.
- **Absorb:** migrate only when journeys, demand, promises, and data rights are preserved.
- **Retire:** remove only after traffic, customers, records, and obligations have verified destinations.

Apply posture per surface, not once for the whole acquisition. A product name may remain while billing identity, legal disclosure, analytics ownership, and sales operations change separately. Use `references/brand-posture-decision-matrix.md` when stakeholder preference outruns evidence.

## Segment people before systems

Split records by relationship and permission before deduplication:

1. active customers and contracted users;
2. open opportunities with a named owner and next step;
3. opted-in marketing contacts;
4. historical leads without current permission;
5. workers, applicants, suppliers, or partners whose relationship is not a sales lead.

Resolve duplicate identities without collapsing provenance. Preserve source brand, permission, contract entity, acquisition channel, and last meaningful interaction. A shared email does not make records interchangeable, and an acquired database is not automatically a campaign audience.

## Protect live demand before consolidation

Trace each high-intent path: branded search, pricing, contact, registration, login, password reset, demo, email reply, and sales handoff. Assign an owner and rollback.

Keep brand analytics and attribution separable even under central ownership. Consolidated reporting can sit above brand data; it cannot recover overwritten provenance. Preserve working pricing and product language until the commercial owner approves replacements across every affected surface.

## Sequence by reversibility

Run the integration in gates:

1. **Observe:** inventory, export configurations, baseline demand, and document unknowns.
2. **Separate ownership from experience:** establish company control of domains, analytics, mail, repositories, and records without changing customer-facing journeys.
3. **Stabilise:** repair broken paths and assign operating owners while retaining provenance.
4. **Test:** preview messaging, routing, redirects, reporting, and handoffs with approved internal or low-risk records.
5. **Migrate:** change one surface at a time with rollback criteria and explicit approval.
6. **Retire:** remove duplicates only after observation shows no unresolved demand or customer dependency.

Score readiness with `references/integration-readiness-scorecard.md`. A calendar date never overrides a failed critical gate.

## Communicate by audience and consequence

Customers need to know what changes, what stays, who operates the service, and whether action is required. Leads need continuity, not an acquisition story. Internal teams need owners, systems of record, and escalation paths.

Draft communications only after the operational path exists. Use `references/communication-and-approval-gates.md` for approval decisions. Never promise seamless integration while login, support, billing, or data handling remains uncertain.

## What good looks like

- The operator notices broken journeys and permission mismatches before visual inconsistency.
- Every retained or changed asset has evidence, an owner, a system of record, an approval state, and a rollback.
- Brand-level demand and attribution remain measurable after parent-level reporting is introduced.
- No active customer, qualified opportunity, or high-intent route becomes unreachable during integration.
- The mediocre version starts with logos and a CRM import; the strong version starts with provenance, customer continuity, and reversible gates.
- The final plan makes unknowns visible rather than hiding them behind a single migration deadline.

See `references/worked-integration-case.md` for an anonymised example that keeps a legacy application live while modernising the public GTM layer.

## Rules

- MUST preserve record provenance, permission basis, and working customer access until replacements are verified.
- MUST require explicit human approval before bulk messaging, record merges, campaign launches, domain cutovers, pricing changes, or destructive retirement.
- MUST separate reversible control changes from irreversible customer-facing changes.
- NEVER infer marketing consent from acquisition ownership, CRM presence, or prior product use.
- NEVER combine analytics, domains, pricing, or pipelines merely to make the acquisition look complete.
- NEVER call a migration successful without read-back evidence for customer journeys, routing, attribution, and rollback readiness.
