---
name: crm-health-scoring
title: Score CRM health over time
description: |
  Use this skill when leaders need a repeatable measure of CRM reliability, its trend, and the defects driving it. Produces a deterministic health score, object- and rule-level diagnostics, a confidence statement, and a prioritized remediation queue.
category: RevOps
tags: [RevOps, Leadership]
---

Use this when a team needs to measure whether CRM reliability is improving. Produce a reproducible score and diagnosis, not a decorative grade.

## Define health as rules

Translate “clean CRM” into explicit checks across identity, ownership, completeness, pipeline integrity, process conformance, and integration drift. Every rule must declare its population, condition, severity, evidence, exclusions, and owner.

Measure only fields and relationships that influence execution or decisions. Do not reward filling optional fields merely because they are easy to count. Keep rule definitions versioned; a changed rule creates a new baseline and must not be presented as organic improvement or decline.

## Score the population

Calculate rule failure rates on eligible records. Weight by business impact, not raw finding count. A handful of duplicate accounts splitting live opportunities can matter more than thousands of missing optional fields.

Score objects separately before rolling them up. Contacts, accounts, opportunities, and activities have different populations and failure modes. Use [references/scoring-model.md](references/scoring-model.md) for a deterministic 0–100 model and minimum sample rules.

Report the score with:

- evaluated and excluded record counts;
- rule failures and rates;
- object-level scores;
- top contributors to lost points;
- rule-set version and snapshot time;
- confidence or coverage limitations.

Never hide an unevaluable rule by scoring it as passing. Mark it unknown and explain what data is missing.

## Diagnose the movement

Compare snapshots only when the rule set and eligible population are comparable. Decompose change into corrected records, newly introduced defects, population changes, and definition changes.

Look for source concentration. Break failures down by integration, form, import, owner, segment, record age, and pipeline stage. A worsening score caused by one new source calls for a source control; a broad decline may indicate incentives or process design.

Read [references/worked-health-review.md](references/worked-health-review.md) for an example where the overall score improves while opportunity health worsens.

## Prioritize remediation

Rank rule-source combinations by severity, affected share, recurrence, and downstream reach. Fix ongoing creation of defects before paying down the backlog. Prioritize identity and ownership defects that contaminate routing, signals, and reporting across several workflows.

For every remediation item, name the source, accountable owner, immediate containment, durable control, target metric, and review date. Keep corrective writes in a separate reviewed plan; a health report does not authorize changes.

## Establish the cadence

Save snapshots on a consistent schedule and after material migrations or cleanups. Use weekly measurement for operational databases and monthly leadership review unless the data changes more slowly. Annotate migrations, acquisitions, new integrations, and rule changes.

Set targets by critical rule as well as total score. A 95 overall score is unacceptable if customer suppressions or ownership routing still fail. Trend the number of recurring defects, not only the remaining backlog.

## What good looks like

- Another operator can reproduce the score from the rule definitions and snapshot.
- Object-level results reveal where the system is unhealthy.
- Unknown and excluded records remain visible.
- Trend explanations separate fixes, new defects, population movement, and rule changes.
- The remediation queue points to sources and owners.
- Critical safety and routing rules have explicit targets independent of the composite score.

The mediocre version averages field completeness, awards a green badge, changes definitions without rebasing, and celebrates improvement caused by excluding difficult records.

## Rules

- MUST version rules and preserve eligible, excluded, failed, and unknown counts.
- MUST report object- and rule-level results with the composite score.
- MUST require separate approval before applying any remediation.
- NEVER score unevaluated records as passing.
- NEVER compare incompatible snapshots without a visible rebaseline.
- NEVER let a composite score mask a failing critical rule.
