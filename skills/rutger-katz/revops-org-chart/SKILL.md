---
name: "revops-org-chart"
title: RevOps org chart and team design
description: "RevOps team org design, role structure, and hiring sequencing by company size and ARR stage. Use whenever a client asks about structuring their RevOps team, hiring order, business partner vs. center-of-excellence model, when to engage a Systems Architect (FTE, fractional, or advisory), evolving a CRM or automation team toward RevOps, who RevOps should report to, how to give RevOps a mandate or charter, centralized vs. embedded vs. hub-and-spoke model, multi-BU or multi-instance team design, or how to use agencies without creating dependency. Also trigger when a client has Business Partners and is theorizing about adding an Architect role. Includes frameworks from RevOps Co-op, Revenue Wizards, Hyperscayle, Go Nimbly, Maxio, Leanlayer, Stage2 Capital, and a practice-based hiring guide."
category: RevOps
---

# RevOps Org Chart & Team Design

## Purpose
Answer client and prospect questions about RevOps team structure, role sequencing, and evolution. Apply through a systems lens: RevOps is the steward of the revenue system; not a report factory or CRM admin function.

Always frame org design advice in terms of **outcomes and identity**:
- What does the leader gain (forecast trust, steerability, fewer fire drills)?
- Who does the RevOps person become (system owner vs. spreadsheet janitor)?
- What changes in their week?

---

## Quick Reference: Team Size by Stage

| ARR / Stage | Team Size | First Hire | Key Additions |
|---|---|---|---|
| <€5M / pre-scale | 0-1 | Generalist consultant or fractional | N/A |
| €5-15M / early | 1 | RevOps Manager (generalist) | CRM Admin |
| €15-30M / growth | 2-3 | + Analyst | RevOps Manager |
| €30-75M / scale | 4-6 | + Ops Leads (proto-BPs) | BI/Insights Manager |
| €75-150M / mature | 7-10 | + FTE Architect | Marketing Ops Lead, CS Ops Lead |
| €150M+ / enterprise | 10+ | Full hub-and-spoke | VP RevOps, full functional split |

**Note on the Architect:** FTE hire is a late-stage move, but Architect *engagement* is not. A fractional or advisory Architect adds disproportionate value earlier; especially during platform launches, revenue architecture rollouts, or when the internal team is technically junior. Think of it as a spectrum: advisory → fractional → FTE, not a binary 0/1.

**Staffing ratios (Leanlayer portfolio data, based on Insight Partners benchmarks, 2026):**
- AE:RevOps = 4:1 (small teams) → 12.2:1 (100+ AEs)
- Revenue:RevOps FTE = 11:1 (€0-10M) → 15:1 (€50-100M)
- Budget rule: 5-10% of total GTM budget for mature RevOps (Squad4, 2026)

---

## The Four Archetypes (never confused)

**1. Generalist Manager**: always first hire; connective tissue between strategy and execution. Never opens CRM to change a field. Ratio: 1 generalist per 5 experts.

**2. Business Partner** (Sales/Marketing/CS Ops Lead): embedded ops point of contact aligned to a GTM function. Owns function-specific workflows, reports, and process design. NOT the first hire.

**3. Systems Architect**: designs the revenue tech stack for scale. Owns: data model, integration architecture, CRM architecture, automation framework, tool selection. Explicitly NOT an admin. Requires: coding (JS/Python), data architecture, executive communication.

**4. Analyst**: data, reporting, ad-hoc insight. Subject matter expert. Never the first hire; scales in clusters once the generalist is in place.

---

## AI Governance & Agentic Automation Roles (New for 2026)

By early 2026, 73% of RevOps teams embedded AI in GTM stacks (LeanData, 2026). Agentic automation (autonomous workflows, AI SDRs, predictive scoring) is no longer novel; it's table stakes. The question is no longer "do we use AI?" but "who owns the governance layer?"

RevOps typically inherits three new accountability areas:

**1. Prompt Engineer / Agent Architect** (€30M+ ARR or high automation intensity)
Owns: AI model prompts for customer-facing agents (lead scoring, routing, forecasting), fine-tuning triggers, failure modes. Unlike a general AI/ML hire, this is tactical RevOps-specific work (not data science). Sits in the Systems team. Often fractional at first.

