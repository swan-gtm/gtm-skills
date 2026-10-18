---
name: customer-health-tiers
title: Customer health tiers
description: |
  Use this skill to run a nightly health check across every paying customer from product usage, and to replace a single blended health score with three separate reads: lifecycle phase (activating, established, churned), risk tier and expansion tier, each high, medium or low. It applies explicit rules (went dark, never activated, key setup step missing, usage down month over month, output nobody reviews, repeated top-ups, a cheaper plan at their volume), writes all three to the CRM, alerts the owner the moment an account turns high risk or high expansion, opens one expansion deal per account, and sends a weekly digest. Also answers "customer health score", "churn risk model", "which customers are at risk", "usage-based expansion signals".
category: Deals
tags: [RevOps, Sales]
---

Applies when you need to know, every day, which paying customers are slipping and which are outgrowing their plan, from what they actually do in the product. Produces three tiers per customer in the CRM, immediate alerts on changes that matter, and a weekly digest.

A single health score hides the thing you need to act on. A customer can be at high risk and high expansion at once: heavy usage concentrated in one person who is about to leave. So this skill keeps three independent reads, each with its own rules, and never blends them.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full list and the defaults to tune.

- `{{USAGE_SOURCE}}`: Where product usage lives (e.g. your product database or warehouse); read-only access is enough
- `{{BILLING_SOURCE}}`: Where subscriptions live: status, plan, price, first paid date, renewal date, included and used allowance, seats
- `{{CRM}}`: Your CRM (e.g. HubSpot, Salesforce)
- `{{USAGE_EVENT}}`: The event that means "the product did work for them" (e.g. a workflow run, a report generated, an API call)
- `{{HUMAN_ACTION}}`: The event that means "a person actively used it" (e.g. a user message, a login with an action)
- `{{KEY_SETUP_STEP}}`: The setup step whose absence best predicts churn (e.g. connecting a sending account, installing the integration)
- `{{GENERATED_OUTPUT}}`: Output the product produces for people to review, if any (e.g. drafts, alerts, recommendations)
- `{{USAGE_UNIT}}`: The allowance customers consume (e.g. credits, seats, API calls)
- `{{PLAN_PRICING}}`: Per-unit rate and base fee for the plans in the plan-upgrade check
- `{{TOP_TIER_TAGS}}`: Account tiers whose expansion goes to the dedicated owner (e.g. Diamond and Gold)
- `{{EXPANSION_OWNER}}`: Owner of expansion for top-tier accounts
- `{{CS_OWNER}}`: Owner of risk alerts, and of expansion for everyone else
- `{{EXPANSION_CHANNEL}}`: Team channel that sees every high-expansion change
- `{{EXPANSION_PIPELINE}}`: The CRM pipeline and first stage for expansion deals
- `{{DIGEST_RECIPIENT}}`: Who gets the weekly digest

## Step 1: Pull the data (all read-only)

Run these against `{{USAGE_SOURCE}}` and `{{BILLING_SOURCE}}` in parallel and join on the customer account. If one pull fails, log it, treat that signal as missing for everyone, and carry on. Never abort the whole run because one source is down.

For every active paying customer (status active or pending cancellation, excluding free plans and internal accounts):

- **Subscription:** plan, status, first paid date, renewal date, monthly price, included and used `{{USAGE_UNIT}}`, base and purchased seats.
- **Activity, last 30 days:** count of `{{USAGE_EVENT}}`, date of the last one, and the share that completed successfully.
- **People:** distinct users with a `{{HUMAN_ACTION}}` in the last 30 days and the 30 days before; date of the last `{{HUMAN_ACTION}}`.
- **Momentum:** `{{USAGE_EVENT}}` count this 30 days against the previous 30 days.
- **Setup:** whether `{{KEY_SETUP_STEP}}` is in place.
- **Output review, last 14 days:** `{{GENERATED_OUTPUT}}` items created and items reviewed.
- **Top-ups:** extra `{{USAGE_UNIT}}` purchases in the last 60 days.
- **Paid-period volume:** average monthly `{{USAGE_UNIT}}` consumed over the last three months, counting only months after the first payment, with at least two full months of data. Trial usage often runs hot and would distort this.

