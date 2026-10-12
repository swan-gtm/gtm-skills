---
name: quote-builder
title: Customer-ready quote builder
description: |
  Use this skill when a rep, founder or deal desk needs to build, draft or revise a customer quote, order form or pricing proposal in whatever quoting tool or CPQ they run. Turns "quote Acme for 150 seats and the signature add-on" into a correct, saved draft: the right customer and contact, real catalog SKUs, the right term structure (auto-renew, fixed co-termed term, or one-time), prorations as clean one-off lines, discounts that show their math, a sensible expiry, and a line-by-line reconciliation against what was asked. Builds two or three options when asked for good/better/best. Stops at draft by default and never sends to the customer without an explicit go. Trigger phrases: build a quote, draft an order form, price this out, quote them for, add a line item, co-term, prorate, renewal quote, three pricing options, apply a discount, quote PDF.
category: Deals
tags: [Sales, RevOps]
---

# Customer-ready quote builder

Applies whenever a quote, order form or pricing proposal has to be assembled for a named customer. Produces a saved draft quote whose customer, lines, term, discounts and total have been reconciled against the request, plus a short report of what was built.

A quote is the first document a buyer forwards to finance and legal. A wrong SKU, a discount that does not add up, or an expiry that reads one day short gets noticed there, not by the rep, and costs credibility that the deal needed. Treat the build as careful assembly of a customer-facing record, not data entry.

## The play

1. **Pin the requirements before touching the tool.** Customer company, the contact the quote is addressed to (name and email), products and quantities, term basis, any discount, and whether to send or only save. If any one is missing or ambiguous, ask. When the request is for several options, pin every option's exact lines first. Read `references/intake-and-term-structure.md` for the intake checklist and how to choose the term.
2. **Confirm you are quoting from the right place.** Many teams run several entities, workspaces or price books, each with its own catalog. Open the catalog and confirm the expected products are there before building. An empty or unfamiliar catalog means the wrong entity, and everything built there is wasted.
3. **Make the customer record exist.** Find the company and the contact; create them only if they are truly absent. Search by email domain as well as name, because duplicates are the most common source of quotes landing on the wrong account.
4. **Make the SKUs exist.** Every recurring line should come from the catalog. Create a missing product only when it is a real, repeatable offering, and match the existing naming and SKU convention. One-off charges such as prorations go in as custom lines, not new SKUs. Read `references/line-items-and-discounts.md` before creating products or applying discounts.
5. **Build the quote.** Give it a self-describing name (customer, headline products, cadence). Set the term structure. Default the expiry to the last day of the current month unless told otherwise.
6. **Add lines, then discounts.** Insert catalog products, add custom lines for prorations or services, apply discounts as percent or fixed amount per the request, and check each row's subtotal moves by exactly the expected amount.
7. **Reconcile and QA on the customer-facing view.** Compare the rendered quote, not the edit screen, against the request line by line. Read `references/pre-send-qa.md` for the full check and the report format.
8. **Stop at draft.** Save it, export the PDF if asked, and report back. Sending is a separate, explicit decision.

## What good looks like

- **The expert checks the entity first.** The average builder starts clicking and discovers twenty minutes in that the catalog is the wrong one. The expert spends ten seconds confirming the catalog before anything else.
- **Duplicate products are resolved by SKU code, never by display name.** Catalogs accumulate an old record and a current record with the same name, sometimes at the same price. The current one usually carries a versioned SKU and a description. Picking by title is how a retired price ends up on a live quote.
- **Prorations are one clear line.** "Coverage from signature to co-term date, 7 months" as a single one-time line reads better and survives finance review. A fake SKU per stub period pollutes the catalog forever.
- **Discounts show their work.** List price, the discount, and the net are all visible. A silently lowered unit price hides the concession and resets the anchor for the renewal.
- **The quote is checked as the customer sees it.** Edit screens hide truncation, date offsets and missing lines. The rendered view does not.
- **The mediocre version** has a generic name like "Quote 14", one line missing from a multi-select insert, an expiry two weeks out that nobody chose, and was sent before anyone looked at it.
- **Good output** is a draft whose every line, quantity, price, discount, term and expiry matches the request, with a report the rep can forward to their manager without edits.

## Rules

- MUST confirm customer, contact, products, quantities, term, discount and send-versus-save before building. Ask instead of guessing on anything customer-facing.
- MUST verify the entity or price book against the catalog before creating any record.
- MUST reconcile the final lines and total on the rendered quote against the request.
- MUST respect the company's discount approval rules. If a requested discount exceeds what the requester can approve alone, build the draft, flag the approval needed, and do not send.
- NEVER send a quote to the customer without an explicit instruction to send that specific quote. Approval for one quote is not approval for the next.
- NEVER create a catalog product for a one-off charge, and never edit a live product's price to make one quote work.
- NEVER enter, request or store customer payment details while building a quote.
