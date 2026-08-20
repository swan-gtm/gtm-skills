#!/usr/bin/env python3
"""build.py — classify an audience into ICP buckets. Refuses invalid input.

TWO-PASS BY DESIGN. Neither pass is optional.

  Pass 1 (this script, default mode) — deterministic. Sorts every lead into
  exactly one of excluded / match / review / no_match using the pattern
  taxonomy, and reconciles the counts. Guarantees nothing is lost and that
  exclusions are applied uniformly.

  Pass 2 (the model, then --adjudicate) — semantic. Patterns cannot read
  meaning: 'Chief Happiness Officer' matches the C-level pattern but is an HR
  role; 'Nothing' is not a company; a competitor absent from the exclusion list
  is invisible to a regex. The model reviews EVERY bucket, proposes overrides
  with reasons, and this script re-validates them so the model cannot lose or
  duplicate a lead either.

Pass 1 alone is fast and wrong at the edges. Pass 2 alone is unauditable and
leaks. The combination is the point.

Usage:
    python3 scripts/build.py spec.json                 # pass 1
    cat spec.json | python3 scripts/build.py -
    python3 scripts/build.py --adjudicate review.json  # pass 2, validated
    python3 scripts/build.py --test
"""
import sys, os, json, re, argparse

TAXONOMY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "references", "title-taxonomy.json")

VALID_SENIORITY = {"founder_c", "vp_head", "manager_lead", "ic"}
BUCKETS = ("match", "review", "no_match", "excluded")


class ValidationError(Exception):
    pass


def _compile(pattern):
    """Compile a taxonomy pattern, case-sensitively when it carries an uppercase.

    Short acronyms are indistinguishable from common words once case is thrown
    away: `\bIT\b` under re.IGNORECASE matches the English pronoun, so a bio
    reading "making it happen" scored as product_tech and the lead was dropped
    from the ICP without ever reaching pass 2. Uppercase in a pattern is
    therefore load-bearing — it means the capitals are part of the signal.

    Everything else stays case-insensitive, which is why the detectors are fed
    the original-case string rather than a lowercased one.
    """
    return re.compile(pattern, 0 if re.search(r"[A-Z]", pattern) else re.I)


def _load_taxonomy(path=TAXONOMY_PATH):
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    tax = {
        "seniority": [(t["tier"], [_compile(p) for p in t["patterns"]])
                      for t in raw["seniority"]],
        "function": {f["key"]: [_compile(p) for p in f["patterns"]]
                     for f in raw["function"]},
        "noise": [_compile(p) for p in raw["noise_patterns"]],
        "industry_synonyms": {k.lower(): [v.lower() for v in vs]
                              for k, vs in raw.get("industry_synonyms", {}).items()},
        "agency": [_compile(p) for p in raw.get("agency_patterns", [])],
    }
    return tax


def expand_industries(industries, tax):
    """Add known LinkedIn industry variants for any canonical bucket the user
    named. 'SaaS' alone would miss a company labelled 'Technology, Information
    and Internet'; expanding it up front stops that lead becoming a false
    no_match the model then has to repair. Returns a de-duplicated list."""
    if not industries:
        return industries
    syn = tax.get("industry_synonyms", {})
    out = []
    for term in industries:
        t = term.strip().lower()
        out.append(term)
        for key, variants in syn.items():
            if key in t or t in key:
                out.extend(variants)
    seen, dedup = set(), []
    for x in out:
        xl = x.lower()
        if xl not in seen:
            seen.add(xl)
            dedup.append(x)
    return dedup


def is_agency(lead, tax):
    """True if the lead's company or bio reads like an agency / freelance /
    consulting shop. Not an exclusion — a flag so pass 2 double-checks."""
    hay = (_norm(lead.get("companyName")) + " | " + _norm(lead.get("shortBio")))
    return any(p.search(hay) for p in tax.get("agency", []))


# ---------------------------------------------------------------- validation

