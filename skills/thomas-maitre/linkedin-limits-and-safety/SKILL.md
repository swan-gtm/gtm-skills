---
name: linkedin-limits-and-safety
title: LinkedIn limits and safety
description: |
  Use this skill when a LinkedIn account is used for outreach and someone asks how much
  is safe: connection requests, messages, profile visits, reactions and comments per
  day, the invitation-note character limit (200 free, 300 Premium), pending-invite
  hygiene, warm-up order, weekday and working-hour pacing, the warning signs of a
  restriction, and a Monday health check with a one-screen report. Fires on "how many
  invites per day is safe", "is my LinkedIn account at risk", "LinkedIn jail", "weekly
  invitation limit", "restricted", "connection request limit", "why was my invite not
  sent", or "pace this account". Numbers hold whatever tool sends the action.
category: Outreach
tags: [Sales]
---

Applies to any LinkedIn account that sends outreach, by hand or through a tool, and to
the weekly question "are we about to lose this account?". Produces a cap per action,
a set of rules that cost more than the caps when broken, and a one-screen health
report with a verdict.

Every number is per LinkedIn account per day, whatever sends the action. They were
tuned against real LinkedIn throttling and against the ceiling most automation
providers allow (roughly 80 to 100 invites a day), and they sit deliberately under it.

## The play

1. **Set the caps.** Connection requests 20, direct messages 40, profile visits 40,
   reactions 30, comments 15. Sum 145 actions a day, the ceiling for one account
   across every tool that touches it. Lower for a new or thin account (under 3 months
   or under 200 connections: half for the first month), never for a crowded one. Caps
   and their reasons in `references/caps-and-rules.md`.
2. **Apply the rules that cost more than the caps.** Invitation notes are 200 characters
   on a free account and 300 on Premium; over the limit the invite is silently never
   sent. Weekdays only. Warm up before inviting: visit on day 0, react or comment two
   days later, then invite. Withdraw invites pending over 3 weeks. Acceptance under 30
   percent means stop and fix targeting, not send more. All rules with the reason for
   each in `references/caps-and-rules.md`.
3. **Watch for the warning signs, in order.** The weekly limit message arriving early,
   search results that stop paging, a CAPTCHA or identity check at login, notes
   silently dropped, a temporary restriction. Each sign has a response (halve, pause 72
   hours, stop a week). The ladder is in `references/warning-signs.md`.
4. **Run the Monday check.** Five yes-or-no questions on last week's numbers, then the
   one-screen report: account, usage per action against cap, 7-day invites and
   acceptance rate with a verdict, hours and weekdays, tools touching the account,
   stale invites withdrawn, next check. Template and verdict rules in
   `references/health-report.md`.

## What good looks like

- The best operator watches the **acceptance rate** before the invite count. Under 30
  percent, the caps are irrelevant: more invites at that rate is what earns the
  restriction. Fix targeting first.
- The mediocre version raises the daily cap when the pipeline is slow. The cap is the
  one number that should only ever go down; slow pipeline is a targeting or copy
  problem, and sending more of it faster is how accounts get restricted.
- Warning sign 1 or 2 with an immediate halving for two weeks is a non-event. The same
  sign ignored for a week is a restriction. The response to the first sign is what
  decides.
- The report fits on one screen, in plain words, with one verdict. Anyone can read it
  and know whether to touch the cap.

## Rules

- MUST keep the invite cap at 20 a day on a healthy account and halve it on a new one.
- MUST write invitation notes for 200 characters unless the account is known Premium.
- MUST withdraw pending invites older than 3 weeks; a pile of ignored requests is the
  strongest automation signal LinkedIn has.
- NEVER send a connection request on a weekend.
- NEVER raise a cap, resume a paused account or ignore an acceptance rate under 30
  percent to hit a pipeline number.
- NEVER appeal a restriction with "I use a tool".
