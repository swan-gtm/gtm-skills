---
name: call-kpi-scoring
title: Call KPI scoring
description: |
  Use this skill after a sales call — coaching a rep, judging whether a call moved the deal
  forward, or producing a scorecard on how the conversation actually went — call scoring, call
  quality, call coaching, call KPIs, talk ratio, question rate, monologue length, engagement
  score. Different from a behavior-based scorecard: this measures nine largely quantitative
  KPIs (talk-to-listen ratio, question rate, longest monologue, talking speed, engagement,
  sentiment, agenda set, next steps, next meeting scheduled) directly from the call itself,
  plus a tenth narrative one (improvement tips). Input: a call transcript, a raw audio file, or a live connection to a
  call-recording/conversation-intelligence system (required — one of the three); always
  recomputes every metric from the source material rather than trusting a connected system's
  own numbers. Classifies the call's type from its content first, scores each KPI against a
  type-specific target band where one exists, and groups the KPIs into conversation-quality
  and forward-motion — surfacing it explicitly whenever a call scores well on one and poorly
  on the other, rather than flattening both into one average or an "N of 10 green" tally.
category: Sales
tags: [Sales, RevOps, Coaching]
---

Use this skill after a sales call — coaching a rep, judging whether it moved the deal forward, or just getting a scorecard on how it went. **Input:** a call transcript, a raw audio file, or a live connection to a call-recording system — this skill has nothing to score without one of the three; an audio file needs to be transcribed with speaker separation and timestamps before some of the scoring below is possible. It classifies the call's type first, then scores nine call-quality KPIs against a target band matched to that type — always computed fresh from the source material rather than pulled from any connected system's own numbers — plus a tenth, Improvement Tips, written as narrative rather than scored.

## The play

1. Confirm at least one valid input exists: a transcript, an audio file, or a live connection. If it's an audio file, transcribe it first; the transcription must include speaker separation and per-turn timestamps to support the timing-dependent KPIs in step 4 — if it doesn't, treat it the same as a plain-text transcript for those KPIs. If a live connection to a call-recording/conversation-intelligence system is used, pull the raw transcript and any speaker/timing metadata from it, but always compute every KPI in this skill directly from that raw material — never adopt the connected system's own precomputed KPI values, even when it offers them, so scoring stays consistent across all three input paths.
2. Resolve who's speaking before scoring anything. See `references/speaker-attribution.md` for the fallback chain — domain/calendar metadata, then contact-list/CRM match, then a content-cue guess that must be proposed and confirmed before use. On a call with more than one person per side (two reps, or two buyer-side attendees), treat every KPI that splits time or turns between "the seller" and "the prospect" as a per-side aggregate — pool all seller-side speakers into one side and all buyer-side speakers into the other — rather than picking one representative speaker per side or scoring individuals separately. For Longest Monologue specifically, this means an uninterrupted stretch where the other side never gets a turn counts as one continuous monologue even if it passes between two speakers on the same side — measured or estimated, it's about one side holding the floor, not any one individual's turn length.
3. Classify the call's type from its actual content — what was discussed and how, not just its label. A calendar invite title, meeting subject line, or CRM meeting-type/stage field can be checked first as a hint, but the transcript content is the deciding signal and overrides them on conflict. Four types: Discovery, Demo/Technical, Commercial, and General (the default for a low-confidence call). If a call's content spans more than one type (e.g. opens with discovery, moves into a demo), classify it by its dominant type — whichever the content leans toward overall — rather than splitting it across two scorecards. There's no fixed rule for what counts as low-confidence-enough-for-General; use judgment, and say so explicitly when a call is a close call between two types.
4. Score the nine graded KPIs using the target bands in `references/kpi-targets.md` (defaults, with overrides on three of the nine for Discovery and Demo/Technical; everything else uses the default band regardless of type). Five are timing-dependent and need a diarized, timestamped transcript to compute directly: Talk-to-Listen Ratio, Question Rate, Longest Monologue, Talking Speed, Engagement Level. Without that data:
   - Talk-to-Listen Ratio, and Engagement Level's turn-frequency component, can still be estimated from word share and turn counts in the text alone — label these explicitly as estimates, not measured values.
   - Longest Monologue can be estimated too: take the seller side's longest uninterrupted stretch by word count (see step 2 on multi-seller aggregation) and convert it to seconds using an assumed average speaking rate (150 WPM, the midpoint of the Talking Speed target band) — label this as a word-count-based estimate.
   - Talking Speed and Question Rate cannot be estimated this way — Talking Speed would require assuming the very rate it's supposed to measure, and Question Rate needs a real call duration. Skip both and disclose explicitly that they're unavailable without timing data, rather than guessing.
   The remaining four graded KPIs — Customer Sentiment, Introduction & Agenda Set, Next Steps & Action Items, Next Meeting Scheduled — are content-judgment calls readable from any transcript regardless of timing data. Improvement Tips is not a graded KPI at all — it's the narrative output written in step 7, with nothing to score or cite against a target.
