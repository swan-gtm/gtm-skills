# Source playbook — platforms, query patterns, fallbacks

How to sweep each candidate source: which platforms to use for which roles, how to construct queries, and what to do when a lane comes back empty.

## Platform selection

| Lane | Search where | Use for | Skip when |
|---|---|---|---|
| Professional network | Public professional-network profiles (e.g. `site:linkedin.com/in`) | Every role | Never — always run |
| Resume boards | Public resume/job-board pages (e.g. `site:indeed.com resume`) | Every role, strongest for mid-level and high-volume roles | Rarely useful for C-level |
| Code hosting | Developer profiles (e.g. `site:github.com`) | Engineering, data, DevOps, ML — any role where public code is a work sample | **Skip entirely for non-technical roles** (sales, marketing, ops, finance) and note the skip in the report header |
| Startup talent + communities | Startup-hiring platforms (e.g. `site:wellfound.com`) and open professional communities | Startup-profile roles, "open to work" discovery | Enterprise-only briefs |

Run all applicable lanes **in parallel** — one lane per search thread. Sequential sweeps double the runtime and tempt you to stop after the first lane looks "good enough".

## Query construction

Two queries per lane, always: one **site-scoped** (precision) and one **open-web** (recall). Fill from the confirmed brief.

**Professional network**

```
site:linkedin.com/in "[Role]" "[Location]" [Skill1] [Skill2]
"[Role]" "[Location]" linkedin profile [Skill1] [Skill2]
```

**Resume boards**

```
site:indeed.com resume "[Role]" "[Location]" [Skill1]
"[Role]" resume "[Location]" [Skill1] [Skill2]
```

**Code hosting** (technical roles only)

```
site:github.com "[Role]" "[Location]" [Skill1]
github [Skill1] [Skill2] developer "[Location]" "open to work"
```

**Startup talent + communities**

```
site:wellfound.com "[Role]" "[Location]" [Skill1]
"[Role]" "[Location]" ("open to work" OR "seeking opportunities") [Skill1]
```

Construction rules:

- Quote multi-word phrases (role titles, city names); leave single-word skills unquoted so stemming helps recall.
- 2–3 skills per query maximum. Stuffing five skills into one query returns only resume-keyword spam; run a second query with the other skills instead.
- For remote roles, replace the location term with `remote` plus the country/region constraint (`remote US`), and add the seniority word (`senior`, `staff`, `director`) to the role phrase — remote pools are too large to search without it.
- Availability phrases worth searching explicitly: `"open to work"`, `"seeking opportunities"`, `"available for"`, `"looking for my next"`. A hit on one of these is a first-class signal — record the phrase, the date if visible, and the URL.
- ~15 results for the primary lane (professional network), ~10 for the others. More than that per lane produces dedup work, not candidates.

## Structured search tools

If your stack includes a structured people-search or profile-extraction tool for any of these platforms, prefer it over open-web queries for that lane — feed it the role title, location, and skill keywords from the brief. Validate its output on the first run (does it return real, current profiles?) before trusting it for the whole sweep. Open-web search remains the fallback for any platform with no working structured tool.

## Fallback ladder

When a lane fails, degrade in this order — never silently return an empty lane:

1. **Zero results** → simplify: drop the least-important skill, then drop the location qualifier. Two simplification rounds max.
2. **Search errors** on a platform → retry once with a simplified query; if it still fails, skip the platform and state so in the report header.
3. **Profile behind a login wall** at extraction time → keep the search-snippet entry (name/title/location/skills as visible in the snippet), mark it "full profile unavailable — login required". Snippet-only candidates are scored like any other, on what is known.
4. **All lanes thin (<5 candidates total)** → this is a brief problem, not a search problem. Report the shortfall and propose one concrete broadening — location → remote first, seniority down one notch second — and wait for approval before re-running.

## Source-quality tiers

When the same person surfaces on multiple platforms, keep one entry and cite the richest source. Trust order for conflicting facts: the person's own current profile page > resume-board listing > community mention > search snippet. An availability signal is only as good as its date — an undated "open to work" from an unknown-age snippet is recorded as "date unknown", never assumed fresh.
