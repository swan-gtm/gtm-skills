---
title: Company matching rules
description: Reference for the Track contact job changes skill.
---

# Company matching rules

Deciding whether two company references are the same is the crux of this play — it drives both
"still there vs left" and "is the new company already in the CRM?". Company names are noisy; hard
identifiers are not. Rank the signals accordingly.

## Signal order (strongest first)

1. **Domain** — normalize both (lowercase, drop scheme, `www.`, path, and port; reduce to the
   registrable domain, keeping the extra label for known two-part suffixes like `co.uk`). Equal
   normalized domains → **same company**. Explicitly different domains → treat as **different**
   unless a LinkedIn page agrees.
2. **LinkedIn company page** — compare the `/company/<slug>` slug. Equal slugs → **same company**
   (near-certain).
3. **Name** — only a supporting signal. Normalize before comparing: lowercase, strip punctuation,
   drop a leading "the", and remove legal/suffix noise (inc, llc, ltd, corp, gmbh, co, holdings,
   group, technologies, labs, software, solutions, …). Identical normalized names, or one fully
   contained in the other, is a moderate signal — never enough on its own to justify a CRM write.

## Verdict bands

- **Match** — a hard identifier (domain or LinkedIn slug) agrees. Safe to treat as the same company.
- **Ambiguous** — only names are similar, or signals partially conflict. This is the **"can't confirm"**
  outcome: re-find the LinkedIn URL or flag for review. Do not write.
- **Different** — domains disagree and nothing else confirms a match. Even a high name similarity does
  not override disagreeing domains.

## Edge cases

- **Acquisitions / rebrands / subsidiaries** — count as the same company only when domains or LinkedIn
  pages agree. Matching names across a rebrand without an identifier is "can't confirm".
- **Holding companies and DBAs** — a shared parent name with different operating domains is *different*.
- **Thin current-employer data** — if the new employer came back with only a name and no domain/LinkedIn,
  a "left" verdict is not confident enough. Fall to "can't confirm".

The principle: earn "confirmed left" from a hard-identified new employer. Prefer leaving a record as
"can't confirm" over writing a confident guess.
