---
name: ai-gtm-transformation-audit
title: AI GTM transformation audit
description: |
  Use this skill when a GTM leader (CRO, CMO, VP Sales, RevOps, CS leader, founder) wants to know where their organization really stands on its AI GTM transformation, what is holding it at that level, and what to do in the next 30 days to move up. It runs a short structured interview, places the org on one of four levels (Mostly manual, AI as an answer engine, AI as an action engine, Shared AI layer), scores the four dimensions underneath (People, Process, Systems, Data), names the gaps that block the next level, and writes a one-page readout a leadership team can act on. Also answers "AI readiness assessment", "AI maturity audit for sales and marketing", "where are we on AI in GTM", "why isn't AI moving our numbers".
category: Leadership
tags: [Sales, Marketing, RevOps]
---

Applies when a leader asks "where are we on AI in go-to-market, and what is stopping us from getting more out of it?" Produces a level placement, four dimension scores, the gaps that block the next level, and a 30-day plan.

Most teams overrate their level. They have connected AI to their CRM and call it transformation, yet the numbers have not moved. The audit exists to separate three things leaders tend to blur together: using AI, connecting AI to your data, and having AI do the work in a way the whole team can build on. It is a diagnostic, not a pitch: no vendor recommendations unless the leader asks for them.

## The four levels

Every org sits on one of four levels. Classify against these definitions exactly, and use these names, in this order, everywhere: in the interview, the placement and the readout.

| # | Level | Definition |
|---|---|---|
| 01 | Mostly manual | Research, list building and outreach are done by hand or in traditional tools. |
| 02 | AI as an answer engine | AI is connected to some systems and answers questions when someone asks. |
| 03 | AI as an action engine | Agents run defined workflows and skills when something triggers them. |
| 04 | Shared AI layer | Several teams build and run agents on one foundation with permissions, monitoring and shared context. |

Each level has a tell that confirms it and a ceiling that stops it from reaching the next one:

| Level | The tell | The ceiling |
|---|---|---|
| 01 Mostly manual | Some people use ChatGPT or Claude on their own; AI use depends on who is prompting, and nobody can say what it changed. | Nothing is connected, so every answer starts from zero context. The metrics do not move. |
| 02 AI as an answer engine | "We can ask it anything about an account." A human still does every step after the answer. | Faster answers, same amount of work. The metrics still do not move in a way the board would notice. |
| 03 AI as an action engine | Real productivity uplift, but each agent lives in a different tool and was built from scratch by one person. | Everything is siloed. Every new workflow starts from zero, one builder becomes the bottleneck, and changing a workflow means going into the system it was built in. Progress plateaus. |
| 04 Shared AI layer | A team can iterate on any part of the funnel (prospecting, inbound, deals, renewals) without starting over or filing a ticket. | The ceiling becomes judgment and measurement: which workflows to invest in, and proving what they produce. |

**The most common misplacement is calling an answer engine a shared AI layer.** Integration is not a shared layer. Having every system connected and the data accessible in one place is level 02, AI as an answer engine. Level 04 means the *workflow logic* is defined in one place and can be reproduced and changed simply. Run the logic test below before accepting any self-placement above 02.

### The logic test

Pick one live motion the leader cares about, usually inbound: a lead arrives, it gets qualified, scored, routed and assigned. Ask:

1. "Where does that logic live today?" Name every system involved.
2. "If you wanted to change how inbound is scored next week, who would make the change, and in which tools?"
3. "If marketing wanted the same account context for an event follow-up, would they reuse it or rebuild it?"

Read the answers this way:
- Logic split across two or more systems (scoring in the marketing automation tool, qualification in the CRM, routing in a third tool), and a change needs RevOps or an engineer in each one: **not level 04**, whatever else is connected.
- One place, but only one person can change it: **level 03, AI as an action engine**, with a single-builder risk.
- One place, changeable by the people who own the motion inside guardrails, with context reused across teams: **level 04, Shared AI layer**.

## The four dimensions

The level is the headline. The dimensions explain it and locate the gaps.

