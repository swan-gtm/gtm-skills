---
name: hiring-signal-verification
title: Hiring signal verification
description: |
  Use this skill whenever a hiring or open-roles signal is about to be used as a fact — in
  account scoring, an ACV or tier assessment, an MQL alert, an outreach hook, or a CRM/account
  note. It is a verification gate, not a signal finder: it forces every hiring claim to be
  confirmed at the target company's OWN source (their careers page, or a job listing matched by
  company name AND domain) before it can influence a score, an alert, or a message. AI
  web-research summaries routinely attribute another company's job openings to your target —
  shared applicant-tracking-system tenants, shared job-board slugs, and similarly named
  companies all cause it — and a wrong "saw you're hiring" line is worse than no line at all.
  Do NOT use this to discover hiring signals (that is a signal-sourcing job); use it to decide
  whether a hiring signal you already have is allowed to be used.
category: Signals
tags: [Sales, RevOps]
---

# Hiring signal verification

"They're hiring" is one of the most-used signals in outbound — and one of the most
misattributed. Research tools stitch together careers pages, job boards, and ATS tenants, and
they regularly hand you another company's hiring spree under your target's name. The prospect
knows their own company better than any research tool: one wrong "noticed you're opening a
sales org" and your credibility is gone, or worse, your scoring model promotes an account on
evidence that belongs to someone else. This skill is the gate every hiring claim passes
through before it becomes a fact.

## Template placeholders

Replace every `{{...}}` before enabling. See the [setup checklist](references/setup-checklist.md)
for the full setup list.

- `{{WEB_RESEARCH_TOOL}}` — Your AI web-research tool or agent whose prose summaries feed
  scoring and outreach (e.g. a deep-research agent, an enrichment provider's AI summary)
- `{{PEOPLE_SEARCH_TOOL}}` — Your people/employee search tool, filterable by company domain
  and title (e.g. LinkedIn Sales Navigator, Apollo, Lusha)

---

### When this applies

Any time a hiring or open-roles signal is about to be used as a **fact** — in an ACV/tier
assessment, an MQL or scoring alert, an outreach observation/hook, or a CRM/account memory
note. If you are about to write "they're hiring X" or "actively hiring for Y," this standard
governs it. No exceptions.

---

### The rule — verify at the company's OWN source

A hiring claim only counts when confirmed from the **target company's own source**:

- The company's **own careers page** (hosted on their domain), OR
- A **LinkedIn Jobs** listing (or other job board) whose posting is confirmed to belong to
  the target company — matching company **name AND domain**, not just a shared ATS or
  job-board slug.

**`{{WEB_RESEARCH_TOOL}}` prose is NEVER sufficient on its own for a hiring claim.** Web
research summaries routinely misattribute another company's roles to your target — same ATS
tenant, same job-board slug, or a similarly named company. Treat any hiring detail that came
from web research as **unverified** until it is confirmed at one of the two sources above.

To verify at source, use any of: the company's careers page directly, a LinkedIn Jobs (or
company-page jobs tab) check scoped to the exact company, or `{{PEOPLE_SEARCH_TOOL}}`
filtered by title at the exact domain.

---

### Misattribution guard — discard when citations point elsewhere

When a `{{WEB_RESEARCH_TOOL}}` answer supplies hiring (or any firmographic) "facts,"
**check the citations before using anything.** If the answer's sources are dominated by a
domain that is **NOT the target company's domain**, **DISCARD those derived facts entirely.**
Do not launder another company's data into the target's record, score, alert, or outreach.
Re-verify from the target's own source, or drop the claim.

---

### When a hiring signal fails verification

**Drop it.** Do not soften it ("they may be hiring…") or hedge it ("I noticed what looked
like…"). If it did not verify at the company's own source, it does not appear in the score,
the ACV assessment, the alert, the outreach, or the account record. A wrong hiring claim is
worse than none — the prospect knows their own company better than any research tool.

---

### Real failure this prevents

A scoring run's web research returned a full GTM hiring spree for a target account — VP Sales
($280–400K OTE), CMO, Director of RevOps, GTM Engineer, Demand Gen Lead, and more — and it
landed in a high-priority MQL alert as a "KEY INSIGHT" driving a "massive GTM expansion"
narrative. **Every role was cited from a different company's careers page** — an unrelated
software vendor the research tool had conflated with the target. The target actually had one open role (an
analyst position). Checking the target's own careers page or LinkedIn Jobs for the real
domain would have caught it in one step.

---

### What good looks like

Every hiring claim that reaches a score, an alert, an outreach draft, or an account note
carries a source on the target company's own domain (or a name-AND-domain-matched job
listing). Web-research prose alone never survives as a hiring fact. Signals that fail
verification disappear — no hedged versions leak through. And when a research answer's
citations point at the wrong domain, everything derived from it is discarded, not just the
hiring lines.
