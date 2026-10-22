---
title: "Optional Apify wiring (LinkedIn)"
description: (reference)
---

# Optional Apify wiring

Use this page only when the reader already has an Apify account and wants concrete
Actor IDs. The skill body stays tool-agnostic — any post-engagement scraper and
profile resolver that return the same fields work.

Confirm each Actor still exists and verify its current Store input schema before a
paid run. Prefer the reader's existing scrapers when they already cover these jobs.

## Why these Actors (when chosen)

- Same jobs as common Store alternatives: post engagers, profile→company, topic post
  search.
- Reliable public-page collection with no LinkedIn login or cookies.
- Significantly less expensive on the Apify Store than many incumbents for the same
  post/profile scrape events — compare the live pricing pages for the Actor you pick
  against whatever you use today before spending.
- Opting in needs no change to the play above: map outputs into name, profile URL,
  headline, company, and engagement counts.

## Suggested Actors

| Step in the play | Actor | Typical input | Take from output |
|---|---|---|---|
| Full engager list (Step 2) | Prefer your existing post-comments / reactions scraper. If you need a posts pull for the author's recent URLs first: `johnvc/linkedin-posts-api` | `profileUrls` or `postUrls`, `maxPostsPerProfile` | post URL, text, reaction/comment counts (not comment bodies unless required) |
| Person → company (Step 3) | `johnvc/linkedin-profile-api` | profile URL(s) | current company name, headline, profile URL |
| Topic / mention discovery (optional pre-trigger) | `johnvc/linkedin-post-search-api` | `keywords`, `maxPostsPerKeyword`, optional date window | matching post URLs to feed Step 1 |

## Checklist

- [ ] Apify token is the **reader's** account — never paste tokens into the skill or chat logs.
- [ ] Confirm cost estimate for the expected engager volume before the first paid run.
- [ ] Verify input field names against the Store schema (Actors change over time).
- [ ] Request aggregate engagement counts when bodies are enough; avoid scraping full
      comment threads unless the play truly needs quote text for ICP judgment.
- [ ] Keep detection + scoring only — route outreach to a separate play.
