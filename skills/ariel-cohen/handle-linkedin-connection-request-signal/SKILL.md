---
name: handle-linkedin-connection-request-signal
title: Handle LinkedIn connection request signal
description: >-
  Use this skill when someone sends a team member an inbound LinkedIn connection
  request. An inbound request is a deliberate, ACTIVE first-party intent signal —
  meaningfully stronger than a passive profile view — and it deserves different
  scoring rules. The skill resolves and enriches the requester, gates them
  through dedup / internal / relationship / ICP checks, attaches the signal to
  the CRM, and scores it with active-signal overrides: a decision maker at a
  serious company is MQL-eligible on this lone signal, a weak persona caps at
  the awareness tier, and a request from a closed-lost account is treated as a
  reactivation candidate rather than ignored. Every ICP-relevant outcome posts
  to a visibility channel; replies and accepts stay human. It never sends
  outreach.
category: Signals
tags: [Sales]
---

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{PROFILE_OWNER}}` — Team member whose inbound connection requests are processed
- `{{CRM}}` — Your CRM (e.g. HubSpot, Attio)
- `{{INTERNAL_DOMAINS}}` — Your company domain(s); requests from these stop silently
- `{{VISIBILITY_CHANNEL}}` — Slack channel that gets one visibility post per processed request
- `{{CRM_HYGIENE_SKILL}}` — Sub-skill reference: how to create/update companies & contacts in your CRM
- `{{LEAD_SCORING_SKILL}}` — Sub-skill reference: your lead scoring & qualification methodology (its normal MQL alerting stays on)
- `{{REACTIVATION_SKILL}}` — Sub-skill reference: how you handle closed-lost account reactivation (optional — skip the reactivation branch's owner notification if you don't have one)
- `{{SELF_SERVE_THRESHOLD}}` — Company profile below which accounts route self-serve rather than MQL (default: fewer than 50 employees AND ≤$10M raised)
- `{{REACTIVATION_WINDOW}}` — Minimum time since a closed-lost deal before a request counts as a reactivation signal (default: ~90 days)

## Overview

This skill runs when someone sends **{{PROFILE_OWNER}}** a LinkedIn
**connection request**. The requester reached out to YOU — this is a
deliberate, **active** first-party intent signal, meaningfully stronger than a
passive profile view. The job is: resolve + enrich the requester and their
company, gate it, attach to CRM per standard hygiene, and score the signal.

**Golden rule — the CRM is never polluted.** Only a requester who is
identified + company-resolved + not-internal + not-a-current-customer +
ICP-matched ever reaches a CRM write. Everyone else is silently discarded or
logged to account memory only.

The webhook trigger only validates + routes. All behavior lives here.

### Payload shape

The routing trigger passes a single, already-deduplicated signal with the
person's name, LinkedIn member id / URL, headline, and the invitation note (or
null), plus a detection timestamp. Be robust to both a structured `person`
object and a stringified context blob carrying the same fields.

- The **invitation note**, when present, is **strong verbatim intent
  evidence**. Carry it through verbatim to scoring, account memory, and any
  alert. Never invent one if absent.
- The **headline** is a LinkedIn headline, **not a company name** — never
  treat it as a company or parse a company out of it.

### Scope — score + alert only

This skill does scoring + routing + CRM/account-memory updates ONLY. These are
people who reached out to YOU — any reply or accept is handled manually by
{{PROFILE_OWNER}} outside the agent. Do not send outreach of any kind, do not
build or enroll sequences, do not queue or accept connection requests or DMs,
and do not create review/approval tasks. Letting {{LEAD_SCORING_SKILL}} post
its normal MQL alert for a genuine qualifying account is expected and is NOT
outreach. *(⚠️ Policy decision — see the checklist. Wire outreach on top only
as a conscious opt-in once you trust the signal quality.)*

## Step 1 — Dedup (before enrichment)

A connection request is a single discrete action, so the only real duplicate
source is webhook redelivery from the same person. After you have the person's
LinkedIn member id (and, once resolved, the account), check the resolved
account's memory for an existing connection-request entry with the same member
id. If found → redelivery of an already-processed request → **stop silently.**
No new CRM writes, no memory writes, no channel post.

If the person cannot be identified at all (no name and no LinkedIn URL /
member id) → **stop silently** (anonymous). No enrichment, no writes, no post.

## Step 2 — Resolve requester identity & company (mandatory)

Identifying the *person* is not the same as resolving the *company*. You need
both before proceeding. **Never infer the company from the headline.**

1. Run contact enrichment on the person's LinkedIn URL (or member id) to
   resolve current employer name, company domain, confirmed title, and location.
2. **Headline-vs-enrichment conflict (mandatory live check).** Enrichment is
   frequently stale and lags job changes. If the headline names a specific,
   different current company or status than enrichment returns — "Stealth",
   "Building X", "Founder/Co-Founder at [new co]", "ex-[Company]", or a named
   employer that is not the enriched one — do NOT trust enrichment. Verify
   against the person's live LinkedIn profile via a profile scrape and use the
   current position shown there. A request from someone who has left the
   enriched company is not intent for that company.
3. If enrichment does not return a confident company name + domain, run a
   LinkedIn profile scrape on the profile URL, then general web research as a
   last resort.

**Exit condition — UNRESOLVED:** If after the full waterfall you still cannot
confidently determine a company name + domain, set outcome = UNRESOLVED, write
nothing to CRM / account memory, do NOT post, and stop. A guessed company is
worse than UNRESOLVED.

Exit this step with: full name, confirmed title, company name + domain, location.

## Step 3 — Internal check

If the resolved domain is one of {{INTERNAL_DOMAINS}} → **stop silently.** No
CRM, no memory, no post.

## Step 4 — CRM relationship check

Look up the company in the CRM and branch:

- **Active Partner** → **stop silently.** Partner accounts are managed by
  their owner — no CRM writes, no scoring, no post.
- **Current customer (Closed Won)** → outcome = EXISTING CUSTOMER. Log the
  request (with verbatim note) to the account's memory so the owner sees the
  touch — memory-only write. Do NOT create/update CRM records, do NOT score.
  Jump to Step 8.
- **Active (open) deal** → outcome = EXISTING RELATIONSHIP. Log the request
  (with verbatim note) to account memory so the deal owner sees it. Do NOT
  create outreach. Jump to Step 8.
- **Closed-Lost → reactivation candidate (do NOT ignore).** A deliberate
  connection request from a decision maker months after a lost deal is a
  genuine reactivation signal. Do NOT silent-stop. Instead:
  1. Log the request (with verbatim note) to account memory.
  2. Continue to Step 5 (ICP) and Step 7 (score) treating it as a live signal.
  3. In Step 7, apply the closed-lost reactivation judgment: the top-tier
     reactivation floor applies only when there was a **genuine prior buying
     evaluation** (a real deal / demo / trial), the requester is a **strong
     buyer persona**, and **enough time has elapsed ({{REACTIVATION_WINDOW}}
     since the close)**. A weak persona, a very recent close, or a loss driven
     by low-dollar pricing friction does NOT lift it — it stays at the
     awareness tier: log + visibility post, no MQL.
  4. For a qualifying reactivation, also load {{REACTIVATION_SKILL}} for the
     deal-owner notification and "what changed" framing — notify the deal
     owner and post, but do NOT run any reactivation outreach or sequence.
     The MQL channel must get **exactly one post** per reactivation: the lead
     scoring skill's normal alert owns it; the reactivation skill contributes
     only the deal-owner notification.
- **No existing relationship (net-new)** → continue to Step 5.

## Step 5 — ICP check

Compare the company against your ICP segments.

- **Not ICP** → outcome = NOT ICP. No CRM writes, no account-memory write.
  Still post one {{VISIBILITY_CHANNEL}} message. Jump to Step 8.
- **ICP match** → continue to Step 6.

## Step 6 — Log signal & create/update Company + Contact in the CRM

**⛔ Hard gate — do nothing in this step unless ALL are true:** (a) requester
identified (not anonymous); (b) company confidently resolved to a real domain
in Step 2; (c) domain not internal (Step 3 passed); (d) not a current customer
(Step 4); (e) passed the ICP check (Step 5). If any fails, skip this step
entirely. (Closed-Lost reactivation candidates that are ICP DO proceed here.)

Follow {{CRM_HYGIENE_SKILL}} to create/update the company and a contact for
this person (name, title, LinkedIn URL, company, location), associated
together. Add a CRM note on the contact:

```
LinkedIn connection request → {{PROFILE_OWNER}}
• Sent {{PROFILE_OWNER}} a connection request on [detected_at]
• Note included: [verbatim invitation note, or "none"]
• Prior connection requests from this company: [n]
```

Log the same to the account's memory and refresh its state summary, keyed by
the person's LinkedIn member id (this is what Step 1's dedup reads).

## Step 7 — Score the signal (ACTIVE-signal rules)

Run {{LEAD_SCORING_SKILL}} on this account. Pass forward the full signal
context: signal type, who received it, the verbatim invitation note, the
person's name / title / LinkedIn URL / company, prior connection-request
count, and that enrichment + CRM attach are done.

**A connection request is an ACTIVE signal — these overrides apply and take
precedence over generic passive-signal caps:**

- Classify persona first:
  - **Decision maker / strong buyer persona:** CRO, VP/Head of Sales, VP/Head
    of Marketing, CMO, CEO, Co-founder, RevOps Lead, GTM Engineer, Growth
    Lead, Head of Demand Gen, Agency Owner, or equivalent GTM leadership with
    buying authority *(tune to your ICP's buying committee)*.
  - **Weak / non-buyer persona:** IC, Support, Finance, HR, Ops, Analyst,
    Strategy/Partnerships/BD, or any junior title without buying authority.
- **Decision maker → top-tier / MQL-eligible on this lone signal.** Do NOT
  cap at the awareness tier the way a lone passive profile view is capped. A
  note referencing your product, their pain, or a meeting request strengthens
  this.
- **"Serious company" still governs the tier.** The self-serve gate runs
  first: a decision maker at a company below {{SELF_SERVE_THRESHOLD}}
  correctly lands in the self-serve tier, not MQL — that is expected, not a
  bug. A genuine MQL means a decision maker AND a company that clears that
  gate.
- **Weak / non-buyer persona → caps at the awareness tier.** Accumulates in
  memory; lifts when other signals stack.
- **Never the maximum tier on a lone LinkedIn signal.**
- The verbatim invitation note feeds CRM + scoring exactly as written.

Instruct the scoring skill explicitly: scoring, tags, stage, CRM sync, memory,
and its normal MQL alert are all in scope; outreach is not. For a qualifying
account, let its Lead Scoring Alert post to the real MQL channel as usual — do
NOT suppress or redirect it.

## Step 8 — Visibility post

Post to {{VISIBILITY_CHANNEL}} for these outcomes: SCORED (any tier), NOT ICP,
EXISTING CUSTOMER, EXISTING RELATIONSHIP. This is a visibility log and is **in
addition to** any MQL-channel post the scoring skill sent in Step 7 (do not
deduplicate them away).

Post nothing (fully silent) for: ANONYMOUS / UNRESOLVED requesters,
INTERNAL-domain requesters, ACTIVE PARTNERS, and duplicate redeliveries.

Format:

```
🤝 [Full Name] — [title]
Company: [company name] ([domain]) | [location]
Note: [verbatim invitation note, or "no note"]
Prior requests: [n] (this company)
LinkedIn: [linkedin_url]

