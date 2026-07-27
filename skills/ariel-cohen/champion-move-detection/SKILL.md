---
name: "champion-move-detection"
title: Champion move detection
description: "Use this skill on a monthly cadence to detect champions and heavy users of your paying customers who changed jobs, verify the move against live LinkedIn data, score the new company, and surface qualifying moves as MQLs — while catching churn risk on the account they left. A known buyer bringing your product to their next company is one of the highest-converting signals in B2B; this skill turns it into a deterministic, deduped, monthly machine with hard guards against the classic failure modes (stale headlines, same-name profiles, warm familiarity mistaken for advocacy)."
category: Signals
---

# Champion move detection

Once a month, detect champions and heavy users of your paying customers who changed jobs and moved to a new company. A known buyer bringing {{PRODUCT}} to their next company is one of your highest-conversion signals — score the new company and surface it as an MQL when it qualifies. Secondary purpose: catch churn risk on the account they left.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist for the full list.

- `{{PRODUCT}}` — Your product's name
- `{{CRM}}` — Your CRM (e.g. HubSpot, Salesforce, Attio)
- `{{SCORING_SKILL}}` — Your account-scoring skill/process; this skill feeds moves into it as a high-intent signal
- `{{LINKEDIN_LOOKUP}}` — Live LinkedIn profile lookup tool (e.g. an Apify profile-search actor). Must return the profile's full experience section
- `{{MQL_OWNER}}` — Who owns champion-move MQL tasks and alerts
- `{{DIGEST_CHANNEL}}` — Where the monthly digest posts
- `{{COMPETITORS}}` — Your direct competitors (moves into these are logged, never scored)
- `{{WATCHLIST_MAX}}` — Max watched people per account (default: **5**)
- `{{REFRESH_WINDOW}}` — Days before an account's watchlist is rebuilt (default: **90**)
- `{{USAGE_WINDOW}}` — Lookback for "materially active" usage (default: **90 days**)
- `{{SELF_SERVE_THRESHOLD}}` — Company size/funding below which a move is future pipeline, not an MQL (default: **<50 employees AND ≤$10M raised**)
- `{{TIER_FLOOR}}` — Minimum tier a confirmed champion move scores (default: one tier above your standard mid-tier — mirror of a closed-lost floor if you run one)

### Scan set (which accounts run each month)

Run across BOTH:
1. **All accounts in your Closed Won stage** — the customer base.
2. **Any company carrying an active carried-forward champion** — tagged `champion-move` AND holding an active `[CHAMPION WATCHLIST]` entry marked `carried-forward` (see Phase 3.C). These are NOT customers; they are companies a proven serial champion moved into, tracked so you catch the person's NEXT move. A serial champion is your highest-value signal — never drop them because their current employer isn't a customer.

Expect the first full run to be slow and partial — it builds a watchlist for every customer from messy records. Report coverage gaps honestly in the digest rather than skipping silently; coverage compounds monthly.

### Writes permitted by this skill
Memory updates, state summaries, the `champion-move` tag, MQL stage moves, and alerts — nothing else. **Never send outreach from this skill. It recommends; humans send.**

---

### Phase 1 — Build / refresh the champion watchlist (per customer account)

For each Closed Won account, maintain a watchlist of up to {{WATCHLIST_MAX}} people, persisted in the account's memory under the header `[CHAMPION WATCHLIST]`. If the header exists and was refreshed within the last {{REFRESH_WINDOW}} days, reuse it and go straight to Phase 2 for that account.

A person qualifies via **either** bar:

1. **Champion / economic buyer of the account** — named champion in account memory, state summary, or {{CRM}} deal history (deal contacts, meeting attendees who drove the purchase).
   - **Realized-value requirement (do not soften).** Only watchlist someone under this leg if the relationship actually demonstrated value: EITHER the account reached **Closed Won**, OR the person was a **materially active** user (real usage, per the heavy-user bar below). A named contact or "economic buyer" on a deal that **never closed**, or a registered user of a free/never-activated workspace with negligible usage, is **warm familiarity — NOT a champion.** Brand recognition is not advocacy. Do not watchlist them under the champion leg.
