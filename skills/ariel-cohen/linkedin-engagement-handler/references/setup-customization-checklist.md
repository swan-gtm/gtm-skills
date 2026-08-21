---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Trigger setup

This skill runs from a **LinkedIn Engagement trigger** on the profile
owner's connected LinkedIn account — one trigger + one skill instance per
tracked person. Reference trigger instructions (keep stop-conditions in the
trigger so obvious noise never loads the skill):

```
## Overview
This trigger monitors all engagement on [Owner]'s LinkedIn posts — comments
and reactions. This is direct inbound interest in your content and
[Owner]'s thought leadership.

## Stop Conditions
Stop immediately and take no action if the engager:
- Works at [your company] ([internal domain], or known team members by name
  — include teammates whose LinkedIn doesn't show your company as employer)
- Works at a university, college, or academic institution
- Has an academic title (Professor, Lecturer, Researcher, PhD Student, ...)
- Has no identifiable company

Otherwise, load and follow the <LinkedIn Post Engagement Handler> skill.

## Notification Routing
- Only send notifications when a meaningful action was taken (outreach
  drafted, account updated, follow-up scheduled)
- Do NOT send notifications when engagement is filtered out for lack of
  intent
- Route all notifications from this trigger ONLY to [engagement channel]
```

- [ ] Profile owner's LinkedIn account connected to the workspace
- [ ] Decide comments-only vs comments+reactions at the trigger level
      (reactions are higher volume, lower signal)
- [ ] Dedicated Slack channel per profile owner recommended

## 2. Placeholders

All `{{...}}` in SKILL.md filled — most important:

- [ ] **Persona lists** — the "relevant personas" and "ignore" lists are the
      main quality lever. Tune to your buying committee before enabling.
- [ ] `{{HIGH_ACV_TAG}}` — must actually exist as a tag/attribute in your
      workspace, and something must be setting it (the high-value path never
      fires otherwise).
- [ ] `{{SELF_SERVE_THRESHOLD}}` and `{{ALERT_TIERS}}` — match your
      segmentation and scoring model.
- [ ] Sub-skills exist: CRM hygiene, lead scoring, alert format.

## 3. Policy decisions

- [ ] **Connection requests default to queue-for-approval** (high-value
      path step 5). The original deployment auto-sent them with no approval
      — deliberate, but only for the narrow high-ACV + decision-maker path
      with no note attached. Switching to auto-send is a conscious opt-in;
      align with your risk tolerance and LinkedIn account hygiene.
- [ ] **Reactions are a separate lane** — a lone like only logs to CRM +
      account memory; the {{ALERT_TIERS}} and repeat-engagement exceptions
      are the only escalators. Widening this is a conscious choice —
      reaction volume is much higher and signal much lower than comments.
- [ ] **Repeat engagers get a multi-channel sequence built and queued for
      review** (at 2+ interactions), never sent automatically. If your org
      wants auto-send, that's an explicit policy change on your side.
- [ ] **Lead magnet section** — keep it accurate. The skill must only ever
      share the URL currently written in that section; when no lead magnet
      is active, it must say so explicitly (prevents the agent improvising a
      link).

## 4. Behavioral invariants (do not remove)

- ICP company alone is not enough — persona gate applies to every engager.
- LinkedIn engagement is the lowest-weight signal; tier cap unless stacked.
- Never move an account backwards in the funnel.
- A lone reaction never fires the high-value path or an alert, and the
  active-buyer check runs before every repeat-engagement escalation.
- High-value Slack post fires only when an action was taken — filtered
  engagement stays silent.
