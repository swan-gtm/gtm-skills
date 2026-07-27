---
title: "Tiering a net-new company"
description: Reference for the Track contact job changes skill.
---

# Tiering a net-new company

When a confirmed mover lands at a company **not** already in the CRM, decide whether it's worth creating
as an account. Score the enriched company against the operator's fit criteria from setup. Keep it
deterministic and auditable — the operator should be able to read why a company was or wasn't a fit.

## The rubric

Evaluate only the criteria the operator actually defined; a criterion they left blank is not a filter.
Typical criteria:

- **Employee count** within a floor/ceiling range.
- **Revenue** above a floor.
- **Industry / market** matches one of the target verticals (check industry, description, and keywords).
- **Keywords** — target technologies, motions, or descriptors appear in the company's profile.
- **Geography** — headquartered in a target country/region.

**Fit (Tier 1):** every defined criterion that was evaluated passes → propose creating the account, then
update the contact onto it and set the account tier.

**Non-fit (Tier 2/3):** any defined criterion fails → **skip & flag** (do not create the account), record
the tier and a needs-attention flag, but still update the contact's new company and title so the record
is honest.

**No criteria evaluated:** if nothing could be scored (missing enrichment, or no rules defined), do **not**
auto-promote to fit — treat as non-fit / needs review, and surface why.

## Notes

- Record the pass/fail reasons alongside the proposal so the approval step shows the operator the
  evidence, not just a verdict.
- Both tiers end at an updated contact — the difference is only whether a new account is created.
- Never create an account here for a company that a stronger identifier shows is already in the CRM under
  a different name; that belongs to the "already in CRM" branch, not this one. See [matching.md](matching.md).
