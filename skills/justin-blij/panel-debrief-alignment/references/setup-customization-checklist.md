---
title: Setup and customization checklist
description: Trigger setup, placeholders, policy decisions and the behaviour that must never be removed.
---

# Setup and customization checklist

## 1. Trigger setup

The skill fires when an interview round closes for a candidate, or on demand ("debrief the panel for [candidate]"). Reference trigger:

```
Interview round [n] has closed for [candidate], [role].

Load and follow the <Panel debrief alignment> skill in full.

Context for this run:
- Candidate and role: [ATS link or ID]
- Interviewers this round: [names]
- Group debrief time, if one happened: [time]
- Who holds the candidate relationship: [name]
```

- [ ] `{{ATS}}` is connected and returns per-interviewer feedback with timestamps. The contamination check depends on the timestamps.
- [ ] Interviewers submit feedback in `{{ATS}}` before any group debrief. If your team debriefs verbally, change that first. The skill can flag contamination; it cannot remove it.
- [ ] Someone owns getting the candidate's read within 24 hours of the final interview.
- [ ] `{{REVIEW_CHANNEL}}` exists and `{{HIRING_MANAGER}}` actually reads it.

## 2. Placeholders

- [ ] `{{ATS}}`, `{{NOTES_TOOL}}`, `{{REVIEW_CHANNEL}}`, `{{HIRING_MANAGER}}`, `{{COMPLIANCE_OWNER}}`, `{{DRIFT_WINDOW}}` all filled, or the optional ones deleted.
- [ ] If you do not record interviews, delete `{{NOTES_TOOL}}` and its line in Step 1.
- [ ] Map "advance" to your own stage names in `{{ATS}}`.

## 3. Policy decisions

- [ ] **Start in trial mode** for the first three roles. ATS writes off, cards marked TRIAL.
- [ ] **Drift window.** 48 hours is the default. Shorter for SDR and high-volume roles, longer only if your process genuinely needs it.
- [ ] **Who sees bias flags.** Decide who `{{COMPLIANCE_OWNER}}` is before the first flag appears, not after.
- [ ] **Work samples.** Decide now whether you pay for them and the maximum time you will ask of a candidate. Never use a free strategy project.
- [ ] **Brokering log.** Decide where resolved concerns are logged so the library compounds across roles.

## 4. Behaviour that must never be removed

- BLIND rows are worked before DIVERGENT rows.
- Panel and candidate interest are rated separately, each with a quote.
- Feedback written after a group discussion is tagged and cannot make a row ALIGNED on its own.
- Missing inputs are named at the top of the card, never inferred.
- Interviewer words are never passed to the candidate verbatim.
- Protected-attribute comments are excluded from the decision and routed to `{{COMPLIANCE_OWNER}}`.
- No stage change, rejection or offer without a human Yes.
- Every ATS write is read back, and a failed write is reported on the card.
