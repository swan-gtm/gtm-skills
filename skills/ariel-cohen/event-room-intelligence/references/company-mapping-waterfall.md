---
title: "Company mapping waterfall"
description: "The four-rung waterfall that turns a registration row into a company, the alias-list logic that grows across events, and the dedup rules."
---

# Company mapping waterfall

Every downstream number (companies in the CRM, tier counts, who gets a card) depends on this step. Last run: 254 registrants, 170 mapped to 132 companies. The 84 that did not map were personal-email registrants with no company field, and roughly a third of those resolved later from LinkedIn.

## Rung 1 - Business email domain

Take the domain after `@`, lower-cased. Skip it if it is on the free-mail list, then treat the remainder as the company domain.

Free-mail list to start from: `gmail.com yahoo.com yahoo.co.uk hotmail.com hotmail.co.uk outlook.com outlook.de live.com msn.com icloud.com me.com aol.com protonmail.com proton.me gmx.com mail.com ymail.com` plus your local consumer providers. Add any domain you discover to be a tenant default (an `onmicrosoft.com` subdomain) or a personal vanity domain.

Two domain traps that need a fix table, not the free-mail list:

- **Tracking and redirect domains**: a marketing-suite subdomain such as `email.<vendor>.com` maps to the vendor; a link-shortener domain maps to whichever company the person is known to be at.
- **Vanity personal domains of known people**: keep a `domain -> real company domain` fix so the row does not become a one-person company.

Record `src = email`.

## Rung 2 - Registration form company field

If the email domain is free-mail and the form has a company field, normalise it (strip `Ltd`, `Inc`, `Group`, `Technologies`, `Software`, `LLC`, parentheses, punctuation) and match it against company names already seen in `{{CRM}}` or prior rosters. A match sets the domain; no match keeps the raw name for Phase 3 profile search. Record `src = form`.

## Rung 3 - The alias list

`{{ALIAS_LIST}}` is a normalised-name-to-domain map you maintain by hand and carry from event to event. Normalise a name by NFKD-folding accents, lower-casing, and stripping everything that is not a letter or digit, so `José Núñez-García` and `jose nunez garcia` collide.

It holds three kinds of entry:

1. **Known people who register with a personal address.** Once you resolve them on LinkedIn, add them so the next event maps them on rung 3 without spending a lookup.
2. **Corrections from verification.** When Phase 3 shows the person has moved, the alias points at the NEW company, and a correction record carries the new title so the card shows current reality.
3. **Non-Latin names.** Names in a local script rarely match anything automatically; store the exact string as typed.

Record `src = manual`. Review the alias list before every event and delete entries older than two events unless re-verified; people move.

## Rung 4 - Prior-roster name match

Load the attendee lists of prior events you have already mapped and build a normalised-name-to-domain index from them. A hit here is weaker than the other rungs (same name, different person is possible), so mark `src = prior` and let Phase 3 confirm the company.

## Unmapped rows

Rows that fail all four rungs stay on the roster with `dom = null`. They are not dropped: Phase 3 runs a name-only profile search restricted to the event's country, and any hit with a plausible current employer gets a `name-only` confidence and a candidate domain. First-name-only rows go through the same search with the email domain root as the company hint when the domain is not free-mail. This is how a first-name-only invite row became a Senior VP of Sales at a funded fintech last run.

## Dedup

- Key is `(domain, normalised name)`. Process approved rows before invited rows so the approved row wins.
- Keep a `dup = true` flag on the loser instead of deleting; the directory count should still show every registration.
- Same name, two different domains: keep both. The person may have registered from an old and a new employer, which is itself a move signal.

## Title hygiene before role classification

Blank out titles that are actually the company name or a single word like `yes`. Fix obvious typos of `Founder`. Then classify each title into a role bucket with regex rules, most specific first: job seeker, then sales-development leadership before sales-development IC, then founder and C-suite, sales leadership, sales management, account executive, RevOps and GTM engineering, GTM generalist, marketing, partnerships, customer success, engineering and product, consultant, investor, other. Print every title that landed in `other` and fix the rules until that list is short.

## Output of this phase

A roster with `id, name, email, status, form title, form company, linkedin url, dom, src, created` per registrant, and a company list with `domain, name, employee count, industry, HQ, in_crm, tier, stage, owner, tags, n_attendees, attendees[]`. Print the counts (registrants, mapped, companies, in CRM) and the tier and stage distributions before moving on; they are the first line of the methodology section.