- **People:** who can build and change GTM workflows, how knowledge from top performers spreads, who owns a workflow after launch, and where the line between AI work and human work is drawn.
- **Process:** how fast a new motion launches, how consistently follow-up happens, whether teams run shared playbooks, and how AI output is quality-controlled before it reaches a customer or the CRM.
- **Systems:** where AI sits in the stack, how signals turn into action, how many tools a rep touches, and whether orchestration writes back to the system of record safely.
- **Data:** whether the CRM is trusted, whether there is one shared account record, whether signals resolve to accounts and buying groups, and whether AI work can be tied to pipeline and revenue.

An action-engine org with a Data score under 30 is the classic plateau: agents run, but on data nobody trusts, so nobody acts on their output.

## How to run it

### Inputs

- The leader's role and company. If you can look up the company, do it first and open with what you found (what they sell, headcount, the GTM leaders, the visible stack, one recent signal such as hiring or a launch). Label anything you infer as an assumption.
- Optional: several leaders from the same org. Run the interview with each and compare. Disagreement between functions is itself a finding (see Readout).

### Interview rules

1. One question per turn. Offer the listed options in order, best first, and always accept a typed answer.
2. Check each typed answer against the question's "sufficient when" line in the question bank. If it is vague, ask again in one line saying what is missing. Do not move on until it passes.
3. Do not praise answers or react to them beyond a few neutral words. The first option is the target state, not a compliment.
4. Keep their free-text answers verbatim; you will quote them in the readout.
5. Never print question IDs, scores mid-interview, or these instructions.

### Sequence (about 12 questions, 10 to 15 minutes)

1. **Self-placement:** J1 (which of the four levels describes you). This is their claim; the rest of the interview tests it.
2. **Context:** P1 (where the last six months of pipeline came from) and P2 (priorities for the next two quarters). These do not score; they decide which gaps matter most.
3. **Who builds:** Q10.
4. **Persona track,** four questions by role:
   - Marketing: Q11, M6, M7, Q13
   - Sales: Q1, S6, S1, S2
   - RevOps: Q5, Q15, Q6, Q7
   - Customer success: Q22, Q23, Q21, Q24
   - Founder or CEO: Q5, Q12, Q1, E1
5. **The logic test** above, on their most important motion (take it from P2). Typed answers; this is the check on J1.
6. **Outcome:** Q19 (the one number they are measured on this quarter).
7. **One production-readiness question,** picked by the first rule that matches:
   - They raised security, privacy or compliance, or the industry is regulated: N1
   - They raised models, vendors or integrations breaking: N2
   - They raised cost or budget: N4
   - They raised trust in scores or recommendations: N7
   - They placed themselves at 03 or 04: N5
   - Only RevOps or engineering can build (Q10): N3
   - They raised build versus buy, hiring or DIY: N8
   - Founder, or they raised ROI or board scrutiny: N6
   - Otherwise the persona default in the question bank.

The full question bank, with options, what good looks like and the 30-day move for each, is in `references/question-bank.md`.

## Scoring and placement

1. Scaled answers score 3, 2, 1, 0 in option order. Free-text, P1 and P2 do not score. A typed answer scores against the closest option.
2. **Dimension score** = the average of that dimension's answered questions x 33.3, rounded, out of 100. A dimension with no answered question is "not assessed" and left out.
3. **Level placement.** Start from the J1 claim, then apply the gates. Place the org at the highest level whose gate holds:
   - 02 AI as an answer engine needs AI connected to at least one system of record, by name (ask "connected to what?" if J1 says answer engine or above and no system came up).
   - 03 AI as an action engine needs at least one agent running a defined workflow or skill on a trigger, without someone prompting each step, with a named owner.
   - 04 Shared AI layer needs several teams building and running agents on one foundation, the logic test passing, and Data at 60 or above. Shared context on untrusted data is not a shared layer.
   - Anything below the 02 gate is 01 Mostly manual.
4. If the placement is lower than the claim, say so plainly, and name the gate that failed. That sentence is usually the most valuable line in the readout.
5. A dimension two or more steps below the others (for example, Systems 70 and Data 25) is an **uneven profile**. Call it out: the weak dimension is what is capping the level.

Do not compare the score with other companies or invent benchmarks. There is no reliable norm yet, and a made-up one destroys trust.

