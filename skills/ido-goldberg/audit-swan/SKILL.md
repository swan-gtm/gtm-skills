---
name: "audit-swan"
title: Audit Swan
description: "Checks whether a Swan workspace is structurally healthy. Use for configuration audits that surface missing knowledge, disconnected integrations, exhausted senders, broken triggers, sparse CRM data, and credit or subscription issues."
category: RevOps
---

## Instructions

### What this skill checks

Eight structural dimensions. Each is small — most produce 0-2 findings. Process them one at a time, write down the verdict (OK / WARN / FAIL) + a one-line summary, and move on. Do not try to gather all eight dimensions' raw data before reasoning. By the time you reach the report, you should have eight short verdicts in hand, nothing more.

---

### Dimension 1 — Subscription and credits

`swan-get-subscription`. Check three things:
- Plan tier (FREE / paid).
- Credit balance + recent burn rate. If you don't have burn data in the response, estimate from a small `swan-search-sequences` recent-activity sample (page 10) — don't pull the full log.
- Feature flags vs. what active plays use.

Verdict:
- FAIL: out of credits, or active plays use features not enabled.
- WARN: < 30 days runway.
- OK: comfortable.

One-line summary. Move on.

---

### Dimension 2 — Org knowledge

`swan-get-memory` for org memory.

Required:
- ≥ 1 ICP segment.
- ≥ 1 persona per primary buying motion.
- Value prop set and non-trivial.
- Target markets defined.
- Competition documented.

Verdict:
- FAIL: ICP missing or value prop empty.
- WARN: any other missing or stale (no update in 90+ days).
- OK: all current.

One-line summary.

---

### Dimension 3 — Senders

`swan-get-org-senders` (this returns a small list — usually < 10 senders). Per sender, check auth status and capacity headroom.

Verdict:
- FAIL: no working sender, or all senders 100% saturated.
- WARN: any sender 80%+ saturated for > 7 days, or auth-broken channel that a play expects.
- OK: ≥ 1 healthy sender with capacity.

One-line summary.

---

### Dimension 4 — Integrations

For each integration referenced by an active trigger:
- Connected and authorized.
- Last successful sync recent.

If integration is referenced by an active trigger but not connected: FAIL.

Don't enumerate integrations the org doesn't use. One-line summary.

---

### Dimension 5 — Active triggers (gradual)

Pull active triggers, page size 10. For each:
- Required inputs available? (sender connected, list exists, integration present)
- Has it fired ≥ 1 time in 60 days, or is it new?

Most triggers are healthy. Stop after the first 10 unless ≥ 3 problems surface — then pull more.

Verdict per trigger group, summarized to one line.

---

### Dimension 6 — CRM hygiene

Only if a CRM is connected. Two tiny calls:
- `hubspot-list-object-properties` for companies. Check that the properties active plays depend on exist.
- `hubspot-search-objects` with page size 10 to sample populated-ness of `hubspot_owner_id` + lifecycle stage. 10 is enough to spot a hygiene problem.

Verdict:
- FAIL: < 50% of sampled records have core fields, or referenced properties missing.
- WARN: < 80%.
- OK: ≥ 80%.

---

### Dimension 7 — Execution errors

Pull execution log, last 7 days, page size 20.

If > 20 failures returned in the truncated preview: switch to `swan-execute-code`. Read `files/tool-outputs/<filename>`, group by `errorClass` in pandas, print classes with count > 3.

Verdict based on top class count: > 10 → FAIL, 3-10 → WARN, < 3 → OK.

---

### Dimension 8 — Skill library hygiene

Quick check: any orphan child skills (path points to a deleted parent)? Any duplicate display names across personal + org scope?

Usually clean. If WARN, one-line note. Otherwise skip.

---

### Composing the report

After all eight dimensions, the agent has eight one-line verdicts. Compose:

```
SWAN DOCTOR REPORT

FIX NOW:
  - <every FAIL, one line each with the exact tool to use>

PAY ATTENTION:
  - <every WARN, one line each>

ALL CLEAR:
  - <every OK dimension, one line each — "Subscription: OK ($45 credit, ~28 days runway")>

NEXT STEP:
  <one sentence: the single highest-impact thing to fix>
```

If no FAILs: lead with "no critical issues" before the WARN section.

---

### Rules

- MUST process dimensions sequentially. Each dimension's verdict + one-line summary is committed before the next runs.
- MUST cite specifics ("3 FAIL: 2 from HubSpot 401s, 1 from missing sender") not generalities ("integration issues").
- NEVER change anything. This skill is read-only.
- NEVER pull large logs in full. Use code + file-pointer if a list is > 20 items.
- If the org is < 7 days old, skip Dimensions 5-7 and label the report as "early-stage check — performance dimensions will populate as you use Swan."
