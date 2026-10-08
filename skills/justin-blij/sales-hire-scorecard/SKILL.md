---
name: sales-hire-scorecard
title: Sales hire scorecard
description: |
  Use this skill before interviews start for a sales, customer success or other GTM hire, and again after each interview to score candidates against it. Writes the motion of the seat, builds a scorecard of six to eight motion-fit criteria, force-ranked and weighted by the team, each with an owned interview question and anchored 1 to 4 scoring, then scores candidates on evidence from what they actually did, not where they did it. Ends with a ranked summary and one Yes/No decision for a human. Handles one candidate or a whole shortlist. Triggers on "build a scorecard", "interview scorecard", "how do we assess AEs", "what should we look for in a sales hire", "rank these candidates", "the panel keeps disagreeing", "they came from a great company", "hiring rubric", "who should we shortlist".
category: Hiring
tags: [Sales, Leadership]
---

# Sales hire scorecard

Runs in two modes. **Build** runs once, before the first interview, and produces a scorecard the whole panel agrees to in advance. **Score** runs after every interview and produces a ranked candidate list where every score points to the answer that earned it.

**The prime rule: score the motion, not the logo.** A rep who sold a famous product into inbound demand at a company everyone wanted to buy from has a different skill set from a rep who built pipeline from nothing for a product nobody had heard of. Both look great on a CV. Only one of them matches most hiring briefs. The scorecard asks how they sold, and to whom, before it asks where.

## Template placeholders

Replace every `{{...}}` before enabling. The setup checklist in `references/setup-customization-checklist.md` covers each one.

- `{{ATS}}`: where the role, candidates and interview feedback live
- `{{NOTES_TOOL}}`: interview recordings or notes, if you record interviews
- `{{REVIEW_CHANNEL}}`: where the scorecard and summaries are posted
- `{{HIRING_MANAGER}}`: who owns the ranking and the final call
- `{{PANEL}}`: the interviewers who sign the scorecard
- `{{CURRENCY}}`: currency for deal sizes in the seat motion

## Trial mode (recommended for the first role)

Build the scorecard and score candidates, but write nothing to `{{ATS}}`. Post every summary to `{{REVIEW_CHANNEL}}` marked TRIAL and let the panel run their usual process alongside it. At the end, compare who each process would have hired, and why. Switch writes on once the panel trusts the scores.

## Diagnostic questions (before the first build)

Ask these once per team.

1. Think of your best and worst sales hires of the last two years. What did the interviews miss about each?
2. Where does pipeline in this seat really come from, as a rough percentage?
3. Does the panel agree what "good" looks like before meeting candidates, or after?
4. How often does the final call go to the candidate the most senior interviewer liked?
5. Which criterion do you suspect you over-weight because it is easy to see in an interview?

## Build mode

### Step 1. Pull the inputs

- From `{{ATS}}`: the role, the job description, the target start date and the panel.
- From the hiring manager: the numbers behind the seat. If they are not known, ask for them before going further. A scorecard built on a guess at the motion scores the wrong things.
- If the team has a past scorecard for a similar seat, load it as a starting point, never as the answer.

### Step 2. Write the seat motion

One line each: average deal size in `{{CURRENCY}}`, sales cycle length, who the buyer is, where pipeline comes from, how complex the product is, and whether this is new business or growing existing accounts. This is the target every candidate is measured against.

### Step 3. Pick six to eight criteria

From `references/motion-fit-factors.md`. Choose the ones where a mismatch would actually sink the hire. Drop anything a good rep learns in their first month.

### Step 4. Force-rank and weight

No ties. The hiring manager decides the order. Then spread 100 points across the criteria in rank order using `references/scoring-method.md`, and mark up to two must-haves. The weights belong to the team running the hire, because they encode what this seat needs. There is no universal answer.

### Step 5. Assign questions and owners

Each criterion gets one primary question and one follow-up from the factor library, and one interviewer who owns it. No criterion goes unasked and none is asked three times.

### Step 6. Get it signed and lock it

Post the scorecard to `{{REVIEW_CHANNEL}}` with a Yes/No: "Agree scorecard v1 before the first interview?" Every `{{PANEL}}` member answers. Once agreed, it gets a version number and is locked. A change after interviews start creates a new version, and every candidate scored so far is re-scored against it.

## Score mode

### Step 7. Pull each interviewer's evidence

From `{{ATS}}` and `{{NOTES_TOOL}}`: each interviewer's written notes and scores for their owned criteria, with timestamps. Scores entered after a group discussion are tagged `(group)`.

