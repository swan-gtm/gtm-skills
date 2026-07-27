---
name: "linkedin-abm-monthly-report"
title: Monthly LinkedIn ABM report
description: "Use this skill when someone wants a monthly LinkedIn Ads & ABM performance report for the last full calendar month — a month-end / end-of-month ABM report, a LinkedIn ads recap, a stakeholder or exec report, a \"report on last month's ads/campaigns\", a monthly performance summary, or a shareable report with month-over-month comparison. Pulls spend, pipeline, deals, campaign and ad-format performance and engaged companies for the last calendar month, compares to the prior month, grades ad formats against ZenABM benchmarks, and lists recommendations and next steps. Do NOT use for a diagnostic fix-list audit of the trailing 30 days (use the LinkedIn ads & ABM audit skill), planning a NEW campaign/budget, or profiling COMPETITORS' ads."
category: ABM
---

# LinkedIn ABM ad reporting (ZenABM)

This skill produces a **monthly report** — a clean, shareable
**"[Company] LinkedIn ABM Ad Report — [Month Year]"** covering the **last full calendar month**, compared to the
month before, delivered as a self-contained branded HTML document and a downloadable PDF.

This is a **report, not an audit.** Its job is to summarize what happened last month for a stakeholder / exec
audience: the numbers, what moved vs the prior month, what worked, and what to do next. It is the reporting
sibling of the LinkedIn ads & ABM audit skill (which is a diagnostic, trailing-30-day, fix-list audit) — reuse
the same benchmarks and math, but frame it as a recap, not a to-do list.

**Requires a ZenABM account and the ZenABM connector** (app.zenabm.com) for live LinkedIn ads data — that's how
the skill pulls last month's spend, pipeline and deals influenced, best campaigns/formats/ads, month-over-month
changes, and engaged companies. Without it, the report can't be produced, and figures are never invented. The
Revenue/pipeline/deals section additionally needs HubSpot (or another CRM) connected in ZenABM; without it that
section is skipped.

## The golden rule

**The user only chats. You do all the technical work** — pull the numbers, do the math, compare to last month and
to benchmarks, write the report — with short progress notes so it always feels like a conversation. The only
thing you ask them to *do* is connect ZenABM (and ideally their CRM).

**Probe before promising numbers:** call `get_linkedin_metrics` for the report month. If it errors or is empty,
the connector isn't ready — help them finish connecting and wait. Never fabricate data.

## Step 1 — Set the window (LAST CALENDAR MONTH) and pull the data

**The window is the last FULL calendar month — not the trailing 30 days.** Compute from today's date: if today is
2026-07-11, the report month is **June 2026** (`2026-06-01` to `2026-06-30`) and the comparison month is
**May 2026** (`2026-05-01` to `2026-05-31`). Use explicit `startDate`/`endDate` for both months (you can also use
`period: "lastMonth"` for the report month, but pass explicit dates for the comparison month). Tell the user the
month you're reporting on and let them override (e.g. they may want a specific past month).

Pull everything with the ZenABM connector — exact calls and fallbacks are in the Data playbook reference on the
LinkedIn ads & ABM audit skill: account totals (report month + prior month), per-format performance
(`get_creative_performance` `groupBy:"format"`), best ads and best-per-format, campaigns and ABM campaigns,
deals (CRM), and engaged companies. Keep the user posted with short progress lines.

## Step 2 — Compute the report

Use the Metrics reference on the LinkedIn ads & ABM audit skill (effective CTR/CPC to LP, CPM, month-over-month
deltas) and grade formats against the Benchmarks reference on the same skill. Compute, for the report month and
the prior month:

- **Pipeline generated** and **deals open / influenced** (from CRM deals) + **total spend.**
- **Top ABM campaign and top LinkedIn campaign** (by pipeline/deals, then by clicks/efficiency).
- **Top ad formats** and **spend per ad format** (share of spend), graded vs benchmark.
- **Top ads** (by clicks / landing-page clicks).
- **Top engaged companies.**
- **Month-over-month deltas** on spend, impressions, engagements, clicks, CPC, CPM, CTR, pipeline — and a plain
  verdict (improving / steady / declining efficiency).

