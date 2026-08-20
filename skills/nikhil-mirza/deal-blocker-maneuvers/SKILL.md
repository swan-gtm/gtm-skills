---
name: deal-blocker-maneuvers
title: Deal blocker maneuvers
description: |
  Use this skill after any meaningful interaction on a complex deal — a call, a stakeholder
  meeting, a procurement exchange — when the question is not "what's missing" but "what do I
  actually run next week." Takes a qualification assessment (supplied, or scored here from
  primary evidence), reads it against what the deal's stage should already have proven rather
  than against an absolute bar, and converts the single worst blocker into a two-cycle
  maneuver the rep can save and execute: trigger conditions, a pre-mortem, a go/no-go
  checklist, a verbatim opening, IF/THEN counter-moves, and explicit abort criteria. Covers
  deal coaching, deal strategy, forecast defence, stalled and blocked deals, gone-dark
  champions, procurement stalls, third-party and partner blockers, deal reviews, and "this
  deal is stuck and I don't know why." Built for enterprise and complex deals; not for
  transactional velocity motions.
category: Deals
tags: [Sales, RevOps]
---

# Deal blocker maneuvers

Runs after every meaningful interaction on a complex deal. Produces one saved artifact: a stage-adjusted read of the deal's qualification, a named primary blocker, and a two-cycle maneuver with abort criteria — plus a missing-information report listing exactly what nobody has asked yet.

This is the layer *after* diagnosis. Knowing that the economic buyer is unverified is not a plan; the plan is the specific move that verifies them, what you do when it backfires, and the condition under which you stop trying.

## Scope — where this works and where it does not

Built for **enterprise and complex deals**: multiple stakeholders, a real evaluation process, third parties or procurement in the path, months rather than days. That is where the eight dimensions all carry information and where a two-cycle maneuver is worth constructing.

**On transactional and high-velocity deals, the economics invert.** A two-call deal has no buying committee to segment, no paper process to map, and rarely a blocker that survives a single well-aimed question — the diagnostic overhead exceeds what the deal returns, and the output reads as bureaucracy to the rep. Below `{{COMPLEX_DEAL_FLOOR}}`, use whatever lighter qualification standard your team already runs; the evidence rule below is still worth borrowing, but the rest of this is built for a different shape of deal.

## Template placeholders

Replace every `{{...}}` before enabling. Full setup list in **references/setup-customization-checklist.md**.

- `{{TERMINOLOGY_MAP}}` — your org's labels for the eight dimensions, if they differ from textbook terms. Declare them here; the skill then uses **only** your labels in output.
- `{{STAGE_NAMES}}` — your pipeline stage names, mapped onto the five bands in Step 3.
- `{{CONTEXT_LAYER}}` — where primary evidence lives: call recordings and transcripts, email threads, meeting records, shared documents.
- `{{COMPLEX_DEAL_FLOOR}}` — the deal size, cycle length, or segment below which this skill does not run (default: anything that closes in under 30 days or without a second stakeholder).
- `{{FORECAST_OWNER}}` — who is told, same day, when a deal breaches an escalation condition.
- `{{REVIEW_CADENCE}}` — default is after every meaningful interaction; weekly also works. Anything but "when the deal feels stuck."

---

## The evidence rule — read this before any step

**Score only from primary evidence in `{{CONTEXT_LAYER}}`: what the buyer actually said or wrote.** Never from the rep's summary of what happened, their confidence, or their answer to "is the economic buyer engaged?"

This is the failure mode that kills the whole framework. A rep who believes the deal is strong will report it as strong, the framework will faithfully convert that belief into a number, and the number will carry an authority the belief never earned. The output is a confident, wrong forecast — worse than no framework, because it launders optimism into arithmetic.

If a dimension has no evidence in the context layer, it scores **0 (Unknown)**. Zero is an honest, useful state. A guess dressed as a score is neither.

## Step 1 — Run the segmentation gate

Test whether one assessment is even valid. If the definition of success, the identity of the decision-maker, or the risks in play differ across the parties in this deal, one blended assessment averages two realities into a third that describes neither.

Three outcomes: **unified track**, **segmented track** (run the diagnostic separately per party), or **stop and ask** — when the deal plainly has divergent stakeholders but the evidence cannot tell you how they diverge. The stop is deliberate: guessing here corrupts every downstream step, and the question that resolves it takes one message. Variance test in **references/segmentation-and-lanes.md**.

## Step 2 — Establish the assessment

Eight dimensions: **metrics, economic buyer, decision criteria, decision process, third parties and paper process, implicated pain and initiative, champion, competition.**

**If a current qualification assessment already exists** — from the deal record, a prior review, or a diagnostic pass someone else ran — prefer it over re-deriving one, but only per dimension and only where it passes the provenance test.

