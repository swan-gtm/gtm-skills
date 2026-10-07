---
name: panel-debrief-alignment
title: Panel debrief alignment
description: |
  Use this skill after an interview round for a sales, marketing, customer success or other GTM hire, when the hiring manager has panel feedback and a read on the candidate and needs to decide what happens next. Pulls each interviewer's written feedback and the candidate's debrief, builds one alignment map across every interviewer and the candidate, ranks the concerns with the exact move to resolve each, rates interest on both sides independently, and ends with a 48-hour momentum plan and one Yes/No decision for a human. Handles one candidate or a whole round. Triggers on "debrief the panel", "interview debrief", "the panel is split", "hiring committee", "should we move them forward", "they were fine", "is this a slow no", "candidate feedback", "we can't agree on this hire", "final round debrief", "are they still keen".
category: Hiring
tags: [Sales, Leadership]
---

# Panel debrief alignment

Runs after any interview round where two or more people formed a view: a panel, a final round, or a hiring manager plus the candidate's own debrief. Produces a decision, not a summary.

**The prime rule: never average the panel.** Two strong yeses and a quiet no do not add up to a yes. Disagreement is the data. The job is to find exactly where the reads split, why, and whether the split can be closed with evidence the process already holds.

## Template placeholders

Replace every `{{...}}` before enabling. The setup checklist in `references/setup-customization-checklist.md` covers each one.

- `{{ATS}}`: where candidates, interview stages and feedback live
- `{{NOTES_TOOL}}`: interview recordings or notes, if you record interviews
- `{{REVIEW_CHANNEL}}`: where the debrief card is posted for the hiring manager
- `{{HIRING_MANAGER}}`: who makes the call on each role
- `{{COMPLIANCE_OWNER}}`: who receives bias flags
- `{{DRIFT_WINDOW}}`: hours before a stalled process escalates (default **48**)

## Trial mode (recommended for the first three roles)

Run with every write to `{{ATS}}` switched off. Post the card to `{{REVIEW_CHANNEL}}` marked TRIAL, and let the hiring manager compare it with how they would have called it. Switch writes on once the cards match their judgment, or once they prefer the card.

## Diagnostic questions (before the first run)

Ask these once per team. They usually show where the debrief process is leaking.

1. Do interviewers write feedback before the group debrief, or does the group debrief happen first?
2. When the panel splits, who decides, and on what basis?
3. How often does a candidate hear a concern for the first time at rejection?
4. How long, on average, between the final interview and an offer or a no?
5. Which interviewer's "no" has turned out to be right most often?

## The play

### Step 1. Pull the inputs

- From `{{ATS}}`: the role, the agreed hiring criteria or scorecard if one exists (use its ranking), every interviewer's written feedback for this round, and the candidate's stage history.
- From `{{NOTES_TOOL}}`, if available: interview notes or transcripts for this round.
- The candidate's own read, from whoever holds the relationship (hiring manager, recruiter or talent partner): what they thought happened, what they were asked, where they felt strong and where they felt exposed.
- If no agreed criteria exist, ask the hiring manager for the three to six things this hire must prove, and use those.

Missing inputs are named at the top of the card, never filled with a guess. A debrief without the candidate's read runs the panel half only and says so.

### Step 2. Check for contamination

Compare each feedback timestamp with the group debrief time. Feedback written after a group discussion, or only given verbally in one, is tagged `(group)` and cannot on its own make a row ALIGNED. Once the most senior person speaks, everyone else anchors to them and the independent signal is gone.

### Step 3. Build the alignment map

One row per hiring criterion, then one row per concern anyone raised. Classify each row against the evidence bar in `references/alignment-states-and-scales.md`:

- **BLIND**: one side raised something the other has not registered at all. Worked first, every time.
- **DIVERGENT**: both sides engaged, different reads. Including interviewer against interviewer.
- **UNCLEAR**: a feeling with no example. Converted into a question, never decided on.
- **ALIGNED**: both sides read it the same way, with evidence from each.

Every row cites a quote or an observed behaviour from each side. "Great energy" is not evidence.

### Step 4. Rate interest on both sides, separately

Panel conviction and candidate intent, each 1 to 5 against the anchors in the same reference, each with a quote. Flag any single interviewer two or more points from the rest of the panel. That outlier is usually the most important row on the map.

### Step 5. Translate the soft language

Run every piece of feedback through `references/vague-positive-phrase-library.md`. Praise with no example, no next step and no urgency is a slow no. Name it in those words and attach the forcing question.

### Step 6. Broker each concern

For every BLIND and DIVERGENT row: whose concern it is, whether it is solvable, and the move. Four kinds, lightest first: unused evidence the candidate has not shown, a targeted reference question, a short paid or time-boxed work sample, or a direct question. Patterns that recur in GTM hires are in `references/brokering-moves.md`. Log every resolved concern there, so the next debrief inherits a move that already worked.

