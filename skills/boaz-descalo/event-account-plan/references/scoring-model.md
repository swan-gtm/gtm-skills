# Scoring model

Additive, 0–100, one score per account. Additive rather than multiplicative on
purpose: a rep can read a score and see which component earned it, and you can
defend any ranking line by line when the CRO asks why a logo they recognize sits
in Tier 2.

Adapt the weights to the ICP you read off the vendor's site. The table below is
a sane default for a product sold into a technical buyer at a mid-to-large
company, not a universal truth.

| Component | Range | How to set it |
|---|---|---|
| Industry fit | 0–30 | Rank the verticals from the ICP research, not from instinct |
| Size | 4–15 | By revenue band |
| Tech signal | 0–25 | Defunct competitor 25 · live competitor 15 |
| Named attendee | 0–25 | +5 if their title matches a buyer persona |
| Multi-division | 0–10 | 2 per extra division that registered |
| Segment penalty | −15 to −25 | Partner-motion segments |

## Industry fit (0–30)

Take the verticals the vendor names on its own site and rank them. A workable
default shape:

- 30 — a vertical named on the homepage or with a dedicated solution page
- 20 — named in customer stories or on a product page, but not headlined
- 10 — adjacent: same buyer, same compliance regime, different label
- 0 — outside the ICP entirely

Two-thirds of the spread in a finished list comes from this component and the
tech signal. If everything scores 20, you have not read the site closely enough.

## Size (4–15)

By revenue band, with employee count as the fallback when revenue is missing —
and it will be missing on a fifth of a typical list. Set the bands off the
vendor's actual deal sizes; the shape is a floor of 4 so that an unknown-size
account still ranks on its other components rather than falling out of the list.
Never score a blank as zero: a blank is missing data, not a small company.

## Tech signal (0–25)

The highest-leverage component and the one most lists skip.

- **25 — defunct competitor.** Shut down, acquired and sunset, or end-of-life.
  The install base has no choice but to move, and the timeline is somebody
  else's deadline rather than yours.
- **15 — live competitor.** A displacement conversation. Real, slower, and
  worth a different play than a green field.
- **0 — no competitor tag.** Not evidence of absence; tech-tag coverage is
  partial on most data sources. Say so in the method section rather than
  implying the account runs nothing.

The vendor's own tech tag does not score here. It routes the account to the
expansion track instead.

## Named attendee (0–25)

Someone physically in the room is worth more than any firmographic. Score the
presence, then add 5 when the title matches one of the buyer personas from the
ICP research. An account with three named attendees and no persona match is
worth less than an account with one attendee who owns the budget.

## Multi-division (0–10)

Two points per additional division that registered independently, capped at 10.
Divisions registering separately means separate budgets noticed the same event
in the same quarter without coordinating. Capping at 10 keeps a sprawling
conglomerate from outranking a focused ICP account on org chart alone.

## Segment penalty (−15 to −25)

Vendors, hyperscalers, consultancies, and systems integrators are a partner
motion, not a buyer motion. Left unpenalized they colonize the top of the list:
they are large, they are technical, they send many attendees, and a rep who
calls them wastes the pre-show window. Penalize the segment rather than deleting
the rows — they are still worth a partner conversation, on a different track.

## Tiering

- **Tier 1** — top ~50 accounts. Full treatment: buying committee, both written
  fields, an owner assigned before the show.
- **Tier 2** — next ~100. Scored and angled, worked opportunistically.
- **Tier 3** — the remainder. Present in the file, not in anyone's plan.

Tune the cuts to the size of the team walking the floor, not to the size of the
list. Five reps cannot work 50 Tier 1 accounts in two weeks; two hundred
attendees do not produce 50 accounts worth that treatment. The tier boundary is
a capacity decision wearing a scoring costume.

## The expansion track

Existing customers — flagged by the vendor's own tech tag **or** a logo on the
customers page — score on a **separate ranked list**. They will otherwise
dominate: a customer matches the ICP by definition, is the right size by
definition, and often sends the most attendees. Running one ranking for both
means the new-logo motion silently disappears from the top of the file, and
nobody notices until the show is over.

Score the expansion list on expansion logic — divisions not yet using the
product, attendees from teams outside the current footprint, and named
competitors present alongside the vendor's own tag (a competitive displacement
happening inside an existing account is the most urgent row in the whole file).

## Sanity checks before you publish the ranking

- Every deduplicated account appears in exactly one tier on exactly one track.
- Spot-check the top 10 by hand against the source rows and the customers page.
  Two of ten being wrong means a mapping bug, not bad luck.
- Look at what sits at ranks 45–55. The accounts straddling the Tier 1 line are
  where a mis-weighted component shows up most visibly.
- Check the score distribution. A list where nothing scores above 60 usually
  means the industry-fit ranking was done from instinct.
