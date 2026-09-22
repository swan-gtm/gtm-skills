---
name: "pre-conference-outreach"
title: "Pre-conference outreach"
description: "Use this skill when you have a conference attendee list and the goal is meetings booked before or during the event, not generic warm-up. Every row is researched first, routed to the teammate whose lens matches the contact's real job, and staged as a tight 4-step sequence: a sub-250-character email that names the conference plus one verified angle, a blank connection request, a verbatim side-door offer (exec dinner or a hands-on session), and a short LinkedIn nudge. Scoring tier never skips anyone. Nothing auto-sends."
category: Events
---

# Pre-conference outreach

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{EVENT_NAME}}` - The conference as people say it in a DM (e.g. "GTM2026", "SaaStr")
- `{{EVENT_CITY}}` - Host city, used to pick "hitting the conf?" vs "Making the trip?"
- `{{EVENT_DATES}}` - Date range, used to pick "this week" vs "next week" at send time
- `{{EXEC_SIDE_EVENT}}` - Your executive side-door offer, as it reads in a sentence (e.g. "an exec dinner on Tuesday night")
- `{{PRACTITIONER_SIDE_EVENT}}` - Your hands-on side-door offer (e.g. "a skills hackathon during the conference", "a build session")
- `{{EXEC_SENDER}}` - Teammate with the authority lens: talks to whoever owns the problem and its budget
- `{{SALES_LEADER_SENDER}}` - Teammate with the seller-management lens: talks to people who manage sellers
- `{{PRACTITIONER_SENDER}}` - Teammate with the practitioner lens: talks to hands-on operators of the GTM stack
- `{{EXEC_SENDER_MIN_ORG_SIZE}}` - Employee count above which {{EXEC_SENDER}} may send (default: 100)
- `{{CRM}}` - Your CRM (e.g. HubSpot, Attio, Salesforce)
- `{{SIGNAL_LIBRARY}}` - Optional: your list of verified third-party angles and how to verify each (funding, hiring, product launches, stack changes)
- `{{ATTENDEE_TAG}}` - The tag or memory line you use to record "this person attended {{EVENT_NAME}}"
- `{{M1_CHAR_CAP}}` - Hard character cap on the first email body (default: 250)
- `{{VOICE_GUIDE}}` - Optional: a sender's voice guide to load when they are the sender

---

### When to use this page

An attendee list for {{EVENT_NAME}} (or an explicit "run pre-conference outreach on these people") needs sequences that drive a **meeting before or during the conference**, plus a side-door CTA: {{EXEC_SIDE_EVENT}} for the exec and sales-leader senders, {{PRACTITIONER_SIDE_EVENT}} for the practitioner sender.

This is a reusable play. Swap the event fill-ins when the next conference is the instance. Sequence **everyone on the file**. Score or scoring tier does **not** route or skip anyone.

**Do not use this play when:**

- They registered for or attended an event and the ask is generic warm-up or post-event follow-up with no side-door CTA. That is a generic event-registrant play (a separate play, not included here).
- The list is booth or badge scans after the conference. That is post-conference outreach.
- You already sat with them at an in-person dinner. That is a dinner follow-up (a separate play, not included here).
- {{CRM}} shows the account is a current customer or closed-won (including alias or sibling domains). Existing-customer hard stop. Do not sequence.

Approval is always queued for a human. There is no auto-send carve-out on this play.

---

### Event fill-ins

| Fill-in | Value |
|---|---|
| `{{EVENT_NAME}}` | e.g. GTM2026 |
| `{{EVENT_CITY}}` | e.g. NYC |
| `{{EVENT_DATES}}` | e.g. September 28 - October 1 |
| `{{EXEC_SIDE_EVENT}}` | e.g. an exec dinner on Tuesday night |
| `{{PRACTITIONER_SIDE_EVENT}}` | e.g. a skills hackathon during the conference |

Phrasing that depends on timing and location is decided at send time, not hardcoded: "this week" vs "next week"; "hitting the conf?" if they are based in {{EVENT_CITY}} vs "Making the trip?" if they are traveling in.

---

### HARD STOP - research every account on the upload, without exception

This is not optional and it is not only a first-party signal scan. Do not draft M1, assign a sender, or stage a sequence for a row until research has run on that domain.

Skipping research because "they're probably cold", "no CRM match", or "it's a list upload" is a failure.

For every row, read **both**:

1. **Account memory** for the company (the contact's domain, plus any alias or sibling domain already on the account).
2. **{{CRM}} activity at the company level**, not just this contact. Pull the company's engagements, notes, meetings, emails, and open or closed deals. Scan every associated contact, not only the person on the list.

**If a prior deal exists (open, closed-won, or closed-lost), research the deal context the way your closed-lost re-engagement procedure does.** Run it. Do not fork the procedure here. At minimum:

- {{CRM}} activity feed on the company **and every associated contact** (emails, meetings, notes, close reason, blockers named)
- Call transcripts if meetings appear
- Whether they ever trialed, how far it got, and any obvious setup gaps
- Capture churn or loss reasons verbatim. The close-reason field is usually a one-line summary that hides the full list.

Closed-won or customer (including alias domains) still hits the existing-customer hard stop: do not sequence.

If research surfaces material history (open deal, booked meeting, live thread, closed-lost with a stated "not now", prior trial, another owner working it), do not pretend the account is cold. Use that history as first-party context in M1 when it is still appropriate to sequence, or **stop and flag** when a standard pre-send gate trips (live unanswered inbound thread, account already engaged, booked meeting, active owner).

Empty memory plus a quiet {{CRM}} feed is still a completed research pass. Then fall through the M1 ladder below. Record what was read in the reasoning log:

`research: [memory + CRM records actually read]; prior deal: none | [deal stage + one-line context]`

If that line is missing, the research did not happen. Do not build.

This is in addition to your standard live-thread and account-engagement gates, not a substitute for them.

---

### Sender and outcome (persona lens, not account tier)

This play **overrides tier-based sender routing**. Sender is the persona owner for the contact's actual role: judgment on the real job, not a fixed title list. Titles vary wildly company to company ("VP GTM Programs", "Global Head of Revenue Strategy, Ops & Enablement", "GTM Systems & Operations" appear on no list and are exactly the right people). One contact, one sender.

Use a verified employee count when available (a LinkedIn-verified count is the preferred source); otherwise the count already on the account record. State the count and the resulting sender in the reasoning log.

| Sender | When | Mandate | Desired outcome |
|---|---|---|---|
| **{{EXEC_SENDER}}** | **Only if org > {{EXEC_SENDER_MIN_ORG_SIZE}} employees** AND the contact owns the problem or the budget (C-level or VP-equivalent who owns GTM systems and tooling decisions) | Authority lens, not hands-on-keyboard | Meeting before or during the conference, and/or {{EXEC_SIDE_EVENT}} |
| **{{SALES_LEADER_SENDER}}** | People who manage sellers (VP or Head of Sales, VP of Sales Development, Head of SDR/BDR; Director of Sales only if no department head). **Also** exec-mandate contacts at **<= {{EXEC_SENDER_MIN_ORG_SIZE}} employees** | Seller-management lens, plus small-org exec fallback | Meeting before or during the conference, and/or {{EXEC_SIDE_EVENT}} |
| **{{PRACTITIONER_SENDER}}** | Hands-on practitioners (GTM engineers, RevOps who run the stack, growth and funnel leads, director-level marketing ops or GTM systems owners). No employee-count gate. | Practitioner lens | Meeting before or during the conference, and/or {{PRACTITIONER_SIDE_EVENT}} |

**Exec size gate (hard):** if employee count is {{EXEC_SENDER_MIN_ORG_SIZE}} or below, do not assign {{EXEC_SENDER}} even when the title is CRO, CMO, CEO, or VP RevOps. Route that contact to {{SALES_LEADER_SENDER}} and keep the exec side-door CTA (Scenario 1). If the count is unknown after a reasonable lookup, do not default to {{EXEC_SENDER}}. Use {{SALES_LEADER_SENDER}} and note the unknown count.

Hard exclusions:

- **{{PRACTITIONER_SENDER}} never connects with salespeople or sales managers.** AE, SDR/BDR, Account Executive, Sales Manager, Sales Director, Head of Sales, VP Sales, or any equivalent quota-carrying or seller-management title goes to {{SALES_LEADER_SENDER}} (Scenario 1).
- Prefer director-level operators over manager-level RevOps for {{PRACTITIONER_SENDER}}.
- Prefer VP or Head over Director of Sales for {{SALES_LEADER_SENDER}}.

If the upload already names a sender, still verify the mandate **and** the exec size gate; reassign if either fails.

If a row has no resolvable LinkedIn URL, skip the LinkedIn steps and flag the row. Do not invent a URL. If there is no work email after enrichment, fall back to LinkedIn-only rather than emailing a personal inbox.

Load {{VOICE_GUIDE}} when it exists for the chosen sender.

---

### Two scenarios, same 4-step shape

**Scenario 1 - Meetings + exec side event** ({{EXEC_SENDER}} when over the size gate, otherwise {{SALES_LEADER_SENDER}})

**Scenario 2 - Meetings + practitioner side event** ({{PRACTITIONER_SENDER}}). M1 can still ask for a meeting. **M2 is the only structural change.**

| Step | Timing | Channel | Content |
|---|---|---|---|
| 1 / M1 | Day 0 | Email | Conference attendance is the primary hook, tied to a researched angle. Ask for a meeting. **Max {{M1_CHAR_CAP}} characters.** |
| 2 | Immediate (same day as M1) | LinkedIn connection request | Blank. No note. Auto-skips if already connected. |
| 3 / M2 | Day 3 | Email | Side-door offer. Verbatim. **No name in the message.** |
| 4 / M3 | After M2 (next LinkedIn touch) | LinkedIn DM | Verbatim. **No name in the message.** |

---

### Scenario 1 - Meetings + exec side event

**Who:** {{EXEC_SENDER}} (over the size gate + authority-lens contact) or {{SALES_LEADER_SENDER}} (seller-management lens, or exec-mandate at or under the gate).

**M1:** researched email per the ladder below. Meeting ask.

**Step 2:** blank connection request.

**M2 - email, Day 3, verbatim (no name):**

```
We're also hosting {{EXEC_SIDE_EVENT}} if that's preferable - can shoot over the reg link if interested. Lmk!
```

Do not paste the registration link in the email. Offer to send it.

**M3 - LinkedIn DM, verbatim (no name):**

```
tried you on email - in town for {{EVENT_NAME}} this week?
```

Adjust "this week" / "next week" to the actual timing of the send vs the conference. Do not add a name.

---

### Scenario 2 - Meetings + practitioner side event

**Who:** {{PRACTITIONER_SENDER}}. The angle should be relevant to technical personas (GTM engineers, RevOps, marketing ops, GTM systems, as examples). Do not use a seller-management angle on this path.

**M1:** researched email per the ladder below. Meeting ask is still allowed.

**Step 2:** blank connection request. {{PRACTITIONER_SENDER}} never connects with salespeople or sales managers, so those contacts should not be on this scenario.

**M2 - email, Day 3, verbatim (no name):**

```
We're also running {{PRACTITIONER_SIDE_EVENT}} if that's more your speed - can shoot over the details if interested. Lmk!
```

Do not paste the side-event link in the email. Offer to send details.

**M3 - LinkedIn DM, verbatim (no name), same as Scenario 1:**

```
tried you on email - in town for {{EVENT_NAME}} this week?
```

---

### M1 - research ladder and copy

Conference attendance is the primary signal and **may be named**: it is a public, intentional act, the same logic that lets you name an event registration or a profile view. After the mandatory account research, pick the secondary angle with this ladder. **Stop at the first that survives.**

1. **First-party.** Material engagement found in the research: LinkedIn content engagement, website visits, prior replies, closed-lost or prior-deal context, {{CRM}} activity. If it exists, that is the secondary angle. Do not also weave in a third-party observation.
2. **Else third-party.** Load {{SIGNAL_LIBRARY}}. Run its verification protocol. Pick **one** verified angle and tie it to conference attendance. Role-to-angle mapping still applies. Scenario 2 uses technical angles only.
3. **Else conference-only.** Attendance plus a meeting ask. No invented signal.

Never mention that you pulled them from a registration or attendee list. Never dump product in M1.

**Hard cap: {{M1_CHAR_CAP}} characters** on the M1 email body (count the full message, including the name if used). If a draft exceeds the cap, cut before staging. Do not keep both a long observation and a long ask. Conference + one angle + one meeting ask is the whole message. Record the character count in the reasoning log.

M1 **is allowed** to ask for time ("How's your sched looking?", "Making the trip?"). This play is **exempt** from your cold-outreach no-mention, no-pitch, no-CTA rules. A persona-matched pitch check is not applicable on this short cadence: there is no pitch step.

**Angle examples (reference only. Write fresh, stay under the cap):**

First-party (LinkedIn engagement):

> You've been engaging a lot with our content on LinkedIn. Given we're both in {{EVENT_CITY}} this week for {{EVENT_NAME}}, thought it might be a great time to connect. How's your sched looking?

Third-party (GTM scale-up):

> Noticed you guys are in rapid GTM scale-up mode. So given we're both in {{EVENT_CITY}} this week for {{EVENT_NAME}}, thought it might be a great opportunity to connect re how AI agents are supporting the scale-up efforts. How's your sched looking?

Third-party (the prospect deploys AI in their own product). Traveling in:

> Given the focus on deploying AI agents into call centers, was curious if agents are also driving your own GTM motion. Happy to chat on it live if you're at {{EVENT_NAME}} next week. Making the trip?

Local variant of the close: `hitting the conf?`

---

### List-upload execution

- Sequence every row on the file unless a standard gate trips (customer, live thread, booked meeting, account already engaged, already-engaged owner).
- **Research every row first.** No exceptions.
- Check existing sequences per contact; read the full message history; edit, don't duplicate.
- Blank connection requests (no note). Plain-text URLs. No unfilled merge fields left in copy. No markdown-wrapped links.
- Stage queued for approval. Confirm: "Drafted a 4-step pre-conference sequence for [contact] at [company], staged for your approval. Sender: [name]. Hook: [one line]. Scenario: exec side event / practitioner side event."
- **After staging:** write the person-level attendee line to account memory and apply {{ATTENDEE_TAG}} on the company. Write it for every sequenced row **and** for connection-only rows. Do not duplicate an existing person+event line.

The reasoning log on every sequence must include:

- Sender mandate + why (quote the role, not just the title)
- Employee count + exec size gate verdict
- `research:` + `prior deal:` line (see HARD STOP)
- First-party vs third-party vs conference-only, and what was used
- Scenario 1 vs 2
- Event instance
- M1 character count
- A compact pre-flight line citing this play's sender override, not tier routing

---

### Rules

- MUST research every account on the upload before drafting or staging. No exceptions.
- MUST run your closed-lost research procedure when a prior deal exists. Do not invent deal context.
- MUST assign sender from the persona mandate + exec size gate. Do not use tier routing.
- MUST keep M1 <= {{M1_CHAR_CAP}} characters.
- MUST use Scenario 1 (exec side event) for {{EXEC_SENDER}} and {{SALES_LEADER_SENDER}}, and Scenario 2 (practitioner side event) for {{PRACTITIONER_SENDER}}. Do not mix CTAs.
- MUST leave M2 and M3 verbatim and nameless (aside from this-week / next-week timing on M3).
- MUST NOT paste side-event registration links into M2. Offer to send them.
- MUST NOT mention the attendee list as the source.
- NEVER auto-send on this play.
- NEVER sequence a closed-won or customer account.
- MUST, after staging, write the attendee line to account memory and apply {{ATTENDEE_TAG}} on the company. One line per person per event.

---

## What good looks like

Every row on the file has a research line before it has a draft. Sender was chosen by what the person actually does, and the exec size gate was applied even when the title said CRO. M1 reads like a 30-second note from someone who is also going to be in the room: the conference, one real angle, one ask for time, under the cap. M2 and M3 are word-for-word the verbatim lines, with no name added and no link pasted. Everything sits queued for approval with a reasoning log a colleague could audit.

Spot first: a row with no research line, an account under the size gate assigned to the exec sender, a salesperson routed to the practitioner sender, and an M1 over the cap.

Mediocre looks like: "saw you're attending, want to meet?" sent to everyone with no angle; a pitch paragraph in M1; a dinner link dropped in M2; a hackathon offer sent to a VP Sales; or a closed-lost account sequenced as if it were cold because nobody opened the deal history.