def validate_spec(spec):
    """Raise ValidationError on anything that would produce a wrong sort."""
    if not isinstance(spec, dict):
        raise ValidationError("spec must be a JSON object")

    icp = spec.get("icp")
    if not isinstance(icp, dict):
        raise ValidationError("spec.icp is required and must be an object")

    sen = icp.get("seniority")
    if not isinstance(sen, list) or not sen:
        raise ValidationError("icp.seniority must be a non-empty list")
    bad = set(sen) - VALID_SENIORITY
    if bad:
        raise ValidationError(
            f"unknown seniority tier(s): {sorted(bad)}. Valid: {sorted(VALID_SENIORITY)}")

    fns = icp.get("functions")
    if not isinstance(fns, list) or not fns:
        raise ValidationError("icp.functions must be a non-empty list")

    leads = spec.get("leads")
    if not isinstance(leads, list):
        raise ValidationError("spec.leads must be a list")
    if not leads:
        raise ValidationError("spec.leads is empty — nothing to classify")

    for i, ld in enumerate(leads):
        if not isinstance(ld, dict):
            raise ValidationError(f"leads[{i}] must be an object")
        has_id = bool(str(ld.get("leadId") or "").strip())
        has_name = bool(str(ld.get("firstname") or "").strip()) and \
                   bool(str(ld.get("lastname") or "").strip())
        if not (has_id or has_name):
            raise ValidationError(
                f"leads[{i}] needs a leadId, or both firstname and lastname — "
                "without an identifier it cannot be written back safely")


def validate_result(leads, result):
    """Nothing lost, nothing duplicated, nothing in two buckets."""
    total = sum(len(result[b]) for b in BUCKETS)
    if total != len(leads):
        raise ValidationError(
            f"count mismatch: {len(leads)} leads in, {total} classified out")
    seen = {}
    for b in BUCKETS:
        for row in result[b]:
            key = row["_key"]
            if key in seen:
                raise ValidationError(
                    f"lead {key!r} classified into both {seen[key]} and {b}")
            seen[key] = b


# ------------------------------------------------------------ classification

def _norm(v):
    return str(v or "").strip()


def _haystack(lead):
    """Every field that can reveal who someone really works for.

    Deliberately includes shortBio: attendees routinely have an empty company
    and no email while their bio says 'Client Partner @ Acme'. Matching on
    company alone lets those through.
    """
    return " | ".join([
        _norm(lead.get("companyName")),
        _norm(lead.get("proEmail")),
        _norm(lead.get("persoEmail")),
        _norm(lead.get("shortBio")),
        _norm(lead.get("companyUrl")),
    ]).lower()


def detect_seniority(title, tax):
    for tier, patterns in tax["seniority"]:
        for pat in patterns:
            if pat.search(title):
                return tier
    return None


def detect_functions(title, tax):
    found = []
    for key, patterns in tax["function"].items():
        if any(p.search(title) for p in patterns):
            found.append(key)
    return found


def _squash(s):
    """Strip everything but letters and digits.

    People write the same company a dozen ways: 'Northwind Labs',
    '@NorthwindLabs', 'northwind-labs'. Matching the spaced form alone
    misses the collapsed one, which is exactly how a colleague ends up in your
    prospect list. Squashing both sides makes the comparison spelling-agnostic.
    """
    return re.sub(r"[^a-z0-9]", "", s.lower())


# Below this length, a squashed substring match is too collision-prone to trust
# ('nwl' would fire inside unrelated words), so short terms stay word-bounded.
_SQUASH_MIN = 5


def check_exclusions(lead, exclusions):
    hay = _haystack(lead)
    hay_squashed = _squash(hay)

    for dom in exclusions.get("domains", []):
        d = dom.strip().lower().lstrip("@")
        if not d:
            continue
        if d in hay:
            return f"excluded domain: {dom}"
        # 'northwindlabs.com' should also catch a bare '@NorthwindLabs'
        stem = _squash(d.rsplit(".", 1)[0])
        if len(stem) >= _SQUASH_MIN and stem in hay_squashed:
            return f"excluded domain: {dom}"

    for comp in exclusions.get("companies", []):
        c = comp.strip().lower()
        if not c:
            continue
        if re.search(r"(?<![a-z0-9])" + re.escape(c) + r"(?![a-z0-9])", hay):
            return f"excluded company: {comp}"
        cs = _squash(c)
        if len(cs) >= _SQUASH_MIN and cs in hay_squashed:
            return f"excluded company: {comp}"

    for kw in exclusions.get("keywords", []):
        k = kw.strip().lower()
        if not k:
            continue
        if k in hay:
            return f"excluded keyword: {kw}"
        ks = _squash(k)
        if len(ks) >= _SQUASH_MIN and ks in hay_squashed:
            return f"excluded keyword: {kw}"

    return None


