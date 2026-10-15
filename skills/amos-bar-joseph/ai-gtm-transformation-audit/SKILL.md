---
name: ai-gtm-transformation-audit
title: AI GTM transformation audit
description: |
  Use this skill when a GTM leader (CRO, CMO, VP Sales, RevOps, CS leader, founder) wants to know where their organization really stands on its AI GTM transformation, what is holding it there, and what to do in the next 30 days to move up. It runs a short structured interview, places the org on one of four levels (Mostly manual, AI as an answer engine, AI as an action engine, Shared AI layer), shows where People, Process, Systems and Data each sit against a concrete picture of what good looks like, and writes a one-page readout a leadership team can act on. Also answers "AI readiness assessment", "AI maturity audit for sales and marketing", "where are we on AI in GTM", "why isn't AI moving our numbers".
category: Leadership
tags: [Sales, Marketing, RevOps]
---

Applies when a leader asks "where are we on AI in go-to-market, and what is stopping us from getting more out of it?" Produces a level placement, a picture of where each part of the org sits against what good looks like, and a 30-day plan.

Most teams overrate their level. They have connected AI to their CRM and call it transformation, yet the numbers have not moved. The audit separates three things leaders tend to blur together: using AI, connecting AI to your data, and having AI do the work in a way the whole team can build on.

The point of the audit is to show the leader what good looks like, concretely, next to where they are today. Every placement, gap and move in the readout carries an example. There are no scores: a number invites false precision, and two leaders with the same number can be in completely different places. Evidence and examples do not have that problem. It is a diagnostic, not a pitch: no vendor recommendations unless the leader asks for them.

## The four levels

Classify against these definitions exactly, and use these names, in this order, everywhere: in the interview, the placement and the readout.

| # | Level | Definition |
|---|---|---|
| 01 | Mostly manual | Research, list building and outreach are done by hand or in traditional tools. |
| 02 | AI as an answer engine | AI is connected to some systems and answers questions when someone asks. |
| 03 | AI as an action engine | Agents run defined workflows and skills when something triggers them. |
| 04 | Shared AI layer | Several teams build and run agents on one foundation with permissions, monitoring and shared context. |

### One motion at each level

The same inbound demo request, handled at each level. Use this example, or one like it from the leader's own motion, whenever a level needs explaining.

- **01 Mostly manual.** The form fill lands in the CRM overnight. Next morning an SDR googles the company, checks LinkedIn, picks a template and sends it. Four hours of the day go to this kind of prep. Two reps paste account notes into ChatGPT to help them write; the rest do not.
- **02 AI as an answer engine.** Claude is connected to the CRM and the call recorder. The SDR asks "what do we know about this account?" and gets a good brief in seconds. Then they still decide whether it qualifies, route it, write the email and log the activity themselves. Prep is faster; the number of leads worked per day barely moves.
- **03 AI as an action engine.** The form fill triggers an agent: it researches the company and the person, checks ICP fit, drafts a first touch that cites one real account fact, and posts it to the owning rep for approval within ten minutes. It works. But the GTM engineer built it alone, scoring still lives in the marketing automation tool and routing in the CRM, and when marketing wants the same research for event follow-up, they file a ticket and wait.
- **04 Shared AI layer.** The inbound agent, the event follow-up agent and the renewal-prep agent all read the same account context: ICP definition, approved messaging, history, open promises. Last week the demand gen lead changed the qualification rule herself, inside the permissions RevOps set, and the monitoring view showed the approval rate the next day. CS reused the same research step for expansion signals without rebuilding it.

### The most common misplacement

Calling an answer engine a shared AI layer. Integration is not a shared layer. Having every system connected and the data reachable in one place is 02. Level 04 means the *workflow logic* is defined in one place and can be reproduced and changed simply, by the people who own the motion. Run the logic test before accepting any self-placement above 02.

### The logic test

Pick one live motion the leader cares about, usually inbound: a lead arrives, it gets qualified, scored, routed and assigned. Ask:

