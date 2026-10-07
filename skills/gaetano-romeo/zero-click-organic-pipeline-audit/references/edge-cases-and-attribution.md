# Edge Cases & Attribution Anomalies

When analyzing B2B SaaS organic performance, resolve two primary structural edge cases before finalizing a diagnostic verdict.

## Edge Case 1: Extended Enterprise Sales Cycles

In B2B enterprise SaaS, median sales cycles frequently range from 6 to 12 months. Current quarter pipeline creation reflects organic engagement and search touchpoints from previous quarters.

### Analysis Protocol:
1. Extract the median time-to-close metric from the CRM.
2. Apply a temporal offset equal to the median sales cycle length when comparing session drops with opportunity creation.
3. Group opportunity cohorts by the date of initial organic touchpoint rather than the date of opportunity creation.
4. If the active evaluation window is shorter than the median sales cycle, suspend definitive verdicts and issue a status of **Pending Cohort Closure**.

## Edge Case 2: Paid Campaign & External Channel Confounding

Surges or reductions in brand search volume are often driven by external paid activities rather than organic performance.

### Analysis Protocol:
1. Cross-reference brand search volume fluctuations against timeline logs for LinkedIn ad spend increases, paid search expansion, product launches, or major PR events.
2. If brand search volume increases concurrently with paid campaign scaling, isolate pure brand queries from high-intent brand queries (e.g., `[Brand] vs [Competitor]` or `[Brand] pricing`).
3. If paid campaigns are scaled down and brand search volume decreases symmetrically, classify the decline as a paid channel effect rather than an organic SEO degradation.
4. Suspend organic attribution claims until cross-channel spend changes are isolated from search console baselines.