**The provenance test.** A dimension in an incoming assessment is usable only if it carries the evidence behind it — a quote, a cited exchange, a named source in the context layer. **A qualification field on a deal record usually carries none, and an unsourced field is a rep's self-assessment wearing a score's clothing.** Accept the dimensions that cite evidence. Every dimension that does not is discarded — score it here from the context layer like any other, which will often mean 0, and will sometimes mean the field was right for reasons nobody had written down. Never accept an assessment wholesale because it exists.

Where an accepted dimension conflicts with newer evidence in the context layer, say so explicitly and cite both sides rather than quietly replacing it.

**For every dimension not accepted,** score here: **−1 (blocker)**, **0 (unknown)**, **+0.5 (friction)**, **+1 (accelerator)**, against evidence thresholds rather than impressions. Per-dimension criteria in **references/scoring-and-stage-bands.md**.

Range is **−7 to +8**, because one asymmetry is deliberate: **the champion dimension has no −1.** A champion is proven, unproven, or absent — and "high-risk champion" is almost always a rep describing someone who was never a champion at all. Forcing that judgment into *unproven* or *absent* is more honest and points at a better next action.

**Mapping a different rubric.** Incoming assessments often use a two-axis shape — how well evidenced a dimension is, and whether the answer favours you. Collapse it onto this scale in that order, never by feel:

| Incoming | Maps to |
|---|---|
| Well evidenced, favourable | **+1** |
| Well evidenced, neutral or merely adequate | **+0.5** |
| Well evidenced, actively unfavourable — a condition that kills the deal unaddressed | **−1** |
| Well evidenced, unfavourable but survivable | **+0.5** |
| Asserted without evidence, any direction | **0** |
| Explicitly flagged as a gap or an unknown | **0** |

Three constraints on the table. **The per-dimension criteria govern wherever the incoming detail is specific enough to apply them** — the table is a fallback for assessments too coarse to map directly, not a shortcut past the thresholds. **The champion dimension never maps below 0**: a documented finding that a contact lacks influence or has misled you is *absent*, not a blocker. And a documented risk is an unfavourable finding, not an absence of information — it maps on the favourability rows, never to 0.

The collapse is lossy — a documented "no budget confirmed" and an undocumented worry look similar in prose and land a point and a half apart here, which is enough to flip an escalation. Record the original label alongside the mapped score so the reconciliation is auditable, and where the incoming rubric cannot be resolved on the evidence axis, score **0** and re-derive.

## Step 3 — Read the score against the stage, never in isolation

A raw total means nothing on its own. **+3 is healthy in discovery and alarming in negotiation.** What matters is the gap between actual and what this stage should already have proven.

| Band — map your `{{STAGE_NAMES}}` onto these | Expected | Hard floor | Additional gate |
|---|---|---|---|
| Discovery / qualification | ≥ 0 | −2 | Unknowns are normal — nobody has asked yet |
| Validation | ≥ +2 | 0 | No unknowns on metrics, economic buyer, or champion |
| Proposal / business case | ≥ +4 | +2 | No dimension sitting at −1 |
| Negotiation | ≥ +5.5 | +4 | Any −1 triggers a forecast review |
| Commit / close | ≥ +6.5 | +5 | Decision process and paper process both at +1 |

Every threshold is a tunable default. Calibrate against your own closed-won and closed-lost history before letting any of it touch a forecast.

**Escalate to `{{FORECAST_OWNER}}` the same day when either condition holds:** the total is more than 1.5 below its band expectation, or it is under the hard floor. Between those — up to 1.5 below expectation and above the floor — the deal is recoverable inside its stage: build a maneuver, leave the forecast alone.

**The unknown-cluster override.** Regardless of total, if **three or more** dimensions score 0 *and* the missing evidence all sits behind a single stakeholder, **the deal does not hold its current stage.** Escalate regardless of the gap test, and recommend moving the opportunity back one stage until a second independent source exists inside the account — the close date and forecast category should follow the stage the deal can actually defend. The recommendation stands until the cluster clears; it does not compound into a further rollback on each run. You do not have a qualified deal; you have one relationship and a story, and a healthy-looking total is what makes it dangerous.

**The stall rule.** No movement across two consecutive runs at validation-or-later is a stalled deal at any level — a live deal generates new information, and one that has stopped generating it has usually stopped moving inside the account. Flag the stall as a finding in its own right.

**Band gates have consequences, not just descriptions.** A breached gate acts on its own, independent of the total — three of the four bind the plan, and one escalates:

| Breached gate | Consequence |
|---|---|
| Validation — an unknown remains on metrics, economic buyer, or champion | The deal cannot advance past validation. Every one becomes a lane 3 item this cycle. |
| Proposal — any dimension at −1 | Cycle 1 must target that dimension. A proposal does not go out, or is not pursued, while it stands. |
| Negotiation — any dimension at −1 | Forecast review: `{{FORECAST_OWNER}}` decides that week whether the close date holds, recorded either way. |
| Commit — decision process or paper process below +1 | The close date is not defensible. Treat it as a date estimate, not a commit, until both are +1. |

