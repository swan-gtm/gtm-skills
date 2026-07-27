---
name: skillify
title: Skillify
description: "Turns useful work from the current conversation into a reusable org skill. Captures the trigger, outcome, procedure, and judgment so the play can be rerun."
category: RevOps
---

## Instructions

### When this applies

Only skillify work that is **repeatable** and **already proven**. The conversation has to have produced a real procedure with a real outcome — not a half-finished attempt, not a one-off task. If the conversation mostly wandered, say so and ask what to capture.

Shapes that skillify well: a qualification rubric just used on an inbound, a research pattern that should run on the rest of the list, a scoring approach, an outreach framework, a triage flow for a signal. Shapes that don't: ad-hoc questions, one-time data pulls, debugging sessions.

### Procedure

**1. Reconstruct the three load-bearing pieces.**

- **Trigger** — the specific repeatable situation. "When an inbound demo request comes in" beats "the user asked about a lead."
- **Outcome** — the concrete deliverable. A scored list, a draft sequence, a research brief, a CRM cleanup, a Slack handoff.
- **Procedure** — the steps the agent actually ran, in order, pulled from the transcript. Do not invent steps the agent did not run. Do not add tools that "might be useful next time."

If any of the three is fuzzy, ask one focused question. Do not guess.

**2. Strip the specifics. Generalize the pattern.**

The work was done for one company, one contact, one list. The skill has to work for the next one.

- Real company / contact names → "the target company," "the buying-committee persona," "the account on the list."
- Hard-coded filter values, segment definitions, list IDs, stage names → load from org knowledge. "Load the ICP." "Pull funnel stages." "Check org memory."
- Hard-coded copy, weights, thresholds → defer to the customer's voice. "Pull past approved messages and match the style." "Load the sender's voice." Do not paste the exact subject line that worked once.

Exception: if the user explicitly says the skill is locked to one account or campaign (rare — usually a named-account play), keep the specifics and call it out in the description.

**3. Capture the judgment, not just the steps.**

Look back at the moments the agent or the user made a non-obvious call: a filter narrowed, an objection reframed, a draft rejected, a signal upweighted. Those are the judgment beats and they go in a `## What good looks like` section: what to spot first, what gets overlooked, the failure modes, success vs. mediocre.

If the only thing worth writing down is "call these three tools in order," the conversation produced an execution, not a skill. Tell the user.

**4. Lay the skill out for gradual disclosure.**

The agent never loads the whole skill at once. Information reveals in layers: description → skill main page → sub-page. Authoring is mostly deciding what goes in which layer.

- **Description** — read by the router to decide whether to invoke the skill. Lead with "Use this skill when…" + the outcome. Pack in real user phrasings ("we keep hearing the wrong objections," "score these accounts," "the funnel is leaking"). Dense with trigger language, not warmth. 1–3 short paragraphs.
- **Skill main page (`## Instructions`)** — read once the skill is routed. The decision tree and the general procedure. Lean. No re-selling the skill, no scenario-specific detail.
- **Sub-pages** — one level deep, one per scenario. The main page routes to them by name. The agent only opens the one that matches the situation.

When does the procedure need sub-pages? Whenever the conversation surfaced **branching scenarios** that each carry their own methodology. Inbound demo from an existing customer vs. a brand-new ICP-fit account → two sub-pages. Funding-event outreach vs. new-hire outreach → two sub-pages. If every branch fits in one or two lines, keep it on the main page; if a branch wants three or more paragraphs of its own logic, lift it out.

Common failures of the disclosure layout:

- **Disagreement.** Description sells one shape; main page executes another. Router keeps invoking the skill in the wrong situations.
- **Branches stuffed into the main page.** Every scenario inlined as another `###` section. The agent loads detail for situations that don't apply. Push them into sub-pages and route by name from the main page.
- **Sub-pages for things that aren't scenarios.** A sub-page per step, or a sub-page for "rules." Sub-pages are for situational variants, not for chunking.

**5. Speak in GTM verbs, not tool names.**

The next run might be on a different CRM, a different sender, a different scraper. Say "check the CRM," "load the ICP," "pull recent meeting transcripts," "scrape the page" — not `hubspot-search-objects` or `apify-list-store-actors`.

The short list of tools worth naming explicitly when the procedure depends on them: `swan-execute-code`, `swan-build-sequence`, `swan-create-trigger`, `swan-delegate-to-sub-agents`. Everything else stays a verb.

**6. Confirm and create.**

Surface the draft and confirm:

