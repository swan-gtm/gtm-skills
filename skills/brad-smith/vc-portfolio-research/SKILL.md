---
name: "vc-portfolio-research"
title: VC portfolio research
description: "Use this skill when preparing for a meeting with a VC, PE, or accelerator partner and you need to know how their portfolio companies use your product — paste the firm's portfolio URL and get a demo-safe, partner-facing analysis (product penetration, plan mix, usage, AI adoption, open pipeline) plus a separate internal sheet with the full account-level financial detail. Built for partner and emerging-customer teams; turns hours of manual portco research into one structured run."
category: Research
---

# VC portfolio research (demo-safe)

Analyzes a venture capital or private equity firm's portfolio companies to surface how those companies use your product — product penetration, plan mix, usage, AI adoption, and open CRM pipeline.

The core judgment is the **demo-safe split**: the partner-facing document excludes all financial figures (no ARR, revenue, or deal amounts). A separate internal spreadsheet keeps full account-level detail — including ARR — for your team only.

**Typical trigger:** paste a firm portfolio URL and ask for a usage / portco analysis, or a "demo-safe portfolio summary."

**One-liner:** paste a VC/PE portfolio URL → the skill runs → you get a partner-safe doc of product usage, AI adoption, and pipeline across the portfolio, plus an internal sheet with the ARR detail your team needs.

## How it runs

1. **Extract the portfolio** — fetch and parse the firm's portfolio page (with fallbacks for JS-rendered sites; a pasted company list works when the site doesn't scrape cleanly).
2. **Match accounts by email domain** — resolve each portfolio company to an account in the data warehouse: paying status, plan type, tasks used (past 30 days), AI feature milestones, and ARR.
3. **Pull open pipeline** — open CRM opportunities by company domain (deal name, stage, close date, owner).
4. **Produce the two-artifact output** (below), then update a **portfolio registry** entry (firm, date, doc/sheet links, portco → domain → account IDs) so downstream skills — like pipeline-overlap analysis — can reuse the portfolio mapping without re-scraping.

## Outputs

Three artifacts in a shared drive, under `Partners > {Firm Name}`:

- **Folder — `{Firm Name}`** — container for the doc + sheet.
- **Partner-facing doc — `{Firm Name} — Portfolio Analysis`** (demo-safe, no financials): executive summary of the portfolio footprint; paying-vs-free penetration and plan-tier view; usage and AI-adoption highlights (feature-level, not dollars); open opportunities with **no amounts**; additional insights (upsell angles, growth signals, greenfield list); and an appendix on match quality and ambiguous domains. Default sharing: internal domain only — an external link is created **only with explicit confirmation**.
- **Internal sheet — `{Firm Name} — Account Data`** (never shared externally): account IDs, domains, ARR, plan, paying status, tasks (30d), plus a summary tab with the portfolio financial snapshot and plan breakdown.

## When to use it

- Preparing for a partner meeting with a VC/PE firm
- Building a demo-safe portfolio readout to share externally (after confirmation)
- Mapping product footprint and AI adoption across a fund's companies
- Feeding the portfolio into later pipeline-overlap work

## When NOT to use it

- Single-account ARR lookups
- General product questions
- Partnership strategy without a portfolio data pull

## Prerequisites

- A data-warehouse connection (Brad's implementation: Databricks via MCP, with the CRM's deal/company tables synced into the warehouse)
- A docs/sheets/drive connection for the output artifacts (his implementation: Google Workspace via the Zapier MCP)
- A portfolio URL — or a pasted company list if the site doesn't scrape cleanly

## What good looks like

The partner doc contains zero dollar figures anywhere — penetration, plans, usage, and pipeline stages tell the story without ARR. External sharing never happens by default; it is gated on an explicit confirmation. The internal sheet stays internal, always. Ambiguous domain matches are disclosed in the appendix rather than silently counted. And the portfolio registry is updated on every run, so the next skill that needs this firm's portco mapping starts from the registry instead of re-scraping.

---

*This page documents Brad's production workflow at Zapier, where it runs as a Cursor Agent Skill against their warehouse. The pattern — a demo-safe external doc, an internal-only financial sheet, and a reusable portfolio registry — replicates on any warehouse + CRM + docs stack.*
