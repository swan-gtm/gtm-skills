---
name: "inbox-zero"
title: Inbox zero
description: "Triage a user inbox across email, Slack, LinkedIn, and Swan. Use for inbox sweeps where the agent should archive obvious noise, draft replies, and return a single summary of items needing attention."
category: RevOps
---

## The four-bucket model

For each item the agent encounters, exactly one of these:

| Bucket | When | What the user sees |
|---|---|---|
| **1. Auto-archive** | Obvious noise (newsletters, mass mailers, status alerts), items already handled by someone else, items needing no action | One-line FYI in the batched summary, always with a reason |
| **2. Auto-handle** | The agent can fully complete the work itself — mark a CRM task done, schedule a follow-up reminder, archive after the other side already replied | One-line FYI in the batched summary |
| **3. Draft → approve** | A reply is needed | Reviewed one by one in the batched output |
| **4. Park** | Ambiguous, or the user's judgment is required | Left in inbox with a one-line reason |

## Steps

1. **Sweep all connected surfaces.** Pull unread / unactioned items from email, Slack DMs, LinkedIn DMs, the Swan inbox, and the CRM task queue. Count them. If above ~30, switch to `swan-execute-code` — load the inbox snapshot into a frame and process in passes.

2. **Classify silently into the four buckets.** For each item:
   - Read the message.
   - **Investigate first when facts are needed** — check the CRM for prior touches and the account record, check the subscription, search product documentation, pull recent Slack threads where the customer was discussed. If the question is about a bug, product behavior, or code-level issue, route to the org's internal investigation/auditor agent when one is available (these typically have access to logs and the codebase; that context lands in the draft).
   - Decide the bucket. When uncertain → park, don't auto-archive.

3. **Execute autonomous actions.** Archive bucket 1, complete bucket 2. Keep a running tally of WHY each was actioned, so the FYI summary is specific ("David replied he's on it"), not generic ("archived 14").

4. **Draft replies for bucket 3.** Substantive, in the sender's voice (load the sender instructions and pull past approved messages first), citing the facts gathered in Step 2. Use `swan-build-sequence` when the reply belongs to an existing outreach thread; otherwise draft via the appropriate sending tool for the surface.

5. **Present the batched output.** In this order:
   - **FYIs first** — auto-archived + auto-handled, each with the reason in one line.
   - **Drafts second** — numbered, each with a 1-2 line context above the draft body. Compress to what the user needs to decide.
   - **Parked last** — each with a one-line reason for why it stayed.
   Then wait. The user responds with decisions in one shot — "send 1, edit 2 to add X, skip 3, leave parked alone."

6. **Execute the user's decisions.** Send approved drafts, apply edits, archive skips. Report exact counts: "Sent 2 drafts, archived 1, 2 parked items left for you."

## What good looks like

The best inbox-zero pass touches the user exactly once. The user reads the FYI summary, scans the drafts, approves most, edits one, leaves the parked items alone. The inbox is empty or contains only items the user consciously kept.

- **Catches attention first** — the substantive ask buried in a thread that *looks* archivable. The "thanks!" email with a feature request in paragraph 4. The churn signal mentioned in passing.
- **Gets overlooked** — the "I'm on it" reply from a teammate that means the customer email is already handled. A trial-extension ask hidden inside a long account update.
- **The trap** — narrating every archive ("I'm about to archive 14 newsletters…"). The user doesn't need ceremony around obvious decisions. Confirming archives is a form of asking permission for work the agent should own.
- **Failure modes** — drafting generic "thanks, will look into it" replies (do the investigation first); investigating items that didn't need it (stalls the flow); auto-archiving when ambiguous (park instead); dumping the customer's full history in the context line (compress to what the user needs to decide); presenting drafts one-by-one with interstitial confirmations (single batched output is the contract).
- **Success** — every draft reads like the agent did the homework. Subscription details cited, bug status confirmed, prior conversation referenced. The user hits send without rewriting.

## Rules

- **MUST** process every item. Surface only via the single batched output.
- **MUST** investigate before drafting when the reply needs facts — check the CRM, search the docs, route to the internal investigation/auditor agents when available, pull prior Slack threads.
- **MUST** explain WHY in every auto-archive and auto-handle FYI. Generic counts are a failure.
- **MUST** park (not auto-archive) when uncertain. State the reason.
- **NEVER** auto-send a draft. User approval is the gate.
- **NEVER** ask the user to confirm obvious-noise archives. Do them and report.
- **NEVER** present a draft without investigation when facts are needed. A "thanks, will look into it" reply is a failure.
