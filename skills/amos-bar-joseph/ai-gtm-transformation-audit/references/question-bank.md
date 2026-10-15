# Question bank

Every scaled question lists its options best first. The number in brackets is the score (3, 2, 1, 0); show the options without it. Every question also accepts a typed answer: score it against the closest option, or ask again if it cannot be placed.

Each question carries the dimension it scores, what good looks like, and the 30-day move to use if it turns up as a gap.

## Opening (every role)

### J1. Where is your team on its AI GTM transformation journey?

Dimension: Systems. This is the self-placement; the gates in SKILL.md test it.

1. Shared AI layer across GTM. Multiple teams build and run agents off a common foundation, with permissions, monitoring and shared context in place. (3, claims level 4)
2. Agents in production. We've defined workflows and skills, and agents run them when something triggers them, without someone prompting each step. (2, claims level 3)
3. AI as a Q&A layer. Claude or ChatGPT is connected to some of our systems, and we ask it questions when we need something. (1, claims level 2)
4. Mostly chat, mostly manual. Some people use AI on their own; research, list building and outreach are done by hand or in traditional tools. (0, claims level 1)

- Sufficient when: a typed answer can be placed on one of the four. If not, ask which of the four is closest, naming them.
- Good: multiple teams run agents on one shared foundation with permissions, monitoring and shared context.
- 30-day move: pick one repeatable workflow and run it as a triggered agent with an owner, an approval boundary and an outcome metric.

### P1. Think about the new pipeline you created in the last 6 months. Roughly what % came from each source?

Typed only, does not score. Prompt with the sources: inbound (website, forms, content, SEO), outbound (SDR or AE prospecting), LinkedIn and social, events and webinars, partners and referrals, product-led signups, existing customers. Example: 50% inbound, 25% outbound, 15% LinkedIn, 10% events.

- Sufficient when: it names sources with a share for each and covers most of the pipeline. "100% outbound" passes; "mostly inbound" or "a mix" does not.
- Use: the largest source is their dominant channel and decides which play leads the 30-day plan.

### P2. What are your top priorities for the next two quarters? Pick all that apply.

Multi-select, does not score. Options by role:

- Marketing: Increase pipeline / Increase revenue from marketing / Expand into a new channel (LinkedIn, events, partners) / Improve inbound conversion / Speed up lead follow-up with sales / Prove marketing's impact on revenue / Launch or scale ABM / Scale content with AI
- Sales: Increase pipeline / Increase revenue and hit quota / Expand outbound (email, LinkedIn, phone) / Raise win rates / Shorten sales cycles / Ramp new reps faster / Improve forecast accuracy / Get the team using AI day to day
- RevOps: Increase pipeline coverage / Trusted CRM data / Launch new channels or motions faster / Build signal routing and lead scoring / Improve forecast accuracy / Consolidate the tool stack / Roll out AI agents safely / Prove attribution
- Customer success: Increase net revenue retention / Reduce churn / Grow expansion revenue / Faster onboarding and time to value / Scale CS without adding headcount / Better health scoring / Smoother sales-to-CS handoffs / Customer advocacy and referrals
- Founder or CEO: Increase pipeline / Increase revenue / Expand into a new channel or market / Grow without adding headcount / Prove ROI on AI / Build a repeatable pipeline engine / Improve forecast predictability / Hit board or fundraise goals

- Sufficient when: at least one is picked, or a typed priority names a concrete goal ("grow" is too vague; "grow our LinkedIn motion" passes).
- Use: decides which motion gets the logic test and how the gaps are ranked.

Q10 (Core, below) is the fourth opening question. Sufficient when a typed answer names who builds: a role, a team or a number of people. "It depends" is asked again.

Q19 (Core, below) is the outcome question for every role. Offer two or three options that fit the role (marketing: pipeline sourced, MQL to SQL conversion; sales: new ARR, win rate; RevOps: forecast accuracy, pipeline coverage; customer success: net revenue retention, gross churn; founder: ARR growth, burn multiple) and accept their own.

