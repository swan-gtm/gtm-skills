---
name: "reverse-etl-activation"
title: Reverse ETL activation
description: "Use this skill when you need to turn a scored, segmented audience sitting in the warehouse (BigQuery, Snowflake, Redshift) into live GTM motion, syncing accounts, contacts, and computed traits out to the CRM, ad platforms, and sequencing tools. It encodes the judgment that keeps reverse ETL from quietly polluting every downstream system: identity resolution before any write, a change-data-capture diff so only real deltas move, field-level mapping with type and format guards, suppression and consent gates, sync scheduling matched to each destination's rate limits, and a mandatory dry run plus row-count reconciliation before and after the live push. Every threshold (match-confidence floor, batch size, sync cadence, max-delete guard, suppression rules) is a tunable default. Each run produces a validated sync plan, a dry-run diff of adds, updates, and suppressions with counts, and a reconciliation report after the live sync."
category: RevOps
---

# Reverse ETL activation (warehouse to GTM)

The warehouse is the source of truth. This skill moves a computed audience out of it and into the tools where GTM actually happens, without corrupting those tools. The failure mode this skill exists to prevent: a naive "sync the table" job that writes half-matched rows, re-writes unchanged records, blows past API limits, and pushes suppressed or non-consented contacts into a sequence. Do it in this order every time.

## Inputs (block and ask if missing)
- **Source**: warehouse + the exact model/table of the scored/segmented audience (e.g. `analytics.gtm.enterprise_high_intent`). Confirm the grain: account, contact, or both.
- **Destination(s)**: CRM (Salesforce/HubSpot), ad platform (Meta/Google/LinkedIn), and/or sequencer (Outreach/Salesloft/Swan). Each has its own object model and limits.
- **Sync key**: the stable identifier used to match a warehouse row to a destination record (domain, email, CRM Id, ad-platform match key).
- **Field mapping**: which warehouse columns map to which destination fields, and which are read-only in the destination.

## Procedure

1. **Resolve identity BEFORE writing.** Map each warehouse account/person to a destination record on the sync key. Apply a match-confidence floor (default `0.90`). Rows below the floor are quarantined to a review list, never guessed into a create. Ambiguous many-to-one matches (two warehouse rows, one CRM account) are collapsed by a deterministic rule (most-recent, highest-score), never duplicated.
2. **Compute the change-data-capture (CDC) diff.** Compare the resolved audience to the last-synced state. Only real deltas flow: new adds, changed updates (field-level, not whole-row), and intended removals. Unchanged rows never sync (this is what wrecks API budgets and audit logs).
3. **Map fields with type/format guards.** Coerce and validate every mapped field: dates to the destination's format, enums to allowed picklist values, currency/number types, string length caps. A row that fails schema is rejected to an error list with the reason, not force-written.
4. **Apply suppression + consent gates.** Drop anything on the do-not-contact / unsubscribe list, anything failing region/consent (GDPR/CCPA), and anything a channel-specific rule excludes (e.g. no ad-platform push for opted-out contacts). Suppression runs AFTER matching so you can log exactly who was held and why.
5. **Batch + schedule to the destination's limits.** Chunk to each API's batch size and rate limit (default batch `200`), backoff on 429s, and schedule cadence per destination (default: CRM near-real-time, ad audiences hourly, sequences gated on an explicit enrollment step, never automatic).
6. **Dry run first.** Emit the planned adds / updates / suppressions / errors with counts and a sample of each. Enforce a **max-delete guard**: if intended removals exceed a share of the audience (default `10%`), ABORT and surface it, do not mass-delete on a bad upstream run. Require sign-off unless the run is under an auto-approve threshold.
7. **Live sync, then reconcile.** Execute, capture per-row success/failure, and produce a reconciliation report: expected vs. written counts per object, error rows with reasons, suppressed rows. Persist the new sync state so the next run's CDC is correct.

## Tunable defaults
`match_confidence_floor: 0.90` · `batch_size: 200` · `max_delete_guard: 0.10 of audience` · `auto_approve_under: 500 rows` · `sequence_enrollment: manual gate` · `cadence: {crm: realtime, ads: hourly, sequencer: on-enroll}`

## Outputs
- **Sync plan**: resolved audience, field map, per-destination schedule.
- **Dry-run diff**: adds / updates / suppressions / errors with counts + samples.
- **Reconciliation report**: expected vs. written per object, error rows with reasons, suppressed rows, new sync-state pointer.

## Notes
- Never let the sequencer auto-enroll off a warehouse sync; a bad upstream filter becomes a mass mis-send. Enrollment is always a separate, gated step.
- If identity resolution can't clear the floor for a meaningful share of the audience, the problem is upstream (missing keys), not here. Fix the model, don't lower the floor.
- The warehouse is authoritative for computed traits (scores, tiers, segments); the CRM is authoritative for rep-owned fields. Never let a sync overwrite a rep-owned field.
