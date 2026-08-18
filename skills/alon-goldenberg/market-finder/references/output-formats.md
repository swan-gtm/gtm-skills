# Output formats

Three output shapes: discovery (geographic verticals), the SaaS variant, and — for audit mode — the template in the audit reference. Every entity row in every format carries at least one clickable source URL (map listing, review page, website, registry profile, software-directory page, or code repository). An entity without a verifiable source doesn't ship.

---

## Discovery output (geographic verticals)

```markdown
# Market Finder: [Business Type] in [Geography]
*Found [N] businesses | [Date] | Strength: [H] High, [M] Medium, [L] Low*

## Summary
- **Total discovered:** [N] unique businesses across [M] metros
- **Geographic breakdown:** [top 5 metros by count]
- **Source coverage:** [each source used, with entity counts]

## Top Results (High Strength)
| # | Name | Location | Rating | Reviews | Strength | Sources |
|---|------|----------|--------|---------|----------|---------|
| 1 | Acme Dental | Miami, FL | 4.8 | 312 | *** High | Maps, Yelp, BBB |

## All Results by Geography
### [Metro 1] ([n] businesses)
[table]
### [Metro 2] ([n] businesses)
[table]

## What's Missing
[Data gaps, honestly: metros with low coverage, entities without websites,
sources that failed or returned thin results, anything skipped in quick scan.]
```

Strength displays as `*** High`, `** Medium`, `* Low`. The "What's Missing" section is mandatory — a market inventory that hides its own blind spots gets trusted for decisions it can't support.

---

## SaaS variant

Same header and summary; replace "All Results by Geography" with tier grouping. The tiers are a positioning statement, not a size ranking — a small pure-play outranks a giant with a feature.

```markdown
## Players by Tier

### Pure-Play (dedicated to this vertical)
| # | Name | Domain | Funding | Key Metric | Strength | Sources |
|---|------|--------|---------|------------|----------|---------|

### Adjacent (feature overlap from larger platforms)
| # | Name | Domain | Funding | Key Metric | Strength | Sources |
|---|------|--------|---------|------------|----------|---------|

### Open Source
| # | Name | Repo | Stars | Key Metric | Strength | Sources |
|---|------|------|-------|------------|----------|---------|
```

Funding column rules: sourced amount + date, or the word "Undisclosed". No inferred stages, no directory figures that failed verification. "Key Metric" is whatever best evidences traction for that entity (review count, notable customers, stars, seats) — with its source.

---

## Delivery conventions

- **Full output** goes to the user and to the market slug's workspace files (rendered output + structured entity data), so the next run can diff instead of rediscover.
- **Summaries for chat channels:** total count plus the top 10 entities only — never paste hundreds of rows into a channel.
- **CSV export:** offer, don't assume; generate from the structured entity file, and confirm before producing anything destined for bulk outreach.

## Follow-ups to offer (discovery mode)

- **"Tell me more about #N"** — full detail for one entity from the structured data
- **"Filter by [criteria]"** — re-filter existing results, no new discovery
- **"Expand to [new geography]"** — add metros, run discovery only for the new tiles, merge and re-dedup
- **"Audit against my existing list"** — switch to audit mode using this run's results as the discovery side
