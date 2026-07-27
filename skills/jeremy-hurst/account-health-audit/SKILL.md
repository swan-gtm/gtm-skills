---
name: "account-health-audit"
title: Account health audit
description: "Use this skill when you need an on-demand health check of a trial or customer account — before a renewal conversation, when adoption looks shaky, or when a champion goes quiet. It audits five lanes from real data: what the account is actually solving for, lead scoring and qualification integrity, alerting coverage, messaging architecture, and user adoption trends. The output is a tight, evidence-only report with hard numbers on every gap and a concrete intervention mapped to every flag — no hedging, no filler. Built for vendors whose product runs their customers' GTM workflows: the audit reads the account's scoring, sequencing, and messaging configuration inside your own platform."
category: Deals
---

# Account Health Audit

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{USAGE_DATA_SOURCE}}` — Where your product's usage/engagement data lives (analytics, admin console)
- `{{CRM}}` — Your CRM (e.g. HubSpot, Attio, Salesforce)
- `{{CALL_LIBRARY}}` — Your call recording/transcript tool (e.g. Gong, Grain, Fireflies)
- `{{TIER_LABELS}}` — Your lead-scoring tier names (default: Bronze / Silver / Gold / Diamond)
- `{{ALERT_DESTINATIONS}}` — Where qualified-account alerts route (Slack channels, task queues, inboxes)
- `{{SCORING_WORKFLOW}}` — The audited account's central lead scoring & qualification workflow (theirs, configured in your platform — not your own org's)
- `{{VOICE_GOVERNANCE}}` — The single place where outreach voice, tone, and CTA rules are supposed to be defined
- `{{STALE_DAYS}}` — Days of zero activity before an automation counts as dead (default: 5)
- `{{LOOKBACK_DAYS}}` — Window for usage/spend analysis (default: 30)

---

### Overview

Run this on demand for any trial or customer account. It produces a signal-dense health check across five lanes — use-case fit, lead scoring, alerting, messaging, and user adoption — closing with a prognosis and concrete interventions. No filler. No guesses.

---

### Step 1 — Gather data (all in parallel, before writing anything)

Pull the following before producing a single section:

- **{{USAGE_DATA_SOURCE}}:** Every configured automation/workflow for the account (name, enabled/disabled, created/updated dates, execution counts), connected sending accounts, connected integrations, registered users (name, email, last login), and usage/spend by feature for the past {{LOOKBACK_DAYS}} days.
- **Account notes/memory:** Stated goals, context, relationship history — whatever your team has recorded about why this account bought or trialed.
- **{{CALL_LIBRARY}}:** Search for call transcripts tied to the account's domain.
- **{{CRM}}:** Company activity feed — notes, calls, emails, deal stage history.

Proceed to the sections only once all data is in hand.

---

### Section 1 — What are they solving for?

**What to check:**
- Review their automation/configuration stack. What motions are they primarily building? (Top-of-funnel / prospecting, operational / RevOps, expansion / retention, or a mix?)
- Cross-reference setup against execution: are the workflows they built actually running? Check execution counts per workflow. Anything with zero executions for {{STALE_DAYS}}+ days is not solving anything — flag it specifically.
- Outreach-oriented workflows: are sending accounts connected? Are sequences approved and sending, or just drafted and sitting?
- Integration-dependent workflows (e.g., website visitor identification): is the connected tool live and producing executions?

**Output rules:**
- Max 750 characters.
- Lead with what they're solving for (1–2 sentences, shorthand).
- Follow with whether the setup actually points at solving it — name specific gaps (e.g., "Visitor-ID workflow: 0 executions in 6 days").
- No "likely," "probably," or "seems." Only what the data shows.

---

### Section 2 — Lead scoring & qualification

**What to check:**

Tiering:
- Does a scoring system exist with at least 3 tiers ({{TIER_LABELS}} or equivalent)?
- Is it binary (ICP fit / not fit)? Binary = flag.
- No scoring at all? Flag as critical.

Centralization:
- Is there one core scoring/qualification workflow ({{SCORING_WORKFLOW}})?
- Do other workflows (social engagement, website visitor, inbound lead, funding signals, etc.) route back to that core, or do they each qualify inline?
- Check actual structure: are "multiple scoring workflows" really sub-components of one parent, or genuinely separate? Sub-components ≠ separate — state which it is.

Tier persistence:
- Do not assume. Run three checks and compare:
  1. **Tagged accounts:** count accounts in {{USAGE_DATA_SOURCE}} carrying a tier label. State the exact count and label names found.
  2. **Accounts that passed the ICP gate:** count accounts whose status/notes show sequencing language ("sequence drafted," "queued," "awaiting approval"). These definitively passed qualification and received outreach.
  3. **Compare the two counts.** If tagged count is significantly below sequenced count, tier persistence is broken. Report the exact gap as a number and percentage (e.g., "7 of 26 qualified accounts tagged — 19 missing, 73% gap").
- If a gap exists, read the instructions of the workflows responsible for untagged accounts. Confirm whether they call {{SCORING_WORKFLOW}} before sequencing. If they don't, state that as the root cause explicitly.
- Do not stop at "zero tier tags" as the only failure mode. Partial persistence — some workflows tag, others don't — is real and common. Catch both.

Spend/usage waste:
- Pull the top usage-consuming features from the past {{LOOKBACK_DAYS}} days (actual data).
- Do NOT flag spend as waste based on percentage or volume alone. High spend on enrichment or research is not waste if the ICP gate is working.
- Before flagging waste, run the mandatory cross-reference: pull recent processing history for 30+ accounts. Classify each as qualified (got enrichment/outreach) or disqualified. If every disqualified account shows processing stopped at the qualification gate — the gate is working. Do NOT flag as waste.
- Only flag waste if: (a) disqualified accounts show expensive enrichment/research firing after disqualification, or (b) no qualification gate exists in the workflow instructions at all.
- Base every statement on the cross-reference. No assumptions from spend data alone.

**Output rules:**
- Max 1,000 characters. Short labeled bullets: Tiering / Centralization / Tier persistence / Spend waste.
- State what you found. Flag gaps without padding.

---

### Section 3 — Alerting & notifications

**What to check:**
- Are alert workflows configured for top-tier accounts, routing to {{ALERT_DESTINATIONS}}?
- Do alerts route to specific destinations or are they generic?
- What does the alert body contain? Check for: company context, multiple stakeholders (multi-threading), drafted outreach.
- Is the alert actionable — can a seller act immediately from it — or is it an FYI ping with no context?

**Scope boundary:** Do NOT assess sequence approval status, outreach pipeline, or whether drafts are acted on — that belongs in Section 4. This section covers only: whether notification workflows exist, what triggers them, where they route, and whether a seller can act from the notification alone.

**Output rules:**
- Max 500 characters. Shorthand (e.g., "Top-tier alerts → sales channel. No drafted sequences. No multi-stakeholder. Task alerts: none configured."). State what's there and what's missing.

---

### Section 4 — Messaging

**What to check (run all four steps):**

**Step 1 — Voice governance configuration:** Read the {{VOICE_GOVERNANCE}} setup state word-for-word from the account's actual configuration. Does it say "not yet configured" (or equivalent default text)? If yes, flag immediately — voice governance is almost certainly fragmented. Never assume the messaging stack is healthy while the central voice layer is unconfigured.

**Step 2 — Identify every workflow that actually drafts outreach:** Read all workflow instructions word-for-word. Do not rely on titles, descriptions, or usage counts. Find every workflow that builds sequences, references a sender, or defines a sequence structure. List each by name and which sender/channel it governs. These own messaging — not the voice-governance layer.

**Step 3 — Check where voice is governed in each:** For each workflow from Step 2, check whether voice, tone, CTA rules, or style prohibitions are defined inline, or whether it delegates to {{VOICE_GOVERNANCE}}. Inline voice rules = architecture flag. Correct pattern: the play workflow owns signal, hook, and contact research; the voice layer owns voice. State how many workflows have inline voice rules and name them.

**Step 4 — Message examples:** Check saved message examples for every connected sender. Zero examples for any sender is a hard flag — not a soft one. Approved sequences never saved as examples do not count. State the exact count per sender.

**Output rules:**
- Max 1,000 characters. Four labeled bullets: Voice governance / Outreach-drafting workflows / Architecture / Message examples.
- No "likely" or "probably" — you read the actual instructions.

---

### Section 5 — User adoption patterns

**What to check:**
- How many registered users exist? Pull from {{USAGE_DATA_SOURCE}}.
- List all registered users by name and title (where available).
- Flag the primary contact / champion (cross-reference account notes and {{CRM}}).
- Which users are most active? Use last-login dates and execution activity.
- Month-over-month login trend: starting count vs. current — growing / flat / declining.

**Output rules:**
- Max 1,000 characters. User list first (name, title, active/inactive indicator), then a 2–3 sentence adoption trend narrative.

---

### Section 6 — Summary: prognosis & interventions

**Format:**
- 1–3 sentences on overall health: Is adoption healthy and growing? Stalled? Churn risk? Are they getting real value?
- Bulleted key findings from Sections 1–5. Each bullet: 1–2 sentences, max 200 characters.
- For each flagged finding, name one concrete intervention, mapped from the failure:
  - Dead workflows ({{STALE_DAYS}}+ days, zero executions) → configuration/re-enable session with the champion
  - Binary or missing scoring → tiering working session; build or centralize {{SCORING_WORKFLOW}}
  - Tier persistence gap → wire the offending workflows to call {{SCORING_WORKFLOW}} before sequencing
  - Post-disqualification spend → add/repair the qualification gate before enrichment steps
  - Non-actionable alerts → rebuild alert bodies with context, stakeholders, and drafted outreach
  - Unconfigured voice layer / inline voice rules → consolidate voice into {{VOICE_GOVERNANCE}}
  - Zero message examples → save approved sends as examples for each sender
  - Flat/declining logins or single-threaded adoption → champion check-in, onboard additional users

**Output rules:**
- Max 1,000 characters. Each bullet is a real finding with its intervention — never a section-header restatement.

---

### General rules

- Never use "likely," "probably," or "seems." Every statement must be grounded in data pulled in Step 1.
- Customized vs. default: read the actual instructions. Generic structure with no org-specific context = default. Call it that.
- Checking "separate" vs. sub-components: check the actual parent-child structure. Sub-components of one parent ≠ separate workflows.
- Output sections in sequence, clearly labeled.
- Signal-to-noise beats completeness. If a data point doesn't inform a decision, leave it out.

---

## What good looks like

A great audit reads in under two minutes and leaves nothing to interpretation: every claim traces to Step 1 data, dead workflows are named with exact zero-execution day counts, the tier-persistence check reports a hard number and percentage (never "some accounts seem untagged"), spend is only called waste after the 30-account cross-reference proves the gate is leaking, the messaging section names each outreach-drafting workflow and where its voice rules actually live, and every flag in the summary arrives paired with one concrete intervention someone can schedule this week.

Mediocre looks like: hedged language ("adoption seems low"), spend flagged as waste from percentages alone, "no tier tags" reported without checking partial persistence, messaging judged from workflow titles instead of read instructions, scope bleeding between sections, or a summary that restates headers instead of findings — describing the account instead of diagnosing it.
