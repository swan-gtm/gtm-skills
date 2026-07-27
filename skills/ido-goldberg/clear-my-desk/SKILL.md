---
name: "clear-my-desk"
title: Clear my desk
description: "Triages pending Swan work for a user. Use to prioritize review items, sequence approvals, alerts, and suggestions into act-now, bulk-approve, acknowledge, or investigate buckets."
category: RevOps
---

## Instructions

**State check.** This skill assumes the caller is the user whose desk is being cleared and that the org actually generates review items and sequence approvals — i.e. at least one play or radar is wired up producing tasks. Run `swan-search-user-tasks` filtered to the caller as the first probe. If nothing comes back across statuses, the desk is empty because no plays are producing work yet, not because the user is on top of it — tell the user and recommend wiring up a radar or play before this skill becomes useful.

### What this skill does

The user has a backlog and wants to clear it in one pass without reading every item. Triage in slices, summarize as you go, never load the whole desk into context. By the time the agent has scanned a few high-signal slices, it should know what's bulk-approvable and what needs attention.

### Step 1 — Scan high-priority items first

Call `swan-search-user-tasks` filtered to the caller, `status: PENDING`, ordered by priority/recency, **page size ≤ 20**. Read the structural preview the agent gets back — it shows the shape (taskType, companyId, age, priority) for the first 20 items.

For each item in this slice, classify in one pass:

| Bucket | Criteria | Per-item record |
|--------|----------|-----------------|
| **Act today** | High priority, named target account, fresh signal | Title + one-line context |
| **Bulk approve** | Outreach sequence approval, shared template, looks safe | Group key (template + sender) |
| **Acknowledge** | Stale informational alerts, low-priority FYIs | Group key (taskType + age bucket) |
| **Stop / investigate** | Auto-approved sequence with a red flag | Title + the concern |
| **Worth a look** | Open-ended suggestion needing user judgment | Title + impact score 1-5 |

Keep a running tally as a short JSON in your head — one entry per item, max one line per item. Drop the raw task objects after classification.

### Step 2 — Decide whether to keep going

After the first slice of 20:

- If at least 8 items hit "Act today" or "Stop / investigate" → the desk is hot. Stop scanning, report, let the user act. Don't drown them in more items.
- If the slice is mostly "Acknowledge" with very little action → fetch the next page (20 more), same classification pass. Repeat up to ~60 items total.
- If the slice is mostly empty / boring → the desk is in good shape; report briefly and stop.

If the user's desk genuinely has > 100 items and they want everything triaged, switch to code: dump the JSON to a file via `swan-execute-code`, classify in pandas, write per-bucket summaries to stdout. Don't try to do that in tool messages.

### Step 3 — Also check pending sequence approvals

Separately call `swan-search-sequences` with `status: STOPPED_AWAITING_APPROVAL`. Same gradual approach — read the first 20, group by template + sender + signal type. Anything that looks templated and consistent is a bulk-approve candidate. Anything that looks one-off or has a wrong contact / off-message is "Stop / investigate."

### Step 4 — Compose the report

In this exact order, omitting any empty bucket:

1. **Act today** — numbered list, one sentence of context per item.
2. **Bulk approve** — one line per group: "5 sequences using the [template] for [signal] — approve all?"
3. **Acknowledge** — one line per group: "12 website-visit alerts > 30 days old — clear all?"
4. **Stop / investigate** — flagged items with the specific concern.
5. **Worth a look** — top 1-3 open-ended suggestions, with why.

Then one sentence: "Scanned X items. Y action items, Z ready to clear in bulk."

Don't pad with caveats.

### Step 5 — Execute approvals in bulk on confirmation

When the user confirms a bulk action:

- For groups ≥ 5 items, switch to `swan-execute-code` with `output/actions.json`: write one action per item calling `swan-acknowledge-user-task` or the relevant approval mutation. Single batch (max 50 per code call).
- For groups < 5 items, just call the tool directly per item.

After bulk execution, report exactly what was done: "Approved 5 sequences, acknowledged 12 stale alerts, stopped 1 misfired sequence."

### Rules

- NEVER pull the entire desk up front. Always slice → classify → continue.
- NEVER auto-approve. Bulk approve = "approve all?" with a yes/no, not "approving now."
- NEVER bulk-acknowledge items in the "Act today" or "Stop / investigate" buckets.
- MUST report exact counts after execution, not just "done."
- If the desk is empty after the first slice, say so in one sentence and stop. Don't invent work.
- If the response from `swan-search-user-tasks` is truncated, read the full JSON from `files/tool-outputs/swan-search-user-tasks_<callId>.json` in `swan-execute-code` to classify the rest.