2. **Heavy user of the account** — a registered user of the customer's workspace who is **materially active**: a top-2 consumer of product usage over the last {{USAGE_WINDOW}}, or clearly driving the account's workflows. A senior GTM title is NOT required — the heaviest hands-on user is often the strongest future champion regardless of title; that is the whole point of the heavy-user leg.
   - **Floor (exclude these even if they are a top consumer):** pure non-GTM-adjacent roles — Engineering/IT/DevOps, Support, Finance/Accounting, HR/People, Legal. They operate the tool for reasons unrelated to the buying motion and rarely carry it to a new GTM org.
   - **Keep** anything GTM or GTM-adjacent: sales, marketing, content, growth, RevOps, GTM/product ops, demand gen, founders, GTM-technical roles. When a title is ambiguous, keep them — a false include costs one monthly lookup; a false exclude misses the signal entirely.
   - Resolve titles via {{CRM}} first, then LinkedIn.

**How to identify heavy users.** Use **per-person** usage attribution from your product's analytics (individual events/credits/seats-activity by user). Org-level totals cannot attribute usage to a person — never use them for this. Treat self-declared titles in product data as a persona hint; confirm seniority via {{CRM}}/LinkedIn, never as ground truth.

**Watchlist rules (do not soften):**
- The heaviest user is often NOT the recorded champion. Always check usage; never rely on the champion record alone.
- **Exclude external consultants.** A workspace user whose email domain differs from the customer's domain (agency, RevOps consultancy) is not part of that company — do not watchlist them under this account.
- Resolve each person's **LinkedIn URL at watchlist-build time** — Phase 2 depends on it. Prefer vanity URLs; store whatever resolves. Enrich only when the URL is missing.

Persist in account memory:
```
[CHAMPION WATCHLIST] — refreshed [date]
- [Name] | [title] | [email] | [LinkedIn URL] | [champion / economic buyer / heavy user: ~N usage/{{USAGE_WINDOW}}] | last verified [date]
```

---

### Phase 2 — Move detection (the monthly LinkedIn check)

**Skip guard (dedup — check FIRST).** Skip any watchlist entry already marked `MOVED → [company], processed [date]` (see Phase 3.A). That move already fired once; re-detecting it would re-surface the same MQL. These entries are historical records, not active watch targets. Only the person's CURRENT-employer entry (active, or `carried-forward`) is live for detection.

For every ACTIVE watchlist person, verify current employment against **live LinkedIn** via {{LINKEDIN_LOOKUP}}.

**Live lookup is the authoritative source for the move-check — always run it for every active watchlist person.** You are detecting *recent* job changes, and cached enrichment lags exactly where recent moves happen — a champion who changed jobs last month is precisely the case cached data gets wrong. So:
- Cached enrichment may be used ONLY to help LOCATE a profile (resolve a LinkedIn URL) at watchlist-build time — never to decide employment status.
- If the live lookup errors, retry once with adjusted input. **If it fails twice for a person, classify that person UNCERTAIN and record the actual error verbatim in the digest** — a failed lookup is an UNCERTAIN classification, not an operational ticket.
- **NEVER fall back to cached enrichment or generic web research for a STILL or MOVED decision.**

Batch lookups aggressively — this is lookup work, not deep research; delegate across sub-agents when the watchlist is large.

**Verification rules (do not skip):**
1. **Read the EXPERIENCE section, not just the headline.** Headlines go stale. Current employer = the most recent experience entry with no end date.
2. **MOVED requires affirmative evidence** — the profile must explicitly list a NEW current employer. Absence of the old company alone is NOT a move.
3. **Wrong-person guard (HARD RULE).** A MOVED classification additionally requires that the destination profile's OWN experience history contains the ORIGIN company. A name + destination match alone is NEVER sufficient — confirm it is the same human by finding the origin company in their experience history. If it does not appear → classify UNCERTAIN. *(Rationale: a real sweep once matched a departed champion to a same-name profile at a different company and created a false high-tier MQL. Same name, different person.)*
4. **Advisor, fractional, board, and "managing partner"-style roles are NEVER a MOVED** — classify UNCERTAIN and note the role type. If they became a fractional consultant or agency operator, note them as a potential partner lead instead.
   - **Dual-role exception:** if a person lists BOTH the old and new companies as CURRENT (no end date on either), classify MOVED but flag `dual-role` — and soften all churn language on the old account (they have not left; they have added a role).
5. **Profile not found → UNCERTAIN.** Never guess. UNCERTAIN people go to the human-review list in the digest and are retried next month.

Classify each person: **STILL** (update "last verified" date) / **MOVED** (record new company, new title, move date if shown) / **UNCERTAIN**.

Ignore moves where the new company is **another existing customer** — that is an internal reshuffle, not a new-logo signal. Note it in the old account's memory but do not create an MQL.

---

### Batch mode (delegated sweeps)

