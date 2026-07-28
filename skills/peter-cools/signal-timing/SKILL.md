---
name: signal-timing
title: Signal timing
description: |
  Use this skill when a signal has fired and you need to decide when and how to reach out —
  "when do I contact them," "is this signal still warm." Given a signal type and the date it
  fired, it returns the outreach window, when it goes cold, the cadence, channel order, and a
  one-line angle.
category: Signals
tags: [Signals, Outreach]
---

An agent that turns a fired signal into a timing plan. Signals decay differently — some demand a reply within a day, some open a window over weeks — so a single cadence for everything wastes the strongest and burns the freshest.

## Input

- `signal_type` — the kind of trigger (e.g. high-intent page visit, new leadership, hiring, funding, competitive engagement, post/reaction).
- `fired_at` — the date the signal occurred.
- *(optional)* `account` — anything that shifts urgency (a deadline named in the trigger, corroborating signals).

## Procedure

1. **Classify the decay profile.** Is this an *act-now* signal (short, sharp intent — someone on a pricing or demo page) or a *ramp* signal (a window that opens over weeks — new leadership settling in)?
2. **Set the window** from `fired_at`: a reach-out-by date and a cold-after date. Starting guidance, to calibrate against your own reply data:
   - High-intent behavioral (BOFU page, demo request): reach out within ~24-48h; cold within days.
   - New leadership / role change: a ramp — the productive window tends to open a couple of weeks in and run into the second month, not day one.
   - Hiring / funding / expansion: days to weeks; the trigger names a real deadline you can anchor to.
3. **Pick cadence and channel order** to match — tight and multi-touch for act-now; patient and value-first for ramp.
4. **Frame the angle** — one line tying the outreach to the trigger's why-now.

## Output

`{ reach_out_by, cold_after, cadence, channel_order, angle }`

## What good looks like

- **Timing matches the signal, not the calendar.** The mistake: one cadence for every signal type — it over-chases ramp signals and misses act-now ones.
- **Freshness is load-bearing.** A stale act-now signal is just a cold lead again; do not treat a two-week-old page visit like a live one.
- **The window is honest.** If the trigger provides no real deadline, do not manufacture urgency — say the window is soft.
- Good output: a rep knows the exact day to send by, and why this week beats next.

## Rules

- MUST match cadence to the signal's decay profile, never a fixed sequence for all signals.
- MUST treat freshness as load-bearing — an expired window is a cold lead.
- NEVER manufacture urgency the trigger does not support.