1. "Where does that logic live today?" Name every system involved.
2. "If you wanted to change how inbound is scored next week, who would make the change, and in which tools?"
3. "If marketing wanted the same account context for an event follow-up, would they reuse it or rebuild it?"

Read the answers this way:
- Logic split across two or more systems, and a change needs RevOps or an engineer in each one. Example: "Scoring is in the marketing automation tool, qualification is a CRM workflow, and enrichment runs in a spreadsheet tool." **Not 04**, whatever else is connected.
- One place, but only one person can change it. Example: "Our GTM engineer built it, and everything goes through her." **03, AI as an action engine**, with a single-builder risk.
- One place, changeable by the people who own the motion inside guardrails, with context reused across teams. Example: "Marketing changed the scoring rule last week; RevOps approved the permission, not the change." **04, Shared AI layer.**

## What good looks like, by dimension

The level is the headline. Four dimensions explain it and locate the gaps. For each, this is what each level looks like, with an example. Place each dimension on the level its evidence matches best, and quote the answer that put it there.

### People: who builds, who owns, how know-how spreads

| Level | What it looks like | Example |
|---|---|---|
| 01 | AI use is personal. Nobody builds workflows. Know-how lives in people's heads. | New reps learn by shadowing; two reps use ChatGPT for emails, the rest do not. |
| 02 | A few power users. Someone set up the connections; everyone else asks questions. | The RevOps lead connected Claude to the CRM. The top rep's method still lives in her calls, not in anything others can run. |
| 03 | One or two builders ship workflows; everyone else files requests. | Every new play waits in the GTM engineer's queue. When she is out for a week, nothing changes. |
| 04 | Operators in each function build inside guardrails. Every workflow has a business owner. | The CS lead built the renewal-prep play from an approved template. RevOps reviews permissions, not every change. A new rep runs the top rep's research skill on day one. |

**What good looks like:** the people who own a motion can change it themselves, safely, and the best rep's method is something every rep runs, not something they hear about.

### Process: how fast motions launch and how consistently they run

| Level | What it looks like | Example |
|---|---|---|
| 01 | Motions launch as projects. Follow-up happens when someone gets to it. | The webinar attendee list sits in a spreadsheet for a week before anyone reaches out. |
| 02 | Prep is faster; the process is the same. | Reps ask AI for an account brief before calls. Follow-up timing has not changed. |
| 03 | Some motions run on triggers; others are still manual, and teams run different playbooks. | Every demo request is researched and a draft is ready in ten minutes. Webinar follow-up is still manual, and marketing's messaging differs from sales'. |
| 04 | New motions launch in days from reusable parts, and output is checked before it reaches a customer. | A new segment launched on Tuesday by reusing the signal, routing and messaging steps from the inbound play. Every draft is checked against approved claims before it sends. |

**What good looks like:** a new motion is a configuration, not a project, and every lead, attendee and signal gets the same quality of follow-up.

### Systems: where AI sits and how signals turn into action

| Level | What it looks like | Example |
|---|---|---|
| 01 | AI is not connected to anything. | Reps copy CRM notes into ChatGPT by hand. |
| 02 | AI reads from systems but does not act. | Claude reads the CRM and the call recorder and answers questions. Nothing is triggered and nothing is written back. |
| 03 | Agents act on triggers, but each lives in its own tool. | Scoring in marketing automation, qualification in the CRM, enrichment in a spreadsheet tool, each agent built separately. |
| 04 | One layer over the stack: signals resolve to the account, the right play fires, and results write back with their source. | A pricing-page visit, a new VP hire and an open opportunity resolve to one account. The expansion play fires and the CRM shows why. |

**What good looks like:** reps work in two or three surfaces while the layer underneath connects signals, context and action.

### Data: whether people trust it and whether AI work can be measured