## Persona defaults for the adaptive question

When no routing rule in SKILL.md matches: marketing M5 if J1 is Q&A, else M2; sales S3 if J1 is Q&A, else S4; RevOps R3 if Q15 is Some or Little, else R1; customer success C1 if Q23 is "when they tell us" or "after they leave", else C2; founder E4.

## Core (all roles)

### Q1. How much of your sales team's week is manual work such as research, list building, CRM updates, and follow-up?

Dimension: Process

1. Under 2 hours per rep (3)
2. 2 to 5 hours (2)
3. 5 to 10 hours (1)
4. Over 10 hours (0)

- Good: systems assemble research, update records and prepare follow-up; reps keep judgment over customer moments.
- 30-day move: time one representative week by task, then automate the two highest-volume chores with an owner and an accuracy check.

### Q2. Can you get reporting from your reps without asking them for it?

Dimension: Data

1. Always (3)
2. Mostly (2)
3. Rarely (1)
4. Never (0)

- Good: reporting comes from system events, not rep updates, with clear definitions and visible exceptions.
- 30-day move: list the reports that still need rep input and instrument the activity underneath each.

### Q3. Can SDRs spin up their own workflows and automations?

Dimension: People

1. Themselves (3)
2. With help (2)
3. It needs a ticket (1)
4. Nobody does (0)

- Good: authorized SDRs launch approved plays themselves from reusable components, with tests and approval gates.
- 30-day move: create three pre-approved workflow patterns SDRs can configure without a ticket.

### Q4. Do marketing and sales use the same playbooks, skills, and messaging?

Dimension: Process

1. Shared skills and context (3)
2. Shared documents (2)
3. Separate (1)
4. Don't know (0)

- Good: both teams run skills on one maintained context: ICP, positioning, approved claims, objections, qualification rules.
- 30-day move: name an owner for the shared GTM context and turn one cross-functional motion into a reusable skill.

### Q5. How long does it take to launch a new GTM motion such as a segment, signal, or sequence?

Dimension: Process

1. Days (3)
2. Weeks (2)
3. A quarter (1)
4. Longer (0)

- Good: data, routing, content, approvals and measurement are modular, so a new motion launches in days.
- 30-day move: document the last launch, find the longest dependency, and make it a reusable component.

### Q6. Can your GTM infrastructure capture signals in real time, connect them at both the person and account level, and trigger the right response?

Dimension: Systems

1. Real-time at both levels, with automated action (3)
2. Combined manually before someone acts (2)
3. Captured in separate tools or at only one level (1)
4. No consistent signal capture (0)

- Good: signals resolve people to accounts with source and history; high-confidence combinations act automatically, the rest reach a person with the evidence.
- 30-day move: pick three high-value signals and define source, identity rule, threshold, next action and exception path.

### Q7. Do marketing, sales, Customer Success, and RevOps work from one shared GTM brain for accounts, people, ICP, and decisions?

Dimension: Data

1. One shared GTM brain (3)
2. Several connected sources (2)
3. Tribal knowledge (1)
4. No (0)

- Good: every function reads and writes one maintained record of fit, buying group, history, signals, promises and decisions.
- 30-day move: define the minimum shared account record, name owners, connect the two systems that lose the most context.

### Q8. How long does a new rep take to ramp, and can they use your best reps' knowledge on day one?

Dimension: People

1. Under a month and yes (3)
2. 1 to 3 months (2)
3. Over 3 months (1)
4. Not captured (0)

- Good: new reps run current examples, account history, objections and playbooks from day one; competency is measured in weeks.
- 30-day move: capture one top-rep workflow end to end and use it in the next hire's onboarding with a proficiency checkpoint.

### Q9. When a top rep performs, is their method captured in a system others can run?

Dimension: People

1. Yes, as workflows (3)
2. Documents only (2)
3. Shadowing (1)
4. No (0)

