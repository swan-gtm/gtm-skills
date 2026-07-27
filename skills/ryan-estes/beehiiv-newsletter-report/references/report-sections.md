---
title: Report sections
description: (reference)
---

# Report sections

Data shapes below are described generically (field name, type, meaning), not tied to any one
language or framework. Adapt to whatever the implementation stack actually is.

## 1. Hero stats

Three numbers, no chart, at the top of the report:

- **Total growth**: `(currentAudience - launchAudience) / launchAudience`, as a percentage.
  Pair with the date range it covers (launch date to "now").
- **Current audience**: latest point in the audience growth series, plus the launch figure for
  contrast ("from X at launch").
- **Average open rate**: average of `openRate` across recent issues (choose a window, e.g.
  "this year to date" or "last 6 months": state the window in the label so it's not read as
  all-time).

Data needed: `{ totalGrowthPct, currentAudience, launchAudience, avgOpenRate, windowLabel }`.

## 2. Website / lead magnet links

A short list of outbound links, not chart data. Typically:

- The newsletter's own homepage/website.
- Any sponsor or partner destination being tracked for click-through (the same link that powers
  section 8, if present).

Data needed: `{ label: string, url: string }[]`. Render as plain external links, each opening in
a new tab.

## 3. Audience growth chart

One area/line chart, `growthData: { label: string, recipients: number }[]`, spanning the
publication's full history. Label the launch-to-now growth percentage directly on the chart
(e.g. a badge: "+X% since launch"), and mark any notable transition point (a platform migration,
year boundary) with a reference line if one is meaningful to the audience.

See `beehiiv-api-reference.md` for the `per-issue` vs `subscriber-timeline` decision.

## 4 & 5. Open rate analysis / click rate analysis

Same structure for both, one instance per metric:

- A per-issue bar chart: `chartData: { label: string, value: number }[]` (open rate as a
  percentage, or click count/rate).
- Optionally highlight bars above a threshold (e.g. open rate ≥ 50%) in a distinct color to
  visually separate "good" issues from average ones.
- A short caption stating the date range and one-sentence takeaway.
- A structured narrative block, `content: { question, verdict, points[], opportunity }`:
  - `question`: the thing a client would actually wonder, phrased in their words (e.g. "Is open
    rate holding up as the list grows?").
  - `verdict`: the direct, one-sentence answer.
  - `points`: 2 to 4 supporting bullet points with specific numbers, not vague claims.
  - `opportunity`: one forward-looking suggestion or thing worth watching.

This four-part structure (question / answer / evidence / opportunity) is the load-bearing
pattern for both rate-analysis sections; keep it rather than replacing it with generic prose,
since it's what makes the section scan quickly.

## 6. Audience insights

Two views from one `audience` object (see `beehiiv-api-reference.md` for how it's computed):

- **Engagement segmentation**: a donut/pie chart of `segments: { key, count, pct }[]` (superfan
  / loyal / at-risk / dormant), with the engaged-base total in the center. Below or beside it,
  list each segment with a one-line description of what the bucket means (e.g. "opens nearly
  every issue").
- **List health**: a single stacked horizontal bar of `listHealth: { key, count, pct }[]`
  (active / inactive / invalid), with a legend showing counts and percentages.

State the "as of" generation date and the engagement-base threshold (e.g. "computed over the
X active subscribers who have received at least 3 issues") directly in the section's caption, so
the denominator is never ambiguous. Render nothing if there's no audience data yet.

## 7. Month-over-month tabs

One tab per calendar month with data, most recent first or last (pick one and stay consistent).
Each tab contains, top to bottom:

- **Synopsis**: `{ headline: string, highlights: string[], opportunities: string[] }`. The
  headline is one sentence capturing the month. Highlights and opportunities are each a short
  bulleted list, kept visually distinct (e.g. two columns, different accent colors) so a reader
  can separate "what went well" from "what to watch" at a glance.
- **Month rollup stats**: peak audience, average open rate, average click rate, total
  unsubscribes for that month (see rollup formulas in `beehiiv-api-reference.md`).
- **Individual issue list**: every issue published that month, each rendered per section 9.

Only regenerate the synopsis for months whose underlying data actually changed; see
`automation-pipeline.md`.

## 8. Engaged-reader export

Include only when a report tracks click-through to a specific sponsor/partner link. Shows:

- Two headline numbers: total distinct readers who clicked, and total distinct companies
  represented (derived from unique email domains, typically excluding personal/generic email
  domains from the company count).
- A "click to export" action that downloads the full list as CSV (email, domain, category).
- A "view full list" action opening a searchable table (search by email, domain, or category)
  of every clicker.
- A horizontal bar chart of company/industry category counts, with a one- or two-sentence
  narrative naming the top categories and noting what share falls into an "uncategorized"
  bucket.

Data needed: `clickers: { email, domain, category }[]` and a derived `categories: { category,
subscribers, companies }[]` (sorted descending by subscriber count). Exclude personal/generic
email domains and the uncategorized bucket from the narrative's "top categories" callout, but
still show them in the chart and full list.

See `beehiiv-api-reference.md` for how this data is actually sourced (it is not a live query).

## 9. Per-issue KPI cards

One card per issue, typically nested inside its month tab. Shows, per issue:

- Title, publish date, a link to the live issue.
- Recipients, delivered count, delivery rate.
- Open rate, unique opens (visually highlight if above a strong-performance threshold).
- Click rate (the display value from `beehiiv-api-reference.md`), unique clicks (same
  highlight treatment).
- Unsubscribes, spam reports (flag spam reports if greater than zero; otherwise show "0 spam"
  plainly so its absence is visible, not just omitted).
