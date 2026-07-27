---
title: "Setup & Customization Checklist"
description: (reference)
---

# Setup & Customization Checklist

## 1. Trigger setup

This skill runs from a **meeting-completion trigger** — fired when
{{MEETING_NOTES_TOOL}} finishes processing a meeting involving
{{MEETING_OWNER}}. One skill instance per person. Reference trigger
instructions:

```
A meeting involving [Owner] has completed and its notes are ready.

Load and follow the <Post-meeting execution> skill in full.

Context for this run:
- Meeting owner: [Name] ([email])
- Meeting record: [meeting ID / link from the notes tool]
- Internal domain: [yourcompany.com]
```

- [ ] {{MEETING_NOTES_TOOL}} is connected and produces summary + full
      transcript + attendees. The transcript is load-bearing — the
      grounding rule, qualification scoring, and next-step distillation
      all read from it.
- [ ] {{MEETING_OWNER}}'s LinkedIn account is connected (Step 12).
- [ ] {{REVIEW_CHANNEL}} exists and the owner actually reads it — this
      is the single surface for every approval.

## 2. Placeholders

- [ ] `{{MEETING_OWNER}}`, `{{MEETING_NOTES_TOOL}}`, `{{CRM}}`,
      `{{REVIEW_CHANNEL}}`, `{{INTERNAL_DOMAIN}}`,
      `{{FOLLOWUP_SCENARIOS_SKILL}}`, `{{VOICE_GUIDE_SKILL}}`,
      `{{LEAD_SCORING_SKILL}}`, `{{ENTERPRISE_ACV_THRESHOLD}}`,
      `{{SALES_ACTIVE_TAG}}`, `{{METRICS_LOG}}` — all filled.
- [ ] Map the Step 6 stage-semantics table to **your** funnel stage
      names. The table references semantics (scoping, consideration,
      procurement...), not your labels.
- [ ] Write or adapt the two sub-skills before going live:
      {{FOLLOWUP_SCENARIOS_SKILL}} (your outcome taxonomy + per-category
      email frameworks) and {{VOICE_GUIDE_SKILL}} (how the owner
      actually writes — without it every draft sounds like a bot).
- [ ] If you don't track meeting metrics, delete Step 3 rather than
      leaving {{METRICS_LOG}} unfilled.

## 3. Policy decisions

- [ ] **The owner sends the email, always.** The skill drafts; the human
      copies it into their own inbox (preserves CC and threading). If
      you'd rather have the agent send on approval, change Step 10's
      closing rule deliberately — don't drift into it.
- [ ] **Deal creation is a recommendation, never an action.** Even a
      4/4 qualification score only produces a Yes/No question. Confirm
      the override criteria (authority in the room + exceptional fit +
      structural growth pressure) match your motion.
- [ ] **Trial stage ownership:** if a product signup event sets your
      trial stage, keep the Step 6 warning — meetings must never set it.
      If you have no such event, delete the warning and treat trial like
      any other stage.
- [ ] LinkedIn connection requests (Step 12) default to queued for
      approval. If blank-note requests to actual attendees fit your
      norms, flip them to auto-send — that is how the workflow ran in
      production.
- [ ] Default follow-up reminder of 5 business days when the owner
      doesn't answer the timing question — adjust to your cycle length.

## 4. Behavioral invariants (do not remove)

- Non-blocking errors never skip downstream steps; only a missing
  meeting record aborts the run.
- Deal existence is never evidence of a prior meeting — the 6-month
  recency filter and same-day-deal rule stay, or first-touch metrics
  will be silently wrong.
- Read-after-write verification on every metrics-log write; a false
  success is surfaced, never swallowed.
- The grounding rule: nothing enters the email that wasn't in the call.
- Every contact enriched, new or existing — no title, not done.
- The full email body appears in the Slack post — no truncation, no
  "see task for details."
- The next-step line: hard blockers only, one line, under 150 chars.
- Step 12 runs in its own action, last, regardless of prior failures.
