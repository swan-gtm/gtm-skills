# Site audit checks

The complete rule set for the site audit play: what to extract, the seven check categories with severities, confidence tiers, escalation rules, dedup, and the health grade.

## Scope and sampling

Ask two things up front: how thorough (Quick ~50 pages / Standard ~200 / Deep ~500) and whether the site is a JS-heavy single-page app (determines whether to start with rendered extraction). Discover URLs via the sitemap plus a crawl of the link graph — discovering from both is what surfaces orphan pages.

When the site has more URLs than the scan size, sample representatively:

- **Always include:** the homepage, `/robots.txt`, `/sitemap.xml`
- **Depth 1:** every page one click from the homepage
- **Depth 2:** a proportional cross-section per site section (`/blog/`, `/products/`, `/docs/`…)
- **Paginated:** at least one page-2/page-3 URL per section
- **Orphans:** a few URLs present in the sitemap but absent from the link graph

## Per-page extraction

Capture for every sampled page: `title`, `meta_description`, `canonical` (and whether it is self-referential), `og_title`, `og_description`, `twitter_card`, all `h1` values, the H2–H6 outline, JSON-LD `@type` values, internal and external link counts, count of images missing alt text, body word count, content-to-HTML ratio, hreflang presence, `<html lang>` value, and the HTTP status code.

**Render escalation:** start with plain extraction for static sites. If a page (or, after the first batch, more than 30% of pages) returns an empty or near-empty head, re-extract with JS rendering; if that still fails, use your heaviest rendering option. Only after the heaviest tier fails do you record a page as "extraction failed" — and failed pages are excluded from checks, never guessed at.

## The seven categories

### 1. Meta tags

| Rule | Condition | Severity |
|---|---|---|
| Missing title | title null/empty | Critical |
| Duplicate title | same title on 2+ pages | High |
| Title too short / too long | < 30 chars / > 60 chars | Medium |
| Missing meta description | null/empty | Medium |
| Duplicate meta description | same on 3+ pages | High |
| Description too short / too long | < 70 chars / > 160 chars | Low |
| Missing canonical | null/empty | Medium |
| Non-self-referential canonical | canonical points elsewhere | Medium |
| Missing OG tags / Twitter card | og_title or og_description null / twitter_card null | Low |

Fixes: unique title per page, primary keyword near the start, 30–60 chars; unique 70–160-char descriptions (shared descriptions signal thin content); self-referential canonicals to prevent duplicate-content issues.

### 2. Heading structure

| Rule | Condition | Severity |
|---|---|---|
| Missing H1 | no H1 | Critical |
| Multiple H1s | 2+ H1s | High |
| Hierarchy gap | H3 without preceding H2, etc. | Medium |
| Empty heading | whitespace-only heading | Low |
| Duplicate H1 | same H1 on 2+ pages (excluding homepage) | Medium |

### 3. Schema markup (JSON-LD)

| Rule | Condition | Severity |
|---|---|---|
| No JSON-LD on a content page | none present and word count > 300 | High |
| Missing required fields | Article without headline+datePublished; Product without name+offers; Organization without name+url | Medium |
| Deprecated @type | outdated schema.org types | Low |
| No Organization/WebSite schema on homepage | absent | Medium |

### 4. Internal links

| Rule | Condition | Severity |
|---|---|---|
| Orphan page | in sitemap, 0 inlinks from crawled pages | Critical |
| Broken internal link | linked URL returns 4xx/5xx | High |
| Redirect chain | resolves through 3+ redirects | High |
| Excessive links | > 100 internal links on one page | Medium |
| Deep page | > 4 clicks from homepage | Medium |
| No internal links | 0 internal links on a content page | High |

Fixes: link orphans from relevant hub pages; point links at final destinations; keep important pages within 3 clicks.

### 5. Content quality

| Rule | Condition | Severity |
|---|---|---|
| Thin content | < 300 words on an indexable page | High |
| Very thin content | < 100 words on an indexable page | Critical |
| Duplicate content | 4-gram shingle Jaccard similarity > 0.9 between two pages | High |
| Images missing alt text | any on a content page | Medium |
| Low content-to-HTML ratio | < 0.10 | Low |