- Good: the repeatable parts of top performance live as maintained workflows, examples and decision rules.
- 30-day move: convert one proven rep practice into a runnable workflow and review its results monthly.

### Q10. Who in your organization can build a GTM workflow today?

Dimension: People

1. Anyone (3)
2. RevOps only (2)
3. Engineering (1)
4. Nobody (0)

- Good: authorized operators in every function build inside clear permissions, tests and approvals.
- 30-day move: define builder roles and release one safe self-service path before widening access.

### Q11. What is your current process for turning anonymous website visitors into meetings and pipeline?

Dimension: Systems

1. Identified, researched and worked automatically, with outreach sent (3)
2. Identified, researched and routed with outreach drafted, the rep approves (2)
3. Identified and dropped into Slack, a CRM task or a report (1)
4. We don't identify anonymous visitors (0)

- Good: a qualified visitor is identified, researched for fit and context, and worked right away: automatically when confidence is high, with one-click rep approval otherwise.
- 30-day move: build one visitor-to-meeting workflow with an ICP filter, ownership rules, a response-time target and a clear line between automatic sends and rep approval.

### Q12. What share of pipeline can you attribute to a signal or campaign with confidence?

Dimension: Data

1. Over 75% (3)
2. 50% to 75% (2)
3. 25% to 50% (1)
4. Under 25% (0)

- Good: most pipeline has source and influence evidence that survives deduplication and stage changes.
- 30-day move: standardize campaign, signal and opportunity IDs, then reconcile last quarter before adding models.

### Q13. Who follows up on event and webinar attendees, and how fast?

Dimension: Process

1. Same day through a reusable skill (3)
2. Same week through a manual process (2)
3. Later (1)
4. Nobody (0)

- Good: one skill turns every attendee list into enriched, prioritized, personalized, approved same-day follow-up.
- 30-day move: write and test one event follow-up skill before the next event.

### Q14. How many GTM tools does a rep touch in a normal day?

Dimension: Systems

1. 1 to 3 (3)
2. 4 to 6 (2)
3. 7 to 10 (1)
4. More than 10 (0)

- Good: reps work in one to three surfaces while orchestration handles enrichment, routing, sequencing and updates.
- 30-day move: map each daily tool to its job and remove duplicate steps before replacing platforms.

### Q15. How much of your CRM data would you trust in a board deck without cleaning it?

Dimension: Data

1. All (3)
2. Most (2)
3. Some (1)
4. Little (0)

- Good: definitions, ownership, validation and exception handling are explicit, so the CRM is board-ready as is.
- 30-day move: pick the five board-critical fields, add validation rules, and route exceptions to owners continuously.

### Q17. Where does AI sit in your GTM today?

Dimension: Systems

1. Agents run workflows (3)
2. Copilots for writing (2)
3. Individual ChatGPT/Claude use (1)
4. Nowhere (0)

- Good: AI runs bounded workflows with owners, evidence, controls, human escalation and measured outcomes.
- 30-day move: pick one repeatable workflow and define inputs, owner, approval boundary, failure path and outcome metric.

### Q18. If you could remove one weekly GTM chore, which would it be?

Dimension: none (free text, does not score)

- Good: the chore is named with frequency, owner, time cost and quality bar.
- 30-day move: write it up as a workflow brief with volume, inputs, exceptions, approvals and a 30-day target.

### Q19. What is the one number you are measured on this quarter?

Dimension: none (free text, does not score)

- Good: one business outcome with baseline, target, owner and period.
- 30-day move: tie every recommended workflow to this number or a leading indicator of it.

### Q20. How much of your outbound is personalized with a real account fact rather than a template?

Dimension: Process

1. Most (3)
2. Some (2)
3. Little (1)
4. We don't do outbound (0)

- Good: most outbound carries a verified, decision-relevant account fact and a persona-fit angle.
- 30-day move: define the minimum evidence required per message and test one fact-based framework against the current baseline.

