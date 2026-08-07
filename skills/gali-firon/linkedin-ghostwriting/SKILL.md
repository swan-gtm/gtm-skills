---
name: linkedin-ghostwriting
title: LinkedIn ghostwriting
description: |
  Use this skill when ghostwriting LinkedIn posts for a founder or executive - the ask is "what should our CEO post", "draft the next posts for [exec]", "write this in [exec]'s voice", "an industry-news take", "a repost", or "exec thought leadership". Produces three ranked, typed post options per executive in that person's own voice - a news share, a repost, and a thought-leadership piece with a graphic - each short, each with an attachment, each gated against everything they have already posted. Reach for it whenever you are writing exec social content that has to sound like them, stay fresh, and never repeat itself.
category: Positioning
tags: [Marketing]
---

Applies when ghostwriting a named executive's next LinkedIn posts. Produces three ranked, typed options per exec, each a few lines, each with an attachment, each cleared by an anti-repeat gate.

This skill exists to fix the two failure modes of exec ghostwriting: posts that repeat what the exec already said, and posts that read like marketing copy instead of the person. It runs in one pass and hands the exec ready-to-post options to approve by hand. It never posts anything.

## Required inputs

Gather these before drafting. A thin input set produces generic posts.

- **A voice card per exec** - their real diction, the arguments they own, what they will never say, and one or two of their best past posts. Build it from their actual posting history, not a guess. Format and starter questions are in `references/voice-card-and-cadence.md`.
- **A post ledger** - every post that has gone out, with hook, core argument, attachment, and any performance note. This is what the anti-repeat gate reads.
- **A fresh signal feed** - this week's news, competitor moves, earnings, and regulatory shifts on the exec's beat, plus repost candidates. Verify each peg's date at the primary source, not the commentary's date.

## The play

1. **Read the history first.** Before generating anything, read the ledger and the last several live posts: what argument, what attachment, what landed. This feeds the anti-repeat gate and keeps cadence honest.
2. **Mine the signal, then decide the angles.** Read the whole signal feed and generate the angles from it. Treat any pre-suggested angle as one raw input, never the plan.
3. **Run the anti-repeat gate.** Diff every candidate angle against the ledger and the exec's off-limits list. Kill or re-angle anything on the off-limits list, in the same argument family as a recent post, or inside the same-argument cooldown window. A rejected or deleted past option counts as a rejection - never re-serve it. The full gate logic, cooldown windows, and cadence targets are in `references/anti-repeat-and-cadence.md`.
4. **Lock the three types and the attachments.** Assign one of each type per exec: a news share plus comment, a repost, and a thought-leadership piece with a graphic. For the graphic, recommend single image versus carousel and hand over a ready-to-paste image-generation prompt. The format gates, attachment rules, and image-prompt spec are in `references/format-and-attachments.md`.
5. **Check messenger and lane fit.** The exec must plausibly follow that source and their audience must care about it - not merely "is the argument sound". Route the peg to the exec whose lane it is (regulatory to the policy voice, product to the builder, numbers to the finance voice). Two execs never comment on the same article.
6. **Draft in voice, then two finishing passes.** Draft each option against the voice card and closest samples. Then strip AI tells to a clean baseline, and add one or two real human moves so the post reads as the person, not a clean bot. One or two moves, never invented detail.
7. **Score, rank, and deliver.** Score each on hook strength and on commercial value (audience precision, proof, narrative fit, why-now). Below bar gets one revision. Deliver three ranked options per exec with attachments and, for the graphic, the image recommendation. Dependencies and posting-order notes travel with the delivery, never on the post itself.
8. **Close the loop.** After the exec picks, edits, or posts, append the chosen post to the ledger - it re-enters play only after the cooldown window, never sooner. If they rewrote it, that rewrite becomes the new gold line - update the voice card. Any angle the exec killed or rejected goes to the off-limits map as a permanent block. (Ledger entries return after the cooldown; off-limits entries never do.)

## What good looks like

- **What the best operator notices first:** repetition is the real enemy, and it is an argument-family problem, not a wording problem. Two posts with different words making the same underlying point read as repetition to the audience. The gate has to compare angles, not phrases, and it has to include options the exec already rejected, because a killed angle resurfacing is the most common way stale content ships.
- **The common mistake:** drafting posts that are clean but sound like a brand, not a person - marketing lines and deadline-pitch closers ("so this is a now decision"). A clean, on-message, voiceless post is a fail, not a pass. The other common miss is routing a peg to the wrong exec because the argument was sound, ignoring whether that exec's audience follows that beat.
- **How you know it worked:** three options per exec, each a few lines with a real attachment, each an angle the exec has not run, each closing on a genuine thought or question rather than a plug. Read the thought-leadership one aloud - it should sound like that specific person, and the graphic should match their established visual style, not a generic stock illustration.

## Rules

- MUST diff every angle against the ledger and rejected options before drafting; kill anything inside the cooldown.
- MUST ship every post with an attachment - a news link, a repost, or a graphic. Never a bare text post.
- MUST run tell-stripping and then a human-texture pass on every draft.
- MUST route each peg to the exec whose lane and audience fit it, and never let two execs comment on the same source.
- NEVER post, send, or reshare externally - deliver options for a human to post by hand.
- NEVER close on a self-plug or a deadline pitch; close on a thought or a question.
