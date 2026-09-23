#!/usr/bin/env python3
"""Turn a Pavilion session export (CSV) into the three tiers the skill reads.

usage: python3 scripts/build_event.py data/gtm2026-sessions.csv references/events/gtm2026

Writes into the output folder:
  event.md     tier 1 — facts, chips, chip → session ids (always read)
  day-*.md     tier 2 — one line per session, grouped by start time (read per day attending)
  sessions.md  tier 3 — one `## <id>` section per session with description, speakers, bios, URL (read per shortlisted id)
Re-run whenever the agenda changes. Never hand-edit the generated files; edit OVERRIDES / KEYWORDS here.
"""
import csv, re, sys, collections, datetime, os

SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

# --- interest chips ---------------------------------------------------------
CHIPS = [
    ("ai_gtm",       "AI-GTM transformation",  ["ai", "agent", "agentic", "automation", "automate", "llm", "genai", "generative", "revenue per employee", "ai-native", "copilot"]),
    ("pipeline",     "Pipeline & forecasting", ["pipeline", "forecast", "quota", "outbound", "prospect", "sdr", "bdr", "win rate", "deal", "closing", "sales cycle", "seller", "sales team", "cro"]),
    ("category",     "Category & positioning", ["category", "positioning", "narrative", "differentiat", "chasm", "market leader", "moat", "story"]),
    ("brand_demand", "Brand vs demand",        ["brand", "demand", "marketing", "cmo", "content", "seo", "be found", "search", "campaign", "abm", "awareness"]),
    ("customer_led", "Customer-led growth",    ["customer", "retention", "expansion", "churn", "success", "community", "nrr", "renewal", "post-sale", "onboarding"]),
    ("revops",       "RevOps & the stack",     ["revops", "rev ops", "operations", "attribution", "stack", "tooling", "crm", "data", "systems", "territor", "comp plan", "compensation", "instrument"]),
    ("leading",      "Leading the GTM org",    ["leader", "leadership", "board", "ceo", "culture", "hiring", "org", "alignment", "align", "team", "exec", "founder", "manage", "people"]),
]
TRACK_CHIPS = {"CRO Circle": ["pipeline", "leading"], "CMO Circle": ["brand_demand"], "RevOps Circle": ["revops"], "CEO Circle": ["leading"]}
OVERRIDES = {  # session id -> chip ids (replaces keyword result). Reviewed by hand.
    "439539": ["category", "leading"],          # Geoff Moore fireside
    "439560": ["leading", "customer_led"],      # Nick Mehta fireside
    "439542": ["ai_gtm", "leading", "pipeline"],# Amos Bar-Joseph — AIxGTM transformation
}
PUBLIC_AGENDA = "https://www.accelevents.com/e/gtm2026"  # the only human-readable official agenda URL
LOGISTIC_TYPES = {"Break", "Networking", "Other"}  # Expo = Spotlight Stage talks: short, real sessions

def chips_for(r):
    sid = r["Session ID"]
    if sid in OVERRIDES:
        r["_scores"] = {c: 99 - i for i, c in enumerate(OVERRIDES[sid])}; return OVERRIDES[sid]
    if r["Session type"] in LOGISTIC_TYPES: return []
    text = " ".join([r["Session title"], r["Short summary"], r["Full description"]]).lower()
    scores = {}
    for cid, _, kws in CHIPS:
        s = sum(text.count(k) for k in kws)
        if cid == "ai_gtm" and re.search(r"\bai\b", text): s += 2
        if s: scores[cid] = s
    for t, cs in TRACK_CHIPS.items():
        if t in r["Track"]:
            for c in cs: scores[c] = scores.get(c, 0) + 2
    ranked = sorted(scores, key=lambda c: -scores[c])
    if not ranked and r["Session type"] == "Keynote Session": ranked = ["leading"]
    r["_scores"] = scores
    return ranked[:3]

def speakers(r):
    out = []
    for line in r["Speakers (name; role; company)"].split("\n"):
        parts = [p.strip() for p in line.split(";")]
        if parts and parts[0]:
            name = parts[0]; role = parts[1] if len(parts) > 1 else ""; co = parts[2] if len(parts) > 2 else ""
            out.append((name, role, co))
    return out

def linkedin(r):
    out = {}
    for line in r["Speaker LinkedIn profiles"].split("\n"):
        if ":" in line:
            n, u = line.split(":", 1); out[n.strip()] = u.strip()
    return out

