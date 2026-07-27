---
name: "account-tier-scoring"
title: Account tier scoring
description: "Use this skill when you want a production-grade account scoring system instead of a vibes-based one: it tiers every account onto a Bronze/Silver/Gold/Diamond ladder, scoring pre-conversion accounts on intent signals + ACV potential and trials/customers on activation depth + expansion headroom. It encodes the judgment that makes scoring trustworthy — a hard self-serve gate with LinkedIn headcount verification, an enterprise persona gate, anonymous-signal and social-engagement caps, prior-relationship floors, and never-demote rules — with every threshold exposed as a tunable default. Each run produces a verified tier tag and ACV tag, a prepended signal-stack snapshot in account memory, a CRM lead-score sync, and correctly routed Gold/Diamond alerts with per-stakeholder engagement recommendations."
category: Deals
---

# Account tier scoring

Scores any account onto a four-tier ladder — pre-conversion on intent + ACV potential, post-conversion on usage depth + expansion potential. Every run updates the running signal stack in memory, applies exactly one tier tag and one ACV tag, and routes alerts so high-tier accounts reach a human same-day.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{CRM}}` — Your CRM (e.g. HubSpot, Attio, Salesforce)
- `{{ALERTS_CHANNEL}}` — Channel where Gold/Diamond alerts post (your MQL channel)
- `{{ACTIVE_DEALS_CHANNEL}}` — Channel for tier upgrades on accounts a rep is already working (optional; defaults to {{ALERTS_CHANNEL}})
- `{{SALES_OWNER}}` — The rep or founder-seller whose queue Gold/Diamond accounts feed
- `{{PARTNERSHIPS_OWNER}}` — Person to flag agency/partner/investor signals to
- `{{SOCIAL_SELLER}}` — Team member whose LinkedIn profile/posts generate engagement signals (optional; delete LinkedIn rows if unused)
- `{{SELF_SERVE_THRESHOLD}}` — Profile that routes to self-serve instead of being scored (default: <50 employees AND ≤$10M total funding)
- `{{ENTERPRISE_THRESHOLD}}` — Employee count where the enterprise persona gate applies (default: 1,000+)
- `{{BUYER_PERSONA_LIST}}` — Titles with real buying authority for your product (default GTM list: CRO, VP/Head of Sales, VP/Head of Marketing, CMO, CEO, Co-founder, RevOps Lead, GTM Engineer, Growth Lead, Agency Owner)
- `{{DISQUALIFIED_MARKETS}}` — Segments you structurally cannot serve, e.g. compliance-blocked verticals (optional)

**Tier names:** Bronze / Silver / Gold / Diamond is the default ladder. Rename freely — the ordering, gates, floors, and caps are the methodology; labels are cosmetic. Canonical alert emojis: 🟤 ⚪ 🟡 💎.

### ⚠️ Optional EVAL mode (recommended for the first 1–2 weeks)

While evaluating output quality, run with {{CRM}} writes disabled: skip every "write/update in {{CRM}}" step and instead include the exact tag, stage, and note text that WOULD have been written in the alert post. Memory writes stay ON either way. Once you trust the tiers, follow the steps as written.

---

### Overview

Every scoring run produces two labels:
- **A tier tag** (`tier: bronze|silver|gold|diamond`) — how strong is the case for human attention right now. Bronze is the floor.
- **An ACV tag** (`high-acv-potential` / `medium-acv-potential` / `low-acv-potential`) — how big could this account get. Assessed once per run, before tiering, and consumed by the tier rules.

Scoring mode follows lifecycle stage: customers score on usage + expansion headroom, trials on activation depth, pre-conversion accounts on intent, and zero-signal accounts get an ACV assessment only (no tier, no alert). Two reference pages carry the detailed rules: the **Intent scoring reference** and the **Trial scoring reference**.

---

### Global rules (every scoring run)

**Tiebreaker rule.** When an account is genuinely borderline between Silver and Gold, default to Gold — {{SALES_OWNER}} would rather review a Silver-quality account than miss a real one. The tiebreaker does NOT apply when all signals are third-party: high third-party volume is not "borderline" — an account with only post engagement is Silver, full stop.

**Enterprise persona gate ({{ENTERPRISE_THRESHOLD}} employees).** At large accounts, a single signal from a non-buyer persona (IC, ops specialist, junior title without buying authority) caps at Silver — regardless of how strong the company looks on paper. Anonymous signals count as non-buyer persona here: even stacked anonymous pricing-page visits stay Silver. Gold requires either (a) a named, verified senior stakeholder on {{BUYER_PERSONA_LIST}} (or equivalent VP+/C-suite/budget-holding Director), or (b) 2+ distinct first-party signals from named people. The tiebreaker never overrides this gate — a single junior contact at a large org has no realistic path to a buying conversation; Silver holds until there's a senior entry point or real volume.

**Never demote on a weak new signal.** Score the full signal stack from account memory, not just the incoming event. A new low-weight signal on an account that previously scored higher never lowers the tier. Demotion happens only through this skill's explicit gates (self-serve, disqualified market, vendor reclassification) or a deliberate periodic review — never as a side effect of routine scoring.

---

### ⛔ Self-serve gate — runs before everything else. No exceptions.

Check two things before any other step:

**1. Employee count** — take the LOWER of the enrichment-provider count and the company's LinkedIn count. Enrichment providers return bucketed ranges whose midpoints inflate small-company headcount — exactly how a 27-person shop gets mis-scored as a Gold MQL. If the enrichment count is unavailable, a range, or resolves near the threshold (default: under 3x the floor), verify against the company's LinkedIn page first. Never skip the verification in the risk band to save a lookup — a wrongly-promoted account wastes far more rep time than the check costs.

**2. Funding** — total raised. Meaningful funding (default: >$10M) AND headcount at/above the floor together skip this gate. Funding alone never overrides the employee floor — a small team with big seed capital still routes to self-serve; runway is not a buying motion.

**If the account meets {{SELF_SERVE_THRESHOLD}}:** remove any tier tags, apply `self-serve` plus the Bronze floor tag, move the account to your self-serve stage (mirroring it in {{CRM}} if you sync stages), and note the gate in the state summary. Then **⛔ STOP — no scoring, no alerts, no buying committee, no outreach** — regardless of how strong the signals look. A CEO hand-raise, stacked profile views, direct replies: none change the employee count. Small accounts do not belong in {{ALERTS_CHANNEL}} or {{SALES_OWNER}}'s queue.

**Edge cases:**
- **Subsidiaries:** the funding override applies to the legal entity itself, not a parent. A 6-person subsidiary of a unicorn is still self-serve — default to what the entity can buy and approve independently.
- **Count unavailable:** unknown headcount + no confirmed funding → gate by default (funded companies almost always show in enrichment). Override only when ALL hold: established web presence, a description strongly implying a team above the floor, and funding genuinely unknown rather than zero.
- **Geo data-quality flags:** where your enrichment is known-unreliable, require LinkedIn verification at a higher threshold and gate by default when you can't verify.
- **Borderline band:** resolved count within ~10 employees of the floor (either side) → never auto-launch outreach in {{SALES_OWNER}}'s name; get explicit approval first, even if the account passed.

---

### Step 0 — Exclusion checks

In order; each is a hard stop when it fires.

**0a. Vendor/partner check.** Check BOTH tags (vendor, partner, or equivalent non-prospect label) and funnel stage — they are not always in sync. If either matches: do not score. Update memory with the signal that fired (what, when, who — vendors aren't scored, but their record stays current), set the state summary to "Vendor/partner — scoring skipped," post a 3–4 sentence note to {{PARTNERSHIPS_OWNER}}, and stop.
> **Exception — signup/trial events:** do NOT hard-stop — known partners and agencies can also be real buyers. Score in full, flag the partner status to {{PARTNERSHIPS_OWNER}}, surface in {{ALERTS_CHANNEL}} if Gold/Diamond. All other signal types on confirmed partners still hard-stop.

**0b. Disqualified markets.** If the account's customer base is primarily in {{DISQUALIFIED_MARKETS}} (flag when 2+ independent signals confirm: positioning language, listed customers, compliance credentials, segment-specific job requirements), move it to your unqualified stage, set the state summary with the specific blocker, log the reasoning, and stop. Delete this step if you have no blocked segments.

**0c. Investor firms.** If the account's primary business is managing a fund or making investments (VC, PE, angel syndicate, family office), do not score. Log the signal, move to your potential-partner stage, and post a short note to {{PARTNERSHIPS_OWNER}} with fund size and portfolio count if known — investors are a partnership play, not a deal. Stop.

---

### Step 1 — ACV assessment

Run for every account that reaches this step. Evaluate all six dimensions with judgment — no single one is a hard gate; weight the whole picture. Defaults are tuned for a mid-market B2B GTM product; recalibrate to your price points.

1. **Employee size.** Relevant range ~30–3,000. Below: self-serve territory (already gated). Above ~3,000: enterprise motion — very high ceiling but multi-stakeholder work to unlock.
2. **Buyer-team size.** For a GTM product: dedicated sellers. <3 = low ceiling (founder-led); 3–15 = medium; 15–50 = high (scaled team). Substitute the team your product serves.
3. **Team maturity.** Strongest to weakest: dedicated leadership (VP/CxO of the function), mid-level management, active ICs, a supporting ops function. The fuller the pyramid, the higher the ceiling.
4. **Inbound maturity.** Meaningful traffic, blog/SEO investment, content roles, PLG motion (most advanced). Low inbound doesn't disqualify — it just signals a less sophisticated buyer.
5. **Funding.** $10M+ = validated budget; $30M–$99M should resolve to `high-acv-potential` in most cases; $100M+ = enterprise-scale budget.
6. **Hiring signals** — what problem are they solving right now? Ops/infrastructure roles for the team you serve = highest signal (building before the stack locks in — ideal adoption window). Volume IC hires = strong (scaling pain). Leadership hires = context, but lower alone (new leaders slow motion during ramp).
**Output — apply exactly one ACV tag, removing any previous one first**, and commit the write immediately (never batched with the tier tag later): `high-acv-potential` (majority of signals high; clear budget authority and scale), `medium-acv-potential` (mixed), `low-acv-potential` (most signals low). Verify by re-reading the record; retry once; if still missing, note the failure in memory — never report a tag as applied that wasn't confirmed.

**When a human explicitly asks for an ACV assessment, show your work:** the full six-dimension table — your signal for each, which pointed high, which pulled it back. Never just state the tag; the reader must be able to independently agree or challenge.

---

### Step 2 — Prior-relationship floor (closed lost / trial alumni)

If the account is in Closed Lost OR previously trialed your product, apply a **Gold floor**: any signal that would otherwise score Silver is raised to Gold — re-engagement after a real prior evaluation outweighs cold engagement.

**⛔ Genuine-evaluation gate — verify first.** The floor's premise — "they evaluated us and didn't convert" — isn't always why an account is Closed Lost. Apply it only when at least one exists: a prior deal in {{CRM}} (any stage), a logged sales touchpoint (demo, call, meeting, real email thread), or a prior trial record. If Closed Lost happened for a non-buying reason (a vendor selling INTO you, a mis-tag, disqualified without evaluating), score current signals on their merits. When in doubt, don't apply the floor.

**Limits:** lifts Silver→Gold only, never Bronze→Gold; Step 0 hard stops still apply; and it never overrides the self-serve gate — a sub-threshold account's ceiling is too low for Gold routing no matter the history.

---

### Step 3 — Route by lifecycle stage

In this order:
1. **Paying customer (Closed Won)?** → Customer expansion scoring (below)
2. **On trial?** → Load the **Trial scoring reference**
3. **Any first-party intent signal?** (website visit, chat, completed meeting, outreach reply, LinkedIn profile view or post engagement on {{SOCIAL_SELLER}}) → Load the **Intent scoring reference**
4. **None** → No-signal handling (below)

**LinkedIn caps (full rules in the intent reference):** a profile view is medium-high weight; post engagement is Silver-level alone at any volume. A profile view as the ONLY first-party signal caps at Silver; stacked with another high-intent first-party signal it qualifies for Gold — but only when the viewer is on {{BUYER_PERSONA_LIST}}. A weak-persona viewer with stacked signals: keep Silver and target a buyer persona from the buying committee (Step 6), never the junior viewer.

#### Customer expansion scoring (paying accounts)

Goal: how deeply are they using the product, and how much bigger could this account get? Signal stack, strongest first: (1) **meetings** — extract expansion topics, new departments/use cases, budget conversations; (2) **product depth** — integrations connected beyond defaults, workflows built beyond defaults, usage-unit consumption, multiple active users. *Anything auto-created at onboarding counts for nothing — judge depth only by what users deliberately built;* (3) **support/chat questions** about advanced use cases; (4) **return website visits** (pricing = upgrade signal); (5) **social engagement** = advocacy. Then assess **expansion headroom**: current seats vs. addressable team size (from the ACV assessment), untouched divisions, growth signals, proximity to plan limits.

**Hard cap:** no product usage in the last 30 days → cap at Silver; churn risk takes priority over expansion — flag it explicitly. **Senior-stakeholder exception:** an active VP+/C-suite user at a high-quality company ($10M+ funded, 100+ employees, or a known brand) scores Gold regardless of team size — seniority + company quality is itself an expansion signal.

**Tiers:** Diamond = deep multi-user usage + high ACV + clear 3–5x ARR headroom; Gold = meaningful usage + medium-to-high ACV + some headroom; Silver = shallow usage or low ceiling; Bronze = barely active — re-engage before expanding.

#### No-signal accounts (ACV assessment only)

For accounts with zero first-party signals (typically list-loaded prospects): confirm no signal exists (if one does, re-route to intent scoring), sanity-check the ACV tag against firmographics (flag inconsistencies; don't re-run), confirm the funnel stage is an early/target stage. **No tier, no alert, no committee enrichment** — write the memory snapshot (Step 5) and stop. Zero-signal accounts never generate noise.

---

### Step 4 — Apply the tier

*(Skip for no-signal accounts.)* The tier tag write happens FIRST — before CRM sync, memory, or any alert.

1. **Write:** remove all four tier tags, apply the one scored. Bronze is the floor — every scored account carries exactly one tier tag.
2. **Verify:** re-read the record and confirm the tag. Not found → retry once → re-verify. Track `TIER_TAG_STATUS = VERIFIED | FAILED` through Steps 5 and 7 — never silently continue as if a failed write succeeded.
3. **Expansion-target flag (post-conversion only):** Diamond — or Gold with explicitly flagged strong headroom — also gets an `expansion target` tag.
4. **Sync to {{CRM}}:** write the tier to your lead-score field on the company record, exact casing. Record not found → skip and note in memory.

---

### Step 5 — Update account memory

Prepend a full snapshot to the top of the account's memory — preserve all history below; the running stack is what future runs score. Header: `[SCORE: tier] [Mode: Intent|Trial|Expansion] — date` (or `[ACV ASSESSMENT ONLY — No Signals] — date`). Body by mode — **Intent:** signal stack strongest-first, persona quality (Strong/Weak/Mixed + why), buyer-team size, maturity signals, ACV tag + 1-sentence reason, hard caps applied (or None). **Trial:** product usage (integrations, workflows, multi-user, last-30-days), persona quality, conversion signals, ACV, caps. **Expansion:** product usage, persona quality, expansion headroom, **churn risk — flag any 30-day usage gap explicitly**, ACV, caps. **No-signal:** ACV tag, team size, maturity signals, 1–2 sentence reasoning.

Also set the one-line state summary: `[SCORE: tier] [Mode] — [what drove it]`, appending `⚠️ TIER TAG WRITE FAILED — tag not persisted` when `TIER_TAG_STATUS = FAILED`.

---

### Step 6 — Buying committee enrichment

*(Skip for no-signal and Bronze accounts.)* Check contacts in {{CRM}}. Sufficient = 3+ contacts matching {{BUYER_PERSONA_LIST}} with LinkedIn URLs or emails — note "already populated" and move on. If thin: research leadership matching your buyer personas, **always including the specific person who triggered this run** (resolve their title and profile), add/update the contacts in {{CRM}}, and append the names to the memory entry.

---

### Step 7 — Alerts and routing

**Bronze or Silver → no alert. No channel post, no DM, no task. Stop here.** Silver is a holding tier, not an alert tier — this discipline keeps {{ALERTS_CHANNEL}} readable.

**Gold and Diamond:** post to {{ALERTS_CHANNEL}} in your team's standard lead-scoring alert format — one channel, one format; never invent a custom layout per signal type. The actions-taken section must reflect `TIER_TAG_STATUS` honestly: "written and verified" only when verified; on FAILED, say the write failed after retry and needs a manual fix. Follow with a short briefing: relationship history in 1–2 lines from {{CRM}} engagements and meeting records ("Discovery call Mar 14, closed lost, no contact since"); known contacts with titles; exec stakeholders not yet engaged; an opinionated recommendation per stakeholder.

**"Already being worked?" check:** is {{SALES_OWNER}} already actively on this account — an open deal in {{CRM}} plus a recent logged touchpoint? Yes → post the upgrade to {{ACTIVE_DEALS_CHANNEL}} as one line (company, domain, tier, trial end date if applicable, the single signal that drove it). No → {{ALERTS_CHANNEL}} as pipeline generation.
> **⚠️ Self-artifact guard:** on signup/trial-start events, the run itself may have just created the deal, tags, or owner assignment. Never count artifacts created in the current execution as evidence the rep is engaged — a deal counts only if its create-date predates this execution, a touchpoint only if logged in the prior 90 days. Only self-created "evidence" → pipeline generation.

**Trial tier upgrade to Gold/Diamond:** draft (never auto-send) outreach from {{SALES_OWNER}} to the primary trial user — whoever built the most or holds the highest role — personalized with the actual signal stack (usage volume, workflows built, days active, trial end date). Queue for explicit approval; skip if an unsent draft exists; if {{SALES_OWNER}} is out of office, flag a teammate.

**Agency check (after routing):** if the account is an agency/consultancy in your space, flag it to {{PARTNERSHIPS_OWNER}} in 3–4 sentences (company, domain, what they do, tier, triggering signal) as a potential partner. On signup/trial events this fires at every tier; otherwise Gold/Diamond only.

---

## What good looks like

A great run is one where every gate fired before any judgment call: the self-serve gate caught the 30-person company before its CEO hand-raise reached {{ALERTS_CHANNEL}}, headcount was verified against LinkedIn because enrichment said "51–200", the enterprise gate held a lone anonymous pricing visit at a 5,000-person company to Silver, and the ACV tag was written and verified before tiering began. The tier is defensible from the memory snapshot alone — signal stack strongest-first, persona quality named, every cap or floor stated explicitly. Gold/Diamond alerts land in the right channel, report tag status honestly, and close with per-stakeholder recommendations a rep can act on in 60 seconds. Bronze and Silver stay silent.

Mediocre looks like: a small account scored Gold because signals "felt strong"; enrichment headcount trusted at face value near the threshold; an anonymous visit lifted to Gold by the tiebreaker; a tier justified by the last event instead of the full stack; Silver accounts generating alerts; a demotion sneaking in on one weak signal; or an alert claiming "tag applied" over a failed write.