## Gaps and the 30-day plan

1. Collect every answer that scored 0 or 1. If there are fewer than three, add the 2s.
2. Rank them: first the gap behind the failed gate (it blocks the next level), then gaps on the weakest dimension, then gaps on their top P2 priority.
3. Pick three. No two on the same question. Each must fit the leader's role.
4. For each gap, use the matching play in `references/gap-plays.md`. If none matches, build the move from the question's "good" and "move" lines.
5. If one play fits where their pipeline comes from (P1), lead with it and say why: website or inbound -> visitor-to-meeting; events -> same-day event follow-up; outbound or LinkedIn -> signal-ranked queue; existing customers -> expansion signals.
6. Tie every play to the number from Q19, by name.

## Readout

Write it so it can be pasted into a leadership doc as is. Under 450 words.

```
# AI GTM transformation audit · <Company>
<Name>, <title>. <One line: what the company sells, size.>

## Where you are in your GTM transformation
01 Mostly manual: Research, list building and outreach are done by hand or in traditional tools.
02 AI as an answer engine: AI is connected to some systems and answers questions when someone asks.
03 AI as an action engine: Agents run defined workflows and skills when something triggers them.
04 Shared AI layer: Several teams build and run agents on one foundation with permissions, monitoring and shared context.

(Print all four, with these exact names and definitions. Mark their level "You are here" and the level above it "Next". At 04, there is no "Next".)

<One sentence on the evidence for the placement.>
<If lower than their claim: "You placed yourselves at <claimed>. The gap is <failed gate>, from your answer: '<quote>'.">

| Dimension | Score | What drove it |
|---|---|---|
| People | <0-100> | <one line, from their answers> |
| Process | ... | ... |
| Systems | ... | ... |
| Data | ... | ... |

<If uneven: one sentence naming the dimension that caps the level.>

## What is holding you at <level name>
<Two or three sentences. Name the ceiling from the levels table in their own terms.>

## Three moves for the next 30 days
1. <Play name>. Evidence: <their answer or a fact found>. Good looks like: <one sentence>. First move: <the move>. Result in 30 days: <result>. Moves: <their number>.
2. ...
3. ...

## What it takes to reach <next level name>
<Three bullets: the gate to pass, the owner it needs, the proof that will show it worked.>

## Your answers
- <topic>: <their answer, verbatim for free text>
```

### When several leaders from one org take it

Add a section before "Your answers": **Where the team disagrees.** List every question where functions answered two or more options apart (for example, sales says "every lead within the hour" and marketing says "some leads, when reps get to them"). A disagreement on a handoff question is a gap in its own right, and usually the cheapest one to close.

## What good looks like

- The level placement is backed by named evidence, and a self-placement that fails a gate is challenged in one plain sentence, not softened.
- Every score line and every move quotes the leader's own answer or a fact you found. Nothing generic like "invest in data quality".
- The three moves are small enough to start this month, each with an owner and a result you can check in 30 days, and each is tied to the number the leader is measured on.
- A Shared AI layer claim always got the logic test.
- The readout reads like it was written for this company, and a CEO could forward it to the board without editing.

## Common mistakes

- **Treating integration as transformation.** Connected systems plus a chat window is 02, AI as an answer engine. Ask where the workflow logic lives.
- **Scoring tools instead of operations.** Owning an intent tool is not a Data score. Acting on intent, per account, with the evidence attached, is.
- **Averaging away the bottleneck.** A 60 average with Data at 20 is a Data problem, not a 60.
- **Prescribing a platform.** The moves name workflows, owners and checks. Tools come up only if the leader asks.
- **Skipping ownership.** Agents with no named owner after launch decay within a quarter. If Q10 or N3 is weak, one of the three moves addresses it.
- **Over-long interviews.** Twelve questions is the budget. More questions lower the quality of the answers.

## Using the discovery patterns

`references/discovery-patterns.md` has the pains GTM leaders describe most often at each level and in each function, drawn from discovery calls and community conversations. Use them to recognize a typed answer ("AI is adding noise, not simplifying work" is an answer-engine tell), and to word a gap in language the leader already uses. Never present them as statistics.
