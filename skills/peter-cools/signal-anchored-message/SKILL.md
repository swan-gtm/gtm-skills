---
name: signal-anchored-message
title: Signal-anchored message
description: |
  Use this skill when writing outbound to a lead who surfaced from a signal — "write the
  message for this trigger," "personalize this off the signal, not the profile." Given a
  contact, their company, and the signal that surfaced them, it returns a short connection
  note and two follow-ups anchored to the trigger and stripped of AI tells.
category: Outreach
tags: [Outreach, Sales]
---

An agent that writes outreach *from the signal*, not the profile. The trigger that surfaced someone (a raise, a hire, a move, a post) is both the reason to reach out and what the message should be about — so it reads like a person who noticed a real change, not a template with a merge field.

## Input

- `contact` — `{name, title}` and anything public about their remit.
- `company` — `{name, what_they_do}`.
- `signal` — `{type, what_happened, when}` — the trigger that surfaced this lead.
- `allowed_context` — only public or two-way-consented facts you may reference.

## Procedure

1. **Anchor on the signal's why-now.** Open on the change, not the person's title. The first line should only make sense *because* the trigger happened.
2. **Use only clean context** — public facts, or things from a real two-way exchange. Never anything that reveals scraping or surveillance.
3. **Write three touches** — a connection note (1-2 lines) and two follow-ups, each adding a new angle, not "just bumping this."
4. **Strip the AI tells** (below) and cut every word that is not load-bearing.

## Output

`{ connection_note, follow_up_1, follow_up_2 }` — short, trigger-anchored, human.

## What good looks like

- **The opener dies without the trigger.** If the first line would work on anyone, it is not anchored — rewrite it.
- **It sounds like a person, not a model.** Tells to strip: "I hope this finds you well," "I noticed you're the {title} at {company}," empty flattery, three-adjective stacks, "excited to connect," and stiff transitional filler. Short, plain, specific wins.
- **Never creepy.** It reads as "I saw the news," never "I saw you did X" — anchor on the public change, never on how you found them.
- Good output: a note the recipient could believe a thoughtful human wrote in ninety seconds.

## Rules

- MUST anchor the opener on the signal — no generic-profile openers.
- MUST reference only public or consented context; NEVER hint at how the lead was found.
- MUST make each follow-up add a new angle; NEVER "just following up."
- NEVER ship copy carrying the AI tells above.
