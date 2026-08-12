# Batch resolver script

Write the script at the bottom of this page verbatim to `clearbit_resolve.py`
in the working directory, then run the three subcommands in order.

## 1. Plan

```bash
python3 clearbit_resolve.py plan input.csv --column "Company Name" --out plan.json
```

Dedupes on a normalized key, strips legal suffixes, and emits `plan.json`
with a `urls` map of `query -> URL`. Plain-text input (one name per line)
works too — omit `--column`.

## 2. Fetch

Try direct first — it costs one call and works outside sandboxes:

```bash
python3 clearbit_resolve.py fetch plan.json --out raw.json
```

If it exits with the network-blocked message, fall back to your agent's
web-fetch tool:

- Read `plan.json` → `urls`.
- Fetch each URL, 5–8 in parallel per batch.
- Assemble `raw.json` yourself, keyed by the **query string** (the key in
  `urls`, not the URL, and not the original CSV value):

```json
{
  "Ramp": [{"name": "Ramp", "domain": "ramp.com", "logo": null}],
  "Bright Data": []
}
```

- Empty arrays must be recorded as `[]`, not omitted — omitted queries land
  in the output as `not_fetched`, which is a different problem than
  "no match".

## 3. Merge and score

```bash
python3 clearbit_resolve.py merge plan.json raw.json --out resolved.csv
```

Output keeps every original column and appends `resolved_domain`,
`matched_name`, `confidence`, `needs_review`, `alternatives`, and prints
counts per confidence level.

## The script

