# Edge Cases & Attribution Anomalies

When analyzing enterprise LinkedIn Ads performance, resolve two primary structural edge cases before finalizing a diagnostic verdict.

## Edge Case 1: High Exposure Frequency with Low ICP Coverage

Average frequency metrics reported at the campaign level can disguise structural reach imbalances.

### Analysis Protocol:
1. Extract persona-level frequency alongside total target account reach percentage.
2. If average campaign frequency appears high while overall target account penetration remains low, isolate whether budget is being consumed by a small fraction of heavy users.
3. Calculate cumulative frequency across all active campaigns to identify hidden overlap where individual decision-makers are exposed across multiple ad sets.
4. Do not reduce overall budget; instead, implement persona-level caps, segment targeting lists, and test controlled audience expansion parameters.

## Edge Case 2: High CPO with Accelerated Sales Cycle Velocity

In enterprise B2B SaaS, campaigns with a high Cost per Opportunity (CPO) may generate significant revenue value by shortening sales cycles on high-ACV deals.

### Analysis Protocol:
1. Extract median time-to-close metrics for opportunities associated with ad-exposed target accounts versus non-exposed accounts.
2. Evaluate whether exposed accounts exhibit a shorter sales cycle length (e.g., a 20% to 30% reduction in deal duration).
3. Check for selection bias: verify whether exposed accounts were already in active sales conversations or possessed higher baseline intent before ad exposure.
4. Compare exposed vs. non-exposed accounts within matching deal stages and firmographic tiers.
5. If baseline intent bias cannot be ruled out, issue a status of **Unproven Hypothesis** and escalate for human review before declaring campaign efficacy.
