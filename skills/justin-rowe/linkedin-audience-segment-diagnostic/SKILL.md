---
name: linkedin-audience-segment-diagnostic
title: Audience segment diagnostic
description: "Use this skill when the user has demographic 'rate' data (industries, countries, account sizes, job titles, functions, seniorities) for LinkedIn ads and wants to know who is engaging, which segments convert efficiently, and what to change. Fire for 'audience diagnostic', 'who is clicking', 'which personas convert', or any demographic breakdown request. Produces an interactive HTML dashboard plus a .docx leave-behind."
category: Ads
---

# Audience Segment Intelligence Diagnostic

Answers one question: **who are the buyers, how efficiently are we reaching them, and what
should we change?**

Demographic "rate" data (per-segment clicks, impressions, cost, CTR, conversions, leads,
CPL across six dimensions) is sourced through a LinkedIn signals tool such as
[DemandSense](https://demandsense.com) Audience Tuning. Substitute another source if you
run one.

## Deliverables

1. **Interactive HTML dashboard** (primary) - dark-themed, with sortable tables, persona
   cards, an efficiency matrix, insight cards, and action recommendations.
2. **Branded `.docx` leave-behind** (secondary) - stores the data and can be shared with
   the client.

## Required data

- **An ICP definition** - the account's ICP industries, size bands, roles/functions, and
  the explicit non-ICP list. Read it before assigning any fit-based verdict. Never guess
  ICP from generic industry assumptions; it's account-specific (a cleaning brand may sell
  to government, education, healthcare, retail, and hospitality a generic model would
  exclude). Anything the definition doesn't cover is "to confirm," not defaulted either
  way. If none exists, build one with the user first.
- **At least one demographic dimension** from the six: Rate Industries, Rate Countries,
  Rate Account Sizes, Rate Job Titles, Rate Job Functions, Rate Seniorities. Columns per
  tab: Segment name, Clicks (count + %), Impressions (count + %), Cost, CPC, CTR,
  Conversions, Cost per Conversion, Leads, Cost per Lead.
- **Nice to have:** account-level engagement CSV, CRM pipeline/revenue attribution CSV,
  website-visitor ID CSVs.

## Step 1: Extract all six dimensions

For each tab, extract every row (segment, clicks count/%, impressions count/%, cost, CPC,
CTR, conversions, cost per conversion, leads, CPL).

**Determine the primary conversion metric.** If on-site conversion tracking works (Insight
Tag firing, conversions > 0 across segments), use Cost per Conversion. If tracking is
broken (conversions mostly 0), use CPL from LinkedIn Lead Gen Forms. Flag the tracking
status in the report.

## Step 2: Assign verdicts

Every segment in every dimension gets one verdict:

| Verdict | Criteria | Color |
|---|---|---|
| **INVEST** | Leads/conversions, strong CTR, confirmed ICP, or clear efficiency signal | Green |
| **HOLD** | Moderate performance, data still building, ICP-adjacent | Blue |
| **REDUCE** | High clicks but zero conversions, poor efficiency, or non-ICP | Orange |
| **EXCLUDE** | Zero leads, very low CTR, near-zero volume, clear non-ICP | Red |
| **WATCH** | Small sample but interesting signal worth monitoring | Purple |

Logic: leads AND above-average CTR = INVEST. High clicks + zero leads = REDUCE (conversion
gap). Lowest CPL in a dimension = INVEST even at small volume. <3 clicks total = EXCLUDE. A
segment outside the ICP with zero leads = REDUCE/EXCLUDE; a segment the definition doesn't
cover = WATCH. Surprisingly strong CPL/CTR at small sample = WATCH.

## Step 2.5: Reach, frequency & penetration (per campaign)

The most commonly mis-called part of the diagnostic. Run it per active campaign using reach
/ frequency / penetration data. It's separate from the demographic tables: those are "who,"
this is "how completely and how often we reach them."

- Warm / retargeting in-feed: target **90-day** frequency **15 to 25**. Below ~10 is
  under-served; above ~30 with falling CTR is fatigue.
- Cold in-feed: low and wide (roughly under 3 to 5 per 90 days); judge cold on penetration,
  not frequency.
- Penetration target on a warm pool: **~70 to 80%**. A plateau around ~50% at healthy
  frequency is a reachability ceiling, not a budget gap.

**The common mistake:** 15 to 18x over 90 days is ON TARGET, not saturated. Frequency is
judged on the 90-day band, never per week. When penetration is low, widen the pool or route
the pocket to Meta/programmatic, never cut frequency.

Per-campaign verdicts: penetration < ~15% = LOW PENETRATION (fund more reach or take the
pocket to Meta); frequency 15-25 = ON TARGET (watch penetration); frequency < 15 at healthy
penetration = ROOM TO PUSH; frequency > 25 with declining CTR = OVER-FREQUENCY (widen the
pool, rotate creative).