def bios(r):
    """Bios are multi-paragraph and contain colons; a new entry starts only when the prefix is a known speaker name."""
    names = {n for n, _, _ in speakers(r)}
    b, cur = {}, None
    for line in r["Speaker biographies"].split("\n"):
        if ":" in line and line.split(":", 1)[0].strip() in names:
            cur, t = line.split(":", 1); cur = cur.strip(); b[cur] = t.strip()
        elif cur and line.strip():
            b[cur] += "\n  " + line.strip()
    return b

rows = list(csv.DictReader(open(SRC, encoding="utf-8-sig")))
COLS = list(rows[0].keys())

# --- source 2: Circles day guide (pavilion-circles-day-guide.netlify.app, Sep 23 2026) --------
# The organizer's guide is more complete than the Accelevents export for Tuesday (missing speakers,
# missing opening keynotes). Its rows REPLACE every Tuesday row of the export. Bios + LinkedIn are
# carried over from the export by speaker name.
GUIDE = os.path.join(os.path.dirname(SRC), "gtm2026-circles-guide.csv")
if os.path.exists(GUIDE):
    bio_by_name, li_by_name = {}, {}
    for r in rows:
        for n, u in (l.split(":", 1) for l in r["Speaker LinkedIn profiles"].split("\n") if ":" in l): li_by_name[n.strip()] = u.strip()
        names = {p.split(";")[0].strip() for p in r["Speakers (name; role; company)"].split("\n") if p.strip()}
        cur, local = None, {}
        for line in r["Speaker biographies"].split("\n"):
            if ":" in line and line.split(":", 1)[0].strip() in names:
                cur, t = line.split(":", 1); cur = cur.strip(); local[cur] = t.strip()
            elif cur and line.strip():
                local[cur] += "\n" + line.strip()
        for n, t in local.items():
            if len(t) > len(bio_by_name.get(n, "")): bio_by_name[n] = t
    guide = list(csv.DictReader(open(GUIDE, encoding="utf-8-sig")))
    gdates = {g["Date"] for g in guide}
    rows = [r for r in rows if r["Date"] not in gdates]
    for g in guide:
        r = {c: "" for c in COLS}; r.update(g)
        names = [p.split(";")[0].strip() for p in g["Speakers (name; role; company)"].split("\n") if p.strip()]
        r["Speaker LinkedIn profiles"] = "\n".join(f"{n}: {li_by_name[n]}" for n in names if n in li_by_name)
        r["Speaker biographies"] = "\n".join(f"{n}: {bio_by_name[n]}" for n in names if n in bio_by_name)
        r["Description status"] = "From organizer Circles guide" if g["Full description"].strip() else "No description published"
        r["Timezone"] = "EDT"; r["Scraped at (UTC)"] = rows[0]["Scraped at (UTC)"]
        rows.append(r)

# --- source 3: organizer's Wed/Thu agenda sheet (data/gtm2026-organizer-days.csv, Sep 23 2026) -----
# Hand-reconciled against the export; only the differences are patched here. Reviewed by hand.
PATCHES = {
    "439510": {"Session title": "The Decade Ahead — Welcome Remarks & Keynote"},
    "439562": {"Start time (EDT)": "16:50", "Session title": "Day 1 Close & A Moment of Appreciation"},
    "439561": {"Start time (EDT)": "16:15", "End time (EDT)": "16:45"},
    "439556": {"End time (EDT)": "15:55", "Session title": "Closing Remarks"},
    "439539": {"Session title": "Geoff Moore Fireside Chat w/ Sam Jacobs",
               "Speakers (name; role; company)": "Geoff Moore; Author, Crossing the Chasm; \nSam Jacobs; CEO; Pavilion",
               "Notes": "Geoff Moore confirmed as speaker on the organizer sheet."},
    "439538": {"Speakers (name; role; company)": "Mike Hoffman; Chief Revenue Officer, Pavilion NYC Co-Chapter Head; WAE\nAndrea Kayal; Chief Revenue Officer, Pavilion NYC Co-Chapter Head; Help Scout"},
    "439560": {"Speakers (name; role; company)": "Nick Mehta; EIR at Bessemer Venture Partners, former CEO & Co-Founder; Gainsight\nSam Jacobs; CEO; Pavilion"},
    "439523": {"Notes": "Organizer sheet lists this in Breakout 1 at 14:15 alongside 'PE/VC and the AI Use Cases'; the export says Breakout 2. Room unconfirmed — check signage."},
    "439520": {"Notes": "Organizer sheet lists this talk at both 14:15 and 15:30 in Breakout 2; the export says 15:30 only. Treat 15:30 as the real slot."},
}
for r in rows:
    if r["Session ID"] in PATCHES: r.update(PATCHES[r["Session ID"]])