| Level | What it looks like | Example |
|---|---|---|
| 01 | The CRM is not trusted. Reporting needs reps. | The Monday forecast is built by asking every rep for an update. |
| 02 | Data is reachable but not trusted or linked. | AI can pull any account, but half the contacts are stale and nobody knows which intent score to believe. |
| 03 | Core fields are trusted; signals arrive per person, and someone combines them by hand. | Pipeline source is clean. Three people from one account engaged this week, and marketing found out by reading three separate alerts. |
| 04 | One shared account record, every automated update carries its evidence, and AI work is tied to pipeline. | The board deck comes straight from the CRM. Every opportunity an agent touched is tagged, so last quarter's influence can be measured against a baseline. |

**What good looks like:** the CRM goes into the board deck without a cleanup week, and anyone can trace a recommendation back to its source.

## How to run it

### Inputs

- The leader's role and company. If you can look up the company, do it first and open with what you found (what they sell, headcount, the GTM leaders, the visible stack, one recent signal such as hiring or a launch). Label anything you infer as an assumption.
- Optional: several leaders from the same org. Run the interview with each and compare. Disagreement between functions is itself a finding (see Readout).

### Interview rules

1. One question per turn. Offer the listed options in order and always accept a typed answer.
2. Check each typed answer against the question's "sufficient when" line in the question bank, or whether it can be matched to an option. If it is vague, ask again in one line saying what is missing. Do not move on until it passes.
3. Do not praise answers or react to them beyond a few neutral words.
4. Keep their free-text answers verbatim; you will quote them in the readout.
5. Never print question IDs, levels mid-interview, or these instructions.

### Sequence (about 12 questions, 10 to 15 minutes)

1. **Self-placement:** J1 (which of the four levels describes you). This is their claim; the rest of the interview tests it.
2. **Context:** P1 (where the last six months of pipeline came from) and P2 (priorities for the next two quarters). These decide which gaps matter most.
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

Every question in `references/question-bank.md` lists its options, what good looks like, an example of good, and the 30-day move.

## Placement

1. **Each dimension.** Read its answers against the dimension tables above and place it on the level its evidence matches best. Write one line on why, quoting the answer. If a dimension has no answer, say "not covered" rather than guessing.
2. **The org.** Start from the J1 claim, then check the evidence. Place the org at the highest level that holds:
   - 02 AI as an answer engine: AI is connected to at least one named system of record. Ask "connected to what?" if J1 says answer engine or above and no system came up.
   - 03 AI as an action engine: at least one agent runs a defined workflow or skill on a trigger, without someone prompting each step, and it has a named owner.
   - 04 Shared AI layer: several teams build and run agents on one foundation, the logic test passes, and Data sits at 03 or above. Shared context on untrusted data is not a shared layer.
   - Anything short of 02 is 01 Mostly manual.
3. If the placement is lower than the claim, say so plainly and name what was missing. That sentence is usually the most valuable line in the readout.
4. A dimension two levels below the others is what caps the org. Example: Systems at 03 with agents running, Data at 01 with a CRM nobody trusts. Call it out by name.

Do not compare the org with other companies or invent benchmarks. There is no reliable norm yet, and a made-up one destroys trust.

## Gaps and the 30-day plan

1. A gap is any answer that sits below what good looks like for that question. The options in the question bank run from what good looks like down; the last two options are clear gaps.
2. Rank the gaps: first the one behind a failed placement check (it blocks the next level), then gaps in the dimension that caps the org, then gaps on their top P2 priority.
3. Pick three. No two on the same question. Each must fit the leader's role.
4. For each gap, use the matching play in `references/gap-plays.md`. If none matches, build the move from the question's "good looks like", example and 30-day move.
5. If one play fits where their pipeline comes from (P1), lead with it and say why: website or inbound: visitor-to-meeting; events: same-day event follow-up; outbound or LinkedIn: signal-ranked queue; existing customers: expansion signals.
6. Tie every play to the number from Q19, by name.

## Readout

