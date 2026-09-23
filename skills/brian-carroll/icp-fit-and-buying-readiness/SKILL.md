---
name: icp-fit-and-buying-readiness
title: ICP Fit and Buying Readiness
description: |
  Use this skill when evaluating whether an account is worth pursuing, preparing
  for a discovery meeting, or deciding mid-conversation whether to continue
  investing time. Produces an account-level verdict (Investigate / Watch / Pass
  before discovery; Pursue / Watch / Pass after discovery) grounded in fit,
  readiness, and discovery evidence. Separates observed facts from hypotheses
  from conclusions. Designed for AI agent execution: every output requires
  cited evidence, and every unknown produces a next question rather than an
  assumption.
category: Sales
tags: [Sales, Marketing, RevOps]
contributors: []
---

Build an evidence-based qualification framework that separates company fit from
buying readiness, and both from what can only be confirmed in conversation.
Produces a verdict for each account with cited evidence, explicit unknowns, and
a flip condition. The method is transferable; the specific criteria are yours to
define from your own win/loss/no-decision data.

The core conviction: diagnosis before prescription. Fit describes a market —
it does not explain buying behavior. The companies that actually buy share a
pattern: something disrupted the status quo enough to make change feel
necessary. This skill builds the system for separating "looks like a fit" from
"has a reason to change right now."

(See references/diagnostic-philosophy.md for the full reasoning chain and the
central question this framework answers.)

## Skill contract

### Inputs

- ICP or customer fit criteria (operator-defined or to be built in Step 1)
- Closed-won, closed-lost, and no-decision opportunity data
- CRM and account history
- Public company information (filings, press, job postings, leadership pages)
- Observable trigger events
- Discovery notes or call transcripts when available

### Outputs (required for every account evaluated)

- Fit assessment: each criterion rated Yes / No / Unknown with cited evidence
- Readiness assessment: each signal evaluated as Observed Fact → Hypothesis →
  Unknown, with evidence strength (Strong / Mixed / Weak)
- Investigation questions: what to research or ask next, derived from Unknowns
- Verdict: Investigate / Watch / Pass (pre-discovery) or Pursue / Watch / Pass
  (post-discovery)
- Flip condition: what would need to change for the verdict to move
- Next best action: the single most valuable thing to do next for this account

### Evidence the skill may use

- CRM history, deal records, activity logs
- Direct buyer statements from calls, emails, or transcripts
- Documented leadership announcements, press releases, SEC filings
- Confirmed technology or organizational changes
- Job postings with specific, relevant content
- Network intelligence from known, named sources

### Evidence the skill must not infer

- Buying intent from generic activity (downloads, page views, ad clicks)
- Business problems from industry membership alone
- Executive sponsorship from title alone
- Urgency from signal presence alone
- Budget or timeline without direct confirmation
- Status quo dissatisfaction from external observation alone

## Required behavior: facts, hypotheses, and unknowns

Every important conclusion requires three fields:

- **Observed fact:** what is actually known from a cited source
- **Hypothesis:** what this may mean for the account's readiness
- **Unknown:** what we still need to learn before acting on the hypothesis

This separation is required throughout the skill. Never collapse an observed
fact into a conclusion. "Company hired a CRO" is a fact. "Company has a GTM
problem and is ready to buy" is a conclusion that skips the hypothesis and
ignores the unknowns.

## Step 1: Study what distinguishes wins from no-decisions

Before defining criteria, study your own evidence. Pull recent wins, losses,
and — critically — good-fit opportunities that ended in no decision.

The no-decision group is the most important. These companies matched the ICP,
engaged, took meetings, and asked good questions, but ultimately did nothing.
Understanding what separated them from the companies that bought is how you
move from a market description to a qualification framework.

For each group, investigate:

- What triggered the search? What motivated them to start looking?
- Why then? What was happening inside the company?
- What had they already tried? What made the status quo harder to maintain?
- How many stakeholders were involved? Who drove the decision?
- What was the business problem in their own words?

The patterns that emerge — especially the patterns that distinguish wins from
no-decisions — are your qualification criteria.

(See references/fit-vs-readiness.md for a worked example where this analysis
increased average deal size by 33% and revenue by 20%.)

## Step 2: Interview the people closest to the customer

Talk to salespeople, account managers, and customer success. Ask them to
identify the 5-7 must-have questions they need answered for an account to
be genuinely qualified, versus the nice-to-have questions everyone asks out
of habit.

