# Briefing and memory formats

The two output formats (full briefing, quick refresh), the workspace memory layout that makes dedup possible, and the run-mode windowing rules that decide between them.

## Run modes and date windowing

Decided from the profile's last-run date, before any searching:

| Last run | Mode | Search window |
|---|---|---|
| Never (first run) | **Full** | Past 14 days |
| More than 14 days ago | **Full** | Past 14 days |
| 3–14 days ago | **Quick refresh** | Since the last run date, but never narrower than 7 days |
| Under 3 days ago | **Quick refresh** | Past 7 days (the same floor — near-empty windows read as false quiet) |
| Today, and today's briefing exists | **Same-day repeat** | Ask before re-running; never silently duplicate |

Tune the 14-day boundary to the market's tempo — weekly for fast-moving spaces, monthly for slow ones — but keep the structure: a wide window with the full format, a narrow window with the delta format.

## Full briefing format

Sections in this order:

1. **TL;DR** — 3–5 P1 signals, most recent first. Every line: what happened, the verified event date, a clickable source link. If there are fewer than 3 genuine P1s, list fewer — never promote a P2 to fill space.
2. **Per competitor** (one section each):
   - **Recent** — NEW/UPDATED signals from this run, dated and sourced, P1s first.
   - **Older context** — 1–3 lines of standing context from memory (only what's needed to make Recent legible; this is the one place prior-run material may appear, clearly labeled as context, never as news).
   - **Where they win vs. where you win** — a short two-column table; honest on both sides.
   - **What this means** — 1–2 sentences of interpretation, not summary.
3. **Industry trends** — signals from the industry-keyword searches; only what's dated and real.
4. **Your company update** — releases and news from the own-company searches, so readers see both sides of the contrast.
5. **Cross-competitor patterns** — moves converging across 2+ competitors (everyone shipping the same feature category, hiring the same role, chasing the same segment). This section is often the most valuable and only exists because the research ran in parallel across all of them.
6. **What this means for [Company]** — strategic implications plus 2–4 suggested actions, each tied to a specific signal above.

Tone: terse, dated, sourced. Interpretation is welcome; padding is not. P3 signals get one line or nothing.

## Quick refresh format

Three sections, short by design:

1. **New signals** — each with competitor name, priority, event date, one-line description, clickable source URL.
2. **Nothing new** — explicit list of competitors with no validated new signals. Naming the quiet ones is what makes the reader trust the loud ones.
3. **Action items** — only if a signal genuinely demands attention; omit the section otherwise.

A quick refresh with one new signal and five quiet competitors is a successful run. Do not decorate it.

## Workspace memory layout

Keep everything in a dedicated directory in your workspace (never a shared or third-party location):

```
competitive-intel/
  profile.md               # company, competitor list (name/domain/category),
                           # industry keywords, preferences, last-run date
  competitors/
    <competitor-name>.md   # one running file per competitor — the dedup baseline
  briefings/
    briefing-<YYYY-MM-DD>.md
  competitive-landscape.md # synthesis page (see below)
```

### Per-competitor memory file

Append one entry per validated signal (NEW and UPDATED only — STALE/UNCERTAIN must never be written, or they poison every future dedup):

```
## [EVENT_DATE] — [SIGNAL one-liner]
- type: [news|product|funding|hiring|partnership|review]  priority: [P1|P2|P3]
- source: [URL]  ([SOURCE_TYPE])
- reported: [run date]
- notes: [optional 1–2 lines: corroboration found, what it updates, implications]
```

Keep a short header block at the top of each file (domain, category, one-line positioning, standing strengths/weaknesses) and update it only when a signal genuinely changes the picture. On each run, load these files first — the entries are the known-signals list passed to research threads.

### Saved briefings

Save the **full briefing text** to `briefings/`, not a summary — it is the local source of truth for "what did we already tell people," and the thing you diff against when someone asks what changed.

### Landscape synthesis

When a run researches 3+ competitors, or competitor files have changed since the synthesis was last generated, refresh `competitive-landscape.md` from all competitor files: a market map (who plays where), a feature comparison, a pricing comparison where known, key cross-competitor patterns, and strategic implications. Keep a short backlog list at the bottom for unanswered questions (competitors with unknown pricing, unverified funding) — these seed the next run's "go deeper" follow-ups.
