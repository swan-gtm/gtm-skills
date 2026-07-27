---
title: Trial scoring reference
description: (reference)
---

# Trial scoring reference

Use when the account is on an active trial.

Goal: how deeply are they activating, and are they on a path to convert? The parent has already run the ACV assessment and applied the ACV tag — reference those results, do not re-research them.

---

### Signal stack (highest to lowest weight)

Gather all available signals from account memory, product event history, and {{CRM}}.

1. **Completed meeting during the trial** — active evaluation. Extract: use cases explored, objections, integration questions, timeline, attendee roles, sentiment. A meeting covering specific workflows they want to build, or pricing = high conversion signal.
2. **Product depth** — the real indicators of activation:
   - **Integrations/tools connected beyond defaults** — each one is deliberate setup effort
   - **Workflows/automations built beyond what onboarding creates** — variety and count show how much they're actually building
   - **Usage-unit consumption** (credits, runs, API calls — whatever your product meters) — volume and rate reflect engagement intensity. **Exhausting the trial's usage limit before the trial ends is a Diamond-level signal** — high-volume active usage under real constraint. Note it explicitly.
   - **Multiple team members active** — multi-user adoption during trial is one of the strongest conversion signals
   > **What does NOT count as depth:** anything your product auto-creates at onboarding (default workspaces, sample workflows, starter automations) is present on virtually every account. Never treat it as engagement. Judge depth only by what users deliberately built.
3. **Chat/support interactions** — technical or workflow-specific questions signal someone actively trying to build
4. **Post-signup website visits** — return visits to docs, pricing, or feature pages signal active evaluation
5. **Social engagement** — engagement with {{SOCIAL_SELLER}}'s content during trial signals relationship building

---

### Persona quality

**Strong:** titles on {{BUYER_PERSONA_LIST}}. **Weak:** functions outside the buying motion — need stronger product signals to compensate. **Multiple buyer personas signed up during the trial** = significant multiplier; multi-threading early is among the strongest conversion signals. Persona quality matters for both conversion likelihood and post-conversion expansion — always note the role and the number of active users.

---

### Hard caps, floors, and exceptions

**Fresh-trial exception:** if the trial started fewer than 14 days ago AND usage is thin, do NOT cap for inactivity — early-trial quiet is expected. Score on ACV potential and persona quality alone during this window, and say so: "Fresh trial (<14 days) — inactivity cap bypassed."

**Inactivity cap:** no product usage in the last 30 days AND the trial is past the fresh window → cap at Silver. Inactivity during an active trial is a conversion-risk signal — flag it: "30-day inactivity during active trial — capped at Silver, conversion risk flagged."

**High-ACV floor:** if the parent assigned `high-acv-potential`, the minimum tier on trial is **Gold** — regardless of usage depth, persona confidence, or single-threaded status. The fresh-trial exception waives inactivity; this adds the ACV-backed floor on top. **Precedence:** the 30-day inactivity cap beats this floor — an inactive high-ACV trial caps at Silver with the conversion-risk flag; re-apply the Gold floor when activity resumes.

**Senior-stakeholder exception:** if the registered user is VP/SVP/C-suite (or a budget-holding Director) AND the company is high quality (default: $10M+ funded OR 100+ employees OR a known brand with a clear buying motion), score **Gold regardless of team size or single-threaded status** — this person can unlock budget and teammates.

---

### Tier definitions

**Diamond:** deep activation — multiple integrations connected, multiple deliberately built workflows running, multi-user, heavy usage — plus high ACV potential. Clear path to conversion and expansion.

**Gold:** meaningful activation (1–2 integrations, active workflows, regular usage) + medium-to-high ACV potential. Engaged trial; nurture toward conversion.

**Silver:** active trial but shallow activation (minimal integrations, single user, little built, low usage) OR low ACV potential with a limited ceiling. Monitor and support.

**Bronze:** barely active — minimal or no usage, no integrations, low ACV potential. Prioritize re-engagement or a trial extension before writing off.

---

### Output

Produce: tier + 2–3 sentences of reasoning — activation depth, persona quality, usage volume, ACV ceiling from the parent, conversion likelihood, and any cap/floor applied. Then return to the parent skill's apply-the-tier step.
