# Expansion Pipeline Architecture

On-demand reference for the revops-handoffs skill. Read before designing an expansion or cross-sell pipeline.

Expansion is the cheapest revenue you will ever book. Historically, it costs about $0.27 per $1 ACV against $1.16 for new logos (Pacific Crest, 2016), and modern data shows best-in-class companies now source 50-60% of new ARR from the existing base (OpenView 2023, KeyBanc 2024), up from historical 35-40%. But most orgs jam every expansion into one pipeline and then wonder why their win-rate and velocity data is noise. The fix is to model three distinct types.

## 1. The three expansion types

| Type | Buying group (DMU) | Pipeline shape | Discovery required |
|---|---|---|---|
| **Upsell** | Same champion, same budget | Short: Identified, Proposal, Won | SPICED refresh only |
| **Cross-sell (warm)** | Partial overlap, champion introduces the new buyer | Standard: Identified, Needs Assessment, Proposal, Negotiation, Won | Partial new SPICED |
| **Cross-sell (new DMU)** | Completely new buying group inside the account | Full discovery stages added | Full new SPICED, mandatory |

The critical case is the third. A cross-sell into a completely new decision-making unit is a new-logo sale wearing a familiar company name. Trust sits with the account, not with the new buying group. Force it into the short upsell pipeline and you poison both your win rate (it looks like a loss against easy upsells) and your velocity data (it takes far longer, so it drags every average).

## 2. The litmus test

One question decides which pipeline a deal belongs in:

> "Would losing the contract in business unit A affect our ability to close in business unit B?"

- **Yes** to the linkage: it is a genuine expansion. The existing relationship is load-bearing. Use the upsell or warm cross-sell pipeline.
- **No** to the linkage: it is a new logo with a customer referral source. Use a full-discovery pipeline and count it honestly.

## 3. Ownership thresholds

Ambiguity here means nobody closes. Define the thresholds in governance, not in the moment.

| Expansion ACV | Owner | CS role |
|---|---|---|
| Under $10K | CSM closes | End-to-end |
| $10K to $50K | AM or AE closes | CSM provides context, stays in meetings |
| Over $50K | AE runs full cycle | CSM introduces, then advisory only |

Write these thresholds into the operating cadence and the CRM routing rules. A threshold that lives only in someone's head is not a threshold.

## 4. The deal-to-deal association model

Expansion deals must be linked to the originating deal, not floated as orphans. On HubSpot Professional and above (and equivalent Salesforce structures) use deal-to-deal associations so you can:

- Trace lineage: which original deal seeded this expansion, and how long after close it landed (the time-to-expansion metric, sometimes tracked as days from onboarding to first expansion).
- Report expansion ARR by cohort and by originating segment, source, and rep.
- Keep expansion out of new-business win-rate reporting so neither number lies.

Structure: one original deal, associated to N expansion deals, each tagged with an `expansion_type` property that drives the conditional pipeline stages above.

## 5. SPICED requirements by type

The discovery bar rises with the distance from the original buying group.

- **Upsell:** refresh the existing SPICED. Confirm the Situation and Impact still hold and that the Critical Event is real. Do not re-run full discovery on a champion who already trusts you.
- **Warm cross-sell:** partial new SPICED. The Pain and Impact are new (different function, different problem), even if the Situation is shared. Map the new stakeholder before proposing.
- **New-DMU cross-sell:** full new SPICED, no shortcuts. New Situation, new Pain, new Impact, new Critical Event, new Decision process. The account relationship gets you the meeting. It does not get you the deal.

## 6. Why separating types pays off

- **Honest win rates.** Easy upsells stop inflating the number and hard new-DMU deals stop deflating it.
- **Clean velocity data.** Each pipeline has a coherent cycle length, so forecasting per type actually works.
- **Correct capacity planning.** A team told that "expansion closes fast" will be badly under-resourced for new-DMU work.
- **Better handback discipline.** The CS to Sales handback brief can be sized to the type: light for upsell, full stakeholder map and whitespace analysis for new DMU.

## Sources

- Pacific Crest / David Skok and Matrix Partners (2016) SaaS Survey. Expansion costs $0.27 per $1 ACV versus $1.16 for new logos.
- OpenView Partners (2023) SaaS Benchmarks, 700-plus companies. 50 to 60% of new ARR from expansion (best-in-class).
- KeyBanc (2024). Expansion equals 52% of new ARR.

Calibrate ownership thresholds to your ACV bands and org structure before committing them to governance.
