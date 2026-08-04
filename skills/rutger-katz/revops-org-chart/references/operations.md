# RevOps Operations Reference
## Charter, Backlog, Fractional/Agency Guidance

---

## RevOps Function Charter (Template)

Use this to formalize the RevOps mandate when transitioning from a CRM/automation team, or when RevOps has existed informally and needs authority to operate properly.

**Section 1: Purpose**
> [Team name] owns the operational infrastructure that revenue runs on: definitions, data model, systems, cadence, and change governance across [Sales / Marketing / CS / Finance]. Our job is to make the revenue engine steerable, not to report on it.

**Section 2: Decision Rights**

| Domain | RevOps Owns Outright | Requires RevOps Sign-off | RevOps Advises |
|---|---|---|---|
| Data definitions | Stage names, metric codes, lifecycle status values | New custom properties, field additions | Naming conventions for local objects |
| Systems | Integration architecture, automation framework, tool deprecation | New tool purchases >$X/year | Tool configuration within existing stack |
| Process | Cadence structure, handoff SLAs, qualification criteria | Changes to pipeline stages, funnel definitions | Function-specific playbooks |
| Reporting | Shared dashboards, metric cards | New board-level metrics | Function-level reports |

**Section 3: Change Control**
- No definition, field, stage, or automation change goes live without: (1) a named owner, (2) an effective date, (3) a logged reason in the change log.
- Emergency changes (system down / data corruption): implement within 4 hours, log within 24 hours.
- Standard changes: minimum 5 business days notice; stakeholder review for changes affecting >1 function.

**Section 4: Backlog Authority**
- RevOps maintains a visible, prioritized backlog. All requests enter the backlog.
- RevOps triages by: revenue impact, urgency, implementation effort, dependency on other items.
- Requests that don't meet the triage threshold are declined with a written reason and a suggested alternative or deferral timeline.
- Backlog is reviewed weekly in the RevOps standup and shared with stakeholders monthly.

**Section 5: Sponsorship**
- This charter is sponsored by: [CRO / CEO / COO name]
- Effective date: [date]
- Review date: [6 months from effective date]

---

## Backlog Triage Framework

RevOps without triage becomes a ticket queue. The goal is not to do more; it's to sequence correctly.

### Intake Categories

**Category A: System Health (always prioritize)**
- Data integrity issues (duplicates, broken syncs, stage mismatches)
- Automation failures
- Reporting broken or misleading

**Category B: Revenue Impact (prioritize when clear line to outcome)**
- Changes that directly affect pipeline velocity, forecast accuracy, or NRR
- New capabilities unlocking a GTM motion the team is blocked on
- Examples: new lead routing logic, expansion trigger automation, forecast category update

**Category C: Efficiency (schedule, don't rush)**
- Process improvements that reduce manual work
- Dashboard improvements that don't change underlying logic
- Training and documentation

**Category D: Nice to Have (backlog or decline)**
- Requests driven by preference, not pain
- Duplicates existing functionality in a slightly different format
- Requests with no named owner on the business side

### Triage Questions
1. What breaks if we don't do this? (Tests urgency)
2. Which metric does this move, and by how much? (Tests revenue connection)
3. Who owns this on the business side? (Tests commitment; no owner = no priority)
4. Does this fit the current architecture, or does it require a structural change? (Tests complexity)

### WIP Limit
Protect WIP. A RevOps team of 3-5 should run no more than 5-7 active items simultaneously. More than that and nothing finishes; it just slows down together.

---

## Fractional / Advisory / Agency / FTE: When to Use What

### The Spectrum

```
ADVISORY ──────────── FRACTIONAL ──────────── AGENCY ──────────── FTE
 Periodic sparring     Part-time embedded      Resource + expertise  Full-time in-house
 Low cost              Medium cost             Medium-high cost      Highest cost
 Low continuity        Medium continuity       High resource,        Full continuity
                                               variable expertise
```

### Advisory (including Fractional RevOps Architect)

**Best for:**
- Platform launches where architectural decisions need experienced oversight (e.g., deploying HubSpot + integrated pipeline architecture across business units)
- Teams that are technically capable but architecturally junior; they can build, but they need someone to validate the design before they build in the wrong direction
- Inflection points: new motion, new product, new region, significant re-architecture
- Cost: typically $1,000-2,000/day or a fixed retainer for availability

**How to use it well:**
- Define specific decisions or deliverables the advisor is accountable for; not "general guidance"
- Create a rhythm: structured monthly or bi-weekly sessions, async availability for urgent questions
- Treat sessions as knowledge transfer, not just problem-solving; the advisor should be making the internal team more capable each time, not more dependent

**Red flag:** If the team is still calling the advisor for the same category of question after 3 months, the advisory is filling a gap instead of closing it.

### Fractional RevOps (general)

**Best for:**
- $5-30M ARR companies that need a RevOps Manager function but can't justify a full-time hire
- Specific functional gaps (e.g., Marketing Ops lead while searching for a FTE hire)
- Ongoing support after completing an initial implementation or architecture project

**How to engage:**
- Define deliverables and time allocation upfront (e.g., 2 days/week, 12 weeks)
- Assign internal ownership early; fractional should be training a successor or internal champion, not owning the system indefinitely

### Agencies

**The rule: drain them of expertise. Every agency engagement should end with more capability in-house than when it started.**

Agencies provide two things: resources (headcount you don't have) and expertise (skills you don't have). When your company hires an agency, you often get the resources but not the expertise transfer, because agencies have an incentive to keep you dependent.

**How to use agencies without creating dependency:**

1. **Pair every agency task with an internal shadow.** The agency implements; the internal person watches, documents, and asks why. The goal is that the internal person can maintain and iterate independently within 90 days.

2. **Own the architecture, outsource the execution.** Agency configures and builds. You own the data model, the definitions, and the governance. If the agency owns those too, you can't switch providers without starting over.

3. **Require documentation as a deliverable.** Not post-project documentation; documentation that's written as the work is done. Every workflow, integration, and data model decision should be documented and owned by your team.

4. **Define a knowledge transfer milestone explicitly.** "By week 8, the internal team can configure a new workflow without agency support." Make it contractual if necessary.

5. **Reduce dependency as a success metric.** If you measure agency success by tickets closed, you'll keep needing them. Measure by: how many agency-initiated tasks can the internal team now own independently?

**When agencies make sense:**
- Short-term capacity gap (hiring is in progress; agency covers the interim)
- Specialized technical work that the internal team won't need to maintain frequently (e.g., complex data warehouse build, one-time migration)
- Accelerating a launch where speed matters more than internal capability building

**When agencies become a trap:**
- Core CRM configuration and workflow management; these change constantly and require deep context
- Definitions and governance; you cannot outsource the authority to own what a "qualified lead" means
- Anything that touches the data model; the agency will leave, and no one internally will understand why it was built that way

### FTE Hire

**Signals it's time to move from fractional/agency to FTE:**
- The same fractional person is working 3+ days/week for 6+ months; that's a FTE cost in a fractional wrapper
- Agency is owning processes that change weekly; you're paying for ongoing maintenance, not episodic expertise
- Institutional knowledge is leaving every time a freelancer or agency contract ends; you're rebuilding context repeatedly

**Hiring sequence:** hire generalist first, always. Adding specialists (Analyst, Architect, BP) before the generalist is in place produces brilliant individual contributors with no connective tissue. The generalist defines what the specialists work on.
