---
name: icp-lookalike-expansion
title: Expand a target list from one good-fit profile
description: "Use this skill when you have a handful of accounts or people who converted and need more like them, or when a black-box 'similar profiles' feed gives you a list you cannot explain. Extracts an explicit similarity signature from the seed and searches on it, so you control what 'similar' means and can widen or tighten deliberately."
category: Prospecting
tags: [Sales, ICP]
---

Use this when a few leads converted and you need more like them. It produces a deduplicated target list built on a similarity definition you chose, not one a vendor's feed chose for you.

## The play

1. **Read the seed properly.** Pull the seed's full record and extract two things: current title and current employer. That pair is the similarity signature. Everything downstream depends on it being right, so read the actual current role rather than the headline, which is often aspirational or stale.

2. **Decide what "similar" means.** There are two different searches and they answer different questions:
   - **Peers inside the same company** — title plus employer. Use when you are mapping a buying committee or expanding within a won account.
   - **The same role across the market** — title only, optionally narrowed by geography. Use when you are building a net-new list. Drop the employer filter or you will get nothing.

3. **Search on short titles.** Pass the core role, not the decorated headline. "Chief executive officer" works; "CEO & Founder | Investor | Speaker" returns zero. Most title matching is loose, so a shorter string casts the right net.

4. **Branch deliberately if you need depth.** Depth 1 searches off the seed alone. Depth 2 takes each discovered profile, reads its role and employer, and searches again. Depth 2 is dozens of lookups; depth 3 is hundreds. Cap how many profiles you branch on (top 10 is usually enough) and confirm the spend before going past depth 2.

5. **Deduplicate by handle and drop the seed.** The same person surfaces under many searches, and most search endpoints return the seed itself. Keep a seen-set across the whole run.

6. **Return a clean list**, not the recursion tree: handle, name, headline, location, and which seed it came from.

## What good looks like

- The best operator tightens one filter at a time. Stacking exact title, all-skills-match, and a city filter returns zero rows and reads as "no market" when it is really an over-narrowed query. Start broad, then narrow.
- The mediocre version trusts a "people similar to this" feed and cannot explain why anyone is on the list. When a rep asks "why him?", there is no answer.
- Empty results are a signal, not a failure. Widen by dropping the employer filter, shortening the title, or removing geography, and note which loosening produced the hit.
- You know it is good when every row survives the question "what specifically makes this person like the seed?"

## Rules

- MUST deduplicate by handle across the whole run, not per search.
- MUST drop the seed from its own results before ranking.
- MUST confirm the cost with the user before running depth 3.
- NEVER pass a full headline as the title filter.
- NEVER re-process a handle already seen. It costs money and adds nothing.