### Q21. When a customer signal fires, can Customer Success interpret it and launch the right action with full account context?

Dimension: Data

1. The right play launches automatically with full context (3)
2. Context is available, but someone must decide and act (2)
3. The team assembles context across tools (1)
4. The signal is missed or no play follows (0)

- Good: usage, exec, champion and support signals are read against the whole relationship and launch an expansion or risk play with evidence.
- 30-day move: join one expansion signal and one churn signal to customer history, each with play, owner and threshold.

### Q22. How do you find expansion and upsell opportunities in your customer base today?

Dimension: Systems

1. Signals routed to CSMs (3)
2. QBR reviews (2)
3. CSM gut feel (1)
4. We don't look (0)

- Good: product, relationship and company signals are scored and routed to the CSM with evidence and timing.
- 30-day move: back-test two expansion signals against recent wins and route qualified accounts to a CSM queue.

### Q23. How early do you see churn risk before a renewal?

Dimension: Data

1. 90 or more days out, from signals (3)
2. At the renewal call (2)
3. When they tell us (1)
4. After they leave (0)

- Good: risk shows 90+ days out from validated usage, stakeholder, support and sentiment signals.
- 30-day move: test an early-warning set against the last ten renewals and assign a play to each risk type.

### Q24. Does a CSM know what sales promised before taking over an account?

Dimension: Process

1. Automated handoff brief (3)
2. Handoff call (2)
3. They read the CRM (1)
4. No (0)

- Good: a brief is generated at close with goals, stakeholders, promises, risks, commercials and source links.
- 30-day move: make a close-to-CS handoff template and generate it from the deal record and call evidence.

### Q25. Can CS launch its own plays such as renewal preparation, champion departure, or usage drop without RevOps?

Dimension: People

1. Themselves (3)
2. With help (2)
3. It needs a ticket (1)
4. Nobody does (0)

- Good: CS configures approved post-sale plays with guardrails while RevOps governs data and architecture.
- 30-day move: give CS one self-service play template with triggers, approvals and outcome reporting.


## Marketing

### M1. Can you combine signals from several people into one account-level buying-group view?

Dimension: Data

1. Automatically, with identities and source evidence (3)
2. Manually in a campaign or CRM view (2)
3. We see person-level signals separately (1)
4. No (0)

- Good: signals resolve to people, roles, accounts and buying groups with sources and timestamps.
- 30-day move: in one segment, define identity, role, account and buying-stage rules before adding providers.

### M2. When a high-intent person or account does not convert, what happens next?

Dimension: Systems

1. Routed immediately with account context and a timed play (3)
2. Alerted to an owner (2)
3. Reviewed in a batch (1)
4. Nothing consistent (0)

- Good: unconverted demand enters a timed, owned play that keeps the signal, context and reason to follow up.
- 30-day move: pick one high-intent event, set an SLA, and measure how many qualified accounts get action in time.

### M4. Can lifecycle content and next actions change automatically by behavior and segment?

Dimension: Systems

1. Yes, with experiments and guardrails (3)
2. Rules for a few segments (2)
3. Batch campaigns built manually (1)
4. No (0)

- Good: content, channel, timing and next action adapt to behavior and segment, with experiments and stop rules.
- 30-day move: launch one behavioral lifecycle experiment on two segments with a holdout.

### M5. How consistently does AI-generated content follow your approved positioning and claims?

Dimension: Process

1. Tested against a maintained brand and claims library (3)
2. Templates plus human review (2)
3. Depends on the person prompting (1)
4. It is not controlled (0)

- Good: generated content is checked against current positioning, approved claims and banned language before use.
- 30-day move: build a versioned messaging and claims library and test a sample of outputs against it.

### M6. Which buying signals does your team act on today, and how?

Dimension: Data

1. Several signals (intent, LinkedIn engagement, events, product usage) combined per account and acted on automatically (3)
2. Several signals, but someone combines them by hand (2)
3. One main signal, for example form fills (1)
4. We don't act on buying signals yet (0)

