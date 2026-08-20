---
title: Scoring criteria and stage expectation bands
description: (reference) Evidence thresholds per dimension, the stage bands that make a score meaningful, calibration procedure, worked scores, and edge cases.
---

# Scoring criteria and stage expectation bands

The evidence thresholds behind every score, the stage bands that make a score mean something, how to calibrate both against your own history, and what to do at the edges.

## The scale

| Score | Label | What it means |
|---|---|---|
| **+1** | Accelerator | Strong, validated evidence. Someone with authority confirmed it in their own words. |
| **+0.5** | Friction | Partial evidence. Known but unvalidated, or true but weak. Creates drag, not death. |
| **0** | Unknown | No evidence either way. Nobody has asked, or nobody answered. |
| **−1** | Blocker | Active evidence of a condition that kills the deal if unaddressed. |

Eight dimensions. The champion dimension has no −1 (see below), so the range is **−7 to +8**.

Note the asymmetry between steps: friction to accelerator is 0.5, but unknown to blocker is a full point. That is intentional — a confirmed blocker is a bigger event than a confirmed strength, because deals are lost by unaddressed blockers more often than they are won by stacked accelerators.

## Per-dimension criteria

Written in neutral terms — substitute your `{{TERMINOLOGY_MAP}}` labels and your own category of value.

### Metrics — is there a quantified economic impact that justifies the spend?

- **+1** — The economic decision-maker has confirmed that hitting a specific number achieves a business outcome they own. There is a jointly agreed case connecting your impact to their financials.
- **+0.5** — A target number is known but treated as a nice-to-have. The metrics are operational rather than financial — real, measurable, and connected to nothing on the P&L.
- **0** — No target numbers stated at all.
- **−1** — The buyer cannot articulate what happens to the business if the target is missed, or the conversation is anchored on a pilot budget disconnected from any larger outcome.

A frequent mis-score is +1 on an operational metric. A number the buyer is measured on is not the same as a number their business depends on. If missing it costs them nothing they can name, it is +0.5.

### Economic buyer — is the person who owns the budget identified and engaged?

- **+1** — Direct, substantive interaction with the person who ultimately releases the money, in which they articulated the priority this solves in their own words.
- **+0.5** — You know who they are, but every interaction is filtered through a subordinate. Support is inferred from secondhand reports.
- **0** — You cannot name the person who approves spend at this size.
- **−1** — You have identified them and been actively blocked from reaching them, and your contact cannot or will not facilitate access.

The line between +0.5 and −1 is whether the blocking is passive or active. "We haven't got to them yet" is friction. "You don't need to talk to her" is a blocker — and it is routinely recorded as friction, because it arrives politely.

### Decision criteria — do you know what the buyer will actually judge on?

- **+1** — The criteria are explicit and favour capabilities you hold and competitors do not.
- **+0.5** — Criteria exist but are generic — the kind any credible vendor satisfies.
- **0** — You do not know the formal or informal criteria.
- **−1** — The criteria are written around a competitor's differentiators, or a constraint you cannot meet.

Criteria you helped shape score +1. Criteria you merely learned score +0.5, however favourable they look. Discovering requirements is not the same as influencing them.

### Decision process — do you know how the decision actually gets made?

- **+1** — Every step, approval, and timeline is documented and confirmed by someone inside the account.
- **+0.5** — You have a verbal outline nobody has validated, with assumed steps.
- **0** — Not mapped.
- **−1** — The process has stalled with no restart date, or you are being excluded from steps you should be in.

### Third parties and paper process — is anyone outside the buying team in the path?

Covers implementation partners, agencies, resellers, integrators, procurement, legal, and security review.

- **+1** — Every external party is identified, their role is clear, and none blocks value delivery.
- **+0.5** — There is involvement but the timelines or the incentives are unclear.
- **0** — No visibility into whether third parties are involved at all.
- **−1** — A third party is actively blocking — deprioritising the work, gating the timeline, or lacking any incentive to help you.

Read incentives, not intentions. A partner who is friendly but earns nothing from your integration is a blocker with good manners, and reps score this +0.5 because the relationship feels fine.

### Implicated pain and initiative — what is forcing action on a timeline?

- **+1** — A funded, time-bound initiative with executive sponsorship is driving this, and slipping it has a named consequence.
- **+0.5** — The pain is acknowledged but there is no deadline and no specific initiative creating urgency.
- **0** — You do not know what prompted the evaluation.
- **−1** — There is no real pain, or the pain is not big enough to displace anything else competing for the same budget.

This is where no-decision losses are decided. A deal can score well everywhere else and die here, because the buyer's alternative — doing nothing for two more quarters — costs them nothing.