Duplicate detection: compute 4-gram shingle sets from body text per page pair; above 100 pages, compare within site sections only to stay tractable.

### 6. Technical foundations

| Rule | Condition | Severity |
|---|---|---|
| robots.txt missing | 404 or empty | Critical |
| robots.txt blocks important paths | blanket `Disallow: /` or high-value paths blocked | Critical |
| Sitemap missing | none at `/sitemap.xml` or in robots.txt | Critical |
| Sitemap stale | all `<lastmod>` older than 90 days | Medium |
| HTTPS not enforced | HTTP doesn't 301 to HTTPS | Critical |
| Mixed content | HTTPS page loads HTTP resources | High |
| URL hygiene | underscores, uppercase, or session IDs (`?sid=`…) in paths | Medium |
| Missing lang attribute | no `<html lang>` | Low |
| AI bots blocked | robots.txt disallows GPTBot, ClaudeBot, PerplexityBot, or ChatGPT-User | Medium |
| No llms.txt | no `/llms.txt` at root | Low |

The last two connect the audit to AI visibility: each blocked AI crawler is a visibility channel closed. Recommend allowing AI bots unless there is a documented reason not to; `/llms.txt` (see llmstxt.org) is low priority but forward-looking.

### 7. Core Web Vitals (observational)

These are inferred from HTML patterns, not measured with a performance lab — always Hypothesis-confidence:

| Rule | Condition | Severity |
|---|---|---|
| Large images without lazy loading | likely-heavy images with no `loading="lazy"` | Medium |
| Render-blocking resources | stylesheets/scripts in `<head>` without async/defer | Medium |
| Excessive DOM depth | nesting beyond ~32 levels | Low |
| No viewport meta tag | missing | Medium |

## Confidence tiers

Tag every finding with how it was detected, and show the tag in the report (`[C] Missing title tag on /about`):

| Tier | Meaning |
|---|---|
| `[C]` Confirmed | Deterministically measured (parsed from the actual HTML head, fetched robots.txt) |
| `[L]` Likely | Strong signal from content analysis (link counts from extracted text are approximate — nav boilerplate inflates them) |
| `[H]` Hypothesis | Inferred, needs manual verification (all CWV checks; HTTPS enforcement inferred from URLs) |

Meta tags, headings, and schema parsed from raw HTML are Confirmed. Internal-link counts from extracted text are Likely. CWV is always Hypothesis.

## Severity escalation

- **Widespread duplication:** the same rule firing on > 10% of audited pages bumps its severity one level (Low→Medium, Medium→High, High→Critical).
- **No homepage bonus:** homepage findings keep their base severity — the rule severity already encodes impact.
- **Combined impact:** a page with 3+ distinct Critical/High findings is flagged as a "high-priority fix page" in Quick Wins.

## Dedup against the prior audit

When a prior findings file exists for the domain, signature each finding as `page_url|rule_id` and classify: **Unchanged** (same signature, same severity), **Worsened** (same signature, higher severity), **New** (no prior match), **Resolved** (prior signature gone). New and Worsened go in the summary and severity tables; Unchanged only in category breakdowns; Resolved counted as wins in the summary ("3 issues resolved since last audit").

## Health grade

| Grade | Criteria |
|---|---|
| A | 0 Critical, ≤ 2 High |
| B | 0 Critical, 3–5 High |
| C | 1–2 Critical, or 6–10 High |
| D | 3–5 Critical, or > 10 High |
| F | > 5 Critical |

## Report shape

Header (domain, date, pages audited / discovered, render tier used) → TL;DR (grade, top 3 critical issues, biggest quick win, delta line if a prior audit exists) → severity tables (Critical / High / Medium / Low; columns: page, issue, category, recommendation) → per-category breakdown with pass rates → site structure overview → Quick Wins (each under ~2 hours of work) → "What this means" (where to start, expected impact). Every finding row names its page URL and confidence tier.
