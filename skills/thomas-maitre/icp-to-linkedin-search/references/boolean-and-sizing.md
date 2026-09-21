# The boolean string, then the company count

## Syntax for the current-title field

```
("CFO" OR "Chief Financial Officer" OR "VP Finance" OR "Head of Finance" OR "Finance Director")
NOT (fractional OR interim OR freelance OR intern OR assistant)
```

Rules:

- Quotes around every multi-word title. `Head of Finance` without quotes is three
  separate words, each matched anywhere.
- `OR` inside a family, `NOT` for the exclusions, parentheses around each group.
- At most 15 operators per field. Past that, split into two searches (for example one
  per language) rather than one string that the search silently truncates.
- Keywords are a separate field. Put the chore or the tool there ("outbound", the name
  of the CRM they run), never in the title field; a keyword in the title field finds
  nobody.
- The search platform's own filters carry `seniority`, `industries`, `sizes` and
  `locations`. Do not write them into the string.

## Sizing: count companies

Before anyone builds a list, size the audience. A daily pace of 20 invites needs a few
thousand matching companies to run for months.

| Company count | What it is | What to do |
|---|---|---|
| under 50 | a target-account list, not an ICP | widen one facet, usually `locations` |
| 50 to 500 | a campaign | fine for a one-off push; not a daily motion |
| 500 to 5,000 | a motion | build the search |
| 5,000 to 30,000 | a market, not a buyer | add an industry or narrow the size band |
| over 30,000 | the ICP has not been chosen yet | go back to the facets |

Count companies, not people. Titles do not change the company count, and people counts
double-count every firm with two matching titles.

How to count by hand, in order of precision:

1. **Account search in the paid LinkedIn search product**: industry, headcount and
   geography only. The result count is the estimate.
2. **LinkedIn company search**: industry, location and company size. Less precise (no
   fine headcount bands on the free filter), fine for an order of magnitude.
3. **A company database** the reader already has, filtered on the same three facets.

Iterate on the three company facets only. "40 companies" means widen the locations;
"30,000" means add an industry or narrow the size band. Report the count next to the
change that would move it, and only then write the people search.

## What the search cannot filter on

Two or three facets will not map to a filter: a language, "does their own prospecting",
a tech stack, "has an SDR team". Name them on the card. They get judged per person at
reading time, from the profile and the posts, not per search. A card that hides them
promises a precision the search cannot deliver.
