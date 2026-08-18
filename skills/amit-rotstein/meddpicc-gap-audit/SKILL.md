---
name: meddpicc-gap-audit
title: Deal MEDDPICC gap audit
description: |
  Use this skill when a deal is coming up for a forecast call, a stage change, when someone
  asks what's actually missing on a deal, or after a new call or email that might change
  qualification — deal review, deal inspection, deal qualification, MEDDPICC gap check,
  qualification gap. Input: one or more meeting transcripts and/or email threads for the deal
  (required) plus, optionally, the deal's current CRM/qualification field values (for
  reconciliation). It maps MEDDPICC/MEDDIC signal straight out of the transcripts and emails,
  citing the exact line behind every mapping, then reconciles that against the CRM values if
  supplied — separating confirmed risks from open unknowns and weighting gaps by deal stage.
  Can optionally write reconciled values back to a connected CRM, but only field by field and
  only with the user's explicit permission — never from a live connection alone.
category: Deals
tags: [Sales, RevOps, Sales Qualification]
---

Use this skill when a deal is coming up for a forecast call, a stage change, when someone asks what's actually missing on it, or after a new call or email that might change qualification. **Input:** one or more meeting transcripts or email threads for the deal — this skill has nothing to work from without at least one. The deal's current CRM/qualification field values are optional, supplied separately, and used only for reconciliation, not as the primary input. Produces a per-component status — verified, unverified, or confirmed risk — for every MEDDPICC/MEDDIC component, each backed by the exact evidence that produced it.

## The play

1. Start from the meeting transcript(s) or email thread(s) supplied for this deal — that's the material everything else is extracted from. If the deal's current qualification data (CRM fields, a deal doc, notes) was also supplied, note it as the baseline to reconcile against later; if it wasn't, say so explicitly rather than silently skipping reconciliation.
2. Read the transcripts/emails and map language to each MEDDPICC component (Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition) as you go. For every mapping, quote the exact line or lines that justify it. A paraphrase is not a citation.
3. If more than one transcript or email is supplied for the deal, order them chronologically before mapping anything. Where a component has evidence in more than one source, the most recent statement is the current status — unless it actually reverses an earlier one (a champion's enthusiasm cooling, a budget that was confirmed becoming unconfirmed). A reversal is a finding in its own right — cite both the earlier and later statements rather than quietly keeping only the newer one. Added detail that doesn't conflict (a second call naming specific frameworks after a first call named compliance generally) is enrichment, not a reversal — no flag needed.
4. Before mapping anything from a transcript, resolve who's speaking. See `references/speaker-attribution.md` for the fallback chain — domain metadata, then contact-list match, then a content-cue guess that must be confirmed before use. When a CRM connection is available, its own contact and owner records for the deal are usually the strongest source for the contact-list rung — check there before falling back to a guess.
5. For every mapping, check that the speaker actually matches the side the component expects — a seller describing their own product is not evidence of the buyer's pain, need, or criteria, even when the topic overlaps. Discard or re-flag any mapping that fails this check rather than citing it anyway.
6. If CRM/qualification values were supplied in step 1, reconcile each mapped value against the existing value for that component: does the source material support it, contradict it, or say nothing? Where the CRM is blank and the source speaks directly to that component, that's a fillable gap with the citation already attached. Where the CRM and the source disagree, surface the disagreement explicitly — never quietly overwrite one with the other — and say what kind of disagreement it is: a hard factual conflict (a number, a name) is a different problem than a qualitative maturity mismatch (a status claim the source doesn't support). Apply the same defensibility check to the CRM's existing value, too — a vague entry doesn't get a pass just because nothing in the source material contradicts it. If no CRM values were supplied, skip this step and say so in the output rather than presenting the extraction as a reconciled audit.
7. Grade every component on two separate axes: is it defensible (a real citation exists, not a restated field or a paraphrase), and is the actual answer favorable. A well-cited "no budget confirmed" is defensible but still a real risk — flag it as a confirmed risk, not a data gap, and never let a good citation round an unfavorable answer up to verified.
8. Cross-check gap severity against deal stage. A missing component early on is routine. The same gap at a mature stage — verbal commit, contract-out — is urgent; surface it as a stage/qualification mismatch on its own, not folded quietly into the individual component's score.
9. If a live CRM connection exists, the default is still to only report — a connection is not permission. Only if the person running this skill explicitly asks to update the CRM, go field by field: show the field name, its current value, the proposed new value, and the citation behind it, and get explicit confirmation on that specific change before writing it. Let them skip any field they don't want touched. Never write a value that has no citation behind it, even on request — say it's unconfirmed instead of writing it.

