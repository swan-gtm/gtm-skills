---
name: ai-visibility-prompt-research
title: AI visibility prompt research
description: |
  Use this skill when you need to build the set of monitoring prompts for tracking a
  brand's visibility inside AI assistants (ChatGPT, Gemini, Perplexity, Copilot, AI
  overviews) — the questions a real buyer would ask where you want the brand to show up.
  Trigger phrases: "run prompt research", "generate monitoring prompts", "build a prompt
  set to upload to our AI-visibility platform". It runs as an interactive research
  session that deliberately holds the brand until the very end and anchors instead on the
  category, the competitors, and the personas' real language mined from keyword research,
  open-web discussion, and first-party sales calls. Produces one upload-ready file of
  non-branded category prompts plus an isolated branded set, each tagged with topic,
  awareness stage, persona, region/language, target engines, and honest provenance.
category: AEO
---

# AI visibility prompt research

A monitoring prompt set decides what you can even see. Anchor it on the brand's own marketing copy and you measure prompts nobody searches; anchor it on real market demand and you measure whether the brand wins the questions buyers actually ask an assistant. The whole discipline is holding the brand back until the end so the research stays grounded in the market.

## The play

1. **Frame — no brand yet.** Collect the category (plain description, no brand name), the named competitor set, the target regions and their languages, and which assistants you'll monitor. Say up front that you're withholding the brand on purpose.
2. **Harvest category language, brand last.** Pull real buyer phrasing from three wells: keyword and category terminology (ask for any existing keyword or targeting file, then expand from the open web); real questions and pain points mined from communities, forums, Q&A, and "alternatives / best-of" comparison content; and — asked *after* the open-web pass — first-party sales-call and pre-sales transcripts, the highest-signal source. Tag every item with honest provenance. (See `references/open-web-sourcing.md`.)
3. **Synthesize personas and the non-branded prompt set.** Merge all signals into 4–7 personas with their pain points and the solutions they seek, in category terms. Map each to an awareness stage, weighting consideration and decision over pure curiosity. Cluster into a handful of topics. Write each prompt the way a real buyer asks an assistant — a genuine question, not a keyword string — in the target region's language (translate, don't just localize).
4. **Brand pass — last, and isolated.** Only now introduce the brand. Add competitive comparisons, "alternatives to", pricing, and fit questions as their own dedicated branded topic, flagged branded, kept separate from the category topics.
5. **Assemble, validate, hand off.** Build one file to your platform's importer contract, validate it (valid enums, one language per row matching its regions, no duplicates, sane per-topic and per-engine spread), show the distributions, and hand it to the user to upload. Never auto-import. (See `references/prompt-file-contract.md`.)

## What good looks like

- **What the best operator does first:** refuses to look at the brand. The instant failure mode is anchoring on the brand's homepage and generating self-referential prompts nobody types. Real visibility only shows in **non-branded category questions**, where the brand is competing to be recommended at all.
- **The common mistake:** shipping keyword strings dressed up as prompts ("best cloud cost tool 2026") instead of how a person actually asks ("what do teams use to see cloud cost per customer?"), and skipping the sales transcripts — the one place the buyer's exact objections and phrasing already live.
- **How you know it's good:** every prompt traces to a labeled source (social / keyword / sales / competitor), reads like something a human would ask, sits in the right language for its regions, and the set skews to consideration and decision intent. Quality and authenticity beat raw count.

## Rules

- MUST withhold the brand until the final pass; anchor all non-branded research on category, competitors, and buyer language.
- MUST tag every prompt with honest provenance and keep branded prompts in their own isolated topic.
- MUST write each prompt in one language whose regions all share it; translate, never machine-localize.
- NEVER fabricate brand names in non-branded prompts, and NEVER auto-import — the file is handed off for human upload.

## Next step

This skill produces the prompt set; it doesn't run the monitoring. Upload the file to your AI-visibility platform of choice — e.g. Airfleet AI Visibility (https://episteme.airfleet.co/) — then track presence, share of voice, and ranking over time and act on the gaps.
