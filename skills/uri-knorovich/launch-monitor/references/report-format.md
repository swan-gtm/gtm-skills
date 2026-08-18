# Response war room — report format spec

One report shape, every run. Markdown, section order fixed. Tone: operational, terse, plain-language — a war room board, not a market-research essay. Name the outlet, the claim, the competitor; never "some coverage suggests".

Save each run as `launch-monitor-[YYYY-MM-DD].md` in the launch's workspace folder, next to the running memory file.

---

## Section order

### 0. Header block

```markdown
# Launch Monitor — [Product Name]
**Launch date:** [DATE]
**Monitored window:** [DATE RANGE]
**Generated:** [TIMESTAMP]
**Total signals:** [N]
**Dedup:** [X] net-new · [Y] returning (urgency changed) · [Z] suppressed
```

The dedup line is mandatory on every run after the first — it is the honesty line that tells the reader how much of this report is actually new.

### 1. TL;DR — always first

Two to three sentences: overall sentiment read (positive / mixed / negative / trending which way), count of act-now items, and the single most urgent signal or mischaracterization by name. Example: "Sentiment is mixed-to-negative in the first 48 hours, with 5 act-now items. The dominant risk is the '[wrong-framing]' claim spreading across HN and press. Three mischaracterizations are active, two spreading."

### 2. Attention summary

One bold line for scanners: **"[N] things need your attention right now —"** followed by the 2–3 most urgent items in plain language. Be specific: the outlet, the claim, the competitor move — not categories.

### 3. Coverage stats

One compact line or mini-table: All signals · Act now · Monitor · Good · Mischaracterizations · Competitor moves · Overall sentiment.

### 4. Sentiment velocity

A small table, intervals as rows (hourly for the first 24h, daily after):

```markdown
| Interval | Positive | Negative | Neutral | Top signal |
|---|---|---|---|---|
| Launch–6h | 4 | 1 | 2 | [headline] |
```

Below the table, two lines of reading: the inflection point (when sentiment peaked or flipped) and any velocity spike, with the likely cause.

### 5. Signal feed — the war room

Grouped by urgency, 🔴 first, then 🟡, then 🟢. Within a group, highest reach first. Per signal, this exact card shape:

```markdown
- **[RESPOND]** · [Signal type] · [Headline — what happened, in one line]
  Context: [One sentence — why it matters]
  Source: [outlet/platform] · [reach estimate] · [time since launch] · [exact URL]
  Action: [The specific suggested action — what to say, where to post it]
```

Rules: the URL is the exact article/thread/post URL (see the triage reference); the Action line on 🔴 cards must be executable in sixty seconds; 🟢 cards may compress Context and Action into one line. Returning signals whose urgency changed carry a `↩ returning · urgency changed` marker after the headline. Suppressed known signals do not appear here — appendix only, and only if the user asked for full history.

### 6. Mischaracterization tracker

Only render if mischaracterizations were found. One row per wrong claim, claim on the left, correction on the right:

```markdown
| The claim | Source · reach | Status | The correction | Suggested response |
|---|---|---|---|---|
| "[Exact wrong claim]" | [Outlet · author · ~reach] ([URL]) | SPREADING | [Accurate version] | "[One-sentence, copy-ready correction]" |
```

The suggested response is written to be pasted verbatim — quote it so the boundary is unambiguous. Carry unresolved rows forward from previous runs; a row leaves the tracker only at CORRECTED.

### 7. Competitor responses

Only render if competitor monitoring is enabled. One entry per competitor — including the silent ones:

```markdown
- **[Competitor]** — [what they did: published comparison, posted, counter-announced, stayed silent] ([URL if any])
  Urgency: [read] · Suggested counter-move: [specific move]
```

### 8. Source index

Flat list for auditability — every signal in the report, one line each: `[URL] · [source] · [date] · [urgency] · [action]`.

### 9. What this means — always last

Two to three sentences synthesizing what the signal pattern implies for the launch trajectory, ending with the single most important action for the team to take right now. This is the section an exec reads if they read nothing else — write it like a recommendation, not a summary.

---

## Tone and honesty rules

- Every number in the report was counted from found signals; every reach figure is sourced or marked as an estimate.
- Quotes are verbatim from the source, never paraphrased inside quotation marks.
- Empty sections are omitted, not filled — "no mischaracterizations found" is one line in the stats, not an empty table.
- No hedging filler ("it seems", "arguably") on act-now items — the card either earns 🔴 with evidence or it moves to 🟡.
