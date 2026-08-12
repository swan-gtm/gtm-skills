# CRM health scoring model

Give every rule an impact weight from 1–5. For a rule, calculate `pass rate = 1 - failures / eligible records`. Exclude unknowns from the denominator but report their rate; if unknowns exceed 10%, mark the rule low confidence.

Object score is the weighted mean of its rule pass rates × 100. Composite score weights objects by business relevance, not record count. A starting model is accounts 30%, contacts 25%, opportunities 35%, activities 10%.

Do not publish an object score with fewer than 30 eligible records without a small-sample warning. Set critical-rule floors separately: suppression conflicts 100% pass, active ownership at least 99%, and unresolved duplicate accounts tied to open opportunities 0 tolerated.

Version weights, populations, and thresholds together. When any changes, calculate the prior snapshot under both versions if possible and label the rebaseline.