### Champion — do you have an advocate who sells for you when you are not there?

**This dimension has no −1.** Deliberately.

- **+1** — Proven: they advocate internally without prompting, share information they were not asked for, and coach you on how to win. Their influence has been demonstrated at least once.
- **+0.5** — Unproven: friendly, responsive, shares information — but has never demonstrated influence and has never sold on your behalf.
- **0** — Absent: nobody identified.

There is no "high-risk champion." A contact shown to have no influence, or who has misled you, was never a champion — they were a friendly contact who got mislabelled. Recording that as a blocker hides the real problem and points at the wrong action. Score them **0 — absent**, and the next action becomes finding one, which is correct.

The +0.5 that sits at +1 for months is the quiet version of the same error, and it is worth re-testing every time this runs: what has this person actually done on your behalf since the last run?

### Competition — where do you stand against the alternatives?

Include the status quo. Doing nothing is the alternative that wins most often.

- **+1** — Preferred or sole-sourced, with differentiation the buyer can articulate back to you.
- **+0.5** — In a fair competitive evaluation with identified advantages.
- **0** — You do not know who else is being considered.
- **−1** — You are viewed as undifferentiated, a competitor is favoured, or the criteria are written against you.

## Stage expectation bands

| Band | Expected total | Hard floor | Additional gate |
|---|---|---|---|
| Discovery / qualification | ≥ 0 | −2 | Unknowns are normal — nobody has asked yet |
| Validation | ≥ +2 | 0 | No unknowns on metrics, economic buyer, or champion |
| Proposal / business case | ≥ +4 | +2 | No dimension at −1 |
| Negotiation | ≥ +5.5 | +4 | Any −1 triggers a forecast review |
| Commit / close | ≥ +6.5 | +5 | Decision process and paper process both at +1 |

**Reading the gap** — actual minus expected:

| Gap | Read | Action |
|---|---|---|
| At or above expectation | On track | Work the highest-value unknown |
| Up to 1.5 below, and above the floor | Recoverable in stage | Build a maneuver; leave the forecast alone |
| More than 1.5 below, **or** under the hard floor | Wrong stage, or something was scored on faith | Escalate to `{{FORECAST_OWNER}}` same day |

**The unknown-cluster override.** Regardless of total, if **three or more** dimensions score 0 and the missing evidence all sits behind a single stakeholder, **the deal does not hold its current stage**: escalate regardless of the gap test, and recommend moving the opportunity back one stage until a second independent source exists inside the account.

The override never softens a read. A deal that already fails the gap test and also clusters is not rescued by being re-read at an earlier stage — it fails both tests, and the earlier stage is the recommendation, not the excuse.

**Band gate consequences.** A breached gate acts on its own, independent of the total — three bind the plan, one escalates. An unknown remaining on metrics, economic buyer, or champion blocks advancement past validation and becomes a lane 3 item that cycle; any −1 at proposal obliges cycle 1 to target it and holds the proposal; any −1 at negotiation triggers a forecast review that week; and a decision process or paper process below +1 at commit means the close date is an estimate, not a commit.

**The stall rule.** No movement across two consecutive runs at validation-or-later is a stalled deal at any level — a live deal generates new information. Report it as a finding in its own right.

## Worked scores

### A deal that reads better than it is

Proposal stage. Metrics +1, economic buyer +0.5, decision criteria +0.5, decision process 0, third parties 0, initiative +1, champion +0.5, competition 0. **Total +3.5.**

Expected at proposal is +4, so the gap is −0.5: on the gap test alone, recoverable, no escalation. But three dimensions sit at 0 — decision process, third parties, competition — and every one traces to the same contact, the only person who has spoken about any of them. **The unknown-cluster override fires**, so the gap test does not govern: escalate today, and recommend the deal move back to validation. A business case is sitting with a buyer whose approval path nobody has verified, and the −0.5 gap is what makes that easy to miss.

Target for cycle 1: the economic buyer's +0.5, because resolving it also produces an independent source for the three unknowns.

### A deal that reads worse than it is

Discovery. Metrics 0, economic buyer 0, decision criteria 0, decision process 0, third parties +0.5, initiative +1, champion +0.5, competition 0. **Total +2.**

Five zeros looks alarming and is not. Expected at discovery is ≥ 0 and unknowns are the normal state — nobody has asked yet. The cluster override does not fire, because the zeros are not behind one stakeholder; they are behind nobody, which is what discovery looks like. Initiative at +1 with a funded, time-bound driver is the strongest possible thing to know this early. Correct action is lane 3 discovery, not a maneuver.

### A −1 that should stop a forecast

