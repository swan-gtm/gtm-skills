---
name: "warm-intro-intelligence"
title: Warm intro intelligence
description: "Use this skill when a rep wants warm intro paths into a target prospect — \"Find warm intro paths for [company]\", \"Who do we know at [company]?\", \"Can anyone intro me to [role] at [company]?\", \"Warm intro - [company]\". Surfaces the strongest available warm intro paths from your company's relationship network — employees, customers, partners, investors, advisors, call transcripts — with honest, evidence-based confidence labels. Decision support only: never contacts anyone, never writes to the CRM. The rep always decides."
category: ABM
---

# Warm Intro Intelligence

## Template placeholders

- `{{COMPANY_NAME}}` — Your company's name.
- `{{COMPANY_DOMAIN}}` — Your company's email/website domain (e.g. `acme.com`). Also used to filter your own employees out of partner data.
- `{{TEAM_ROSTER}}` — A sub-page you build and maintain: every employee at your company with LinkedIn handle and full career history. Build instructions are in the Node Registry sub-page.
- `{{INVESTOR_REGISTRY}}` — A sub-page you maintain: your company's investor firms plus (ideally) the named individual partners. Build instructions are in the Node Registry sub-page.
- `{{CUSTOMER_LIST}}` — Your CRM's source-of-truth list of active customers (examples assume HubSpot; adapt to your CRM).
- `{{PARTNER_LIST}}` — Your CRM's partner list or custom object (name/view of your partner records).
- `{{HUBSPOT_PARTNERS_OBJECT_ID}}` — The objectTypeId of your partners custom object, if you store partners as a HubSpot custom object (e.g. `2-XXXXXXXXX`).
- `{{PERSONA_MAP}}` — Your segment → buyer-persona priority table (from your ICP qualification process): for each ICP segment, the primary personas and fallbacks.

## Purpose

On-demand play that surfaces the strongest available warm intro paths from your company's relationship network to a target prospect.

Triggered by natural language such as: "Find warm intro paths for [company]", "Who do we know at [company]?", "Can anyone intro me to [role] at [company]?", "Warm intro - [company]", or similar intent.

Output is decision support only. The agent never contacts anyone, drafts outreach to connectors, or takes any action. The rep always decides.

---

## Step 1 - Resolve Input

Determine what the rep provided:

- **Specific contact named** -> target that contact only. Skip Steps 2 and 3. Go directly to Step 4.
- **Persona or role specified** -> go to Step 3b to find matching contacts at the prospect.
- **Company only** -> go to Step 2.

---

## Step 2 - ICP Segment Classification (company-only input)

Check the company record and account memory for an existing ICP classification.

- Valid classification found -> use the stored segment. Note whether it is confirmed or inferred.
- No classification or expired verdict -> run lightweight enrichment (company description, website scrape, CRM data) to infer the segment. Do NOT run your full ICP qualification gate - this is for persona selection only, not outreach gating. Flag the segment as inferred in the output.

Using the segment, identify up to 3 most relevant buyer personas using `{{PERSONA_MAP}}`. Use the primary persona column for the matched segment, then fallback personas if needed.

Prioritize by: segment fit, use case relevance, persona responsibilities, and seniority - in that order. Do not apply a generic seniority hierarchy. The segment determines persona priority.

Proceed to Step 3a.

---

## Step 3a - Find Target Contacts at the Prospect

Pull CRM contacts associated with the prospect company. Also run LinkedIn enrichment to find people matching the identified personas who may not yet be in the CRM.

For each matched contact, collect:
- Full name, current title, company
- LinkedIn URL
- CRM contact ID (if exists)

Limit to 3 target contacts. If no contacts are found for a persona, note it in the output - do not skip silently.

---

## Step 3b - Persona-Specified Input

Find contacts at the prospect matching the specified persona using CRM contacts and LinkedIn enrichment. Follow the same process as Step 3a but filtered to the specified persona.

---

## Step 4 - Query the Node Registry and Compute Edges

