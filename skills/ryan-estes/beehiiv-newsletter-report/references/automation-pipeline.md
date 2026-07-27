---
title: Automation pipeline
description: (reference)
---

# Automation pipeline

## Split deterministic data from generated narrative

Treat these as two separate jobs with two different reliability bars, run in sequence:

1. **Deterministic data** (correctness matters absolutely, no room for interpretation): post
   stats and rollups, poll tallies, audience segments, list health, growth-series appends. Do
   this with plain code (a script, a job, a typed function), not an LLM, because several of
   these require cursor-paginating an endpoint fully and doing exact arithmetic (see the poll
   and audience segmentation notes in `beehiiv-api-reference.md`); a model asked to "compute the
   poll results" is liable to stop at whatever page it fetches first and silently under-report.
2. **Generated narrative** (headlines, highlights, opportunities, rate-analysis prose): this is
   the one place an LLM pass is the right tool, precisely because it needs to read like someone
   actually looked at the numbers. Scope it tightly: only regenerate the narrative for the
   period whose underlying numbers actually changed, matching the existing tone and length, and
   leave every other period's prose untouched. Wholesale regeneration on every run produces
   visible tonal drift between runs and makes the diff impossible to review.

## Multi-tenant registry pattern

If the same pipeline runs across several publications (different clients, different sponsors),
keep one registry (JSON/YAML) listing, per publication:

- A slug/identifier and human-readable name.
- Where its report data lives (a file path, a database key, whatever the storage is).
- The environment variable names holding its publication ID and API key (never the credentials
  themselves in the registry).
- Its growth-series mode (`per-issue` / `subscriber-timeline`, see
  `beehiiv-api-reference.md`) and any freeform notes about that report's specific conventions
  (e.g. "this one has pre-migration months that use a different data shape, don't touch them").

Drive the refresh job by iterating the registry, and make each entry's failure independent: if
one publication's credentials are missing or its API calls fail, log it and skip to the next
entry rather than aborting the whole run. A single broken credential should never block every
other client's report from refreshing.

## Refresh flow, in order

1. Start from a clean checkout of the latest committed report data (pull before doing anything).
2. For each registry entry: fetch confirmed posts with stats; reconcile against what's already
   stored (refresh numbers for issues already present in case Beehiiv has more mature figures;
   insert genuinely new issues in their correct chronological position); recompute affected
   month rollups.
3. Append to the growth series according to that entry's mode.
4. Regenerate poll results and audience segments via the deterministic scripts (steps 1-2 in the
   split above), not the narrative pass. These commonly opt in per-report via explicit markers
   in the data file (e.g. a `POLLS_START`/`POLLS_END` region), so a report can be onboarded to a
   new section before its historical data exists, and a script can safely skip any report that
   hasn't opted in without erroring.
5. Run the narrative pass, scoped to only the newly changed period(s).
6. **Validate before shipping anything**: type/schema-check the changed data, and run any
   content-policy lint relevant to the project (banned phrases, required disclosures, etc.)
   against exactly the files that changed. Abort the entire run without committing if validation
   fails, and leave the working tree as-is for a human to inspect: never partially ship.
7. If nothing actually changed for a given publication, leave its files untouched and say so in
   the run log; don't force a commit just because the job ran.
8. Commit, push, and deploy only after every gate passes. Log a one-line summary per publication
   (what changed, or "no change") so a scheduled/unattended run is auditable after the fact.

## Idempotency and scheduling

Run on a fixed schedule (e.g. weekly, timed to when a publication typically sends its issue for
the week) via whatever job scheduler is available (cron, a managed scheduler, a CI pipeline). A
rerun with no new upstream data should produce zero diff and exit cleanly rather than generating
a no-op commit or duplicate narrative pass; treat "nothing to do" as the expected common case,
not an edge case.