def _criterion_ok(lead, field, wanted):
    """Return True / False / None (None = data missing, cannot judge)."""
    if not wanted:
        return True
    val = _norm(lead.get(field)).lower()
    if not val:
        return None
    return any(w.strip().lower() in val for w in wanted)


INFERRED_DROP = " (inferred from bio)"


def classify(lead, icp, exclusions, tax):
    """Return (bucket, reason)."""
    reason_excl = check_exclusions(lead, exclusions)
    if reason_excl:
        return "excluded", reason_excl

    title = _norm(lead.get("jobTitle"))
    if not title:
        return "review", "no job title — cannot judge seniority or function"

    for pat in tax["noise"]:
        if pat.search(title):
            return "no_match", f"noise title: {title}"

    # The title is the primary signal, but since enrichment now exposes the bio,
    # use it as a fallback: many people write their function in the bio, not the
    # title ("Managing Director" + bio "Développement commercial"). Only fall
    # back when the title is silent — the title is more reliable when present.
    bio = _norm(lead.get("shortBio"))

    seniority = detect_seniority(title, tax)
    sen_src = "title"
    if seniority is None and bio:
        seniority = detect_seniority(bio, tax)
        sen_src = "bio"

    functions = detect_functions(title, tax)
    fn_src = "title"
    if not functions and bio:
        functions = detect_functions(bio, tax)
        fn_src = "bio"

    if seniority is None:
        return "review", f"seniority unclear from title or bio: {title}"

    if seniority not in icp["seniority"]:
        return "no_match", (f"seniority {seniority} not in ICP"
                            + (INFERRED_DROP if sen_src == "bio" else ""))

    founder_pass = (seniority == "founder_c" and
                    icp.get("founder_qualifies_regardless_of_function", False))

    if not founder_pass:
        if not functions:
            return "review", f"function unclear from title or bio: {title}"
        if not set(functions) & set(icp["functions"]):
            return "no_match", (f"function {functions} not in ICP"
                                + (INFERRED_DROP if fn_src == "bio" else ""))

    for field, key in (("location", "locations"), ("industry", "industries")):
        ok = _criterion_ok(lead, field, icp.get(key))
        if ok is None:
            return "review", f"{field} required by ICP but missing on this lead"
        if ok is False:
            return "no_match", f"{field} outside ICP"

    detail = f"{seniority}"
    if functions:
        detail += f" / {'+'.join(functions)}"
    src = []
    if sen_src == "bio":
        src.append("seniority from bio")
    if fn_src == "bio":
        src.append("function from bio")
    if src:
        detail += f" (inferred: {', '.join(src)} — worth a pass-2 glance)"
    return "match", f"ICP match: {detail}"


def build(spec):
    validate_spec(spec)
    tax = _load_taxonomy()

    icp = dict(spec["icp"])
    # expand SaaS/tech/etc. into their real LinkedIn industry variants up front
    if icp.get("industries"):
        icp["industries"] = expand_industries(icp["industries"], tax)
    exclusions = spec.get("exclusions", {}) or {}
    leads = spec["leads"]

    result = {b: [] for b in BUCKETS}
    queue = []
    for i, lead in enumerate(leads):
        bucket, reason = classify(lead, icp, exclusions, tax)
        key = _norm(lead.get("leadId")) or \
            f"{_norm(lead.get('firstname'))} {_norm(lead.get('lastname'))}#{i}"
        row = dict(lead)
        row["_key"] = key
        row["_bucket"] = bucket
        row["_reason"] = reason

        # Flag the leads pass 2 should actually look at — so it reviews ~a few
        # dozen, not the whole audience. Three risk classes:
        flag = None
        if bucket == "review":
            flag = "ambiguous"                                   # always
        elif bucket == "match":
            if "inferred:" in reason:
                flag = "bio-inferred match"                      # soft match
            elif is_agency(lead, tax):
                flag = "agency/freelance — confirm it's the ICP" # false-positive risk
        elif bucket == "no_match":
            # dropped ONLY on a soft substring criterion → likely false negative
            if reason.startswith("location outside") or reason.startswith("industry outside"):
                flag = "dropped on geo/industry — check the variant"
            elif INFERRED_DROP in reason:
                # Dropped on a signal read out of free text, not off the title.
                # Nothing may leave the ICP on an inference without a second look.
                flag = "bio-inferred drop — confirm before discarding"
        if flag:
            row["_flag"] = flag
            queue.append(row)

        result[bucket].append(row)

    validate_result(leads, result)

    return {
        "pass": 1,
        "adjudicated": False,
        "counts": {b: len(result[b]) for b in BUCKETS} | {"total": len(leads)},
        "pass2_queue_size": len(queue),
        "pass2_queue": queue,
        "buckets": result,
    }


