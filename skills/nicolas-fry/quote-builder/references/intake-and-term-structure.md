# Intake and term structure

Read this before building, whenever the request is shorter than a full spec (it almost always is) or involves a renewal, a co-term, or several options.

## The intake checklist

A quote is ready to build only when every row below has an answer. Anything marked "ask" is customer-facing and expensive to undo once the buyer has seen it.

| Field | Default when unstated | If missing |
|---|---|---|
| Customer company (legal name) | None | Ask |
| Contact the quote is addressed to (name, email) | The person who asked for pricing, if known from the thread | Ask |
| Products and quantities | None | Ask |
| Term basis | Annual auto-renew for a subscription | Confirm if a co-term or contract end date is mentioned anywhere |
| Start date | Date of signature | Confirm if the request mentions a go-live or existing contract |
| Discount | None | Never invent one |
| Expiry (valid until) | Last day of the current month | Use what was asked |
| Currency | Company default | Confirm for a customer outside the home market |
| Tax | Off unless the company always applies it | Ask if the customer is in a new jurisdiction |
| Send or save | Save as draft | Never assume send |

Shorthand requests decode predictably. "Quote them for 150 docs and 300 signatures" means two catalog lines at those tiers, annual, no discount, draft. Say that interpretation back in one line before building so a wrong read gets caught early: "Building a draft annual quote for the 150 tier plus the 300 tier, no discount, valid to month end."

## Choosing the term structure

| Situation | Structure | Why |
|---|---|---|
| New customer, standard subscription | Auto-renew, annual | Matches how the product is sold. Renewal is the default, not a negotiation |
| Add-on to an existing contract that renews on a fixed date | Fixed term ending on that date, or a proration line plus the standard annual line on the next renewal | One renewal date per customer. Two dates double the renewal work and create a churn window |
| Pilot, proof of concept, or a defined project | Fixed term, no auto-renew | The buyer is approving a bounded spend. Auto-renew on a pilot reads as a trap |
| Setup, training, migration, services | One-time line | Never recur a service that happens once |
| Multi-year | Fixed term in years, with the price per year shown | Finance teams compare per-year cost. Hide the escalator and it gets found in legal review |

## Proration and co-terming, worked

The customer's main contract renews on a fixed date. They want an add-on now. The goal is one renewal date.

**Inputs.** Add-on list price 4,000 per year. Signature expected at the start of a month. Seven full months remain until the co-term date.

**Math.** 4,000 x 7 / 12 = 2,333.33. Round to the cent and do not round up to a "nicer" number; a prorated line that does not reconcile against the list price invites a question from procurement.

**How it appears.** One custom one-time line: "Add-on coverage, 7 months to co-term." Quantity 1, unit price 2,333.33. At renewal, the add-on joins the main renewal quote at its full annual price.

**Alternative.** When the quoting tool supports a fixed term in months, a 7-month fixed term on the catalog product does the same job. Pick whichever the finance team already reconciles against; consistency beats elegance.

**Edge cases.**
- Partial month at the start: prorate by days (annual price x days / 365) only when the company does so elsewhere. Months are the common convention and easier to read.
- Fewer than 30 days to co-term: most teams waive the stub and start the add-on at renewal. Ask rather than quoting a tiny line.
- Discounted main contract: the proration inherits the same discount percent unless told otherwise. Note it on the line.

## Several options (good, better, best)

When asked for options, pin each one's lines before building any of them. Defaults that hold up:

- Three options at most. A fourth turns a decision into homework.
- Each option is its own quote, named so the difference is visible in the title: "Customer, 150 tier, annual" / "Customer, 230 tier + signatures, annual" / "Customer, 400 tier + signatures, 2-year".
- The middle option is the one the rep wants chosen. Build it first and check it hardest.
- Hold the term constant across options unless the term is the thing being compared. Changing two variables at once makes the options impossible to compare.
- Report the three totals side by side at the end, with the per-year figure for any multi-year option.
