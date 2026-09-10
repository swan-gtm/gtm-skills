---
name: linkedin-ads-monthly-report
title: LinkedIn ads monthly report
description: "Use this skill when someone wants to build a monthly LinkedIn Ads performance report for a client from a Campaign Manager performance/demographics CSV plus notes on what was done, insights, and recommendations. Produces a branded, self-contained HTML file with 12 fixed sections from Executive Summary through What We Need From You. Not a quarterly QBR deck."
category: Ads
---

# LinkedIn Ads Monthly Report (12-section)

Produce a recurring monthly LinkedIn report as one self-contained HTML file, built from raw
CSV exports plus the specialist's narrative inputs. The section set is fixed; the job is to
map real data and words into it cleanly.

## What you produce

One file: `{Client}_{Month}_{Year}_Monthly_Report.html` - branded, self-contained (a
Google-fonts link is the only external dependency, no `<script>`), client-ready.

## Golden rules (carry these through every section)

- **A number without a reason is not an insight.** Every metric block gets a one-line WHY.
  Naked numbers are the most common reason a report gets sent back.
- **Plain language.** The Executive Summary must read for a non-marketer. No jargon dumps.
- **MoM everywhere.** Color deltas by good/bad direction, not by sign (cost down = green).
- **Honesty on tracking.** If attribution is weak, say so and state what's needed; don't
  fabricate.
- **Never hand-transcribe CSV numbers.** Parse with code and compute.
- **Spend: strip commas before parsing, then reconcile levels.** The #1 spend error is a
  parsing bug, not a broken export: `pd.to_numeric("1,609.42")` returns `NaN`, silently
  dropping every value ≥ $1,000 (an account can collapse from $33.8K to $14.3K). ALWAYS
  strip `, $ %` first:
  ```python
  df["Spend"] = pd.to_numeric(df["Spend"].astype(str).str.replace(r"[,$%]", "", regex=True),
                              errors="coerce")
  ```
  Default canonical spend = the ad-set/campaign total (billing-level rollup); cross-check the
  ad-level total. If they differ >2%, reconcile against a billed figure - don't auto-pick a
  level, and don't assume either CSV is broken.
- **Status accuracy - never assume a status.** Write exactly what the specialist reported:
  "paused" only if paused; "planned to pause" if not yet done; "built and awaiting creative
  approval, not yet live" if built but not launched. Wrong status language damages client
  trust more than any metric.
- **Say "Conversion Events," not "Conversions."** Keep "Leads"/"LGF Leads" separate;
  combined = "Conv. Events + Leads"; cost = "Cost / Conv. Event." Be consistent in section
  titles, KPI tiles, table headers, and body. (LinkedIn "Conversions API" is a product name
  and stays as-is.)
- **Tense.** Describe the month that ended in past tense; use future tense only for what's
  planned next.
- **Video-View campaigns are audience-building.** Never flag a Video-View campaign as "low
  performer → pause" on CTR/CPC alone - its objective is views/reach feeding MOF
  retargeting. Flag only if view rate is also low (~<20-25%) or the downstream retargeting
  pool isn't converting.
