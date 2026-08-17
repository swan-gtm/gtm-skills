# The analysis engine

`scripts/analyze.py` does the arithmetic. No dependencies beyond the standard library.

```bash
python3 scripts/analyze.py /path/to/deals.json --since-days 365
```

Accepts `.json`, `.csv`, or `-` for stdin. Returns a single JSON object.

## Flags

| Flag | When you need it |
|---|---|
| `--value-field "ARR"` | The money lives somewhere other than the standard amount column |
| `--won-stage "Closed Won,Gagné"` | A real won stage exists — restrict to it. Comma-separated, exact labels, localised spellings welcome |
| `--source-field "Lead Source"` | Acquisition source is in a custom column |
| `--since-days N` | Window length; default 365, `0` disables windowing |
| `--as-of YYYY-MM-DD` | Anchor the window to a fixed date rather than today |
| `--top N` | How many deals and accounts to return |
| `--test` | Run the golden-case self-test |

Column matching is alias-based, so raw CRM exports with human-readable headers usually run with no flags at all. Amounts parse in both European (`1.234,56`) and US (`1,234.56`) notation.

## Reading the output

**`summary`** — the framing numbers, and two fields that govern how strongly you may phrase everything else:

- `selection_basis` — either a detected won stage or flag, or `value-in-window` when no won signal exists. When it's `value-in-window`, state the basis in one line and ask the user to confirm it maps to their definition of won.
- `excluded` — what was dropped and why (`dropped_no_value`, `out_of_window`, `lost_excluded`, `not_won_excluded`, `no_date`). Check this first when a total looks wrong. A large `dropped_no_value` usually means the wrong value field.

**`top_deals`** — individual deals ranked by size. The headline table.

**`top_accounts`** — revenue aggregated per company, so a customer with four deals appears once at its true weight. This, not `top_deals`, is the input to clustering.

**`concentration`** — `top_1_account_share`, `top_5_accounts_share`, `top_10_accounts_share`, and `accounts_for_80pct_revenue`. A `top_1_account_share` above roughly 25% means revenue leans on one customer; report that rather than fitting an archetype to it. A low `accounts_for_80pct_revenue` says the same thing in the other direction.

**`segments`** — revenue and counts broken out by `industry`, `size_bucket` and `country`. The raw material for archetypes. Read revenue share, not counts.

**`acquisition`** —

- `top_sources_by_frequency` — the ranking, with revenue attached.
- `source_coverage_pct` — the share of deals carrying a source at all. Below ~70%, the ranking describes a sample; say so.
- `source_field_present` — false means no source field was found anywhere on deal, company or contact.
- `campaign_field_present` / `campaign_values_present` — when either is false, the data shows channel but not campaign. Name that gap: the team can see outbound produced revenue but not which sequence did.

**`data_quality.warnings`** — surface these plainly. They set the ceiling on how confidently anything can be stated.

## When it refuses

The engine exits with an error rather than guessing when there is no usable value field, no company column, or nothing left after filtering. Each refusal names the cause.

A refusal is a question for the user — where does deal value live, how do you mark a deal won — not a condition to work around by loosening the filters until something comes back.

## Self-test

```bash
python3 scripts/analyze.py --test
```

Golden cases cover deal-size ranking, revenue aggregation across multi-deal companies, European and US amount parsing, the `value-in-window` selection path including the newest-deals-are-empty failure mode, windowing, won-signal detection, always excluding lost deals, custom field overrides, source-frequency ranking, campaign-field detection, and each refusal.

## Worked example

`examples/sample-deals.json` is a fictional 14-row export — 12 won, 1 lost, 1 open, across 10 companies — carrying a channel-level source but no campaign field, so it exercises the campaign-gap path.

```bash
python3 scripts/analyze.py examples/sample-deals.json --since-days 3650
```

The rows carry a stage label, so the won signal is detected and the lost and open deals are excluded. Revenue concentrates in FinTech and SaaS; the leading source by frequency is LinkedIn. The wide window is only because the sample dates are fixed — use 365 on real data.