## Step 4 — Codify and pick the target

Sort the dimensions into blockers (−1), friction (+0.5), unknowns (0), accelerators (+1).

**Cycle 1 targets the single worst blocker.** Not all of them — one. A rep executing one well-constructed move beats a rep holding a list of eight. **Cycle 2 either flanks that blocker or clears the highest-value unknown**, and does not begin until cycle 1 reaches a defined exit state.

With no −1 anywhere, the target is the unknown that most constrains the stage gate above.

## Step 5 — Construct the maneuver

Each cycle gets trigger conditions, the strategic reframe it depends on, a pre-mortem, a go/no-go checklist, a verbatim opening, IF/THEN counter-moves, a named pitfall, and explicit success and abort criteria. Build it from **references/maneuver-construction.md**, which carries the full structure and two worked examples.

**First, if the target blocker has already survived a straightforward attempt to clear it,** classify what kind of contest the deal actually is before writing the reframe — a hostile negotiation, a zero-sum resource fight, and the sale of a financial abstraction each demand a different response, and ordinary qualification logic prescribes the same wrong move for all three. On a first pass, or where the obvious move has not yet been tried properly, skip this. See **references/domain-model-retrieval.md**.

## Step 6 — Assign lanes and publish the missing-information report

Route each maneuver into a lane — third parties and procurement, client-direct, or targeted discovery — and ship discovery items as **literal questions addressed to a named person**, never as topics. A topic gets postponed; a written question gets asked. See **references/segmentation-and-lanes.md**.

Every dimension scored 0 appears in the missing-information report as an unchecked item with the question that would close it. This is what makes the artifact usable in a deal review: it turns "we don't know" into an assignable task.

## Step 7 — Persist the delta and re-run

Mark every dimension **retained**, **upgraded**, **downgraded**, or **new**, against the previous assessment as baseline. Change a score only on clear new evidence; where new evidence contradicts an existing score, write the contradiction down and cite both sides. Where nothing new landed, retain and say so — silence is neither progress nor decay.

Re-run at `{{REVIEW_CADENCE}}`.

## What good looks like

- **Every score traces to a quote.** Open the artifact, pick any dimension, and there is a line from a call or an email behind it. If a rep cannot produce the sentence, the score is not a score.
- **The expert tell: unknowns clustered on one stakeholder.** Novices read the total. What predicts a loss is three or more zeros all sitting behind the same person — a single point of contact and a story you have been told rather than a process you have verified. The total can look respectable while this is true, which is exactly why it is the first thing to check.
- **The mediocre version is a scorecard with no maneuver.** It grades the deal, hands the rep a list of gaps, and calls that coaching. Reps already know their gaps; what they lack is the move. If the artifact contains nothing the rep can say out loud on Tuesday, it has not done its job.
- **The second mediocre version is eight simultaneous plays.** A plan addressing every dimension at once is a plan abandoned by Wednesday. One blocker, one maneuver, one exit condition.
- **The forecast changes.** The test is not whether reps like the coaching — it is whether stage-adjusted scores start predicting outcomes, and whether deals leave the forecast earlier and more honestly than they used to.
- **Reps run the abort.** When a rep stops a play at its stated failure condition instead of trying once more, the framework is operating rather than being filled in. It is the hardest behavior to establish and the clearest signal it is working.

## Rules

- **MUST** score only from primary evidence in `{{CONTEXT_LAYER}}`. **NEVER** score from a rep's self-reported summary, confidence level, or verbal assurance.
- **MUST** score a dimension 0 when evidence is absent. **NEVER** infer a score to avoid an unknown.
- **MUST** read every total against its stage band. **NEVER** report a raw score as healthy or unhealthy on its own.
- **MUST** stop and ask when the segmentation gate is ambiguous. **NEVER** blend divergent stakeholders into one assessment to keep things moving.
- **MUST** prefer an existing evidenced assessment over re-deriving one, and **MUST** state any conflict between it and new evidence rather than overwriting it.
- **MUST** give every maneuver an explicit abort criterion before it is executed.
- **MUST** run the pre-mortem before any move that goes around a stakeholder, and **NEVER** propose a move that bypasses a required approver without naming the political cost and its mitigation.
- **MUST** use `{{TERMINOLOGY_MAP}}` labels in all output, and **NEVER** let borrowed external jargon reach the rep.
- **MUST** explain any downgrade in writing. **NEVER** overwrite a prior score silently.
- **NEVER** write to the deal record without explicit human approval, field by field.
- **MUST** treat the stage bands as provisional until calibrated against your own closed-won and closed-lost history. **NEVER** let an uncalibrated band pull a deal from the forecast.
- **NEVER** run the full framework on a deal below `{{COMPLEX_DEAL_FLOOR}}`.
