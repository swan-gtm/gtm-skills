# CRM audit rubric

Score each rule on impact, prevalence, confidence, and recurrence.

## Severity

| Score | Definition | Example |
| --- | --- | --- |
| 4 critical | Causes unauthorized access, material reporting error, or immediate customer harm | Active records owned by a departed user with live routing |
| 3 high | Breaks routing, pipeline decisions, or attribution for a meaningful segment | Duplicate accounts splitting activity and opportunity value |
| 2 medium | Slows execution or weakens analysis but has a safe workaround | Missing industry on target accounts |
| 1 low | Cosmetic or rarely used | Optional formatting inconsistency |

## Batch priority

Calculate `severity × affected percentage × recurrence multiplier`. Use affected percentage as a decimal. Set recurrence multiplier to 2 when the source is still producing defects, otherwise 1. Prioritize ongoing corruption even when its current count is smaller.

Start with no more than 100 operations or 5% of the affected population, whichever is smaller. For irreversible merges, begin with 10. Expand only after the same audit passes and reconciliation shows no unexplained outcomes.

Confidence of 100% means the value follows deterministically from an owned source or explicit rule. At 80–99%, require sampled review. Below 80%, route the record for a human decision rather than proposing a write.