### Step 7. Write the momentum plan

Three actions, each with an owner and a deadline inside `{{DRIFT_WINDOW}}` hours. Where the owner is waiting on someone else, the plan states what happens at the deadline. "Waiting on client" or "waiting on the panel" is not an action.

### Step 8. Post the card and stop

Post the debrief card to `{{REVIEW_CHANNEL}}`, full content every time, never a pointer elsewhere. A human decides.

```
[Candidate] / [Role] / Round [n] / [date]
Reads in: [interviewers] + candidate ([who debriefed them]) | Missing: [none or who] | Contaminated: [none or who]
Panel conviction: [1-5] "[quote]" | Outlier: [name, score] | Candidate intent: [1-5] "[quote]"
BLIND ([n]): [one line each]
DIVERGENT ([n]): [one line each]
UNCLEAR ([n]): [question to ask, and who asks it]
Slow-no flags: [phrase, who said it, forcing question]
Bias flags: [any feedback excluded and why, or none]
Momentum: 1. [action] [owner] [by when] 2. ... 3. ...
Decision: Advance to [next step]? Yes / No
          Broker [top concern] before deciding? Yes / No
```

### Step 9. Write back, after the decision

Only after the hiring manager answers:

- Log the debrief as a note on the candidate in `{{ATS}}`: states, top concerns, the decision and who made it.
- Move the stage only if the answer was Yes, and only to the stage named on the card.
- Create the momentum actions as tasks with their owners and deadlines.
- Read every write back. Not found means retry once, then post a visible warning on the card: "ATS write failed, manual entry needed". Never report a write that did not land.

Write failures never block the card. The card is the primary output.

## Batch mode

When a round has several candidates, build one card per candidate, then a round summary: candidates ranked by panel conviction, BLIND counts, slow-no flags, and the one decision the hiring manager must make first. Never compare candidates on a criterion one of them was not assessed on.

## Handoffs

The skill works on its own. When other parts of the hiring process exist, it uses them:

- **Before:** if the team agreed a ranked scorecard before interviews, use its criteria and ranking as the map's rows.
- **After:** when the decision is to make an offer, carry the candidate's stated reasons for moving, in their own words, and the counter-offer signals heard in the debrief, onto the card. The offer stage needs both.

## What good looks like

- The hiring manager reads the card in two minutes and makes the call without re-listening to anyone.
- The single most dangerous item sits at the top: the thing one side knows and the other does not.
- Split panels get resolved with new evidence, never with the most senior voice or a vote.
- The quiet interviewer with one specific doubt gets heard first. They are usually right about something the enthusiasts missed.
- In sales hires the classic miss is rating the pitch, not the pipeline. The candidate who interviews best often sold the easiest product. Good debriefs ask how the numbers were made: deal size, cycle length, self-sourced versus handed, and who else was in the room.
- By the third role, most concerns match a brokering pattern already logged, and the debrief takes half the time.

## Anti-patterns

- **The averaged score.** Three interviewers, three numbers, one mean. Hides the outlier, which is the signal.
- **The group-first debrief.** Everyone talks, the VP speaks first, the feedback form is filled in afterwards. Every row is contaminated.
- **"Let's see a couple more."** Not a decision. It is a no that nobody wants to own, and the candidate signs elsewhere while the panel waits.
- **The secret concern.** The panel doubts something and the candidate never hears it until the rejection email. A candidate cannot answer a concern they do not know exists.
- **Quoting the interviewer to the candidate.** Broker the substance, protect the source.

## Why the hard rules exist

- **BLIND before DIVERGENT.** The usual failure is a strong candidate rejected for a gap they could have closed in one conversation. They were never told it was a gap.
- **Independent written feedback first.** Senior voices set the anchor. In a group-first debrief, the most junior interviewer's specific doubt rarely survives the first five minutes.
- **The drift window.** Strong sales candidates are usually in more than one process. The company that goes quiet for a week after a final round tends to lose to the one that did not.
- **Bias flags out of the decision.** Comments about age, family, accent or appearance turn up in panel feedback more often than teams expect. Left in, they shape the decision and expose the company.

## Rules

- MUST collect individual written feedback before any group discussion, or flag the contamination.
- MUST rate panel and candidate interest independently, each with a quote.
- MUST work BLIND items before DIVERGENT items.
- MUST end with a Yes/No decision for a human. NEVER advance, reject or make an offer from this skill.
- MUST read back every write and report failures on the card.
- NEVER infer one side's read from the other side's read. Missing input is named, not guessed.
- NEVER pass an interviewer's words to the candidate verbatim.
- NEVER let feedback about age, family plans, accent, appearance, health or any other protected attribute into the decision. Exclude it, flag it on the card, and route it to `{{COMPLIANCE_OWNER}}`.