When this skill runs as a **delegated batch sub-agent** (e.g. a monthly sweep fanned out across many accounts), execute **Phases 1–2 ONLY**. Do NOT execute Phase 3: no stage moves, no tier tags, no {{CRM}} writes, no channel posts, and **no tasks of any kind**.

- Return classifications + evidence in the requested report format.
- Operational problems (lookup failures, missing workspaces, unresolved profiles) go in a **PROBLEMS** section of the report — never into tasks or alerts.
- Phase 3 runs only when explicitly instructed, and only for named, verified movers.

---

### Phase 3 — On every CONFIRMED move

> **Task ownership (routing).** Every champion-move task or alert this phase produces is assigned to **{{MQL_OWNER}}**. The prior-relationship owner is not an automatic sender — surface them as a **recommendation inside the task** (e.g. "consider having [prior deal owner] send — they owned the relationship at [Old Account]"). {{MQL_OWNER}} decides who sends.

**A. The old account (company losing a champion):**
1. Prepend to account memory: `[CHAMPION DEPARTED] [date] — [Name] ([title]) left for [New Company] ([new title]). Was: [qualification reason].`
2. **Mark the watchlist entry processed (dedup).** Update the person's `[CHAMPION WATCHLIST]` line on this account to `MOVED → [New Company], processed [date]`. This entry is now a historical record — Phase 2's skip guard will never re-detect it, so the same move can only ever fire ONE MQL. Do not delete it; the record is what makes the run idempotent month over month.
3. If the account is an active paying customer and the departed person was its primary user or champion, flag it as a **churn risk** in the digest and in the account's state summary.
4. **Compound-departure escalation:** if TWO OR MORE watchlist people from the same account have left (this run or across prior `[CHAMPION DEPARTED]` entries), flag a **critical churn risk** prominently in the digest.

**B. The new company:**

0. **Champion-qualification gate (run BEFORE everything else in Phase 3.B).** The champion-move machinery — tier floor, MQL, `champion-move` tag — only applies to a person who actually realized value at the origin company. A move is NOT a champion move just because the person was a registered user or a named deal contact. Confirm BOTH:
   - **Realized value.** The origin relationship must be EITHER a **Closed Won** customer, OR the person must have been a **materially active** user there (real usage). A registered user of a free/never-activated workspace with negligible usage, or a named contact on a deal that never closed, fails this check — brand recognition ≠ advocacy; the person never saw the product deliver.
   - **Origin deal is not a recent loss.** If the origin is **Closed Lost within the last 90 days**, the person is leaving a company that *just declined* you — that is not a buying signal. Fails this check.

   **If EITHER check fails → STOP: no tier floor, no MQL, no champion-move tag, no scoring run.** Log the move to both companies' memory and, only if the person is GTM-relevant and the new company is a plausible ICP fit, post a soft FYI to the digest as a *potential future warm intro from the prior deal owner* — never a sales motion, never an MQL. Still carry the person forward per Phase 3.C (trajectory tracking is independent of this gate). Only when BOTH checks pass does the move proceed to scoring with the tier floor.

1. **Competitor / never-prospect check FIRST.** If the new company is one of {{COMPETITORS}} (or any direct competitor per your competitive knowledge) → log to memory only. No scoring, no outreach, no MQL. Also respect any standing never-prospect entries in org memory.
2. **Verify the new company's employee count and funding with real sources** (LinkedIn company page; enrichment for funding). **Never guess funding** — routing hinges on it. If funding cannot be sourced and employee count is near {{SELF_SERVE_THRESHOLD}}, classify routing as **NEEDS-REVIEW** in the digest instead of deciding.
3. **Score the new company — this trigger behaves like every other signal-driven trigger.** Load and run {{SCORING_SKILL}} in full, feeding the champion move in as the triggering **high-intent, first-party signal with relationship context**. The scoring skill then owns everything downstream: gates, tier, MQL routing, buying-committee enrichment, alerts, and any outreach — exactly as it does for a website visit or a hand-raise. Do NOT hand-craft a separate outreach motion here.
   - **Relationship context to pass into the signal:** who the person is, which customer they championed, what they did with {{PRODUCT}} there (role, usage, workflows built), their new title + company, and **who owned the prior relationship**. That owner is surfaced as a recommendation inside {{MQL_OWNER}}'s task — not an automatic assignment.
   - **Champion-move tier floor:** a confirmed champion move is demonstrated first-party history — the person has already bought or heavily used {{PRODUCT}} (guaranteed by the B.0 gate; a warm-familiarity or recent-loss move never reaches this step). Any result that would land mid-tier is raised to **{{TIER_FLOOR}}** (does not lift the lowest tier). Pass this floor to the scoring run.
   - **⛔ Gate precedence:** the tier floor does NOT override the scoring skill's hard gates. If the self-serve gate fires ({{SELF_SERVE_THRESHOLD}}), there is **NO MQL** — post an FYI to the digest: a champion joining a small startup is future pipeline and deserves a personal note from the old account's owner, not a sales motion. Same precedence for vendor/partner, government, VC/PE, and competitor gates.
