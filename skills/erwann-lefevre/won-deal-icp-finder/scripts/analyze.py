#!/usr/bin/env python3
"""analyze.py — turn a deal dataset into a proven-ICP analysis.

Deterministic engine. It does the arithmetic the LLM must NOT improvise:
rank deals by size, aggregate revenue per company, measure concentration,
break revenue down by firmographics, and rank acquisition sources by
frequency. It validates the input and REFUSES to emit a best-effort result
on garbage — a wrong revenue number discovered downstream is exactly the
silent failure this tier exists to prevent.

SELECTION (this is the part that matters — pipelines differ wildly):
A deal is included if it has a deal VALUE (not null, > 0) AND falls inside the
time window (default: last 365 days, by close date, else create date). On top
of that:
  • Deals in a clearly "lost" stage are always excluded.
  • If the team marks won deals (a won stage label or a won flag), only won
    deals are kept.
  • If there is NO won signal at all, every value-bearing deal in the window is
    kept — and `selection_basis` says so, so the caller can tell the user.
This is why pulling "the newest N deals" is wrong: new deals are often empty.
Pull value-bearing deals in the window instead.

The engine produces NUMBERS. Clustering companies into named ICP archetypes is
the model's job, on top of this output.

Usage
    python3 analyze.py deals.json --since-days 365
    python3 analyze.py deals.csv --value-field "Deal value"   # value isn't in `amount`
    python3 analyze.py deals.csv --won-stage "Closed Won,Gagné"  # restrict to won stages
    python3 analyze.py deals.csv --source-field "Lead Source"
    python3 analyze.py deals.csv --since-days 0                # no time window
    cat deals.json | python3 analyze.py -
    python3 analyze.py --test

Output: a JSON report on stdout. Errors go to stderr with exit code 2 — when
the engine refuses, the caller should ASK the user, not guess.
"""
import sys, csv, json, argparse, io, re
from datetime import datetime, date, timedelta

TOP_DEFAULT = 25
SINCE_DAYS_DEFAULT = 365

SYNONYMS = {
    "amount":   ["amount", "deal amount", "deal value", "value", "montant",
                 "weighted amount", "hs_acv", "acv", "arr", "mrr",
                 "total revenue", "revenue", "ca", "chiffre d'affaires"],
    "account":  ["company", "company name", "associated company",
                 "associated company (primary)", "account", "account name",
                 "company domain", "domain", "company id", "companyid",
                 "société", "entreprise"],
    "stage":    ["dealstage", "deal stage", "stage", "pipeline stage",
                 "étape", "etape"],
    "won":      ["is_won", "hs_is_closed_won", "is closed won", "closed won",
                 "won", "gagné", "gagne"],
    "close":    ["closedate", "close date", "date closed", "won date",
                 "date de clôture", "date de cloture"],
    "create":   ["createdate", "create date", "created", "creation date",
                 "date de création", "date de creation"],
    "industry": ["industry", "company industry", "secteur",
                 "secteur d'activité", "vertical"],
    "employees":["numberofemployees", "number of employees", "no. of employees",
                 "employees", "employee count", "headcount", "company size",
                 "size", "effectif", "effectifs"],
    "country":  ["country", "company country", "hs_country", "pays", "geo",
                 "region", "région"],
    "source":   ["hs_analytics_source", "hs_analytics_source_data_1",
                 "original source", "original source type", "source",
                 "latest source", "deal source", "lead source",
                 "acquisition channel", "channel", "canal"],
    "campaign": ["campaign", "campaign name", "hs_campaign", "utm_campaign",
                 "utm campaign", "outreach campaign", "sequence",
                 "prospecting campaign", "hs_analytics_source_data_2"],
}

WON_PATTERNS = ["closed won", "closedwon", "closed-won", "closed_won", "won",
                "gagné", "gagne", "client", "signed"]
LOST_PATTERNS = ["closed lost", "closedlost", "closed-lost", "closed_lost",
                 "lost", "perdu", "abandoned", "disqualified", "nurturing-lost"]

SIZE_BUCKETS = [(1, 10, "1-10"), (11, 50, "11-50"), (51, 200, "51-200"),
                (201, 500, "201-500"), (501, 1000, "501-1000"),
                (1001, 5000, "1001-5000"), (5001, 10**9, "5001+")]


class ValidationError(Exception):
    pass