```python
#!/usr/bin/env python3
"""Company name -> domain resolution via the Clearbit autocomplete endpoint."""
import argparse, csv, json, re, sys, urllib.parse, urllib.request

ENDPOINT = "https://autocomplete.clearbit.com/v1/companies/suggest?query="

SUFFIXES = {
    "inc", "inc.", "llc", "l.l.c", "ltd", "ltd.", "limited", "corp", "corp.",
    "corporation", "co", "co.", "company", "gmbh", "plc", "sa", "s.a", "ag",
    "bv", "b.v", "nv", "ab", "oy", "as", "pty", "pte", "srl", "spa", "kk",
    "holdings", "holding", "group", "the",
}
PREFIXES = ("www.", "get", "join", "try", "use", "hey", "the", "my", "go")


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[‘’“”\"']", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    toks = [t for t in s.split() if t not in SUFFIXES]
    return " ".join(toks) if toks else s


def clean_query(s: str) -> str:
    """Strip trailing legal suffixes, keep casing. The endpoint degrades badly
    on 'Acme Inc.' / 'Acme Ltd' -- literal junk match or an empty array."""
    s = re.sub(r"\s+", " ", (s or "").strip().strip(","))
    toks = s.split()
    while toks and re.sub(r"[^a-z0-9.]", "", toks[-1].lower()) in SUFFIXES:
        toks.pop()
    out = " ".join(toks).strip(" ,.;-")
    return out or s


def compact(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def domain_slug(domain: str) -> str:
    d = (domain or "").lower()
    if d.startswith("www."):
        d = d[4:]
    core = d.split(".")[0]
    for p in PREFIXES:
        if p != "www." and core.startswith(p) and len(core) > len(p) + 2:
            core = core[len(p):]
            break
    return re.sub(r"[^a-z0-9]", "", core)


GTLD = (".com", ".io", ".ai", ".co", ".net", ".org")


def score(query: str, results: list) -> dict:
    q_n, q_c = norm(query), compact(norm(query))
    if not results:
        return {"domain": "", "matched_name": "", "confidence": "none",
                "needs_review": "yes", "alternatives": ""}

    name_hits = [r for r in results if norm(r.get("name")) == q_n]
    slug_hits = [r for r in results if domain_slug(r.get("domain")) == q_c]

    def rank(r):
        d = (r.get("domain") or "").lower()
        return (0 if domain_slug(d) == q_c else 1,
                0 if d.endswith(GTLD) else 1,
                d.count("."), len(d))

    pool = sorted(slug_hits or name_hits or results, key=rank)
    best = pool[0]

    if len(slug_hits) == 1:
        conf = "exact" if name_hits and results[0] is slug_hits[0] else "strong"
    elif len(slug_hits) > 1:
        conf = "plausible"
    elif len(name_hits) > 1:
        conf = "ambiguous"
    elif len(name_hits) == 1:
        conf = "strong"
    else:
        conf = "weak"

    review = {"exact": "no", "strong": "no", "plausible": "spot-check"}.get(conf, "yes")
    alts = [r.get("domain", "") for r in pool[1:4] if r.get("domain")]
    return {"domain": best.get("domain", ""), "matched_name": best.get("name", ""),
            "confidence": conf, "needs_review": review, "alternatives": "; ".join(alts)}


def read_names(path, column):
    with open(path, newline="", encoding="utf-8-sig") as f:
        if path.lower().endswith((".csv", ".tsv")):
            delim = "\t" if path.lower().endswith(".tsv") else ","
            rows = list(csv.DictReader(f, delimiter=delim))
            if column not in (rows[0].keys() if rows else []):
                sys.exit(f"Column '{column}' not found. Available: "
                         f"{list(rows[0].keys()) if rows else []}")
            return rows, [r[column] for r in rows]
        names = [ln.strip() for ln in f if ln.strip()]
        return [{"Company": n} for n in names], names


def cmd_plan(a):
    rows, names = read_names(a.input, a.column)
    seen, queries = set(), []
    for n in names:
        k = norm(n)
        if k and k not in seen:
            seen.add(k)
            queries.append(clean_query(n))
    plan = {"column": a.column, "rows": rows, "queries": queries,
            "urls": {q: ENDPOINT + urllib.parse.quote(q) for q in queries}}
    json.dump(plan, open(a.out, "w", encoding="utf-8"), indent=2)
    print(f"{len(rows)} rows -> {len(queries)} unique queries. Plan: {a.out}")


def cmd_fetch(a):
    plan = json.load(open(a.plan, encoding="utf-8"))
    raw = {}
    for i, (q, url) in enumerate(plan["urls"].items(), 1):
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                raw[q] = json.load(r)
        except Exception as e:
            sys.exit(f"Direct fetch failed on '{q}' ({e}).\n"
                     f"Network is likely blocked here -- use a web-fetch tool "
                     f"on plan['urls'], hand-build raw.json, then run `merge`.")
        if i % 25 == 0:
            print(f"  ...{i}/{len(plan['urls'])}", file=sys.stderr)
    json.dump(raw, open(a.out, "w", encoding="utf-8"), indent=2)
    print(f"Fetched {len(raw)} queries -> {a.out}")


def cmd_merge(a):
    plan = json.load(open(a.plan, encoding="utf-8"))
    raw = json.load(open(a.raw, encoding="utf-8"))
    by_norm = {norm(q): score(q, res) for q, res in raw.items()}
    col = plan["column"]
    out_fields = list(plan["rows"][0].keys()) + [
        "resolved_domain", "matched_name", "confidence", "needs_review", "alternatives"]
    counts = {}
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        for row in plan["rows"]:
            s = by_norm.get(norm(row.get(col, "")), {
                "domain": "", "matched_name": "", "confidence": "not_fetched",
                "needs_review": "yes", "alternatives": ""})
            counts[s["confidence"]] = counts.get(s["confidence"], 0) + 1
            w.writerow({**row, "resolved_domain": s["domain"],
                        "matched_name": s["matched_name"],
                        "confidence": s["confidence"],
                        "needs_review": s["needs_review"],
                        "alternatives": s["alternatives"]})
    print(f"Wrote {a.out}")
    for k in ("exact", "strong", "plausible", "ambiguous", "weak", "none", "not_fetched"):
        if counts.get(k):
            print(f"  {k:11} {counts[k]}")


p = argparse.ArgumentParser()
sub = p.add_subparsers(dest="cmd", required=True)
sp = sub.add_parser("plan"); sp.add_argument("input")
sp.add_argument("--column", default="Company"); sp.add_argument("--out", default="plan.json")
sp.set_defaults(fn=cmd_plan)
sf = sub.add_parser("fetch"); sf.add_argument("plan")
sf.add_argument("--out", default="raw.json"); sf.set_defaults(fn=cmd_fetch)
sm = sub.add_parser("merge"); sm.add_argument("plan"); sm.add_argument("raw")
sm.add_argument("--out", default="resolved.csv"); sm.set_defaults(fn=cmd_merge)
a = p.parse_args(); a.fn(a)
```
