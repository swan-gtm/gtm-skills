---
name: lookalike-candidate-sourcing
title: Source candidates who look like your best hire
description: "Use this skill when a role worked and you want more of that person, or when you are backfilling someone strong and a job-board post is not going to find them. Takes one exemplar profile and returns a ranked, scored shortlist with the reasoning behind each score visible."
category: Prospecting
tags: [Recruiting, Sourcing]
---

Use this when one hire worked and you want more like them. It produces a ranked shortlist where every score decomposes into title, skills, seniority, and location, so a hiring manager can argue with it.

## The play

1. **Take one exemplar, not a job description.** A JD describes what someone wrote down. A person who is actually good in the role describes what worked. Start from the exemplar's real current title, skills, and location.

2. **Push filters into the search, not into post-processing.** Role family, country, city, and current-role-only belong in the query. Filtering a large result set client-side wastes lookups and hides how narrow you actually were.

3. **Start broad, then tighten once.** Role family plus two skills plus a country is a good opening net. Stacking an exact title, an all-skills-match, and a city returns zero and looks like "nobody exists" when it is really a bad query.

4. **Decide whether to enrich.** Without enrichment you get a cheap keyword-ordered list. With it you get skills, education, and geography per candidate, at one extra lookup each. Enrich 20, not 200, until the shortlist direction is confirmed.

5. **Score transparently out of 100:**
   - **Title match, 40** — exact title 40, same role family at any seniority 25, different family 0.
   - **Skills overlap, 30** — shared skills over the exemplar's skill count, times 30, compared on normalized names.
   - **Seniority, 15** — same level 15, one level off 7, further 0. Infer from title prefix: Senior, Staff, Principal, Head of, VP.
   - **Location, 15** — same city 15, same metro 10, same country 5.

6. **Drop the exemplar** before ranking. Search returns them, they score 100, and it makes the list look broken.

7. **Return a table**, not JSON. Name, current title, company, location, score, and the one line explaining the score.

## What good looks like

- The strongest sourcers treat a zero-result search as information about the query, not the market, and can say which filter they loosened and why.
- The mediocre version returns fifty unranked names and calls it a pipeline, leaving the hiring manager to do the actual sourcing work.
- A score is only useful if it decomposes. "77" means nothing; "77: exact title, 6 of 9 skills, one level junior, same metro" is a conversation.
- You know it is good when the hiring manager disagrees with a specific score for a specific reason. That means they can see the reasoning.

## Rules

- MUST remove the exemplar from their own results.
- MUST show the score breakdown, never a bare number.
- MUST start broad and tighten deliberately, one filter at a time.
- NEVER infer salary, notice period, or willingness to move. That data is not in a public profile.
- NEVER present a keyword-ordered list as a ranked one when enrichment was skipped. Say the scores were not computed.
