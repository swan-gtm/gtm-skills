---
name: "account-progression-staging"
title: Account progression staging
description: "Use this skill when you want attribution that measures whether GTM activity actually moves accounts forward — not touchpoint \"credit.\" It assigns each account a single current progression stage (Unaware → Aware → Engaged → Qualified → Sales Ready → Customer) from its full signal stack using deterministic, auditable rules, so the same inputs always produce the same stage and every assignment is explainable from the evidence that triggered it. Progression is measured at the account level with a buying-group gate — advancement requires multiple distinct contacts, never one power user — so a single loud champion can't fake momentum. Each run applies exactly one stage tag, records a stage-entry event with an evidence snapshot and time-in-prior-stage, updates the running stack in account memory, and routes a Sales-Ready alert with buying-group context and a recommended next action. Because it writes stage history, it turns attribution into delta-versus-baseline: conversion rate and velocity per stage transition, exposed cohort vs. control — so budget goes to what drives stage movement, not what drives clicks. Every threshold is exposed as a tunable default. Use it for stage assignment, progression tracking, \"why is this account here?\" explainability, stuck-account activation lists, and Sales-Ready routing."
category: ABM
---

# Account progression staging

Assigns any account a single current progression stage from its full signal stack, records the stage entry with the evidence that triggered it, and routes an alert when an account crosses into Sales Ready. Progression is account-level and buying-group-gated: the question is never "did one person do something" but "is this buying group moving forward." Every run updates the running stack in account memory and writes exactly one stage tag, so the stage is always defensible from the memory snapshot alone.

The point of staging this way is measurement. Once accounts carry a stage and a stage-entry history, "attribution" stops being touchpoint credit and becomes **delta versus baseline** — did exposure to a campaign or channel raise the conversion rate or shorten the time for a stage transition, versus a comparable unexposed cohort. This skill produces the per-account substrate that makes that measurement possible; the measurement layer at the end covers the cohort math.

## Template placeholders

Replace every `{{...}}` before enabling.