**Apply the shared rules** (they live in the audit skill's Metrics and Benchmarks references): grade link-driving
formats (Single Image, Carousel, Video) on **effective CPC to landing-page click**, not raw CPC; classify ads by
their real `adFormat`, never by campaign name; and **quarantine obvious test/sandbox CRM deals** (dev-org URLs,
placeholder names, mismatched company, round outsized amounts) so they don't inflate pipeline.

Show the user the headline numbers in chat before building, so they can sanity-check.

## Step 3 — Build the report (HTML + PDF)

1. Build a **clean, self-contained, branded HTML monthly report** — light mode, inline CSS/JS, designed to print
   to PDF. (The full plugin, including the original branded report template and assets, lives at
   github.com/ZENABM/linkedin-abm-skills.)
2. Use plain **✓ / ✗** grade marks (never emoji — they don't render in the PDF).
3. **If HubSpot/CRM isn't connected**, delete the Revenue/pipeline/deals section and the pipeline figures in the
   exec summary, and note that connecting a CRM in ZenABM unlocks it. Don't invent pipeline.
4. Title it **"[Company] LinkedIn ABM Ad Report — [Month Year]"**, and export a PDF of the same HTML (e.g.
   WeasyPrint: `weasyprint report.html out.pdf`).
5. Hand the user the PDF + HTML and give a 2-3 sentence plain-English recap.

## Report structure (in order)

Open with a short **table of contents** on the first page (right after the cover, before the executive summary)
— a numbered list of the sections below, so a reader can scan the report at a glance. Then:

1. **Executive summary** — a one-glance dashboard for the month:
   - **Pipeline generated**, **deals open**, **total spend** (headline stat cards, each with the MoM delta).
   - **Top performing ABM and LinkedIn campaigns.**
   - **Top performing ad formats** and **spend per ad format.**
   - **Top performing ads.**
   - **Top engaged companies** — show these as **bold bullet points** (name + the key metric), not buried in a
     sentence. This is a preview of the full section 6.
   - **General summary + comparison to the previous month + recommendations** — a short narrative: what happened,
     how it compares to last month, and 2-4 recommendations.
2. **Revenue, pipeline & deals** — influenced pipeline, deals open/won, deal list with amounts and the campaigns
   that touched them, pipeline-per-$ and ROAS. **Skip this whole section if HubSpot/CRM isn't connected** and
   note that connecting a CRM in ZenABM unlocks it.
3. **Ad spend** — a **pie/donut chart of spend by ad format** plus a spend-per-format breakdown, and an explicit
   verdict: **was this a good budget allocation, or should it be re-allocated?** Name the over- and under-funded
   formats and give the recommended split. Render the chart as **inline SVG** (it must show in the PDF; Chart.js
   only renders in the live HTML, not the PDF export — so use SVG, or SVG plus an optional Chart.js enhancement).
4. **Campaign performance** — every active campaign with impressions, clicks, engagements, spend, CTR, CPC, and
   the MoM change; call out the best and worst, and the best campaign *type*. Compare CTR/CPC context to the
   benchmark table.
5. **Ad performance by inventory type** — for each format the user ran: CTR, raw CPC, effective CTR-to-LP,
   **effective CPC-to-LP**, CPM, each graded ✓/✗ against the benchmark; plus best/worst individual ads. **Also
   include the full ZenABM per-format benchmark reference table (all six formats, including CPM and dwell time)**
   from the Benchmarks reference on the LinkedIn ads & ABM audit skill, so the reader can see where every format
   should land. Link-driving formats are graded on effective CPC-to-LP, not raw CPC.
6. **Top engaged companies** — a full section (not just the exec-summary preview):
   - **Top ~15 engaged companies** with impressions, clicks, engagements and ABM stage.
   - A highlighted list of **companies with 3+ clicks in the month** — a strong buying signal — flagged as
     **likely "Interested"** and the best candidates to route to sales.
7. **Next steps — to implement next month** — a short, forward-looking checklist of the concrete actions to take
   in the coming month (scale the winners, reallocate off the losers, creatives to refresh, accounts to route to
   sales). This is the action list the report ends on.
8. **Footer** — a directional-figures disclaimer.

Aim for a **detailed, elaborate report** — each section gets a short explanatory paragraph plus its data, not
just a bare table. Write for a stakeholder who wants to understand *why*, not only *what*.

## What good looks like

- **Last calendar month, not trailing 30 days.** This is the defining difference from the audit — get the month
  boundaries right and label the report with the month name and year.
- **Never fabricate live numbers** — if a tool returns nothing, say so; don't invent.
- **No CRM → no revenue section.** Skip it and prompt to connect; still deliver the rest of the report.
- **Effective-to-LP needs landing-page clicks;** formats/ads with no link have no LP metric (mark "n/a (no
  link)"). Lead Gen Forms are judged on cost-per-lead (see the Benchmarks reference on the LinkedIn ads & ABM
  audit skill).
- Keep it **report-toned** for a stakeholder audience — summarize and recommend; save exhaustive fix-lists and
  decaying-ad forensics for the LinkedIn ads & ABM audit skill (you can point them to it).
- Treat figures as **directional**, not guarantees — say so on the report. Light mode, self-contained, prints to
  PDF.

## Scheduling (run it every month)

This report is designed to run automatically on the **1st of each month** for the previous calendar month. After
delivering the first report, offer to schedule it (cron `0 8 1 * *`) using whatever scheduling your platform
supports.
