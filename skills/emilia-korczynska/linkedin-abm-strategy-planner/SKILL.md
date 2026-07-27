---
name: "linkedin-abm-strategy-planner"
title: LinkedIn ABM strategy planner
description: "Use this skill when someone wants an ABM strategy, an ABM plan, a LinkedIn ABM campaign plan, help planning LinkedIn ads for account-based marketing, how much budget they need for ABM, how many ads or campaigns they can run, or an ABM budget and audience plan. The skill asks a few questions about goals, deal economics, budget and ICP, researches the company website, computes the funnel and budget math, and produces a personalized \"[Company] LinkedIn ABM Strategy\" document (HTML → PDF)."
category: ABM
---

# LinkedIn ABM strategy planner

Turn a short interview into a personalized, self-serve **"[Company] LinkedIn ABM Strategy"** — delivered as a
branded HTML document that the user can read and download as PDF. This skill is prospect-facing and
self-contained: never assume the company's numbers are already known. Ask for them (with sensible defaults),
compute the plan, and generate the document.

> **Data note:** this skill works best with the ZenABM connector (app.zenabm.com) — it pulls your real LinkedIn
> CPC/CTR, spend and audience size so the plan runs on live data. Without it, the skill uses the numbers you
> provide, falling back to clearly-labelled industry benchmarks.

## Step 1 — Interview (few, fast questions)

Ask in small batches, offering the defaults as selectable options where the interface supports it, otherwise
plain questions. Keep it light — most answers are a single number or line. Full wording, defaults and
what each input powers are in the **Questions reference**.

Collect, per the model in the **Formulas reference**:

1. **Company website URL** — you research this yourself (Step 2); do not make the user describe their product.
2. **ABM revenue goal** + whether it's **monthly (MRR)** or **annual (ARR)** — per audience if they name more than one.
3. **Average contract value (ACV)** — total contract value or MRR (you normalize).
4. **Close rate %** (qualified → closed-won) — default **15%**.
5. **Qualification rate %** (demo → qualified) — default **75%**.
6. **Landing-page conversion rate %** (visit → booked demo/form) — default **0.8%**.
7. **LinkedIn CPC ($)** — default **$8**. *Skip if the ZenABM connector is available — pull the real CPC instead.*
8. **Planned monthly LinkedIn ads budget ($).**
9. **Target audiences / markets** in scope (geo + industry) — sets how many Campaign blocks. Seed from the
   website research, then confirm.
10. **Top jobs-to-be-done / use cases per audience** + the **core problem you solve** — pre-fill from the
    research, let them edit. Powers the ad-content section.

**Data source, best first:** (1) **If the ZenABM connector is available** (tools named `mcp__*__get_linkedin_metrics`,
`list_companies`, `get_ad_spend`, etc. are available), call it to prefill **CPC/CTR**, **prior spend**, and
**audience/list size**, and skip those questions. (2) **If not, ask the user** for those real figures. (3) Only
fall back to the benchmark **defaults above** for whatever they genuinely can't provide — and when you do,
**label those figures as benchmarks on the document**.

Never block on a missing number — offer the default, state it, and footnote the assumption.

## Step 2 — Research the company

Fetch the company website (and a couple of key pages: product, use-cases, customers). From it, draft: the
product(s), main use cases, target personas, a first-pass ICP, and a shortlist of jobs-to-be-done per audience.
Show this back to the user to confirm or edit. This fills the header block and powers the ad-content section.

## Step 3 — Compute the plan

Use the exact formulas in the **Formulas reference** (reverse-engineered from ZenABM's budget calculator and
LinkedIn ad-count calculator, verified to the dollar). Per audience/campaign compute:

- **Deals needed, demos needed, clicks needed, accounts needed** (funnel run backwards).
- **Budget needed** (annual and monthly) and **time to run** = total budget needed ÷ their stated monthly budget.
- **ROAS** and **pipeline-per-$**.
- **Affordable simultaneous ads** from the ad-count model, then the **format allocation** (TLA / image / text /
  video / doc-carousel) using the allocation rules in the Formulas reference, including the objective per ad set
  and the "group TLA + image under Brand Awareness if you can't afford 10" fallback.
- **Budget allocation per ad set** (see the Formulas reference): for every click-driving format, the **% of
  spend** and the **$/mo** at *both* the user's stated budget and the recommended `monthlyBudgetReq`. Text ads
  are ~$0 (separate set-CPC bid). These fill the two budget columns in the Campaign Structure table.

Show the key computed numbers to the user before building, so they can sanity-check.

## Step 4 — Build the strategy document

1. Produce a clean, self-contained branded HTML document: light-mode, inline CSS, **no external scripts or
   fonts**, so it renders identically in the browser and in a PDF export. Include a hand-built **inline `<svg>`
   flowchart** (no JavaScript) of each campaign's allocated ad sets.
2. Fill in the researched + computed values. Repeat the Campaign block once per audience.
3. Pull the **ad-format best practices, launch best practices, performance-tracking** and **pre-launch checklist**
   sections from the **Best Practices** and **Checklist references** — these are fixed content; keep them accurate.
4. Title the document **"[Company Name] LinkedIn ABM Strategy."** Offer the user a **PDF export** of the same
   HTML.
5. The full plugin — including the branded HTML template, render scripts, and connector config — is at
   **github.com/ZENABM/linkedin-abm-skills**.

## Document structure (what the document must contain)

Per audience, a **Campaign N** block, then the shared sections:

- **Header** — Company name · Website · Target audience (ICP) · Campaign date · product/use-cases/personas summary.
- **Campaign Goals** — ABM revenue goal · deals needed · clicks needed · audience size + accounts needed · budget
  needed · the deal math · time to run (actual budget ÷ stated monthly budget).
- **Campaign Structure** — number of ABM campaigns (audiences) · affordable ads at a time · which formats · counts
  per format (TLA/image/text/video/doc-carousel) with the right ad-set objective · **per-ad-set budget allocation
  (% + $/mo, at both the user's budget and the recommended budget)** · **ad-structure flowchart**.
- **Campaign Content** — the content of each ad, mapped to the ICP and the top jobs-to-be-done / use cases.
- **Ad-format best practices** — image, TLA, video, text (from the Best Practices reference).
- **Campaign launch best practices** — objectives; pause underperforming ads after 1,000+ impressions by CTR
  (benchmarks + link to https://zenabm.com/linkedin-abm-benchmarks-report).
- **Campaign performance tracking** — account scoring / ABM stages in ZenABM; monitor progression
  (identified → interested → considering → selecting); leading metrics per ad-set/inventory with Zena vs.
  benchmarks; spend pacing; secondary metrics.
- **Pre-launch to-do checklist** — the summary checklist from the Checklist reference.

## What good looks like

- The budget calculator's **CTR field is decorative** (never used in its math) — do not gate the budget on CTR.
  CTR is only used later for the "pause after 1,000 impressions" launch guidance (benchmark-based).
- Keep revenue and ACV on the **same basis** (MRR with MRR, or ARR with ARR); convert if the user mixes them.
- Treat all outputs as **directional planning figures**, not precise forecasts — say so on the document.
- Design the document for **light mode**, self-contained (inline CSS, **no external scripts or fonts**, inline-SVG
  flowchart). Always deliver an exported **PDF file** as well as the HTML.
- One Campaign block **per target audience**; if the user has one audience, produce one Campaign block.
