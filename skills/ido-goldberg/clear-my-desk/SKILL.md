---
name: "clear-my-desk"
title: Clear my desk
description: "Triages pending Swan work for a user. Use to prioritize review items, sequence approvals, alerts, and suggestions into act-now, bulk-approve, acknowledge, or investigate buckets."
category: RevOps
---

## Instructions

**State check.** This skill assumes the caller is the user whose desk is being cleared, and that Swan has work waiting for people: at least one automation that asks a person to approve, decide, answer or act. Start by looking up what is open and waits for the caller. If nothing is open and nothing was ever raised for them, the desk is empty because no automation is producing work yet, not because the user is on top of it — tell the user and recommend setting up an automation before this skill becomes useful.

### What this skill does

The user has a backlog and wants to clear it in one pass without reading every item. Triage in slices, summarize as you go, never load the whole desk into context. By the time you have scanned a few slices, you should know what can be settled in bulk and what needs attention.

### Step 1 — Scan what waits for the user

Look up the open items that wait for the caller, **at most 20 at a time**. Take first the ones that are due soonest or already overdue, then the newest. Leave out the items the user put off until later, unless they ask for them. Read only what you need to classify an item: what it asks of the user, which account it is about, how old it is and when it is due.

For each item in this slice, classify in one pass:

| Bucket | Criteria | Per-item record |
|--------|----------|-----------------|
| **Act today** | Due today or overdue, named target account, fresh signal | Title + one-line context |
| **Bulk approve** | Asks only to approve outreach or one repeated action, shared template, looks safe | Group key (what is approved + sender) |
| **Close** | Out of date, a duplicate, or about something that already happened | Group key (what it is about + age bucket) |
| **Stop / investigate** | Something already went out or was approved and has a red flag | Title + the concern |
| **Worth a look** | Open-ended question needing user judgment | Title + impact score 1-5 |

Keep a running tally as a short JSON in your head — one entry per item, max one line per item. Drop the raw items after classification.

### Step 2 — Decide whether to keep going

After the first slice of 20:

- If at least 8 items hit "Act today" or "Stop / investigate" → the desk is hot. Stop scanning, report, let the user act. Don't drown them in more items.
- If the slice is mostly "Close" with very little action → fetch the next 20, same classification pass. Repeat up to ~60 items total.
- If the slice is mostly empty / boring → the desk is in good shape; report briefly and stop.

If more than 100 items genuinely wait for the user and they want everything triaged, switch to code: save the list to a file, classify it there, and print one summary per bucket. Don't try to do that in tool messages.

### Step 3 — Also check sequences awaiting approval

Separately look up the sequences that wait for the user's approval. Same gradual approach — read the first 20, group by template + sender + signal type. Anything that looks templated and consistent is a bulk-approve candidate. Anything that looks one-off or has a wrong contact / off-message is "Stop / investigate." A sequence that already belongs to an item from step 1 counts once, with that item.

### Step 4 — Compose the report

In this exact order, omitting any empty bucket:

1. **Act today** — numbered list, one sentence of context per item.
2. **Bulk approve** — one line per group: "5 sequences using the [template] for [signal] — approve all?"
3. **Close** — one line per group: "12 website-visit alerts > 30 days old — close all?"
4. **Stop / investigate** — flagged items with the specific concern.
5. **Worth a look** — top 1-3 open-ended suggestions, with why.

Then one sentence: "Scanned X items. Y action items, Z ready to clear in bulk."

Don't pad with caveats.

### Step 5 — Carry out the decisions on confirmation

When the user confirms a group, settle each item in it the way the decision calls for:

- Approve or reject what waits for approval.
- Give the user's answer when the automation that raised the item should continue with it.
- Close the item when nothing should happen next. Say first what its automation will then not do.

For groups ≥ 5 items, do it in batches of at most 50 instead of one item at a time.

After bulk execution, report exactly what was done: "Approved 5 sequences, closed 12 stale alerts, stopped 1 misfired sequence."

### Rules

- NEVER pull the entire desk up front. Always slice → classify → continue.
- NEVER approve or close on your own. Bulk approve = "approve all?" with a yes/no, not "approving now."
- NEVER bulk-close items in the "Act today" or "Stop / investigate" buckets.
- MUST report exact counts after execution, not just "done."
- If nothing waits for the user after the first slice, say so in one sentence and stop. Don't invent work.
- If a lookup result is cut short, read the full result from the file it was saved to and classify the rest there.