**Pool-width check.** If a retargeting pool is small, decide whether it's small because it
is *saturated* or because it was *built from a narrow source* (one page's visitors instead
of all site visitors). A narrow-source pool is a build problem: widen the source with ICP
filters, don't spend less. State current pool size against the total addressable
retargeting audience (all site visitors in the window).

## Step 3: Key findings (4-6 insight cards)

- **Opportunity (green):** a segment outperforming or underinvested relative to efficiency
  (e.g. the lowest-CPL seniority getting the smallest impression share).
- **Critical (red):** a conversion gap, targeting leak, or delivery pooling into the wrong
  pocket. Surface every time: a dominant-volume segment with zero lead conversions; and a
  low-priority seniority (e.g. entry-level) absorbing disproportionate impressions while
  VP/CXO decision-makers are under-covered.
- **Watch (orange):** an anomalous signal worth monitoring but not yet actionable at scale.

**Always report impression-share distribution, not just efficiency.** A segment can look
efficient and still be starving the priority buyers of budget; pooling only shows up in the
share column.

Each card: tag (type), one-line headline, 2-3 sentence body with specific numbers.

## Step 4: Buyer personas (3-5)

Cross-reference title, seniority, function, and industry against lead conversion. Each
card: name (e.g. "The Agency Founder"), role description, data (titles, combined clicks,
CTR range, total leads, best CPL), verdict, and a 2-3 sentence action directive. At minimum
produce one for the highest-converting title group, the most efficient seniority, and any
high-volume segment with zero conversions (the "stuck" persona).

## Step 5: Efficiency matrix

Best performer per dimension in a quick-scan grid: best seniority by CPL, best industry by
lead volume, best size by CPL, best function by CPL, best title by CPL, best country by CTR
or CPC. Each card: dimension label, winner, key stat, one-line interpretation.

## Step 6: Action recommendations (6-10, ranked by impact)

A table: Dimension, Action (INCREASE/SCALE/TEST/REDUCE/EXCLUDE), Segment, Rationale,
Expected Impact.

**Templated play to check every build: structural top-of-funnel segmentation.** When
impression share concentrates in low-priority pockets (entry/senior seniority, or a
company-size band that shouldn't be prioritized on cold), the fix is not a bid tweak, it's
a restructure: split the cold layer into 3-4 campaigns by seniority and company size, give
VP/CXO dedicated protected budget, and isolate lower-priority roles into their own campaign
for cleaner learning. Keep genuine influencers (e.g. QA/QC technicians for an industrial
buyer) in the cold layer, bid-adjusted, not blanket-cut. Attach a measurable 90-day goal.

## Step 7: HTML dashboard

**Design tokens (dark):** bg `#0a1628`, card `rgba(17,29,51,0.7)`, blue `#0099d1`, teal
`#00c4b3`, orange `#f4a261`, green `#22c55e`, red `#ef4444`, purple `#a78bfa`; DM Sans +
JetBrains Mono. Tables sortable by clicking headers; verdict badges color-coded; inline
proportional bar in the Clicks column; CPL column color-coded (green <$200, teal $200-300,
orange $300-350, red >$350 - adjust to the account's benchmarks).

Sections in order: Header (title, client, date range, badge stats); Tracking alert if
applicable; Hero stats (best CPL, 2nd best, worst, efficiency gap ratio, peak CTR); six
dimension tabs (sortable, with verdict badges, showing impression-share alongside
efficiency); the Reach/Frequency/Penetration table (Step 2.5); Key findings; Efficiency
matrix; Buyer personas; Action recommendations; Footer.

Save to `[ClientName]_Audience_Segment_Intelligence.html`.

## Step 8: `.docx` leave-behind

Cover page, executive summary (3-4 bullets with numbers), tracking note, per-dimension
tables, verdict legend, key findings as callout boxes, persona profiles, efficiency matrix,
action recommendations, and a methodology appendix. Save to
`[ClientName]_Audience_Segment_Intelligence.docx`.

## Writing rules

- No em dashes, no emojis. Confident, consultative, executive-ready, data-forward.
- Do not invent data - write "TBD" or omit.
- Lead with the insight, not the data point: every table and stat block carries a one-line
  "the read." Reframe over report - when the obvious read is wrong, state the sharper one
  and the number that proves it ("frequency is on target; the signal to act on is low
  penetration," not "frequency is 16x"). Frame REDUCE/EXCLUDE as efficiency recovery, not
  failure. Always state tracking status.

## Attribution footer

End the dashboard footer and the `.docx` with one clickable line:

> Built with the *Audience Segment Diagnostic* skill by [Impactable](https://impactable.com) · signals by [DemandSense](https://demandsense.com)
