---
name: event-account-plan
title: Event account plan
description: |
  Use this skill in the weeks before a conference, trade show, or field event,
  when an attendee or registration list exists and the question is which
  companies to work, who to talk to at each one, and what to say. Trigger on
  "we have the attendee list for the show", "who should we target at this
  conference", "build the event account plan", "prep the team for the booth",
  "score this registration export", "which accounts are worth booking before
  the event". Turns a raw list into a deduplicated, signal-scored, tiered
  account plan with the buying committee behind each top account, a play per
  track, and a shared war-room page the floor team and the CRO both read.
  Leads on competitor tech signals — a dead competitor in the room is the
  best target on the list.
category: Events
tags: [Marketing, Sales]
contributors: []
---

Applies once an attendee, registration, or target-audience list exists and there
is still time to act on it — typically the two weeks before the show. Produces a
ranked account file, a decision-maker file, and a war-room page: which companies
to work, the buying committee behind each, and the play per segment. Not a
summary of the event.

## Collect five things

Ask only for what you cannot find yourself. Missing 1 or 2 blocks the work.

1. **The attendee list** — export, sheet, or paste. Company rows, and named
   registrants if you are lucky.
2. **Whose GTM this is** — the vendor's site. Homepage, product pages, and the
   customers/logos page.
3. **The event** — name, dates, venue, attendee count, track list. The track
   list tells you which personas actually show up.
4. **Credit policy** — ask explicitly whether you may spend enrichment credits.
   Most users say no. Default to search-only and say so in the deliverable.
5. **How to treat existing customers** — expansion track (the usual answer) or
   excluded. Never silently drop them.

## The pipeline

Each step feeds the next and is cheap to redo alone.

1. **Normalize.** Parse to two tables — accounts and named attendees. Dedupe
   accounts by **parent company, not by row**; big lists are full of divisions
   registering separately. Merge them, keep every division name in a
   `sheet_names` field, and count them: multiple divisions registering
   independently is a buying signal, so carry the count into scoring. Check
   which columns are actually populated first — a location column that is
   empty on every row is common.
2. **Read the ICP before scoring anything.** From the vendor's own site: what
   the product does, the named buyer personas, the verticals, the
   deal-blocking compliance regimes, the competitors they name, and the
   customer logo list. Skip this and your weights are guesses.
3. **Resolve companies.** Run accounts through whatever company-data connector
   is available for ID, revenue, employee count, HQ, and industry. Batch by
   domain. Expect roughly 90% to match; carry the misses through with blanks
   rather than dropping them.
4. **Find signals.** Firmographics rank accounts; signals tell you why now.
   Pull tech-stack tags for the vendor's own product and for every named
   competitor. **A dead or dying competitor is the best signal that exists**:
   if one has shut down, been acquired and sunset, or gone end-of-life, its
   install base must migrate. Search for that explicitly, every time. Read
   `references/signal-sourcing.md` before the first batch — it covers the
   connector traps that silently return zero rows.
5. **Score and tier.** Additive 0–100, weights adapted to the ICP from step 2,
   with a penalty for partner-motion segments. Full rubric, bands, and tier
   cuts in `references/scoring-model.md`. Score existing customers on a
   **separate expansion track** — a customer scores high on everything and
   will otherwise crowd out every new logo.
6. **Find the buying committee.** Tier 1 and top expansion accounts only.
   Names and titles are enough. Target the personas from step 2, cap at about
   eight per account, rank by persona fit first and seniority second.
7. **Write the plays.** One per track — migrate the defunct competitor,
   displace the live ones, new logo, expand customers, booth demo. Each gets a
   title, an audience, a body, a verbatim opening question a rep can say out
   loud, and a proof point. Then count buyer-persona titles among the named
   attendees: if most attendees do not own the budget, say so plainly and
   re-aim the copy at operational cost. See
   `references/plays-and-messaging.md`.
8. **Ship all three deliverables** — accounts file, decision-makers file, and
   the war-room page. Column lists, page sections, and the verification pass
   are in `references/deliverables.md`.

## What good looks like

- The best operator resolves the tech stack before touching the score. A list
  of 400 companies ranked purely on firmographics is a directory; the same list
  with "runs a competitor that shut down" on eleven rows is a quarter of
  pipeline. Rank on fit, sequence on signal.
- The common mistake is generic messaging. A play that could be sent to any
  vertical at any event has failed — the copy must name the compliance regime,
  the network zone, the audit, or the workflow that this vertical actually
  cares about. The second most common mistake is letting vendors, hyperscalers,
  consultancies, and SIs float into Tier 1; they are a partner motion, not a
  buyer motion, and they pollute the top of the list.
- Good output reconciles. Every deduplicated account lands in exactly one tier,
  existing customers sit on the expansion track, the two written fields — *why
  this account* and *the angle to open with* — are filled on every Tier 1 row,
  and the method section states plainly what you could not get.

## Rules

- MUST ask the credit policy before the first connector call, and confirm at
  the end how much was spent — "none" is a result worth stating.
- MUST record which fields came from the supplied list and which you sourced;
  a reader cannot audit a plan whose provenance is invisible.
- MUST keep existing customers on a separate expansion track, scored
  separately, never merged into the new-logo ranking.
- MUST raise sourcing and personal data unprompted: attendee lists are rarely
  public and connector data is licensed, so the user needs an answer ready for
  "where did you get this list?". Offer a masked version — initials and titles
  only — for anything shared outside the team.
- NEVER collect emails or phone numbers unless the user explicitly asks for
  them.
- NEVER drop unmatched or unenriched accounts; carry them with blanks and count
  them in the funnel.
- NEVER present a score without the weights that produced it.