Load and follow the Node Registry and Edge Discovery sub-page of this skill.

For each target contact identified in Step 3, query each node type in the registry to find potential bridge nodes with a plausible connection to the target.

Also run the Champion Migration check from the Known Contacts (Relationship Pool) node: build the relationship pool and test whether any pool member now works at the target account. This flips the question from "who shares history with the target contact?" to "does someone your company already knows now work here?" Each hit is a candidate 1-hop path. Run this only for qualified/target accounts (the cost gate is defined in the node registry). If two or more pool members work at the target, record the team-migration cluster as informational awareness only - it does not affect confidence or ranking.

Track which sources were checked vs. unavailable - this appears in the output card footer.

---

## Step 5 - Assess Edge Confidence

Load and follow the Evidence Rules and Confidence Scoring sub-page of this skill.

For each edge found, determine:
- Confidence tier: Verified / Moderate / Inferred
- Evidence detail and source
- Last verified / last interaction date
- What is unknown
- Why it may still be worth checking
- What would increase confidence on this edge

---

## Step 6 - Score and Rank Paths

Path confidence = weakest edge in the path:
- Weakest edge Verified -> **Strong**
- Weakest edge Moderate -> **Medium**
- Weakest edge Inferred -> **Low**

Apply the full ranking logic defined in the Evidence Rules and Confidence Scoring sub-page (Path Ranking section) - confidence tier, then recency weighting, then persona priority, then hop count. That section is the single source of truth for ranking; do not re-derive it here.

Select top 2 paths. Prefer paths targeting different personas where evidence quality allows. If both top paths target the same persona, note that no strong alternative path to a second persona was found.

Always return the best available paths regardless of confidence level. Never return an empty result.

---

## Step 7 - Context Enrichment (runs on the final top 2 paths)

Now that the top 2 paths are scored and ranked, run a supplementary context lookup for each. This step enriches the output with recent public signals - it does not affect confidence tiers or path ranking, and must never re-order the paths chosen in Step 6.

For each of the top 2 paths, search for co-mentions between the bridge node and the target prospect contact:

1. **Web research:** Search for the bridge's name and target contact's name appearing together in press articles, conference panels, published interviews, co-authored content, or public announcements. Run a web research query combining both names and their companies.

2. **LinkedIn posts:** Use a LinkedIn post scraper (e.g. an Apify actor) to pull recent public posts from both the bridge's and the target contact's LinkedIn profiles. Look for: mutual mentions, replies to each other's posts, shared content, or posts referencing the same event or topic. Requires a LinkedIn URL for both parties - if either URL is missing, note it and skip the LinkedIn scrape for that path.

Record any co-mentions found with: source, date, and a one-line description of the shared context.

If nothing is found, do not add a context section - omit it entirely rather than noting "no context found."

This step costs one web research call and up to two scraper runs per path. Run only for the final two paths, not for all paths discovered during edge computation.

---

## Step 8 - Warm Relationship Intake Check

Load and follow the Warm Relationship Intake sub-page of this skill.

Check both conditions:
- Any Inferred edge involves the rep who initiated the play -> send on-demand Slack confirmation prompt to that rep (and only that rep - intake never messages anyone else).
- All paths are Low confidence -> add gap-triggered prompt to the output card (no Slack message).

---

## Step 9 - Generate Output Card

Load and follow the Warm Intro Output Card Format sub-page of this skill.

Deliver the completed output card in chat. No tasks created. No CRM writes. No outreach initiated. No one is contacted.

---

## What good looks like

- Every confidence tier traces to record CONTENT that was actually read - never to a meeting count, an email count, or a title. Honest under-labeling protects rep trust; a single false-Strong path destroys it.
- Every path names its weakest edge explicitly, so the rep can see the gap without reading all edge details.
- The card always shows what was checked and what wasn't - the sources footer is never omitted.
- The best available paths are always returned, fully labeled, even when everything is Low - never an empty result, and never an inflated one.
- Nothing was sent, written, or contacted. The rep decides.
