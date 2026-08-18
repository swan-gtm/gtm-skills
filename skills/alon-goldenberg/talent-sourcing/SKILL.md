---
name: talent-sourcing
title: Talent sourcing
description: |
  Use this skill when you need to find, source, or recruit candidates for a role —
  "find candidates for", "source engineers in", "who can I hire for", "find me a
  [role] in [city]", "build a candidate list", "recruiting for", "talent search",
  "who's available for", "find potential hires" — or when a job description is
  pasted with a sourcing request. Produces a ranked, tiered candidate report with
  profiles, skills, availability signals, and contact signals, deduplicated against
  every previous search for the same role. Not for salary benchmarking or job-market
  research, and not for researching one already-known person.
category: Research
tags: [Leadership]
---

# Talent sourcing

Runs when someone needs a candidate list for an open role — a title and location, a pasted job description, or a vague "who could we hire for this". Produces a tiered candidate report (Strong / Partial / Stretch) with per-candidate profiles, availability and contact signals, and a hiring-outlook read — with repeat candidates from earlier runs flagged instead of re-pitched as new.

## The play

### 1. Turn the request into a search brief

Extract five fields: **role** (title or function), **location** (city, metro, region, or remote), **skills/requirements** (technologies, years, domain), **seniority** (junior → C-level), and **source preference** (specific platforms or all). If a full job description was pasted, pull the fields out of it rather than asking again. If the role itself is missing or ambiguous, ask one question — "What role, and where?" — and stop until answered.

Then confirm the brief back before searching: role, location, key skills, seniority, and the platforms you intend to sweep. Searches are cheap but a wrong brief wastes the whole run; a ten-second confirmation is the highest-leverage step in the play.

### 2. Fan out searches across platforms in parallel

One search lane per platform, run simultaneously, never sequentially: professional-network profiles, resume boards, code-hosting profiles (technical roles only — skip this lane entirely for sales, marketing, and operations roles), and startup-talent / community sources. Query construction per platform — site-scoped operators, availability-phrase patterns, the two-query rule per lane, and the fallback ladder when a platform returns nothing — is in `references/source-playbook.md`. Read it before writing the first query.

Each lane returns raw candidate leads: name if visible, profile URL, current title, location snippet, inferred skills, and any availability phrase ("open to work", "seeking", "available") with its date and source URL.

### 3. Extract the top profiles — inside a budget

Aim for 10–20 unique profiles across all lanes; extract full details for at most 15. If the lanes surfaced more, triage by relevance (seniority match + skill overlap + location match) *before* extracting — extraction is the expensive step, so spend it on the plausible ones, not the first ones found.

From each profile pull: full name, current role and company, location, skills/stack, experience summary (years, notable employers), education, availability signals, and contact signals (email, personal site, code-hosting handle). When a profile sits behind a login wall and extraction fails, keep the search-snippet summary and note "full profile unavailable — login required" — never drop the candidate just because the page wouldn't open.

### 4. Score and tier

Score each candidate 1–10 on weighted signals — role match 30%, skill overlap 30%, location 20%, seniority 10%, availability 10% — and group into Tier 1 (Strong, 7–10), Tier 2 (Partial, 4–6), Tier 3 (Stretch, 1–3). The full rubric, tier definitions, and a worked scoring example are in `references/scoring-rubric.md`; read it before assigning any score, and score against the confirmed brief, not against what the search happened to return.

### 5. Dedup against role memory

Keep a running file per role in your workspace (one file per role slug, e.g. `talent/senior-ml-engineer-remote-us.md`). Before presenting, load it: any candidate surfaced in a prior run for this role gets marked `(previously surfaced)` — still listed, still scored, but never re-presented as a fresh find. This is what makes the second and third run on the same role useful instead of noise. After presenting, write every candidate from this run back into the file with date and score.

### 6. Present the report

Follow the structure in `references/report-format.md` exactly: header with platforms searched and tier counts, TL;DR, tiered candidate entries, and a closing "What this means" hiring-outlook read. Every Tier 1 candidate gets a one-sentence "Why this candidate". Missing data is written as "unknown" — a field is never guessed to make an entry look complete.

### 7. Offer the next move

Close with concrete options: go deeper on one candidate (full profile + contact discovery), broaden (remote, relaxed seniority, more platforms), narrow (add a required skill, tighten location), or export the list as a CSV or document. If the run found fewer than five candidates total, don't present a thin list as an answer — say so, propose the specific broadening (usually location → remote, or seniority down one notch), and ask before re-running.

## What good looks like

- The best operator notices **availability signals with dates** first — a candidate who posted "open to work" last month outranks a slightly better-matched candidate with no availability signal, because reply rates, not resume quality, decide whether a sourcing list converts. They also read the tier *distribution* as market data: a thin Tier 1 with a fat Tier 3 means the brief is over-constrained for this market, and they say so instead of padding Tier 1.
- The mediocre version is a flat list of profile links: no scores, no tiers, GitHub searched for a sales role, the same candidates re-presented as new on the second run, and fields silently invented to make entries look uniform.
- Output is good when a hiring manager can act on it in five minutes: every Tier 1 entry has a "why", an availability read with a source, and at least one contact path — and the "What this means" line tells them whether to move fast (thin supply) or be picky (deep supply).

## Rules

- MUST confirm role, location, skills, and seniority with the requester before searching.
- MUST run platform lanes in parallel and cap deep extraction at 15 profiles, triaged by relevance first.
- MUST check the role's running memory file and mark repeat candidates `(previously surfaced)`.
- MUST attach a date and source URL to every availability claim, or state "date unknown".
- MUST note skipped or failed platforms in the report header (e.g. "code-hosting not searched for this role type").
- NEVER fabricate candidate details — missing fields are "unknown", and a candidate kept from a snippet is labeled as snippet-only.
- NEVER contact, message, or email a candidate as part of this play; sourcing ends at the report, and any outreach is a separate, explicitly human-approved action.
- NEVER drop a strong candidate because their profile is login-walled — keep the snippet entry.
- NEVER present fewer than five candidates as a finished answer without flagging it and proposing a broader brief.
