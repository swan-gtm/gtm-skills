# Setup and customization checklist

## Placeholders

- [ ] `{{USAGE_SOURCE}}` and `{{BILLING_SOURCE}}`: read-only access to usage events and subscriptions, joined on the customer account.
- [ ] `{{USAGE_EVENT}}`: the one event that means the product did work for the customer. Pick one, so the counts mean something.
- [ ] `{{HUMAN_ACTION}}`: the event that means a person actively used it, as distinct from automated runs.
- [ ] `{{KEY_SETUP_STEP}}`: check it against your churned customers. If a different setup step predicts churn better, use that one.
- [ ] `{{GENERATED_OUTPUT}}`: if your product produces nothing for people to review, drop the review signal.
- [ ] `{{USAGE_UNIT}}` and `{{PLAN_PRICING}}`: per-unit rates and base fees for the plan-upgrade check.
- [ ] `{{TOP_TIER_TAGS}}`, `{{EXPANSION_OWNER}}`, `{{CS_OWNER}}`, `{{EXPANSION_CHANNEL}}`, `{{DIGEST_RECIPIENT}}`.
- [ ] `{{EXPANSION_PIPELINE}}`: the pipeline and first stage. Resolve stage IDs at run time instead of hard-coding them.
- [ ] CRM properties: lifecycle phase, risk tier, expansion tier, subscription status, plan, renewal date, allowance total and used, 30-day activity, last activity date, MRR, ARR, last synced. Create them before the first run; missing ones are skipped and logged.

## Defaults to tune

| Default | Value | Notes |
|---|---|---|
| Activating window | 60 days from first payment | |
| Never activated | No activity and 14+ days since first payment | |
| Went dark | 21+ days since last activity (high), 14 to 21 (medium) | |
| Human silence | 14 to 30 days since last human action (medium) | |
| Month-over-month floor | 50 events in the prior 30 days | Below it, momentum signals are skipped |
| Volume drop | More than 50% (high), 30% to 50% (medium) | Established customers only |
| User drop | Half or more, from at least 2 users | Established only |
| Unreviewed output | 50+ items in 14 days, none reviewed | |
| Failure rate | Over 40% of at least 10 events | |
| Top-ups | 2+ in 60 days (high expansion) | |
| Running out | 14+ days before renewal, two months running (high); 7+ days once (watch) | |
| Plan-upgrade floor | $40 a month in savings | Recompute the volume threshold on any price change |
| Seat utilization | 75%+ (watch) | |
| Autopilot drift | 50+ events in 30 days, no human action in 45+ days | Digest only |
| Running low | 85%+ of allowance used | Digest only |

## Behaviour that should not change

- Three separate tiers; never blend them into one score.
- Read-only against product and billing data.
- A failed pull is logged and skipped; the run continues.
- One alert and one deal per account per run.
- Medium expansion never triggers outreach, and nothing here contacts a customer.
- Subscription status, not the renewal date, decides churn.
