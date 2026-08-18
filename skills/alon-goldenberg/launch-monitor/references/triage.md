# Triage rubric — urgency, action badges, mischaracterization records

Apply to every signal, every run. A signal without all four labels (urgency, action, type, exact URL) is not done being triaged.

---

## Urgency levels

- 🔴 **Act now** — a mischaracterization going viral, high-reach negative coverage, a competitor counter-announcement, or a crisis-shaped signal. The team should see it today.
- 🟡 **Monitor** — an emerging negative theme, mid-reach inaccurate coverage, competitor positioning content. Track for escalation; no action yet.
- 🟢 **Good signal** — accurate positive coverage, organic enthusiasm, adoption signals. Candidates for amplification.
- ⬜ **Noise** — irrelevant mentions, same-name products, spam. Filtered by the materiality threshold below; never shown in the main feed.

Urgency is a function of **reach × wrongness × velocity**, not tone alone. A scathing post with 12 views is Monitor at most; a politely wrong claim in a high-reach outlet is Act now.

### Reach heuristics (when platforms don't publish numbers)

- Hacker News: 50+ comments = high priority; front page = treat as press-tier reach
- X: 100+ likes within 24h = meaningful; quote-posted by a journalist or known account = escalate a level
- Reddit: top-of-subreddit in a large sub, or 100+ upvotes = meaningful; comment depth signals real engagement over drive-by voting
- YouTube/TikTok: view velocity in the first 48h matters more than the absolute count
- Press: use the outlet's typical audience as a proxy; secondary pickup (another outlet citing the piece) is worth more than raw readership
- State reach as an estimate ("~50K readers", "front page of HN") and mark it unverified when you could not confirm it

---

## Action badges

- `RESPOND` — needs a direct public response: a reply in the thread, a comment, press outreach
- `CORRECT` — needs a correction or clarification: a DM, a comment, a note to the journalist
- `AMPLIFY` — worth sharing, reposting, or building on
- `ESCALATE` — belongs with comms, legal, or leadership — not with whoever is watching the feed
- `WATCH` — no action yet; track for escalation and name what would trigger it
- `IGNORE` — filtered noise (record it in the appendix, not the feed)

Every RESPOND/CORRECT badge must come with a *specific* suggested action — the actual sentence to post and where to post it. "Consider responding" is not an action. All suggested actions are drafts for a human to approve and send.

## Signal types

Press coverage · Community discussion · Social mention · Competitor move · Mischaracterization · Churn signal · Influencer take · Developer reaction · Analyst comment

---

## Source URL — required for every signal

Every signal carries the **exact URL** of the specific article, thread, or post, exactly as the search tool returned it.

Correct:
- `https://techcrunch.com/2026/06/11/example-product-launch`
- `https://news.ycombinator.com/item?id=12345678`
- `https://reddit.com/r/MachineLearning/comments/abc123/thread_title`
- `https://x.com/[username]/status/[POST_ID]`

Wrong — never use: `https://techcrunch.com`, `https://news.ycombinator.com`, `https://reddit.com`, `https://x.com`. A homepage link is useless to the reader, and a fabricated deep link is worse than no link — if you don't have the exact URL, say so on the card.

---

## Mischaracterization record — six fields, all required

For every piece of coverage that gets something wrong:

1. **The claim** — exactly what was said, quoted
2. **The source** — outlet, author, reach estimate, date
3. **What's wrong** — the specific inaccuracy, not a vibe
4. **The correct version** — the accurate statement, checkable against the announcement
5. **Spread risk** — search for secondary coverage citing the wrong claim before assigning this; "is being picked up" requires found evidence
6. **Suggested response** — a one-sentence, copy-ready correction

### Status badges

- `SPREADING` — found in 2+ independent sources, or being cited/quoted onward
- `CONTAINED` — single source, no secondary pickup found
- `CORRECTED` — the source amended it, or the correction is visibly winning in the thread

Status drives urgency more than the original outlet's size: a small blog's wrong claim that three other places are citing outranks a big outlet's wrong claim nobody repeated. A mischaracterization stays on the tracker across re-runs until its status is CORRECTED — carry it forward even when no new coverage mentions it.

---

## Materiality threshold

Skip entirely (don't triage, don't count):
- Clearly a different product with the same name (the context profile is the filter)
- Automated bots or spam accounts
- Duplicate coverage with no new information — syndicated wire copy counts once, at the original
- Single-digit reach with no amplification potential

Flag but don't prioritize:
- Neutral coverage that accurately describes the product
- Positive signals that need no action
