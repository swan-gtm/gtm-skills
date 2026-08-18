# Output format — the triage report

The output is a triage console, not an essay: dense, action-oriented, sorted by urgency. The tier badge is the primary label on every mention — the composite number supports it, never replaces it. Deliver the report in the conversation first; save a copy alongside the brand's memory file. If pushing to a team channel, send Crisis and Watch tiers only, never the full feed.

Sections in this exact order.

## 1. Header block

```markdown
# Brand mention monitor — [Brand]
**Window:** [start] – [end]   **Generated:** [timestamp]
**Total mentions:** [N]   **Depth:** [quick|deep]
**Dedup:** X net-new · Y returning (score changed) · Z suppressed (already logged)
```

The window is the one confirmed at setup — state it even when it was a default. The dedup line is mandatory on every run after the first.

## 2. TL;DR

2–4 lines: total mentions, the tier breakdown (`X Crisis · Y Watch · Z Engage`), and the single most urgent item with its response window. A reader who stops here must still know whether anything is on fire.

## 3. Sources searched

A short table of every source group queried this run with mention counts — and an explicit note for any stream that failed or was skipped. This is the honesty panel: the reader must be able to see what the sweep did and did not cover.

| Source | Searched | Mentions |
|---|---|---|
| Reddit | yes | 14 |
| LinkedIn | yes | 6 |
| TikTok | skipped — low signal for this profile | — |

## 4. Score summary

One line of aggregates: average reach, top velocity (with its arrow), top sentiment risk, top opportunity. Fast context for how hot the window was overall.

## 5. Share of voice (when competitors are tracked)

The brand's share of the conversation vs each tracked competitor in this window. One row per brand, user's brand first, percentages summing to ~100 with an "Other" bucket:

| Brand | Share | Mentions | Trend vs last window | Sentiment (+/0/-) | Signal |
|---|---|---|---|---|---|
| [Brand] | 42% | 87 | ↑ +6pts | 55/30/15 | [one line on what's driving the share] |

The Signal column is the analysis — one line per brand explaining what is driving its share (a launch, a complaint cluster, a viral post). Omit the section entirely when no competitors are tracked; never pad it with guesses.

## 6. Crisis alert cards — respond within 2 hours

Full-width treatment, before everything else in the feed. One card per Crisis mention:

```markdown
### 🔴 CRISIS — [Platform] · [Author] · [published date]
**Scores:** composite [N] · R:[N] V:[N] S:[N] RT:[N] · [↑ accelerating|→ stable|~estimated]
> "[Excerpt — the actual words, enough to judge tone]"
**Why flagged:** [the specific signals: risk topic hit, velocity, reach]
**Owner:** [who responds] · **Window:** < 2h
**Suggested action:** [a concrete draft move — requires human approval before anything is sent]
**Source:** [EXACT post/article URL]
```

## 7. Mention feed by tier

Then Watch (respond < 24h), Engage (act within 48h), and Log, in that order, each mention sorted by composite within its tier. Compact card format:

```markdown
- **[Tier] [composite]** · [Platform] · [Author] · [date] · R:[N] V:[N] S:[N] RT:[N] [velocity arrow]
  "[Excerpt]"
  Owner: [owner] · Window: [window] · Action: [suggested action]
  Source: [EXACT URL]
```

Returning mentions whose score shifted carry a `↩ returning · score changed` badge. Log entries can compress to one line each (tier, platform, excerpt fragment, URL) — they exist as a searchable record, not for reading.

## 8. Mentions by platform

A count-per-platform table so the reader sees where the conversation is concentrated. When mentions cluster geographically (a regional outage, a local press story), add a geographic breakdown: location, mention count, highest tier there, and the exact source links. Skip geography when it adds nothing.

## 9. What this means

The closing section, always present: what this window's sweep signals for the brand right now, then the top 1–3 recommended actions — each tied to a tier and an owner ("Watch item #2 → comms, draft a response today"). This is judgment, not a recap; it should read like the first paragraph of the note the marketing lead forwards.

## Source URL rule (applies to every line above)

Every mention links to the exact article, post, or thread URL as returned by the search — never a homepage, never a search-results page.

- CORRECT: `https://reddit.com/r/SaaS/comments/abc123/title`
- CORRECT: `https://x.com/username/status/1234567890`
- WRONG: `https://reddit.com` · WRONG: `https://x.com`

## Follow-ups to offer (only the relevant one)

- First run with no prior memory → suggest re-running in a few days to establish the velocity baseline and trends.
- Competitors framing the brand negatively in Watch/Crisis → offer a deeper competitor messaging and positioning analysis as a separate exercise.
- Mostly positive mentions → offer to turn the strongest ones into amplification or content angles.
