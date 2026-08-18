# Vertical presets

Each preset defines the trigger keywords that select it, the discovery sources in priority order, the enrichment targets, and the query pattern. Match the user's business type against trigger keywords; a clear match loads the preset, a partial match gets confirmed with the user, no match falls through to Custom.

Source tiers matter: run primary and secondary for every metro; add the tertiary source only when primary + secondary return fewer than ~10 combined unique results for that metro. When a structured source is unavailable, substitute a plain web search for the same query — don't skip the metro.

---

## Healthcare

**Trigger keywords:** doctor, dentist, dermatologist, ophthalmologist, optometrist, chiropractor, therapist, psychiatrist, pediatrician, clinic, medical, healthcare, hospital, pharmacy, urgent care, physical therapy, orthodontist, surgeon, physician, practice, practitioner

**Discovery sources:**

| Source | Tier | Purpose |
|--------|------|---------|
| Map/local listings (e.g. Google Maps) | Primary | Geo-targeted discovery — best coverage of physical practices |
| Review directories (e.g. Yelp) | Secondary | Catches practices missing from map listings |
| Accreditation registries (e.g. BBB) | Tertiary | Credibility and complaint data |

**Enrichment:** review volume and sentiment from map listings; accreditation status and complaint history from registry profiles.

**Query pattern:** `"{specialty} {type}" in {metro}` — e.g. `ophthalmologist in Miami FL`, `dentist in Tampa FL`.

**Geo-tiling:** yes — tile by metro areas within the target state/region.

**Disambiguation note:** "practice" alone is ambiguous (medical / dental / legal) — ask before assuming.

---

## SaaS / Software

**Trigger keywords:** SaaS, software, app, platform, tool, cloud, B2B, startup, project management, CRM, ERP, analytics, automation, API, fintech, martech, edtech, healthtech, devtools, developer tools, productivity software

**Discovery:** no map sources. Two search passes, run in parallel:

**Pass 1 — product discovery** (find the players):
- `{vertical}` restricted to major software review directories (e.g. `site:g2.com`, `site:capterra.com`)
- `best {vertical} software {current year}` — roundups and comparison articles
- `{vertical}` on launch platforms (e.g. `site:producthunt.com`)
- `{vertical} open source github` — the open-source contingent

**Pass 2 — financial & traction discovery** (funding, market context):
- `{vertical}` restricted to funding databases (e.g. `site:crunchbase.com`)
- `{vertical} startup funding raised` — news-focused search
- `{vertical} market landscape players` — analyst and landscape pieces

Pass 2 is critical: without it, funding and traction data will be missing or wrong, and the tier grouping in the report collapses.

**Enrichment:** structured product data, ratings, and pricing tier from software directories; funding rounds, valuation, and team size from funding databases.

**Geo-tiling:** no — software markets are not geography-bound. If the user names a region, interpret it as "headquartered in" and add it as a search qualifier, not a tiling plan.

**Dedup key:** root domain (there is no place identifier).

**Verification:** every funding figure needs its own source check before it appears in output — search `"{company} funding raised series"`, use only sourced amounts and dates, otherwise report "Undisclosed".

---

## Restaurants / Food

**Trigger keywords:** restaurant, cafe, coffee, bakery, bar, pub, brewery, pizza, sushi, taco, brunch, diner, bistro, food, catering, food truck, ice cream, juice, steakhouse, seafood, burger, ramen, pho, thai, italian, mexican, chinese, indian, mediterranean, vegan, vegetarian

**Discovery sources:**

| Source | Tier | Purpose |
|--------|------|---------|
| Map/local listings | Primary | Geo-targeted discovery |
| Review directories | Secondary | Especially strong for food and drink |

**Enrichment:** review volume and rating from map listings.

**Query pattern:** `"{cuisine} restaurant" in {metro}`.

**Geo-tiling:** yes — metros, or neighborhoods for dense large-city runs.

---

## Legal / Financial

**Trigger keywords:** lawyer, attorney, law firm, legal, accountant, accounting, CPA, financial advisor, wealth management, insurance, tax, bankruptcy, immigration, personal injury, real estate attorney, family law, criminal defense, corporate law, patent, IP, intellectual property

**Discovery sources:**

| Source | Tier | Purpose |
|--------|------|---------|
| Map/local listings | Primary | Geo-targeted discovery |
| Accreditation registries | Secondary | Accreditation and complaint history |

**Enrichment:** accreditation status, years in business, complaint history from registry profiles.

**Query pattern:** `"{practice area} {type}" in {metro}` — e.g. `immigration attorney in Austin TX`.

**Geo-tiling:** yes — metros within the target state/region.

---

## Auto / Home Services

**Trigger keywords:** mechanic, auto repair, body shop, car wash, oil change, tire, plumber, plumbing, electrician, HVAC, roofing, landscaping, pest control, cleaning, maid service, handyman, locksmith, moving, storage, painting, flooring, contractor, renovation, remodeling, garage door, appliance repair

**Discovery sources:**

| Source | Tier | Purpose |
|--------|------|---------|
| Map/local listings | Primary | Geo-targeted discovery |
| Review directories | Secondary | Strong for home services |
| Accreditation registries | Tertiary | Complaint history — matters more in this vertical than most |

**Enrichment:** review volume and sentiment; complaint history and years in business from registry profiles.

**Query pattern:** `"{service}" in {metro}`.

**Geo-tiling:** yes — by metro.

---

## Custom (fallback)

Used when no other preset matches.

**Discovery sources:** map/local listings (primary), review directories (secondary).

**Enrichment:** review volume and rating.

**Query pattern:** the user's own keywords per metro.

**Geo-tiling:** yes, unless the query is clearly non-geographic — in which case borrow the SaaS shape: two search passes, dedup by domain, no tiling.