**2. AI Governance / Agent Oversight Lead** (€75M+ ARR or multi-agent orchestration)
Owns: data readiness for agents (60% of AI projects abandoned over non-agent-ready data; Gartner, 2026), model monitoring, impact tracking, compliance (EU AI Act, GDPR for enrichment agents). Bridges RevOps and Legal/Compliance. Executive-facing.

**3. Agentic Process Owner** (Any stage)
Owns: which processes qualify for agent automation, pilot runways, change management when agents replace manual work. Usually embedded in Business Partner role or Analyst. Does not require coding; requires process discipline.

**When to engage:**
- Platform shift to outcome-based agent pricing (HubSpot Breeze Agents; Salesforce Agentforce): Architect reviews cost model and automation ROI.
- Agent pilot live (lead scoring, nurture, forecast): Governance lead owns data quality checks and success metrics.
- Beyond 10 agents in production: dedicated oversight, not ad-hoc.

**Hiring sequence for AI governance:**
At €30M, fractional prompt engineer within Architect role. At €50M, dedicated agent oversight (often a promoted analyst). At €75M+, formal Governance Lead reporting to Head of RevOps. The Architect always owns the orchestration layer; governance lead owns the monitoring and compliance.

**Departmental Model** (Go Nimbly / early-scale)
Sales Ops, Marketing Ops, CS Ops as separate teams under Head of RevOps. Good for €15-50M. Risk: re-siloing.

**Functional / Hub-and-Spoke Model** (RevOps Co-op Stage 3-4 / mature)
Systems team + Insights team + Enablement team, each serving all departments. Business Partners are spokes; Architecture and Analytics are the hub. Good for €50M+.

**Flat Structure**: minimal hierarchy, empowered ICs. Early-stage startups only. Does not scale past €15M without explicit governance.

---

## The Org Chart Evolution (RevOps Co-op Model)

Stage 1: **Siloed**: Ops people report to department VPs; gets deprioritized behind quota targets.

Stage 2: **Departmental**: All ops under one RevOps manager, organized by function they support (Sales Ops, Marketing Automation, Salesforce Admin). Conflict: API limits, data conflicts, no authority to say no.

Stage 3: **Functional Specialization**: Reorganize by capability, not department. **Systems team** (Architects + Admins) and **Insights team** (Analysts). Manager of Systems team should have been a Systems Architect. *This is the critical transition.*

Stage 4: **Evolved**: Enablement joins RevOps. Cross-functional PMs and Analysts. Agile methodologies. Quarterly "ride-alongs" where ops staff shadow end users.

---

## When to Engage the Systems Architect

The Architect is not a binary hire. Engagement comes in three modes; match the mode to current complexity and team maturity:

| Mode | When | What they do |
|---|---|---|
| **Advisory** | Any stage; especially at platform launch or architecture inflection points | Periodic sparring partner; reviews decisions; catches structural mistakes before they compound |
| **Fractional** | Team is junior, or complexity is high but FTE isn't justified yet | Owns specific deliverables; available for escalations; transfers knowledge intentionally |
| **FTE** | Team has 3-6+ RevOps people; 10+ tools with active integrations; architectural decisions are a weekly bottleneck | Fully embedded; owns the entire systems layer |

**Trigger for any engagement (advisory minimum):**
- Launching a new CRM or revenue architecture (HubSpot, bowtie implementation)
- Integrating 3+ systems with bidirectional data flows
- Internal team is technically capable but architecturally junior; good at configuring, not at designing for scale
- Multi-BU complexity where one team's changes break another's processes
- Platform shift affecting cost model or automation path (see Platform Shifts & Architecture Implications below)

**What the Architect owns (regardless of mode):**
- End-to-end system architecture; not day-to-day admin
- Integration design and data flows
- Underlying data model and single source of truth
- Business process → technology translation (process drives tech, never the reverse)
- Workflow automation and reference architecture documentation

## Platform Shifts & Architecture Implications (2026)

Three major platform shifts reshape Architect engagement and cost models:

