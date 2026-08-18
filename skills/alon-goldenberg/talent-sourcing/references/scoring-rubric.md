# Scoring rubric — weights, tiers, extraction budget

Score every candidate against the **confirmed brief**, not against whatever the search returned. The same profile can be a 9 for one brief and a 4 for another.

## Weighted score (1–10)

| Signal | Weight | What earns full marks |
|---|---|---|
| Role / title match | 30% | Current or most recent title is the target role or its direct feeder (e.g. "Staff Engineer" for a "Senior Engineer" brief) |
| Skill overlap | 30% | All must-have skills evidenced on the profile — listed AND backed by role history or work samples, not keyword-listed only |
| Location match | 20% | In the target metro, or explicitly remote-open for a remote brief |
| Seniority match | 10% | Years and scope line up with the brief's level — one notch either side scores partial |
| Availability signals | 10% | A dated "open to work"/"seeking" phrase, a job change in the last few months, or active job-search behavior — with source URL |

Scoring discipline:

- Score each dimension 0–10, multiply by weight, sum. Don't eyeball a single holistic number — the dimension scores are what make the ranking defensible when the hiring manager pushes back.
- **Evidence over keywords.** A skill listed in a profile's skill section with no supporting role or project scores half; a skill demonstrated in role descriptions or public work scores full.
- **Snippet-only candidates** (login-walled profiles) are scored on what the snippet shows; unknown dimensions score the midpoint (5), never zero and never full — and the entry says "scored from snippet".
- **Overqualified is a real score, not a bonus.** A VP applying to a senior-IC brief scores partial on seniority match — flag it, don't inflate it.

## Tiers

| Tier | Score | Meaning |
|---|---|---|
| **Tier 1 — Strong match** | 7–10 | All required signals present. Every entry gets a one-sentence "Why this candidate". |
| **Tier 2 — Partial match** | 4–6 | Most signals present, 1–2 gaps — name the gap explicitly in the entry (e.g. "no availability signal", "adjacent stack"). |
| **Tier 3 — Stretch** | 1–3 | Worth reviewing only if Tiers 1–2 are thin. Cap at 5 entries; a long Tier 3 is noise. |

Read the distribution as market data: a healthy brief yields roughly 3–6 Tier 1, 5–10 Tier 2. Near-empty Tier 1 with a heavy Tier 3 means the brief is over-constrained for this market — say that in "What this means" rather than quietly promoting 6s to Tier 1.

## Extraction budget

Deep-extract **at most 15 profiles** per run. When the lanes surface more than 15 unique candidates, triage before extracting using the three cheap dimensions visible in snippets — seniority match + skill overlap + location match — and extract the top 15 by that pre-score. Everyone else stays in the report as a snippet-level Tier 2/3 entry. Never extract in discovery order; the first results found are not the best results found.

## Worked example

Brief: **Senior ML Engineer, remote US, must-have PyTorch + production model serving, nice-to-have Kubernetes.**

Candidate A — "Staff ML Engineer" at a known AI company, profile shows PyTorch projects and a serving-infrastructure role, based in Austin, posted "open to new roles" two weeks ago (dated, with URL):
role 9 × .30 + skills 9 × .30 + location 10 × .20 + seniority 8 × .10 + availability 10 × .10 = **9.2 → Tier 1.** Why: exact stack with production evidence plus a fresh, dated availability signal.

Candidate B — "Data Scientist" listing PyTorch among 14 skills, no serving experience visible, NYC, no availability signal:
role 5 × .30 + skills 4 × .30 + location 10 × .20 + seniority 5 × .10 + availability 0 × .10 = **5.2 → Tier 2.** Gap to name: no production-serving evidence; PyTorch is keyword-only.

Candidate C — login-walled profile, snippet shows "ML Engineer • PyTorch • Kubernetes", location not visible:
role 8 × .30 + skills 7 × .30 + location 5 × .20 (unknown → midpoint) + seniority 5 × .10 + availability 5 × .10 = **6.5 → Tier 2**, marked "scored from snippet — full profile unavailable, login required". Kept, not dropped.
