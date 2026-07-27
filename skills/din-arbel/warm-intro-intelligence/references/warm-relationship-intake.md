---
title: Warm Relationship Intake
description: Reference for the Warm intro intelligence skill.
---

# Warm Relationship Intake

Sub-page of the Warm Intro Intelligence skill. Load when executing Step 8 - checking whether intake should be triggered.

---

## Purpose

Captures relationship signals that automated sources cannot find - relationships your team members know personally but that don't appear in the CRM or LinkedIn in any meaningful way.

Principle: infer first, confirm second. The agent identifies probable relationships from automated sources. Human input is requested only to validate or add what automation cannot reach.

---

## V1 Triggering Rules

### Trigger 1 - On-Demand Confirmation (fires during the play)

When to fire: The play finds an Inferred edge involving one of your employees, AND that employee is the same rep who initiated the play.

When NOT to fire:
- The edge is already Moderate or Verified.
- A confirmation or rejection for this bridge-target-contact pair already exists in memory.
- The Inferred edge involves an employee other than the rep who initiated the play.

Action: Send a single Slack DM to the rep who initiated the play. Intake never messages anyone else - not other employees, not customers, not the prospect.

Message format:
---
"I found a possible connection while mapping warm intro paths for [Prospect Company].

[One-line evidence: e.g. 'You worked at [Company] during overlapping years' or 'You're 2nd-degree connected on LinkedIn with [Target Contact Name], [Role].']

Is there anyone at [Prospect] you'd feel comfortable reaching out to, or asking for an intro to their [Target Persona]?

- Yes, know them personally - I could make an intro
- Yes, I have someone who could intro us
- No"
---

Rules:
- One message per bridge-target-contact pair. Never re-send after a response is received.
- If the rep does not respond within the session: treat the edge as Inferred (unchanged). Do not follow up.
- After a response: update the edge confidence and store the intake flag per the schema below.

Response mapping:
- "Yes, know them personally" -> upgrade edge to Verified. Set intro_willingness: "strong".
- "Yes, I have someone who could intro us" -> upgrade edge to Moderate. Set intro_willingness: "possible".
- "No" -> soft-delete: set intro_willingness: "unlikely". Do not re-prompt this pair. Edge remains Inferred from original signal source.

### Trigger 2 - Gap-Triggered Prompt (fires in the output card only - no Slack)

When to fire: The play returns zero paths above Low confidence across all target contacts.

Action: Add the following block to the output card, immediately before the decision prompt:

---
"No verified or moderate warm path found to [Prospect Company].

If you have a personal relationship with anyone at this company or in their network that the system may not know about, sharing it could help surface a stronger path."
---

No Slack message. No follow-up. The rep decides whether to share anything.

---

## Storage Schema Per Intake Flag

Store in account memory under the prospect company domain. Each flag is a structured record:

- internal_contact_name: string
- internal_contact_email: string
- external_contact_name: string
- external_contact_company: string
- external_contact_role: string
- external_contact_linkedin: string or null
- relationship_type: personal | former_colleague | investor | advisor | other
- intro_willingness: strong | possible | unlikely | unknown
- context: free text from rep - optional
- source: intake | inferred | inferred+confirmed
- date_logged: ISO timestamp
- expires: 180 days from date_logged
- confirmed_by: rep name if confirmed via Slack prompt, otherwise null

---

## Expiry and Stale Flag Handling

Intake flags expire 180 days after logging.

On expiry:
- Mark the flag as stale but do not delete it.
- In any output card that uses this flag as evidence, add the label: "Last confirmed [date] - may be stale."
- Re-confirmation via weekly digest is deferred to V2. In V1, stale flags surface with the stale label and the rep judges whether to act.

---

## Rejected Flags

If a rep responds "No / don't know them well":
- Soft-delete: set intro_willingness to "unlikely" and record the rejection date.
- Never re-prompt the same rep about the same external contact.
- The original Inferred edge from the automated signal source remains in the output - it is not removed. The rejection only means this rep cannot confirm it; another bridge node may still have a real relationship.

---

## What Intake Does NOT Do

- Does not send Slack messages to anyone other than the rep who initiated the play.
- Does not contact customers, partners, investors, advisors, or prospect contacts.
- Does not auto-run the intake process outside of the warm intro play (weekly digest is V2).
- Does not upgrade an edge to Verified based on an unconfirmed flag alone.