- Good: several signals are resolved to the account, combined, and trigger the right action with the evidence attached.
- 30-day move: pick three signals you already have, combine them per account, and route the accounts that cross a threshold to an owner.

### M7. When marketing hands a lead to sales, how fast and how consistently does sales follow up?

Dimension: Process

1. Every lead, within the hour, and it is tracked (3)
2. Most leads, within a day (2)
3. Some leads, when reps get to them (1)
4. We don't really know (0)

- Good: every handed-off lead is researched, routed and followed up within the hour, and follow-up is tracked back to marketing.
- 30-day move: set a speed-to-lead target, draft the first touch automatically, and report follow-up rate by rep weekly.


## Sales

### S1. When pipeline is short, who owns creating it?

Dimension: Process

1. Named ownership and targets by segment and channel (3)
2. Shared AE-BDR plan (2)
3. Leadership asks everyone to prospect (1)
4. Ownership is unclear (0)

- Good: ownership, target accounts, channels and contribution targets are explicit by segment.
- 30-day move: publish a one-page pipeline responsibility model and review contribution by segment weekly.

### S2. Can reps prioritize accounts using verified signals instead of static lists or intuition?

Dimension: Data

1. Ranked account actions with evidence and timing (3)
2. Signal dashboards plus rep review (2)
3. Static lists with occasional intent (1)
4. Mostly intuition (0)

- Good: reps get a ranked action queue with evidence, timing, history and a reason to act now.
- 30-day move: back-test three signals against recent opportunities and build one prioritized queue from the winners.

### S3. Is there a defined boundary between work AI may perform and work an SDR or AE must own?

Dimension: People

1. Documented by task risk and buyer impact (3)
2. Team norms with manager review (2)
3. Individual rep choice (1)
4. No (0)

- Good: the boundary is set by risk, reversibility, relationship impact and required judgment.
- 30-day move: classify each sales step as autonomous, assisted, approval-required or human-only.

### S4. How do call insights and seller activity reach the CRM?

Dimension: Systems

1. Automatically with evidence, deduplication and validation (3)
2. Automated for some activities (2)
3. Rep-entered summaries (1)
4. They usually do not (0)

- Good: insights and activity update the CRM automatically with source, confidence and deduplication.
- 30-day move: send one high-value call insight to a staging layer, validate it, then allow CRM writeback.

### S5. When outreach or calls work, how does the method improve for every rep?

Dimension: People

1. Outcomes update a governed playbook and coaching loop (3)
2. Enablement reviews patterns regularly (2)
3. Reps share examples informally (1)
4. It stays with the individual (0)

- Good: outcomes feed shared playbooks, examples and coaching through a governed review loop.
- 30-day move: hold a monthly evidence review that promotes winning examples and retires weak ones.

### S6. When someone joins your sales team, how do they learn your playbook, messaging and process?

Dimension: People

1. They run shared skills and workflows that carry our best practice from day one (3)
2. A maintained playbook plus shadowing (2)
3. Shadowing and scattered docs (1)
4. They figure it out (0)

- Good: new hires work from the same maintained context (ICP, messaging, objections, playbooks) that your agents use, so best practice is runnable on day one.
- 30-day move: capture your best rep's research and outreach as one shared skill and make it part of the next hire's first week.


## RevOps

### R1. Where does signal orchestration live relative to your CRM?

Dimension: Systems

1. Governed data or agent layer writing validated outcomes to the CRM (3)
2. Defined workflows inside the CRM (2)
3. Point tools write directly (1)
4. No architecture decision (0)

- Good: a governed layer resolves identity, applies policy, keeps evidence, and writes validated outcomes to the CRM.
- 30-day move: draw today's signal-to-CRM flow and set a staging, identity and writeback policy.

### R2. Can an operator trace a CRM recommendation or field update back to its evidence?

Dimension: Data