4. **When scoring lands at or above {{TIER_FLOOR}} with no gate fired, it produces an MQL through its normal flow.** This skill contributes only its provenance markers:
   - Apply the `champion-move` tag to the new company.
   - Ensure the champion exists as a contact on the new company with their LinkedIn URL and a note capturing the prior relationship.
   - The scoring skill's own steps handle the MQL stage move, {{CRM}} sync, buying committee, and the alert. Do not duplicate them; just make sure the champion-move story and the prior-owner relationship are present in the signal so the alert carries them.
5. **Multiple movers to the SAME destination = ONE stronger signal**, scored once. Never fire several MQLs for one company.
6. Prepend to the new company's memory: `[CHAMPION ARRIVED] [date] — [Name] joined as [new title]. Ex-[Old Account] ([qualification reason]). Scored [tier]. MQL: [yes/no + why].`

**C. Carry the champion forward (track serial movers forever):**

A proven mover — someone who already carried {{PRODUCT}} from one company to another — is your highest-value person to keep watching. Their NEXT move is a hotter signal than this one, not colder. The champion travels with the person, not the account.

1. **Add the person to the NEW company's `[CHAMPION WATCHLIST]`** as a live, `carried-forward` entry:
   `- [Name] | [new title] | [email if known] | [LinkedIn URL] | carried-forward: ex-[Old Company] ([original qualification reason]) | last verified [date]`
   This entry is ACTIVE for detection — next month Phase 2 verifies them against the new company and detects their move to a third company, firing a fresh MQL there. The chain continues indefinitely across every future move.
2. **This applies regardless of gate outcome.** Even if the move was FYI-routed or gated (no MQL fired), still carry the person forward — the tracking is about the person's trajectory, not this single company's score. A champion at a tiny startup today may be at a perfect-fit company next year, and you only catch it if you keep watching.
3. The `champion-move` tag on the new company (from B.4) + the active `carried-forward` watchlist entry are what put this company into next month's scan set. Both are required.
4. **Watchlist-rebuild interaction:** the {{REFRESH_WINDOW}}-day rebuild in Phase 1 refreshes an account's OWN champions/heavy users from current {{CRM}} + usage. It must NOT delete `carried-forward` entries — those are tracked people, not native champions of the account, and would never be rediscovered by a {{CRM}}/usage scan. Preserve all `carried-forward` and `MOVED → processed` entries across rebuilds; only refresh the natively-sourced lines.

---

### Phase 4 — Monthly digest

End every run with ONE summary message to {{DIGEST_CHANNEL}} containing: accounts scanned, watchlist size, moves confirmed (with tiers + MQL status), FYI-routed moves (self-serve/gated), UNCERTAIN people needing human review, churn-risk flags (compound departures first), NEEDS-REVIEW routing calls (unsourced funding), and coverage gaps (accounts with no identifiable champion; customer domains with no matching workspace).

---

### Guardrails
- Never fire the MQL flow on UNCERTAIN. False champion-move alerts erode trust in the signal.
- Never send outreach from this skill.
- Credit discipline: this fans out a LinkedIn lookup per watched person monthly. Keep watchlists tight (Phase 1 filters + {{REFRESH_WINDOW}}-day reuse) rather than checking every contact on every account.

## What good looks like

A monthly run reads like a machine, not a hunch: every active watchlist person got a live LinkedIn check; every MOVED classification survived the experience-section read, the affirmative-evidence bar, and the wrong-person guard; warm familiarity never got promoted to champion; a mover into a competitor or a tiny startup produced a memory note and an FYI, not an MQL; one company with three arriving champions fired exactly one scoring run; the old accounts got churn flags (critical when compound); serial movers stayed on watch at their new company; and the digest let a human review every UNCERTAIN instead of the machine guessing. The failure modes this skill exists to prevent: a same-name stranger becoming a hot MQL, a stale headline hiding a move, the same move firing MQLs two months running, and a free-trial signup being treated like an advocate.