- **Title** — plain sentence case. No `<DEFAULT>` / `<SYSTEM>` wrapper, no decorations — lifecycle is metadata, not display.
- **Category** matched to the outcome, not the procedure. A research run that ends in expansion outreach is a customer skill. A scoring run that ends in drafted messages is an outreach skill.
- **Scope** — `org` vs. `personal`. Personal when the workflow centers on one person's day-to-day (meeting prep, their inbox, their calendar) or pulls from their personal integrations. Org when it's a shared GTM motion the team will reference. Org skills don't load on a user's personal triggers' integrations unless explicitly added; personal skills don't load on org triggers at all. Default to org unless the user signals otherwise.

Once confirmed, call `swan-create-skill` (plus `swan-create-skill` again per sub-page if the layout calls for sub-pages, with `path` set to the parent's id). Echo back the title, the trigger phrasing it will match on, and one line on when the agent will reach for it next.

### Rules

- MUST confirm title, category, and scope before creating the skill.
- MUST only cite tools the agent actually used in the conversation.
- MUST include a `## What good looks like` section in the produced skill — what to spot first, what gets overlooked, failure modes, success vs. mediocre. A skill without it is a step-list.
- MUST keep titles plain. No `<DEFAULT>` / `<SYSTEM>` / `<DEFAULT:AUTO>` prefix in the title field — that convention is dead. Lifecycle lives in metadata.
- MUST keep `swan-execute-code`, `swan-build-sequence`, `swan-create-trigger`, and `swan-delegate-to-sub-agents` named explicitly when the procedure depends on them. Everything else stays as a GTM verb so the skill survives a CRM or sender switch.
- MUST use `###` (h3) for sub-section headings inside the body. The top-level `## Description` / `## Instructions` / `## What good looks like` stay h2.
- MUST use the inline reference format `${type:id:label}$` whenever the body points at another skill, a sender, a Slack channel, a HubSpot user, a HubSpot list, or a tag. Plain-text names break click-through and break when the resource is renamed. Available types: `skill`, `sender`, `slack-channel`, `slack-user`, `hubspot-user`, `hubspot-list`, `tag`.
- NEVER use markdown tables in the body. The renderer doesn't show them. Use bullets or plain text.
- NEVER skillify a one-off task — the trigger has to be repeatable.
- NEVER bake in the customer's voice, weights, or segment definitions. Defer to org knowledge.
- NEVER add a step the conversation did not run.
- NEVER inline more than one or two lines per branch on the main page. Multi-paragraph branches go to sub-pages.

## What good looks like

The next person on the team — or the next run a month later, against a different account — can execute the skill cold and get a comparable result. The specifics from this conversation are gone. What survives is the trigger, the procedure, and the *why* behind the non-obvious moves.

What to spot first: the moment the agent made a call that wasn't mechanical. A filter pulled tighter, an account dropped, an objection sidestepped, a draft thrown out. That is the load-bearing judgment and it has to make it into the skill, or the skill is hollow.

What gets overlooked:

- **The strip-and-generalize pass.** Half-skillified outputs read like "here's exactly what was done for Acme" with the names lightly swapped. Cleaner test — read the draft as someone who has never heard of the company in the transcript. If it still tells them what to do, the generalization landed.
- **The description.** Authors spend their care on the body and slap a one-liner at the top. The description is what decides whether the skill ever fires again. Spend real time on the trigger phrasings.

Failure modes:

- **Frankenstein skill.** The conversation covered two distinct procedures and the draft tries to hold both. Ask which one. Save one, not a hybrid.
- **Tool-coupled skill.** The draft cites the exact CRM or scraper used this run, locking the skill to that stack. Most should be verbs ("check the CRM," "scrape the page") so a switch doesn't break the play.
- **Step-list with no judgment.** No `## What good looks like`, or it's just "do the steps well." The conversation didn't produce judgment worth saving — be honest with the user.
- **Hard-coded voice.** The exact subject line, weight, or threshold from this run is pasted into the body. The skill stops compounding the moment the org's voice evolves.
- **Description-body disagreement.** The description sells one shape; the body executes another. The router keeps invoking the skill in the wrong situations.
- **Everything-on-the-main-page.** No sub-pages, just one long main page with every branch inlined. The agent loads detail for situations that don't apply, and the relevant logic gets buried. Push branches to sub-pages and route by name.
- **Wrong scope.** A workflow that depends on one user's calendar saved as an org skill — won't load where it needs to. A team-wide GTM motion saved as personal — invisible to org triggers. Get scope right before creating.

Success: the user installs the skill and reruns it next month against a different account without re-prompting the agent on the same judgment. One-time work has been converted into compounding org capability.
