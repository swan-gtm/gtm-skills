---
name: reply-pull-gate
title: Reply pull gate
description: |
  Use this skill when scoring an outbound draft before it sends, and when writing a cold or
  re-engagement touch that has to earn a reply from someone who owes you nothing. Produces a
  verdict, SEND or SEND BACK, with the named rewrite when it fails. Clean is table stakes;
  this scores pull. Trigger phrasings: "review this cold email", "score this draft", "is this
  good enough to send", "why is nobody replying", "this reads clean but forgettable", "our
  reply rate is flat", "write the subject line".
category: Outreach
---

Run this on a drafted touch before it goes out. Produces SEND, or SEND BACK naming which move is missing.

## The one-line law

A cold recipient owes you nothing. The first touch's only job is to earn five seconds and a reason to answer. It is not to describe you, and it is not to get the meeting.

## The four moves

Every cold touch needs at least two. A first touch in a sequence needs three.

**1. Show the work.** An artifact beats a claim. Not "want a one-pager?" but a named, concrete thing that could only exist for this account: the audience list you pulled for them, a teardown of their current setup, what a named non-competitor in their category ran and what it did. The ask then names the artifact, not "more info."

**2. Poke, don't pitch.** Open on a cost or blind spot the buyer may not have priced, as an observation or a genuine question. "Your competitors all moved that spend last quarter and you are still carrying it in-house" pokes. "We are the leading platform for X" pitches. Poke with the situation, never with a sweeping market declaration and never with a statistic.

**3. One unscrapeable line.** One sentence proving a human did homework this week: their dated campaign, their new agency setup, their role change, their launch. Dated within three months, and specific enough that a scraper could not have written it. This is what stops the archive swipe.

**4. Write to be forwarded.** Replies are often redirects rather than answers, so make the redirect cheap. The message must make sense to a colleague with zero context, name the domain in plain words, and carry an ask so small that forwarding costs nothing. "If this sits with someone else on your team, happy to be pointed there" is part of the single ask, never a second ask.

## Calibrate the ask to the rung

- **Rung 0, true cold.** Ceiling: permission to send the named artifact. Never a call.
- **Rung 1, warmed.** They accepted a connection, opened a thread, or the account has recent history. Ceiling: the artifact plus a soft "worth a look?"
- **Rung 2, engaged.** They replied once, or you have personal history. Only here does a meeting ask belong.

Asking above your rung reads as vendor desperation and burns the thread.

A dormant thread reopens on new information only, never on elapsed time. Banned outright: "circling back", "just following up", "bumping this".

## Score it

Score pull 0 to 10 on its own. Do not average it against tone and grammar. Below 7 on a cold first touch is SEND BACK however clean the rest reads, and a send-back names the missing move and demands a rewrite, not a tweak.

Five checks first. Any failure is a rewrite:

1. Delete the opener. Does it still make sense? Then the personalization was decoration.
2. Could this exact message go to another company this week? Then it is a blast in costume.
3. One ask, follow-ups shorter than the last, subject two to five words and lowercase.
4. Is the proof a number or a name? "Helps teams like yours" is not proof.
5. Read it as the recipient with a full inbox. Any reason to reply beyond politeness?

## What good looks like

The mediocre version is the polite nothing: compliant, well-spelled, forgettable. It passes every grammar check and gets archived. Scoring that "fine" is how a team ships hundreds of touches into silence, and it is the whole reason this gate exists.

The best reviewer names which move is missing rather than what the words got wrong. Three product claims in a row is a capability dump, not an email. The same two customer logos across five drafts is social proof as wallpaper. A statistic in the opener on any channel is a pitch wearing a fact.

The output is good when the recipient could not have received it from anyone else that week, and when a colleague forwarded the thread would understand it cold.

The gate only improves if replies feed back into it. Log the winning move on every reply and promote the highest-yield opener once you have five: `references/reply-autopsy.md`.

## Combines with

**Alex Vacca's `sdr-outbound-rules`** owns the hygiene floor: word count, one CTA, no bullets, which frameworks are allowed. Run it first and treat it as settled. This skill scores the thing hygiene cannot see, whether a stranger has a reason to answer, which is why a draft can clear every rule there and still fail here.

**`bridge-before-cold`** runs before both and decides what the opener stands on.

## Rules

- MUST name the missing move on every SEND BACK. A verdict without a named move is an opinion.
- MUST keep the touch to one ask.
- NEVER lead a first touch with a statistic, on any channel.
- NEVER cite a direct competitor of the recipient as proof.
- NEVER reopen a dormant thread with the passage of time as the reason.
