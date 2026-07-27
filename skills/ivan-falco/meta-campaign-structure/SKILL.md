---
name: "meta-campaign-structure"
title: Meta campaign structure
description: "Use this skill when structuring Meta campaigns for B2B — account architecture, campaign and ad-set layout, budget placement, and consolidation rules for high-ACV SaaS."
category: Ads
---

# Campaign Structure for B2B Meta Ads - High-ACV SaaS

How to structure Meta campaigns for B2B SaaS with $30K+ ACV. Covers the three phases (ABO to CBO to Advantage+), campaign architecture, settings, and the 12-month scaling roadmap.

---

## The Three Phases of Campaign Structure

### Phase 1: Audience Validation (ABO - Ad Set Budget)

**Purpose:** Determine which audience sources produce quality leads before spending on creative testing.

**When to use:** Starting Meta for the first time, launching a new offer, entering a new market segment.

**Structure:**
```
Campaign: [Product] - Prospecting - Audience Validation
-- Ad Set 1: 1% CRM Lookalike         [$X/day]
-- Ad Set 2: Third-Party Data (Primer) [$X/day]
-- Ad Set 3: Interest + Job Titles     [$X/day]
-- Ad Set 4: Broad Targeting           [$X/day]
   -- Same 3-4 ads in every ad set (isolate the audience variable)
```

**Critical settings:**
- **Use Ad Set Budget (ABO), NOT CBO** - guarantees each audience gets dedicated budget. CBO would let Meta shift budget away from expensive-but-quality audiences.
- Same ads across all ad sets - you're testing audiences, not creative
- Equal budgets per ad set for fair comparison
- Run for 2-4 weeks minimum
- Turn off Advantage+ audience expansion - click "Further limit the reach" and select your specific audience per ad set

**Validation criteria (check in CRM, not Ads Manager):**
- Job title match to ICP
- Company match to target firmographics
- Lead-to-MQL conversion rate
- Cost per qualified lead (not just cost per lead)
- Quality score from sales calls (see message-validation.md)

**After validation:**
- Kill ad sets producing low-quality leads
- Take winning audience(s) to Phase 2

**Alternative (simpler test):** Two ad sets only - open/broad targeting vs. interest-based. After 2-4 weeks, compare which brings better results. Use the winner going forward.

### Phase 2: Creative Scaling (CBO - Campaign Budget Optimization)

**Purpose:** Scale winning audiences through creative concept testing.

**When to use:** After validating audience quality in Phase 1.

**Structure (Option A - by concept):**
```
Campaign: [Product] - Prospecting - CBO - [Winning Audience]
-- Ad Set 1: UGC Concept                [CBO distributes budget]
   -- 3-4 UGC variations
-- Ad Set 2: Before/After Concept
   -- 3-4 Before/After variations
-- Ad Set 3: Problem/Solution Concept
   -- 3-4 Problem/Solution variations
```

**Structure (Option B - by batch):**
```
Campaign: [Product] - Prospecting - CBO - [Winning Audience]
-- Ad Set 1: Creative Batch 1 (mix of concepts)
-- Ad Set 2: Creative Batch 2 (iterations from Batch 1 winners)
-- Ad Set 3: Creative Batch 3 (double down on winners)
```

**Critical settings:**
- Use **Campaign Budget Optimization (CBO)** - let Meta shift budget to winning creative concepts
- Target only the validated winning audience
- Give each batch/concept 7-10 days minimum before judging
- When a concept wins, create more variations of that concept
- When a concept dies, replace with dramatically different concept

**Transition trigger to Phase 3:** Once you have 50+ conversions/week consistently with a proven offer and audience.

### Phase 3: Automated Scaling (Advantage+)

**Purpose:** Maximum scale with automation.

**When to use:** Proven offer, proven audience, strong tracking, 50+ conversions/week.

**Structure:**
```
Campaign: [Product] - Advantage+ Leads
-- Ad Set: Broad with audience suggestions
   -- 5-10 proven creative assets + new test variations
   -- Advantage+ Creative enabled
```

**Settings:**
- Campaign objective: Leads
- Advantage+ Audience ON (provide custom audiences and lookalikes as suggestions)
- Campaign Budget Optimization (automatic)
- Work email validation + SMS verification on lead form
- 3-5+ creative variations minimum

**See advantage-plus.md for full setup and details.**

---

## The Recommended Account Architecture

For a B2B SaaS running full-funnel Meta:

```
-- Campaign 1: Remarketing (Start Here)
   -- Ad Set: Website visitors (30/90/180 day)
   -- Ad Set: Video viewers (50%+)
   -- Ad Set: Cross-channel UTM retargeting
   -- Budget: $20-50/day (small audience)
   -- Objective: Leads or Conversions

-- Campaign 2: Prospecting - ABO (Testing)
   -- Ad Set: 1% CRM Lookalike
   -- Ad Set: Third-party data audience
   -- Ad Set: Interest + Job Titles
   -- Budget: Equal per ad set
   -- Objective: Leads

-- Campaign 3: Prospecting - CBO or Advantage+ (Scaling)
   -- Ad Set: Winning audience from testing
   -- Multiple creative concepts
   -- Budget: Main prospecting budget here
   -- Objective: Leads or Conversions

-- Campaign 4: ABM (If Applicable)
   -- Ad Set: Tier A accounts
   -- Ad Set: Tier B accounts
   -- Budget: ABO (control per tier)
   -- Objective: Awareness or Video Views

-- Campaign 5: Acceleration (If Applicable)
   -- Ad Set: Open pipeline (high-value)
   -- Ad Set: Stalled deals
   -- Budget: ABO
   -- Objective: Awareness
```

---

## The Roadmap: Build in This Order

### Month 1: Remarketing
- Lowest risk, highest ROI
- People already know you - just stay top of mind
- Cross-channel remarketing amplifies existing LinkedIn/Google investment
- Small budget required (audience is small)
- Proves Meta works for your brand before committing prospecting budget
- Creates the "they're everywhere" perception with minimal spend

### Month 2-3: Prospecting (Audience Validation to Creative Scaling)
- Phase 1: ABO audience validation (2-4 weeks)
- Phase 2: CBO creative scaling on winning audiences
- This is where the majority of budget eventually goes
- Follow the message-validation.md process to find true top ads

### Month 4+: Scaling + ABM + Acceleration
- Phase 3: Advantage+ for proven offers (if 50+ conversions/week)
- Add ABM campaigns if running LinkedIn ABM (see abm-on-meta.md)
- Add acceleration campaigns against open pipeline (if applicable)

### Month 12+: Expansion
After ~12 months of focused prospecting, your top 5% of in-market buyers will either be customers or know about you. Next stage:
- Expand outside top 5% in-market buyers
- Repeat validation process for new, colder audiences
- Story-based ads work well for prospects who aren't actively looking
- Message shifts from "solve your problem now" to "here's what companies like yours are doing"

---

## Key Campaign Settings Reference

### Optimization Events

| Event | When to Use | Min Volume Needed |
|-------|-----------|-------------------|
| **Lead** | Lead form submissions, demo requests | 50/week |
| **Landing Page Views** | Low conversion volume, need more events for learning | 50/week |
| **CompleteRegistration** | Webinar signups, trial signups | 50/week |
| **Custom: MQL** | Sending qualified lead events via CAPI | 50/week |
| **Custom: Opportunity** | Sending pipeline events via CAPI (advanced) | Lower volume OK if pipeline-focused |

**The 50-event threshold:** Meta needs 50 optimization events per ad set per week to exit learning phase. If you can't hit 50 demos/week, optimize for a higher-volume event (lead form submissions, landing page views) and retarget converters toward demos.

### Budget Formula
```
Minimum Daily Budget = (Target CPA x 50 conversions) / 7 days
```

### Naming Convention
```
[Product] - [Campaign Type] - [Budget Type] - [Audience/Detail]

Examples:
- DataSync - Prospecting - ABO - Audience Validation
- DataSync - Prospecting - CBO - 1% CRM Lookalike
- DataSync - Remarketing - CBO - Website 90d
- DataSync - ABM - ABO - Tier A Accounts
- DataSync - Acceleration - ABO - Open Pipeline
```

---

## Cross-Channel Remarketing (Advanced)

Retarget traffic from validated channels (LinkedIn, Google) on Meta at lower cost:

1. Run ads on LinkedIn - traffic lands on website with LinkedIn UTMs
2. In Meta: Audiences - Create - Custom Audience - Website - URL contains `utm_source=linkedin`
3. Now retarget your LinkedIn-validated audience on Meta at 50-70% lower CPM
4. Same works for Google traffic: `utm_source=google&utm_medium=cpc`

**Requires:** Sufficient traffic volume from those channels to build a usable audience size.

**Why it's powerful:** LinkedIn's precision targeting validates who the right people are. Meta's cheap retargeting keeps you in front of them. Result: LinkedIn-quality audience at Meta-level costs.

---

## What to Avoid

- **Mixing ABM and broad prospecting in one campaign** - completely different targeting logic, separate them
- **Running CBO during audience validation** - CBO will shift budget to cheapest audience, which may not be the best quality
- **Changing campaign settings during learning phase** - any significant edit resets the 50-conversion counter
- **More than 5-6 ad sets per campaign** - dilutes signal, slows learning
- **Optimizing for "Link Clicks" for B2B** - vanity metric; optimize for leads or conversions

---

## Related Files

- **audience-strategy.md** - Data hierarchy, CRM lookalikes, third-party sources, validation criteria
- **advantage-plus.md** - Full Advantage+ setup and when to use it
- **offer-strategy.md** - What offers to run at each funnel stage
- **creative-strategy.md** - What creative concepts to test
- **optimization-playbook.md** - Weekly cadence, decision trees, scaling protocol
- **message-validation.md** - How to score ads against revenue quality, not vanity metrics