1. Yes, with source, timestamp and change history (3)
2. For important fields (2)
3. Only in the originating tool (1)
4. No (0)

- Good: every automated update carries source, timestamp, confidence and change history.
- 30-day move: add provenance fields and an audit trail to the next automated CRM workflow.

### R3. How do you prevent enrichment, intent, and automation tools from muddying the CRM?

Dimension: Systems

1. Staging, identity resolution, confidence thresholds and write rules (3)
2. Field-level rules and review (2)
3. Each tool writes its own fields (1)
4. We clean it later (0)

- Good: external data passes staging, identity resolution, confidence thresholds and controlled writeback.
- 30-day move: stop direct writes from one noisy source and route it through governed staging.

### R4. When a workflow, schema, prompt, or vendor changes, who tests and maintains the downstream process?

Dimension: People

1. Named owner, automated regression tests and service expectations (3)
2. Scheduled owner review (2)
3. Original builder checks it when asked (1)
4. Nobody (0)

- Good: each production workflow has business and technical owners, a regression set, alerts and rollback.
- 30-day move: inventory production workflows and give the riskiest one an owner, test set and rollback plan.


## Customer success

### C1. Are renewal, churn, downgrade, and expansion events represented in one consistent post-sale model?

Dimension: Data

1. Yes, with reconciled ARR movement and forecasting (3)
2. Mostly, with manual exceptions (2)
3. Separate pipelines and spreadsheets (1)
4. No consistent model (0)

- Good: one event model reconciles ARR movement across CRM, billing, forecast and CSM work.
- 30-day move: define canonical post-sale events and reconcile a sample of recent renewals across CRM and billing.

### C2. Can every customer receive a value story based on actual usage and outcomes?

Dimension: Systems

1. Automatically, with metric gates and channel rules (3)
2. Generated for priority accounts (2)
3. Built manually for QBRs (1)
4. No (0)

- Good: usage and outcome data produce a credible, customer-specific value story through approved channels.
- 30-day move: automate a value summary on one measurable outcome for a controlled cohort.

### C3. How is a customer health or risk recommendation validated before a CSM acts?

Dimension: Process

1. Back-tested signals, source evidence and clear thresholds (3)
2. Reviewed against account context (2)
3. CSM judgment on a score (1)
4. The score is accepted as-is (0)

- Good: health scores are back-tested, explainable and combined with account context.
- 30-day move: back-test the current score against recent churn and renewals, then publish evidence and thresholds.

### C4. How is CSM operating knowledge kept current and reusable?

Dimension: People

1. Versioned playbooks tied to workflows and outcomes (3)
2. Maintained enablement library (2)
3. Shared documents and shadowing (1)
4. Tribal knowledge (0)

- Good: CSM knowledge is versioned, tied to workflows and outcomes, with named owners.
- 30-day move: turn one high-performing CSM motion into a maintained playbook with examples and results.


## Founder and CEO

### E1. What proof is required before an AI GTM initiative receives more budget?

Dimension: Data

1. Measured business outcome, cost, risk and adoption (3)
2. Funnel improvement with a baseline (2)
3. Usage and anecdotal wins (1)
4. No standard proof (0)

- Good: funding needs a baseline, business outcome, total cost, quality bar, adoption and risk view.
- 30-day move: define one investment gate and apply it to the next AI GTM funding decision.

### E2. Does every AI GTM initiative have an accountable business owner and a technical owner?

Dimension: People

1. Both, with decision rights and service expectations (3)
2. One clear owner with support (2)
3. Informal champions (1)
4. No (0)

- Good: business and technical owners hold decision rights, outcome accountability and maintenance duties.
- 30-day move: assign both owners to every active initiative; pause any without them.

### E4. Can leadership compare an AI investment with the human capacity and vendor spend it replaces?

Dimension: Data

1. Yes, using total cost and outcome quality (3)
2. Directional capacity estimate (2)
3. Hours saved only (1)
4. No (0)