**HubSpot Breeze (April 2026 onward)**
Outcome-based agent pricing: Customer Service Agent €0.50 per resolved conversation, Prospecting Agent €1.00 per recommended lead (HubSpot, 2026). Agentic Automation Builder replaces workflows + agents. Impact on Architect: must model agent cost per use case, recommend advisory/fractional Architect engagement to optimize routing and qualification logic before scaling agents (cost blowup risk if agents churn low-quality leads). Architects unfamiliar with agent economics should engage external guidance.

**Salesforce Agentforce & Data 360 (Current state 2026)**
Workflow Rules and Process Builder end of support 31 December 2025; Flow is the only automation forward path (Salesforce, 2026). Agentforce 360 consumption-model pricing. Data 360 (formerly Data Cloud, October 2025) is now the agent intelligence foundation. Flow Logging (Spring 2026) enables debug visibility. Impact on Architect: Architects designing new Salesforce implementations now MUST scope as Flow-first, not WR/PB, and must integrate Data 360 for agent context. Existing implementations running on deprecated automation paths need migration roadmaps. Advisory/fractional Architect strongly recommended for clients at inflection points.

**Multi-Agent Orchestration (€50M+ ARR or 10+ agents in production)**
When a company runs 10+ autonomous or semi-autonomous agents (lead scoring, nurture, forecasting, forecasting adjustment), the Architect role expands to orchestration governance: Which agent owns which decision? What's the data contract between agents? Where do conflicts surface? Impact on hiring: at this scale, FTE Architect is non-negotiable; consider a dedicated Agent Orchestration lead within the Architecture team.

---

**The Architect ≠ Admin distinction:** Admin configures the platform within an existing framework. Architect designs the system for scale. An Admin who becomes an Architect needs a mandate, new skill investment, and explicit separation from ticket work. The transition rarely happens without external scaffolding.

**Hiring rubric: screening Architect from Admin**

Use this when evaluating whether a candidate or internal promotion fits the Architect role (vs. Admin/specialist):

| Signal | Architect Hire | Admin Hire |
|---|---|---|
| **Problem approach** | Asks "how do we structure this for growth?" before tool selection | Asks "which field do we add?" |
| **System thinking** | Can map how a change in one area breaks another; thinks in data flows | Strong in single-tool depth; functional fix-focused |
| **Technical foundation** | Coding skills (JS/Python) or data engineering; pipeline orchestration experience | Strong platform certification; workflow/automation builder certified |
| **Communication** | Can explain architecture decisions to executive stakeholders who don't know Salesforce | Speaks fluent Salesforce; struggles to abstract patterns to non-technical audience |
| **Scaling questions** | "How do we ingest data from 5 sources consistently?" | "How do we report on this metric?" |
| **Failure learning** | Dissects why an approach failed; iterates on architecture | Debugs the immediate error; ships the fix |

**Interview focus for Architect role:**
1. Walk me through a tech stack integration (3+ systems) you designed. Where did it break and why? (Tests architecture thinking and scaling awareness.)
2. Describe a time you said no to a request because it violated your data model. What happened? (Tests governance instinct and authority.)
3. Code sample: show me a script you wrote to orchestrate a workflow or sync data. (Tests technical foundation.)
4. Explain your current CRM to someone who has never seen it. (Tests abstraction and communication.)

---

## Business Partner + Architect Coexistence

The hub-and-spoke model at maturity (7-15+ people):

```
VP / Head of RevOps
├── Systems / Architecture (Hub)
│   ├── RevOps Architect
│   ├── CRM Admin(s)
│   └── Data Engineer / Integration Specialist
├── Business Partners (Spokes)
│   ├── Sales Operations Lead
│   ├── Marketing Operations Lead
│   └── CS Operations Lead
├── Analytics & Insights
│   └── RevOps Analyst(s)
└── Enablement
    └── Revenue Enablement Manager
```

