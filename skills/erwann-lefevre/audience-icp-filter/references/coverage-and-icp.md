# The coverage gate and the ICP questions

Run in this order. Coverage first, always — it decides which questions are worth asking.

## Coverage

```bash
python3 scripts/build.py --coverage leads.json
```

Reports fill rates per field and names which criteria the data cannot support.

| Field | Needed for | Below threshold |
|---|---|---|
| Job title | Seniority and function detection | Classification degrades; most leads land in review |
| Company name | Company-based exclusion | Exclusion is unreliable |
| Bio | Catching people whose company **and** email are both empty | Own-team and competitor exclusion **will leak** |
| Work email | Domain-based exclusion | Job-changers slip through |
| Location | Geography filtering | Geo criteria **cannot** be applied |
| Industry | Industry filtering | Industry criteria **cannot** be applied |

The bio row is the one people skip. It's the only field that catches a colleague whose company field is blank and who has no email on file — and that's the exact profile of someone imported from a social export.

## Enrichment

When the gate flags gaps, offer profile enrichment, quote the exact cost, and wait for an explicit yes.

The coverage output returns `leads_needing_enrichment` — the number of rows actually missing at least one of the fields that came back insufficient, not the size of the list. On an audience that is mostly complete those are very different numbers, and quoting the total overstates the cost of the fix.

Enrichment aimed at finding email addresses is a different, more expensive product and contributes nothing to ICP scoring. If someone asks for it here, say plainly that it serves deliverability rather than filtering, and let them decide.

If enrichment is declined, proceed — and state which criteria were dropped and that exclusion is now best-effort.

## The ICP questions

Ask after coverage, and don't offer criteria the data can't support.

| # | Question | Feeds |
|---|---|---|
| 1 | Which seniority levels qualify? Founder/C-level · VP/Head of · Manager/Lead · IC | `icp.seniority` |
| 2 | Which functions? Sales · Growth/Marketing · RevOps/GTM · Partnerships · Product/Tech | `icp.functions` |
| 3 | Do founders qualify regardless of stated function? | `founder_qualifies_regardless_of_function` |
| 4 | Any geography or industry constraint? *(only if coverage supports it)* | `icp.locations`, `icp.industries` |
| 5 | Who is excluded outright — own company, competitors, agencies? | `exclusions` |

**Question 3 carries more weight than it looks.** Most founder titles state no function at all: `Co-Founder`, `Fondatrice`, `Founder @ Stealth`. If founders don't auto-qualify, every one of them lands in review. On a real 150-lead list this single answer moved about fifteen leads. Ask it explicitly and explain the trade-off rather than assuming.

If the ICP comes back vague — "good leads", "decision makers" — push once for specifics. A vague ICP produces an enormous review bucket, which is the problem this skill exists to remove.

## The spec

`build.py` reads one JSON object:

```json
{
  "icp": {
    "seniority": ["founder_c", "vp_head", "manager_lead"],
    "functions": ["sales", "growth_marketing", "revops"],
    "founder_qualifies_regardless_of_function": false,
    "locations": ["France", "Paris"],
    "industries": ["saas"]
  },
  "exclusions": {
    "domains": ["yourcompany.com"],
    "companies": ["Your Company"],
    "keywords": ["competitor-a", "competitor-b"]
  },
  "leads": [
    {
      "leadId": "...", "jobTitle": "...", "companyName": "...",
      "proEmail": "...", "shortBio": "...", "location": "...", "industry": "..."
    }
  ]
}
```

Include `locations` and `industries` only when coverage supports them. Each lead needs an id, or both a first and last name.

Then:

```bash
python3 scripts/build.py spec.json > pass1.json
```

It refuses invalid input rather than emitting a best-effort sort. When it errors, fix the spec — never work around it by classifying by hand.

For pass 2, pass `{"result": <pass1 output>, "overrides": [{"_key": "...", "bucket": "...", "reason": "..."}]}` to `--adjudicate`. It re-runs the same reconciliation and rejects an override on a lead that doesn't exist, an invalid bucket, a duplicate, or a reclassification with no substantive reason.

## Two spec traps

**Geography matches on substring, so list the real variants.** Enrichment writes `"Greater Paris Metropolitan Region"` and `"Greater Lyon Area"` — neither contains the string `"France"`, so `locations: ["France"]` silently drops both. Glance at the actual location values before writing the spec and include the metros and regions that appear.

**Industry expands automatically — don't hand-list variants.** Pass a canonical bucket (`saas`, `software`, `tech`, `fintech`, `healthtech`, `ecommerce`) and the script expands it to the platform labels that mean the same thing, so `["saas"]` also catches `Software Development`, `Technology, Information and Internet` and `IT Services`. This matters: real software companies routinely get labelled "Technology, Information and Internet" and would otherwise be dropped. For a bucket outside the synonym map, list the variants yourself, or let the geo/industry queue flag surface the misses in pass 2.

## The buckets

| Bucket | Meaning |
|---|---|
| `match` | Seniority and function both in ICP, constraints satisfied |
| `review` | The engine declined to guess — unclear title, missing function, absent geo/industry data |
| `no_match` | Out of ICP, or a noise title (student, intern, open-to-work, investor) |
| `excluded` | Own team, competitor, or a listed exclusion |

Every lead lands in exactly one, with a reason, and the counts reconcile against the input.

A review bucket around a third is normal on thin data. Say so plainly and name the cause rather than presenting it as a finding.

## Self-test

```bash
python3 scripts/build.py --test
```

Covers seniority precedence, multi-function collection, bio fallback, each exclusion leak mode, the short-token guard, industry synonym expansion, count reconciliation, and every refusal path.
