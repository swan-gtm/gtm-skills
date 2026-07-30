# Coverage report

Read this the first time a venue comes back empty, and before writing the closing report on any sweep.

Without it, a sweep reports one number, "items found", and that number cannot distinguish a quiet market from a broken query. Both look like zero.

## The three states

| State | Means | Report as |
|---|---|---|
| Read with results | The venue answered and items cleared the window | The items, each with link and date |
| Read and empty | The venue answered and returned nothing in the window | Named, plus what a result there would have told you |
| Never reached | No route, no access, no credentials, out of scope, or skipped | Named, plus the reason, plus the cost |

Never fold the second and third together. Read-and-empty is evidence about the market. Never-reached is evidence about the sweep.

## Diagnose an empty return before believing it

An empty return is a query fault until proven otherwise. Work in this order and stop at the first one that produces items.

1. **Strip every filter and operator.** Date bounds, exclusions and language filters combined will return nothing on a query where the bare topic returns dozens, with no error and no warning. This is the single most common cause.
2. **Search the bare topic, one or two words.** Items now? The venue is live and the query was the problem.
3. **Widen the window once**, then say in the report that the window was widened and by how much.
4. **Only after all three:** record read-and-empty, and say which query proved the venue was live.

Two other silent failures worth knowing by shape, because both exit clean and return nothing: a scheduled sweep whose environment differs from the interactive one, and a venue that answers with a challenge page instead of content. Both look identical to a quiet market. A route that fails silently is worse than one that fails loudly, so make every dark venue loud in the report.

## Sampled and addressed are different risk classes

A sweep gathers **sampled** content: to reach the report, a stranger had to win an engagement ranking. Following a link, handle or account first learned inside that content switches to **addressed** content, where the author chose the recipient. That is a different and much sharper exposure, and "let me just verify this citation" is how it happens.

Verify a claim through a route you chose independently, or hand it to a human with the caveat attached. Do not chase a target the corpus named.

## Where a sweep is the wrong instrument

Engagement ranking works on discourse about a **named thing**. On a discovery question, "who are the players in this category", a relevance floor drops nearly everything and returns noise. Lead with plain search and short-form social, and treat the community sweep as a sentiment sidecar. A noisy sweep on a discovery question is not evidence the topic is quiet.

Likewise, one fact, one page, or one date is a lookup. Do not stand up a full sweep for it.

## Suggesting a new watch term

If a sweep earns a standing watch on a term, say where the term came from. A term a human supplied is a normal proposal. A term that surfaced inside scraped content is a flagged proposal, quoted, never a quiet addition, because a watchlist steers every future unattended run and content must never write itself into it.