**Division of labor:**
- Architect: centralized infrastructure, data model, integration layer, standards
- Business Partners: function-specific workflows, reports, process design (within Architect's standards)
- When a Business Partner needs an architectural change → brings to Architect
- Architect ensures one function's request doesn't break another's process

**OpenAI model (Maxio):** Two branches: Systems (tech stack, integrations, data infrastructure) and Strategic (planning, forecasting, process design). Architect leads Systems. Business Partners sit in Strategic.

---

## For Clients Transitioning from Business Automation / CRM Teams

A Business Automation team is the natural predecessor to RevOps. The transition requires:

1. **Mandate shift:** From "configure what's asked" → "steward how revenue runs on the platform"
2. **Governance charter:** Explicit authority to own definitions, say no to random requests, manage change control
3. **Role evolution:** Existing admins can grow toward Analyst or Architect; existing leads can grow toward Business Partner
4. **Gap to fill:** Process authority and business partnership skills; the technical foundation is already there

The constraint is rarely technical. It's governance. Read the Governance Model 0.3 file for the framework.

---

## Reporting Lines & Political Standing

Where RevOps sits determines what it can do. There is no neutral answer.

| Reports to | What it enables | What it limits |
|---|---|---|
| **CRO** | Fast Sales alignment; natural authority over pipeline and forecast | Marketing and CS feel under-served; harder to challenge sales data |
| **CEO / COO** | Genuine neutrality across functions; authority to set definitions without political debt | Can feel distant from the commercial engine; harder to get traction on Sales priorities |
| **CFO** | Credibility with finance; strong on metrics and forecasting rigour | Risk of over-indexing on reporting vs. execution; CS and marketing deprioritised |
| **VP Sales** | Maximum Sales alignment at early stage | Becomes Sales Ops, not RevOps; Marketing and CS lose trust immediately |

**Default recommendation for €15-75M scale-up:** Report to CRO or CEO/COO. Reporting to CFO works if the CRO role doesn't exist yet and the company runs forecast-first. Reporting to VP Sales only works as a transitional arrangement; it signals to Marketing and CS that RevOps is not theirs.

**The political test:** Can RevOps say no to a VP Sales request that would break a shared process? If not, it doesn't matter who they report to; the authority isn't real.

---

## Function Mandate & Charter

RevOps without a mandate is just a ticketing function with a better job title.

A RevOps charter defines four things explicitly:

**1. Decision rights**: What RevOps owns outright (definitions, data model, stage names, metric cards, cadence structure), what requires RevOps sign-off (new tool purchases, field additions, workflow changes), and what RevOps advises on but doesn't block.

**2. Change control**: No definition, field, or process change goes live without an owner, an effective date, and a logged reason. RevOps is the gatekeeper, not the bottleneck. The distinction matters: a gatekeeper has a clear process and SLA; a bottleneck doesn't.

**3. Backlog authority**: RevOps maintains a visible, prioritised backlog of system changes and improvements. Stakeholders request; RevOps triages and sequences. Random asks that don't fit the roadmap are declined with a reason, not silently deprioritised.

**4. Governance sponsorship**: The charter must be signed off by whoever RevOps reports to. Without executive cover, the mandate is theoretical.

For clients transitioning a Business Automation team → RevOps: the charter is the single most important document. The technical capabilities often exist already. The mandate does not.

See `references/operations.md` for a charter template and backlog triage framework.

---

## Centralized vs. Embedded Model

The perennial debate. Both are right in different contexts.

**Centralized (Center of Excellence)**
- One RevOps team serving all GTM functions as a shared service
- Owns all definitions, data, and systems centrally
- Business Partners may exist as relationship managers but report into RevOps, not into Sales/Marketing/CS
- *Best for:* single-motion GTM, strong RevOps leader, €15-100M ARR with one product line
- *Risk:* functions feel under-served; RevOps becomes a queue

**Embedded Model**
- Ops people sit within (and report to) their aligned function
- Faster response; deeper domain knowledge
- *Best for:* fast-moving orgs, large GTM teams where context matters more than consistency
- *Risk:* re-siloing within 6-12 months; data model drifts; no one can say no across functions

**Hybrid / Hub-and-Spoke** (recommended for €50M+ or multi-BU)
- Central hub owns: data model, governance, architecture, shared definitions, cadence standards
- Embedded spokes (Business Partners) own: function-specific execution within those standards
- Spokes report into RevOps (dotted line to function head) or directly into function head (dotted line to RevOps)
- *The reporting line for spokes matters:* dotted line to function head = RevOps credibility but execution proximity; direct report to function = speed but risk of drift

**The question to ask:** Can your centralized team make a binding decision that affects Sales without Sales VP approval? If yes, centralized works. If no, you need embedded spokes with enough central governance to hold the shared layer together.

---

## Multi-BU / Multi-Instance Team Design

When one company runs multiple BUs with separate CRM instances and different maturity levels, the standard org chart breaks down. Multi-BU enterprises at scale (especially software companies) handle this through shared governance layers and local autonomy.

**The core tension:** BUs need autonomy to run their own motion. The company needs comparability to make cross-BU investment decisions.

**Design principles:**

1. **One shared definitions layer, local implementations.** Bowtie stage names, metric codes (VM/CR/Δt), and data model standards are set centrally. Each BU defines its own trigger events, bands, and local workflows within that schema. Don't merge instances; share the dictionary.

2. **One Systems Architect (fractional or FTE) across all BUs.** The Architect owns the interoperability contract between instances; how data surfaces up for cross-BU reporting without requiring a merge. This is the role that cannot be fragmented per BU.

3. **One Business Partner per BU.** Each BP serves their BU's operational needs. They work within the shared schema but own the local implementation. BPs need to communicate with each other; a monthly cross-BU sync is minimum governance.

4. **Maturity-adjusted expectations.** Don't apply a uniform maturity target across BUs. Run a quick scan per BU, plot them on the same model, and let leadership see the spread. This prevents the highest-maturity BU from being held back and the lowest-maturity BU from being crushed by requirements they can't meet.

5. **Governance before automation.** In a multi-BU context, the temptation is to centralize reporting via a data warehouse. That's correct eventually. But if the upstream definitions across 4 BUs are inconsistent, you're building a warehouse on top of 4 different languages. Fix the dictionary first.

**Team structure example: multi-BU enterprise at ~250M ARR, 4 BUs**
```
Head of RevOps / Business Automation
├── Systems Architect (fractional or FTE): cross-BU orchestration
├── Business Partner: BU 1 (Sales motion)
├── Business Partner: BU 2 (Mid-market motion)
├── Business Partner: BU 3 (Channel/Partnerships motion)
├── Business Partner: BU 4 (Services/Managed motion)
└── Analyst(s): cross-BU reporting and data enablement
```

---

## Key Sources

See `references/sources.md` for full source summaries and URLs.
See `references/operations.md` for: RevOps charter template, backlog triage framework, fractional/agency/in-house tradeoffs.

Primary sources:
- RevOps Co-op: evolutionary org chart model (4 stages, explicit Architect roles)
- Revenue Wizards: seven-tier FTE breakdown by company size
- Hyperscayle: maturity-level visual org chart (5 levels, GTM complexity lens)
- Go Nimbly: three structural models comparison
- Maxio: team structures by size with OpenAI Systems/Strategic split
- Stage2 Capital: hiring sequencing and RevOps Co-op endorsement
- Leanlayer: team size calculator with ratio benchmarks
- Practice-based hiring guide: role structures at 4 team sizes (1-3 / 4-6 / 7-10 / 10+)

> Built by [Neon Triforce](https://neontriforce.com)

---

## Operator Templates: Competency Matrices

For CS/AM and management hiring and calibration:

**Account Management Competency Matrix:** `Frameworks/Templates/cro-school/account-management-competency-matrix-neon.xlsx`
Use in: CS maturity assessments, AM performance reviews, hiring rubrics.

**Management Competencies Matrix:** `Frameworks/Templates/cro-school/management-competencies-matrix-neon.xlsx`
Use in: Manager hiring, org design, succession planning.

Original sources: `Sources/Courses/CRO-School/CRO School Class #4 Template - CS Fundamentals - Account Management Competency Matrix.xlsx` + `Management Competencies Matrix.xlsx`
Attribution: Adapted from Pavilion CRO School. Original author: Carter/Nalbandian/Dick.
