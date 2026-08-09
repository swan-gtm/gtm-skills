# Open-web sourcing tactics

Goal: mine **real buyer language** — the questions, jargon, and pain points people actually type — from public sources, with no paid data provider required. Anchor everything on the **category and the competitors**, never the brand; you're harvesting how the *market* talks so the prompts reflect genuine demand rather than the client's own copy.

## Where the signal is

- **Community threads and subreddits.** The highest-signal source for real questions. Public search engines often block site-scoped queries here, so read the community's own public JSON/search endpoints directly. Find the right communities by asking where the buyers hang out and inferring from the category. Pull post titles, bodies, and top comments; keep questions phrased as users wrote them.
- **Developer and technical discussion (for technical categories).** Discussion aggregators expose public search APIs — use those rather than scraping rate-limited item pages. Good for infra/dev-tool categories; harvest problem and comparison phrasing.
- **Q&A and forums.** Technical "how do I / why does" questions, consideration-stage "what's the best / is X worth it" questions, and vertical/vendor community boards. Search for URLs, then read the page text.
- **Video and its comments.** Review and comparison videos surface buyer objections in titles, descriptions, and top comments.
- **Public professional posts.** Useful for exec/business-persona language.

## Keyword expansion without a keyword tool

Approximate demand and phrasing from open sources:
- **Autocomplete, related searches, "people also ask"** — seed a term and note the phrasings surfaced; try modifiers (`best`, `vs`, `alternatives`, `pricing`, `how to`, `for <persona>`).
- **Competitor sites, blogs, and comparison pages** — this is where category jargon and the real competitive set come from; harvest the exact terminology and the way they frame problems.
- **Glossaries and docs** — precise technical vocabulary.

Record each as `keyword | estimated intent (informational / commercial / transactional) | source`. You won't have exact volumes — estimate intent and label the honest source.

## Noise filters (strip before synthesizing)

- Acronym/homonym collisions and product-name clashes with unrelated brands.
- Jobs, salaries, courses, certifications, "how to become a…" — unless the category *is* education.
- Academic and unrelated-hobby variants of a seed term.
- Spam, giveaways, affiliate-listicle fluff with no real question.
- Anything outside the target category or from the wrong audience.

## Optional enrichment (never required)

If the environment already exposes richer data (a keyword-data source, a scraping service), you may use it to enrich volumes or fetch blocked pages. Treat it as a bonus — never tell the user to install or authenticate anything. The skill must produce a complete result from public sources alone.

## What to capture

For every mined item, keep a compact block, then dedupe near-identical questions and prefer consideration/decision intent over pure curiosity:

```
QUESTION:  <the real question, verbatim or lightly cleaned>
PERSONA:   <who asks it>
THEME:     <category theme / topic cluster it maps to>
STAGE:     <consideration | decision | awareness guess>
SOURCE:    <community r/x | forum | q&a | competitor:<name> | keyword:<term> ...>
LANGUAGE:  <language it was found in>
```
