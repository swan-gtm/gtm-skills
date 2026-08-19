---
name: audit-the-base-not-the-rate
title: Audit the base, not the rate
description: |
  Use this skill whenever a percentage in a commercial term is being set, questioned, or is
  producing a number nobody expected — sales commission, revenue share, affiliate and creator
  payouts, channel margin, agency fees, referral fees, rebates. Triggers: "reps are hitting quota
  but margin isn't moving", "what does this promo actually cost us", "our partner payouts are
  higher than the model", "is 15% a fair rate", "we're renegotiating the split", "the comp plan
  is paying out on deals we lost money on". It finds what the percentage multiplies, identifies
  the condition under which that choice starts to matter, quantifies the gap at that condition,
  and identifies the clause to revisit.
category: RevOps
tags: [RevOps, Sales]
---

Percentages get negotiated loudly. Bases get agreed in a subordinate clause. The rate is what everyone argues about and the base is what determines the money.

**This is a check, not the answer.** Run it, state what it found in a line or two, then return to the question actually asked and answer that. If someone asks whether a discount is survivable, the base is one input among retention, cash flow, acquisition cost and cost to serve — surface it, quantify it, and move on. An answer that audits the clause thoroughly and never addresses the decision is a worse answer, however correct the audit.

A term counts as unambiguous only when it states which side of fees, tax and refunds it sits on. "The amount actually paid" does not: it reads as the customer's payment or as what settled to you after processing, and those are different numbers. If the clause does not say which, the base is undefined — name both readings and price the gap, however confident the wording sounds. Where it genuinely does say, confirm it in a sentence and spend nothing further on it.

## Find the multiplicand

Every percentage term multiplies something. Locate the noun, not the number:

- **Sales commission** — bookings, billings, recognised revenue, or cash collected? Before or after discount? Before or after churn and clawback? Of revenue or of gross margin?
- **Supplier or creator revenue share** — list price or the price actually paid? Gross or net of processing fees? Does it reach shipping and tax?
- **Affiliate and channel payouts** — order total or product subtotal? Before or after a discount code? New customers only, or every order the cookie touches?
- **Agency fees** — gross media spend or net? Does it include the platform's own fees?
- **Referral fees** — first-year contract value, total contract value, or collected cash?

These are starting points, not a taxonomy. Do not rely on an assumed industry default. Read the clause and name the noun.

## Find the condition where the bases diverge

This is the part that gets skipped, and it explains why bad bases survive for years: **under normal conditions the difference between competing bases is invisible, small, or quietly accepted.** Some pay out identically until an event separates them; others differ on every transaction by an amount nobody has ever totalled. Find the point where the difference becomes material.

Name the event, then compute both bases at it:

| Term | Difference stays invisible when | It becomes material on |
|---|---|---|
| Revenue share | full price | any discount, promo code, or negotiated price |
| Commission on revenue | standard pricing | discounting, or a deal with unusual delivery cost |
| Commission on bookings | nothing churns | refunds, non-payment, early cancellation |
| Affiliate on order total | no discounts, no returns | codes, partial returns, shipping-heavy orders |
| Agency on gross spend | fees are trivial | platform fees rise, or spend shifts channel |

If a base has never been tested against its divergence condition, its economic consequences have been assumed rather than validated.

## Quantify at the condition

Model both bases at the divergence event and state the per-unit gap, not just the totals.

Worked, revenue share: supplier takes 55%, your percentage costs are 10%. On a **list-price** base the supplier's payout does not move when you discount, so every 1.00 of discount costs you **0.90**. On a **received-price** base their payout falls with the price, so the same 1.00 costs you **0.35** — roughly a third of the damage, from a clause, not a negotiation.

The same shape appears elsewhere. Commission on bookings rather than collected cash pays full rate on revenue that never arrives; the gap equals your non-payment rate times total commission. Affiliate on order total rather than product subtotal pays partners a percentage of your shipping costs.

State the figure as a rate — "each 1.00 of discount costs 0.90 against 0.35" — because that number is what survives into the renegotiation. Then multiply it by the affected volume where that volume is known: a gap of 0.09 per order is a rounding error on one deal and a budget line across four million. The scaled exposure, not the per-unit figure, is what decides whether the clause is worth reopening.

## Work backwards when payouts miss the model

The common real case is not a clause being drafted — it is a payout that came in wrong and nobody knows why. The same arithmetic runs in reverse, and it localises the error before anyone opens the contract.

If the rate is unchanged and payout is otherwise simply `rate × base` — no tiers, caps, minimums, accelerators, fixed fees or clawbacks — the discrepancy is in the base:

`actual base / modeled base = actual payout / modeled payout`

and the size of what the model missed is:

`unexplained base = (actual payout − modeled payout) / rate`

So a payout 40% above model means the real base is roughly 1.40× the modelled one — and you are looking for a component of about that size. That number is the search filter. Shipping, tax, discount treatment, returns not deducted, renewal or cookie attribution: check them against the magnitude rather than one at a time.

Before diagnosing a base error, confirm that actual and model cover the same period, event, population and unit. A quarter's lag or an accrual-against-payment mismatch produces a stable overage that looks exactly like a base error.

Do not name a cause from the ratio alone. A total cannot distinguish an inflated base from an elevated rate — both produce the same number — so check the effective rate per line before concluding either. State the magnitude, offer the common candidates, and if none of them fit, ask what sector-specific variable could move a base by that amount.

## Change the base, not the rate

A base change can be easier to frame than a rate cut, because the headline percentage stays where it is. Where the two bases coincide on ordinary business, say so and quantify it — the ask then costs the counterparty nothing outside the condition being fixed, and that arithmetic is the argument. Where they differ on every transaction, the ask is a real transfer and should be traded as one rather than presented as a technicality.

## What good looks like

- The multiplicand is named before anyone argues about whether the rate is fair. A rate without its base is not a number you can evaluate.
- The output is a figure someone can act on — "each 1.00 of discount costs 0.90 against 0.35, and we discount 4,000 orders a quarter" — not an observation that the base matters.
- The base finding stays in proportion. A commercial question gets a commercial answer with the clause as one input; an answer that audits the contract thoroughly and never addresses the decision has failed even when the audit is correct.
- Where the base is genuinely ambiguous, both readings are priced. Where it is genuinely defined, that is confirmed in a sentence and nothing further is spent on it. Manufacturing ambiguity is as costly as missing it.
- A mismatch between actual and modelled payouts produces a magnitude to search for, not a named cause. The ratio narrows the field; the line-level data closes it.

## Rules

- MUST answer the question that was asked. The base audit is an input to it, never a replacement for it, and never the structure of the response.
- MUST identify the multiplicand before discussing whether the rate is fair.
- MUST treat a base as undefined unless the clause states its position relative to fees, tax and refunds. Confident phrasing is not definition.
- MUST scale the per-unit gap to the affected volume where that volume is known.
- NEVER assume a standard base, or infer one from what the parties presumably meant.
- NEVER present a base change as a rate cut. They are different asks and the second one loses.
- Where the base is unknown, model both and recommend neither. Leading with one and noting the other differs is not a caveat — the reader keeps the first number.
