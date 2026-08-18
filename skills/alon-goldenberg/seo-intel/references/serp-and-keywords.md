# SERP research and keyword scoring

Query construction and results-page parsing rules shared by the keyword-research and rank-check plays, plus the difficulty, intent, and opportunity rubrics.

## Query normalization

Before searching any keyword:

1. Lowercase the whole query; trim and collapse whitespace.
2. Preserve intentional quotes (the user asking for `"project management"` means exact phrase) — but never add quotes to unquoted keywords.
3. Strip characters that break searches: `[ ] { }`. Keep hyphens, ampersands, and periods — they matter in brand names and domains.
4. Set country and language explicitly per run ("UK rankings" means UK geo-targeting with English results; "German rankings" means German geo and language). Never rely on defaults when the user named a market.

If a search returns fewer than 3 organic results, broaden once — drop modifiers, shorten to core terms — then skip the keyword and note "insufficient SERP data" rather than forcing a result.

## Domain matching (rank checks)

For each keyword, capture the top 20 organic results, then:

1. Normalize each result URL: strip protocol, `www.`, trailing slash; reduce to the root domain (`blog.example.com` → `example.com`).
2. The target "ranks" if any organic result's root domain matches. Record the **first** (highest) matching position — a match at #3 and #7 records 3.
3. No match in the top 20 → `position: null`. Still record which result-page features appeared and when the check ran — knowing what the results page looks like is useful even when you're absent, and it proves the query ran.

## Results-page feature taxonomy

Scan each results page and record which features are present (as evidence, and because they change strategy): AI Overview, Featured Snippet, People Also Ask, Knowledge Panel, Image Pack, Video Pack, News Pack, Shopping Pack, Local Pack, Site Links. Harvest for free while you're there: People Also Ask questions (long-tail content ideas) and related searches (keyword expansion). Feature detection is worth a deeper pass only on the ~5 highest-priority keywords per run — position checks alone don't need it.

## Rank deltas

`delta = previous_position - current_position` (positive = moved up). Classify each keyword:

| Condition | Classification |
|---|---|
| abs(delta) ≥ 5 | Major move |
| abs(delta) 2–4 | Notable shift |
| abs(delta) ≤ 1 | Stable |
| Was null, now ranked | New entry |
| Was ranked, now null | Drop-out |
| Both null | Not ranked |

Summarize: counts in positions 1–3 / 4–10 / 11–20 / unranked vs the prior run; improved / declined / stable totals; average movement. First-run convention: label baseline entries "BASELINE", never "NEW" — "NEW" is reserved for keywords entering the top 20 in delta mode. For unranked keywords, list the top 3 domains holding those positions so the user sees who owns the ground. Maintain a canonical keyword list per domain that new keywords merge into (union, never replace) so future runs auto-load the tracked set.

## Keyword research: seed expansion

Expand the user's topic into 15–25 variations across five strategies:

1. **Core terms** — the exact seeds.
2. **Modifiers** — "best", "how to", "vs", "alternatives", "tools", "guide", "template", "for [audience]".
3. **Long-tail questions** — "how to X", "what is X", "why X", "X for [use case]".
4. **Commercial variants** — "X pricing", "X reviews", "X comparison".
5. **Adjacent concepts** — what the same audience also searches.

Group into 3–5 thematic clusters before searching, then sweep the live results for every seed, collecting top URLs, dominant content types (listicles, tools, comparison pages, videos), and which domains recur across keywords. Extract the top 3–5 ranking pages per priority cluster (word count, heading outline, topic coverage) and map each recurring competitor's site structure — a competitor with deep topical coverage is harder to displace, and that feeds difficulty.

## Difficulty rubric

Score Low / Medium / High / Very High from observable evidence only — every score must trace to results-page data:

| Difficulty | Criteria |
|---|---|
| Low | Niche/small domains in the top 5, thin content (< 1,500 words avg), few features, content-type match |
| Medium | Mixed authority, moderate depth, some features |
| High | Authority domains dominate top 5, deep content (3,000+ words avg), multiple features |
| Very High | Major brands own the top 10, rich features, deep topical coverage, content-type mismatch |

Content-type alignment is the underrated input: if every top result is an interactive tool and the user plans a blog post, difficulty rises regardless of who ranks.

## Intent and AI-surface classification

Classify from what the results page actually shows, not from the keyword's wording:

| Intent | Evidence |
|---|---|
| Informational | How-to guides, blog posts, encyclopedic content dominate |
| Navigational | Brand results; official site owns #1 |
| Commercial | Comparison pages, "best of" lists, review sites |
| Transactional | Product/pricing pages, buy CTAs, shopping results |

Mixed intent is real — note primary and secondary. Also classify which AI surface the keyword triggers, because it changes the content recommendation:

| Surface | Signal | Content strategy |
|---|---|---|
| GEO (AI Overview / assistant answers) | AI Overview present; question or comparison query | Self-contained 134–167-word passages, statistic- and citation-rich |
| AEO (Featured Snippet / PAA) | Snippet or PAA box present | Direct 40–55-word answer blocks; FAQ schema |
| Traditional only | No AI features | Standard SEO: title, meta, depth, links |

## Clustering and opportunity scoring

Group all keywords (seeds + PAA discoveries + long-tails) into 3–7 clusters, each with a pillar keyword, supporting long-tails, and a recommended content approach (pillar page + supporting posts, comparison hub, tool). Then rank:

```
Opportunity = (Relevance x Intent Value) / Difficulty
```

Relevance: High=3 / Medium=2 / Low=1 against the user's stated goal. Intent value: Transactional=4, Commercial=3, Informational=2, Navigational=1. Difficulty: Low=1 → Very High=4.

Bucket into three tiers: **Quick Wins** (low/medium difficulty + high relevance + commercial/transactional intent — fastest path to traffic), **Growth Targets** (medium/high difficulty + high intent value — worth quality content), **Moonshots** (very high difficulty, exceptional intent value — long-term plays).

## Report shapes

**Keyword research:** TL;DR (opportunity count, cluster count, top opportunity, dominant content type) → Quick Wins and Growth Targets tables (keyword, intent, difficulty, content type, top competitor, source URL) → topic clusters with per-cluster content strategy → results-page landscape (features observed, dominant domains, PAA questions found) → competitor strength table → "What this means" in 2–4 strategic sentences.

**Rank check:** TL;DR → position summary table with change-vs-last column → biggest movers (gains, drops, new entries, drop-outs) → top competitors per unranked keyword → full rankings table (keyword, position, delta, URL, features) → feature-presence table with deltas → interpretation: are features squeezing organic clicks, which clusters are strongest, which dropped pages need an audit.