**Month-over-month floor:** only use momentum signals for accounts with at least 50 `{{USAGE_EVENT}}` in the previous 30 days. Below that, percentages swing on noise.

## Step 2: Lifecycle phase

Phase is based on tenure. It changes once (activating to established) and resets only on cancellation. Use the first paid date as the start: it is unaffected by trial extensions.

| Phase | Rule |
|---|---|
| Churned | Status is pending cancellation |
| Activating | Active, and first paid date is within the last 60 days (or missing; log the gap) |
| Established | Active, and first paid date is more than 60 days ago |

## Step 3: Risk tier

Go top to bottom. The first high match sets high; otherwise check medium; otherwise low.

**High risk**, if any of:
- Status is pending cancellation.
- No `{{USAGE_EVENT}}` in the last 30 days, and they first paid more than 14 days ago. They never activated.
- Last `{{USAGE_EVENT}}` more than 21 days ago. They went dark.
- `{{KEY_SETUP_STEP}}` is missing. This is often the single strongest churn predictor; confirm it against your own churned customers.
  - For activating customers more than 14 days past first payment, give this its own alert reason ("paid customer past day 14, key setup step still missing"). Some usage can run without the setup step, which hides the problem.
- Established customers only, above the floor: `{{USAGE_EVENT}}` volume down more than 50% month over month.

**Medium risk**, if any of (and not already high):
- Established, above the floor: volume down 30% to 50% month over month.
- Last `{{USAGE_EVENT}}` 14 to 21 days ago.
- Last `{{HUMAN_ACTION}}` 14 to 30 days ago, with no high signal.
- Established: active users dropped by half or more month over month, from at least 2.
- 50 or more `{{GENERATED_OUTPUT}}` items in 14 days and none reviewed. The product is working and nobody is looking.
- More than 40% of `{{USAGE_EVENT}}` failed, out of at least 10.

**Low risk:** none of the above.

## Step 4: Expansion tier

Only for active customers. Churned customers get no expansion tier.

**High expansion**, if any of:
- **Credit upsell:** 2 or more top-ups in 60 days.
- **Credit upsell:** on pace to run out more than 14 days before renewal, two months in a row. Check that last run also flagged it before setting high; one month is a watch signal, not an upsell. Skip this projection if the renewal date is missing or in the past.
- **Plan upgrade:** on a lower plan, sustaining enough volume that the next plan is cheaper for them (see below).

**Plan-upgrade check (required before flagging).** Using `{{PLAN_PRICING}}`, compute what they would save per month:
- Current plan cost = average monthly volume × current per-unit rate.
- Next plan cost = next plan base fee + average monthly volume × next plan per-unit rate.
- Savings = current cost − next plan cost.
- **Do not flag it if savings are under $40 a month.** The conversation promises savings; below that, it is not worth the customer's effort to switch.
- Volume threshold = (next plan base fee + savings floor) / (current per-unit rate − next per-unit rate). Example: a $0.20-per-unit plan against a $99 base plus $0.16 per unit gives (99 + 40) / 0.04 ≈ 3,475 units a month. Recompute it whenever pricing changes, and do not run this signal on stale pricing.

**When both credit upsell and plan upgrade fire:** send one alert, not two, and open one deal. Lead with the plan upgrade (the bigger conversation) and include the usage-efficiency points as supporting content.

**Medium expansion (watch only, no outreach):**
- Above the floor: volume up 30% or more month over month.
- Seat utilization at 75% or more of base plus purchased seats.
- On pace to run out more than 7 days before renewal, once (same renewal-date guard).
- 2+ distinct users with a `{{HUMAN_ACTION}}` in 30 days and 200+ `{{USAGE_EVENT}}` in 30 days: broad adoption.