- `{{CRM}}` — Your CRM (e.g. HubSpot, Salesforce, Attio)
- `{{STAGE_FIELD}}` — The account/company field this skill writes the stage into (create one if it doesn't exist; keep it distinct from your opportunity pipeline stage)
- `{{ALERTS_CHANNEL}}` — Channel where Sales-Ready transitions post (your MQL/handraiser channel)
- `{{ACTIVATION_CHANNEL}}` — Channel (or list owner) for stuck-account activation plays (optional; defaults to marketing ops)
- `{{SALES_OWNER}}` — The rep or founder-seller whose queue Sales-Ready accounts feed
- `{{ICP_DEFINITION}}` — What counts as ICP fit (firmographic + segment rules); consumed by the Qualified gate
- `{{KEY_PAGES}}` — High-intent pages that count as key page views (default: pricing, product, integrations, demo/contact)
- `{{INTENT_SOURCE}}` — Third-party intent provider, if any (optional; delete intent rows if unused)
- `{{MIN_CONTACTS}}` — Distinct engaged contacts required to advance past Aware (default: **2**)
- `{{QUALIFIED_CONTACTS}}` — Distinct contacts required for the Qualified committee path (default: **3**)
- `{{QUALIFIED_DEPARTMENTS}}` — Distinct departments those contacts must span for Qualified (default: **2**)
- `{{AWARE_ADS_14D}}` — Ad impressions in 14d that qualify for Aware (default: **> 3**)
- `{{AWARE_VISITS_14D}}` — Web visits in 14d that qualify for Aware (default: **≥ 2**)
- `{{ENGAGED_KEY_PAGES_14D}}` — Key page views in 14d for Engaged (default: **≥ 2**)
- `{{ENGAGED_EMAIL_CLICKS_14D}}` — Email clicks in 14d for Engaged (default: **≥ 2**)
- `{{INTENT_THRESHOLD}}` — Intent score that qualifies for Qualified on its own (default: provider's "strong" band)
- `{{ENGAGEMENT_HALF_LIFE}}` — Days after which an engagement signal stops counting toward current stage (default: **30**)
- `{{ADS_HALF_LIFE}}` — Days after which an ad-exposure signal decays (default: **14**)
- `{{STALE_WINDOW}}` — Days with zero qualifying signal before an account is eligible for review-driven regression (default: **90**)

**Stage ladder:** Unaware / Aware / Engaged / Qualified / Sales Ready / Customer is the default. Rename freely — the ordering, gates, and precedence are the methodology; labels are cosmetic. Keep the ladder strictly ordered: every rule below depends on precedence.

### ⚠️ Optional EVAL mode (recommended for the first 1–2 weeks)

While you're calibrating thresholds, run with `{{CRM}}` writes disabled: skip every "write/update in `{{CRM}}`" step and instead include the exact stage tag, stage-entry record, and note text that WOULD have been written, inside the run output. Memory writes stay ON either way — you want the history accumulating so baselines can form. Once you trust the stages, follow the steps as written.

---

### Overview

Every run produces two things:

- **One stage tag** (`stage: unaware|aware|engaged|qualified|sales-ready|customer`) — the highest stage the account currently qualifies for. Exactly one, always.
- **A stage-entry record** (only when the stage changes) — stage, `entered_at`, the rule that fired, an evidence snapshot of the features at entry, the prior stage, and time-in-prior-stage. This is the row that later powers conversion-rate and velocity measurement.

Staging follows the full signal stack from account memory, not just the incoming event. Signals decay by type (`{{ENGAGEMENT_HALF_LIFE}}`, `{{ADS_HALF_LIFE}}`); an account that goes quiet doesn't hold a stage forever, but it also never drops on a single weak or aged event — only through the decay rules below or a deliberate review.

---

### Global rules (every run)

**Deterministic and auditable.** Same signal stack in → same stage out, every time. No "felt like Qualified." If two operators can't reach the same stage from the same evidence snapshot, the rule is underspecified — tighten the threshold, don't add judgment.

**Mutual exclusivity + precedence.** Evaluate every stage's entry criteria, then assign the **highest** stage that qualifies. Precedence, high to low: `Customer > Sales Ready > Qualified > Engaged > Aware > Unaware`. A Sales-Ready signal overrides a Qualified-only picture; Closed Won overrides everything.

**Buying-group gate — the core discipline.** Advancement past Aware requires **`{{MIN_CONTACTS}}` distinct engaged contacts**, not one person doing a lot. A single power user generating ten sessions is still one contact — that's Aware, not Engaged. Anonymous/deanonymized-but-unnamed activity counts toward Aware volume only, never toward the distinct-contact gate for Engaged+.

**Never regress on a weak or new signal.** A new low-weight event on an account that already scored higher never lowers the stage. Regression happens only via (a) signal decay dropping the qualifying evidence below threshold **and** the account passing `{{STALE_WINDOW}}`, surfaced for review — or (b) an explicit disqualification. Never as a side effect of routine scoring.

**Evidence or it didn't happen.** Every stage assignment stores the exact features that triggered it in the stage-entry record. A stage with no evidence snapshot is a bug, not a stage.

---

### Step 0 — Resolve identity + assemble the account signal stack

Before any stage logic, get the account and its rolled-up signals.

1. **Resolve to one account.** Join the incoming event to `account_id` in this order: `account_id` if present → `contact_id` → account → `email` → contact → account → `domain` → account. If none resolve, hold as unassigned and stop — never stage an orphan event.
2. **Roll contact-level signals up to the account.** Progression is account-level; most raw signals are contact-level. Aggregate the stack over the relevant windows (see Step 1).
3. **Load the running stack from memory.** Score the full decayed stack, not just today's event. Apply `{{ENGAGEMENT_HALF_LIFE}}` and `{{ADS_HALF_LIFE}}` — signals older than their half-life don't count toward the current stage (but stay in history).

### Step 1 — Compute buying-group features

Compute over the account's decayed stack:

- `distinct_contacts_engaged_14d` — named contacts with any first-party engagement
- `distinct_departments_engaged_30d`, `distinct_titles_engaged_30d`
- `key_page_views_14d` (pages in `{{KEY_PAGES}}`), `web_visits_14d`, `email_clicks_14d`
- `ad_impressions_14d`
- `webinar_or_event_30d`, `handraiser_events_30d` (demo request / trial / contact-us)
- `intent_score` (from `{{INTENT_SOURCE}}`, if configured)
- Hard CRM flags: `sales_meeting_held`, `sales_accepted`, `closed_won`

These features — not the raw event — are what the stage criteria read.

### Step 2 — Evaluate stage criteria, assign the highest that qualifies

Deterministic entry criteria. Evaluate all, take the highest by precedence.

- **Customer** — `closed_won = true` on the account.
- **Sales Ready** — any of: `handraiser_events_30d ≥ 1` (demo request / trial signup / contact-us), `sales_meeting_held`, or the `sales_accepted` flag in `{{CRM}}`. A genuine hand-raise or booked meeting is Sales Ready regardless of buying-group breadth — one authorized buyer asking to talk is the signal.
- **Qualified** — `{{ICP_DEFINITION}}` = true **AND** ( `intent_score ≥ {{INTENT_THRESHOLD}}` **OR** ( `distinct_contacts_engaged_14d ≥ {{QUALIFIED_CONTACTS}}` **AND** `distinct_departments_engaged_30d ≥ {{QUALIFIED_DEPARTMENTS}}` ) ). ICP fit is a hard gate here — a non-ICP account never reaches Qualified on engagement alone.
- **Engaged** — `distinct_contacts_engaged_14d ≥ {{MIN_CONTACTS}}` **AND** ( `key_page_views_14d ≥ {{ENGAGED_KEY_PAGES_14D}}` **OR** `email_clicks_14d ≥ {{ENGAGED_EMAIL_CLICKS_14D}}` **OR** `webinar_or_event_30d ≥ 1` ).
- **Aware** — ( `ad_impressions_14d {{AWARE_ADS_14D}}` **OR** `web_visits_14d ≥ {{AWARE_VISITS_14D}}` ) with **at least `{{MIN_CONTACTS}}` contacts exposed or engaged** (anonymous exposure volume counts here).
- **Unaware** — account exists in `{{CRM}}` or the target list, no qualifying mapped signal in the decayed stack.

If an account qualifies for none of Aware+ but exists, it's Unaware. If it qualifies for several, precedence decides — assign the top one only.

### Step 3 — Apply the stage (write + verify)

The stage tag write happens FIRST — before memory, history, or any alert.

1. **Write:** remove any existing `stage:` tag, apply the one scored. Every account carries exactly one.
2. **Verify:** re-read the record and confirm. Not found → retry once → re-verify. Track `STAGE_WRITE_STATUS = VERIFIED | FAILED` through the remaining steps — never continue as if a failed write succeeded.
3. **Sync to `{{CRM}}`:** write the stage into `{{STAGE_FIELD}}`, exact casing. Record not found → skip and note in memory.

### Step 4 — Record stage history + evidence snapshot

**Only when the stage changed from the last run.** Append a stage-entry record:

- `account_id`, `stage`, `stage_entered_at`
- `prior_stage`, `time_in_prior_stage_days` (from the prior entry record)
- `entry_reason` — the specific rule that fired (e.g. "Engaged: 3 distinct contacts + 2 key page views")
- `evidence_snapshot` — JSON of the exact feature values at entry (the buying-group features from Step 1)

This is the history the whole measurement layer runs on. Without it you're stuck doing fragile point-in-time inference; with it you get time-in-stage, conversion rates, velocity, and cohort analysis. Never skip it on a real transition.

### Step 5 — Update account memory

Prepend a snapshot to the top of the account's memory; preserve all history below.

Header: `[STAGE: stage] — date` (append `⚠️ STAGE WRITE FAILED` when `STAGE_WRITE_STATUS = FAILED`).
Body: signal stack strongest-first (with decay applied), buying-group summary (`distinct_contacts_engaged`, `distinct_departments`, whether the `{{MIN_CONTACTS}}` gate passed), the rule that fired, and any gate that held it back (e.g. "3 sessions but 1 contact → held at Aware; buying-group gate not met").

Also set the one-line state summary: `[STAGE: stage] — [what drove it / what's blocking advance]`.

### Step 6 — Detect the transition + route

**No stage change → no alert.** Update memory (Step 5) and stop. This discipline keeps `{{ALERTS_CHANNEL}}` readable.

**Advanced to Sales Ready →** post to `{{ALERTS_CHANNEL}}` in your standard alert format, routed to `{{SALES_OWNER}}`. Include: the triggering signal, the buying-group summary (who engaged, titles, departments), relationship history in 1–2 lines from `{{CRM}}`, exec stakeholders not yet engaged, and an opinionated recommended next action. Report `STAGE_WRITE_STATUS` honestly in the actions-taken line.

**Advanced into an earlier stage (Aware/Engaged/Qualified) →** no rep alert; the stage tag and history are enough. These feed reporting and the account's own record.

**Stuck-account check (activation, not alert).** If an account has held Aware for more than 30 days (or your `{{STALE_WINDOW}}`) with no advance, add it to the activation list for `{{ACTIVATION_CHANNEL}}` — this is the "Accounts stuck in Aware > 30 days" play, run as a batch, not a per-account ping.

**Velocity note.** On any advance, record `time_in_prior_stage_days` against the transition. Faster-than-baseline transitions are the leading indicator the measurement layer watches; slower-than-baseline is the early warning.

---

### Measurement layer (why the history matters)

This skill deliberately writes stage history so attribution can be **lift versus baseline** instead of touchpoint credit. Once you have a stable window of stage-entry records (give it ~90 days before publishing lift):

- **Baseline:** per transition (Aware→Engaged, Engaged→Qualified, …), the conversion rate within N days and the median / P75 time-in-stage.
- **Lift:** cohort accounts by exposure (e.g. ran a campaign / attended an event vs. a matched unexposed control on ICP, starting stage, and firmographics), then compare conversion rate and velocity. `lift = (exposed_rate − control_rate) / control_rate`.
- **The line for finance:** budget goes to what produces the biggest lift in *stage movement*, per transition — not to what produces the most clicks.

Don't publish lift until baseline sample sizes are stable, or the numbers bounce and lose trust.

---

## What good looks like

A great run assigns one stage, and the memory snapshot alone tells you why: signal stack strongest-first, buying-group summary named, the exact rule that fired, and any gate that held the account back. The buying-group gate caught the single power user with ten sessions and held them at Aware. ICP fit gated Qualified so a non-fit account with high intent didn't sail through. The transition into Sales Ready landed in `{{ALERTS_CHANNEL}}` with a buying-group summary and a next action a rep can act on in 60 seconds — and it carried `time_in_prior_stage_days`, so velocity is measurable. Nothing regressed on a stray weak signal.

Mediocre looks like: a stage justified by the last event instead of the full decayed stack; one contact's activity promoted to Engaged; a non-ICP account scored Qualified on intent alone; a transition written with no evidence snapshot (so it can never be audited or measured); every stage change paging a rep; or a demotion sneaking in because one signal aged out, with no review and no `{{STALE_WINDOW}}` check.