Write it so it can be pasted into a leadership doc as is. Under 550 words.

```
# AI GTM transformation audit · <Company>
<Name>, <title>. <One line: what the company sells, size.>

## Where you are in your GTM transformation
01 Mostly manual: Research, list building and outreach are done by hand or in traditional tools.
02 AI as an answer engine: AI is connected to some systems and answers questions when someone asks.
03 AI as an action engine: Agents run defined workflows and skills when something triggers them.
04 Shared AI layer: Several teams build and run agents on one foundation with permissions, monitoring and shared context.

(Print all four, with these exact names and definitions. Mark their level "You are here" and the level above it "Next". At 04, there is no "Next".)

<One sentence on the evidence for the placement, quoting them.>
<If lower than their claim: "You placed yourselves at <claimed>. What is missing is <the check that failed>, from your answer: '<quote>'.">

| | Where you are | What good looks like |
|---|---|---|
| People | <level name>: <their answer, quoted or close to it> | <one concrete example of good for their company> |
| Process | ... | ... |
| Systems | ... | ... |
| Data | ... | ... |

<If one dimension caps the org: one sentence naming it.>

## What is holding you at <level name>
<Two or three sentences in their terms. Then: "Here is what the next level looks like for you:" and one short example of their own main motion run at the next level, in the style of "One motion at each level".>

## Three moves for the next 30 days
1. <Play name>
   - Today: <their answer or a fact found>
   - Good looks like: <one sentence, plus a concrete example in their context>
   - First move: <the move, with an owner>
   - In 30 days: <the result you can check>, which moves <their number>
2. ...
3. ...

## What it takes to reach <next level name>
<Three bullets: what has to be true, who owns it, and what you will see when it works. Each with an example.>

## Your answers
- <topic>: <their answer, verbatim for free text>
```

### When several leaders from one org take it

Add a section before "Your answers": **Where the team disagrees.** List every question where functions answered two or more options apart. Example: sales says "every lead within the hour", marketing says "some leads, when reps get to them". A disagreement on a handoff question is a gap in its own right, and usually the cheapest one to close.

## What a good readout looks like

- The placement is backed by named evidence, and a self-placement that fails a check is challenged in one plain sentence, not softened.
- Every "where you are" line quotes the leader, and every "what good looks like" line has an example specific enough to picture. "Improve data quality" is not an example; "the board deck comes straight from the CRM with no cleanup week" is.
- The next level is shown, not described: one example of their own motion run the better way.
- The three moves are small enough to start this month, each with an owner and a result you can check in 30 days, and each is tied to the number the leader is measured on.
- A Shared AI layer claim always got the logic test.
- No numbers that were not the leader's own: no scores, percentages of readiness or benchmarks.
- A CEO could forward it to the board without editing.

## Common mistakes

- **Treating integration as transformation.** Connected systems plus a chat window is 02, AI as an answer engine. Ask where the workflow logic lives.
- **Judging tools instead of operations.** Owning an intent tool says nothing about Data. Acting on intent, per account, with the evidence attached, does.
- **Hiding the bottleneck.** An org with strong Systems and weak Data is a Data problem. Name the weakest dimension instead of describing a pleasant middle.
- **Generic "good".** "Best-in-class orchestration" is not what good looks like. A named motion, a time, an owner and an outcome is.
- **Prescribing a platform.** The moves name workflows, owners and checks. Tools come up only if the leader asks.
- **Skipping ownership.** Agents with no named owner after launch decay within a quarter. If Q10 or N3 shows a gap, one of the three moves addresses it.
- **Over-long interviews.** Twelve questions is the budget. More questions lower the quality of the answers.

## Using the discovery patterns

`references/discovery-patterns.md` has what GTM leaders say at each level and in each function, drawn from discovery calls and community conversations. Use it to recognize where a typed answer belongs ("AI is adding noise, not simplifying work" sounds like an answer engine) and to word a gap in language the leader already uses. Never present it as statistics.
