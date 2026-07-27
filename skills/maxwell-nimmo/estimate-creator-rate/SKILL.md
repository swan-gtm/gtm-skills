---
name: "estimate-creator-rate"
title: Estimate creator rate
description: "Use this skill when you need to price a B2B LinkedIn thought-leadership creator from their real post performance. A weighted-engagement model cross-checked against a CPM anchor produces an initial / budget / max rate band to open a negotiation from."
category: Influencers
---

# Estimate Creator Rate

Price a B2B LinkedIn thought-leadership creator on what their content actually does, not on follower count. This skill turns a creator's recent post performance into an **initial / budget / max** rate band you can open a negotiation from, and works for a creator you know or a cold one you're pricing for the first time.

## Connectors for this skill

Optional. The skill runs entirely from pasted inputs, but will use these if available:
- **A LinkedIn or creator-analytics source** — to pull the creator's recent post metrics (impressions, likes, comments, reposts) automatically instead of by hand.
- **Your past-deal records / rate card** — to calibrate the model's weighting multiples from rates you've already closed.

If none are connected, gather the inputs manually in Step 0.

## Step 0 – Gather the inputs

Collect, asking the user for anything missing:
- The creator (LinkedIn profile, or their recent post metrics directly).
- The niche and the brand they'd be posting for.
- The deliverable: a single post, or a package (e.g. 3 posts).
- A representative sample of recent posts: average impressions, likes, comments, and reposts per post. Exclude obvious viral outliers and dead posts.

If the niche isn't given, use a general B2B CPM anchor and state the assumption. Niche changes the anchor, not the method.

## Step 1 – Weighted-engagement model (primary)

LinkedIn engagement is weighted by intent, not counted flat. A repost is a far stronger signal than a like:
- **Likes** = lowest weight
- **Comments** = middle weight
- **Reposts / shares** = highest weight

```
weighted engagement = (avg likes × W_like) + (avg comments × W_comment) + (avg reposts × W_repost)
```

Combine the weighted-engagement score with average impressions to produce three price points:
- **Initial** — where you open (leaves room to move).
- **Budget** — the number you expect to land at.
- **Max** — the ceiling you won't cross for this creator.

> **You set the multiples.** `W_like`, `W_comment`, `W_repost` and the mapping from (weighted score + impressions) to the band are yours to calibrate. Set them once, keep them consistent across creators, and document them. Back-solve from your own closed deals: find the multiples that reproduce rates you've already agreed.

**Principle: historical performance is the driver.** A smaller, perfectly on-ICP audience with strong comment/repost velocity outprices a large generalist. Follower count is context only.

## Step 2 – CPM anchor (cross-check)

```
implied rate = (avg impressions / 1000) × target CPM
```

Organic thought-leadership content prices at a premium to paid social CPMs. Pick a target CPM band for the niche and audience quality (set your own; B2B organic creator content commonly anchors in the tens-to-low-hundreds per 1,000 impressions).

> **You set the CPM bands.** Define a target CPM per niche (e.g. regulated/finance, technical/developer, marketing/GTM, general B2B) so the anchor reflects how much a relevant audience is worth to you.

Use the CPM-implied rate as the sanity check against Step 1. The engagement model leads for highly engaged niche creators; the CPM anchor leads for high-impression, low-engagement reach plays.

## Step 3 – Reconcile and recommend

State the initial / budget / max band, the CPM cross-check, and where to open. If the two methods disagree sharply, say which you trust and why rather than blindly averaging. Name the levers that move the number: single post vs package, content-usage / paid-ad rights, exclusivity, timeline, or a longer-term partnership.

## Output

```
CREATOR RATE ESTIMATE — [Creator], [niche], [brand]
Data: [N] recent posts

Avg impressions:      [X]
Weighted engagement:  (likes × W) + (comments × W) + (reposts × W) = [score]

RATE BAND (per [post / package])
  Initial (open here):  [ ]
  Budget (land here):   [ ]
  Max (ceiling):        [ ]

CPM cross-check:        [ ] implied at [target CPM]
Verdict:                [band holds / adjust because ...]
Levers:                 [package, usage rights, exclusivity, timeline]
```

Use the user's own currency throughout. This band is the anchor a negotiation works from and the basis a benchmark-setting exercise uses to translate rate into expected reach; keep it consistent across those uses.

## What good looks like

- The band is built on real post data, not follower count.
- Both methods were run; any divergence between them is explained, not averaged away.
- The opening number is defensible if the creator pushes back.
- If the multiples or CPM bands haven't been set yet, the output shows the structure, states clearly that the numbers are pending calibration, and stops. A labelled gap beats a fabricated rate.
