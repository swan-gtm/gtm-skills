# Line items and discounts

Read this before creating any catalog product, adding a custom line, or applying a discount.

## Catalog hygiene

The catalog outlives every quote built from it. A sloppy product created to finish one quote shows up in every future search.

**Before creating a product, check all three:**
1. Search by SKU code, then by name, then by a distinctive word in the name. Catalog search often keeps the previous query in the box; clear it before each new search or the second search silently returns nothing.
2. Look for a near-duplicate with a different version suffix. Current records commonly carry a version or effective-date suffix in the SKU.
3. Confirm the offering is repeatable. If it will be sold again, it belongs in the catalog. If it exists for this deal only, it is a custom line.

**When creating one, match the house convention exactly:**

| Field | Rule |
|---|---|
| Name | Same pattern as siblings, for example "50 Signatures / Month" next to an existing "150 Signatures / Month" |
| SKU code | Same structure as siblings, including any version suffix. Uppercase, hyphenated, no spaces |
| Category | Same as siblings |
| Billing frequency | Matches how it is sold. Annual products set to annual; tools often default to monthly, which silently prices the product at twelve times the intended annual total |
| List price | The real list price, never a discounted one. Discounts belong on the quote |
| Description | One line a buyer can read. It prints on the customer document |

**Resolving duplicates by SKU, not title.** Two records with the same display name usually mean an old price and a current price. Prefer the one with the current versioned SKU and a populated description. If both look current, ask; do not pick by position in the list.

## Custom lines

Use a custom (non-catalog) line for:
- Prorated coverage to a co-term date
- One-time setup, migration, training or services scoped for this deal
- A credit for an existing balance

Every custom line needs a name a buyer understands, a one-line description, quantity, unit price, and a one-time billing frequency unless it genuinely recurs. If it recurs, it probably belongs in the catalog.

## Line items are snapshots

Adding a product to a quote copies its name, description and price at that moment. Editing the product later does not update quotes already built. To refresh a line, remove it, add it again, then re-apply any discount on that line. Check this whenever a catalog fix was needed partway through a build.

## Multi-select inserts

Inserting several products at once occasionally lands fewer than were selected. After every insert, count the lines on the quote against the request. If one is missing, insert it on its own.

## Discounts

**Percent or fixed amount.** Use the form the request used. "200 off" is a fixed amount per unit or per line; "10 percent" is a percent. If the request says "200 off the deal", put it on the line it belongs to, or split it evenly only when told to.

**Worked check.** List 1,800, fixed discount 200, quantity 1. Row subtotal must read 1,600 and the quote total must drop by exactly 200. If the total did not move, the discount did not apply; re-enter it.

**Presentation rules that protect the next renewal:**
- Discount on the quote, never on the product's list price. The buyer should see the list price, the concession, and the net.
- Name time-limited concessions on the line ("first-year discount") so the renewal quote does not inherit an anchor nobody meant to make permanent.
- Multi-year discounts belong on the multi-year option only. Putting the multi-year rate on a one-year option removes the reason to sign for longer.

**Approval.** Most companies have a discount approval matrix by depth and deal size. Check it before applying anything the requester did not already clear. Common defaults when no matrix is written down: a rep can give up to 10 percent alone, 10 to 20 percent needs a sales leader, above 20 percent or any non-standard term needs the deal desk or finance. Build the draft either way; flag the approval needed in the report and hold the send.