Negotiation. Metrics +1, economic buyer +1, decision criteria +0.5, decision process +1, third parties −1, initiative +1, champion +1, competition +0.5. **Total +5.0** — above the +4 floor, 0.5 below the +5.5 expectation, so the gap test alone says "recoverable, build a maneuver." But third parties sits at −1: procurement has gated the timeline with no restart date. At negotiation, **any −1 triggers a forecast review** regardless of total. `{{FORECAST_OWNER}}` decides that week whether the close date holds, and records the decision either way. The total is comfortable; the deal cannot close through a gate nobody has opened.

## Edge cases

**Segments in different stages.** On a segmented track, each party gets its own score, band, and stage read — and **the deal takes the weaker of the two**. A partner assessment sitting a full band behind the client assessment is the deal's real position, not an averaging problem. Never report a blended total.

**The decisive call is missing from the context layer.** If the interaction everyone refers to was never recorded, the dimensions that depended on it score **0**, not the rep's recollection of it. Add a lane 3 item to re-establish the fact in writing — "confirming what you mentioned on the call, the sign-off sequence after you is…" — which both closes the gap and creates the evidence.

**Renewals and expansions.** Metrics, initiative, and champion carry over from the existing relationship only where there is evidence they still hold; sponsors move and initiatives get defunded. Decision process and paper process reset to 0 by default — a renewal frequently takes a different approval path than the original purchase, and assuming otherwise is the most common way a renewal slips a quarter.

**Multi-year or phased commitments.** Score the phase actually being decided now. A phase-two commitment that nobody has budgeted is not an accelerator on phase one; it is an unknown attached to a future deal.

**A dimension genuinely does not apply.** Score it **+1** only where its absence is confirmed and favourable — no third parties in the path at all, verified — and record why. Where it is merely not visible, that is **0**. The difference between "no procurement involvement" and "nobody has mentioned procurement" is most of a quarter.

## Calibrating the bands

The numbers above are defaults, not findings. Calibrate before letting any of them touch a forecast.

**1. Build a per-stage dataset.** Take your last 30–40 closed deals with a usable context layer, mixed won and lost. For each deal, score it **once per stage it passed through**, using only evidence available as of that stage's exit. One deal that reached negotiation yields four data points, not one. Score blind to the outcome — ideally have someone score deals whose results they do not know.

**2. Set expectation from the winners.** At each stage, take the distribution of scores from deals that eventually closed won. Set the expectation near the **40th percentile** — most winners clear it, and the ones that do not are the genuinely scrappy wins you do not want the framework calling healthy. Setting it at the median guarantees half your winners read as behind, which trains everyone to ignore it.

**3. Set the hard floor from the same distribution.** Put the floor near the **10th percentile of winners** at that stage: the level below which winning is rare enough that a same-day conversation is warranted.

**4. Check the floor against the losers.** At each stage, what share of eventual losses were already below the floor? **Under a third** — the floor is too low to catch anything; raise it toward the 20th percentile of winners and re-check. **Over three quarters** — confirm you are not simply describing deals that had already visibly failed by that stage; if the breaches cluster in the last stage before the loss, the bands are recording death rather than predicting it, and the earlier stages are where the calibration effort belongs.

**5. Small samples — count winners per stage, not deals.** Every percentile here is computed on *the winning deals that reached one particular stage*. A 40-deal set can still leave a dozen winners at negotiation, and a 10th percentile of twelve observations is a single data point wearing a statistic's clothing.

Aim for **about 30 winners at the stage you are calibrating**. Below that: use the minimum and median of the winning set as floor and expectation, mark those bands provisional, and keep them out of forecast decisions until the sample fills in. Late stages fill slowest, so expect the commit band to stay provisional longest.

Note also that a deal contributing four observations contributes four *correlated* ones — a strong deal tends to score well at every stage. Effective sample size is meaningfully smaller than the observation count, which is a reason to be conservative with the tails and to prefer the median-and-minimum fallback longer than the raw count suggests.

Recalibrate when the motion changes — new segment, materially different price point, or a cycle length that shifts by more than about a third. Bands built on a six-month cycle mislead on a two-month one, because the same score had half the time to be earned.

## Delta tracking on re-runs

Every dimension carries a marker: **retained**, **upgraded**, **downgraded**, or **new**.

- **Clear new evidence** → change the score.
- **No new evidence** for that dimension → retain, and state that nothing new landed.
- **New evidence contradicting the current score** → change it and write the contradiction down, citing both the earlier and later evidence.

A written downgrade with its reason is the most useful line in a deal review. An unexplained one is noise, and a silent one is how a framework loses the trust of the people who have to act on it.