### Step 8. Score against the anchors

1 to 4 per criterion, against the anchors in the scoring method. Every score cites the answer or example that earned it. A hypothetical answer caps at 2. No evidence, no score: mark it not assessed and assign the question to the next interviewer. Where two interviewers scored the same criterion two or more points apart, flag the gap first.

### Step 9. Rank, flag and post

Weighted total per candidate, plus any must-have scored 1, which fails regardless of the total. Post the summary and stop.

```
[Role] / scorecard v[n] / agreed by [panel] on [date]
Seat motion: deal [size] | cycle [length] | buyer [level] | pipeline [source] | [new business/expansion]
Criteria (rank, weight): 1. [ ] [w] 2. [ ] [w] ... | Must-haves: [ ]
Candidate | weighted score | must-have fails | not assessed | top evidence
[A]       | [ ]            | [ ]             | [ ]          | "[quote]"
[B]       | [ ]            | [ ]             | [ ]          | "[quote]"
Scorer gaps: [criterion, interviewers, scores] or none
Decision: Advance [names] to [next round]? Yes / No
          Fill the not-assessed gaps before deciding? Yes / No
```

### Step 10. Write back, after the decision

Only after a human answers:

- Log each candidate's scores and cited evidence as a note in `{{ATS}}`, with the scorecard version.
- Move stages only for the names the human said Yes to.
- Read every write back. Not found means retry once, then post a visible warning: "ATS write failed, manual entry needed".

Write failures never block the summary.

## Batch mode

Score mode handles a whole shortlist in one run. Rank only candidates scored on the same scorecard version. A candidate with not-assessed criteria is shown with those gaps, never ranked as if a 0 were a real score. Totals within five points are a tie, broken on the top-ranked criterion.

## Handoffs

The skill works on its own. When other parts of the hiring process exist, it feeds them:

- **After:** the ranked criteria, the evidence quotes and the scorer gaps are the rows a panel debrief should work from. A two-point scorer gap is usually the debrief's first item.
- **After the hire:** at month six, compare each criterion's score with how the hire is actually performing. Move the predictive criteria up for the next role.

## What good looks like

- The scorecard exists before anyone meets a candidate, and the panel signed it. Nobody changes the weights after seeing who they like.
- Every score has a quote or an example behind it. "Strong communicator" is not evidence. "Walked me through how they got a CFO to sponsor a 400k deal in their second month" is.
- The best operators ask for the numbers behind the numbers: attainment by year, not the best year; actual earnings, not on-target; how much pipeline was self-sourced.
- A mismatch on deal size or pipeline source shows up as a low score early, before the panel falls for the candidate's stories.
- Not assessed is a valid score. It means the next interview has a job to do.
- In sales hires the classic miss is the polished interviewer who sold an easy product. The scorecard catches them because the motion criteria do not reward polish.

## Anti-patterns

- **The copied rubric.** Last year's traits list, reused for a seat with a different motion.
- **Everyone scores 3.** No anchors, no evidence, no signal. The 1 to 4 scale exists to stop this.
- **Weights moved after the interviews.** The scorecard now describes the favourite candidate, not the seat.
- **The logo ranking.** A shortlist ordered by previous employer brand. Feels safe, predicts little.
- **Scoring the CV.** Points for what the CV claims, before anyone asked how it happened.

## Why the hard rules exist

- **Agree before the first interview.** Once the panel has met a candidate they like, every criterion bends toward that person. Agreement in advance is the only point at which the scorecard is about the seat.
- **Evidence for every score.** Interviewers remember how a candidate made them feel far better than what the candidate said. Written evidence is the only defence.
- **Hypotheticals capped at 2.** "I would start by..." describes a plan, not a track record. In sales the gap between the two is the job.
- **Must-haves override totals.** A high total can hide a fatal gap. The inbound-only rep who scores well everywhere else still cannot build pipeline in an outbound seat.

## Rules

- MUST agree and rank the criteria before the first interview.
- MUST score each interview independently, in writing, before any group discussion.
- MUST cite evidence for every score. NEVER score from the CV alone or from how the candidate made the interviewer feel.
- MUST treat a must-have scored 1 as a fail, whatever the total.
- MUST re-score every candidate when the scorecard version changes.
- MUST read back every write and report failures on the summary.
- NEVER include criteria that act as proxies for protected attributes: "culture fit" without a definition, years of experience used as a stand-in for age, "polish" or "presence" without a behaviour attached.
- NEVER advance, reject or rank a candidate without a human decision. The skill scores; people decide.
