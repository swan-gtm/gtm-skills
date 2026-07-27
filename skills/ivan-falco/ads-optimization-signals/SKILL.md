---
name: "ads-optimization-signals"
title: "Optimization Signals & Testing Rules"
description: "Use this skill when reading optimization signals — which metrics justify action, testing rules, and when a result is real versus noise."
category: Ads
---

# Optimization Signals & Testing Rules

## Why Optimization Matters

- After campaigns launch, the real work begins
- Take time for planning new experiments and writing down learnings
- Building on your learnings while others repeat the same mistakes

## Optimization Signal Types

- **Leading** = events that happen quickly (< month) - use for quick optimization
- **Lagging** = events that happen slowly (> month) - use for directional truth

## Signals by Stage

| Stage | Leading | Lagging |
|-------|---------|---------|
| Create | CTR, Engagement Rate | Blended Inbound Leads |
| Capture | CPL, CPMQL | Pipe-to-Spend, CPOPP |
| Accelerate/Activate | Accounts Reached, CTR | Avg time to close, Influenced Revenue |
| Revive | CPL, CPMQL | Pipe-to-Spend, ROI |
| Expand | Accounts Reached, CTR | Expansion Revenue |

## Key Insight

The key is choosing the right leading signals that actually influence your lagging events. Experimentation is key, and you'll likely change over time.

The average B2B sales cycle can range from 2-24 months - you can't afford to wait even 2 weeks without being able to optimize your campaigns.

## Testing Rules

### Find Your Breakeven Costs

**Breakeven CPL Formula:**
```
Breakeven CPL = Average deal size x lead to close won rate
```

Example: $3,000 x 10% = $300 breakeven CPL

**Breakeven CPC Formula:**
```
Breakeven CPC = CPL target x landing page conversion rate
```

Example: $300 x 5% = $15 breakeven CPC

### Two Essential Rules

#### 1. Non-Performer Rule

**When to apply:** All time

Pause ad if it's spent 2-3x your target CPL with 0 conversions.

**Example:** Target CPL = $300, ad spends $600-$900 = PAUSE

This helps with pausing new ads you're testing.

#### 2. Maintenance Rule

**When to apply:** Past 7 to 14 days (depending on volume)

Pause ad if the CPL is 1.5-2x over your target CPL.

**Example:** Target CPL = $300, current ad CPL = $450-$600 = PAUSE

This helps with pausing old ads that start to underperform.

## Important Notes

These aren't statistically significant but they're repeatable, easy to follow, and prevent emotional decision-making.

## Proxy Metrics Concept

Product teams have used this methodology for decades (called proxy metrics in the product world). The goal is to choose leading signals that actually influence lagging events. First prove correlation, then work toward proving causation.

A good proxy metric formula: "Percentage of [customers/users] who do at least [minimum threshold for action] by [X period in time]."

A good proxy metric should be:
- Measurable - you can find, collect, and measure the data
- Moveable - you can affect it through changes
- Not an average - averages can be gamed by a small subset doing more
- Correlated to your high-level engagement metric
- Specifies new vs. existing customers
- Not gameable - if someone can artificially inflate it, revise the metric

## Experimentation Library

Track all experiments systematically. Use a tool like Airtable with two views:
- Backlog: All experiment ideas, crowdsourced from the team
- Sprint: Approved experiments currently running or queued

Hypothesis framework for each experiment: "If we do [X], then I believe [Y], as measured by [Z]."

Prioritize experiments using the RICE framework:
- **R**each: How many people will this experiment affect? (1-5)
- **I**mpact: If successful, how impactful will this be? (1-5)
- **C**onfidence: How confident are you in reach and impact estimates? (1-5)
- **E**ffort: How much effort to execute? (1-5, where 1 = low effort, 5 = high effort)

For each completed experiment, document:
- What was tested and the hypothesis
- The result (success, failure, inconclusive)
- Detailed learnings and notes
- Budget spent
- Channel and creative used

Avoid the "activity trap" - testing for the sake of testing, not testing to learn. Stack on your success by building on documented learnings.

Set up automation: When an experiment is marked as completed, automatically notify the team via Slack with the result and key learnings.