# ----------------------------------------------------------- coverage report

# Below these fill rates a criterion cannot be applied honestly: the engine
# would send most leads to `review` for missing data and call it a result.
COVERAGE_RULES = [
    ("jobTitle",    0.80, "core",       "seniority and function detection"),
    ("companyName", 0.60, "core",       "company-based exclusion"),
    ("shortBio",    0.50, "exclusion",  "catching people whose company/email is empty"),
    ("proEmail",    0.40, "exclusion",  "domain-based exclusion"),
    ("location",    0.80, "locations",  "geography filtering"),
    ("industry",    0.80, "industries", "industry filtering"),
]


def coverage(payload):
    """Report field fill rates and say which ICP criteria the data can support.

    Run this BEFORE the ICP Q&A. There is no point offering geography filtering
    on an audience where `location` is empty everywhere — that just routes the
    whole list to `review`. Better to see the gap and offer enrichment first.
    """
    leads = payload.get("leads") if isinstance(payload, dict) else None
    if not isinstance(leads, list) or not leads:
        raise ValidationError("payload.leads must be a non-empty list")

    n = len(leads)
    fields, blocked, degraded = {}, [], []
    for field, threshold, kind, purpose in COVERAGE_RULES:
        filled = sum(1 for ld in leads if _norm(ld.get(field)))
        rate = filled / n
        ok = rate >= threshold
        fields[field] = {
            "filled": filled, "rate": round(rate, 3),
            "threshold": threshold, "sufficient": ok, "enables": purpose,
        }
        if not ok:
            (blocked if kind in ("locations", "industries") else degraded).append(
                {"field": field, "rate": round(rate, 3), "impact": purpose,
                 "criterion": kind})

    return {
        "total_leads": n,
        "fields": fields,
        "blocked_criteria": blocked,
        "degraded_checks": degraded,
        "enrichment_recommended": bool(blocked or degraded),
        # Leads missing at least one field that came back insufficient — not the
        # whole list. Quoting the total overstates the cost of enrichment on an
        # audience that is mostly complete.
        "leads_needing_enrichment": (
            sum(1 for ld in leads
                if any(not _norm(ld.get(d["field"])) for d in blocked + degraded))
            if (blocked or degraded) else 0),
    }


# ------------------------------------------------------- pass 2: adjudication

MIN_REASON_LEN = 12


