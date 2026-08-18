# Per-competitor research protocol

Run this protocol once per competitor, in parallel threads when researching several. Each thread gets: the competitor's name, its domain, and its previous positioning snapshot (or "first run — no comparison available"). Budget roughly a dozen research calls per competitor — favor extraction quality over quantity.

## Phase 0 — Site discovery (always first)

Map the site's actual structure (sitemap fetch or shallow crawl, up to ~200 URLs) before extracting anything. Guessed paths 404; discovered paths don't.

From the URL list, identify:

- **Homepage** — always extract.
- **Features/product page** — paths containing `/features`, `/product`, `/platform`, `/solutions`, `/why-us`, `/capabilities`. Pick the single most relevant.
- **Pricing page** — `/pricing`, `/plans`, `/get-started`.
- **Blog index** — `/blog`, `/resources`, `/content`, `/insights`.
- **Case studies** — `/case-study`, `/customers`, `/stories`.

Record which pages exist and which don't. Absences are positioning signals in their own right: no public pricing page suggests enterprise/sales-led motion; no blog suggests the company isn't competing on content. Note notable subdomains too (`docs.`, `api.`, `community.`) — a docs subdomain signals a developer audience regardless of what the homepage claims.

If the site blocks sitemap/crawl access, fall back to extracting the homepage directly and trying the common paths above by hand.

## Phase 1 — Page extraction (run simultaneously)

Extract each discovered page as clean text/markdown:

1. **Homepage** → hero copy, tagline, primary CTA, value propositions, top-level nav structure.
2. **Features page** → feature categories, branded feature names, emphasis, explicit differentiation claims ("unlike X", "the only platform that…"). Skip if none found.
3. **Pricing page** → tier names, pricing model, entry price, feature gating, target audience per tier. Skip if none found.

If an extraction returns garbage, retry once; if still empty, record "page not accessible" and continue.

## Phase 2 — Blog and content (run simultaneously)

Three searches:

1. Search within the competitor's domain for its blog index and recent posts (~10 results).
2. Search the live web for the competitor's name plus blog/content/resources terms, windowed to the period since the last run (~10 results). Verify actual publish dates from the extracted content — search-result dates lie.
3. Search within the competitor's domain for case studies, customer stories, and testimonials (~5 results).

Some companies don't blog. Record "no active blog detected" and lean on page-based positioning instead — don't invent content themes from nothing.

## Phase 3 — Deep extraction (if posts found)

Extract the 2–3 most recent blog posts in full for theme analysis: what story does this company tell repeatedly, who is it aimed at, do they name competitors or position against a category, what keywords do titles and headings chase.

## Output — return exactly these sections

**SITE STRUCTURE**
- Pages found / pages missing (with the implication of each absence)
- Subdomains
- Structure signals — what the architecture reveals about positioning

**HOMEPAGE POSITIONING**
- Tagline (exact text) · Hero message · Primary CTA (button text + implied action)
- Value props, each verbatim
- Navigation structure (top-level items — what they choose to emphasize)
- Target audience signals (who the copy speaks to)

**FEATURES PAGE**
- Page URL · Key feature categories · Differentiation claims · Branded feature names
- Missing/notable — conspicuously absent or prominently highlighted capabilities
- (No features page → write "No public features page — [implication]")

**PRICING PAGE**
- Page URL · Model (per-seat / usage / flat / freemium / custom) · Tier names
- Entry price if visible · Enterprise signal ("contact sales", custom tier) · Feature gating
- (No pricing page → write "No public pricing — likely enterprise/sales-led")

**BLOG & CONTENT**
- Last 5–10 posts with titles and dates · Primary recurring themes
- Content types (blog, case study, whitepaper, webinar) · Publishing cadence estimate
- Audience focus (developer / executive / practitioner)

**SOCIAL PROOF**
- Customer logos/names if public · Testimonial themes (what customers praise)
- Case study focus (industries, use cases, outcomes highlighted)

**CHANGES FROM PREVIOUS SNAPSHOT**
- Specific diffs only: "Tagline changed from '[old]' to '[new]'", "New feature category added: [name]", "Pricing model shifted from [old] to [new]", "New blog theme emerging: [topic]", "Page added/removed: [url] — [significance]"
- First run → "First run — no comparison available"
