# Report format and role memory

The output contract for every sourcing run, plus the per-role memory that keeps repeat runs honest.

## Report structure

```
## Candidate Report: [Role] in [Location]
Searched: [platforms actually swept — name skips and failures here, e.g.
"code-hosting not searched for this role type", "resume boards skipped after repeated errors"]
Found: [N] candidates | Tier 1: [N] | Tier 2: [N] | Tier 3: [N]

**TL;DR:** [2–3 sentences: the strongest candidates by name, and any notable
pattern — e.g. "supply is thin outside two metros", "half of Tier 1 shows fresh
availability signals".]

---

### Tier 1 — Strong Match

#### 1. [Name] — [Score]/10
- **Current role:** [Title] at [Company]
- **Location:** [Location]
- **Skills:** [Skill1], [Skill2], [Skill3]
- **Experience:** [X years; notable employers]
- **Availability:** [signal phrase] — [date or "date unknown"] — [source URL]
- **Profile:** [URL]
- **Contact signals:** [email / personal site / code-hosting handle]
- **Why this candidate:** [one sentence — required for every Tier 1 entry]

[…remaining Tier 1, then "### Tier 2 — Partial Match" with the gap named per
entry, then "### Tier 3 — Stretch", max 5 entries…]

---

### What This Means
[1–2 sentences of hiring outlook: supply/demand read from the tier distribution,
a speed recommendation ("move fast — only 3 strong matches and 2 show active
availability"), and the standout sourcing channel for this role.]
```

## Formatting and honesty rules

- **Omit fields with no data rather than padding them** — except availability, which is always present as either a sourced signal or "no availability signal found".
- **"Unknown" is a valid value.** Never infer an email pattern, guess years of experience, or upgrade an undated availability snippet to "recent".
- **Snippet-only candidates** carry the line "full profile unavailable — login required; scored from snippet" so the reader knows the confidence level.
- **Every availability claim carries its source URL and date** (or "date unknown"). This is the field hiring managers act on first; it is also the easiest to accidentally fabricate.
- Tier 2 entries name their gap in one clause ("adjacent stack — Django not FastAPI"). A gap the reader can evaluate is useful; an unexplained middling score is not.
- The report is a research artifact: it never includes drafted outreach, and no candidate is contacted as part of producing it.

## Role memory — dedup across runs

Keep one running file per role in your workspace, named by role slug (e.g. `talent/senior-ml-engineer-remote-us.md`), plus a small index listing all roles searched with last-run dates.

**On every run, before presenting:**

1. Load the role's file (match by role + location; a materially changed brief — new location, different seniority — is a new slug, not an append).
2. Dedup candidates by profile URL first, then by name + current company.
3. Any candidate already in the file is marked `(previously surfaced — first seen [date])` in the report. They keep their tier and score but are never counted or narrated as a new find. If their situation visibly changed (new title, fresh availability signal), say what changed — that delta is the news.

**After presenting, write back:**

- Every candidate from this run: name, profile URL, score, tier, availability signal + date, first-seen date, last-seen date.
- A run header: date, brief as confirmed, platforms swept, tier counts.
- Update the index row for this role.

**Refresh runs.** When re-running an unchanged brief, the deliverable is the *diff*: lead with "New since [last run date]: N candidates", list the new ones in full, and compress previously-surfaced candidates to one line each unless something changed. A refresh that re-presents last week's list at full length is the signature failure of the mediocre version.

**Same-day repeat** (parameters tweaked minutes later): treat as a continuation — dedup against the earlier run silently, don't stamp "(previously surfaced)" on candidates from an hour ago, and overwrite the day's run header rather than appending a second one.
