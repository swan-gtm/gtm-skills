---
name: "linkedin-abm-audit"
title: "LinkedIn ads & ABM audit"
description: "Use this skill when someone wants to review, grade, audit, or improve their OWN LinkedIn ad results, ABM program, or ad spend — or says things like: audit my LinkedIn ads, are my ads any good, how is my ad spend doing, am I running the right number of ads, which ad format is working best, why is my CPC/CPM so high, review my ABM campaigns, which formats influence my deals, are my ads decaying, which companies should I go after, benchmark my LinkedIn ads. Audits the last 30 days of live spend — real CPC, CPM, CTR, ad count, format mix, deal influence, campaign trends and account engagement — grades them against ZenABM's per-format benchmarks, and produces a downloadable audit document with a prioritized fix list. Do NOT use for planning a NEW campaign or budget sizing."
category: ABM
---

# LinkedIn ads & ABM audit

This skill is a **guided conversation you run start to finish**: you pull the user's real last-30-days LinkedIn
ad data, grade it against ZenABM's benchmarks, and hand back a downloadable **"[Company] LinkedIn Ads & ABM
Audit"** with a short, prioritized list of fixes.

> **Requires:** a ZenABM account with the ZenABM connector (app.zenabm.com) authorized — that's how this skill
> reads live LinkedIn ads data. Without it there is nothing to audit, and it will not fabricate data. The
> deal-influence and CRM sections are richer if the user has connected their CRM in ZenABM.

## The golden rule

**The user only chats. You do all the technical work.** They never open a terminal or run a command. Everything
— pulling the numbers, doing the math, comparing to benchmarks, writing the report — is you, quietly, with short
progress notes so it always feels like a conversation and never a silent wait.

## Voice

- Warm, concise, plain-English; explain any jargon in a sentence. Talk like a marketer who lives in demand-gen
  and ABM but stays accessible to a non-technical reader.
- **No emojis in chat.** (The report itself uses small status dots/flags — that's fine.) Prefer hyphens over
  em-dashes.
- This audit is about the user's **own** performance. Planning a brand-new campaign or a budget is a different
  job — don't drift into it here.

---

## Step 1 — Confirm the connection

**Confirm the connector is live before you promise numbers.** Do a tiny probe — call `get_linkedin_metrics` for
the last 30 days. If it errors or returns nothing, the connection isn't ready: tell the user warmly that the
ZenABM connector needs to be authorized and their LinkedIn ads account connected and synced in ZenABM, and wait.
Never fabricate data. If the connector simply isn't available in this session, say so plainly and stop — this
skill can't run on assumptions.

If the user wants the deal-influence section ("which ad formats drive my pipeline"), their CRM needs to be
connected in ZenABM. If it isn't, run the audit without that section and note what they're missing.

## Step 2 — Confirm the window and pull the data

Default window is the **last 30 days**; the previous 30 days is the comparison period for all trend deltas. Tell
the user the dates you're using (compute them — today's date is in your environment) and let them override.

Then pull everything you need with the ZenABM connector. The **exact tool calls, parameters and the fallbacks
per section are in the data playbook reference** — read it and follow it. At a high level you'll gather:

- **Account totals** (this period and previous): spend, impressions, clicks, engagements, landing-page clicks,
  CPC, CPM, CTR — `get_linkedin_metrics`, `get_ad_spend`.
- **Per-format performance**: `get_creative_performance` with `groupBy: "format"` — this is the backbone of the
  benchmark comparison and the allocation section. Run it for this period AND the previous period.
- **Per-ad performance**: `get_creative_performance` (sorted best/worst by clicks; also by format) plus weekly
  windows for the decay check.
- **Ad catalog / counts**: `list_creatives` (how many ads, which are serving) — for the ad-count check.
- **Campaigns / ABM campaigns**: `list_campaigns`, `list_abm_campaigns`, `get_abm_campaign_overview` — for
  campaign trends and top campaign by pipeline.
