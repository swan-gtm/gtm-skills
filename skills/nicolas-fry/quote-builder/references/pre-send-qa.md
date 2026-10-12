# Pre-send QA and the report

Read this once the quote is built, before saving it as final or exporting anything. Every check runs on the rendered, customer-facing view of the quote, not the edit screen. Edit screens truncate long descriptions, show input values rather than stored values, and lag behind lazy-loaded images.

## The reconciliation

Write the request as a list, then tick each item against the rendered quote.

| Check | Pass when |
|---|---|
| Customer | Legal company name, spelled as the customer spells it |
| Contact | Name and email of the person the quote is addressed to |
| Line count | Equals the number of lines requested. Count, do not eyeball |
| Each line | Product, SKU, quantity, unit price and billing frequency match the request |
| Descriptions | Full text renders. Nothing internal (cost, margin, internal notes) prints |
| Discounts | Each discounted row's subtotal equals list minus discount, times quantity |
| Total | Equals the sum of row subtotals, plus tax only if tax was requested |
| Term | Auto-renew cadence, fixed term length, or one-time, as decided at intake |
| Expiry | Reads the intended date on the rendered view |
| Currency | As decided at intake |

**The expiry trap.** Date fields in many tools store a value one day off from what was typed, usually because of a timezone conversion. Typing the 31st can render the 30th. Always read the expiry on the rendered quote. If it is off by one, set the input to the following day and check again.

**Images and logos** on rendered previews often load a second late. A grey placeholder that fills in is loading, not missing.

## Option sets

For a good/better/best set, also check:
- Titles make the difference between options obvious.
- The term is the same across options unless the term is what is being compared.
- The totals step up in the order the options are presented.

## Delivering without sending

- Save as draft. That is the default outcome of this skill.
- Export the PDF only if asked. Some tools generate the PDF in the browser and save it to the local machine, with no shareable link; say so if the user wants it stored elsewhere.
- Sending to the customer requires an explicit instruction for this specific quote. If a discount approval is pending, do not send even when told to; say what is pending.

## The report

Keep it short enough to forward. Template:

> Draft quote **[quote number]**, "[quote name]", for [contact] at [company].
> Lines: [product x qty at price], [product x qty at price, less discount], [custom line].
> Term: [annual auto-renew / fixed N months to co-term / one-time]. Valid until [date].
> Total: [amount and currency].
> Status: saved as draft, not sent. [Approval needed: N percent discount exceeds rep authority.]

For an option set, add one line per option with its total, and the per-year figure for multi-year options.
