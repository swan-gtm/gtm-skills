---
name: weekly-performance-advisor
title: Weekly performance advisor
description: |
  Use this skill for the recurring review of a running outbound book — the Monday question of what
  needs attention this week. Produces a triaged list of replies waiting on an answer, the campaigns
  that are genuinely underperforming with the one step to fix on each, and week-over-week movement
  on the metrics that matter. Trigger phrasings: "how are my campaigns doing this week", "weekly
  outbound review", "my Monday cockpit", "campaign health at a glance", "who do I need to reply
  to", "which campaigns should I fix", "is my outbound trending up or down".
category: RevOps
tags: [Sales, RevOps]
---

Applies to a book of running campaigns on a recurring cadence. Produces a reply queue in urgency order, a ranked fix list, and the week's movement.

## Two questions, in this order

A weekly review answers *who is waiting on me* and *what is broken*, and the first outranks the second every time. A prospect who replied four days ago and got nothing is a lost deal that already happened; a campaign three points below benchmark is a problem that will still be there tomorrow.

Most dashboards invert this, leading with aggregate performance because it's easier to compute. Lead with the people.

## Nothing is scored below ten sends

A campaign with six sends and one reply does not have a 17% reply rate. It has six sends.

Set a floor — ten sends per metric before it gets a status at all — and render everything under it as insufficient volume rather than as a number. Without that floor, the smallest and newest campaigns dominate every ranking, and the weekly review turns into a tour of statistical noise.

The same rule applies per step, not just per campaign: a sequence can have plenty of total volume and a fourth touch that only twelve people ever reached.

## Aggregate on the ratio, not on the percentages

Portfolio-level numbers are where this goes quietly wrong. Averaging campaign reply rates gives a 2,000-send campaign and a 40-send campaign equal weight in the number leadership reads.

Sum the numerators, sum the denominators, divide once. A volume-weighted portfolio rate is the rate that actually happened; a mean of percentages is an artefact of how the work was split into campaigns.

## Judge the campaign on its primary channel

A multichannel campaign that sends 900 LinkedIn messages and 60 emails is a LinkedIn campaign. Letting the email leg's weak numbers flip the whole campaign to "broken" sends someone off to rewrite copy that 6% of the audience saw.

Identify the primary channel by volume, treat a channel as co-primary only when it carries a meaningful share, and let only the driving channel's metrics set the campaign's status. A weak secondary channel is worth flagging as a leg to fix — not worth condemning the campaign for. Technical health is the exception: a bounce problem counts regardless of channel weighting, because it damages the sending domain rather than just this campaign.

The zone thresholds, the scoring floor and the weighting rules are in `references/benchmark-zones.md`.

## One fix per campaign, at the earliest broken step

A campaign failing on three metrics does not need three fixes. Walk the funnel in order — deliverability, then connection acceptance, then opens, then replies — and name the *first* thing that's broken. Everything downstream of a broken step is measuring a filtered audience, so fixing the later metric first is treating a symptom.

Two refinements that matter. Exclude the terminal break-up message from diagnosis: it's designed to underperform and flagging it wastes the fix. And cap how confidently you state a diagnosis when the flagged step's own volume is thin — a red metric on eighteen sends is a hypothesis, not a finding.

Rank the fix list by severity multiplied by the number of people affected. The mildly-broken campaign touching four thousand prospects outranks the badly-broken one touching ninety. `references/campaign-diagnosis.md` covers the funnel order, the cause-to-action mapping, and the severity scoring.

## Sort the replies by what they cost to ignore

Explicit meeting requests first, then interested, then neutral — and inside each group, longest-waiting first. Past about three days a warm reply has cooled enough to flag.

Only surface the replies that need an action. Rejections and wrong-fits collapse to a count; they're worth knowing and not worth reading. Where an automatic qualification was corrected on review, keep that visible — a classifier that keeps mislabelling one category is itself a finding. `references/reply-triage.md` has the classification and the sort.

## Compare against two baselines

Week over week tells you what changed. A trailing multi-week average tells you whether it matters — a single week's movement is mostly noise, and teams that react to it thrash their campaigns weekly.

Show both. Get the direction right per metric: for bounce rate, down is the good direction, and an arrow pointing the wrong way is worse than no arrow. On the first run there is no history — say "baseline week" rather than rendering zeros as deltas. And when a review is re-run mid-week, a refresh may only add to the week's counts, never drop something already counted. `references/weekly-trends.md` covers the comparison and the recount rules.

## What good looks like

The tell of a good operator: they know their own numbers well enough that published benchmarks are a sanity check rather than a target, and they can name which campaign is dragging the portfolio average without opening anything. They treat one bad week as noise and three as a trend.

The mediocre version leads with a portfolio reply rate, averages it wrong, celebrates a number that moved because a small campaign ended, and shows a tidy dashboard with no reply queue in it — so the team reads their metrics and still misses the person who asked for a call on Thursday.

Good output is short and ordered by what to do first. Every rate carries its denominator, every campaign flagged for a fix names one step and one action, and anything with too little volume says so instead of showing a number. If someone reads it and doesn't know what to open first, it failed regardless of how much is on it.

## Rules

- MUST lead with replies waiting on an answer, before any performance metric.
- MUST require a minimum send volume before scoring any metric, and render thin data as insufficient volume rather than as a rate.
- MUST aggregate portfolio metrics as summed numerator over summed denominator, never as a mean of rates.
- MUST set campaign status from the primary channel's metrics, flagging a weak secondary channel separately.
- MUST name one fix per campaign, at the earliest broken step in the funnel.
- MUST state the sample size alongside every rate.
- NEVER diagnose a campaign on its break-up step.
- NEVER present a single week's movement as a trend without a longer baseline alongside it.
- NEVER let a mid-week refresh reduce a count already reported for that week.
