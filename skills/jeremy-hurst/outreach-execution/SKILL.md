---
name: "outreach-execution"
title: Outreach execution
description: "Use this skill when a signal, account list, or named contact needs outreach — it loads sender voice and past approved messages, picks the right path for the situation, and drafts a multi-step sequence anchored on a real hook. It encodes production sender-assignment and approval rails: tiered senders, automatic executive multi-threading on large accounts, and a hard rule that AI-drafted sequences to senior executives are never auto-sent. Every sequence is staged with a written rationale for human approval, and approved copy feeds back into the voice library. Includes references for email/LinkedIn/breakup frameworks and objection handling."
category: Outreach
---

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{CRM}}` — Your CRM (e.g. HubSpot, Attio, Salesforce)
- `{{SENDER_ROSTER}}` — The people who can send outreach, with which channels each has connected (email, LinkedIn)
- `{{AWARENESS_SENDER}}` — Senior exec (usually a founder or CxO) who runs the no-pitch awareness touch to decision makers
- `{{HIGH_TIER_SENDER}}` — Primary sequence sender for your top account tiers (usually your most senior GTM seller)
- `{{LOW_TIER_SENDER}}` — Primary sequence sender for your lower account tiers
- `{{TIER_MODEL}}` — Your account tiering scheme and which tiers count as "high" vs "low" (e.g. Gold/Diamond = high, Silver/Bronze = low)
- `{{APPROVAL_OWNER}}` — The human who reviews and approves staged sequences before anything sends
- `{{MULTITHREAD_THRESHOLD}}` — Company size above which an executive multi-thread must run in parallel with the primary sequence (default: >200 employees)
- `{{LARGE_COMPANY_THRESHOLD}}` — Company size above which executives are never auto-contacted without approval (default: 100+ employees)
- `{{VOICE_SOURCE}}` — Where sender voice lives: saved voice guides, past approved messages, or both
- `{{RESOURCE_LIBRARY}}` — Single source of truth for shareable URLs: booking links, demo video, trust/security docs, one-pagers
- `{{AUTO_APPROVE_CARVEOUT}}` — The one narrow scenario (if any) where a sequence may send without human approval (default: none — everything is approved)

---

### What this skill produces

A staged outreach sequence — queued for approval, never sent — for the right contact(s), with sender, sequence steps, and a written outreach rationale attached. {{APPROVAL_OWNER}} reviews, edits if needed, and approves before anything goes out.

When the user asks about outreach strategically ("how should our cold emails sound," "what is the right cadence shape"), the output is a point of view anchored in {{VOICE_SOURCE}} and past approved messages — not a sequence.

---

### Step 1 — Load voice and sender context

Never draft from a blank page. Before writing a single line of copy:

1. Load {{VOICE_SOURCE}} for the chosen sender. If the sender has a personal voice guide, it governs every message written on their behalf — greeting format, tone, sign-off, formatting quirks.
2. Pull past approved messages for the same play, persona, or channel. Approved copy is the ground truth for what this org actually sounds like.
3. Confirm the sender has the needed channels connected ({{SENDER_ROSTER}}). No LinkedIn-enabled sender means no LinkedIn steps — stop and tell the user rather than improvising.

Never copy voice from another org, another sender, or generic "best practice" cold email templates. Voice is per-sender and earned from approved examples.

---

### Step 2 — Choose the outreach path

Match the situation to the working path before drafting:

| Situation | Path |
|---|---|
| Setup or voice questions | Voice/setup review — no sequence output |
| Named company, named contact, or small account list | Targeted flow (Step 6 onward, one contact per account by default) |
| LinkedIn-only audience (no work email, or LinkedIn-native brand) | LinkedIn-only cadence — see frameworks reference |
| Email-only audience | Email cadence — see frameworks reference |
| Final touch / close-the-loop | Breakup patterns — see frameworks reference |
| Mixed email + LinkedIn | Multichannel cadence (default when both channels are available) |
| Prospect raised an objection or blocker | Objection handling reference — reply, not sequence |
| Pre-conversion signal (visit, intent, hiring, funding) | Run the prior-relationship check (Step 5) first, then route |
| Executive threading needed on a live deal | Peer-to-peer exec outreach from {{AWARENESS_SENDER}}, drafted for their voice |

**Scenario always wins over channel.** When a lifecycle scenario governs the outreach (a hand-raiser, an active trial, a closed-lost re-engagement, a post-meeting follow-up), that scenario's content rules govern every step in the sequence — email, LinkedIn, everything. Channel mechanics (email frameworks, LinkedIn DM structure) only govern when no scenario applies, i.e. a pure cold play. If a scenario rule and a channel rule conflict, the scenario wins without exception.

---

### Step 3 — Sender assignment

Three stages, three jobs. One source of truth — never improvise sender choice per sequence.

**Stage 1 — Initial signal, unknown person (any tier).**
{{AWARENESS_SENDER}} sends a blank LinkedIn connection request to the decision maker, followed by one casual follow-up DM. Goal: get them into the exec's orbit so they see their content and build brand familiarity. No pitch. No product mention. Persona targets: C-level and VP-level.

**Stage 2 — Specific person identified, primary sequence.**
Sender is determined by account tier per {{TIER_MODEL}}:

| Tier | Primary sequence sender |
|---|---|
| High tiers | {{HIGH_TIER_SENDER}} |
| Low tiers | {{LOW_TIER_SENDER}} |

The high-tier sender never sends primary sequences to low-tier accounts, and vice versa. Tier discipline protects the senior sender's reply rates and calendar.

**Stage 3 — Multi-threading.**
{{AWARENESS_SENDER}} is the multi-threading sender for executive-level contacts (C-level, VP-level) at any account.

**Rule: any account above {{MULTITHREAD_THRESHOLD}} MUST have an executive multi-thread from {{AWARENESS_SENDER}} running in parallel alongside the primary sequence.** This fires automatically whenever a primary sequence is created for an account above the threshold. Multi-threading sequences always require {{APPROVAL_OWNER}}'s approval — no exceptions, including when triggered by a signup or trial event.

---

### Step 4 — Approval policy

---

# ⛔ HARD RULE — NO EXCEPTIONS ⛔

## **AI-GENERATED SEQUENCES TO SENIOR EXECUTIVES AT LARGE COMPANIES ARE NEVER AUTO-APPROVED. NEVER. FULL STOP.**

**"Senior executive" = any C-level, VP-level, Head of, or Director-level contact.**
**"Large company" = any company above {{LARGE_COMPANY_THRESHOLD}}.**

**Auto-send is FORBIDDEN for these sequences regardless of:**
- What trigger fired
- What scenario applies
- Whether it's LinkedIn-only
- Whether it's a connection-request-only step
- Whether it's multi-threading
- Whether it was built as part of an automated trial or signup flow

**IF IN DOUBT: queue for approval. ALWAYS.**

---

**High-tier accounts.** All sequences require {{APPROVAL_OWNER}}'s approval before sending, with at most one narrow carveout defined in {{AUTO_APPROVE_CARVEOUT}}. If you define one, keep it this tight:

1. The contact is the **signed-up user themselves** (the person who converted)
2. Triggered by a product lifecycle event (signup or trial start)
3. The sequence has **no more than 4 steps total**
4. The contact is **NOT a senior executive at a large company** (hard rule above)

If any one condition is not met → queue for approval.

**Always requires approval — no exceptions:** all multi-threading sequences; all sequences to executive stakeholders at any company size; all sequences where {{HIGH_TIER_SENDER}} is the sender unless covered by the carveout; anything not explicitly listed in the carveout.

**Low-tier accounts.** May send automatically if your org allows it — except when the contact is a senior executive at a large company, in which case approval is still required.

---

### Step 5 — Prior-relationship check (before any pre-conversion play)

Before running any cold or signal-triggered play, check whether a prior relationship exists.

**Check:** account notes and memory, {{CRM}} contacts (past meetings, calls, emails, notes), {{CRM}} deals (open or closed-lost), and meeting transcripts if you record calls.

**What counts as a prior relationship:**
- Any past meeting (attended or no-show)
- Any outreach that received a reply (even a negative one)
- Any direct DM exchange on LinkedIn or email
- A closed-lost deal at any stage

**What does NOT count:**
- Sequences sent with no reply
- Connection requests not accepted
- Anonymous website visits
- Being in {{CRM}} with no engagement history

**Route:** prior relationship → warm re-engagement framing (acknowledge the history, never pretend it's a cold intro). No prior relationship → cold play.

> Prior relationships always take precedence. A closed-lost account returning to your pricing page is a re-engagement, not a cold website-visitor play.

---

### Step 6 — Anchor on the hook

Every outreach starts from a hook. No hook, no send.

- **Signal-based:** funding, hiring, leadership move, product launch, intent spike, website visit, event attendance, LinkedIn engagement
- **Relationship-based:** champion move, past customer, referral, prior touch
- **Audience-based:** named ICP fit, cohort membership, list inclusion

If the hook is generic ("drum up pipeline," "stay top of mind"), push back and ask for the slice with a real reason.

**Signal rule: never mention the signal directly.** Use signals to inform the angle — reference their role, company context, or challenges aligned with the signal. "Saw you visited our pricing page" is surveillance; "teams at your stage usually hit X" is insight. Keep it subtle.

---

### Step 7 — Cadence shape

Default (scenario pages and saved voice can override):

- 3–5 steps total
- Days 0, 2, 5, 9, 14 as the starting rhythm for single-channel sequences (the multichannel table below has its own rhythm)
- Each follow-up brings a new angle. "Just checking in" is not a step.
- Last touch is a soft breakup — load the frameworks reference for the three patterns.
- Single-channel by default unless the org's saved motion calls for multichannel.

Default multichannel structure for a targeted play:

| Step | Day | Channel | Purpose |
|------|-----|---------|---------|
| 1 | 0 | LinkedIn connection request | Open the channel — no note |
| 2 | 1 | Email | Cold intro — hook + proof + one-line ask |
| 3 | 4 | LinkedIn DM | Different angle |
| 4 | 8 | Email | New asset or new framing — never "just checking in" |
| 5 | 14 | Email | Soft breakup — leave the door open |

**LinkedIn-active contacts default to LinkedIn-only.** If a contact has 10,000+ followers or is visibly highly active on LinkedIn (frequent posting, high engagement), default to a LinkedIn-only sequence. Don't add email steps unless the user explicitly asks.

---

### Step 8 — Build and stage for approval

For a targeted play, in order:

1. **Confirm target and intent.** Company, why-now, channel preference, contact count (default: one contact per account unless the user asked for multi-threading — don't fan out by default).
2. **Research only as much as the outreach needs.** Check your workspace and {{CRM}} first; enrich only if essential data is missing; web-research only if a fresh hook is needed. Capture: one sentence on what they do, the signal that justifies the timing, one fact that proves the research is real.
3. **Find the right contact.** Persona match against your buying-committee definitions, active at the company. Email steps need a verified email; LinkedIn steps need a LinkedIn URL. Find the data first or drop that channel — never guess.
4. **Check for duplicates.** Search existing sequences for this contact before drafting. Same play with an unsent draft → edit it instead of creating a new one. Stale different play → archive it, then create. Multiple active sequences → stop and ask the user. Never create a duplicate.
5. **Build the sequence and queue it for approval.** Attach: the contact, the chosen sender, the steps, and a written **outreach rationale** — one paragraph covering who, why, what hook, and what the approver should know. Default to manual approval per Step 4. Follow-up emails get a blank subject so they thread as replies.
6. **Confirm to the user:** "Drafted a [N]-step sequence for [contact] at [company], staged for your approval. Hook: [one line]."
7. **After approval and send,** save the approved version as a message example in {{VOICE_SOURCE}}. Approved copy feeds future drafts for the same play and persona. Never save unapproved drafts.

---

### Hard rules

- **Scenario always wins over channel** (Step 2). No exceptions.
- MUST load sender voice and message examples before drafting copy. Never guess voice.
- MUST anchor every draft in a hook. If the user cannot say "why now," push back before drafting.
- MUST run the prior-relationship check before any pre-conversion play (Step 5).
- MUST check for existing unsent sequences before creating a new one.
- MUST attach a written outreach rationale to every staged sequence.
- MUST run the {{MULTITHREAD_THRESHOLD}} executive multi-thread check on every new primary sequence.
- NEVER auto-send outside the explicit {{AUTO_APPROVE_CARVEOUT}} — and never to senior executives at large companies, period.
- NEVER include attachments. Use links from {{RESOURCE_LIBRARY}} if a resource is needed.
- **LinkedIn connection requests are ALWAYS blank.** No message text, no connection note. No exceptions, across any sequence type, sender, or scenario. No-note requests accept at meaningfully higher rates.
- NEVER wrap links in markdown syntax in outreach copy. Outreach channels don't render markdown — a markdown-wrapped link renders as duplicated text. Always plain-text URLs.
- NEVER create a sequence without the contact's email (for email steps) or LinkedIn URL (for LinkedIn steps).
- NEVER hardcode URLs in this skill. {{RESOURCE_LIBRARY}} is the single source of truth for booking links, demo videos, and trust/security docs. A final leave-behind step may casually offer one or two of these ("will leave two things for if/when relevant") — use judgment on which fit the scenario.
- NEVER copy voice from another org.

---

## What good looks like

A great run produces one staged sequence per target with a hook the approver instantly recognizes as real: the rationale paragraph says who, why, and why-now in three sentences; the copy sounds unmistakably like the sender because it was drafted from their voice guide and past approved messages, not a template; the prior-relationship check caught the closed-lost history so the opener acknowledges it instead of pretending to be cold; the {{MULTITHREAD_THRESHOLD}} check quietly spawned the parallel executive thread and queued it for approval; connection requests went out blank; every follow-up carries a new angle and the last touch is a clean 25–50-word breakup; and nothing — nothing — reached a senior executive at a large company without a human clicking approve.

Mediocre looks like: sequences with "staying top of mind" as the hook, "just checking in" follow-ups, a signal quoted back at the prospect ("saw you visited our site"), connection-request notes, markdown-wrapped calendar links rendering as duplicated text, duplicate sequences stacked on one contact, voice guessed from generic cold-email lore, or an auto-sent sequence to a VP because a trial trigger fired. Every one of those is a rule in this skill being ignored.