def parse_amount(raw):
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return float(raw)
    s = str(raw).strip()
    if not s:
        return None
    s = re.sub(r"[^\d,.\-]", "", s)
    if not s or s in ("-", ".", ","):
        return None
    if "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s:
        s = s.replace(",", ".") if re.search(r",\d{1,2}$", s) else s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def parse_int(raw):
    if raw is None:
        return None
    s = re.sub(r"[^\d]", "", str(raw))
    return int(s) if s else None


def size_bucket(n):
    if n is None:
        return None
    for lo, hi, label in SIZE_BUCKETS:
        if lo <= n <= hi:
            return label
    return None


def norm_date(raw):
    if not raw:
        return None
    s = str(raw).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%fZ",
                "%Y-%m-%dT%H:%M:%SZ", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(s[:len(fmt) + 6] if "%f" in fmt else s[:len(fmt)],
                                     fmt).date().isoformat()
        except ValueError:
            continue
    return s[:10] if len(s) >= 10 else s


ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def build_field_map(headers):
    lower = {h.strip().lower(): h for h in headers}
    fmap = {}
    for canon, syns in SYNONYMS.items():
        for syn in syns:
            if syn in lower:
                fmap[canon] = lower[syn]
                break
    return fmap


def load_records(raw_text):
    raw_text = raw_text.strip()
    if not raw_text:
        raise ValidationError("Empty input: no deal data provided.")
    if raw_text[0] in "[{":
        try:
            data = json.loads(raw_text)
            if isinstance(data, dict):
                data = data.get("deals") or data.get("results") or data.get("rows")
            if not isinstance(data, list):
                raise ValidationError("JSON must be a list of deals or {\"deals\":[...]}.")
            return [(r.get("properties", r) if isinstance(r, dict) else r) for r in data]
        except json.JSONDecodeError:
            pass
    rows = list(csv.DictReader(io.StringIO(raw_text)))
    if not rows:
        raise ValidationError("Could not parse input as JSON or CSV with a header row.")
    return rows