def adjudicate(payload):
    """Apply the model's pass-2 overrides to a pass-1 result, and re-validate.

    The model may move any lead between buckets, but must justify each move.
    We re-run the same reconciliation as pass 1 so a semantic pass cannot
    silently drop someone — the exact failure mode the two-pass design exists
    to prevent.
    """
    if not isinstance(payload, dict):
        raise ValidationError("adjudication payload must be a JSON object")

    result = payload.get("result")
    if not isinstance(result, dict) or "buckets" not in result:
        raise ValidationError(
            "payload.result must be the output of a pass-1 run (with .buckets)")

    overrides = payload.get("overrides", [])
    if not isinstance(overrides, list):
        raise ValidationError("payload.overrides must be a list (use [] for none)")

    index = {}
    for b in BUCKETS:
        for row in result["buckets"].get(b, []):
            index[row["_key"]] = (b, row)
    original_total = len(index)
    if original_total == 0:
        raise ValidationError("pass-1 result contains no leads")

    audit, seen_keys = [], set()
    for i, ov in enumerate(overrides):
        if not isinstance(ov, dict):
            raise ValidationError(f"overrides[{i}] must be an object")
        key = str(ov.get("_key") or "").strip()
        if not key:
            raise ValidationError(f"overrides[{i}] is missing _key")
        if key in seen_keys:
            raise ValidationError(f"overrides[{i}]: duplicate override for {key!r}")
        if key not in index:
            raise ValidationError(
                f"overrides[{i}]: {key!r} is not a lead from the pass-1 result")
        new_bucket = str(ov.get("bucket") or "").strip()
        if new_bucket not in BUCKETS:
            raise ValidationError(
                f"overrides[{i}]: bucket {new_bucket!r} invalid. Valid: {list(BUCKETS)}")
        reason = str(ov.get("reason") or "").strip()
        if len(reason) < MIN_REASON_LEN:
            raise ValidationError(
                f"overrides[{i}]: every override needs a substantive reason "
                f"(at least {MIN_REASON_LEN} chars) — an unexplained "
                "reclassification is not auditable")
        seen_keys.add(key)

        old_bucket, row = index[key]
        if old_bucket != new_bucket:
            audit.append({
                "_key": key, "from": old_bucket, "to": new_bucket,
                "pass1_reason": row.get("_reason"), "pass2_reason": reason,
            })
        row = dict(row)
        row["_bucket"] = new_bucket
        row["_reason"] = reason
        row["_pass1_bucket"] = old_bucket
        index[key] = (new_bucket, row)

    final = {b: [] for b in BUCKETS}
    for key, (bucket, row) in index.items():
        final[bucket].append(row)

    flat = [r for b in BUCKETS for r in final[b]]
    if len(flat) != original_total:
        raise ValidationError(
            f"adjudication lost leads: {original_total} in, {len(flat)} out")
    validate_result(flat, final)

    return {
        "pass": 2,
        "adjudicated": True,
        "counts": {b: len(final[b]) for b in BUCKETS} | {"total": original_total},
        "changes": audit,
        "buckets": final,
    }


# -------------------------------------------------------------------- self-test

