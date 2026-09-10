---
name: "event-room-intelligence"
title: Event room intelligence
description: "Use this skill 1 to 3 days before any face-to-face event where you hold a registration export (a talk, conference, dinner, booth) and the question is 'I have the attendee CSV, who should I talk to?'. It maps every registrant to a company, joins the list against the live CRM, LinkedIn-verifies every person's title and employer, sizes and funds every company, hand-authors the buying committee for every account worth hunting, and prints a phone-readable PDF dossier: one account per page, warm hunt accounts first, each card telling you within five seconds who the buyer is, whether they are in the room, and what to say. Also answers 'room intelligence', 'attendee report', 'prep me for the event', 'who is coming from which accounts'."
category: Events
tags: [Sales, Marketing]
---

# Event room intelligence

Runs 1 to 3 days before a face-to-face event, as soon as the registration export exists. Produces a phone-readable PDF dossier, one account per page, that the people walking the floor read on the way in: who the buyer is at every account in the room, whether they are physically there, and the one-line play.

## Template placeholders

Replace every `{{...}}` before running. The card-anatomy reference lists them with defaults.

- `{{PRODUCT}}` - Your product's name
- `{{CRM}}` - Your CRM; read live, never from an export
- `{{PROFILE_LOOKUP}}` - Your LinkedIn profile lookup (URL scrape plus name-and-company profile search). Must return photo, current headline, current employer, work email
- `{{COMPANY_LOOKUP}}` - Your company enrichment for employee count, total raised, last round
- `{{HUNT_TIER}}` - The tier that makes an account a hunt target when someone from it is in the room (default: **Gold and above at MQL stage**)
- `{{LARGE_COMPANY_FLOOR}}` - Size above which an untiered company still gets a full card (default: **200+ employees or $50M+ raised**)
- `{{DEMOTE_LIST}}` - Giant, well-known logos that stay in the dossier but move to the end of the cold list (enterprise-gated, or no buyer in the room)
- `{{COMPETITORS}}` - Competitors; they get a watch-list line, never a card
- `{{ALIAS_LIST}}` - Your maintained registrant-name-to-domain overrides, grown event over event
- `{{LOOKUP_BATCH}}` - Companies per enrichment sub-agent when sizing fans out (default: **12**)
- `{{FLOOR_TEAM}}` - Who from your side attends and reads the dossier

## Inputs (ask once)

The registration export (name, email, approval status, and whatever title, company, and LinkedIn fields the form collected), the event date, who from `{{FLOOR_TEAM}}` attends, and the goal: hunt deals, meet customers, or recruit. Everything else is derived.

## Phase 1 - Map every registrant to a company

Run the waterfall in order and record which rung matched, because the rung sets the confidence you show on the card:

1. Business email domain (skip free-mail domains, and a small list of tracking or redirect domains that masquerade as companies).
2. The registration form's company field, normalised.
3. `{{ALIAS_LIST}}`: manual name-to-domain overrides for people you know registered with a personal address.
4. Name match against the roster of a prior event, where the same person was already mapped.

Personal-email registrants who fail all four rungs stay unmapped until Phase 3 resolves them from LinkedIn. Deduplicate on domain plus normalised name, keeping the approved row over the invited one. Read `references/company-mapping-waterfall.md` for the free-mail list, the alias-list format, and the dedup rules.

## Phase 2 - Join against the live CRM

For every mapped company, read from `{{CRM}}` in this order: tier tags, funnel stage, owner, open deal and amount, customer status (active and ever-paid). Tiers move daily; a tier export from earlier in the week is already wrong. Also pull any stage or tier mismatch (a low tier sitting at MQL stage is a data bug, not a hunt target) and the competitor tag.

## Phase 3 - Verify every person on LinkedIn

For every registrant and every buying-committee contact, run `{{PROFILE_LOOKUP}}`:

- With a profile URL: scrape it for photo, current headline, current employer, work email.
- Without one: profile-search by name plus mapped company, then apply the match rules. A single first name needs both a first-name match and a company match. A full-name match with no company evidence is a `name-only` match and is labelled as unverified on the card.
- If the current employer no longer matches the mapped company, mark the person `moved` and show where they are now.
- Every untitled or first-name-only registrant gets this pass. Invite-only rows hide the seniors: last run, 39 Director-and-above people carried no title in the export, and a VP of Global Sales Development surfaced only because her first name plus email domain resolved on LinkedIn. She was the buyer for the whole use case.

