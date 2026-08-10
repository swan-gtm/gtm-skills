---
name: governed-crm-cleanup
title: Governed CRM cleanup
description: |
  Use this skill when CRM data is unreliable, a cleanup is overdue, or a team is considering a bulk correction. Produces an evidence-backed audit, a reviewable change plan, approved corrections, and controls that prevent the same defects from returning.
category: RevOps
tags: [RevOps]
---

Use this when CRM defects affect routing, reporting, pipeline reviews, or execution. Produce a baseline, an operation-level correction plan, a verified result, and a prevention backlog.

## Establish the baseline

1. Snapshot the affected objects, field definitions, owners, pipeline stages, and automation rules before proposing changes. Record the extraction time and record counts.
2. Define each audit check as an explicit rule with a target population, condition, severity, and evidence. Cover duplicates, ownership gaps, stale pipeline, critical-field completeness, stage conformance, and integration drift.
3. Count findings by object, rule, owner, source, and age. Separate isolated bad records from systematic failures created by imports, forms, integrations, or team behavior.
4. Preserve ambiguous findings. An audit should expose uncertainty rather than convert it into a confident correction.

Use [references/audit-rubric.md](references/audit-rubric.md) to score severity and choose the first batch.

## Build the change plan

Represent every proposed change as one reviewable operation containing:

- record type and stable identifier;
- field or relationship being changed;
- current and proposed values;
- rule and evidence supporting the change;
- confidence, reversibility, and impact radius;
- whether a human decision is required.

Group operations by shared cause, but never hide record-level detail inside a bulk total. Separate deterministic corrections from judgment calls. Missing owners, unclear duplicate survivors, disputed lifecycle stages, and inferred values require named human decisions.

Prioritize in this order: changes preventing ongoing corruption, changes restoring routing or ownership, changes correcting live pipeline decisions, then cosmetic completeness. Keep the first batch small enough that a reviewer can inspect examples from every rule and reverse it without reconstructing the entire cleanup.

## Review and apply

1. Present the baseline and expected effect before asking for approval.
2. Sample at least five operations per rule, or every operation when the batch has fewer than five. Include edge cases, not only obvious successes.
3. Require explicit approval for the operation identifiers being applied. Approval of a summary is not approval of unseen records.
4. Re-read each target immediately before changing it. If the current value differs from the plan, stop that operation as stale rather than overwriting newer work.
5. Apply approved operations only. Log the before value, after value, approver, time, and outcome.
6. Re-run the same audit rules after the batch. Reconcile planned, applied, skipped, failed, and newly detected counts.

Read [references/worked-cleanup.md](references/worked-cleanup.md) for a complete example including a stale-value conflict.

## Prevent recurrence

Trace each recurring defect to its entry point. Choose the lightest durable control: validation at creation, duplicate resolution before creation, required stage evidence, owner fallback, integration monitoring, or a scheduled audit. Assign one owner to each rule and record the review cadence.

Do not call the cleanup complete when the backlog reaches zero. It is complete when the source is controlled, the rule is monitored, and the next review has an owner.

## What good looks like

- Every finding is reproducible from a written rule and visible evidence.
- Reviewers can explain why each value will change and can reject one operation without rejecting the batch.
- No correction overwrites a value that changed after planning.
- The post-run reconciliation accounts for every planned operation.
- High-impact defects shrink without raising another defect class.
- The prevention backlog names sources and owners instead of saying “keep the CRM clean.”

The mediocre version starts with mass edits, treats missing data as permission to guess, merges on names alone, and celebrates a temporary cleanliness score while the same imports continue creating defects.

## Rules

- MUST snapshot before changing records and retain operation-level evidence.
- MUST require explicit human approval for merges, deletions, ownership decisions, and bulk changes.
- MUST stop stale operations rather than overwrite concurrent edits.
- NEVER invent field values or silently convert uncertainty into a correction.
- NEVER send CRM data to an endpoint the operator does not own.
- NEVER declare success without re-auditing and reconciling outcomes.
