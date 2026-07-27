---
title: Beehiiv API reference
description: (reference)
---

# Beehiiv API reference

All requests use `Authorization: Bearer <api_key>` and are scoped to one publication:
`https://api.beehiiv.com/v2/publications/{pub_id}/...`. Every list endpoint that supports
`cursor` pagination returns `has_more` and `next_cursor`; loop until `has_more` is false. Do not
assume a single page covers a publication of any real size.

## Endpoints used

| Purpose | Endpoint |
|---|---|
| Per-issue stats | `GET /posts?limit=100&expand[]=stats&order_by=publish_date&direction=asc&status=confirmed` |
| Full subscriber list with lifetime stats | `GET /subscriptions?limit=100&expand[]=stats&order_by=created&direction=asc` (cursor-paginate) |
| Current active-subscriber snapshot | `GET /subscriptions?limit=1` → read `total_results` (or the equivalent count field) |
| Poll list | `GET /polls?limit=100` → filter to `status === "published"` |
| Poll per-choice results | `GET /polls/{poll_id}/responses?limit=100&expand[]=post` (cursor-paginate) |

## Post/issue field mapping

From each post's `stats.email` object:

| Report field | Source | Notes |
|---|---|---|
| `recipients` | `stats.email.recipients` | |
| `delivered` | `stats.email.delivered` | |
| `deliveryRate` | `delivered / recipients` | Compute yourself; format to one decimal, e.g. `"98.5%"` |
| `openRate` | `stats.email.open_rate` | Already unique opens / delivered; use as-is |
| `uniqueOpens` | `stats.email.unique_opens` | |
| `uniqueClicks` | `stats.email.unique_clicks` | |
| `clickRate` (stored) | `uniqueClicks / delivered * 100` | **Not** the API's own `click_rate` field: see below |
| `unsubscribes` | `stats.email.unsubscribes` | |
| `spamReports` | `stats.email.spam_reports` | |

### The click-rate trap

Beehiiv's API returns `stats.email.click_rate` as **click-to-open rate** (clicks divided by
opens), not clicks-per-delivered. If a report's "click rate" is meant to answer "what fraction
of everyone who received this clicked something," that is `unique_clicks / delivered`, computed
manually. If it is meant to answer "of the people who opened, how many clicked," the API field
is already correct.

The two numbers can differ by a large multiple (click-to-open is always ≥ clicks-per-delivered,
often 2 to 4x higher). A client used to seeing Beehiiv's own dashboard will expect the larger,
click-to-open-flavored number. A reasonable default: compute both and display whichever is
larger.

```
clickToOpenRate = uniqueClicks / uniqueOpens * 100
displayClickRate = max(clicksPerDelivered, clickToOpenRate)
```

## Month rollups

Computed by grouping posts into their publish month, not fetched from Beehiiv directly:

- `peakAudience` = max `recipients` across the month's posts
- `avgOpenRate` = simple (unweighted) average of the month's post open rates
- `avgClickRate` = simple average of each post's `displayClickRate`
- `totalUnsubscribes` = sum of the month's `unsubscribes`

Simple averaging, not recipient-weighted averaging, is the convention: an issue sent to 500
people and one sent to 50,000 count equally toward the month's average open rate. Weight by
recipients instead if the report needs to answer a different question ("what fraction of all
sends this month were opened").

## Audience growth series

Two valid ways to build the section-3 time series, and they are not interchangeable:

- **`per-issue`**: one point per confirmed post, using that post's `recipients` count. Correct
  once a publication's entire history has issue-level tracking. Growth is roughly monotonic by
  construction (recipient counts rarely shrink issue to issue even as the underlying list
  churns), so this mode understates real subscriber loss.
- **`subscriber-timeline`**: a hand-curated series of periodic (e.g. weekly) snapshots of the
  publication's active-subscriber count, taken from `GET /subscriptions?limit=1` (or an
  equivalent aggregate field) and appended over time rather than recomputed. This series *can*
  decline, which is the point: it reflects actual list size, not per-send recipient counts. Use
  this mode for any period predating structured per-issue tracking, or after a platform
  migration where early posts are not confirmed/instrumented the same way.

Whichever mode is chosen for a given publication, do not silently switch modes partway through
its history; that produces a visible discontinuity in the chart with no real-world cause.

## Audience segmentation (from subscriptions + stats)

Walk the full paginated subscriber list with `expand[]=stats`. For each subscriber:

- Track `status` (`active`, `inactive`, `invalid`, or anything else bucketed as `other`) across
  **every** subscriber, for the list-health split.
- For engagement segmentation, only consider subscribers with `status === "active"` **and**
  `stats.total_received >= MIN_ISSUES` (3 is a reasonable default: tune per publication send
  cadence). This excludes subscribers too new to have a meaningful lifetime open rate.
- Bucket by `stats.open_rate`:
  - `superfan`: ≥ 80%
  - `loyal`: 50% to 80%
  - `atrisk`: 20% to 50%
  - `dormant`: < 20%

```
pct(n, d) = round(n / d * 1000) / 10   // one decimal place
```

Report both the segment breakdown (as a share of the *engaged base*, i.e. subscribers meeting
the `MIN_ISSUES` threshold) and the list-health breakdown (as a share of *all* subscribers on
file). They are different denominators and should not be conflated in one chart.

Beehiiv's subscriber object does not include location. There is no field to build a geographic
view from; don't invent one.

## Poll results

`GET /polls?limit=100` lists a publication's polls; filter to `status === "published"`. For
each poll's true per-choice tally, cursor-paginate `GET /polls/{id}/responses` and count
occurrences of each `poll_choice_id` client-side.

Do not rely on the `poll_responses` expand available directly on a poll's GET response: it caps
at 10 responses and does not paginate, so any poll with more than 10 votes will silently
under-report through that path while looking like valid data.

## Engaged-reader / "who clicked this link" export

There is no clean, documented single API call for "list every subscriber who clicked link X
across N issues." The practical approach:

1. In the Beehiiv dashboard, build a subscriber segment from click behavior (e.g. "clicked a
   link in post Y" or an equivalent click-based filter) and export it as CSV.
2. Enrich the export offline: derive each subscriber's email domain, then classify domains into
   company/industry categories with a lightweight heuristic (TLD/keyword matching) or an LLM
   pass. At any real volume, exact per-domain research is impractical, so expect a meaningful
   "uncategorized" bucket, especially for branded startup domains that don't self-describe.
3. Treat this as a periodic manual or semi-automated refresh (re-export and re-classify on a
   schedule), not something the automated weekly data refresh recomputes live.