Trust the LinkedIn read over `{{CRM}}`. Between 25 and 35 percent of CRM contacts had changed jobs at the last run. The original hand-raiser at one hunt account had left; the person being sequenced at another had become COO somewhere else. Both would have been the wrong name to walk up with.

Cost and effort marker: roughly $4 of `{{PROFILE_LOOKUP}}` credits for about 130 people. Checkpoint every batch to a file so a retry never re-spends.

## Phase 4 - Size and fund every company

For every mapped company, get employee count, total raised, and last round from `{{COMPANY_LOOKUP}}`. Fan out in batches of `{{LOOKUP_BATCH}}` with one approval for the whole run; 132 companies took about 13 minutes. No account with an attendee may reach the dossier without size and funding; if the provider returns nothing, say `unresolved` on the card rather than leaving it blank.

## Phase 5 - Hand-author the buying committee

For every hunt, warm, large-company, deal, and customer account, write the committee by hand from `{{CRM}}` history, account notes, and the Phase 3 reads: name, title, role in the deal, LinkedIn, email. Decision maker first, then sponsor, then champion or hand-raiser, then the RevOps or systems influencer, then people merely in the room, departed contacts last with a `left` label and their new employer. Read `references/buying-committee-rubric.md` before writing any card.

## Phase 6 - Build and print

Assemble the HTML from the joined data and print to PDF. Cards come first and are ordered: hunt accounts (`{{HUNT_TIER}}` with people in the room), warm accounts, large companies, open deals, customers. Within a group, sort by number of approved attendees, then invited attendees. `{{DEMOTE_LIST}}` goes to the end of the cold list. After the cards: room stats, seniors hidden in the invite list, faces grid, role mix, company map, competitor watch list, full directory, methodology. Card content and print settings are specified in `references/card-anatomy-and-sort-order.md`.

Deliver as a local file only. Read `references/day-of-and-after-checklist.md` for how the floor team uses it and how to close the loop after the event.

## What good looks like

- **What the expert notices first: who came as a group.** Several registrants from one company, and above all a manager plus their team, is the strongest signal in the room. Last run a cybersecurity company registered eight people, its entire sales-development org including the VP. The delegation was itself the buying signal. The play was a team demo, and naming the RevOps director already in a direct-message thread with the CEO so both threads would meet.
- **Second look: the untitled and first-name-only rows.** These are where the seniors sit. A dossier that only covers people with a job title on the form has missed the buyers.
- **The common mistake is trusting CRM titles.** A quarter to a third of them are stale. The second mistake is producing a company table when the job is a floor plan of who to hunt. The third is a face grid: rejected, the per-account card is the product.
- **The numbers from the last run**, useful as a sanity check: 254 registrants, 170 mapped to 132 companies, 87 already in the CRM, 47 dossiers, 39 Director-and-above people with no title in the export.
- **Print for the phone**: 20px body, 120px avatars, no intro page, the first page is the first card, the group label lives inside the card so there are no heading-only pages.
- **The quality bar**: you can read it on your phone walking in; hunt accounts come first; for every card you know within five seconds who the buyer is, whether they are in the room, and what to say. Every person has a photo, a current title, and an email, or is explicitly marked `unresolved`. No account with an attendee is missing size and funding.

## Rules

- MUST LinkedIn-verify every title and employer before the event. A CRM title is a hint, never the label on a card.
- MUST resolve every untitled and first-name-only registrant through profile search before calling anyone undetected.
- MUST read tiers, stages, owners, and deal values live from `{{CRM}}` at build time.
- MUST mark every person who could not be resolved as `unresolved` or `unverified match`; never present a guess as a fact.
- NEVER publish or share the dossier outside `{{FLOOR_TEAM}}` and the account owners. It contains personal data and deal values; it is a local file, not a link.
- NEVER send outreach from this skill. It recommends who to approach and what to ask; humans send.
