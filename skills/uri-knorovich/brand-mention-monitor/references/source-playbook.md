# Source playbook — profiles and query patterns

Source selection must match where the brand's audience actually talks. Pick one profile from the brand research step, run its primary sources every pass, add secondaries on deep sweeps, and skip the deprioritized ones unless the user asks. Run social first (fastest to surface new mentions), then news, then review platforms. Bound every query to the run's date window.

Queries below are written as web search strings. If your search tool has a social-focused mode, use it for the social queries — it surfaces posts and threads better than plain web search. Use shallow results for discovery; extract the full page or thread only on high-signal hits, since engagement counts and reply tone live in the full content.

## The five market profiles

### B2B enterprise software / SaaS
- **Primary (every pass):** LinkedIn, G2, Capterra, Hacker News, category subreddits (r/sysadmin, r/devops, r/[category]), trade press (InfoQ, TechCrunch, ZDNet, The Register), Glassdoor (employee signal)
- **Secondary:** Reddit broad, X/Twitter (exec accounts, analysts), Medium/Substack
- **Deprioritize:** TikTok, Instagram, Facebook — low signal for B2B buyers

### Consumer brand / e-commerce
- **Primary (every pass):** TikTok, Instagram, X/Twitter, Reddit, YouTube, Facebook, Trustpilot, Google Play / App Store
- **Secondary:** news press, blogs, Pinterest
- **Deprioritize:** Hacker News, LinkedIn, trade press — low signal for consumer sentiment

### Regulated industry (finance, healthcare, pharma, insurance)
- **Primary:** wire and sector press (Reuters, AP, Bloomberg, sector-specific), regulatory watchdog sites, journalist accounts on X, LinkedIn exec commentary, formal review platforms (BBB, consumer-protection agency complaint databases)
- **Secondary:** Reddit, X broad, forums
- **Deprioritize:** TikTok, Instagram — press and regulatory risk outranks user-generated content here

### Regional / non-English brand
- **Primary:** local-language news, regional forums and social platforms (Weibo for China, VK for Russia, Naver for Korea, and equivalents), local-language X/Instagram
- **Secondary:** English-language global platforms only where relevant
- **Note:** set your search tool's locale/country parameters so local-language results surface

### Startup / developer tool
- **Primary:** Hacker News, Reddit (r/programming, r/webdev, r/[category]), GitHub discussions, Dev.to, X (developer influencers), Product Hunt
- **Secondary:** LinkedIn, Medium, TechCrunch

## Tier 1 — Social (run first, every pass)

### Reddit
- `"[brand]" site:reddit.com` — broad sweep
- `"[brand]" site:reddit.com/r/[category]` — category subreddit; also the brand's own subreddit if one exists
- `"[brand]" complaint OR issue OR problem site:reddit.com` — risk
- `"[brand]" recommend OR love OR "switched to" OR best site:reddit.com` — opportunity
- `"[brand]" vs OR alternative OR "compared to" site:reddit.com` — competitive
- Signal: sort by new for recency, top for reach; threads with 100+ comments are high priority.

### X / Twitter
- `"[brand]" site:x.com` — broad; `"#[brand]" site:x.com` — hashtag sweep
- `"[brand]" angry OR disappointed OR broken OR "doesn't work" OR worst site:x.com` — risk
- `"[brand]" love OR amazing OR "highly recommend" site:x.com` — opportunity
- `"[brand]" complaint OR refund OR scam site:x.com` — escalation risk
- Signal: verified accounts, 10K+ follower accounts, threads with 50+ replies.

### LinkedIn
- `"[brand]" site:linkedin.com`
- `"[brand]" review OR feedback OR experience OR "working with" site:linkedin.com`
- `"[brand]" CEO OR founder OR team site:linkedin.com` — exec commentary
- Signal: practitioner posts carry weight with B2B buyers; exec commentary shapes enterprise perception.

### Instagram / TikTok / Facebook / Threads
- Social-mode searches: `"[brand]" instagram`, `#[brand] instagram review OR unboxing OR haul`
- `"[brand]" tiktok`, `#[brand] tiktok review OR reaction OR honest`, `"[brand]" tiktok made me buy`
- `"[brand]" facebook group`, `"[brand]" facebook review`
- `"[brand]" site:threads.net`
- Signal: viral reaction content moves faster than press — a high-view negative TikTok is urgent; "TikTok made me buy it" is high opportunity; Facebook groups skew consumer/SMB and older demographics.

### YouTube
- `"[brand]" review OR "honest review" OR "is it worth it" site:youtube.com`
- `"[brand]" "don't buy" OR problems OR "I returned" site:youtube.com` — risk
- `"[brand]" unboxing OR "first impressions" site:youtube.com`
- Signal: view count and like ratio; a negative review with 100K+ views is high risk.

## Tier 2 — News and press

- `"[brand]" news` — broad sweep
- `"[brand]" site:techcrunch.com OR site:theverge.com OR site:wired.com`
- `"[brand]" site:businessinsider.com OR site:forbes.com OR site:bloomberg.com`
- `"[brand]" site:reuters.com OR site:apnews.com`
- Add category-specific press from the brand profile.
- Hacker News: `"[brand]" site:news.ycombinator.com` (or search hn.algolia.com); threads with 50+ comments reach a highly influential technical audience.
- Blogs and newsletters: `"[brand]" site:medium.com`, `"[brand]" site:substack.com`, `"[brand]" blog review OR "my experience"` — long-form opinion shapes search results over time.

## Tier 3 — Review platforms

- G2: `"[brand]" site:g2.com reviews` — new 1–3 star reviews and a score drop are risk; watch trending themes in the cons.
- Trustpilot: `"[brand]" site:trustpilot.com` — a cluster of negatives in a short window is the signal, not any single review.
- Capterra/GetApp: `"[brand]" site:capterra.com`, `site:getapp.com`
- App stores: `"[brand]" site:apps.apple.com`, `site:play.google.com` — version-specific complaints and rating drops after an update.
- Product Hunt: `"[brand]" site:producthunt.com` — launch-day reactions, "alternatives to" pages, maker response tone.

## Tier 4 — Opportunity-specific (run these deliberately)

- **Purchase intent:** `"[brand]" "thinking of buying" OR "should I get" OR "is [brand] worth it"` — an unanswered purchase-intent question deserves a helpful reply, not a sales pitch.
- **Organic advocacy / UGC:** `"[brand]" "I love" OR "obsessed with" OR "game changer"`, `"[brand]" "just got" OR "finally tried"` — amplify or reach out for partnership.
- **Press opportunities:** `"[brand]" "for comment" OR "reached out" OR spokesperson`, `"[brand]" journalist OR "writing a story"` — a journalist looking for a quote gets flagged immediately.
- **Comparison wins:** `"[brand]" vs "[competitor]" site:reddit.com OR site:x.com`, `"switched from [competitor] to [brand]"` — positive comparisons are amplification material; negative ones go to Watch.