- **Deals**: `list_deals` (with ABM-campaign / influence filters) — for format→deal influence. Skip gracefully if
  no CRM.
- **Companies / ABM stages**: `list_companies` (engagement, `includeWeekly` for surges), `list_abm_stages`,
  `get_abm_stage_companies_entering` — for the account-trends section.

Keep the user posted with short lines ("Pulling your last 30 days...", "Comparing each format to benchmark...",
"Looking at which accounts are heating up..."). Give the report a moment; don't narrate every call.

## Step 3 — Compute the audit

Do the math in the metrics reference (effective CTR/CPC to landing page, CPM, the ad-count model, deltas) and
grade against the table in the benchmarks reference. Compute, in this order:

1. **Right number of ads?** Feed last-30-days spend and the real CPC into the **ad-count model** (metrics
   reference) to get the affordable healthy ad count, then compare to how many ads they're actually running.
   Classify: **too few** (headroom to launch more), **about right**, or **too many** (each ad starved below the
   ~$25/day delivery floor). Report per-ad daily spend and the health tier.
2. **Format mix + spend share.** For each format: spend, % of total spend, and the count of ads. This is the
   "where the money goes" picture.
3. **Deal influence by format** (if CRM). Attribute influenced deals/pipeline to the formats that touched them;
   name the formats punching above their spend share. If no CRM, drop this and note that connecting the CRM in
   ZenABM unlocks it.
