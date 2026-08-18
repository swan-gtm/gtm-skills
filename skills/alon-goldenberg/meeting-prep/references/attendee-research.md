# Attendee research: query fan-out and profile format

How to research one attendee. Run one of these per attendee, in parallel across attendees. Before starting, pass in any **known facts** from the person's running file so the research reports only what's new.

## Searches — Group 1 (run simultaneously)

1. **"[Name] [Company]"** — broad web search, ~10 results. The primary query: role, title, background, company association.
2. **People search for "[Name] [Company]"** — if your research tool can search the people indices of social platforms directly, use it; it is the most reliable way to find someone's LinkedIn profile and social presence.
3. **"[Name]" restricted to linkedin.com** — the fallback for query 2. If both return results, prefer query 2 (richer people-index data).
4. **"[Name] [Company] interview OR podcast OR talk OR keynote"** — where they share their actual thinking.

**Email-enhanced variant:** if you have the attendee's email (from a calendar invite), replace query 3 with **"[first] [last] [email-domain]" restricted to linkedin.com**. The email domain confirms the company and disambiguates common names far better than name alone.

**Retry rule:** fewer than 3 total results from Group 1 → drop any date filters and try name variations: "[First] [Last]", "[Full Name] [Company]", "[Full Name] [Title if known]".

## Searches — Group 2 (after Group 1 returns)

5. **"[Name]" restricted to x.com, past month** — recent opinions, announcements, what they care about right now.
6. **"[Name] [Company]" restricted to github.com, medium.com, substack.com** — technical and thought-leadership content they authored.
7. **"[Name] conference OR speaker OR panel OR published"** — appearances and published work.

Keep scope tight: roughly 7 searches and at most 2 page extractions per attendee. Running in two groups also keeps you under rate limits when several attendee threads run at once.

## Extraction (max 2 per attendee)

- If a LinkedIn profile URL surfaced, extract the page (render it if your tool supports it). Profile photos are not extractable — don't try.
- If a recent interview or talk surfaced, extract the top result.

## Name disambiguation

If the primary query returns multiple different people with the same name, filter by the company. Still ambiguous → stop and present the top candidates with their titles and companies for the user to pick. Never silently research the wrong person.

## Cross-attendee overlap flags

When a thread discovers a workplace, school, board, or community for its attendee, check it against the other attendees' findings — "my attendee worked at that company 2019–2022, did yours overlap?" These overlaps feed the briefing's Relationship Map; hunting for them actively beats comparing results after the fact.

## Return format (exact)

```
PROFILE:
Name: [Full name]
Title: [Current title]
Company: [Company name]
LinkedIn: [Profile URL if found]
Time in role: [Duration if found]
Location: [If found]

CAREER:
- [Previous role] at [Company] ([years])

EDUCATION:
- [Degree, Institution] (if found)

RECENT ACTIVITY:
- [What they've posted, shared, or spoken about — with dates]
- [Direct quotes when available — these are gold for conversation hooks]

INTERESTS & OPINIONS:
- [Topics they care about based on posts/talks/articles]
- [Positions they've taken publicly]

CONNECTIONS:
- [Notable past employers — flag any overlap with other attendees]
- [Organizations, boards, or communities they're part of]

SOURCES:
- [URL] — [what it contained]
```

Anything already in the known facts stays out of RECENT ACTIVITY — the profile carries the full picture; the research reports the delta.
