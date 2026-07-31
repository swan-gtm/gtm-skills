---
name: cold-email-preflight
title: Cold email pre-flight check
description: |
  Use this skill right before launching a cold email campaign: the final checklist
  covering authentication, list quality, copy risk, and kill-switch thresholds.
  Produces a launch/hold decision and the monitoring rules for the first week.
category: Outreach
tags: [Sales]
---

Run this in the hour before a cold email campaign goes live. It produces a launch or hold decision, and the thresholds that will stop the campaign if the first days go wrong.

## The play

1. Authentication: confirm the sending domain passes SPF, DKIM, and DMARC, and that tracking runs on a custom domain, not the tool's shared one. Any failure is an automatic hold.
2. List quality: verify every address in the batch and drop anything the verifier is not sure about. A launch list should carry effectively zero known-bad addresses; the bounce budget is spent on the unknowable ones.
3. Copy risk pass: first message carries no links and no attachments, reads like one person wrote it to one person, and every variable has a fallback so no prospect ever sees a naked placeholder. Vary phrasing across the sequence; identical strings at volume are a fingerprint.
4. Volume sanity: the day-one schedule respects each mailbox's earned capacity, ramps across the week rather than front-loading Monday, and total daily volume matches what the warmed infrastructure can carry.
5. Set the kill-switches before launch, in writing: the bounce-rate line and the placement signal that pause the campaign automatically, and who gets alerted. Deciding thresholds after the numbers arrive means deciding them emotionally.
6. First-week watch: check bounce rate and reply rate daily per mailbox. Bounces spiking means the list lied; replies flat while opens hold means the copy missed; both healthy means scale one step.

## What good looks like

- The expert habit is checking the boring plumbing first: authentication and list hygiene kill more campaigns than bad copy ever will, yet they take ten minutes to verify.
- The mediocre version launches full volume on day one with unverified addresses, links in message one, and no agreed stopping rule: every failure after that is improvisation.
- A good launch is quiet: bounces near zero, no placement alerts, and the only surprise in week one is which variant of the copy wins.

## Rules

- MUST pass SPF, DKIM, and DMARC before any send.
- MUST verify the list and remove unverifiable addresses before launch.
- MUST define bounce and placement kill-switch thresholds before the first send.
- NEVER include links or attachments in a first cold message.
- NEVER launch full volume on day one; ramp across the first week.