5. For every graded KPI score, show the basis behind it: a direct quote for the content-judgment KPIs, a disclosed method (word share, or the longest-turn excerpt and its word-count-to-seconds conversion) for the estimated timing KPIs, and an explicit "unavailable — no timestamps" for the two that were skipped. Never present a scored value with no citation or method behind it.
6. Group the nine graded KPIs into two categories before presenting a verdict: conversation-quality (Talk-to-Listen Ratio, Question Rate, Longest Monologue, Talking Speed, Engagement Level, Customer Sentiment) and forward-motion (Introduction & Agenda Set, Next Steps & Action Items, Next Meeting Scheduled). Check whether the two groups agree or diverge — a call can score well on conversation-quality and still fail to move the deal (no agreed next step, no meeting booked), or score poorly on conversation-quality while still landing real forward motion. Call out a divergence explicitly as the headline finding; don't fold it into a flat average or an "N of 10 green" tally.
7. Write the Improvement Tips section grounded in what actually happened on this specific call — anchored to the divergence from step 6 and the cited lines from step 5 — rather than generic advice that could apply to any call.
8. Always produce the chat/text summary. If the environment this skill runs in supports rich interactive output, also render the scorecard visually (e.g. a gauge or bar per KPI against its target band) — but don't assume or require that capability; the text summary must stand on its own.

## What good looks like

- Every graded KPI carries either a quote, a disclosed estimation method, or an explicit "unavailable" — never a bare number with no basis shown, and never an estimate presented as if it were measured. Improvement Tips isn't graded and isn't held to this — it's the narrative writeup.
- The meeting-type classification is shown, including when it was a close call between two dominant types, rather than presented as unambiguous by default.
- Conversation-quality and forward-motion are reported as two groups, and any divergence between them is the headline of the output — not smoothed into a single average score.
- A multi-person call reads as one aggregated seller side vs. one aggregated buyer side on every split-time or split-turn KPI, not scored per individual.
- Tips are specific to this call's actual divergence and citations, not generic coaching boilerplate that could apply to any call.
- Skipped KPIs (no timing data) read as visibly different from KPIs that were checked and passed — "couldn't measure" is not the same as "measured, met target."

## Rules

- MUST have at least one valid input (transcript, audio file, or live connection) to run at all.
- MUST resolve speaker attribution before scoring anything, using the same fallback chain as `references/speaker-attribution.md`.
- MUST classify the call's type from its transcript content, using calendar/CRM signals only as a hint the transcript can override.
- MUST classify a mixed-type call by its dominant type rather than leaving it unclassified or scoring it against two bands at once.
- MUST always recompute every KPI directly from the source material, even when connected to a system that offers its own precomputed values.
- MUST treat any KPI that splits time or turns between sides as a per-side aggregate on a multi-person call — pool every seller-side speaker into one side and every buyer-side speaker into the other, never score individuals separately.
- MUST score each graded KPI against its type-specific target band where one exists in `references/kpi-targets.md`, and the default band otherwise.
- MUST label Talk-to-Listen Ratio, Engagement Level, and Longest Monologue as estimates (not measured values) whenever they're computed from word/turn counts instead of real timestamps.
- MUST skip Talking Speed and Question Rate when no timing data is available, and disclose them as unavailable — NEVER estimate either of these two.
- MUST show a citation (quote, method, or "unavailable") behind every graded KPI score.
- MUST report conversation-quality and forward-motion as separate groups and flag any divergence between them explicitly.
- MUST ground Improvement Tips in this call's actual findings — NEVER generic advice unconnected to what was cited. NEVER grade or cite it against a target band the way the other nine KPIs are.
- MUST always produce the plain chat/text summary regardless of environment.
- NEVER present an estimated value as if it were a directly measured one.
