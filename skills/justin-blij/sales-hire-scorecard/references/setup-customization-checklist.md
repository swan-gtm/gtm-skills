---
title: Setup and customization checklist
description: Trigger setup, placeholders, policy decisions and the behaviour that must never be removed.
---

# Setup and customization checklist

## 1. Trigger setup

Two triggers. Build mode fires when a role opens. Score mode fires when an interviewer submits feedback, or on demand. Reference triggers:

```
A new role has opened: [role].

Load and follow the <Sales hire scorecard> skill in Build mode.

Context for this run:
- Role: [ATS link or ID]
- Hiring manager: [name]
- Panel: [names]
```

```
Interview feedback has been submitted for [candidate], [role].

Load and follow the <Sales hire scorecard> skill in Score mode.

Context for this run:
- Candidate and role: [ATS link or ID]
- Scorecard version: [v]
```

- [ ] `{{ATS}}` returns each interviewer's notes with timestamps.
- [ ] Every `{{PANEL}}` member knows which criteria they own before their interview.
- [ ] `{{REVIEW_CHANNEL}}` exists and `{{HIRING_MANAGER}}` reads it.

## 2. Placeholders

- [ ] `{{ATS}}`, `{{NOTES_TOOL}}`, `{{REVIEW_CHANNEL}}`, `{{HIRING_MANAGER}}`, `{{PANEL}}`, `{{CURRENCY}}` all filled, or the optional ones deleted.
- [ ] Map "advance" to your own stage names.

## 3. Policy decisions

- [ ] **Start in trial mode** for the first role.
- [ ] **Where locked scorecards live**, with their version history.
- [ ] **Must-haves.** Decide whether a must-have fail stops the process at once, or goes to the hiring manager as a flag.
- [ ] **Month-six review.** Put a date in the calendar now to compare scores with performance.
- [ ] **Criteria language.** Review every criterion for proxies of protected attributes before the first build.

## 4. Behaviour that must never be removed

- The scorecard is agreed and locked before the first interview.
- Every score cites evidence. No evidence means not assessed.
- Hypothetical answers cap at 2.
- Not assessed never counts as a real score in a ranking.
- A must-have scored 1 fails regardless of the total.
- A scorecard change re-scores every candidate.
- No stage change without a human Yes.
- Every write is read back, and failures are reported on the summary.
