# Scoring rubric — four dimensions, composite, tiers

Score every mention 0–100 on each dimension, then compute the composite. Points come from evidence visible on the page (follower counts, reply counts, repost counts, domain, language) — never from guesses. When a value can't be verified, leave the points off and note it on the card.

## Reach / visibility (0–100) — how many people can see this?

| Signal | Points |
|---|---|
| 500K+ followers / major publication | +35 |
| 100K–500K followers | +25 |
| 10K–100K followers | +15 |
| 1K–10K followers | +8 |
| Under 1K followers | +3 |
| Thread with 100+ replies/comments | +20 |
| Post going viral (100+ reposts in under an hour) | +25 |
| High-authority domain (major wire or tech press) | +25 |
| Reddit front page / 1K+ upvotes | +25 |

## Velocity (0–100) — the differentiator

How fast is this gaining ground? Velocity separates "viral forming" from "stale," and it is the dimension most often faked. The honesty gate:

- **Hourly-rate rows require a baseline** — a prior engagement count and the current count. A single snapshot cannot yield a rate.
- **Re-run with prior data:** use the full table.
- **First-pass sweep (no baseline):** skip the hourly-rate rows; score only observable proxies. Label the velocity `~estimated` on the card so the reader knows it is inferred, not measured.

| Signal | Points | Needs baseline? |
|---|---|---|
| Engagement climbing 50%+/hour vs baseline | +40 | Yes |
| Engagement climbing 20–50%/hour | +25 | Yes |
| Engagement climbing 5–20%/hour | +10 | Yes |
| Flat engagement | +0 | Yes |
| Cross-platform pickup (same mention on 2+ platforms) | +20 | No |
| Press picking up a social post | +25 | No |
| Crisis-scale absolute engagement (thousands of reposts within the hour) | +40 | No — observable in one sweep |

**Rapid re-check upgrade:** when re-running within 2 hours of a prior run, re-fetch every mention that scored Watch or higher and compare engagement. Grown 20%+ → upgrade the tier and mark `↑ accelerating`. Otherwise mark `→ stable` or `↓ declining`. Every card carries one of these three arrows once a baseline exists.

## Sentiment (0–100 risk score; 0–100 opportunity score — scored separately)

| Negative signals (risk) | Points |
|---|---|
| Explicit negative sentiment | +20 |
| Complaint plus product/service failure language | +20 |
| Sarcasm ("great job [brand]…") | +15 |
| All-caps, exclamation marks, profanity | +10 |
| Replies amplifying the negative tone | +15 |

| Positive signals (opportunity) | Points |
|---|---|
| Organic, unprompted praise | +20 |
| Purchase intent or recommendation | +20 |
| User-generated content the brand could share | +15 |
| Journalist / analyst positive mention | +20 |

## Risk-topic match (0–100) — does this hit a flagged category?

Default dictionary below; add the industry-specific topics from the brand profile and any the user names.

| Topic category | Points |
|---|---|
| Legal / regulatory / lawsuit / class action | +40 |
| Safety / health / injury / recall | +40 |
| Executive misconduct or controversy | +35 |
| Product outage or critical failure | +30 |
| False claim / misinformation about the brand | +25 |
| Pricing / billing complaint (if spreading) | +20 |
| Competitor comparison framing the brand negatively | +15 |

## Composite

```
composite = (reach x 0.30) + (velocity x 0.30) + (max(risk_sentiment, risk_topic) x 0.25) + (opportunity x 0.15)
```

Risk takes the stronger of the two risk reads — a legally dangerous mention with mild wording still scores as dangerous.

## Tier thresholds

| Tier | Rule |
|---|---|
| Crisis | composite 80–100 |
| Watch | composite 50–79 |
| Engage | any composite, sentiment strongly positive and reach high — opportunity worth acting on |
| Log | composite under 50 with no risk signals |

Engage is not a consolation tier: it exists so high-reach praise gets amplified within 48 hours instead of rotting in a log. A mention can be Engage even with a modest composite when opportunity and reach are both strong.