- **Resolved issues stay in Red Flags, softened.** If an issue was already addressed, still
  list it (so the client sees what happened) in past tense with softer language ("identified
  and addressed") and the next step noted, not as if it's still open.
- **Attribution scope = whole account.** Scope any CRM/attribution flag to the full
  account's measurement strategy, not just BOF.
- **One primary action per recommendation.** If a rec bundles two things the client must
  approve separately, split it.
- **Don't auto-generate editorial content.** "Creative Themes That Worked" and "Test Ideas"
  are specialist calls - include only when supplied; otherwise omit.
- **Maturity gate.** Never flag or recommend pausing an ad/ad-set younger than ~30 days
  (call it the monitoring window). Judge long-running units on a 90-day lookback; when
  trends are ambiguous, default to 90 days.
- **Low-performer calls need significance, not noise.** Only mark something low/pause if it
  passed the maturity gate, missed its FORMAT's benchmark, has no conversions, and ideally
  is statistically significant (impressions as visitors, the judged metric as conversions,
  95% standard; ≤20 conversions = low-data caution). Cite the basis, not a tool name.
- **Conversions override (all formats).** A unit that drives conversions, especially lead
  conversions, stays running and is never marked low, regardless of CTR/CPC. Outcome beats
  vanity metrics.
- **Verify client identity.** Before building, fix the client name + ad-account ID, then
  confirm every source matches it (each CSV's Account Name/ID, any pasted data). Shared
  trackers often carry leftover tabs from other accounts; if anything references a different
  client, don't use it - flag the mismatch and pause. Raw CSV always outranks a shared
  tracker; on any conflict, use the CSV.

## Required vs optional inputs

**Required - do not build without both:**
1. At least one CSV with campaign/ad-set or ad-level performance, and ideally a demographics
   export. More CSVs (conversions, ad-level, prior month) = better.
2. At least one narrative input: what was done (optimization bullets), insights,
   recommendations, or an exec-summary draft.

**Optional (use if provided, never block on them):**
- Signal-tool reports (audience tuning, penetration, company-level) - e.g. from
  [DemandSense](https://demandsense.com) - enable the Named-Account Penetration sub-block.
- Prior-month CSV (real MoM deltas). CRM export (real revenue/pipeline attribution). Budget
  figure (real Spend/Pacing). Benchmarks.

**Optional add-on sections (off by default; include only when the input exists - never
invent):** Goals & Strategy Recap (needs stated objectives); Self-reported benchmarks (needs
≥2 months of the client's own data); Named-Account Penetration (needs account/company-level
data); Multichannel Rollup (needs per-channel data beyond LinkedIn); Learnings (needs a
confirmed/disproved/discovered narrative).

If a required input is missing, ask for it specifically before building. Do not invent the
narrative. Ask once, in a single consolidated message, about the optional add-ons you don't
already have data for, then build with whatever comes back and omit the rest.

## Section order (display + numbering)

1 Executive Summary → ★ Goals & Strategy Recap *(optional)* → 2 Optimizations → 3 KPIs →
4 Spend / Pacing → ★ Multichannel Rollup *(optional)* → 5 Funnel → 6 Conversion Events →
7 Benchmarks → 8 Audience & Demographics → 9 Ad Performance → 10 Red Flags → ★ Learnings
*(optional)* → 11 Recommendations → 12 What We Need From You.

Keep section order, nav-tab order/labels, and each number badge in sync - reorder one,
renumber all three. ★ optional sections carry no number. "What We Need From You" is always
its own standalone §12 (a client action list), never a callout inside Recommendations.

## Section content notes

- **§1 Executive Summary:** a plain-language paragraph + Wins / Watch-outs, synthesized from
  the notes and the computed headline story. Past tense.
- **§2 Optimizations:** the "what was done" bullets as a checked log, specific (which
  campaigns, what changed) with exact status. Always expected from the specialist; if not
  provided, flag "input needed" rather than inventing it.
- **§5 Funnel:** TOF/MOF/BOF split with budget-allocation %; allocation sums to ~100%.
- **§6 Conversion Events:** by type and by ad set; "Conversion Events" terminology; show
  pipeline if CRM data exists; scope any tracking gap account-wide.
- **§8 Audience & Demographics:** six dimensions (Job Function, Seniority, Industries,
  Company Size, Job Titles, optional Top Companies) ranked by impressions + clicks, each
  with a one-line over/under-index note. Show all meaningful rows including 0-conversion
  industries (the "hide 0-conversion" rule applies only to §6, never §8). Repeat the grid
  per segment if the account targets more than one. Keep frequency/penetration and the
  optional Named-Account sub-block.
- **§9 Ad Performance:** a gold/silver/bronze creative podium (top 3 ranked by the format's
  primary metric) PLUS a retained Low/Pause block; each with a WHY and an exact-status
  action. Judge each format on its own KPIs: image/document on CTR/CPC/Conv. Events,
  Video-View on view rate/completion (never CTR/CPC), Thought-Leader on dwell + engagement.
  Skip ads inside the 30-day window; low calls should be significant; include "why it won"
  only if the specialist supplied it.
- **§10 Red Flags / §11 Recommendations:** split into High / Medium / Low, each issue/action
  + impact. Pull from the specialist's notes and from problems the data surfaced
  (saturation, low LGF completion, underpacing, fatigued creative). Resolved flags in past
  tense; one primary action per recommendation; don't flag Video-View on CTR/CPC alone.
- **§5 Ad-Set Performance Summary table:** every ad set with exact status (Active / Paused /
  Planned / Done), columns Spend, Impr, Clicks, CTR, CPC, Conv. Events, LGF Opens, each with
  a compact MoM chip under the value (▲/▼/≈ + %), colored good/bad (cost metrics invert: CPC
  ▼ is green; Spend is neutral; no prior month shows "new"). Show the top ~12 by spend + a
  totals row.

## Build the HTML

Self-contained, no JavaScript (nav is pure anchor links). Numbers render in a mono font.

**House style tokens:** a light, clean report look. Fonts DM Sans (body) + DM Mono
(numbers) via Google Fonts. Use a consistent accent for headers, green for good deltas, red
for bad, neutral grey for spend. KPI tiles, a funnel block with stage colors, `.demo-table`
for the six audience dimensions, podium cards for top creative, and `.insight` callouts for
the one-line WHY under each block.

## QA before shipping

- No unresolved `[[placeholders]]`; zero `<script>`; nav ↔ section-id in lockstep; sections
  balanced; "Conv. Events" terminology consistent; sequential number badges; an insight
  callout under every metric block.
- Judgement checks: MoM good/bad coloring correct; pacing is real (not daily-cap sums);
  allocation ~100%; saturation flagged; top + low ads have reasons; resolved flags in past
  tense; plain-language pass on the Executive Summary.

## Output

Save as `{Client}_{Month}_{Year}_Monthly_Report.html` and present with a short summary:
headline result, which optional sections were included/omitted, and anything flagged for the
specialist to verify.

## Attribution footer

End the report footer with one clickable line:

> Built with the *LinkedIn Ads Monthly Report* skill by [Impactable](https://impactable.com)