rows.sort(key=lambda r: (r["Date"], r["Start time (EDT)"], r["End time (EDT)"], r["Room"]))
for r in rows: r["_chips"] = chips_for(r)

dates = sorted({r["Date"] for r in rows})
def dlabel(d):
    dt = datetime.date.fromisoformat(d); return dt.strftime("%a %b %-d")
DAY_FILE = {d: "day-" + datetime.date.fromisoformat(d).strftime("%a").lower() + ".md" for d in dates}
scraped = rows[0]["Scraped at (UTC)"][:15]

# --- tier 2: day files ------------------------------------------------------
for d in dates:
    day = [r for r in rows if r["Date"] == d]
    tracks = sorted({t for r in day for t in r["Track"].split(" | ")})
    lines = [f"# {dlabel(d)} — {' · '.join(tracks)}", "",
             "Format: `id · room · title · type · first speaker (company) · [chips]`. A slot with several rows = pick one. Rows tagged `[buffer]` are breaks, meals, expo floor time. Spotlight Stage talks are 15–20 min vendor sessions that overlap breaks — good fillers, rarely anchors.", ""]
    groups = [(k, list(g)) for k, g in __import__("itertools").groupby(day, key=lambda r: (r["Start time (EDT)"], r["End time (EDT)"]))]
    for track in (tracks if len(tracks) > 1 and "Circle" in tracks[0] else [None]):
        if track: lines += [f"## {track}", ""]
        for (st, en), g in groups:
            g = [r for r in g if track is None or track in r["Track"]]
            if not g: continue
            hdr = f"### {st}–{en}" + (" · pick one" if len([x for x in g if x['Session type'] not in LOGISTIC_TYPES and x['Session type'] != 'Expo']) > 1 else "")
            lines.append(hdr)
            for r in g:
                sp = speakers(r); s0 = f"{sp[0][0]} ({sp[0][2]})" if sp and sp[0][2] else (sp[0][0] if sp else "—")
                ttype = ("Spotlight 15–20 min" if r["Session type"] == "Expo" else "Circle" if "Circle" in r["Track"] and r["Session type"] not in LOGISTIC_TYPES else "Talk" if r["Session type"] == "Regular Session" else r["Session type"].replace(" Session", ""))
                title = r["Session title"].replace("Spotlight Stage Session: ", "").replace(" · ", " — ").strip()
                lines.append(f"- {r['Session ID']} · {r['Room']} · {title} · {ttype} · {s0} · [{' '.join(r['_chips']) or 'buffer'}]")
            lines.append("")
    open(os.path.join(OUT, DAY_FILE[d]), "w").write("\n".join(lines))

# --- tier 3: sessions.md ----------------------------------------------------
S = ["# Sessions — detail cards", "", f"One `## <id>` per session, complete: times, room, description status, summary, full description, every speaker with role, company, LinkedIn and full bio, `Page:` (the URL to link — the public agenda or the Circles guide page) and, where it exists, `Data:` (the JSON endpoint the card was built from; never link it). Jump to an id; never read top to bottom. Export scraped {scraped}; Tuesday ids `cg-*` come from the organizer Circles guide (Sep 23 2026).", ""]
for r in rows:
    S.append(f"## {r['Session ID']} · {r['Session title']}")
    S.append(f"{dlabel(r['Date'])} · {r['Start time (EDT)']}–{r['End time (EDT)']} EDT · {r['Room']} · {r['Track']} · {r['Session type']} · chips: {', '.join(r['_chips']) or '—'}")
    src = r['Source URL']
    if 'apiro.accelevents.com' in src:
        S.append(f"Page: {PUBLIC_AGENDA}  (public agenda; Accelevents publishes no per-session page — link this)")
        S.append(f"Data: {src}  (JSON endpoint used to build this card — never link it in the plan)")
    else:
        S.append(f"Page: {src}")
    S.append(f"Description status: {r['Description status']}" + (f" · Note: {r['Notes'].strip()}" if r["Notes"].strip() else ""))
    if r["Short summary"].strip(): S.append(""); S.append("Summary: " + r["Short summary"].strip())
    if r["Full description"].strip(): S.append(""); S.append(r["Full description"].strip())
    sp = speakers(r); b = bios(r); li = linkedin(r)
    if sp:
        S.append(""); S.append("Speakers:")
        for n, ro, co in sp:
            bio = b.get(n, "")
            bio = "" if bio.lower().startswith("not published") else bio
            url = li.get(n, "")
            S.append(f"- **{n}**" + (f" — {', '.join(x for x in (ro, co) if x)}" if (ro or co) else "") + (f" · {url}" if url and "linkedin" in url.lower() else "") + (f"\n  {bio}" if bio else ""))
    if r["Participants named in title"].strip(): S.append(f"Named in title (no speaker profile): {r['Participants named in title'].strip()}")
    S.append("")
