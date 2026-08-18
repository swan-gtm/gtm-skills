# Content gaps and competitor pages

Rules for the two competitor-facing plays: content gap analysis (what they cover that you don't, validated against live rankings) and on-page reverse-engineering (their SEO playbook read out of their pages).

## Content gap analysis

### Scope and crawl

Compare the user's domain against 1–3 competitors. If the user can't name competitors, discover them: search "[Company] competitors", "[Company] vs", "[Company] alternatives" in parallel, propose a shortlist, confirm. Agree crawl depth up front (~50 pages per domain for a quick pass, ~200 standard, ~500 deep) and whether to scope to a section (`/blog`, `/resources`). Map all domains in parallel from their sitemaps and link graphs; if mapping fails for a domain, fall back to a `site:{domain}` search and build the page list from those results. Always keep the homepage even when scoped to a path.

### Per-page extraction

For every page: URL, title, meta description, H1, H2 outline, primary topic (one noun phrase), secondary topics, inferred target keywords (from title + H1 + first paragraph), word count, content type (blog post / product / landing / docs / resource / pricing / about / other), and publish date if visible.

### Topic modeling and the coverage matrix

1. Extract noun phrases from each page's H1, H2 outline, and primary topic.
2. Normalize: lowercase, strip punctuation, stem ("Content Marketing Strategies" → "content marketing strategy").
3. Cluster pages sharing a normalized primary topic or 2+ overlapping secondary topics; label each cluster with its most common noun phrase.
4. Build the matrix — rows are topic clusters, columns are domains, cells hold page count, average word count, and whether a hub page exists (a landing/resource page with 3+ internal links to other pages in the cluster).

### What counts as a gap

- **Missing:** any competitor has ≥ 1 page on the topic and the user has 0.
- **Thin:** the user's average word count on the topic is under 30% of the best competitor's.

Record per gap: type, which competitors cover it, their page count and best average word count, whether they have a hub, the single best representative competitor URL, and the user's own coverage numbers.

### SERP validation — the honesty step

A competitor page that doesn't rank is a weak reason to write anything. Derive 2–3 representative queries per gap from the topic's H1s and keywords, then validate in two passes to control cost:

- **Pass 1 (all gaps):** a light sweep to check whether the competitor's domain appears in organic results.
- **Pass 2 (confirmed gaps only):** a deeper pass capturing AI Overview presence, Featured Snippets, and People Also Ask questions.

| Competitor rank | Classification |
|---|---|
| Top 10 | CONFIRMED — high-value gap |
| 11–20 | MODERATE — they rank, not dominantly |
| Not in top 20 | LOW PRIORITY — they publish but don't rank |
| Query returned too little data | UNVALIDATED — say so in the report |

If validation covered under 50% of gaps, state it in the TL;DR ("validated N of M gaps — unvalidated gaps scored conservatively") so the tiers aren't misleading.

### Gap scoring

```
score = (competitor_rank_strength x topic_relevance) / estimated_effort
```

Rank strength: CONFIRMED=3, MODERATE=2, LOW_PRIORITY=1, UNVALIDATED=1. Relevance: alignment with the user's themes and goals, High=3 / Medium=2 / Low=1. Effort: from the competitor's average word count (< 1,500 words = 1; 1,500–3,000 = 2; 3,000+ = 3), +1 if they have a hub page the user would need to match.

Tiers: **Quick Wins** (low effort + CONFIRMED/MODERATE), **Strategic Bets** (high effort + CONFIRMED), **Nice-to-Have** (the rest). Sort by score within tiers.

### Delta mode and report

On re-runs, diff against the prior gap snapshot: **NEW** gaps lead the summary, **CLOSED** gaps are called out as wins, UNCHANGED gaps stay in the body. Report shape: TL;DR (gap count, quick-win count, biggest gap, SERP-confirmed count, delta line) → tier tables (gap topic, type, competitor coverage, their best rank, features on that results page, suggested content angle) → full coverage matrix → results-page landscape with PAA questions found → "What this means" with 30/60/90-day priorities. Every gap row carries the verified competitor URL.

## Competitor on-page reverse-engineering

Crawl each competitor domain at the agreed depth, classify pages into sections by path (`/product`, `/pricing`, `/blog`, `/docs`, `/customers`, `/about`), and extract per page: title, H1, meta description, H2 outline (max 10), H3–H6 outline (max 20), body-only internal anchor texts (max 50), image alt texts (max 30), word count, publish date if visible.

**Body-only anchors — the rule that keeps hub detection honest:** collect internal anchors only between the H1 and the first footer marker ("Related Posts", "Subscribe", "Newsletter", a second horizontal rule). Nav, header, and footer links are boilerplate that poisons hub-and-spoke analysis.

### Theme clustering

Collect all titles, H1s, and H2s; normalize; and **filter boilerplate H2s before clustering** — drop generic section headers that appear across unrelated posts: conclusion, summary, introduction, overview, table of contents, FAQ(s), related posts/articles, what's next, next steps, about the author, references, sources, further reading, TL;DR, get started, try it free, contact us, share this post. Then group pages sharing 2+ overlapping content words in title + H1 + filtered H2s, aiming for 5–15 labeled themes per domain, each with its 3–5 most-repeated keyword phrases.

### Hub detection (three steps, in order)

1. Body-only anchor extraction (above).
2. Strip navigation boilerplate: any anchor text appearing on more than 80% of pages ("Features", "Pricing", "Blog") is chrome, not strategy.
3. A page is a hub if its URL appears in the body anchors of 3+ other pages in the same theme, using **exact URL equality** after normalization (strip trailing slash, fragments, tracking params). Never substring-match — `/blog` "matching" every `/blog/*` page is the classic false positive.

### Pattern extraction — seven element categories

- **Titles:** top 20 keywords, length distribution, truncation rate (% over 60 chars), dominant formula (`X | Brand`, `X: Y`, `How to X`, `N Best X`, question titles).
- **H1s:** H1-title alignment rate, dominant tone (benefit / feature / question / how-to / listicle), top keywords.
- **Meta descriptions:** coverage rate, average length, CTA formulas ("Learn more", "Get started", "Try free"), keyword inclusion rate.
- **Blog topics:** theme map scoped to the blog, posting velocity (posts/month from publish dates or dated URL paths), content-type mix (how-to / listicle / comparison / case study / thought leadership).
- **Heading hierarchy:** average H2s per page, H3s per H2, common H2 patterns per content type.
- **Anchor text:** keyword-rich vs generic ratio ("click here"), top 10 most-linked-to pages, detected hub/spoke structures.
- **Image alt text:** coverage rate, top keyword signals, stuffing flags (alt over 125 chars or 5+ comma-separated keywords).

When 2+ domains (or the user's own site) are analyzed, build a comparison matrix across these dimensions and highlight where the user lags and which themes only one competitor targets.

### Delta signals on re-runs

Surface only meaningful changes, with before/after numbers: a **new theme emerging** (3+ new pages under a previously absent theme), a **theme abandoned** (5+ pages, no additions since last snapshot), a **title-pattern shift** (dominant formula changed across 10+ pages), an **anchor-strategy shift** (keyword-rich ratio moved > 10 points), **blog velocity** changing by > 30%, a **new site section** with 5+ pages. If nothing meaningful changed, say exactly that. Fewer than ~10 pages extracted for a domain → skip theme clustering and report raw element analysis only, noting the limited sample.