Outcome: [one of]
  SCORED — [tier]  (decision maker at a serious company = MQL)
  EXISTING CUSTOMER — logged, no scoring
  EXISTING RELATIONSHIP — active deal / closed-lost reactivation, logged, no outreach
  NOT ICP — no CRM, no scoring
What we did: [one line]
```

## Hard rules (non-negotiable)

- Do NOT send any outreach (email or LinkedIn).
- Do NOT create, edit, or enroll anyone in any sequence.
- Do NOT queue, send, or accept any connection request or LinkedIn message.
- Do NOT DM the person or draft a reply, and do NOT create review/approval
  tasks.
- Never infer a company from a headline; never guess when the waterfall comes
  back empty — UNRESOLVED beats a wrong company.
- If any step is blocked, report the blocker in the outcome/memory — never
  substitute an outreach action.

## What good looks like

A great run turns a raw connection request into exactly one of the named
outcomes with zero CRM pollution: the company was resolved through the full
waterfall (with the headline-conflict check actually catching job-changers),
gates ran in order, the invitation note traveled verbatim into the CRM note,
account memory, and the visibility post, and a decision maker at a serious
company produced both the MQL alert and the visibility post — one of each.
Closed-lost requesters got the reactivation treatment instead of a silent
drop.

Mediocre looks like: companies guessed from headlines, weak personas floating
above the awareness tier on a single request, reactivation candidates ignored
because the account was closed-lost, double MQL posts, or any reply/outreach
sent by the agent.
