---
name: hygiene-gated-outbound
title: Hygiene-gated outbound
description: |
  Use this skill before launching outbound from CRM segments when duplicates, ownership gaps, or stale contact data may distort targeting. Produces a launch readiness decision, a bounded remediation plan, and a clean, owned audience for outreach.
category: Outreach
tags: [Sales, RevOps, Demand Gen]
---

Use this before activating a CRM-derived audience. Produce a go, conditional go, or stop decision with the minimum cleanup needed for safe execution.

## Define the execution slice

Name the campaign objective, ICP filters, exclusions, channel, planned volume, owners, and launch date. Materialize the exact accounts and contacts that would enter the campaign. Do not substitute an overall CRM health score for inspection of the actual slice.

Record baseline counts: accounts, contacts, contacts per account, reachable contacts, ownerless records, duplicates, suppressed records, active opportunities, customers, and people contacted inside the campaign cooldown. Reconcile account and contact joins; a clean contact table can still point into duplicate or ownerless accounts.

## Run the launch gates

Evaluate five gates:

1. **Identity:** account domains and contact identities resolve without material duplicate risk.
2. **Ownership:** every target has one accountable owner or an explicit routing rule.
3. **Reachability:** channel details are verified enough for the planned action.
4. **Context:** customers, active deals, prior objections, recent touches, and legal suppressions are respected.
5. **Fit:** every target can be traced to the campaign’s ICP and inclusion reason.

Use [references/readiness-rubric.md](references/readiness-rubric.md) for thresholds. Any hard conflict stops the affected record even if aggregate readiness passes.

## Remediate in dependency order

Fix account identity before contact targeting because duplicate accounts split activity, ownership, and signal history. Resolve ownership before drafting so replies and tasks have an accountable destination. Apply suppressions before calculating reachable volume. Refresh contact details only after the target population is stable.

Create a reviewable plan for each correction. Separate safe fill-from-owned-source operations from human decisions such as duplicate survivors, territory exceptions, and disputed active opportunities. Use small batches and re-read current values before applying approved changes.

Do not turn launch preparation into an unlimited CRM transformation. Bound remediation to defects that can change targeting, context, ownership, deliverability, or measurement for this campaign. Put broader work in a separately owned backlog.

Read [references/worked-launch.md](references/worked-launch.md) for a conditional launch example.

## Rebuild and approve the audience

After remediation, regenerate the audience from the source filters rather than editing the original export. Re-run every gate and reconcile why records entered or left. Sample at least ten targets across segments and owners, including edge cases.

Present the final audience, remaining exceptions, expected reachable volume, owner distribution, and suppression counts. Require an explicit launch decision. A conditional go must name the excluded population and the condition for adding it later.

## Measure without corrupting the loop

Attach outcomes to stable account, contact, owner, segment, and campaign identifiers. Watch for duplicate touches, reply routing failures, and unexplained audience growth during execution. Stop the affected slice when ownership or suppression state changes materially.

Compare response quality by readiness defects as well as message variant. Poor data can masquerade as poor messaging, while aggressive cleanup can hide targeting mistakes by shrinking the denominator.

## What good looks like

- The launch decision evaluates the exact audience, not the whole database.
- Every target has fit evidence, one owner, verified context, and a stable account relationship.
- Suppressions and active opportunities are visible before drafting.
- Remediation is bounded, reviewable, and rerun from source afterward.
- Excluded records have explicit reasons and a route back into eligibility.
- Outcome reporting can distinguish data failure from targeting or messaging failure.

The mediocre version exports a list, patches obvious blanks in a spreadsheet, ignores account duplication, and launches because the total count looks plausible.

## Rules

- MUST resolve identity, ownership, context, reachability, and fit before launch.
- MUST regenerate the audience after remediation and require human launch approval.
- NEVER outreach to unresolved duplicates, active conflicts, or suppressed contacts.
- NEVER silently assign ownerless targets or invent missing contact data.
- NEVER allow a deadline to waive hard safety and context gates.