def _selftest():
    tax = _load_taxonomy()
    icp = {
        "seniority": ["founder_c", "vp_head", "manager_lead"],
        "functions": ["sales", "growth_marketing", "revops"],
        "founder_qualifies_regardless_of_function": False,
    }
    excl = {"domains": ["northwindlabs.com"], "companies": ["Northwind Labs", "NWL"],
            "keywords": ["coldmails"]}

    cases = [
        # (lead, expected_bucket, note)
        ({"leadId": "1", "jobTitle": "Client Partner", "companyName": "",
          "proEmail": "", "shortBio": "Client Partner @ NWL"},
         "excluded", "empty company + empty email, only the bio reveals NWL"),
        ({"leadId": "1b", "jobTitle": "Client Partner", "companyName": "",
          "proEmail": "", "shortBio": "Client Partner @NorthwindLabs"},
         "excluded", "collapsed spelling: @NorthwindLabs vs 'Northwind Labs'"),
        ({"leadId": "1c", "jobTitle": "Growth Lead", "companyName": "northwind-labs"},
         "excluded", "hyphenated spelling"),
        ({"leadId": "2", "jobTitle": "Client Account Executive",
          "companyName": "Vantage Digital", "proEmail": "j.moreau@northwindlabs.com"},
         "excluded", "job-changer: stale company, current email"),
        ({"leadId": "2b", "jobTitle": "Head of Sales", "companyName": "Algomo"},
         "match", "must NOT trip the short-token 'nwl' exclusion"),
        ({"leadId": "3", "jobTitle": "Founding Member", "companyName": "Coldmails.ai"},
         "excluded", "competitor by keyword"),
        ({"leadId": "4", "jobTitle": "Head of Global Business Development",
          "companyName": "TBCASoft"}, "match", "vp_head + sales"),
        ({"leadId": "5", "jobTitle": "Revenue Systems & Operations Lead",
          "companyName": "Doormate"}, "match", "manager_lead + revops"),
        ({"leadId": "6", "jobTitle": "Account Executive", "companyName": "Calderon"},
         "no_match", "IC not in ICP"),
        ({"leadId": "7", "jobTitle": "Chief Technology Officer", "companyName": "Narrio"},
         "no_match", "C-level but product/tech function"),
        ({"leadId": "8", "jobTitle": "Co-Founder", "companyName": "Concourse"},
         "review", "founder with no stated function, founder_qualifies=False"),
        ({"leadId": "9", "jobTitle": "", "companyName": "Smartelia"},
         "review", "no title at all"),
        ({"leadId": "10", "jobTitle": "Venture Scout", "companyName": "Bouken Capital"},
         "no_match", "noise title"),
        ({"leadId": "11", "jobTitle": "General Manager of Sales and Marketing",
          "companyName": "20Cube"}, "match", "vp_head + sales/marketing"),
        ({"leadId": "12", "jobTitle": "Managing Director", "companyName": "Acme",
          "shortBio": "Développement commercial B2B"},
         "match", "function comes from bio, not the title"),
        ({"leadId": "13", "jobTitle": "Principal", "companyName": "Acme",
          "shortBio": "Woodworking hobbyist and dad of three"},
         "review", "bio has no function signal either — stays in review"),
    ]

    failures = 0
    for lead, expected, note in cases:
        got, reason = classify(lead, icp, excl, tax)
        if got != expected:
            failures += 1
            print(f"FAIL [{note}] expected={expected} got={got} ({reason})",
                  file=sys.stderr)

    # founder toggle flips case 8 to match
    icp_f = dict(icp, founder_qualifies_regardless_of_function=True)
    got, _ = classify({"leadId": "8", "jobTitle": "Co-Founder",
                       "companyName": "Concourse"}, icp_f, excl, tax)
    total = len(cases) + 1
    if got != "match":
        failures += 1
        print(f"FAIL [founder toggle] expected=match got={got}", file=sys.stderr)

    # bad specs must be refused, not best-efforted
    bad_specs = [
        ({"icp": icp}, "missing leads"),
        ({"icp": {"seniority": ["cxo"], "functions": ["sales"]},
          "leads": [{"leadId": "x"}]}, "unknown seniority tier"),
        ({"icp": icp, "leads": [{"jobTitle": "CEO"}]}, "lead with no identifier"),
        ({"icp": icp, "leads": []}, "empty lead list"),
    ]
    for spec, note in bad_specs:
        total += 1
        try:
            build(spec)
            failures += 1
            print(f"FAIL [{note}] should have raised ValidationError", file=sys.stderr)
        except ValidationError:
            pass

    # reconciliation: every lead lands in exactly one bucket
    total += 1
    out = build({"icp": icp, "exclusions": excl,
                 "leads": [c[0] for c in cases]})
    if out["counts"]["total"] != len(cases) or \
       sum(out["counts"][b] for b in BUCKETS) != len(cases):
        failures += 1
        print("FAIL [reconciliation] counts do not add up", file=sys.stderr)

    # --- industry synonym expansion: 'saas' must catch a LinkedIn-labelled variant ---
    icp_saas = {"seniority": ["founder_c", "vp_head"], "functions": ["growth_marketing"],
                "founder_qualifies_regardless_of_function": False, "industries": ["saas"]}
    total += 1
    got, reason = classify(
        {"leadId": "s1", "jobTitle": "Head of Marketing", "companyName": "Implicity",
         "industry": "Technology, Information and Internet"},
        {**icp_saas, "industries": expand_industries(icp_saas["industries"], tax)}, {}, tax)
    if got != "match":
        failures += 1
        print(f"FAIL [industry synonym] expected match got {got} ({reason})", file=sys.stderr)

    # a genuinely off-industry lead still drops
    total += 1
    got, _ = classify(
        {"leadId": "s2", "jobTitle": "Head of Marketing", "companyName": "TotalEnergies",
         "industry": "Oil and Gas"},
        {**icp_saas, "industries": expand_industries(icp_saas["industries"], tax)}, {}, tax)
    if got != "no_match":
        failures += 1
        print(f"FAIL [off-industry] expected no_match got {got}", file=sys.stderr)

    # --- pass2_queue is bounded: only ambiguous / risky / soft-drops, not everything ---
    total += 1
    qout = build({"icp": {**icp_saas, "industries": ["saas"]}, "exclusions": {}, "leads": [
        {"leadId": "q1", "jobTitle": "Head of Marketing", "companyName": "Acme",
         "industry": "Software Development"},                       # clean match, NOT queued
        {"leadId": "q2", "jobTitle": "Head of Marketing", "companyName": "Freelance Studio",
         "industry": "Software Development", "shortBio": "Freelance CMO / consultant"},  # agency match → queued
        {"leadId": "q3", "jobTitle": "Head of Marketing", "companyName": "EnergyCo",
         "industry": "Renewables & Environment"},                   # dropped on industry → queued
        {"leadId": "q4", "jobTitle": "Software Engineer", "companyName": "Acme",
         "industry": "Software Development"},                       # dropped on FUNCTION → NOT queued
    ]})
    qkeys = {r["_key"] for r in qout["pass2_queue"]}
    if qkeys != {"q2", "q3"} or qout["pass2_queue_size"] != 2:
        failures += 1
        print(f"FAIL [pass2_queue] expected {{q2,q3}} got {qkeys}", file=sys.stderr)

    # --- pass 2: the semantic failures regex cannot see ---
    # 'Chief Happiness Officer' matches the C-level pattern but is an HR role.
    # Pass 1 must call it a match; pass 2 must be able to correct it.
    icp_f = dict(icp, founder_qualifies_regardless_of_function=True)
    total += 1
    got, _ = classify({"leadId": "hr1", "jobTitle": "Chief Happiness Officer"},
                      icp_f, excl, tax)
    if got != "match":
        failures += 1
        print(f"FAIL [pass1 baseline] expected match got {got}", file=sys.stderr)

    p1 = build({"icp": icp_f, "exclusions": excl, "leads": [
        {"leadId": "hr1", "jobTitle": "Chief Happiness Officer"},
        {"leadId": "ok1", "jobTitle": "Head of Sales", "companyName": "Acme"},
    ]})

    total += 1
    adj = adjudicate({"result": p1, "overrides": [
        {"_key": "hr1", "bucket": "no_match",
         "reason": "Chief Happiness Officer is an HR role, not a GTM buyer"},
    ]})
    if adj["counts"]["match"] != 1 or adj["counts"]["no_match"] != 1 \
       or len(adj["changes"]) != 1 or adj["counts"]["total"] != 2:
        failures += 1
        print(f"FAIL [adjudicate] bad result: {adj['counts']}", file=sys.stderr)

    bad_adj = [
        ({"result": p1, "overrides": [{"_key": "ghost", "bucket": "match",
                                       "reason": "this lead does not exist"}]},
         "override on an unknown lead"),
        ({"result": p1, "overrides": [{"_key": "hr1", "bucket": "nope",
                                       "reason": "invalid bucket name here"}]},
         "invalid bucket"),
        ({"result": p1, "overrides": [{"_key": "hr1", "bucket": "no_match",
                                       "reason": "hr"}]},
         "reason too short to be auditable"),
        ({"result": p1, "overrides": [
            {"_key": "hr1", "bucket": "no_match", "reason": "HR role, not a buyer"},
            {"_key": "hr1", "bucket": "match", "reason": "contradictory duplicate"}]},
         "duplicate override for the same lead"),
        ({"overrides": []}, "missing pass-1 result"),
    ]
    for payload, note in bad_adj:
        total += 1
        try:
            adjudicate(payload)
            failures += 1
            print(f"FAIL [{note}] should have raised ValidationError", file=sys.stderr)
        except ValidationError:
            pass

    # --- coverage gate ---
    rich = [{"leadId": str(i), "jobTitle": "Head of Sales", "companyName": "Acme",
             "proEmail": "a@acme.com", "shortBio": "Sales leader",
             "location": "Paris", "industry": "SaaS"} for i in range(10)]
    total += 1
    cov = coverage({"leads": rich})
    if cov["enrichment_recommended"] or cov["blocked_criteria"]:
        failures += 1
        print("FAIL [coverage] complete data flagged as needing enrichment",
              file=sys.stderr)

    thin = [{"leadId": str(i), "jobTitle": "Head of Sales", "companyName": "Acme"}
            for i in range(10)]
    total += 1
    cov = coverage({"leads": thin})
    blocked = {b["field"] for b in cov["blocked_criteria"]}
    if blocked != {"location", "industry"} or not cov["enrichment_recommended"] \
       or cov["leads_needing_enrichment"] != 10:
        failures += 1
        print(f"FAIL [coverage] thin data misreported: {cov}", file=sys.stderr)

    total += 1
    try:
        coverage({"leads": []})
        failures += 1
        print("FAIL [coverage] empty list should raise", file=sys.stderr)
    except ValidationError:
        pass

    # --- regression: short acronyms must not match common words -------------
    # `\bIT\b` under re.IGNORECASE matched the English pronoun, so a bio
    # reading "making it happen" scored as product_tech and the lead left the
    # ICP silently — with function-based drops absent from pass2_queue, nothing
    # surfaced it. Both halves are covered here.
    acro_icp = {"seniority": ["founder_c", "vp_head", "manager_lead"],
                "functions": ["sales", "growth_marketing", "revops"],
                "founder_qualifies_regardless_of_function": False}
    acro_cases = [
        ({"leadId": "it1", "jobTitle": "Managing Director",
          "shortBio": "I love building teams and making it happen"},
         "review", "pronoun 'it' must not read as the IT function"),
        ({"leadId": "it2", "jobTitle": "Managing Director",
          "shortBio": "it is what it is"},
         "review", "repeated pronoun 'it' must not read as IT"),
        ({"leadId": "it3", "jobTitle": "Head of Sales",
          "shortBio": "we commit it weekly"},
         "match", "pronoun in bio must not override a clear title"),
    ]
    for lead, want, note in acro_cases:
        total += 1
        got, why = classify(lead, acro_icp, {}, _load_taxonomy())
        if got != want:
            failures += 1
            print(f"FAIL [{note}] expected={want} got={got} ({why})",
                  file=sys.stderr)

    # the acronym must still be detected when it is genuinely uppercase
    tech_icp = {"seniority": ["vp_head"], "functions": ["product_tech"],
                "founder_qualifies_regardless_of_function": False}
    for title, note in (("Head of IT", "uppercase IT still detected"),
                        ("Head of R&D", "uppercase R&D still detected")):
        total += 1
        got, why = classify({"leadId": "t", "jobTitle": title}, tech_icp, {},
                            _load_taxonomy())
        if got != "match":
            failures += 1
            print(f"FAIL [{note}] expected=match got={got} ({why})",
                  file=sys.stderr)

    # --- regression: a drop inferred from the bio must reach pass 2 ----------
    # Nothing may leave the ICP on a free-text inference without a second look.
    total += 1
    drop = build({"icp": {"seniority": ["vp_head"], "functions": ["sales"],
                          "founder_qualifies_regardless_of_function": False},
                  "exclusions": {},
                  "leads": [{"leadId": "d1", "jobTitle": "Head of Operations",
                             "shortBio": "I lead the product roadmap"}]})
    d1 = drop["buckets"]["no_match"]
    if not d1 or "_flag" not in d1[0] or drop["pass2_queue_size"] != 1:
        failures += 1
        print(f"FAIL [bio-inferred drop] not queued for pass 2: {drop['buckets']}",
              file=sys.stderr)

    # --- regression: enrichment count is rows missing a gated field ---------
    mixed = ([{"leadId": f"r{i}", "jobTitle": "Head of Sales",
               "companyName": "Acme", "proEmail": "a@acme.com",
               "shortBio": "Sales leader", "location": "Paris",
               "industry": "SaaS"} for i in range(7)]
             + [{"leadId": f"t{i}", "jobTitle": "Head of Sales",
                 "companyName": "Acme"} for i in range(3)])
    total += 1
    cov = coverage({"leads": mixed})
    if cov["leads_needing_enrichment"] != 3:
        failures += 1
        print("FAIL [coverage] enrichment count should be the rows actually "
              f"missing a gated field, got {cov['leads_needing_enrichment']}",
              file=sys.stderr)

    print(f"{total - failures}/{total} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Classify an audience against an ICP (two-pass).")
    p.add_argument("spec", nargs="?", help="path to JSON, or - for stdin")
    p.add_argument("--coverage", action="store_true",
                   help="step 0: report field fill rates before defining the ICP")
    p.add_argument("--adjudicate", action="store_true",
                   help="pass 2: apply and re-validate the model's overrides")
    p.add_argument("--test", action="store_true", help="run the self-test")
    a = p.parse_args()

    if a.test:
        sys.exit(_selftest())
    if not a.spec:
        p.error("provide a JSON file, - for stdin, or --test")

    raw = sys.stdin.read() if a.spec == "-" else open(a.spec, encoding="utf-8").read()
    try:
        payload = json.loads(raw)
        if a.coverage:
            out = coverage(payload)
        elif a.adjudicate:
            out = adjudicate(payload)
        else:
            out = build(payload)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    except ValidationError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