def analyze(records, value_field=None, won_stages=None, source_field=None,
            since_days=SINCE_DAYS_DEFAULT, as_of=None, top=TOP_DEFAULT):
    if not records:
        raise ValidationError("No deal rows found in the input.")

    headers = set()
    for r in records:
        if isinstance(r, dict):
            headers.update(r.keys())
    fmap = build_field_map(headers)
    if value_field:
        fmap["amount"] = value_field
    if source_field:
        fmap["source"] = source_field

    if "amount" not in fmap:
        raise ValidationError(
            "No deal-value field found. `amount` isn't present and no known value "
            "column (deal value, ARR, MRR, ACV…) was detected. Inspect a sample deal "
            "to find the field that holds deal value, then pass --value-field \"<column>\".")
    if "account" not in fmap:
        raise ValidationError(
            "No company/account column found. Each deal must carry the company it "
            "belongs to (column: company, account, associated company, domain…).")

    has_stage = "stage" in fmap
    has_wonflag = "won" in fmap
    won_stage_set = ({s.strip().lower() for s in won_stages.split(",") if s.strip()}
                     if won_stages else None)

    # pre-scan: is there ANY won signal in this dataset?
    won_signal_detected = has_wonflag
    if has_stage and not won_signal_detected:
        for rec in records:
            st = str(rec.get(fmap["stage"], "")).strip().lower()
            if any(p in st for p in WON_PATTERNS):
                won_signal_detected = True
                break

    # time window
    as_of_date = (datetime.strptime(as_of, "%Y-%m-%d").date() if as_of else date.today())
    cutoff = ((as_of_date - timedelta(days=since_days)).isoformat()
              if since_days and since_days > 0 else None)

    def deal_date(rec):
        d = norm_date(rec.get(fmap["close"])) if "close" in fmap else None
        if not d:
            d = norm_date(rec.get(fmap["create"])) if "create" in fmap else None
        return d

    counts = {"dropped_no_value": 0, "out_of_window": 0, "lost_excluded": 0,
              "not_won_excluded": 0, "no_date": 0}
    deals = []
    for rec in records:
        if not isinstance(rec, dict):
            continue
        val = parse_amount(rec.get(fmap["amount"]))
        if val is None or val <= 0:
            counts["dropped_no_value"] += 1
            continue
        dd = deal_date(rec)
        if cutoff is not None:
            if dd and ISO.match(dd):
                if dd < cutoff:
                    counts["out_of_window"] += 1
                    continue
            else:
                counts["no_date"] += 1  # keep, but flag we couldn't window it
        stage = str(rec.get(fmap["stage"], "")).strip().lower() if has_stage else ""
        if has_stage and any(p in stage for p in LOST_PATTERNS):
            counts["lost_excluded"] += 1
            continue
        # won filtering
        if won_stage_set is not None:
            if stage not in won_stage_set:
                counts["not_won_excluded"] += 1
                continue
        elif has_wonflag:
            v = str(rec.get(fmap["won"], "")).strip().lower()
            if v not in ("true", "1", "yes", "won", "oui", "y"):
                counts["not_won_excluded"] += 1
                continue
        elif won_signal_detected and has_stage:
            if not any(p in stage for p in WON_PATTERNS):
                counts["not_won_excluded"] += 1
                continue
        # else: no won signal → value-in-window basis → include

        acct = str(rec.get(fmap["account"], "")).strip() or "(unknown account)"
        emps = parse_int(rec.get(fmap["employees"])) if "employees" in fmap else None
        deals.append({
            "account": acct, "key": acct.lower(), "amount": val,
            "industry": (str(rec.get(fmap["industry"], "")).strip() if "industry" in fmap else ""),
            "employees": emps, "size_bucket": size_bucket(emps),
            "country": (str(rec.get(fmap["country"], "")).strip() if "country" in fmap else ""),
            "source": (str(rec.get(fmap["source"], "")).strip() if "source" in fmap else ""),
            "campaign": (str(rec.get(fmap["campaign"], "")).strip() if "campaign" in fmap else ""),
            "close": dd,
        })

    if not deals:
        raise ValidationError(
            f"No usable deals after filtering (value > 0, within {since_days} days, not "
            f"lost). Dropped: {counts['dropped_no_value']} without a value, "
            f"{counts['out_of_window']} outside the window, {counts['lost_excluded']} lost, "
            f"{counts['not_won_excluded']} not won. Confirm the value field "
            "(--value-field), widen the window (--since-days), or check how this team "
            "marks won deals — then re-run. If unclear, ASK the user.")

    if won_stage_set is not None:
        basis = "won-stage (explicit filter)"
    elif has_wonflag:
        basis = "won-flag"
    elif won_signal_detected and has_stage:
        basis = "won-stage (detected)"
    else:
        basis = "value-in-window (no won status found — verify with the user)"

    won_revenue = sum(d["amount"] for d in deals)
    won_count = len(deals)

    def share(v):
        return round(100 * v / won_revenue, 1) if won_revenue else 0.0

    accounts = {}
    for d in deals:
        a = accounts.setdefault(d["key"], {
            "account": d["account"], "revenue": 0.0, "deals": 0,
            "first_close": None, "last_close": None, "industry": "",
            "employees": None, "size_bucket": None, "country": "", "source": ""})
        a["revenue"] += d["amount"]
        a["deals"] += 1
        for f in ("industry", "country", "source"):
            if d[f] and not a[f]:
                a[f] = d[f]
        if d["employees"] and not a["employees"]:
            a["employees"], a["size_bucket"] = d["employees"], d["size_bucket"]
        if d["close"] and ISO.match(d["close"]):
            if not a["first_close"] or d["close"] < a["first_close"]:
                a["first_close"] = d["close"]
            if not a["last_close"] or d["close"] > a["last_close"]:
                a["last_close"] = d["close"]
    ranked = sorted(accounts.values(), key=lambda x: x["revenue"], reverse=True)
    acct_count = len(ranked)

    cum, pareto_n = 0.0, 0
    for a in ranked:
        cum += a["revenue"]; pareto_n += 1
        if cum >= 0.8 * won_revenue:
            break

    def topslice(n):
        return share(sum(a["revenue"] for a in ranked[:n]))

    seg = {"industry": {}, "size_bucket": {}, "country": {}}
    for d in deals:
        if d["industry"]:
            seg["industry"][d["industry"]] = seg["industry"].get(d["industry"], 0.0) + d["amount"]
        if d["size_bucket"]:
            seg["size_bucket"][d["size_bucket"]] = seg["size_bucket"].get(d["size_bucket"], 0.0) + d["amount"]
        if d["country"]:
            seg["country"][d["country"]] = seg["country"].get(d["country"], 0.0) + d["amount"]

    def seg_table(dd):
        return [{"value": k, "revenue": round(v, 2), "revenue_share": share(v)}
                for k, v in sorted(dd.items(), key=lambda kv: kv[1], reverse=True)]

    by_source, revenue_with_source = {}, 0.0
    for d in deals:
        if d["source"]:
            s = by_source.setdefault(d["source"], {"revenue": 0.0, "deals": 0})
            s["revenue"] += d["amount"]; s["deals"] += 1
            revenue_with_source += d["amount"]
    acquisition_sources = [
        {"source": s, "won_deals": v["deals"], "revenue": round(v["revenue"], 2),
         "revenue_share": share(v["revenue"])}
        for s, v in sorted(by_source.items(),
                           key=lambda kv: (kv[1]["deals"], kv[1]["revenue"]), reverse=True)]
    campaign_field_present = "campaign" in fmap
    campaign_values_present = any(d["campaign"] for d in deals)
    top_deals = sorted(deals, key=lambda d: d["amount"], reverse=True)[:top]

    report = {
        "summary": {
            "total_deal_value": round(won_revenue, 2),
            "deals_analyzed": won_count,
            "account_count": acct_count,
            "avg_deal_size": round(won_revenue / won_count, 2) if won_count else 0,
            "selection_basis": basis,
            "won_signal_detected": won_signal_detected,
            "window_days": since_days,
            "as_of": as_of_date.isoformat(),
            "value_field": fmap["amount"],
            "rows_in_input": len(records),
            "excluded": counts,
        },
        "top_deals": [
            {"account": d["account"], "amount": round(d["amount"], 2),
             "amount_share": share(d["amount"]),
             "industry": d["industry"] or None, "employees": d["employees"],
             "size_bucket": d["size_bucket"], "country": d["country"] or None,
             "source": d["source"] or None, "campaign": d["campaign"] or None,
             "close": d["close"]}
            for d in top_deals],
        "concentration": {
            "top_1_account_share": topslice(1),
            "top_5_accounts_share": topslice(5),
            "top_10_accounts_share": topslice(10),
            "accounts_for_80pct_revenue": pareto_n},
        "top_accounts": [
            {"account": a["account"], "revenue": round(a["revenue"], 2),
             "revenue_share": share(a["revenue"]), "deals": a["deals"],
             "avg_deal_size": round(a["revenue"] / a["deals"], 2),
             "industry": a["industry"] or None, "employees": a["employees"],
             "size_bucket": a["size_bucket"], "country": a["country"] or None,
             "source": a["source"] or None,
             "first_close": a["first_close"], "last_close": a["last_close"]}
            for a in ranked[:top]],
        "segments": {dim: seg_table(d) for dim, d in seg.items() if d},
        "acquisition": {
            "source_field_present": "source" in fmap,
            "campaign_field_present": campaign_field_present,
            "campaign_values_present": campaign_values_present,
            "source_coverage_pct": (round(100 * revenue_with_source / won_revenue, 1)
                                    if won_revenue else 0.0),
            "top_sources_by_frequency": acquisition_sources[:5],
            "all_sources": acquisition_sources},
        "data_quality": {"warnings": []},
    }

    w = report["data_quality"]["warnings"]
    aq = report["acquisition"]
    if basis.startswith("value-in-window"):
        w.append("No closed-won status found on these deals. Analyzing every deal that "
                 "carries a value in the window — confirm with the user that this maps "
                 "to their won deals (not open or lost pipeline).")
    if counts["no_date"]:
        w.append(f"{counts['no_date']} deal(s) had no usable date — kept, but not "
                 "time-filtered.")
    if not aq["source_field_present"]:
        w.append("No acquisition-source field detected — inspect a sample deal + company "
                 "+ contact for a custom field, then re-run with --source-field.")
    elif aq["source_coverage_pct"] < 70:
        w.append(f"Only {aq['source_coverage_pct']}% of value carries a source — channel "
                 "attribution is partial.")
    if not (campaign_field_present and campaign_values_present):
        w.append("No campaign-level detail — you can see the channel, not WHICH campaign "
                 "produced each deal.")
    if "industry" not in fmap:
        w.append("No industry field — vertical clustering unavailable.")
    if "employees" not in fmap:
        w.append("No employee-count field — size-bucket clustering unavailable.")
    if acct_count < 10:
        w.append(f"Only {acct_count} companies — archetypes are directional, not "
                 "statistically strong.")
    return report


