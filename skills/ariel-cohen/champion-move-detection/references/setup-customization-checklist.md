---
title: "Setup & customization checklist"
description: "Placeholders, policy decisions, and behavioral invariants to work through before enabling champion move detection."
---

# Setup & customization checklist

Work through this once before enabling the skill; revisit when your GTM motion changes.

## Placeholders (all required unless noted)

| Placeholder | What to set it to |
|---|---|
| `{{PRODUCT}}` | Your product's name as it appears in memory notes and alerts |
| `{{CRM}}` | Your CRM (HubSpot, Salesforce, Attio, …) |
| `{{SCORING_SKILL}}` | The account-scoring skill this feeds. The champion move enters it as a first-party, high-intent signal — the scoring skill owns tiers, gates, MQL routing, and outreach downstream |
| `{{LINKEDIN_LOOKUP}}` | A live LinkedIn profile lookup (e.g. an Apify profile-search actor) that returns the full experience section — the verification rules depend on it |
| `{{MQL_OWNER}}` | The person/queue that owns champion-move tasks and alerts |
| `{{DIGEST_CHANNEL}}` | Channel for the monthly digest |
| `{{COMPETITORS}}` | Your direct-competitor list; moves into them are logged, never scored |
| `{{WATCHLIST_MAX}}` | Default **5** per account. Raise only for very large committees |
| `{{REFRESH_WINDOW}}` | Default **90 days** between watchlist rebuilds |
| `{{USAGE_WINDOW}}` | Default **90 days** of usage for the "materially active" bar |
| `{{SELF_SERVE_THRESHOLD}}` | Default **<50 employees AND ≤$10M raised** — below it, moves are FYI/future pipeline, never MQLs |
| `{{TIER_FLOOR}}` | The floor a confirmed champion move scores (default: one tier above mid). Must NOT override your scoring skill's hard gates |

## Policy decisions to make deliberately

1. **Per-person usage attribution.** Identify where your product records usage by individual user (events, credits, seat activity). Org-level totals cannot support the heavy-user leg — if you only have org-level data, the heavy-user leg degrades to the champion leg only; say so in the digest.
2. **Tag + stage conventions.** Create a `champion-move` tag (or your equivalent) and confirm which stage your MQLs enter. The tag + an active carried-forward watchlist entry are what keep non-customer companies in the monthly scan set.
3. **Outreach stays human.** This skill never sends. Confirm your scoring skill's outreach steps are queued-for-approval unless you have explicitly opted into auto-send there.
4. **Prior-owner etiquette.** Decide how the prior relationship owner is surfaced (recommendation inside the owner's task is the default) — not as an automatic sender.
5. **Never-prospect list.** Confirm standing exclusions (advisors, partners, government, VC/PE) live where the scoring skill's gates can see them.

## Behavioral invariants (do not remove when editing)

- MOVED requires affirmative evidence from the experience section, plus the wrong-person guard (origin company must appear in the destination profile's history).
- The B.0 qualification gate runs before any scoring: realized value AND not a recent closed-lost. Warm familiarity is not advocacy.
- One move → one MQL, ever (the `MOVED → processed` marker is the dedup record; never delete it).
- Multiple movers to one destination = one signal, scored once.
- Carried-forward entries survive watchlist rebuilds.
- UNCERTAIN never fires the MQL flow.
