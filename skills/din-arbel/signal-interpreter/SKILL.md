---
name: "signal-interpreter"
title: Signal interpreter
description: "Use this skill when interpreting a raw GTM signal — a business event or an intent spike — into relevance, meaning, strength, confidence, category, why-now, and open questions, before any tiering or routing happens. It is a pure interpretation layer with no side effects: it never assigns tiers, chooses actions, sends alerts, or writes memory."
category: Signals
---

# Signal Interpreter

_Pure interpretation layer for GTM signals — returns relevance, meaning, strength, confidence, category, why-now, and open questions. No tier math or memory writes. Runs before your tier-scoring stage._

---

## Template placeholders

- `{{COMPANY_NAME}}` — Your company's name.
- `{{ICP_DOMAIN}}` — The operational world your product lives in: the set of activities, asset types, workflows, and regulatory contexts where a prospect's signal becomes relevant to you. Define it as a concrete list, not a category label. E.g., for a digital-asset custody company: digital assets, stablecoins, treasury flows, tokenized assets, crypto/payment infrastructure, wallet governance, custody, compliance, cross-border settlement, and regulated financial services. Write yours with the same specificity — this list powers the Relevance Gate and every strength/confidence judgment below.
- `{{ICP_VOCABULARY}}` — The specific operational-complexity vocabulary of your domain, used to phrase business implications. E.g., for the same custody company: wallet governance, transaction policy, treasury movement, custody, compliance workflows, settlement operations, approval flows, key management.

Worked examples throughout use the digital-asset custody domain (the domain this skill was battle-tested in) — substitute your own everywhere.

---

### Purpose

This skill is the **interpretation layer** between a raw GTM signal and downstream routing. It explains what a signal likely means, why it matters, what should not be assumed, how strong the signal is, and how confident we are.

It is **pure interpretation and has no side effects.** It does NOT assign tiers, decide actions, choose channels, send alerts, create tasks, or write memory:
- **Tier math** (tier, boosters, reducers, caps, ACV, accumulation, decay, market modifiers, tier action) -> your tier-scoring stage.
- **Routing, alerts, memory writes** -> your signal post-processing/routing stage.
- **Outreach angle / messaging** -> your messaging and lead-routing stages.

Flow: the calling trigger (or your post-processing stage) runs enrichment + identity resolution, calls this skill, receives a structured interpretation, then passes it to your tier-scoring stage. This skill returns data only.

It does not replace your ICP qualification step.

---

### What the Calling Trigger Must Pass In

Before running this skill, the calling trigger must collect and pass:

