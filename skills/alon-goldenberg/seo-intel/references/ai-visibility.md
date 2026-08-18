# AI visibility audit

How to measure whether AI assistants mention and cite a brand, score it against competitors, and fix the gaps. Covers query design, detection rules, scoring, per-platform ranking factors, and the GEO optimization playbook.

## Query set

Test 20–40 queries. Sources, in order of preference: the user's own list; the brand's known industry keywords plus recent keyword-research output; or auto-discovery ("best {category}", "{category} comparison", "{category} reviews", "{brand} {category}") confirmed with the user. Phrase each query as a natural question a buyer would ask an assistant — "What is the best web scraping API?", not the keyword string "web scraping api". Keyword-style phrasing only belongs on search-box surfaces (Google AI Mode / AI Overviews).

## Platforms

Query every AI answer surface you can reach — typically some subset of ChatGPT, Perplexity, Google AI Overviews / AI Mode, Gemini, and Grok — capturing for each query the full answer text and the cited-source list with URLs. Also run a plain Google search per query to record whether it triggers an AI Overview (a distinct surface from AI Mode). Platform rules:

- A platform that errors gets one retry, then is excluded **for that query** with the gap noted. Never fabricate an answer for an unreachable platform, and never abort the run over one platform.
- A query with no AI answer is data, not an error — record "no AI answer present"; those queries are early positioning opportunities.
- Compute all scores only from platforms that actually returned data, and say which were missing.

## Detection rules (per query x platform)

Extract: brand mention (in the answer text), domain citation (in the source list), position of first mention / ordinal position among sources, sentiment of the mention sentence (positive / neutral / negative / unknown — judge only the sentence containing the mention, default to unknown), competitor mentions, competitor domain citations, and a 1–2 sentence excerpt as evidence.

- **Brand mention:** case-insensitive match on the brand name and common variants.
- **False-positive guard for common-word brands** (e.g. a brand named "Nimble", "Notion", "Craft"): count a mention only if (a) the name appears within 5 words of a domain-relevant term, or (b) the brand's domain is also cited in the sources. A bare occurrence of the common word is generic usage — record `brand_mention: false` with a note.
- **Domain citation:** normalize cited URLs to root domain (strip protocol, `www.`, path) before comparing against brand and competitor domains.
- Citations placed earlier in the answer are stronger signals than late ones — record position when the platform exposes it.

## Scoring

- **Visibility score** = % of queries where the brand has at least one mention or citation on any platform.
- **Share of AI voice** = brand signals (mentions + citations) / all signals including competitors' x 100. If nobody — brand or competitor — appears anywhere, set it to 0 and report "the space may not yet trigger AI answers"; never divide by zero.
- **Citation rate** = domain citations / brand mentions. High mentions with low citations means the brand is discussed but not linked — a specific, fixable optimization target.
- **Per-platform breakdown:** queries with an AI answer, mention count, citation count, coverage rate.
- **Competitor gap list:** queries where a competitor appears and the brand doesn't — the highest-priority targets, each with the platform and the competitor's citation as evidence.

## Delta tracking

Keep a per-brand snapshot of every run (per query, per platform: answer present, mention, citation, sources). On re-runs, lead with: citations gained, citations lost, competitor movements, queries newly triggering (or losing) AI Overviews, and score deltas. First run = full baseline, no delta section.

## Per-platform ranking factors

Directional profiles from published research (Princeton GEO study, arXiv:2311.09735; SE Ranking's 400K-page study; ZipTie) — treat as priors to test, not gospel:

- **ChatGPT:** content-answer fit dominates (~55% of citation likelihood); domain authority matters far less (~12%) than in classic SEO; fresh content is heavily favored; lists, tables, and "X is..." definitional openings get cited over prose.
- **Perplexity:** FAQ schema is disproportionately rewarded; public PDFs get priority; publishing velocity beats keyword targeting; it prefers citing content that itself cites sources; sources appearing in the answer's first paragraph carry the most visibility value.
- **Google AI Overviews / AI Mode:** E-E-A-T signals dominate; passage-level optimization beats page-level (the AI extracts passages); featured-snippet winners are ~2x more likely to be cited; pages ranking organically in the top 5 supply ~80% of AI Overview citations — traditional rank is still the entry ticket.
- **Gemini:** mirrors Google AI patterns and the knowledge graph; structured-data work pays on both at once.
- **Grok:** real-time and social signals weigh heaviest; strongest recency bias of any platform; least studied — directional only.
- **Claude (not directly queryable):** extremely selective; factual density with specific numbers is the strongest signal; uses Brave Search for grounding, so estimate visibility via Brave rankings and confirm its crawler isn't blocked.

## GEO optimization playbook

Nine methods ranked by measured visibility boost (Princeton GEO study):

| Method | Boost |
|---|---|
| Cite authoritative sources | +40% |
| Add statistics / specific numbers | +37% |
| Add attributed expert quotes | +30% |
| Authoritative tone (no hedging) | +25% |
| Easy-to-understand language | +20% |
| Appropriate technical terms | +18% |
| Vocabulary diversity | +15% |
| Fluency / readability | +15–30% |
| Keyword stuffing | **−10% — actively hurts** |

Best combinations: fluency + statistics (highest overall); citations + authoritative tone (B2B); easy language + statistics (consumer). Apply the 3–4 most relevant methods per page, not all nine.

**Content block sizing** — different surfaces extract at different granularities, and each block must stand alone without surrounding context:

- AI-answer citations (GEO): 134–167-word self-contained passages
- Featured snippets / PAA (AEO): 40–55-word direct answers
- Voice: under 30 words, one clear sentence

**Optimizing an existing page:** identify its target query → check which platforms currently cite it → score it against the nine methods → add the top-three methods first (citations, statistics, quotes) → restructure into surface-sized blocks → re-query after changes to measure movement.

## AI crawler access — check first

If AI bots can't crawl the site, no content optimization matters. Fetch `robots.txt` and check for: `GPTBot`, `ChatGPT-User`, `ClaudeBot` / `anthropic-ai`, `PerplexityBot`, `GoogleOther`, `Googlebot`. Report which are allowed vs blocked; recommend allowing all unless there is a documented reason. Also check for `/llms.txt` at the site root (llmstxt.org) — low priority, forward-looking.

## Report shape

TL;DR (visibility %, share of voice vs top competitor, delta line, top findings) → per-platform breakdown with top queries where the brand appears → query-level matrix (query x platform: cited / mentioned / absent) → competitor comparison table (visibility, share of voice, citation rate per brand) → optimization opportunities in three buckets: **high priority** (competitor visible, brand absent — with the specific competitor citation), **quick wins** (mentioned but not cited — earn the link), **coverage gaps** (no AI answer triggered yet — early positioning) → a GEO recommendation per high-priority gap naming the methods to apply → strategic interpretation.
