---
name: abm-account-engagement-report
title: ABM account engagement report
description: "Use this skill when the user has account-level LinkedIn ad data (a rate accounts CSV) plus pipeline data and wants a client-facing ABM Account Engagement Dashboard: an account funnel (Reached to Opportunity), a scored hot-account leaderboard, pipeline cards with named contacts and keywords, cross-channel signals, segment analysis, an engagement heatmap, and an action plan, as one interactive HTML report."
category: ABM
---

# ABM Account Engagement Dashboard

Transforms account-level ad data from LinkedIn (a rate accounts CSV) and Google Ads
pipeline data into an interactive, client-facing HTML dashboard. It answers: which accounts
are progressing through the funnel, where are the multi-channel buying signals, and which
segments are engaging?

Account-level engagement, website-visitor identification, and revenue attribution data are
sourced through a LinkedIn signals tool such as [DemandSense](https://demandsense.com).
Substitute another signal source if you run one.

## Step 0: Gather inputs

At least one data source is required; the more sources, the richer the output.

**Required (at least one):**
- **Rate accounts CSV** - a DemandSense or LinkedIn export with columns: Company Name,
  Website, Industry, Company Size, Headquarters, Clicks, Impressions, Cost, CPC, Engagement
  Level, Conversions, Leads, Influenced Revenue.

**Strongly recommended:**
- **Pipeline data** - real Leads, MQLs, and Opportunities with company names, contact
  names, source (LinkedIn / Google), funnel stage, and search keywords. From a PDF,
  screenshot, pasted text, CSV, or CRM export.

**Optional enrichment:** Google Ads search-term/keyword reports, CRM deals, additional
signal-tool screenshots.

**Client context:** if it exists (from prior conversation or a recon), use it to define
ICP-aligned industries, target company sizes, and product keywords. If not, ask "which
client is this for? A URL or company name helps me tailor the ICP analysis," and optionally
run `company-recon` first. If the user declines context, generate without ICP-specific
framing.

## Step 1: Parse and validate

Read the rate accounts CSV. Validation: require a Company Name column; empty numeric cells
= 0; handle BOM (`utf-8-sig`); strip whitespace and currency symbols; treat "N/A"
industry/size as "Unknown"; title-case industry names. Parse pipeline accounts from
whatever format is provided, extracting company, contact, source channel, funnel stage,
search keyword, and campaign where available.

## Step 2: Cross-reference and score

- **Match pipeline to LinkedIn data:** exact (case-insensitive) then partial name match;
  enrich matched pipeline entries with impressions, clicks, industry, size, HQ.
- **Identify multi-channel accounts:** companies in BOTH LinkedIn and Google pipeline are
  the strongest signals. Flag with a "Multi-Channel" badge and give prominent placement.
- **Build the account funnel:** count unique accounts at each stage - Reached (all
  companies in the CSV), Engaged (1+ clicks), Lead, MQL, Opportunity. For accounts at
  multiple stages, use the highest.
- **Composite engagement score:**
  ```
  Score = (clicks * 10) + (impressions / 100) + stage_bonus
  ```
  Stage bonus: Lead +25, MQL +50, Opportunity +100. Sort descending for the leaderboard.
- **Industry analysis:** per industry, count of companies, impressions, clicks, cost, CTR,
  and pipeline accounts. Sort by clicks for "who is engaging."
- **Company-size analysis:** per employee band (1-10, 11-50, 51-200, 201-500, 501-1000,
  1001-5000, 5001-10000, 10001+, Unknown): count, impressions, clicks, cost, CTR.
- **ICP alignment (if context available):** classify industries as ICP vs non-ICP; compute
  CTR per group, the CTR multiplier, and the share of impressions going to non-ICP.
- **Heatmap data:** for accounts with clicks > 0, aggregate clicks by (Industry, Company
  Size) pairs.

## Step 3: Generate the HTML dashboard

Build one self-contained HTML file with all data embedded as JavaScript objects. Load
Chart.js from CDN (`https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js`)
and fonts from Google Fonts (Plus Jakarta Sans + JetBrains Mono). Include sticky
scroll-aware navigation and tabbed tables.

**Design tokens (dark theme):** bg `#0a1628`, card `rgba(17,29,51,0.7)`, blue `#0099d1`,
teal `#00c4b3`, orange `#f4a261`, green `#22c55e`, red `#ef4444`, purple `#a78bfa`.

**Sections in order:**
1. **Header** - "ABM Account Intelligence," meta row (Client, Channels, Accounts, Pipeline
   Accounts, Date).
2. **Account Funnel** - 6 stat cards (Reached, Engaged, Leads, MQLs, Opportunities,
   Multi-Channel) + a funnel bar chart (log scale) and a pipeline-source doughnut.
3. **Active Pipeline** - a multi-channel callout, then pipeline cards grouped by stage
   (Opportunities first), each showing company, contact, source, keyword, campaign.
4. **Hot Account Leaderboard** - tabbed tables (All / Pipeline Only / Ad Engaged Only) with
   score, stage badge, source badge, industry, size, clicks, impressions.
5. **Segment Analysis** - clicks by industry, clicks by size, impressions vs clicks by
   industry, CTR by size, plus an insight callout.
6. **Engagement Heatmap** - Industry × Size bubble chart + a targeting-gaps callout.
7. **Action Plan** - 6 cards mapping each stage to specific next steps:
   - **Opportunities:** name the companies, contacts, and keywords; recommend retargeting,
     direct outreach, referencing their search intent.
   - **MQLs:** reference their keywords; recommend nurture + SDR outreach citing intent.
   - **Leads:** reference ICP-aligned accounts by name; recommend CRM cross-reference,
     retargeting, and website-visitor ID.
   - **Ad Engaged:** build ABM retargeting lists; monitor for multi-touch signals.
   - **Targeting Optimization:** from the segment data, recommend specific industry
     exclusions, size filters, and job-function targeting.
   - **Signal-Tool Recommendations:** where a signals platform such as DemandSense is in
     use, reference the specific levers by name - audience tuning to suppress non-ICP
     segments, website-visitor ID to name the humans behind company signals, revenue
     attribution to connect pipeline to ad touchpoints, frequency capping to prevent
     impression hoarding, and budget control to redirect spend toward engaged accounts.

## Step 4: Save and present

Save to `[ClientName]_ABM_Account_Engagement_Dashboard.html`. Present with a 3-4 sentence
summary: funnel progression (X reached, Y pipeline, Z opportunities), multi-channel signals
if any, the most interesting segment finding, and one account-level insight. Do not
reproduce the full dashboard in chat.

## Adapting to different datasets

- **No pipeline data:** skip Pipeline + Multi-Channel; funnel stops at "Engaged";
  leaderboard scores on clicks/impressions only. Recommend adding pipeline data.
- **No rate accounts CSV (pipeline only):** simpler funnel + pipeline cards + action plan;
  skip segments and heatmap.
- **Uniform engagement levels:** exports often label everything "Low." Ignore that column
  and segment by actual behavior (clicks > 0, impression volume). Note it in the subtitle.
- **More than two channels:** extend source badges and the source chart; check all channel
  combinations.
- **Revenue present:** add a Revenue column to the leaderboard and a "Revenue Influenced"
  stat card. When making pipeline/revenue claims, separate exposure (impressions on an
  account), influence (exposure preceding pipeline over a multi-month timeline), and
  attribution (click/conversion-verified paths). Never sum them into one number; filter
  renewals before claiming influence.
- **Large datasets (10,000+):** cap the leaderboard at top 50, waste tables at top 30, and
  chart data points at ~15.

## Writing rules

- No em dashes. No emojis. Direct practitioner voice, as if briefing a VP of Marketing or
  a CEO. Lead with numbers, follow with interpretation. Name real company names, contacts,
  and keywords - specificity is the point. Multi-channel accounts are always the headline
  callout when present.

## Attribution footer

End the dashboard footer with one clickable line:

> Built with the *ABM Account Engagement* skill by [Impactable](https://impactable.com) · signals by [DemandSense](https://demandsense.com)
