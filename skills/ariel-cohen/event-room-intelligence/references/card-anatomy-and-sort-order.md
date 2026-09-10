---
title: "Card anatomy and sort order"
description: "Exactly what one account card contains, how cards are grouped and ordered, what follows the cards, and the print settings for phone reading."
---

# Card anatomy and sort order

The card is the product. Everything else in the dossier is supporting material. Do not replace cards with a table or a face grid; both were tried and rejected because neither answers "who is the buyer and are they here" in five seconds.

## One card, top to bottom

| Block | Content | Source |
|---|---|---|
| Group label | Inside the card, top-left: Hunt, Warm, Large company, Deal, Customer | Phase 6 grouping |
| Header | Company name, domain, CRM owner (or "no owner") | Live `{{CRM}}` read |
| Size line | `1,200 employees · Series C 2024 · $85M raised`, or `public`, or `bootstrapped`; any note such as "acquired by X" or "in insolvency" | `{{COMPANY_LOOKUP}}` |
| Status label | Right-aligned: `Tier · Stage · $deal · owner first name` | Live `{{CRM}}` read |
| Why | Two to four sentences: what the relationship is, what happened last, who is engaged, what is blocking | Account notes plus CRM history, hand-written |
| In the room | Every registrant from this company: photo, name linked to LinkedIn, verified title, approval status, email | Phase 3 |
| Decision makers and champions | The buying committee in rubric order: photo, name, title, role in the deal, email, one-line note | Phase 5 |
| Play | One line: who to approach, what to ask, who on `{{FLOOR_TEAM}}` takes the name afterwards | Hand-written |

### Title rendering

Show the registration-form title, and when the LinkedIn title differs, append `LinkedIn: <current title>` in a muted style. Both matter: the form title is what the person calls themselves this week; the LinkedIn title is what their employer calls them.

### Person labels

- `unverified match`: profile chosen on name alone, no company evidence. Keep the photo, keep the doubt visible.
- `LinkedIn now: <title> at <company>`: the person has moved. On a registrant it means they may show up representing someone else; on a committee contact it means do not use this name.
- `left`: departed committee contact, sorted last.
- `unresolved`: no profile found after URL scrape, profile search, and email-based enrichment. Never leave the label off and hope.

## Grouping

| Group | Definition | Cards get |
|---|---|---|
| Hunt | `{{HUNT_TIER}}` accounts with at least one person in the room | Full committee, demo-booking play |
| Warm | High-tier or newly relevant accounts with no MQL alert yet; one named VP or a dated meeting moves them | Full committee |
| Large company | Above `{{LARGE_COMPANY_FLOOR}}`, mostly untiered or mid-tier, mostly represented by an individual contributor | Committee looked up so no handshake is blind |
| Deal | Open opportunity in `{{CRM}}` | Committee, and a play that says "do not pitch, advance" |
| Customer | Active or ever-paid | Say thanks, collect a reference, find the expansion seat |

Anything else with an approved attendee goes in the directory table after the cards with a one-line note. Competitors get a watch-list line, never a card, and the note says "be friendly, do not demo".

## Sort order (do not re-litigate)

1. Groups in this order: Hunt, Warm, Large company, Deal, Customer. Cold and warm-but-unworked accounts are what the floor team needs first; deals and customers already have owners and next steps.
2. `{{DEMOTE_LIST}}` accounts sink to the end of the cold list regardless of tier: enterprise-gated, or no buyer in the room. They stay in the dossier because a stray VP may still walk in.
3. Within a group: accounts with approved attendees before invite-only accounts, then by tier, then by number of approved attendees descending, then invited attendees descending.
4. Within a card, committee members follow the rubric order in `buying-committee-rubric.md`.

## After the cards, in this order

1. **Room in numbers**: registrants, approved, mapped, companies, in CRM, tier counts, stage counts.
2. **Seniors hiding in the invite list**: every Director-and-above person whose registration row carried no title, with the LinkedIn-resolved title. Last run this section held 39 people.
3. **Faces on the floor**: every approved attendee as a photo chip, priority accounts first. This is the recognition aid for the door, not a replacement for the cards.
4. **Role mix**: bars by role bucket (founder or C-suite, sales leadership, sales development, account executive, RevOps and GTM engineering, marketing, partnerships, customer success, consultant, investor, job seeker, other).
5. **Company map**: full table of every mapped company with size, round, industry, HQ, tier, stage, attendee count, attendee chips.
6. **Watch list**: competitors and partners in the room.
7. **Everyone on the list**: the unmapped and small-company remainder.
8. **Methodology and data limitations**: sources, match confidence counts, and what was not resolved.

## Print settings

- Body 20px, avatars 120px in the cards (72px thumbnails elsewhere), embedded as base64 so the PDF is self-contained.
- One account per page: page-break before every card, no page break inside a card.
- No cover, no table of contents, no group heading pages. Page one is the first hunt card.
- Print from headless Chrome to PDF, writing into the event folder. Verify the first page is a card before sending.
- Expect roughly 5 to 7 MB for 47 cards with embedded photos. Fine for a phone.

## Placeholder defaults

| Placeholder | Default |
|---|---|
| `{{HUNT_TIER}}` | Gold and above at MQL stage |
| `{{LARGE_COMPANY_FLOOR}}` | 200+ employees or $50M+ raised |
| `{{LOOKUP_BATCH}}` | 12 companies per sub-agent |
| `{{DEMOTE_LIST}}` | Empty until you have a giant logo with no buyer in the room |
| `{{ALIAS_LIST}}` | Empty on the first event, then carried forward |
