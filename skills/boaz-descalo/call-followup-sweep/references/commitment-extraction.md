# Commitment extraction

How to read a call transcript for the four things that survive it. Everything
else in a transcript is context; these four are the only things that create an
obligation, and they are what the sweep is for.

## The four categories

Extract into these buckets, in this order. The order is deliberate — category 1
is the one reps skip and the one that costs deals.

| # | Category | What it sounds like | Why it matters |
|---|---|---|---|
| 1 | **You committed** | "I'll send…", "let me check with…", "I can get you…", "we'll put together…" | The seller's unshipped promise is the single most common silent deal-killer. Nobody chases you for it; they just downgrade you. |
| 2 | **They committed** | "I'll loop in…", "let me get approval…", "I'll pull those numbers…" | This is your legitimate reason to follow up, and the thing to make legible in writing so it does not quietly evaporate. |
| 3 | **Question you didn't answer** | a direct question followed by a pivot, "good question, let me come back to that", a number you approximated | An unanswered question is an open objection wearing a polite face. It resurfaces at procurement. |
| 4 | **Date named out loud** | "before end of quarter", "our board meets the 14th", "we're heads-down until after launch" | Their dates, not yours, set the real cadence. A date said once on a call is worth more than any cadence rule. |

## The extraction pass

1. **Read for first-person future tense from the seller's side.** Search the
   transcript for the seller's own "I'll", "I can", "we'll", "let me". This
   single pass catches most of category 1 and takes under a minute per call.
2. **Read for the same from the buyer's side** — category 2.
3. **Find every question mark from the buyer and check whether an answer
   followed.** A question that got a story instead of an answer is category 3.
   So is any answer containing "roughly", "I think", "around" attached to a
   number, price, timeline, or security claim.
4. **Collect every date, deadline, and time-bounded phrase** regardless of who
   said it — category 4. Convert relative phrases ("end of next month") to
   actual dates against the call date, and mark them as inferred.
5. **Note who was on the call and did not speak.** A silent attendee on a
   multi-stakeholder call is a stakeholder signal, not a commitment. It belongs
   in the sweep report, not in the email.

## What gets missed

- **The conditional promise.** "If you want, I can put together a rough number"
  is a commitment the moment the buyer says "yeah". Reps hear the "if" and file
  it as optional; buyers hear the offer and wait for it.
- **The delegated promise.** "I'll ask our solutions team to look at that"
  creates an obligation on the seller even though the work belongs to someone
  else. It ages exactly like a direct promise and is forgotten faster.
- **The promise made in the last ninety seconds.** Wrap-up is where most
  commitments are made and where transcript attention is lowest. Read the final
  ninety seconds twice.
- **The number said aloud.** Any price, discount, timeline, headcount, or SLA
  figure spoken on a call is a commitment in the buyer's memory whether or not
  it was qualified. Extract every one and flag the ones that were hedged, so the
  user can decide whether to confirm or correct it in writing.
- **The thing the buyer repeated.** If a buyer raises the same concern twice in
  one call, it is the actual blocker regardless of what the stated next step is.

## Worked example

Transcript excerpt, discovery call, 34 minutes, two attendees on the buyer side:

> **Buyer (Dana, VP Ops):** …the part I keep coming back to is whether this
> survives our SOC 2 review. Last vendor took four months.
> **Seller:** Totally fair. We've been through it a bunch — I'll dig up the
> report and get it over to you.
> **Buyer:** Great. And what does this look like at 40 seats instead of 12?
> **Seller:** Roughly it scales linearly, so call it low five figures, but let
> me confirm with our team and come back with a real number.
> **Buyer:** Okay. I'll get Marcus to sit in next time — he owns the budget.
> **Buyer:** …and honestly the SOC 2 thing is the piece I need resolved before
> I can take this anywhere internally.
> **(Second buyer attendee: silent for the full call.)**

Extraction:

- **You committed** — (a) send the SOC 2 report, no date given; (b) come back
  with a real 40-seat number, no date given.
- **They committed** — Dana brings Marcus, budget owner, to the next call.
- **Question you didn't answer** — 40-seat pricing. Hedged aloud as "low five
  figures", which is now anchored whether or not it was meant to be.
- **Date named** — none explicit. Nothing to convert; say so rather than
  inventing "next week".
- **Signals for the report** — SOC 2 raised twice, second time as an explicit
  internal blocker: this is the real gate, not pricing. One buyer attendee never
  spoke; worth naming before the next call.

The draft that follows from this leads with the SOC 2 report and a date, states
the 40-seat number as pending with a date, and confirms Marcus for the next
call. It does not recap what Dana said about her last vendor.