**Low expansion:** none of the above.

## Step 5: Write to the CRM and alert on changes

For each customer, find the company in `{{CRM}}` by domain (skip and log if not found). **Read the current tiers before writing**, so you can tell what changed.

**Risk turns high** (was not high, now is): alert `{{CS_OWNER}}` immediately, any day of the week:
> Risk alert: <Company> (<domain>). Risk → High. Phase: <phase> · Plan: <plan> · MRR: $<mrr>. Reason: <one line, e.g. "key setup step missing", "no activity since day 14", "last activity 24 days ago", "volume down 62% month over month">.

**Expansion turns high** (was not high, now is):
- Owner: `{{EXPANSION_OWNER}}` for accounts tagged `{{TOP_TIER_TAGS}}`, `{{CS_OWNER}}` for everyone else. If `{{EXPANSION_OWNER}}` is out, notify `{{CS_OWNER}}` for visibility only; do not act or draft until the owner is back.
- Send ONE alert, matching the signal: credit upsell, plan upgrade (with the monthly and annual savings), or both (plan upgrade as the headline).
- Post the same alert to `{{EXPANSION_CHANNEL}}`.
- Open ONE deal in `{{EXPANSION_PIPELINE}}` at its first stage: type expansion, named "<Company>: Expansion <Month Year>", amount = MRR × 12, owner = whoever got the alert, linked to the company.

Alerts and deals prompt a person to act. This skill never contacts the customer.

**Then update the company record:** lifecycle phase, risk tier, expansion tier (blank if churned), subscription status, plan, renewal date, allowance total and used, 30-day activity count, last activity date, MRR, ARR, and a last-synced timestamp. If a property does not exist yet in `{{CRM}}`, log it and skip it; never fail the run.

## Step 6: Weekly digest (one day a week, default Monday)

Steps 1 to 5 run every night. The digest goes to `{{DIGEST_RECIPIENT}}` once a week:

```
Customer health digest, <date>

Paying customers: <n>
By phase: Activating <n> · Established <n> · Churned <n>
By risk: High <n> · Medium <n> · Low <n>
By expansion: High <n> · Medium <n> · Low <n>

High risk (act today), least active first:
- <Company> (<domain>): phase, plan, MRR, reason

Medium risk (watch):
- <Company> (<domain>): phase, plan, reason

High expansion, biggest MRR first:
- <Company> (<domain>): owner, plan, MRR, signal, savings if plan upgrade

Medium expansion (watch):
- <Company> (<domain>): signal

Running low (85%+ of allowance used):
- <Company>: <used>/<total>

On autopilot (50+ activity in 30 days, no human action in 45+ days):
- <Company>: <n> in 30 days, last human action <n> days ago
```

Leave out any empty section.

## Rules that keep it trustworthy

- Read-only against product and billing data. The only writes are CRM properties, alerts and expansion deals.
- One failed pull never stops the run.
- Momentum signals need the 50-event floor, and month-over-month risk applies to established customers only. Activating customers are judged on absolute signals: no activity, no setup, last activity date.
- Do not infer churn from the renewal date. Month-to-month customers often have a stale renewal date while still active; subscription status is the source of truth.
- Medium expansion never triggers outreach. Only high does, and only as an alert to a person.

## What good looks like

- Every customer has three tiers in the CRM, and each tier can be traced to a named rule.
- A customer who turns high risk at 2am has an alert waiting for its owner in the morning, with a one-line reason specific enough to act on.
- No customer gets two expansion alerts or two deals from one run.
- Plan-upgrade alerts only fire when the savings clear the floor, and they show the numbers.
- The weekly digest fits on one screen and opens with the accounts to act on today.
- Missing data shows up as a logged gap, never as a silent "low".
