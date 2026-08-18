# Dimension query patterns

One block per research dimension. Each thread runs its queries in parallel, keeps scope tight (roughly 4–5 searches per dimension), and returns findings as structured signals in this exact shape — one per signal, no commentary:

```
SIGNAL: [one-line description]
ARTICLE_DATE: [YYYY-MM-DD or ~YYYY-MM]
EVENT_DATE: [YYYY-MM-DD or ~YYYY-MM]
URL: [source url]
SOURCE_TYPE: [PRIMARY | MAJOR | DERIVATIVE]
TYPE: [one of the dimension's signal types below]
```

Dating and source-type rules live in the signal-dating reference — apply them to every signal.

**Shared conventions across all dimensions:**

- `[start-date]` = the freshness window. Full mode: 12–18 months back for news-type queries. Refresh mode: the date of the last report.
- Date-filter only the queries marked *(dated)* — evergreen facts (investors, competitors, tech stack) live on old pages, and a date filter hides them.
- If the first two queries of a dimension return fewer than 3 results combined, rerun them without the date filter before concluding the dimension is thin.
- In refresh mode, each thread receives the known facts from company memory and skips re-reporting them — it hunts only for what is new or changed.

## Funding & financials

Signal types: `funding | revenue | valuation | investor | ipo`

1. `[Company] funding OR Series OR raised` — news sources *(dated)*
2. `[Company] revenue OR valuation OR ARR`
3. `[Company] investors OR venture capital`
4. `[Company] Crunchbase OR Pitchbook funding`

## Product & technology

Signal types: `product | feature | tech-stack | open-source | engineering`

1. `product OR features OR platform` — restricted to the company's own domain
2. `[Company] product launch OR new feature OR release` — news sources *(dated)*
3. `[Company] tech stack OR engineering OR architecture`
4. `[Company] open source OR GitHub`
5. `blog engineering OR tech` — restricted to the company's own domain

## Leadership & team

Signal types: `leadership | hire | departure | culture | team-size | executive-quote`

1. `[Company] CEO OR founder OR leadership`
2. `[Company] hired OR appointment OR CTO OR VP` — news sources *(dated)*
3. `[Company] employees OR team size OR culture OR glassdoor`
4. `[Company] CEO OR founder interview OR podcast OR keynote` — the richest source of direct quotes; mine these for the report
5. `[Company]` — restricted to LinkedIn

## News & events

Signal types: `news | partnership | acquisition | award | event | social`

1. `[Company] news` — news sources *(dated)*
2. `[Company] partnership OR acquisition OR expansion` — news sources *(dated)*
3. `[Company] conference OR award OR recognition` *(dated)*
4. `[Company]` — restricted to X/Twitter, last week only (social chatter is only useful fresh)
5. `[Company] announcement OR press release` — news sources *(dated)*

## Market position

Signal types: `competitor | market-share | review | analyst | customer`

1. `[Company] competitors OR alternatives OR vs`
2. `[Company] market share OR market position OR industry leader`
3. `[Company] reviews` — restricted to review sites (G2, Capterra, TrustRadius)
4. `[Company] analyst report OR Gartner OR Forrester`
5. `[Company] customers OR case study OR testimonial`

## Framing searches (run before the fan-out)

Not a dimension — two searches that give every thread its skeleton:

1. `about` — restricted to the company's own domain (mission, founding, self-description)
2. `[Company] Wikipedia OR Crunchbase OR Pitchbook` (founding year, HQ, headcount, category)
