---
title: Intent scoring reference
description: (reference)
---

# Intent scoring reference

Use when the account has at least one first-party intent signal (website visit, chat interaction, completed meeting, outreach reply, LinkedIn engagement) and is NOT yet a customer or on trial.

Goal: how strong is the buying intent, and does it combine with the ACV potential the parent already assessed? The parent has already run the ACV assessment and applied the ACV tag — reference those results, do not re-research them.

---

### Step 0 — ICP fit check

**Evaluate ICP fit by motion and use case, not by industry label.** Load your ICP definition, then ask: does this organization run — or need to run — the workflow your product serves? Do NOT disqualify a company just because its industry is unfamiliar or it doesn't look like your typical customer; adjacent motions (e.g. for a sales product: partnerships/BD, franchise development, recruiting firms, investor sourcing) often qualify.

**Hard disqualifiers (Bronze regardless of signals):** no plausible use case for your product's core workflow; clearly wrong persona; bot traffic. When in doubt, look at what the specific person who reached out actually asked. Classify Bronze only if you can articulate WHY your product can't help them — never just because the industry is unfamiliar.

---

### Step 0.5 — Signal source verification

Before weighting signals, verify the people behind them actually work at the company being scored. For every named individual in the signal log:

1. Email domain matches the company's primary domain → **Verified** — count normally
2. Domain does NOT match → **Unverified** — exclude from scoring, flag in your reasoning
3. No email available → **Low confidence** — count at half weight, note explicitly

**Domain-mismatch cap:** if more than 50% of named signals are Unverified, hard-cap at Silver regardless of what remains, and say so in the output: "Capped at Silver — majority of signals from contacts with unverified domain affiliation."

---

### Signal stack (highest to lowest weight)

Gather ALL available signals from account memory, {{CRM}}, and the incoming event — score the stack, not the last event.

1. **Completed meeting** — the strongest possible intent signal. Extract topics, questions and objections, action items, attendee roles, sentiment. A meeting covering pricing, use cases, or technical evaluation = very high weight.
2. **Product signal** — registration, trial start, integrations connected, active usage, multiple team members signing up. **Exhausting a trial usage limit before the trial ends is a Diamond-level signal** — it proves high-volume active usage under real constraint; when present, treat product weight as maximum and bias strongly toward Diamond.
3. **Chat/support interaction** — what did they ask? Was there commercial intent?
4. **Website visit** — pages, session depth, recency, repeats. Pricing or demo pages = strong intent.
5. **LinkedIn profile view on {{SOCIAL_SELLER}}** — an intentional research act, not passive engagement. Weight: medium-high, comparable to a website visit and materially stronger than a post like. The persona multiplier applies heavily — a buyer-persona title viewing is among the strongest single signals short of a meeting. Repeat views stack: check memory for prior views from the same company and note the count. Note connection status (connected = warmer follow-up research; not connected = cold but intentional). **ACV rule (hard):** a profile view contributes toward Gold only at medium or high ACV potential; at `low-acv-potential` it stays Silver even with a strong persona. **Lone-view cap (hard):** a profile view as the ONLY first-party signal caps at Silver regardless of ACV or persona — Gold requires it stacked with a second first-party signal.
6. **LinkedIn post engagement** — likes/comments on {{SOCIAL_SELLER}}'s posts. Lowest weight; a substantive comment beats a like. **Silver-level on its own at any volume — post engagement alone never satisfies the Gold threshold.**

The more signals stacked, the stronger the case.

---

### Persona quality

**Strong:** titles on {{BUYER_PERSONA_LIST}}. **Weak:** functions outside the buying motion (e.g. product, engineering, finance for a GTM product) — need stronger signals elsewhere to compensate. **Multiple buyer personas from the same company** = significant positive multiplier. Persona quality is a multiplier: a weak signal from a strong persona outweighs a moderate signal from a weak persona. Always name the persona role in your reasoning.

---

### Hard caps

**Enterprise persona gate** ({{ENTERPRISE_THRESHOLD}} employees — enforced from the parent): a single non-buyer-persona signal caps at Silver regardless of ACV fit or intent strength. Anonymous, company-level-only signals count as non-buyer persona — stacked anonymous visits, even to pricing, stay Silver at enterprise accounts; the tiebreaker never applies to them. Gold requires a named, verified senior buyer persona OR 2+ distinct signals from named individuals. Apply before the tier definitions and note it explicitly.

**Fewer than 3 dedicated members of the buying team** (e.g. sellers, for a GTM product): maximum tier Silver, with two overrides —
- **Founder/C-suite registration at a real business** (default: >$5M estimated revenue): the economic buyer walked in the door themselves — score normally and note the override.
- **Meaningful funding** (default: >$10M raised): score normally and note the override.

**First-ops-hire timing modifier:** a company hiring its FIRST ops/infrastructure function for the team you serve is at exactly the right maturity stage — building infrastructure before the stack locks in. Treat as equivalent to 1–2 additional intent signals (same weight as a pricing-page visit). It does not override the <3 cap, but pushes the score to the top of the eligible tier.

---

### Tier definitions

**Bronze is the floor — every account receives a tier; there is no "no tier" outcome.**

**Diamond:** strong intent (product engagement or chat with clear buying intent) + high ACV potential. **Persona + ACV override:** a registration by a C-suite/founder title at a `high-acv-potential` account scores Diamond rather than Gold — the economic buyer arriving unilaterally is materially stronger than a standard signup. Note the override explicitly.

**Gold:** a known, identity-resolved person showing clear buying motion (pricing/demo visit, commercial chat questions, light product engagement, registration, direct outreach reply, or a profile view stacked with a second first-party signal per the ACV and lone-view rules above) + medium-to-high ACV potential. Anonymous visits alone never qualify. Gold requires at least one first-party signal; post engagement alone never qualifies.

**Silver:** ICP confirmed but signals light or anonymous (single visit, post like, anonymous pricing visit), OR strong signals but a low ACV ceiling.

**Bronze:** outside ICP, or marginal fit + weak signals + low ceiling. Includes noise (accidental visits, wrong persona, bots). Log and monitor only.

---

### Output

Produce: tier + 2–3 sentences of reasoning — signals present, persona quality, ACV ceiling from the parent, and what drove the decision (including any cap or override applied). Then return to the parent skill's apply-the-tier step.