def _selftest():
    failures = total = 0

    def check(name, cond):
        nonlocal failures, total
        total += 1
        if not cond:
            failures += 1
            print(f"FAIL: {name}", file=sys.stderr)

    def must_raise(name, fn):
        nonlocal failures, total
        total += 1
        try:
            fn(); failures += 1
            print(f"FAIL: {name} (no error raised)", file=sys.stderr)
        except ValidationError:
            pass

    AS_OF = "2026-05-25"
    won = [
        {"Company": "Acme",   "Amount": "1,000.00", "Deal Stage": "Closed Won",
         "Industry": "SaaS", "Number of Employees": "120", "Country": "France",
         "Original Source": "LinkedIn", "Close Date": "2026-01-10"},
        {"Company": "Acme",   "Amount": "500",      "Deal Stage": "Closed Won",
         "Industry": "SaaS", "Number of Employees": "120", "Country": "France",
         "Original Source": "LinkedIn", "Close Date": "2026-03-02"},
        {"Company": "Globex", "Amount": "2 000,50", "Deal Stage": "Closed Won",
         "Industry": "FinTech", "Number of Employees": "800", "Country": "Germany",
         "Original Source": "Email", "Close Date": "2026-02-15"},
        {"Company": "Initech","Amount": "$300",     "Deal Stage": "closedwon",
         "Industry": "SaaS", "Number of Employees": "40", "Country": "France",
         "Original Source": "", "Close Date": "2026-02-20"},
        {"Company": "Umbrella","Amount": "1200",    "Deal Stage": "Closed Won",
         "Industry": "FinTech", "Number of Employees": "5000", "Country": "Germany",
         "Original Source": "Email", "Close Date": "2026-04-01"},
        {"Company": "LostCo", "Amount": "9999",     "Deal Stage": "Closed Lost",
         "Industry": "SaaS", "Number of Employees": "10", "Country": "Spain",
         "Original Source": "LinkedIn", "Close Date": "2026-01-01"},
    ]
    r = analyze(won, as_of=AS_OF)
    check("won_total_5000_5", r["summary"]["total_deal_value"] == 5000.5)
    check("won_count_5", r["summary"]["deals_analyzed"] == 5)
    check("lost_excluded", r["summary"]["excluded"]["lost_excluded"] == 1)
    check("lost_not_in_accounts", all(a["account"] != "LostCo" for a in r["top_accounts"]))
    check("basis_detected", r["summary"]["selection_basis"] == "won-stage (detected)")
    check("top_deal_globex", r["top_deals"][0]["account"] == "Globex" and r["top_deals"][0]["amount"] == 2000.5)
    check("fr_parse", any(d["amount"] == 2000.5 for d in r["top_deals"]))
    acme = next(a for a in r["top_accounts"] if a["account"] == "Acme")
    check("acme_agg", acme["revenue"] == 1500.0 and acme["deals"] == 2)

    # --- Brice's setup: NO won/lost stage, value-bearing recent deals ---
    brice = [
        {"Company": "Alpha", "Amount": "8000", "Close Date": "2026-04-10", "Industry": "SaaS"},
        {"Company": "Beta",  "Amount": "3000", "Close Date": "2026-02-01", "Industry": "FinTech"},
        {"Company": "Gamma", "Amount": "",     "Create Date": "2026-05-20"},  # new, empty → drop
    ]
    rb = analyze(brice, as_of=AS_OF)
    check("brice_total", rb["summary"]["total_deal_value"] == 11000.0)
    check("brice_count", rb["summary"]["deals_analyzed"] == 2)
    check("brice_basis", rb["summary"]["selection_basis"].startswith("value-in-window"))
    check("brice_dropped_empty", rb["summary"]["excluded"]["dropped_no_value"] == 1)
    check("brice_warns_basis", any("No closed-won status" in x for x in rb["data_quality"]["warnings"]))

    # --- the original bug: newest deals empty, older ones valued → must NOT refuse ---
    bug = [
        {"Company": "NewCo", "Amount": "", "Create Date": "2026-05-24"},
        {"Company": "RealCo", "Amount": "5000", "Close Date": "2026-03-01"},
    ]
    rbug = analyze(bug, as_of=AS_OF)
    check("bug_proceeds", rbug["summary"]["total_deal_value"] == 5000.0
          and rbug["summary"]["deals_analyzed"] == 1)

    # --- time window: a valued deal older than 365d is excluded ---
    old = [
        {"Company": "Recent", "Amount": "1000", "Close Date": "2026-03-01"},
        {"Company": "Ancient", "Amount": "9000", "Close Date": "2024-01-01"},
    ]
    ro = analyze(old, as_of=AS_OF, since_days=365)
    check("window_excludes_old", ro["summary"]["deals_analyzed"] == 1
          and ro["summary"]["excluded"]["out_of_window"] == 1)
    # since_days 0 disables the window → both kept
    ro0 = analyze(old, as_of=AS_OF, since_days=0)
    check("window_off", ro0["summary"]["deals_analyzed"] == 2)

    # --- custom value field (amount column absent) ---
    custom_val = [{"Company": "X", "Deal value": "4200", "Close Date": "2026-04-01"}]
    rc = analyze(custom_val, as_of=AS_OF)  # "deal value" is a known synonym → auto
    check("custom_value_auto", rc["summary"]["total_deal_value"] == 4200.0)
    rco = analyze([{"Company": "X", "MyVal": "4200", "Close Date": "2026-04-01"}],
                  value_field="MyVal", as_of=AS_OF)
    check("value_field_override", rco["summary"]["total_deal_value"] == 4200.0)

    # --- custom source-field override + campaign detection ---
    rsrc = analyze([{"Company": "X", "Amount": "100", "Close Date": "2026-04-01",
                     "Lead Source": "Webinar"}], source_field="Lead Source", as_of=AS_OF)
    check("source_override", rsrc["acquisition"]["top_sources_by_frequency"][0]["source"] == "Webinar")
    rcamp = analyze([{"Company": "X", "Amount": "100", "Close Date": "2026-04-01",
                      "Campaign": "Q2 Outbound"}], as_of=AS_OF)
    check("campaign_present", rcamp["acquisition"]["campaign_field_present"] is True
          and rcamp["acquisition"]["campaign_values_present"] is True)

    # --- won-stage explicit restrict ---
    rws = analyze(won, won_stages="Closed Won", as_of=AS_OF)
    # Initech stage is "closedwon" (no space) → excluded by explicit "Closed Won"
    check("won_stage_explicit", rws["summary"]["selection_basis"].startswith("won-stage (explicit")
          and all(d["account"] != "Initech" for d in rws["top_deals"]))

    # --- refusals ---
    must_raise("empty", lambda: analyze([]))
    must_raise("no_value_field", lambda: analyze([{"Company": "X", "Close Date": "2026-04-01"}], as_of=AS_OF))
    must_raise("no_account", lambda: analyze([{"Amount": "100", "Close Date": "2026-04-01"}], as_of=AS_OF))
    must_raise("all_empty_value", lambda: analyze(
        [{"Company": "X", "Amount": "", "Close Date": "2026-04-01"}], as_of=AS_OF))
    must_raise("all_out_of_window", lambda: analyze(
        [{"Company": "X", "Amount": "100", "Close Date": "2020-01-01"}], as_of=AS_OF, since_days=365))

    print(f"{total - failures}/{total} checks passed")
    return 1 if failures else 0