This surfaces the collective intelligence of the team and grounds the
framework in what distinguishes wins from no-decisions, not what looks good in
a spreadsheet or a scoring model.

## Step 3: Sort your criteria into four categories

Once you have your criteria from Steps 1 and 2, sort each one into exactly
one of four categories based on when it can be evaluated and what it tells you.

### Fit criteria

Characteristics of the company that can be evaluated from research before any
conversation. These describe the kind of organization where your offering
creates value.

Examples: company size, industry, business model, organizational complexity,
technology infrastructure, geography, separate functional leadership.

**Test:** Can this criterion be confirmed or disconfirmed from publicly
available information or CRM data without talking to the prospect?
If yes, it is a fit criterion. If no, it belongs in a later category.

### Readiness signals

Observable events or changes that suggest the status quo may be under
pressure. These cannot confirm buying intent, but they indicate something
may be changing that makes the account worth investigating.

Examples: leadership changes, acquisitions, technology migrations, hiring
patterns, competitive pressure, a known contact changing companies.

**Test:** Is this something that happened (observable event) rather than
something the company is (characteristic)? Does it suggest the status quo
may have been disrupted? If yes, it is a readiness signal.

### Discovery criteria

Questions that can only be answered through conversation. These confirm or
disconfirm the real business problem, urgency, sponsorship, and willingness
to act.

Examples: the actual business problem in the buyer's own words, executive
sponsorship, urgency and forcing functions, willingness to share data and
act on findings, cultural readiness for diagnosis versus execution.

**Test:** Is this something we cannot evaluate without talking to the
prospect? If yes, it is a discovery criterion. Do not put it in the fit
threshold — you will either guess wrong or skip the question.

### Disqualifiers

Conditions that kill the opportunity regardless of fit or signals. Split
into two tiers:

**Hard disqualifiers:** When confirmed, downgrade to Pass immediately.
These are patterns from your own stalled deals that did not appear in wins.

**Watch / validate flags:** Conditions that warrant probing before a verdict.
These sometimes appeared in wins, so they are risks to test rather than
automatic kills.

**Test:** Review your stalled deals. For each one, identify the moment you
knew it was going to stall. That signal is a candidate disqualifier. Test it
against your wins: did any closed deal show the same flag? If no, it is a
hard disqualifier. If yes, it is a watch/validate flag.

(See references/discovery-red-flags.md for a worked example with eight hard
disqualifiers, two watch flags, and the probe questions for each.)

## Step 4: Build your fit threshold

Organize your fit criteria into a threshold: the minimum conditions an
account must meet before you invest time evaluating readiness or signals.

For each criterion, track three states:

- **Yes** — confirmed from cited evidence
- **No** — disconfirmed from cited evidence (stop here)
- **Unknown** — not yet established

Unknown is not a pass. Unknown is not a fail. Unknown produces the next
question to ask or the next piece of research to do. An account with three
Yes and two Unknown is a research task, not a verdict.

Add strong-fit indicators that elevate priority when they stack on top of
all must-haves.

## Step 5: Build your readiness signal library

Fit tells you who. Readiness tells you when — or more precisely, it tells you
which good-fit companies may be experiencing enough status quo disruption that
change becomes more likely than inaction.

For each potential trigger, evaluate:

1. **Observable event** — what you can actually see or detect, with source
2. **Possible implication** — what may be changing, and how it might pressure
   the status quo
3. **Relevance** — why this event could create or amplify the specific problem
   your offering addresses
4. **Supporting or contradicting evidence** — other signals that strengthen or
   weaken the read
5. **Unknown** — the gap between observation and certainty
6. **Investigation question** — the specific thing to research or ask next
7. **Next action** — investigate, watch, or engage

(See references/trigger-event-methodology.md for the full framework and
common trigger categories.)

### Finding your highest-value signals

Study your wins: what was observable before the deal started? Then check: were
those same signals present in the good-fit accounts that went nowhere? The
signals that appear more often in wins than in no-decisions are your
highest-value signals.

### Signal windows

Different events have different useful lives. Do not apply a universal decay
rule. A leadership change may create a diagnostic window that lasts months.
A small intent signal may lose relevance in weeks. Define windows based on the
underlying change and your own historical evidence.

## Step 6: Pre-discovery verdict

Before a conversation, the skill can determine fit, observable signals,
hypotheses, research gaps, and whether an account is worth investigating.
It cannot determine the real business problem, urgency, sponsorship, or
whether the status quo has been disrupted enough to drive action.

