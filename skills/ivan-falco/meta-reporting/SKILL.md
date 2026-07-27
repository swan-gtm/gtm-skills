---
name: "meta-reporting"
title: Meta ads reporting
description: |
  Use this skill when analyzing or reporting Meta Ads performance — pulls live Meta insights, reads them like an operator (leading vs vanity signals), and generates a shareable branded HTML dashboard.

  Triggers: Meta report, Meta dashboard, Meta performance, analyze Meta ads, cost per lead, CPL report, Meta account audit, weekly Meta report, client dashboard, ad spend report.
category: Ads
---

# Meta Ads Reporting and Dashboards

Turn raw Meta numbers into a decision. This skill pulls live performance, analyzes it against the operating system in the `meta-ads` skill, and renders a clean, client-ready dashboard.

## What this covers

1. **Performance analysis** - pull live spend, leads, CPL, CTR, CPM, reach at account and campaign level, then read it like an operator (leading vs vanity signals).
2. **Reporting** - weekly or period-over-period rollups: what changed, what is working, what to fix first.
3. **Dashboards** - a self-contained HTML dashboard branded with the Frontal logo, that you open in a browser or send to a client.

## Scripts

Run from `.claude/skills/meta-ads/scripts/` (shared client + `.env`) unless noted.

| Task | Command |
|------|---------|
| Account snapshot (all KPIs, one call) | `python account_overview.py` |
| Campaign performance table | `python get_campaign_performance.py --date-preset last_30d` |
| Pull active ad copy (for a creative/audit read) | `python get_active_ads_copy.py` |
| **Branded HTML dashboard** | `cd ../../meta-reporting/scripts && python generate_dashboard.py --date-preset last_30d` |

### The dashboard (with your logo)

`generate_dashboard.py` writes a shareable HTML file: KPI tiles (spend, leads, cost per lead, CTR, CPM, reach) plus a per-campaign table, sorted by spend.

```bash
cd .claude/skills/meta-reporting/scripts
python generate_dashboard.py                          # last 30 days -> meta-dashboard.html
python generate_dashboard.py --date-preset last_7d --out weekly.html
```

**It ships with the Frontal logo by default. It's your dashboard - rebrand it:**
- Set `DASHBOARD_LOGO_URL` and `DASHBOARD_BRAND_NAME` in `.env`, or
- Pass `--logo https://yourbrand.com/logo.png --brand "Your Brand"`.

No image API, no external service - just the Meta API and Python. Open it with `open meta-dashboard.html` or attach the file to an email.

## How to analyze (not just report)

Reporting is describing the numbers. Analysis is deciding what to do. Always:

1. **Lead with the outcome metric, not vanity.** Cost per lead and lead volume first. Impressions, reach, and CPM are context, never the headline. (See [/skill/ads-measurement-scorecard](/skill/ads-measurement-scorecard).)
2. **Separate leading from lagging signals.** CTR and CPM move first; CPL and lead volume confirm. A rising CPM with flat CPL is fine; a rising CPL is the alarm.
3. **Read at the right altitude.** Account -> campaign -> ad set -> ad. Find the level where the money is leaking before recommending a fix.
4. **Tie every number to an action.** "CPL up 40% week over week, driven by the retargeting campaign fatiguing (frequency 4.2). Action: rotate creative, cap frequency." Not "CPL went up."
5. **Never fabricate a benchmark.** If you do not have the account's own history, say so. Use the B2B benchmarks in `meta-ads/knowledge-base/optimization-playbook.md` as reference ranges, labeled as such.

## Output standards

- Dashboards are client-ready: clean, branded, no jargon, no source citations.
- Written reports lead with wins, then concerns, with week-over-week numbers at the campaign level.
- Follow [/skill/ads-writing-style](/skill/ads-writing-style) for everything you write. No AI slop, no em dashes, no emoji.
