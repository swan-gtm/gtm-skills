---
name: auto-reply-is-not-a-reply
title: An auto-reply is not a reply
description: |
  Use this skill when classifying inbound responses to outbound — out-of-office, vacation and
  parental-leave auto-responders, delivery notices, and other machine-generated mail that looks
  like engagement. Produces a triage decision that keeps the sequence alive, keeps the metrics
  clean, and reschedules the next touch to when the human is actually back.
category: Outreach
tags: [Sales, RevOps]
---

An out-of-office arrives in the same inbox, in the same thread, as a real
answer. Filed as one, it corrupts three things at once. This is how to file it.

## The play

1. **Classify machine mail as its own outcome**, alongside interested,
   question, referral, not now, not interested and unsubscribe. A triage
   vocabulary without this bucket does not skip the auto-responder — it files
   it under the nearest wrong label.
2. **Read the return date if the message states one; never infer one.** "Back
   on the 20th" is a date. "Away for a while" is not, and a guessed date is a
   send at the wrong time dressed as intelligence.
3. **Reschedule instead of advancing.** The touch was never spent: nobody read
   the message. Move the next one to one working day *after* they return —
   landing on their first morning, behind four hundred emails, wastes the
   sequence you just protected.
4. **Record nothing.** Not a reply, not a positive, not a stage change. This
   is the step everyone forgets, and it is the expensive one.
5. **Keep the account in the sequence.** Automatic mail must never mark an
   account worked, closed or exhausted.
6. **File delivery notices separately from auto-responders.** "Temporarily
   deferred, will retry for 47 hours" is the mail system, not the person: no
   date, no reschedule, no bounce. A hard failure is a different outcome with
   a different consequence — suppression.

## What good looks like

- The tell: it is not the vacation message that hurts, it is the *metric* it
  writes. One auto-responder counted as a reply inflates the reply rate of
  whichever template earned it, and every downstream decision — which
  sequence to scale, which segment to keep — is then made on a number a robot
  wrote. On low volume it is the difference between 2% and 4%.
- The mediocre version treats any inbound as engagement: the follow-up stops,
  the account moves to "in conversation", and someone drafts a reply to a
  robot. Six weeks later that account is in the "already worked, no answer"
  pile, having never once been read by a human.
- You know the output is good when auto-responders are visible and boring: a
  named outcome you can count, a next touch dated after the return, and no
  movement in your reply rate when a wave of holiday mail arrives.

## Rules

- **MUST** give machine mail its own outcome, never the nearest human label.
- **MUST** leave the sequence active and the touch unspent.
- **MUST** exclude it from reply, positive and engagement metrics.
- **MUST** use a stated return date, and only a stated one.
- **NEVER** draft or send an answer to an auto-responder.
- **NEVER** mark an account worked, replied or closed on machine mail.
- **NEVER** treat a temporary delivery notice as a bounce — retry-language
  means the address may be fine, and suppressing on it kills a good contact
  permanently over a server hiccup.
