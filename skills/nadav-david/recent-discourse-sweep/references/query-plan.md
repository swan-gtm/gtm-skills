# Query plan

Read this before sweeping a named company, product or person. Skip it for a broad category topic.

Without a plan, a sweep falls back to whatever a keyword match returns, and on a named target that is the wrong corpus: same-name companies, an unrelated product, a different person with the same surname.

## Separate the routing key from the query

Two different strings, and conflating them is the most common way a sweep wastes half its budget.

- **The routing key** is the topic. Plain words, two to four of them, no brackets, no slashes, no colons, no "versus". It decides which venues get searched and how results are labelled.
- **The query terms** carry the disambiguation, the aliases, the category words and the exclusions. This is where "the analytics company, not the beverage" belongs.

Put disambiguation in the topic and it can split into two targets, the second one a fragment of the first. Two tells that this happened: a comparison section nobody asked for, and a second target whose name is a piece of the first. Both mean re-run with a clean key, not synthesise from the wreckage.

## Resolve the identifiers together, or not at all

For a named target, resolve every handle before sweeping: the short-form social handle, the code-host account, the two or three communities where the topic actually lives, and the company's own domain. Pass them as a set.

Passing one identifier and leaving the rest to a fallback produces a thin corpus that looks like a real answer. Either resolve the set or state in the report that identifiers were unresolved and the corpus is keyword-only.

## Anchor the ranking

Write one sentence describing what a relevant item looks like for this target, and rank against it. "A post discussing this company's pricing or its outages" ranks differently from "any post containing this word". Without an anchor, a common product name pulls in a hobby community and the sweep reports enthusiasm that has nothing to do with the buyer.

## Aliases to enumerate every time

- The legal name and the product name, when they differ
- The old name, if there was a rebrand
- The abbreviation and the domain, both of which appear in casual discussion far more than the full name
- The founder or the exec, if the target is small enough that discourse attaches to a person

## What to write down

Keep the plan to five lines, alongside the results, so the sweep is reproducible:

1. Routing key
2. Query terms, including exclusions
3. Resolved identifiers, or "unresolved"
4. Relevance anchor, one sentence
5. Window, in days
