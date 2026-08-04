# Signal → Trigger → Action: Forecast Breach Rules

On-demand reference for the revops-forecasting skill.

These connect forecasting to the Operating Cadence. When a forecast signal fires, the cadence ensures someone acts: not next quarter, but this week. These rules plug into the revenue dashboard and weekly/monthly rituals.

## Forecast-Specific Breach Rules

| Signal | Trigger Threshold | Action | Forum | Owner |
|--------|------------------|--------|-------|-------|
| Pipeline coverage drops below 3x | Coverage < 3x for current quarter target | Activate pipeline generation contingency within 5 business days. Pull forward next-quarter pipeline. Review outbound, partner, and marketing channels. | Weekly revenue dashboard | CRO + CMO |
| Commit coverage below 0.9x target | Commit < 90% of remaining quarter target | Inspect every Best Case deal for acceleration potential. Identify deals that can move to Commit with specific interventions. | Weekly Sales Pipeline Loop | VP Sales |
| Forecast accuracy trending >±20% | 2 consecutive weeks where delta between forecast and pace exceeds 20% | Diagnose root cause: qualification drift, stage definition inconsistency, or rep sandbagging. Initiate A3 problem statement. | Weekly revenue dashboard | RevOps |
| Best Case slippage rate >40% | More than 40% of Best Case deals slip in any 4-week period | Tighten Best Case criteria. Review whether Best Case deals meet at least 3 of 5 Commit validation checkboxes. Likely a qualification problem. | Monthly Strategy Review | VP Sales + RevOps |
| Single rep variance >±30% for 2+ quarters | Individual rep forecast accuracy below ±30% consistently | Coaching intervention: is it optimism (always over), sandbagging (always under), or methodology gap? Different root causes, different fixes. | Manager 1:1 | Frontline Manager |
| New pipeline creation below 80% of period target | Weekly pipeline creation pace tracking below 80% of what's needed | Gap alert to leadership. Diagnose: is it a generation problem (not enough activity) or a conversion problem (meetings happening but not converting)? | Weekly revenue dashboard | CMO + VP Sales |
| Weighted pipeline diverges from category forecast by >25% | Stage-weighted pipeline total differs from Commit + Best Case total by >25% | The two methods are disagreeing. Likely cause: stage inflation (deals in later stages that haven't earned it). Run stage audit on deals contributing to the gap. | Weekly Sales Pipeline Loop | RevOps |

## Forecast Breach Escalation Path

Not all breaches are equal. Use this escalation framework:

```
SEVERITY 1: INFORMATION (no action required yet)
  Coverage between 2.5-3x with >6 weeks left in quarter
  Single-week variance spike (noise, not signal)
  One rep's forecast off in isolation
  → Note in revenue dashboard. Monitor next week.

SEVERITY 2: WARNING (action required this week)
  Coverage below 3x with <6 weeks left
  Forecast accuracy trending >±15% for 2+ weeks
  Best Case slippage rate climbing
  → Assign investigation owner. Report back in next weekly ritual.

SEVERITY 3: BREACH (management intervention immediately)
  Coverage below 2.5x with <4 weeks left
  Commit coverage below 0.8x target
  Forecast accuracy >±25% for 3+ weeks
  → Escalate to CRO/CEO. Activate contingency playbook.
  → Consider: adjust expectations with board proactively.

SEVERITY 4: CRITICAL (executive action)
  Coverage below 2x with <3 weeks left
  Quarter is materially at risk (>20% miss projected)
  → Board-level communication required.
  → Shift focus to: protect what's in Commit, manage the miss, build next quarter.
```

## Pipeline Generation Breach Rules

Forecasting doesn't just measure the current quarter; it must also monitor next quarter's pipeline health:

| Signal | Trigger | Action | Timeline |
|--------|---------|--------|----------|
| Next quarter pipeline < 2x target at quarter midpoint | Projected coverage gap | Activate outbound blitz + partner channel activation + marketing campaign acceleration | Within 1 week |
| Pipeline creation rate declining month-over-month | 2+ months of declining new pipeline | Diagnose: is inbound drying up, outbound slowing, or conversion dropping? Different roots, different fixes | Within 2 weeks |
| Pipeline age increasing (average days open rising) | Average deal age >1.5x segment benchmark for 2+ weeks | Pipeline deflation sprint: remove zombies to restore healthy metrics. See deal-velocity-engineer. | Within 1 week |

## Connecting Forecasting to the revenue dashboard

The forecast is not a spreadsheet; it's a tile in the revenue dashboard with bands and breach rules:

```
FORECAST TILE CONFIGURATION:

  Metric: Current quarter forecast vs. target
  Green band: Commit ≥ 90% of target AND coverage ≥ 3x
  Amber band: Commit 70-90% of target OR coverage 2.5-3x
  Red band: Commit < 70% of target OR coverage < 2.5x

  Secondary: Forecast accuracy trend (trailing 4-week average)
  Green: ±10%
  Amber: ±10-20%
  Red: ±20%+

  Leading indicator: Next quarter pipeline creation pace
  Green: On track for 3x+ coverage
  Amber: Tracking to 2-3x coverage
  Red: Tracking to <2x coverage
```

When a tile turns red, it surfaces in the Weekly revenue dashboard ritual and triggers the corresponding breach action from the table above. The goal is: no surprises at quarter end. Every miss should be visible 6+ weeks in advance.
