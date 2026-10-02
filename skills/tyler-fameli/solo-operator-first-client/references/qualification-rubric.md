# Qualification rubric

Fit and intent are scored separately because they fail separately. A perfect-fit company with no budget is a HOLD; an eager buyer for work the operator cannot deliver is a disqualify. Run hard stops first, then score.

## Hard stops (disqualify, no score)

| Stop | Evidence that triggers it |
|---|---|
| Ineligible | Posting or buyer requires a location, clearance, license or certification the operator does not hold |
| Staffing in disguise | Hourly seat, 30+ hrs/week, "own our systems", full-time conversion language, no bounded deliverable |
| Unfunded | "Solve it first and we'll pay", "minimum payment only if it works", refuses a funded milestone |
| Unsafe access | Wants shared admin credentials, all-users admin, production access with no change control, bulk deletion |
| Fabrication required | Winning needs a client result, portfolio piece or certification that does not exist |
| Liability the operator can't carry | Open-ended correctness guarantees; bookkeeping, legal or clinical judgment outsourced to the build |

## Scoring

Every criterion is scored 0, 50 or 100. No in-between values; the anchors carry the judgment.

- **0** = evidenced mismatch
- **50** = partial but bounded match
- **100** = explicit strong match
- **UNKNOWN** = no evidence yet. Not zero, not neutral, not positive. Any UNKNOWN forces HOLD and blocks a total; do not renormalize the remaining weights.

Record the evidence and its date beside every score.

### Fit (can this operator deliver this bounded thing?)

| Criterion | Weight | 0 | 50 | 100 |
|---|---|---|---|---|
| Company | 40% | Ineligible buyer or incompatible engagement | Eligible buyer, project only feasible at reduced scope | Eligible buyer, clear owner, bounded project |
| Technology | 30% | Unsafe or outside deliverable capability | Achievable only through a paid diagnostic or a named partner | Relevant self-built proof and an understood delivery path |
| Timing | 30% | Deadline impossible | Reduced scope or later start works | Buyer's window matches current capacity |

Timing measures feasibility, not urgency.

### Intent (does this buyer want it, with money and a decision-maker?)

| Criterion | Weight | 0 | 50 | 100 |
|---|---|---|---|---|
| Explicit need | 40% | Buyer says there is no need | Specific indirect signal | Buyer states the problem and asks for help |
| Funding and access to decision | 35% | Refuses paid terms or outside help | A credible sponsor can seek authorization | Authorized buyer confirms a paid path |
| Commitment | 25% | Declines a next step | Open to talk, no date | Agrees a concrete next step and timeframe |

A marketplace posting with a funded budget and a clear problem statement usually starts at explicit need 100, funding 50 (verified payment history moves it to 100 once the client confirms a paid milestone), commitment 50.

### Composite and decision

Fit = weighted sum of fit criteria. Intent = weighted sum of intent criteria. Composite = 60% fit + 40% intent, used for ranking the queue only.

| Decision | Rule | Next action |
|---|---|---|
| KEEP | Fit >= 70, intent >= 60, composite >= 70, no UNKNOWN, no hard stop | Draft for human approval |
| HOLD | Any threshold missed, or any UNKNOWN | Name the missing evidence; recheck when it appears; no outreach |
| DISQUALIFY | Hard stop, or evidenced mismatch | Record the reason; never revive silently |

Low numbers alone are a HOLD, not a disqualify. Disqualify needs evidence.

Scores are prioritization judgments, never win probabilities. Do not report them as odds.

## Signals that look like intent and are not

| Signal | Read it as |
|---|---|
| Company is hiring an integration / systems owner | Insourcing. HOLD unless the buyer separately asks for outside help |
| Acquired a company, adopted a new platform, opened locations | Hypothesis. Mature native-first adopters often have in-house capability |
| Raised money, growing headcount | Fit context only. Not need, not funding for this project |
| A connector says "they'd love this" | The connector's enthusiasm. Score the buyer after the introduction |
| Plausible relevance to the operator's services | Nothing. Relevance is not qualification |

## Worked score (illustrative, constructed to show the math)

Marketplace posting: a small company's order sync between its store and accounting system drops orders with special characters; budget posted, payment verified, client hired before, posted today, asks for a fixed-price fix.

- Company 100 (eligible, owner is the poster, bounded) ; Technology 100 (operator has built API integrations, failure is diagnosable) ; Timing 100 (one-week window fits) → Fit 100
- Explicit need 100 ; Funding 50 (payment verified, paid milestone not yet confirmed) ; Commitment 50 → Intent 40 + 17.5 + 12.5 = 70
- Composite 0.6 × 100 + 0.4 × 70 = 88 → KEEP. Draft a bid with a funded diagnostic milestone first if root cause is uncertain.

Same posting, but "pay only if it works": hard stop, unfunded. Disqualify, or reply once offering a funded diagnostic and score the response.
