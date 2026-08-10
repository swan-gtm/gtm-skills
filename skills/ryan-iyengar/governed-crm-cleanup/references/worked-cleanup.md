# Worked cleanup

A team finds 312 ownerless contacts, 46 duplicate account groups, and 81 open opportunities with past close dates.

The ownerless contacts trace to one form integration whose fallback owner was removed. Fix that source first. Plan 50 deterministic assignments where territory rules identify exactly one active owner; route 12 conflicting territories for human decisions. Leave the remainder untouched until the next reviewed batch.

For duplicates, require an exact normalized domain plus corroborating company evidence. Choose the survivor by active relationships and completeness, not creation date alone. Start with ten groups. Preserve identifiers from merged records in the operation log.

For past close dates, do not invent new dates. Create review tasks for opportunity owners with the last meaningful activity and stage evidence. A missing decision is not a data-cleaning inference.

Immediately before application, one contact has acquired an owner. Mark that operation stale and skip it. After application, re-run all three rules and reconcile: 50 planned assignments, 49 applied, one stale, zero unexplained. Report the source control separately from the reduced backlog.
