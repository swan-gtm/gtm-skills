---
name: linkedin-enterprise-ads-audit
title: LinkedIn enterprise ads audit
description: "Use this skill when auditing B2B enterprise LinkedIn Ads campaigns to evaluate account-level reach, ad fatigue, lead form quality, and cost per opportunity relative to contract value."
category: Ads
---

Audit enterprise LinkedIn campaigns by looking beyond platform-level vanity metrics, isolating account penetration from generic reach, evaluating native lead form pipeline conversion, and measuring revenue impact against contract margin.

## Quick verdict

Execute a two-stage evaluation before adjusting campaign budgets or targeting settings.

### Stage 1: Audience precision and target account reach
* Load campaign demographics and match impressions against the designated ABM account list.
* Check whether Audience Expansion or Audience Network placements are draining spend outside target accounts.
* If spend on out-of-ICP accounts exceeds target thresholds, label as **Audience Dilution**.
* If account coverage is below target depth while frequency rises, label as **Reach Bottleneck**.

### Stage 2: Lead quality and pipeline velocity impact
* Evaluate conversion rates from native Lead Gen Forms vs. landing page requests into qualified opportunities.
* Correlate prior account ad exposure with sales cycle velocity and opportunity creation.

## The four tests

A campaign is classified as **Healthy & Scalable** only if it satisfies all four conditions. Full thresholds are in `references/methodology-and-thresholds.md`.

| Test | Healthy | Critical |
|---|---|---|
| 1. Account coverage and reach depth | At least 60% of target accounts in the ABM list receive at least one impression in the evaluation window | Less than 30% of target accounts are reached while average frequency per persona climbs |
| 2. Audience saturation and frequency | Average exposure frequency remains balanced alongside stable click-through rates | Frequency per persona exceeds 10 impressions in 30 days, with engagement down more than 25% and rising cost per target account reached |
| 3. Form factor quality ratio | Lead-to-opportunity conversion for native Lead Gen Forms reaches at least 40% of the rate for website demo requests on matching segments | Native Lead Gen Form conversion to qualified opportunity drops below 20% of website demo request performance |
| 4. CAC vs. contract value sustainability | Media Cost per Acquired Customer stays below 20% of ACV multiplied by gross margin, with payback within 12 months | Media Cost per Acquired Customer exceeds 35% of gross-margin-adjusted ACV, or payback exceeds 18 months |

## Verdict

* **Healthy & Scalable:** Test 1 Passed + Test 2 Passed + Test 3 Passed + Test 4 Passed. Action: Maintain target criteria, test new creative variations, and scale budget incrementally.
* **Audience/Quality Failure:** Test 1 Failed OR Test 2 Failed OR Test 3 Failed OR Test 4 Failed. Action: Disable audience expansion, review form qualification criteria, and adjust frequency caps.
* **Inconclusive Data:** Account-level attribution untracked or evaluation window shorter than median sales cycle. Action: Suspend verdict and flag data collection requirements.

## Before finalizing

* Resolve the two structural edge cases in `references/edge-cases-and-attribution.md`: high exposure frequency with low ICP coverage, and high cost per opportunity with accelerated sales cycle velocity.
* Check the red flags and the blinding condition in `references/red-flags-and-disqualification.md`.

## What good looks like

* **Account-level linkage comes first.** If campaign impressions and ad engagements cannot be linked to CRM opportunity records at the account level, do not issue budget reallocation recommendations, bid adjustments, or creative pause directives. Require account-level CRM exposure tracking before finalizing the evaluation.
* **Frequency is read per persona, not per campaign.** Campaign-level averages can disguise reach imbalances, so cumulative frequency is calculated across all active campaigns to find decision-makers exposed across multiple ad sets. The fix is persona-level caps and segmented lists, not a lower overall budget.
* **A high cost per opportunity is not a failure on its own.** Exposed and non-exposed accounts are compared within matching deal stages and firmographic tiers, and if baseline intent bias cannot be ruled out, the status is **Unproven Hypothesis** and it is escalated for human review.
* **The common mistake:** letting Audience Expansion or the Audience Network run so that more than 20% of media spend reaches accounts outside the ICP or target ABM list. The algorithm pursues volume over target precision.
* **Lead volume is checked against who is actually converting.** Non-buyer job titles or non-business email domains above 25% of form submissions mean the creative is attracting curiosity rather than decision-maker purchasing intent.