- Good: leaders compare cost, capacity, quality, speed and risk across people, vendors and AI.
- 30-day move: build a before-and-after capacity model for the next initiative, including oversight work.

### E5. When entering a new category or motion, do messaging, incentives, enablement, and accountability change together?

Dimension: People

1. Yes, as one operating-model change (3)
2. Usually within the launch (2)
3. Each team adapts separately (1)
4. The old motion continues to dominate (0)

- Good: strategy, incentives, playbooks, metrics and accountability move together.
- 30-day move: build a launch checklist naming the behavior, incentive, owner and metric changes per function.


## Production readiness (one per interview, adaptive)

### N1. How do you decide what company and customer data an AI GTM workflow may access?

Dimension: Systems

1. Policy by data class with least privilege and audit logs (3)
2. Approved tools and manual review (2)
3. Team-by-team judgment (1)
4. No defined rule (0)

- Good: access follows data class, least privilege, purpose and retention rules, with audit logs.
- 30-day move: classify the data one workflow uses and remove access broader than its purpose.

### N2. When a model, prompt, vendor, or integration changes, how do you know your GTM workflows still work?

Dimension: Process

1. Automated tests and alerts (3)
2. Scheduled regression checks (2)
3. Someone spot-checks outputs (1)
4. We find out when users complain (0)

- Good: representative tests run on every relevant change, with thresholds, alerts and rollback.
- 30-day move: build a small regression set from real cases and run it whenever a dependency changes.

### N3. Who owns an AI GTM workflow after it launches?

Dimension: People

1. Named business owner with technical support and service levels (3)
2. RevOps or IT owns the queue (2)
3. The original builder maintains it informally (1)
4. No clear owner (0)

- Good: a named business owner owns the outcome; a technical owner owns reliability and changes.
- 30-day move: add owner, service level, review cadence and retirement criteria to every production workflow.

### N4. Can you see the cost of an AI workflow per useful business outcome?

Dimension: Data

1. Cost per accepted outcome and downstream result (3)
2. Cost per run or user (2)
3. Total vendor spend only (1)
4. No (0)

- Good: cost is measured per accepted output and tied to meetings, pipeline, retention or expansion.
- 30-day move: instrument token, data, vendor and review cost for one workflow and link it to an outcome.

### N5. Before an AI output updates the CRM or reaches a customer, how is quality controlled?

Dimension: Process

1. Risk-based tests, confidence thresholds and approval gates (3)
2. Rules plus human review (2)
3. Occasional spot checks (1)
4. No standard control (0)

- Good: controls match action risk: validation, confidence thresholds, approvals, logging and rollback.
- 30-day move: classify actions by risk into autonomous, reviewed and human-only.

### N6. Can you connect AI-assisted GTM work to pipeline, revenue, retention, or expansion?

Dimension: Data

1. Yes, with a defensible control or attribution method (3)
2. Directionally, with linked funnel metrics (2)
3. Activity and usage only (1)
4. No (0)

- Good: incremental business impact is separated from activity using baselines, controls or defensible attribution.
- 30-day move: pick one outcome and set the baseline and comparison method before scaling the workflow.

### N7. When an AI system recommends an account action, can the user see why?

Dimension: Data

1. Sources, timestamps, confidence and reasoning are attached (3)
2. Source links are available (2)
3. A summary without evidence (1)
4. No explanation (0)

- Good: each recommendation shows evidence, recency, confidence and the reason for the action.
- 30-day move: require evidence and timestamps in one recommendation workflow and let users flag bad reasoning.

### N8. How do you decide whether to buy, build, or staff a GTM workflow?

Dimension: Process

1. Decision rubric covering differentiation, data, risk, economics and ownership (3)
2. Architecture and ROI review (2)
3. Ad hoc tool comparison (1)
4. Whoever asks loudest (0)

- Good: a repeatable rubric weighs maintenance, data rights, speed, risk, economics and ownership.
- 30-day move: run the rubric on the next workflow before any vendor trial or internal build.

