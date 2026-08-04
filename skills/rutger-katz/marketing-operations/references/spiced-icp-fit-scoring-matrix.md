---
title: SPICED ICP Fit Scoring Matrix
description: (reference)
---

# SPICED ICP Fit Scoring Matrix

On-demand reference for the marketing-operations skill.

When a client uses the SPICED qualification framework, replace the generic Fit Score with a SPICED ICP Fit Matrix. This produces more accurate MQL scoring because it uses the same language sales uses to qualify deals.

**The ICP Fit Matrix: Selection × Urgency**

Instead of a single "fit" number, score two independent dimensions:

**Selection Fit (Is this our ICP?):**

| Criterion | Weight | Data Source | Score 0-3 |
|-----------|--------|-------------|-----------|
| Company size (ARR/employees in ICP range) | 25% | Enrichment (Apollo, ZoomInfo) | 0=outside, 1=adjacent, 2=close, 3=bullseye |
| Industry/vertical match | 20% | Enrichment + self-reported | 0=wrong, 1=tangential, 2=adjacent, 3=core |
| Technology stack signals | 20% | Enrichment (technographic) | 0=no signals, 1=some, 2=strong, 3=exact match |
| Growth stage / funding | 15% | Enrichment + news | 0=wrong stage, 1=early, 2=approaching, 3=ideal |
| Geography (in-market) | 10% | Enrichment | 0=excluded, 1=secondary, 2=primary, 3=core |
| Role/title of contact | 10% | Form data + enrichment | 0=wrong dept, 1=adjacent, 2=right dept, 3=decision-maker |

**Selection Fit Score** = Weighted average × 33.3 (scales to 0-100)

**Urgency Fit (Are they ready now?):**

| Signal | Weight | Data Source | Score 0-3 |
|--------|--------|-------------|-----------|
| Engagement recency (last 7 days) | 25% | MAP behavioral data | 0=none, 1=>30d, 2=7-30d, 3=<7d |
| Content depth (pricing, case studies, demo) | 25% | MAP page tracking | 0=blog only, 1=mid-funnel, 2=bottom-funnel, 3=pricing/demo |
| Critical event signals | 20% | Form data, intent, news | 0=none, 1=implied, 2=mentioned, 3=confirmed |
| Repeat visits / multi-session | 15% | MAP tracking | 0=1 visit, 1=2-3, 2=4-6, 3=7+ |
| Direct request (demo, call, trial) | 15% | Form submission type | 0=content only, 1=newsletter, 2=webinar, 3=demo/trial |

**Urgency Fit Score** = Weighted average × 33.3 (scales to 0-100)

**Qualification Tier Assignment:**

| Tier | Selection Fit | Urgency Fit | MQL Action |
|------|-------------|-------------|------------|
| **T1 — Perfect Fit** | ≥70 | ≥60 | Immediate routing to AE. Speed-to-lead <1 hour. |
| **T2 — Good Fit** | ≥50 | ≥40 | Route to SDR for qualification call. Standard SLA. |
| **T3 — Opportunistic** | ≥30 | ≥30 | Add to nurture sequence. Re-score monthly. |
| **Below threshold** | <30 | Any | Do not route. Passive nurture only. |

**Why this is better than generic scoring:** Selection Fit uses ICP-specific criteria, not generic firmographics. Urgency Fit captures buying intent, not just engagement volume. The tier system (T1/T2/T3) aligns with how sales qualifies deals using SPICED. SDRs and AEs speak the same qualification language as marketing.

**Implementation note:** The scoring weights above are starting points. Calibrate quarterly by running a correlation analysis: which scoring dimensions best predict Closed-Won? Increase weight on predictive dimensions, decrease on noise.

See the icp-builder skill for the full ICP Fit Matrix framework and cluster-specific criteria.
