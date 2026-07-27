---
name: "expansion-opportunity-analysis"
title: Expansion opportunity analysis
description: "Use this skill when you want a deep-dive on a single existing customer's expansion potential — not a portfolio scoring pass, but the full account workup: an adoption and health read, a commercial analysis that decomposes their real spend and consumption, and two priced proposals anchored on trailing usage. It ends with a concrete expansion play: which signal pattern applies, who on the buying committee to approach with which role-matched gap, whether the timing is right, and a draft motion queued for human approval. Run it on accounts your scoring or intuition has already flagged as worth the effort."
category: Deals
---

# Expansion Opportunity Analysis

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{EXPANSION_OWNER}}` — Person who owns expansion revenue and approves every play
- `{{CRM}}` — Your CRM (e.g. HubSpot, Attio) — source of closed-won deals and contact records
- `{{BILLING_SOURCE}}` — Your billing/subscription system (e.g. Stripe) — source of truth for plan, price, and purchase history
- `{{USAGE_SOURCE}}` — Your product's usage data (analytics warehouse, admin DB, or usage API)
- `{{USAGE_UNIT}}` — Your consumption unit (credits, API calls, seats, events, records)
- `{{HIGH_UTILIZATION_THRESHOLD}}` — Utilization level that counts as "at the ceiling" (default: 90% of the monthly allocation)
- `{{OVERAGE_MULTIPLIER}}` — Ratio of the on-demand/overage rate to the committed per-unit rate (default: 2.0×)
- `{{CONSERVATIVE_FACTOR}}` — Multiplier on trailing average usage for the conservative proposal (default: 0.90)
- `{{GROWTH_FACTOR}}` — Multiplier on trailing average usage for the growth proposal (default: 1.50)
- `{{COMMIT_DISCOUNT}}` — Per-unit discount for the larger commitment (default: 10%)
- `{{INACTIVITY_WINDOW}}` — No-usage window that disqualifies an account from expansion outreach (default: 30 days)

---

### Overview

A per-account deep dive on an existing customer that ends in a concrete, ready-to-run expansion play. Three parts, always in this order: an account health and adoption read, a commercial and consumption analysis with two priced proposals, and expansion play construction — which signal pattern applies, who to approach, when, and through what motion.

This is analysis and play design for **one account you already suspect matters** — not a portfolio scoring pass. If you need to rank your customer base to decide *which* accounts to analyze, do that first with whatever scoring you use, then run this on the accounts that surface.

**Identify the customer first.** You need at minimum one of: company name, domain, or account ID. If none was given, ask before proceeding.

**Gather everything in parallel, then present one unified output.** Do not stop between parts to ask for confirmation. If any data source is unavailable (no billing record, no closed-won deal), state clearly what was found vs. unavailable and continue with the rest.

---

### Part 1 — Account Health & Adoption Read

Before any commercial math, establish how the customer actually uses the product. Pull from {{USAGE_SOURCE}} and account memory/notes:

1. **What they bought it for** — the original use case, from deal notes and onboarding records.
2. **Setup completeness** — which core capabilities are configured vs. sitting at defaults. **Judge depth by deliberate configuration, not by anything your product auto-creates during onboarding** — auto-provisioned defaults are present on every account and signal nothing.
3. **Active users** — who logs in, how often, and their roles. Note seats used vs. seats included.
4. **Adoption gaps** — the 1–3 highest-value capabilities they are *not* using. These become the whitespace map in Part 3.
5. **Trajectory** — is usage growing, flat, or declining month-over-month?

End Part 1 with a one-paragraph prognosis: healthy-and-growing, healthy-but-shallow, at-capacity, or at-risk.

**⛔ Hard gate:** if there are no usage signals in the last {{INACTIVITY_WINDOW}}, stop treating this as an expansion opportunity. Flag it as churn risk, recommend a save/re-engagement motion instead, and end the analysis after Part 1. Never build an upsell play on a silent account.

---

### Part 2 — Commercial & Consumption Analysis

#### 2.1 Deal history

Search {{CRM}} for the account's closed-won deal(s). Report the close date ("Month D, YYYY"), deal name and amount if populated, and how long ago it closed. If multiple closed-won deals exist, list all and highlight the most recent — prior upsells are themselves a signal.

#### 2.2 Current plan economics

Pull the live subscription from {{BILLING_SOURCE}} — never from a cached mapping table or from memory; plans drift.

**⚠️ CRITICAL — decompose the monthly charge. Do not report the whole invoice as one number.** Most consumption pricing has two components:
- **Platform/base fee** — the flat portion
- **Consumption fee** — {{USAGE_UNIT}} included/mo × per-unit rate

Base fee + consumption fee should reconcile to the total charge. Report them separately, plus: plan name and tier, {{USAGE_UNIT}} included/mo, per-unit rate (4 decimal places), billing cadence, seat count vs. included seats, and subscription start date as a cross-check against the CRM close date. **The included-allocation figure must come from the plan definition** — a live balance field may have overage purchases merged in.

#### 2.3 Plan and seat changes

Check for upgrades since the original purchase: additional closed-won deals, plan-change records in billing, and active user count vs. included seats. Report original vs. current plan, or "No plan or seat changes detected."

#### 2.4 Monthly consumption (current month + prior 3)

Query {{USAGE_SOURCE}} for monthly {{USAGE_UNIT}} consumed:

| Month | {{USAGE_UNIT}} consumed |
|---|---|
| Current month (partial — MTD) | … |
| Month -1 | … |
| Month -2 | … |
| Month -3 | … |

Label the current month "(partial — month to date)", comma-format the numbers, and add a one-line trend note (e.g., "Usage trending up +18% month-over-month").

#### 2.5 Overage / top-up history (last 60 days)

From {{BILLING_SOURCE}}, pull every on-demand purchase beyond the plan allocation in the last 60 days — filter for charges that don't match the recurring subscription amount. Summarize the 60-day total (count and {{USAGE_UNIT}} purchased), then detail the last 30 days:

| Date | {{USAGE_UNIT}} purchased | Cost | Cost per unit |
|---|---|---|---|

Cost to 2 decimals, cost-per-unit to 4. If none in the last 30 days, say so and note any from days 31–60.

#### 2.6 Pricing scenario analysis

Build two proposals anchored on real consumption. **Use the three most recently completed months (exclude the current partial month):**

- **Trailing average** = (Month -1 + Month -2 + Month -3) ÷ 3
- **Option 1 (conservative)** = trailing average × {{CONSERVATIVE_FACTOR}}, rounded to a natural tier boundary — keep the current plan's allocation when usage doesn't clearly warrant a change
- **Option 2 (growth)** = trailing average × {{GROWTH_FACTOR}}, rounded the same way — adjust upward if the trend or a stated roadmap warrants it
- **Option 1 per-unit rate** = mirror the current rate exactly
- **Option 2 per-unit rate** = current rate × (1 − {{COMMIT_DISCOUNT}}), labeled with the discount
- **Overage rate for each option** = that option's per-unit rate × {{OVERAGE_MULTIPLIER}}

**If {{EXPANSION_OWNER}} specifies explicit volumes for either option, those override the formula.**

Present a comparison table with rows: billing interval, platform fee, {{USAGE_UNIT}} included/mo, committed pool (× 12 for annual), per-unit rate, consumption fees, seat add-on, recent overage purchases and fees (Current column only — N/A under both options), **monthly effective spend**, **annualized**, **vs. current run rate** (+/− monthly and annualized), and **blended per-unit rate** (effective spend ÷ total units available). Footnote the trailing-average math so the customer can check it.

**Formatting rules (strict):** dollars to 2 decimals; per-unit rates to 4; units comma-formatted; deltas signed. For the Current column's blended rate, the denominator is plan units + overage units combined.

**Language rule:** when the customer is commitment-averse, frame the proposal as a "bulk purchase" they "draw down" against — a pre-purchased pool with a coverage estimate (pool ÷ their stated monthly need) — and avoid the words "annual," "contract," and "commitment" in that framing. The math is identical; the framing is not.

Close 2.6 with 2–3 sentences describing their current state in plain terms (plan, spend, overage behavior, blended cost per unit) and one tight line on why the proposals beat the status quo — written to their actual numbers, never a template.

---

### Part 3 — Expansion Play Construction

#### 3.1 Match the signal pattern

Test the account against these patterns, in order. Cite the specific data from Parts 1–2 that triggers each match — never generic statements.

| Pattern | When it applies |
|---|---|
| **Repeated overage purchases** | 3+ on-demand purchases within a billing cycle or recent cycles at the standard overage rate |
| **Customer-initiated capacity request** | They proactively asked for more {{USAGE_UNIT}}/seats via any channel — the warmest signal; treat as a commercial conversation, not support |
| **Upgrades + aggressive overage** | 2+ plan upgrades AND multiple overage purchases in the last 90 days — active investment plus overrun |
| **Ceiling hit + roadmap signal** | ≥{{HIGH_UTILIZATION_THRESHOLD}} utilization AND a recent conversation (QBR, product session, support thread) pointing to even higher future usage |
| **Strong relationship, low realization** | A senior stakeholder believes in the product AND has acknowledged under-utilization AND the account runs it as a point tool — the play is use-case expansion, not volume |

If multiple match, rank by fit strength and recommend which to run first. If none match, **do not force one** — propose a new pattern: a title (max 40 characters) plus a precise definition of the qualifying signals and engagement approach (300 characters total). Every analysis must land on a matched pattern or a proposed new one.

#### 3.2 Map the buying committee

- **Champion** — the warmest contact; usually whoever raised their hand or took the recent meeting.
- **Economic buyer** — whoever owns the budget; may not be the champion.
- **1–2 additional stakeholders to thread** — more senior than the champion or peer-level with broader influence.

**Match each target's message to a role-relevant gap from the Part 1 whitespace map:** practitioners get the workflow gap that costs them daily effort; ops roles get the data/process gap; sales/marketing leaders get the pipeline gap; founders/execs get the "point tool vs. platform" framing. A gap must be real and audit-grounded — pulled from Part 1, never inferred generically.

**For relationship-led plays: ⛔ confirm the champion and stakeholder list with {{EXPANSION_OWNER}} before building anything.** Total targets: 1–3 people, each with role-adjusted messaging.

#### 3.3 Judge the timing

- **Go now:** customer-initiated requests (respond same week), ceiling + roadmap signals (the pain is current), and any window right before a renewal or another overage purchase.
- **Wait:** an unresolved support escalation, a champion who just left, or usage that spiked once and reverted — one hot month is not a trend.
- **Don't:** the account failed the Part 1 inactivity gate, or the "expansion" is really a save.

State the recommended timing explicitly, with the reason.

#### 3.4 Design the motion

- **Volume/pricing patterns** → short direct sequence to the champion: an email that names their actual numbers (overage count, rate paid, what the proposal saves), one channel-switch touch, one one-line follow-up. The ask is a conversation, not a signed order.
- **Customer-initiated requests** → acknowledge, then get a call to understand trajectory **before proposing anything**. Never pitch a specific plan or volume in the first reply.
- **Relationship/realization patterns** → multi-threaded: champion + confirmed stakeholders, each touched with their role-matched gap, referencing the warm relationship by name.
- **Every motion ends with an internal escalation step**: if no reply ~10 days after the final touch, notify {{EXPANSION_OWNER}} with a summary of what was attempted and a suggested next move (usually multi-threading or an exec-to-exec touch) — never another message to the customer.

**Hard rules for any outreach this analysis produces:**
- **Never auto-send. Every sequence requires {{EXPANSION_OWNER}}'s explicit approval.**
- **Never leave placeholder numbers in copy intended to send** — every figure comes from Parts 1–2.
- Keep emails to 5–6 lines; no feature lists; the CTA is a meeting.
- Tag the account as having an active expansion play when the sequence launches; clear the tag on reply or close, so no account carries two plays at once.

---

### Output Structure

Present the full analysis in three labeled parts:

**Part 1 — Account Health & Adoption Read** — usage, setup, users, whitespace, prognosis.
**Part 2 — Commercial & Consumption Analysis** — deal history, plan economics, changes, consumption table, overage history, pricing scenarios.
**Part 3 — Expansion Play** — matched pattern with cited signals (or new-pattern proposal), buying committee with role-to-gap mapping, timing call, and the motion with draft copy queued for approval.

---

## What good looks like

A great run reads like a deal memo, not a data dump: the prognosis in Part 1 is a judgment backed by real adoption evidence, the Part 2 tables reconcile to the penny with base fee and consumption fee cleanly separated, both pricing options anchor on the trailing 3-month average with the math footnoted, the matched pattern in Part 3 cites the account's actual numbers ("4 overage purchases at 2× the committed rate in 60 days"), each committee member's draft names a gap that genuinely exists in their setup, the timing call is explicit, and everything queues for {{EXPANSION_OWNER}}'s approval with zero placeholder numbers left in the copy.

Mediocre looks like: the whole invoice reported as "platform fee," proposals sized from the current partial month, a forced pattern match justified with generic statements, outreach drafted to an account that failed the inactivity gate, a committee of one, or a sequence that auto-sends.