- signal_type: "business_event" or "intent_data" (a topic-intent spike from a third-party intent-data provider, e.g. Bombora)
- event_details: description of what happened (event type, announcement text, topics, dates)
- company_name and company_domain
- icp_segment: the segment classification if known, or "unclassified"
- icp_verdict: "pass" | "borderline" | null - passed from your ICP qualification step. If "borderline", apply a lower confidence floor: Confidence cannot exceed Medium regardless of signal quality, and treat segment/persona as provisional hypotheses. If null, ICP has not been formally confirmed - cap Confidence at Medium regardless of signal quality, and add to Open Questions: "ICP not formally qualified - confirm segment fit before outreach."
- enrichment_data: any company enrichment available (description, headcount, funding, tech stack, HQ)
- account_memory: current content of account memory if it exists - for interpretation context only (e.g. what prior signals reveal about the company's motion). Do NOT compute accumulation upgrades here; your tier-scoring stage owns that.
- intent_corroborating_signals: for intent-data signals only - list any other signals present (website visits, business events, CRM activity, closed-lost history)

The following may also be passed and are useful context for interpretation, but this skill does not act on them (your tier-scoring and post-processing stages do): crm_stage, account_owner, active_pipeline, recent_outreach.

---

### Step 1 - Relevance Gate

Before interpreting the signal, apply the core relevance test:

"Does this signal create or reveal operational complexity that {{COMPANY_NAME}} can help solve?"

{{COMPANY_NAME}}'s world is {{ICP_DOMAIN}}.

- If the answer is clearly no -> stop. Return `relevanceVerdict: not_relevant` with a one-line reason. Do not interpret further. **Write nothing** - your post-processing stage writes the dedup note.
- If the answer is yes or possibly yes -> set `relevanceVerdict: relevant` and continue.

Note: `icp_verdict: "borderline"` does not affect this gate. The Relevance Gate applies equally to Pass and Borderline companies. A Borderline company with a clearly irrelevant event still fails the gate and returns `not_relevant`.

---

### Step 2 - Signal Type Routing

Load the appropriate sub-section based on signal_type:

- For "business_event" -> follow the Business Event Interpretation section below
- For "intent_data" -> follow the Intent-Data Interpretation section below

---

### Business Event Interpretation

#### What makes a Business Event strong

A business event is strong when it suggests the company is moving, managing, securing, scaling, or operationalizing something inside {{ICP_DOMAIN}}.

Strong events (worked examples from the digital-asset custody domain — translate each pattern into your own):
- Funding tied to the infrastructure and operations of {{ICP_DOMAIN}} (e.g. payments infrastructure, stablecoins, digital asset ops, treasury, tokenization, compliance, custody, cross-border settlement)
- Product launches involving {{ICP_DOMAIN}} capabilities (e.g. stablecoins, wallets, custody, tokenization, payment infrastructure) - not generic launches
- Partnerships with players in {{ICP_DOMAIN}} - only when the partnership implies operational use, not just marketing
- Regulatory approvals enabling activity in {{ICP_DOMAIN}} (e.g. crypto, digital assets, stablecoins, custody, EMI, VASP, MSB, broker-dealer, tokenization, cross-border financial services)
- Market or corridor expansion inside {{ICP_DOMAIN}} (e.g. payments, stablecoins, remittances, treasury, digital assets, cross-border settlement)
- Strategic leadership hires who would own the pain in {{ICP_DOMAIN}} (e.g. Head of Payments, Stablecoins, Digital Assets, Treasury, Compliance, CRO, CFO, COO, or product leaders for the relevant infrastructure) - CFO alone is medium signal and requires supporting context to reach high
- Hiring clusters across the operational functions of {{ICP_DOMAIN}} (e.g. blockchain engineering, payments ops, stablecoin ops, compliance, risk, treasury, wallet infrastructure, product infrastructure) - clusters score higher than single hires

Mostly noise unless supported by other context:
- Generic funding with no relevant use of proceeds
- Generic executive hires with no {{ICP_DOMAIN}} connection
- Broad partnerships with no operational implication
- Brand or marketing launches, consumer app features unrelated to your domain
- Awards, events, PR, podcasts, thought leadership
- Hiring for general sales, HR, marketing, or unrelated engineering
- Domain keywords used only as marketing language (e.g. "blockchain" as buzzword)

#### Signal Strength for Business Events

High: The event explicitly and specifically describes activity in {{ICP_DOMAIN}} - e.g. a stablecoin product, relevant license, wallet infrastructure, custody, tokenization, treasury scale-up, or direct payment infrastructure expansion. The connection to operational complexity is stated, not inferred.

Medium: The event is in a relevant area but the operational implication requires inference. E.g. a PSP launching "crypto payments" may create complexity - but whether it involves wallet governance, custody, or treasury movement must be inferred.

Low: The company is relevant but the event itself is generic or tangentially connected to {{ICP_DOMAIN}}. A new CFO at a fintech with no other context. A funding round with no stated use of funds.

Report **raw Signal Strength for the current signal only.** Do not upgrade for prior signals or accumulation - your tier-scoring stage applies accumulation upgrades.

#### Confidence for Business Events

High: The operational complexity is explicitly described in the announcement or event data. We are not inferring - we are reading it.

Medium: The event is in a relevant area and the implication is reasonable, but not stated directly. We are making a well-reasoned inference.

Low: The company is interesting but the event is vague, or the connection to {{ICP_DOMAIN}} requires multiple inferential steps.

Strength-shaping guidance (describes signal quality - your tier-scoring stage owns the hard caps):
- **Funding:** Strength is driven by use-of-funds specificity, not round size. Explicit {{ICP_DOMAIN}} language (e.g. custody, stablecoin payments, wallet infrastructure, tokenization, treasury management, compliance/AML, digital asset operations) -> can reach High. Adjacent language (general fintech, crypto, "payments") without an explicit {{ICP_DOMAIN}} connection -> Medium max. No use-of-funds stated -> Low, always.
- Product launches score on operational relevance, not PR importance.
- Hiring clusters score higher than single hires on both Strength and Confidence.

#### Hiring Signal Corroboration (when called by a hiring-signal analyzer stage)

When called by an upstream hiring-signal analyzer, the input includes a `corroboration` field and a `Business Initiative Hypothesis` in event_details. Use these to sharpen interpretation:

**Business Initiative Hypothesis - interpretation scaffolding only:** A well-formed hypothesis (Initiative + Operational Need + {{COMPANY_NAME}} Fit) helps articulate the operational implication. It is analytical scaffolding, not corroborating evidence - your tier-scoring stage decides tier caps and whether corroboration exists.

**Corroboration context (from the `corroboration` field)** - reflect these in Likely Meaning / Business Implication:
- Job signal + website visit on high-intent page -> strongest combination. The company is actively building AND researching solutions.
- Job signal + funding event (last 60 days) -> capital to deploy + the hire to deploy it.
- Job signal + intent-data spike in {{ICP_DOMAIN}} -> category interest corroborated by a concrete build signal.
- Job signal + competitor engagement -> they are evaluating; this hire will own the decision.
- Job signal + prior job signal in same domain (last 60 days) -> cluster forming.
- Job signal alone -> interpret on its own merits; note the lack of corroboration in What Not To Assume.

**Why Now discipline for hiring signals:** A job posting alone rarely produces a concrete "Why Now" - avoid manufacturing urgency. Valid Why Now sources: the posting is <7 days old; a corroborating signal (funding close, product launch, license grant) provides a real deadline; the JD states a timeline ("to support our Q3 stablecoin launch"); the role is the first of its kind (greenfield). If none are present -> Why Now = null. Do not force it.

---

### Intent-Data Interpretation

#### What makes intent data actionable

Third-party intent data (e.g. Bombora) alone is category interest, not buying intent. Strong ICP fit alone is also not enough. Intent data requires corroborating signals to become actionable.

Signal combinations ranked by strength:

Strongest - Intent + high-intent website visit: If the company shows topic intent AND visited high-intent pages (pricing, demo, security, integrations, API/docs, or your domain-specific product pages), this is actionable when ICP fit is confirmed.

Very strong - Intent + closed-lost context: A closed-lost account showing new intent suggests timing may have changed.

Strong - Intent + relevant business event: If the business event creates a clear "why now" (e.g. a relevant license, product launch, infrastructure expansion, market entry), this combination is meaningful when a clear pain hypothesis exists.

Medium-strong - Intent + relevant hiring cluster: A cluster of relevant roles adds meaningful corroboration. One role alone is insufficient.

Medium - Intent + repeated/escalating intent: Escalating intent across multiple weeks on highly relevant topics adds weight.

Insufficient alone - Intent + strong ICP only: worth tracking but does not prove timing.

Weakest - Intent alone.

#### Signal Strength for Intent Data

High: Intent combined with a first-party signal (high-intent website visit) or a very strong corroborating signal (closed-lost context + relevant topic).

Medium: Intent combined with a relevant business event or hiring cluster.

Low: Intent alone, or intent + weak ICP fit only.

#### Confidence for Intent Data

Intent data rarely reaches High Confidence. It tells us category interest, not actual buying intent.

Medium: Topics highly specific to {{ICP_DOMAIN}} (e.g., for a custody company: "stablecoin custody", "digital asset treasury"), intent escalated or repeated, and at least one corroborating signal.

Low: Topics relevant but broad, intent single-week or non-escalating, or no corroborating signal. Intent alone = Low Confidence even if the topic is highly relevant.

---

### Step 3 - Build the Interpretation Output

Produce the following structured fields. These are interpretation only - your tier-scoring stage consumes them to compute tier and action.

**relevanceVerdict:** relevant | not_relevant (from Step 1).

**signalType:** "Business Event" or "Intent Data" with subtype (e.g. "Business Event - Regulatory Approval").

**subcategory:** The ICP qualification subcategory passed in by the calling trigger. Read directly from the `subcategory` field of the ICP qualification verdict input. Pass it through as-is - do not modify or infer. If not present -> null. Downstream stages (messaging, lead routing) apply subcategory-level personalization.

**cleanSummary:** One sentence. What happened, in plain English. No interpretation yet.

**likelyMeaning:** What this signal probably indicates about where the company is heading. Ground it in the signal details, not generic analysis.

**businessImplication:** What operational complexity this likely creates - in {{ICP_VOCABULARY}}. Be specific. If no implication can be identified, say so.

**productRelevance:** Which of {{COMPANY_NAME}}'s products or capabilities are most relevant. Or "None identified" if the signal does not pass the relevance gate.

**whatNotToAssume:** The most important inferential risks. What the signal does NOT prove. What could be wrong about the interpretation.

**signalStrength:** High / Medium / Low - with one-sentence rationale. Raw, current-signal-only (no accumulation upgrade).

**confidence:** High / Medium / Low - with one-sentence rationale.

**signalCategory:** One of - assign based on what the signal reveals about the company's current motion:
- Growth: expanding operations, markets, team, or product in a direction that creates new infrastructure needs
- Urgency: a time-bound window exists - a license just granted, funding just closed, a compliance deadline, a product going live
- Intent: actively researching or evaluating solutions in {{ICP_DOMAIN}} (intent-data topics, high-intent website visit, relevant post engagement)
- Risk: faces a governance, compliance, or operational control problem likely to surface soon
- Noise: real signal but no actionable implication for {{COMPANY_NAME}} right now

Only one category per signal. When in doubt between two, pick the one that most directly explains why to act now vs. later.

**whyNow:** One sentence - why is this week the right week rather than in 60 days? Must reference something concrete from the signal (a specific event, launch date, hire, announcement, or deadline). If a concrete "why now" cannot be identified -> null. Do not manufacture urgency. (Your tier-scoring and outreach-gating stages decide what a null whyNow means for action; this skill only reports it honestly.)

**competitiveContextDetected:** null, or a short one-line flag when a confirmed {{COMPANY_NAME}} competitor is **explicitly named** in enrichment data, tech stack, or the event/comment text itself (e.g. "Competitor X named in funding use-of-funds", "Competitor Y mentioned in announcement"). This is **detection only** - not displacement strategy, and not proof the account runs the competitor. Do not populate on inference. When populated, your downstream messaging stage shifts to displacement framing; any competitor-in-stack booster in your tier-scoring stage should fire only on tech-stack enrichment evidence, never on this field alone.

**openQuestions:** Maximum 5. Prioritize by impact - questions that block outreach first, then questions that could change the action, then questions that sharpen messaging. Three categories in priority order:
- Signal interpretation gaps: What does the signal actually mean? Is the operational implication real or inferred?
- ICP/relevance gaps: Is {{ICP_DOMAIN}} core to the business?
- Actionability/contact gaps: Is there an owner? Recent outreach? Who is the right contact?

If `icp_verdict: "borderline"` and signal evidence strongly suggests a different segment than ICP qualification returned, do not silently override - add a specific Open Question flagging the discrepancy (e.g. "ICP qualification returned PSP but signal evidence suggests Fintech - confirm segment before outreach.").

If more than 5 meaningful uncertainties exist, the signal is too uncertain for outreach - reflect that in the interpretation (weak Confidence, explicit Open Questions).

Bad Open Questions to avoid: "Is this company good?" / "Should we talk to them?" / "Are they interesting?"
Good Open Questions (custody-domain examples): "Do they actively manage stablecoin or digital asset flows?" / "Is this product launch operational or mostly marketing?" / "Is there an existing account owner or active pipeline?"

---

### Reference - Relevant Contact Personas by Signal Domain

Your orchestrator and lead-routing stage use this to determine whether a relevant contact exists (`contactAvailable`) and who to target. It is reference for contact-finding - this skill does not act on it. Build your own persona map: for each signal domain inside {{ICP_DOMAIN}}, list the personas that own the pain that signal reveals. Worked example for a digital-asset custody company:

- **Regulatory / Risk / Compliance:** CCO, MLRO, CRO, Head of Compliance, Head of Risk, Head of AML, Head of Financial Crime, General Counsel, Head of Legal, Head of Regulatory Affairs
- **Payments / Stablecoin / Settlement:** Head of Payments, VP Payments, Head of Stablecoin Ops, Head of Settlement, VP Treasury, Head of Treasury, Treasurer, CFO
- **Digital Assets / Crypto / Tokenization:** Head of Digital Assets, VP Digital Assets, Director of Digital Assets, Head of Blockchain, Head of Crypto, Head of Tokenization
- **Infrastructure / Custody / Wallet / Migration:** CTO, VP Engineering, Head of Engineering, Head of Infrastructure, Head of Custody, Head of Wallets, Head of Platform
- **Growth / Hiring / Product Build:** CTO, COO, VP Product, Chief Product Officer, Head of Product, Head of Engineering, CEO (<=150 employees), Co-founder
- **Partnership / Ecosystem:** Head of Partnerships, VP Partnerships, Head of Business Development, Ecosystem Lead, Head of Web3 Partnerships

When no domain-specific persona exists and the company has <=150 employees, CEO, Founder, Co-founder, or COO are valid contacts. For larger companies, no functional owner = treat contact as unavailable (Enrich).

---

### Important Rules

- Never jump directly from signal to outreach - this skill interprets; your tier-scoring and outreach-gating stages decide action.
- Separate Signal Strength from Confidence - they measure different things.
- Always include What Not To Assume.
- Report raw current-signal strength - never apply accumulation upgrades (your tier-scoring stage owns accumulation).
- Prefer precision over volume. If the signal is interesting but not proven, say so plainly in Confidence and Open Questions.
- Do not use creepy wording - never say "we saw someone visit your pricing page."
- Funding, hiring, and news signals are noisy unless connected to a relevant business motion.
- First-party signals like website visits are stronger than third-party signals, but still require context.
- Interpretation applies to this specific signal, not the company as a whole.
- Do not populate competitiveContextDetected on inference - only when a competitor is explicitly named in available data.

---

## What good looks like

- Every irrelevant signal dies at the Relevance Gate with a one-line reason - nothing downstream ever sees it.
- Strength and Confidence are always scored separately, each with its own one-sentence rationale, and neither is inflated by prior signals - accumulation is the tier stage's job.
- `whyNow` is either grounded in something concrete from the signal or honestly null. No manufactured urgency, ever.
- Every interpretation includes What Not To Assume - the output states its own inferential risks before anyone acts on it.
- Open Questions are specific and answerable ("Do they actively manage stablecoin flows?"), capped at 5, ordered by what blocks outreach first; a signal with more than 5 real uncertainties is reported as too uncertain for outreach.
- The output contains zero side effects: no tier, no action, no alert, no memory write - structured interpretation fields only, ready for the tier-scoring stage.
