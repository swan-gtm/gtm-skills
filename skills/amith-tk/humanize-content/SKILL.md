---
name: humanize-content
title: Humanize AI-sounding content
description: |
  Use this skill when marketing or sales copy reads as machine-written and needs to sound like a person wrote it: AI drafts of articles, web pages, case studies, emails, LinkedIn posts, meta descriptions and FAQ answers. Produces a rewrite that keeps the meaning and facts, removes six specific patterns that give AI copy away, and comes with a checker report. Fires on "humanize this", "this sounds like AI", "make it sound human", "remove the AI tells", "tidy the copy", "does this sound like AI", "edit this draft", "check this against our style", "this reads like a slogan stack".
category: Positioning
tags: [Marketing]
---

Use when a draft is correct but sounds produced rather than written. Produces a rewrite in plain, connected prose with claims first, evidence attached and a person doing the acting, plus a short list of what changed and what still needs a source.

**Load first:** the draft, where it will appear (page, email, post, article) and who reads it. Ask whether a brand voice guide or house style exists and follow it where it conflicts with the defaults in `references/house-style-options.md`. Confirm the few switches that vary by company: English variant, em dashes, banned vocabulary, and whether byline or headline wording is already agreed. The purpose is clarity and voice. It is not to defeat AI detectors, and it never changes who the author is.

## The play

1. **Diagnose.** Run `scripts/lint_style.py` on the draft when code execution is available (`references/using-the-checker.md`). Otherwise test the draft by hand against the six patterns below. Also read for sentences with no verb, which the checker only partly catches.
2. **Rewrite pattern by pattern.** Give every sentence a subject and a finite verb, keep every fact and number, and use the fixes in `references/retired-patterns.md`. Study `references/rewrite-bank.md` for before-and-after pairs.
3. **Re-check and read aloud.** Rerun the checker until no `RULE` hits remain, decide each `CHECK` hit, then read the draft once as speech. If it sounds like a stack of statements, join them into continuous prose.
4. **Report.** List the patterns removed, the sentences that changed meaning even slightly, and every figure that has no unit, source or date. Ask for those instead of inventing them.

For voice, sentence length and structure, read `references/voice-and-structure.md`.

## The six patterns to retire

| Pattern | Looks like | Fix |
|---|---|---|
| 1. Fragment with a tag | "Four layers, built in order." | Give it a subject and a verb: "The stack has four layers, and each rests on the one beneath." |
| 2. The "so" splice | "Pages that explain the category, so the buyer reads yours first." | Make the effect the main verb, put the condition first, or use "because". |
| 3. "Worth" and other editorial nudges | "worth noting", "it is important to note", "keep in mind" | State the thing and, if needed, the reason it matters. |
| 4. "Long before" and "long after" | "long before anyone books a call" | Give the interval or name the event: "months before". |
| 5. The "none of it" closer | "None of that makes the decision less human." | State the positive fact, or use a precise negative. |
| 6. The sentence that announces its point | "The part that compounds is deciding what to say." | Let the actor do the thing: "Content compounds when a company decides what to say." |

Related contrast shapes ("not just X but Y", "X, not Y", "is not X, it is Y", parallel-pair headings such as "Two teams, one goal") are on by default and can be switched off.

## What good looks like

- **Meaning survives.** Every fact, name, number and qualification in the original is still there, unless the user agreed to cut it.
- **Claim first.** The most important sentence leads the page, the section and the paragraph.
- **Sentences hold 15 to 30 words,** with a ceiling near 40, and no more than two in a row under eight words.
- **Connectors vary** ("because", "while", "although", "when", "but", "yet"), and condition-first phrasing often removes the connector entirely.
- **People are the subject.** Buyers, teams and companies act; abstractions rarely do.
- **Numbers carry a unit, a named source and a year.** Missing ones are flagged, never invented.
- **Confidence is calibrated:** sourced facts stated flatly, forecasts hedged with "could", "may" or "usually".
- **The mediocre version** swaps words for synonyms and leaves the same skeleton, or swaps one tell for another (every "so" becomes ", which"), or flattens a distinctive voice into beige.
- **Done when** the checker reports no `RULE` hits and the draft reads naturally aloud.

## Rules

- MUST preserve facts, names and figures, and flag any change in meaning.
- MUST ask for a source or unit instead of making one up.
- MUST leave intentional examples alone: quoted "what not to write" demonstrations, legal wording that needs exact phrasing, and literal money values such as "worth $5 million".
- MUST ask before changing headlines, slogans or bylines the owner has already approved.
- NEVER invent statistics, quotes, client names or sources.
- NEVER present a rewrite as undetectable by AI-detection tools.