open(os.path.join(OUT, "sessions.md"), "w").write("\n".join(S))

# --- tier 1: event.md -------------------------------------------------------
by_chip = collections.defaultdict(list)
for r in rows:
    for i, c in enumerate(r["_chips"]): by_chip[c].append((i, r))
E = ["# GTM2026 — event file (tier 1, always read)", "",
     f"Pavilion GTM Summit · {dlabel(dates[0])}–{dlabel(dates[-1])} 2026 · The Glasshouse, 660 12th Ave, Floor 6, New York · all times EDT",
     f"Data: {len(rows)} sessions. Sources: official Accelevents agenda export (scraped {scraped}) · organizer Circles day guide (pavilion-circles-day-guide.netlify.app, Sep 23 2026 — replaces all Tuesday rows) · organizer Wed/Thu agenda sheet (Sep 23 2026 — reconciled, differences patched). Re-run `scripts/build_event.py` to refresh; do not web-fetch the agenda unless the attendee asks or this file is older than 7 days.", "",
     "Venue, transport, hotels, tickets, sponsors, Circles and Women's Summit facts: `venue-and-logistics.md` (hand-maintained, read once per run).", "",
     "## Days", ""]
for d in dates:
    day = [r for r in rows if r["Date"] == d]; tracks = sorted({t for r in day for t in r["Track"].split(" | ")})
    E.append(f"- {dlabel(d)} · `{DAY_FILE[d]}` · {' · '.join(tracks)} · {len(day)} rows")
rooms_by_day = {d: sorted({r["Room"] for r in rows if r["Date"] == d and r["Session type"] not in LOGISTIC_TYPES}) for d in dates}
E += ["", "Rooms by day: " + " · ".join(f"{dlabel(d)}: {', '.join(rooms_by_day[d])}" for d in dates) + ". Tue Circles run in parallel across rooms — one track per attendee, VP+/CXO only, 100 seats (RevOps 65).", "",
      "## Interest chips (Stage 1, Q4 — pick up to three) and their sessions", "",
      "Ids are ranked: a session's first chip is its strongest fit. Read the id's card in `sessions.md` before recommending. Buffers (breaks, expo, networking) carry no chip.", ""]
for cid, label, _ in CHIPS:
    items = sorted(by_chip.get(cid, []), key=lambda x: (x[0], x[1]["Session type"] == "Expo", -x[1].get("_scores", {}).get(cid, 0), x[1]["Date"]))
    prim = [x for x in items if x[0] == 0]; sec = [x for x in items if x[0] > 0][:12]
    ids = ", ".join(f"{r['Session ID']}" + ("" if i == 0 else "°") for i, r in prim + sec)
    E.append(f"- **{cid}** · {label} · {ids}")
E += ["", "All primary fits listed, then up to 12 secondary fits marked °. `other` chip: grep `sessions.md` for the attendee's three words.", "",
      "## Role inference", "",
      "leading → CEO/founder · pipeline + revops → CRO · brand_demand + category → CMO · revops alone → RevOps. Role decides the Tuesday Circle; never assume a seat — tag `seat assumed` until confirmed.", "",
      "## Speaker on the program", "",
      "Swan bias applies at normal weight to: " + (", ".join(f"{r['Session ID']} ({dlabel(r['Date'])} {r['Start time (EDT)']}, {r['Room']})" for r in rows if any('Bar' in sp[0] and 'Joseph' in sp[0] for sp in speakers(r))) or "(no Amos Bar-Joseph session in this export)") + ". A normal candidate for its chips; never first-and-bold.", ""]
open(os.path.join(OUT, "event.md"), "w").write("\n".join(E))

print("wrote", OUT, {f: os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)})
