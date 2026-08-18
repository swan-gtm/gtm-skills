# Audit mode

Compares a user's existing business list against fresh discovery results, surfacing gaps in both directions. Read this when a reference list is in play.

---

## When audit mode triggers

| Signal | Example |
|--------|---------|
| Spreadsheet link in the request | a shared Google Sheet or similar |
| CSV file path | `my-practices.csv`, a downloads-folder file |
| Inline list (3+ businesses) | pasted names/addresses, one per line |
| Explicit audit language | "audit my list", "compare against", "what am I missing" |

A list without stated intent gets one question: "Want me to audit it against fresh discovery, or just use it as a starting point?" Audit language without a list gets a request for the list — never proceed on an imagined reference.

---

## Reference list parsing

Detect the format, extract the rows, then normalize every record to a uniform shape.

**Spreadsheet:** extract the sheet as a table. Map columns by header name, case-insensitive:

| Target field | Accepted column headers |
|--------------|------------------------|
| `name` | name, business name, practice name, company, organization |
| `domain` | domain, website, url, web, site |
| `city` | city, location, metro, area |
| `state` | state, st, region |
| `phone` | phone, telephone, tel, phone number |
| `address` | address, street, full address |

**CSV:** read the file, same column mapping.

**Inline list:** parse each line — business name is the first segment before any delimiter; pull city/state, domain, or phone if present. If the format is unclear, ask once: "What columns does your list have? (e.g. name, city, phone)"

**Normalized record:**

```json
{
  "name": "Acme Dental",
  "domain": "acmedental.com",
  "city": "Miami",
  "state": "FL",
  "phone": "3051234567",
  "raw": "original row as-is, for traceability"
}
```

- **Domain:** strip protocol, `www.`, trailing `/`, and path segments
- **Phone:** strip all non-digits; keep the last 10 digits (US) or the full international number
- **Name:** trim whitespace; preserve original casing for display
- **Missing fields:** set to `null` — matching layers skip null fields

**Failure handling:** if extraction returns garbage or the CSV is malformed, ask the user to paste the data inline. If the parsed list has zero valid records, warn and offer to switch to plain discovery.

---

## Matching algorithm

Three layers, in order. Once an entity matches at any layer, stop — don't re-match at lower layers. Track which layer produced each match; it's reported per row.

### Layer 1 — domain match (primary)

Compare normalized root domains.

```
reference: acmedental.com  ↔  discovered: acmedental.com   →  MATCH
reference: acmedental.com  ↔  discovered: acme-dental.com  →  NO MATCH
```

Root domain only (not subdomains). Exact match required — no fuzzy domain matching, ever: near-miss domains are usually different businesses. Skip pairs where either side has `domain: null`.

### Layer 2 — name + city fuzzy match (secondary)

For entities unmatched after Layer 1, compare names within the same city.

Normalization: lowercase both names; remove punctuation (`.,'-&!()[]`); remove common suffixes (`inc`, `llc`, `ltd`, `corp`, `co`, `pllc`, `pa`, `pc`, `dds`, `md`, `dmd`, `do`, `group`, `associates`, `and associates`); split into word tokens.

Matching: both entities must share the same city (case-insensitive, trimmed). Word overlap = `shared_words / max(words_a, words_b)`. **Threshold: 80% overlap = match.**

```
"Acme Dental Associates" in Miami  ↔  "Acme Dental" in Miami
  → tokens [acme, dental] vs [acme, dental]  → 100%  → MATCH

"Acme Dental" in Miami  ↔  "Acme Health" in Miami
  → tokens [acme, dental] vs [acme, health]  → 50%   → NO MATCH
```

Skip pairs where either side has `city: null`.

### Layer 3 — phone match (tertiary)

For still-unmatched entities, compare normalized phones (non-digits stripped, last 10 digits).

```
reference: (305) 123-4567  →  3051234567
discovered: 305-123-4567   →  3051234567  →  MATCH
```

Skip pairs where either side has `phone: null`.

---

## Categorization

| Category | Definition | Business meaning |
|----------|-----------|------------------|
| `matched` | In both reference list AND discovery | Validated — the list is accurate here |
| `discovered_only` | Found by discovery, NOT in reference list | Expansion candidates — gaps in the user's list |
| `reference_only` | In reference list, NOT found by discovery | Coverage gaps — may have closed, moved, rebranded, or be missed by sources |

**Coverage score:** `matched / reference_count × 100`. Zero matches across all three layers is a valid result — report the 0% honestly; it usually means the list and the discovery scope describe different markets, which is itself the finding.

---

## Output template

```markdown
# Market Audit: [Business Type] in [Geography]
*Audited [R] reference entries against [D] discovered businesses | [Date]*

## TL;DR
[M/R × 100]% coverage — [M] of [R] reference entries verified, [DO] new
businesses discovered, [RO] in your list but not found by discovery.

## Summary
- **Reference list:** [R] entries
- **Discovered:** [D] businesses
- **Matched:** [M] ([M/R]% of reference list verified)
- **Discovered only:** [DO] expansion candidates
- **Reference only:** [RO] coverage gaps

## Matched ([M])
| # | Name | Location | Match Layer | Discovery Strength | Sources |
|---|------|----------|-------------|--------------------|---------|

## Discovered Only ([DO]) — Expansion Candidates
| # | Name | Location | Domain | Rating | Strength | Sources |
|---|------|----------|--------|--------|----------|---------|

## Reference Only ([RO]) — Coverage Gaps
| # | Name | Location | Domain | Phone | Possible Reason |
|---|------|----------|--------|-------|-----------------|

## What This Means
[1–3 sentences of interpretation — the coverage percentage in plain terms,
geographic clusters in discovered_only, notable reference_only entries.]
```

Save the report plus a structured data file (all three categories, with match layer per entity) under the market slug in your workspace — the structured file is what downstream exports and follow-up investigations read.

---

## Follow-ups to offer

- **Export discovered-only for outreach** — a CSV of expansion candidates. Confirm before generating anything intended for bulk outreach.
- **Investigate reference-only gaps** — targeted searches per entity to determine closed vs. moved vs. rebranded vs. simply unlisted.
- **Re-run against a different geography** — same list, broader or narrower area.