4. **Benchmark grade per format.** For every format they run, put their CTR, CPC, effective CTR to LP, effective
   CPC to LP, CPM (and dwell time if available) next to the benchmark and mark each ✓ at/above par or ✗ below —
   plain ✓ / ✗ marks print cleanly; avoid emoji, which don't render in the PDF export.
   **For link-driving formats (Single Image, Carousel, Video), grade the cost on effective CPC to LP
   (`cost / landingPageClicks`), not raw CPC — raw CPC bills for likes/expands that never hit the site. Lead with
   the effective number.** TLAs get both. See the benchmarks reference for the table and the effective-metric
   definitions (TLAs without a link legitimately have no LP metric — say so, don't flag it).
5. **Allocation recommendation.** Compare current spend-share to where the value is (best effective-CPC-to-LP and
   deal-influencing formats, led by TLAs) and recommend concrete reallocation — move $X from the weak format into
   the strong one.
6. **Campaign trends.** Period-over-period deltas for impressions, engagements, clicks and spend, plus CPC/CPM/CTR
   this vs previous — and the one-line verdict: *increasing efficiency* (more output, flat/less spend) or
   *decreasing* (more spend, less output). Name the top ABM campaign by pipeline/deals, the best campaigns and
   best campaign types, and explain any CTR spike/drop by pointing at the specific ad(s) behind it.
7. **Ad insights.** Best and worst ads by clicks; best and worst formats in the window; TLA effective CTR and
   effective spend (from landing-page clicks); and **decaying ads** — those with CTR declining three weeks
   running, or below their format's pause threshold after 1,000+ impressions.
8. **Red flags / green flags.** Roll the problems and wins into two short lists — each item names the offending (or
   winning) campaign/ad set/ad, the metric, and the fix. The red-flag and green-flag catalogs are in the flags
   reference.
9. **Company trends.** Top 5-10 engaged accounts to go after; companies surging (biggest engagement jump);
   accounts reached for the first time this period; companies that moved into the **Interested** stage; and
   **impression hogs** (accounts eating a disproportionate share of impressions) — only suggest capping/excluding
   these when one account's share is genuinely lopsided versus the rest.

Show the user the headline numbers in chat before you build, so they can sanity-check ("Here's the shape of it —
$X spend, N ads, CPC $Y vs $Z benchmark, TLAs carrying your pipeline, two decaying image ads. Building the full
report now.").

## Step 4 — Build the audit report

1. Build a **clean, self-contained, branded HTML audit document** titled **"[Company] LinkedIn Ads & ABM
   Audit"** — inline CSS/JS, designed for light mode, print-to-PDF friendly. (The full plugin repo at
   github.com/ZENABM/linkedin-abm-skills ships a ready-made ZenABM-branded template and logo assets if you want
   them.)
2. Fill it with the pulled + computed values. Use the ✓ / ✗ grade marks so a reader can skim the grade. Delete
   any section the data doesn't support (e.g. the deal-influence block with no CRM) rather than leaving it empty
   — note instead that connecting the CRM in ZenABM unlocks it.
3. **Also export a downloadable PDF** so the user gets a file, not just HTML — render the same HTML to
   `<company>-linkedin-ads-abm-audit.pdf` (WeasyPrint works well if available; browser print-to-PDF is a fine
   fallback) and present both.
4. Hand the user the document and give them your top 2-3 takeaways in plain English — the detail lives in the
   report.

## What the report must contain (in order)

- **Header / scorecard** — company, window, and a top-line scorecard: spend, ads live, CPC, CPM, CTR, effective
  cost-per-LP-click, each with its benchmark and a pass/fail mark.
- **Are you running the right number of ads?** — affordable healthy ad count vs actual, per-ad daily spend, health
  tier, and the recommendation (launch more / hold / consolidate).
- **Where your budget goes** — spend share and ad count per format.
- **What's influencing your deals** — format → influenced deals/pipeline (or the connect-your-CRM note if no CRM).
- **Benchmark grade by format** — the full comparison table with a pass/fail mark per metric.
- **Reallocate your budget** — current vs recommended split, with the dollar moves.
- **Campaign trends** — period-over-period deltas, efficiency verdict, top ABM campaign by pipeline, best
  campaigns/types, CTR spikes/drops explained.
- **Ad insights** — best/worst ads and formats; TLA effective CTR + effective spend; decaying ads.
- **Red flags / green flags** — two prioritized lists, each item with the culprit/winner and the fix.
- **Accounts to go after** — top engaged, surging, newly reached, moved-to-Interested, impression hogs.
- **Your fix list** — the 3-5 highest-leverage actions, ranked, pulled from everything above.
- **Footer** — the directional-figures disclaimer.

## What good looks like

- **Never fabricate or assume live numbers.** This audit is only as good as the real data — if a tool returns
  nothing, say the data isn't there yet rather than inventing it.
- **Classify ads by `adFormat`, not by campaign/ad-set name** (a campaign named "TLA" may hold Single Image ads).
  See the rule in the data playbook, §3.
- **Quarantine test / sandbox CRM deals** (dev-org URLs, placeholder names, mismatched company, round outsized
  amounts) — never let them inflate influenced pipeline. See the rule in the data playbook, §4.
- **Effective-to-LP metrics need landing-page clicks.** Formats/ads with no outbound link (many TLAs, lead-gen
  forms, some documents) legitimately have no effective-CTR-to-LP — mark them "n/a (no link)", don't score them as
  a failure. Lead Gen Forms are judged on cost-per-lead instead (see the benchmarks reference).
- **Dwell time** may not be exposed by the connector; include it only if present, otherwise omit that column.
- **Decay needs a time series** — pull consecutive weekly windows (see the data playbook); a single all-window
  pull can't show a 3-week decline.
- **Be honest about limited visibility.** "We can't see X yet" is not "X is zero." Don't tell a user an ad has no
  clicks when the value is simply missing.
- **Small accounts:** if there are only a handful of ads or barely any spend, keep the audit proportional — a
  two-ad account doesn't need an impression-hog analysis. Grade what's there and be encouraging.
- Treat all recommendations as **directional guidance**, not guarantees — say so on the report.
- Design the document for **light mode**, self-contained (inline CSS/JS), print-to-PDF.

## Reference files

- **Data playbook** — which ZenABM connector tool to call for each section, with parameters and fallbacks.
- **Metrics** — effective CTR/CPC to LP, CPM, the ad-count model, and the delta math.
- **Benchmarks** — the per-format benchmark table and pause thresholds.
- **Flags** — the red-flag / green-flag catalog and the fix for each.
