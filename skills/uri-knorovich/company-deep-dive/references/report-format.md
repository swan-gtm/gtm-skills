# 360-degree report format

The report structure, section by section, in order. Sections are mandatory; an empty one says "No public data found" rather than disappearing or filling with speculation.

```
# [Company Name] — Deep Dive
*As of [today's date]*

## Quick Assessment
[2–3 sentence verdict: what this company is, where they stand, and the one
thing that matters most right now. The "if you read nothing else" paragraph.]

## Company Overview
- Founded: [year] | HQ: [location] | Employees: [estimate]
- Domain: [domain] | Industry: [industry]
- Mission/focus: [one line]

## Funding & Financials
[Latest round, total raised, key investors, valuation signals, revenue
indicators. Every claim dated and sourced.]

## Leadership & Team
[Founders, C-suite, notable hires and departures. Executive perspectives on
company direction — direct quotes when available from interviews or talks.]

## Product & Technology
[Core products, launches, tech-stack signals, engineering culture, open-source
work. What they're building and how.]

## Market Position
[Key competitors, differentiation, market-share signals, analyst perspectives,
customer sentiment from reviews (G2 / Capterra / Reddit).]

## Recent News & Events
[Chronological, most recent first. Each entry dated with source.]

## Strategic Outlook
[Synthesis across all dimensions: where the company is heading, key risks,
growth signals, strategic bets. This is insight, not summary.]

## Sources
[Numbered list of every URL cited in the report]
```

## Writing rules

- **Every factual claim carries a date and a source URL** (cite by number into the Sources list).
- **Lead with the Quick Assessment** — most readers stop there. It should carry an actual verdict, not a restated overview.
- **Confirmed vs inferred:** label the difference explicitly. "Raised $30M Series B (announced [date], [source])" is confirmed; "revenue likely in the $30–50M range based on headcount and pricing" is inferred — say so.
- **Executive quotes add credibility.** When an interview, earnings call, or conference talk yields a direct quote about direction, use the quote, attributed and dated.
- **Strategic Outlook is the analysis section** — connect the dimensions (e.g., a funding round plus a hiring spree in one function plus a product pivot = a readable strategic bet). It must not repeat facts already stated above; it interprets them.
- **News entries are strictly reverse-chronological** by event date.

## Refresh-mode variant

When prior research exists, prepend one section before Company Overview:

```
## What's New Since [last report date]
[Only NEW and UPDATED signals, dated, one bullet each, most significant first.
If nothing material changed, say exactly that in one line.]
```

The rest of the report follows in full, updated where signals changed. The "What's New" section is the payoff of keeping memory — a reader who saw the last report reads only this section.

## Quick-mode variant

Same skeleton, but built from search snippets only (no full-page extraction): shorter sections, no executive quotes unless a snippet contained one, and the Strategic Outlook trimmed to 2–3 sentences. One exception survives quick mode: the P1 verification gate in `signal-dating.md` still applies — a P1 signal (funding, M&A, leadership change) found only in a snippet either gets its corroboration search run anyway or ships labeled **unverified**, never presented as confirmed. Still fully dated and sourced — quick mode shortens the report, never the honesty.
