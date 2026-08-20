# Zones, floors and aggregation

## Three zones per metric

Each metric gets a good threshold and a floor, producing on target / watch / to fix.

| Metric | Good | Floor | Direction |
|---|---|---|---|
| Connection acceptance | 30% | 20% | higher is better |
| LinkedIn reply | 25% | 15% | higher is better |
| Email open | 60% | 45% | higher is better |
| Email reply | 6% | 3% | higher is better |
| Email click | 8% | 4% | higher is better |
| Bounce rate | 2% | 5% | **lower is better** |

For a higher-is-better metric: on target at or above good, watch at or above floor, otherwise to fix. For bounce, invert both comparisons.

**Bounce is the one row not to loosen.** The others are calibration and can move with the market; this one is a hard technical limit. A bounce rate in the double digits burns the sending domain — mailbox providers read it as list abuse, and the damage lands on every campaign sent from that address, including the ones that were working. Treat 2% as the ceiling for healthy sending and 5% as the point where sending should stop until the list is verified and the domain re-warmed, rather than a number to watch decline over a few weeks.

This is why bounce is always status-driving regardless of which channel a campaign leans on: it is the only metric here whose damage outlives the campaign.

**These are starting defaults, not truth.** They're calibrated for cold outbound to a B2B audience, and they will be wrong for warm re-engagement, for a different market, or for a notably different offer. Replace them with the team's own trailing median as soon as there's enough history to compute one — their own numbers already account for their offer, their market and their execution, which no published figure does.

The bounce row is excluded from that substitution. A team whose own history sits at 9% bounce has a domain problem, not a benchmark; adopting their median as the target would encode the damage as normal. Every other row moves with the market, that one doesn't.

Email reply in particular swings hard by temperature. Six percent is a reasonable cold bar and a poor warm one.

## The volume floor

**Ten sends minimum before a metric is scored.** Below that, render "insufficient volume" — never a percentage.

One reply on six sends is not a 17% reply rate. Without this floor the newest and smallest campaigns dominate every ranking, because small denominators produce extreme rates in both directions, and the weekly review becomes a tour of noise.

Apply it per metric and per step, not once per campaign. A sequence with two thousand sends can easily have a fourth touch that only reached forty people — and that step's reply rate deserves the same floor.

## Severity

For ranking, measure how far below the floor a metric sits, as a proportion of the floor:

- Higher-is-better: `(floor − value) / floor`, clamped at zero.
- Lower-is-better: `(value − floor) / floor`, clamped at zero.

This normalises across metrics with very different scales, so a bounce problem and a reply problem can be compared on one axis.

## Portfolio aggregation

**Sum the numerators, sum the denominators, divide once.**

Averaging per-campaign rates gives a campaign with forty sends the same weight as one with two thousand. The resulting number describes nothing that happened — it's an artefact of how the work was divided into campaigns, and it moves whenever a small campaign starts or ends.

Only campaigns that are active on that channel and above the volume floor feed a portfolio metric. Carry the count of contributing campaigns alongside the number, so a portfolio rate built from two campaigns is visibly different from one built from twenty.

## On deliverability

Where a platform computes delivered as sent minus bounced, "deliverability" is arithmetically `100 − bounce` and carries no independent information. It is not inbox placement, and showing it as a separate metric implies a measurement nobody made.

Track bounce instead. It's the same information, honestly labelled, and it's the actionable half — bounce is a list-quality and warm-up problem with a known remedy.

## Not every metric drives status

Click-through is worth showing and shouldn't set a campaign's status: it depends heavily on whether the copy contains a link at all, so a campaign with no link scores zero and is fine.

Distinguish metrics that diagnose from metrics that inform, and let only the former drive the red/yellow/green.
