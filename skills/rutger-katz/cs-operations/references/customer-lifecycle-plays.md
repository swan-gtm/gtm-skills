# Customer Lifecycle Plays: Matching CS Action to Customer Phase

On-demand reference for the cs-operations skill. Answers three operator questions: what should CS be doing right now for a given account, which signals say the account is off track, and when is it safe to open an expansion conversation.

---

## Which phase is this account in?

Forget stage labels for a moment. Every post-sale account is in one of four practical situations, and the CS motion is different in each:

**1. Not yet live.** Contract signed, value not yet delivered. The only job is getting the customer to their first meaningful outcome, fast. Everything else (advocacy asks, expansion probes, satisfaction surveys) is noise that erodes trust at this phase.

**2. Live but shallow.** The product works, but usage sits with one team, one use case, or one champion. This is the highest-risk phase that dashboards routinely mark green: value is real but concentrated, so a single reorg or champion exit can erase it.

**3. Live and spreading.** Multiple stakeholders active, more than one use case delivering, outcomes the customer can name unprompted. This is the only phase where expansion conversations start from strength.

**4. Approaching a decision.** Renewal, contraction, or a champion change is on the horizon. The motion shifts from value delivery to value evidence: can the customer's own team articulate what they'd lose?

Classify every account into one of these four before choosing a play. Most CS teams run phase-3 plays on phase-1 and phase-2 accounts, which is why their expansion attempts read as tone-deaf and their QBRs get declined.

---

## What "healthy" looks like per phase

Health scores mean different things depending on the phase. Interpret the same signals differently:

| Signal | Not yet live | Live but shallow | Live and spreading |
|---|---|---|---|
| Low usage | Expected; watch trend, not level | Warning if flat 60+ days | Investigate immediately |
| Single active stakeholder | Normal at kickoff | The defining risk of this phase | Regression; find out who left |
| Champion slow to respond | Escalate now; onboarding stalls compound | Warning | Warning |
| No measurable outcome yet | Acceptable inside the agreed onboarding window | Not acceptable; run an outcome review | Not applicable |

Two thresholds worth wiring into automation:

- **Onboarding overrun:** if time-to-first-value exceeds the agreed window by more than ~20%, trigger an executive-level conversation and reset the success plan. Do not let onboarding drift silently; overruns are the strongest early churn predictor CS controls.
- **Engagement drop:** a health score falling ~20% or more inside 30 days is an event, not a trend to watch. It gets a same-week play, whatever the absolute score still says.

---

## Trigger plays

| You observe | Likely situation | Play |
|---|---|---|
| Onboarding running long, champion still engaged | Scope or resourcing problem | Reset the success plan with the economic buyer in the room; shrink the first outcome to something reachable in 2 weeks |
| Usage flat for 60+ days after go-live | Value plateau: product solved the first problem and stopped | Outcome review meeting: what did we set out to achieve, what's achieved, what's blocked |
| Health dropping and champion gone quiet | Churn risk regardless of renewal date | Escalation play: CS lead + account executive + executive sponsor touch within the week |
| Usage spreading to new teams without CS involvement | Organic expansion demand | Whitespace review: map which teams/use cases are active vs. addressable, then a structured expansion conversation |
| Champion changed roles or left | Relationship restart, whatever the health score says | Introduce to successor within 14 days; re-run discovery with the new owner as if the account were new |

---

## The expansion timing rule

**Do not open expansion conversations before the customer has reached their first agreed outcome.** An account still in onboarding that gets an upsell pitch learns that your interest is share-of-wallet, not their result, and that impression outlasts the deal. The green light for expansion is two conditions at once:

1. The customer has hit the outcome named in the original success plan, and can say so themselves.
2. Usage involves multiple stakeholders, not a single enthusiast.

One more asymmetry worth knowing: accounts delivering value in a single area churn at meaningfully higher rates than accounts with value spread across several teams, even when the single-area value is deep. Breadth beats depth for retention. This means expansion is not just a revenue motion; landing a second use case is often the strongest retention play available, which is why the whitespace review belongs in the CS cadence and not only in the sales playbook.

---

## Wiring this into the operating cadence

- Phase classification: refresh monthly for T1 accounts, quarterly for the rest. It's one field in the CRM; the value is in forcing the conversation.
- Trigger plays: automate detection (usage flat, health drop, champion role change) via CRM workflows; keep play execution human.
- Expansion gate: make "first outcome achieved" a required checkbox before an expansion opportunity can be created. See `references/expansion-scoring-model.md` for the scoring that runs after the gate opens.
- Handoff quality feeds all of this: a CS team that never received the original success criteria cannot classify phases. See `references/sales-cs-handoff-template.md`.