## What good looks like

- The best version shows its receipts: every mapped value carries the exact quote it came from, never a paraphrase, a restated field, or a summary of "what was generally discussed."
- The mediocre version treats a paraphrase as a citation, silently overwrites a CRM value instead of flagging that source material contradicts it, lets a well-cited unfavorable answer round up to verified because it's thoroughly documented, or cites the seller's own pitch as if it were the buyer's stated pain because the topic happened to overlap.
- You know the output is good when CRM/source disagreements are called out rather than resolved silently in either direction, a numeric or named-fact conflict reads differently from a qualitative maturity mismatch, "couldn't check" and "checked, found nothing" read as visibly different outcomes, a mature-stage deal with foundational gaps stands out immediately, and no conclusion rests on a speaker-role guess that was never confirmed.
- If it writes anything back to the CRM, it only ever does so one shown-and-confirmed field at a time — never because a connection existed and the request was vague enough to read as blanket permission.
- A reversal across calls — a champion cooling, a budget disappearing — is called out as its own finding with both citations, never silently smoothed into "most recent wins."

## Rules

- MUST have at least one meeting transcript or email thread to run at all — if none is supplied, say so and stop rather than producing a status from CRM fields alone.
- MUST cite the exact line(s) from the source material for every mapped MEDDPICC value — a paraphrase or a summary is not evidence.
- MUST process multiple sources in chronological order and flag a reversal between an earlier and later statement as its own finding, citing both — never silently keep only the most recent one.
- MUST verify the speaker of a quoted line matches the side the component expects — a seller describing their own product is not evidence of the buyer's pain, need, or criteria, even when the topic overlaps.
- MUST reconcile newly-mapped values against existing CRM fields when they're supplied, surfacing any disagreement explicitly — and labeling whether it's a factual conflict or a maturity mismatch — rather than overwriting silently in either direction; when no CRM values are supplied, say so instead of skipping the step without comment.
- MUST apply the same defensibility check to the CRM's existing value as to a freshly-mapped one — a vague or unevidenced CRM entry doesn't get a pass just because nothing in the source material contradicts it.
- MUST resolve speaker attribution before mapping any transcript or email content to a component, checking CRM contact/owner records first when a connection is available.
- MUST grade defensibility and outcome favorability independently; a well-evidenced unfavorable answer is a confirmed risk, not a verified pass.
- MUST weight gap severity by deal stage and call out stage/qualification mismatches explicitly.
- MUST propose and get explicit confirmation on any speaker role guess made from content cues before using it to support a mapping.
- NEVER treat a paraphrase, a restated field, or a filled-in value with no citation as evidence.
- NEVER overwrite or discard an existing CRM value without flagging the discrepancy with the source material.
- NEVER let an unconfirmed role guess harden into a stated fact anywhere in the output.
- MUST NOT write to the CRM or any system of record unless the person running this skill explicitly asks for the update — a live connection by itself is never permission.
- MUST show the field, its current value, the proposed new value, and the citation behind it, and get explicit confirmation on that specific change before writing it — one field's confirmation doesn't authorize any other.
- NEVER write a value to the CRM that has no citation behind it, even under explicit request — say it's unconfirmed instead of writing it.
