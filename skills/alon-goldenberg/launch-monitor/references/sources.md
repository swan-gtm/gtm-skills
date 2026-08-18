# Source tiers and query patterns

Launch monitoring needs speed and precision. Run tiers in this order: highest-reach first, then community, then niche — a wrong claim in a high-reach outlet spreads to secondary coverage within hours, so that is where the first minutes of any run go. Within a tier, run all queries in parallel.

All patterns below use `site:` operators, which work in any web search tool. Substitute the product's confirmed name variants (from alternate-name resolution) into every `"[product name]"` slot — run the high-signal queries once per variant when variants differ materially.

---

## Tier 1 — High-reach press (run first)

Widest reach, highest chance of a mischaracterization spreading to secondary coverage. Check within the first pass of any run.

- `"[product name]" site:techcrunch.com`
- `"[product name]" site:theverge.com`
- `"[product name]" site:wired.com`
- `"[product name]" site:arstechnica.com`
- `"[product name]" site:venturebeat.com`
- `"[product name]" site:siliconangle.com`
- `"[product name]" site:theregister.com`
- `"[product name]" site:zdnet.com`
- `"[product name]" site:bloomberg.com`
- `"[product name]" site:reuters.com`
- `"[product name]" "[company name]" announcement OR launch OR release`

**Category-specific press** — add based on the context profile:

- Developer tools / APIs: `site:infoq.com`, `site:sdtimes.com`, `site:thenewstack.io`
- AI/ML: `site:theinformation.com`, plus the major AI newsletters
- Enterprise SaaS: `site:cio.com`, `site:computerworld.com`
- Consumer: `site:mashable.com`, `site:engadget.com`

---

## Tier 2 — Community & developer forums (parallel with Tier 1)

Community threads move faster than press and contain the most honest reactions — including the mischaracterizations that later spread *to* press.

### Hacker News
- `"[product name]" site:news.ycombinator.com`
- Also search HN's own search index (hn.algolia.com) with a last-24h date filter
- Signal: threads with 50+ comments are high-priority; read the top comments specifically for wrong claims — an upvoted wrong claim is the seed of tomorrow's press error

### Reddit — broad + subreddit-specific (run all, not just one)
- `"[product name]" site:reddit.com` — broad sweep
- `"[product name]" site:reddit.com/r/[category subreddit]` — from the context profile
- `"[product name]" site:reddit.com/r/[company name]` — brand subreddit if it exists
- `"[product name]" site:reddit.com/r/technology`, plus the profile-relevant subs (`r/programming`, `r/MachineLearning`, `r/SaaS`, `r/webdev`, `r/devops`, `r/artificial`, …)
- Signal: sort by "new" for real-time reaction, "top" for highest-reach threads; "I'm disappointed" and "this is actually X not Y" threads are the priority reads

### Dev communities (if the audience is technical)
- `"[product name]" site:dev.to`
- `"[product name]" site:hashnode.com`
- `"[product name]" site:medium.com`
- `"[product name]" site:stackoverflow.com`
- `"[product name]" site:github.com` — issues, discussions, reactions on the repo if public
- `"[product name]" discord` — find the official or community server; early feedback lands there before it surfaces publicly

---

## Tier 3 — Social (real-time volume and influencer signal)

Sweep every pass, not just the first run — social moves faster than everything else.

### X / Twitter
- `"[product name]" site:x.com`
- `"[product name]" launch OR announced OR "just released" site:x.com`
- `"[product name]" wrong OR broken OR disappointed site:x.com` — complaint hunt
- `"[product name]" "actually" OR "turns out" OR correcting site:x.com` — correction chains
- Check quote-posts of the official launch post — reactions and mischaracterizations concentrate there
- Signal: threads with 100+ likes within 24h; journalist corrections; influencer takes

### LinkedIn
- `"[product name]" site:linkedin.com`
- `"[product name]" launched OR "my take" site:linkedin.com`
- Signal: founder/exec posts, practitioner commentary, buyer takes — for B2B products LinkedIn often carries higher-quality signal than X

### YouTube
- `"[product name]" review OR "hands on" OR reaction site:youtube.com`
- `"[product name]" "first impressions" OR unboxing site:youtube.com`
- `"[product name]" problems OR issues OR "doesn't work" site:youtube.com`
- Signal: view count within 48h and comment themes; large tech channels shape mainstream perception faster than most press

### Instagram / TikTok / Facebook / Threads
These platforms block most direct search — if your web-research tool has a social-focused search mode, use it here; otherwise pair `site:` queries with platform-name keyword queries:
- `"[product name]" site:tiktok.com`, or social-mode query `"[product name]" review OR reaction`
- `"[product name]" site:instagram.com`, or social-mode query `"[product name]" instagram`
- `"[product name]" site:facebook.com` / `site:threads.net`
- Signal: viral reaction videos in the first 48h can reach audiences larger than any press outlet; comment sections surface raw consumer sentiment fast

---

## Tier 4 — Competitor monitoring (if enabled)

- `[competitor] "[product name]" OR "[category keyword]"` — are they writing about the launch?
- `[competitor] "compared to" OR "vs" OR "alternative"` — positioning content
- `[competitor] site:x.com` — real-time reactions from their accounts
- Check each competitor's blog and changelog for counter-announcements within 48h of launch
- `"[competitor] vs [product name]"` — comparison content published since launch date
- Silence is also a data point — record "no visible response" per competitor rather than omitting them

---

## Tier 5 — Mischaracterization-specific queries (every pass)

Build these from the context profile's "what would a mischaracterization look like":

- **Pricing:** `"[product name]" pricing OR price OR "costs $"` — compare against actual pricing
- **Category confusion:** `"[product name]" "[wrong category]"` — e.g. an API being called a "no-code tool"
- **Capability inflation:** `"[product name]" "[feature it doesn't have]"`
- **Capability deflation:** `"[product name]" "only" OR "just" OR "limited to"`
- **Wrong comparisons:** `"[product name]" vs "[wrong competitor]"`
- **Attribution errors:** `"[product name]" "[wrong company name]"`
- **Spread check:** re-run any confirmed wrong claim as its own query — `"[product name]" "[wrong claim]"` and `"[product name]" site:reddit.com "[wrong claim]"` — to see who else is citing it

---

## Tier 6 — Consumer & app-specific sources

Add for consumer launches (apps, hardware, consumer software); skip for pure B2B/developer tools.

- **App stores:** `"[product name]" site:apps.apple.com` / `site:play.google.com` — check the recent-reviews tab directly; 1-star reviews after an update flag regressions before press notices, and platform-specific issues surface here first
- **Podcasts:** `"[product name]" podcast OR episode site:open.spotify.com OR site:podcasts.apple.com` — major tech podcasts shape consumer narrative
- **Product Hunt:** `"[product name]" site:producthunt.com` — launch-day comments and "alternatives to" pages
- **Ecosystem forums:** Apple → `site:forums.macrumors.com`, `site:9to5mac.com`, `site:appleinsider.com`; Android → `site:androidpolice.com`, `site:9to5google.com`; gaming → `site:resetera.com`, `r/gaming`

---

## Alternate name resolution — query patterns

Run before asking the user anything; fold every confirmed variant into the query lists above.

- `"[product name]" codename OR "internal name" OR "project name"`
- `"[product name]" "formerly known as" OR "previously called" OR rebranded`
- `"[company name]" "[product category]" names OR versions`
- Hardware: search both the marketing name and the internal model identifier
- AI products: check API name, model name, and consumer-facing name separately — they are often different
- Software: check the GitHub repo name, package name, and SDK name