Three pre-discovery verdicts:

| Verdict | Condition |
|---------|-----------|
| **Investigate** | All fit must-haves Yes + active readiness signal(s) |
| **Watch** | Fit confirmed + no active signals, or fit has Unknowns worth resolving |
| **Pass** | Any fit must-have disconfirmed (No) |

Investigate means "worth a conversation." It does not mean "ready to buy"
or "qualified." The conversation is the qualifying event.

## Step 7: Discovery — confirm or disqualify

Discovery evaluates what research cannot: the real business problem, the
pressure on the status quo, sponsorship, and willingness to change.

The central discovery question is not "do they have budget?" It is: **what
has made the status quo harder to maintain, and is the pressure sufficient
to overcome the cost of change?**

Run your discovery criteria. For each hard disqualifier, listen for the
pattern. For each watch/validate flag, probe with the specific question you
defined. For each unknown from the fit and readiness stages, seek the
evidence that resolves it.

## Step 8: Post-discovery verdict

| Verdict | Condition |
|---------|-----------|
| **Pursue** | Fit confirmed + readiness signal(s) active + real problem confirmed + status quo under sufficient pressure + sponsor identified + no disqualifiers |
| **Watch** | Fit and problem confirmed but urgency, timeline, or sponsor is weak or Unknown |
| **Pass** | Any fit must-have fails OR any hard disqualifier confirmed in conversation |

For every Watch and Pass, define the flip condition: what specifically would
need to change for the verdict to move?

## Step 9: Learning loop

After enough outcomes accumulate, compare:

- Which Pursue accounts actually closed?
- Which signals occurred frequently in wins?
- Which signals also appeared in no-decisions?
- Which supposed disqualifiers showed up in wins?
- Which Unknowns were most useful to resolve?
- Which criteria added no meaningful separation?
- Were the accounts that bought experiencing more status quo pressure than the
  ones that did not? What form did that pressure take?

Revise your fit criteria, readiness signals, signal windows, discovery
questions, and disqualifiers. This makes the framework a learning system, not
a static scoring model.

Use the standard output template for every account evaluation.
(See references/output-template.md for the full template.)

## What good looks like

- **The best operator starts with their own closed-deal data, not with
  industry benchmarks.** They compare wins against no-decisions and find
  the patterns associated with buying behavior — especially the
  patterns related to status quo disruption.
- **The best operator interviews the sales team first.** They identify the
  5-7 must-have questions, versus the nice-to-haves.
- **The best operator sorts every criterion into exactly one category** —
  fit, readiness, discovery, or disqualifier — based on when it can be
  evaluated and what it tells you. They never put a discovery criterion
  into the fit threshold.
- **The best operator separates facts from hypotheses from conclusions.**
  They never collapse "company hired a CRO" into "company is ready to buy."
- **The best operator asks "why would this company change now?" not just
  "does this company fit?"** They look for evidence that the status quo
  has been disrupted enough to make action more attractive than inaction.
- **The common mistake is treating fit as the final answer.** Good-fit
  companies that show activity get treated as ready to buy without
  confirming that the status quo is under sufficient pressure to drive
  change. The team spends months on accounts where nothing was going to
  move.
- **The output quality test:** After running this framework, the agent
  should be able to state in one sentence why this account should or
  should not be pursued right now, cite the evidence, name the unknowns,
  and identify what would need to change for the verdict to flip.

## Rules

- MUST cite or name the evidence behind every important conclusion.
- MUST separate observed facts from hypotheses from conclusions throughout.
- MUST track Yes / No / Unknown for every criterion and signal. Unknown
  produces a question, never an assumption.
- MUST sort every qualification criterion into exactly one of four categories:
  fit, readiness, discovery, or disqualifier.
- MUST use pre-discovery verdicts (Investigate / Watch / Pass) before a
  conversation and post-discovery verdicts (Pursue / Watch / Pass) after.
  Never issue Pursue without discovery evidence.
- MUST define a flip condition for every Watch and Pass verdict.
- MUST ground criteria in win/loss/no-decision evidence, not assumptions.
- NEVER infer a business problem from external signals alone.
- NEVER infer status quo dissatisfaction from observable data alone. A signal
  suggests the status quo may be under pressure. Only discovery confirms it.
- NEVER infer executive sponsorship from title alone.
- NEVER skip the fit check because signals look strong.
- NEVER assign a confidence score as a substitute for naming what is known,
  what is hypothesized, and what is unknown.