def main():
    p = argparse.ArgumentParser(description="Proven-ICP analysis from closed-won deals.")
    p.add_argument("spec", nargs="?", help="path to .json/.csv, or - for stdin")
    p.add_argument("--value-field", "--amount-field", dest="value_field",
                   help="the column holding deal value (if not the standard `amount`)")
    p.add_argument("--won-stage", help="comma-separated exact won stage labels to restrict to")
    p.add_argument("--source-field", help="override the acquisition-source column (custom field)")
    p.add_argument("--since-days", type=int, default=SINCE_DAYS_DEFAULT,
                   help="time window in days (default 365; 0 = no window)")
    p.add_argument("--as-of", help="reference date YYYY-MM-DD for the window (default: today)")
    p.add_argument("--top", type=int, default=TOP_DEFAULT, help="top-N deals/accounts to return")
    p.add_argument("--test", action="store_true")
    a = p.parse_args()

    if a.test:
        sys.exit(_selftest())
    if not a.spec:
        print("error: provide a deals file (.json/.csv) or - for stdin", file=sys.stderr)
        sys.exit(2)
    raw = sys.stdin.read() if a.spec == "-" else open(a.spec, encoding="utf-8-sig").read()
    try:
        records = load_records(raw)
        report = analyze(records, value_field=a.value_field, won_stages=a.won_stage,
                         source_field=a.source_field, since_days=a.since_days,
                         as_of=a.as_of, top=a.top)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except ValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
