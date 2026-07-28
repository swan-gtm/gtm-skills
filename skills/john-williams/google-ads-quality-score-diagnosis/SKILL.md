---
name: google-ads-quality-score-diagnosis
title: Quality Score diagnosis and prioritization
description: |
  Use this skill when Quality Score is low, CPCs feel high relative to competitors,
  or someone asks "why aren't my ads showing" without a budget explanation. Produces
  a spend-weighted, component-level fix list instead of a vague "improve relevance"
  note. Triggers: Quality Score, expected CTR, ad relevance, landing page experience,
  high CPCs, ad rank, "below average" component flags.
category: Ads
---

# Quality Score Diagnosis and Prioritization

Applies whenever a keyword-level quality signal is available and CPC or ad-rank
performance is in question.

## The play

1. Treat Quality Score as a diagnostic, not a KPI. Never optimize toward the score
   itself or report it as a headline metric — it exists to point at which of three
   components (expected click-through rate, ad relevance, landing page experience) is
   dragging a keyword down, each rated below average, average, or above average.
2. Weight the fix list by spend, not by score. A below-average component on a keyword
   burning real budget matters far more than the same flag on a keyword that barely
   spends — fix the expensive ones first, and don't chase score on low-volume
   keywords where the read is unreliable in the first place.
3. Route each below-average component to a different fix, because they don't share a
   cause: below-average expected CTR means the ad isn't compelling enough for the
   query it's showing on; below-average ad relevance means the ad and the query have
   drifted apart, usually from an ad group covering too many themes; below-average
   landing page experience means the page itself — speed, match to intent, ease of
   use — isn't holding up its end.
4. For ad relevance specifically, check ad group breadth before touching the ad copy.
   A group covering fifteen loosely-related terms with one ad can't be relevant to
   all of them — split it into tighter, single-theme groups before rewriting anything.
5. Give landing page experience issues time and the right owner — cite the estimated
   CPC savings across affected spend to justify the page work, since that's usually a
   different team's backlog item, not something to fix inside the account.
6. Re-check on a weekly cadence, not daily — day-to-day Quality Score noise from
   Google's own recalculation will make a fine account look like it's regressing.

## What good looks like

- The best diagnosis never treats a "below average" flag as one problem — it
  separates which of the three components is actually driving it, because the fix
  for each is completely different work.
- The common mistake is chasing Quality Score to 10. Scores of 7-8 are the realistic
  ceiling for most keywords; treating anything below 10 as broken burns effort with
  diminishing returns instead of moving to the next highest-spend keyword that
  actually needs the attention.
- A good fix list is spend-weighted and names the specific component driving each
  entry — a list that says "improve relevance" without saying which keywords, which
  component, and how much spend is affected hasn't actually diagnosed anything.

## Rules

- MUST weight prioritization by spend affected, not by score alone.
- MUST identify which specific component (expected CTR, ad relevance, landing page
  experience) is below average before recommending a fix.
- NEVER report Quality Score as a performance KPI on its own, and never optimize
  toward the number instead of the underlying component.
- NEVER pursue score improvements on keywords with too little volume for the
  component ratings to be a reliable read.
