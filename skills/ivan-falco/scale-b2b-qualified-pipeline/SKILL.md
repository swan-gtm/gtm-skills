---
name: "scale-b2b-qualified-pipeline"
title: Scale qualified pipeline on Meta
description: "Use this skill when the goal is SQLs and qualified pipeline from Meta, not lead volume — the 6-step spine: map market, build audiences, feed CAPI, creative loop, segments, SQL reporting."
category: Ads
---

# Scale B2B Qualified Pipeline on Meta

A step-by-step playbook for turning Meta Ads spend into **qualified pipeline (SQLs)** for B2B, not cheap lead volume. This is the end-to-end system written at full depth.

> This playbook is the spine. For the deeper mechanics of any single piece, link out (one level) to the reference files in this folder: `audience-strategy.md`, `meta-capi-and-events.md`, `campaign-structure.md`, `creative-strategy.md`, `creative-cadence-operating-system.md`, `optimization-playbook.md`, `meta-ads-operating-system.md`.

---

## The core idea (read first)

Most B2B teams run a Meta campaign, get a pile of low-quality leads, decide "Meta doesn't work for B2B," and move their budget somewhere else. In almost every case the setup was the problem, not the campaign.

**Meta is extremely good at finding exactly what you ask it to find.** If you optimise for "Lead" and give it nothing else to go on, it does its job perfectly and brings you the cheapest form-fills it can. They are real leads, they just never turn into pipeline.

The whole game is to change what you are asking for. When you (1) give Meta the right data so it understands your actual ICP, and (2) feed back which leads become qualified pipeline, Meta learns to go and find more of those. It is the same optimisation engine, now working toward qualified pipeline instead of cheap volume.

Everything below is how you do that.

---

## Step 1 - Map the market & build the audience targeting

**Goal: give Meta a high-quality, matchable audience built from your real target market.**

- Map your **TAM**. Tier every company **Tier 1 -> Tier 4** by fit. Decide where you want to go.
- Pull the **contacts** at those companies. That is your **Tier 1-4 contact list** - this list is the audience targeting.
- Enrich the list. Raw B2B / work-email lists match badly on Meta. Enrich for **personal email + mobile numbers** to lift the match rate, or the custom audience lands too small to run. (Mobile advertiser IDs / MAIDs are a minor assist only - iOS App Tracking Transparency degraded them; personal email + mobile number do the heavy lifting.)
  - Enrichment data: **Contact Level**.
  - Enrich + auto-sync audiences into Meta: **Clay / Freckle**.
- Push the enriched list to Meta as a **custom audience**.

**Why:** Meta builds audiences from people (not company names), so you need the real contacts. Tiering tells you where budget goes first. Match rate decides how big and usable the audience is - work emails barely match, personal email + mobile number are what Meta actually matches on.

> Deeper detail: `audience-strategy.md`.

---

## Step 2 - Structure the audiences (one campaign per audience)

**Goal: give Meta room to scale off your data, cleanly, without losing control of who it targets.**

Push three audiences to Meta:
1. Your full **Tier 1-4 contact list** (all your TAM).
2. A **lookalike** of that list.
3. A **lookalike of your closed-won contacts** (the decision-makers who actually signed).

Structure:
- **One campaign per audience** (or per segment - see Step 5).
- Inside each campaign, run **multiple ad sets - one per creative angle / approach / personalisation**.
- Run **CBO** and set a **30% minimum spend per ad set while validating new angles**, so CBO does not dump everything into one angle and starve the others before they are tested. (Use this sparingly and only during validation. The Meta operating system - `meta-ads-operating-system.md` - prefers a two-campaign testing/scaling split over permanent per-ad-set floors; both are valid, pick one deliberately per account.)

**Tight targeting, controlled expansion.** Keep the targeting tight and do not turn on Meta's audience expansion. The **lookalike is the controlled way you open the audience** - it gives Meta room to find more people like your market without letting it wander off your ICP. That balance (tight seed + lookalike) is the sweet spot.

**Exclusions (hygiene):**
- Exclude existing customers and open pipeline from cold prospecting audiences.
- Exclude Audience Network placements - they are low quality for B2B.

**Why:** the contact list reaches your exact market; the two lookalikes let Meta find more people like your TAM and like your best buyers, with room to scale. One campaign keeps that audience's budget and learning together.

> Deeper detail: `campaign-structure.md`.

---

## Step 3 - Optimise by funnel event (feed the Lead signal)

**Goal: teach Meta what a QUALIFIED lead looks like, so it optimises for pipeline, not form-fills.**

This uses Meta's **Conversion Leads** feature (Conversions API CRM integration), not just sending arbitrary events to a plain Leads objective.

- Set your funnel up as **conversion events / funnel stages in Meta**: Lead, MQL, SQL. Mark the qualified stages (MQL, SQL) as positive.
- Send the qualified stages back from your CRM (HubSpot) to Meta **via CAPI**, on a **daily upload cadence**.
- A **funnel event** tells Meta how your funnel works. Feeding MQL/SQL back tells Meta which form-fills became real pipeline, so it optimises toward buyers, not cheap leads.
- **Optimise for the highest-quality event you get ~10+/wk on (per ad set).** As volume grows, **move up the funnel** (Lead -> MQL -> SQL) to a higher-quality conversion.
  - **~10/wk per ad set** = the practical floor to start optimising on an event reliably (rule of thumb from experience).
  - **~50/wk per ad set** = Meta's documented threshold to fully exit the learning phase. Only the optimised event counts toward it.
- Even while you optimise on **Lead** (because SQL volume is still low), because MQL + SQL are configured as funnel stages, Meta favours the leads that progress down-funnel. (Meta may also silently shift which stage it optimises toward if it finds better performance.)

**Non-negotiable setup requirements for this to actually work:**
- **Capture and store the Meta click ID (fbclid) / Lead ID at lead creation, and pass it through every CRM stage change.** Meta's click attribution window is ~7 days, but MQLs/SQLs land weeks later. Without the stored click/Lead ID, Meta cannot attribute the downstream event back to the ad and the entire "feed the funnel back" premise silently breaks.
- **Keep Event Match Quality (EMQ) high (target 6+/10)** on the CAPI events - send hashed email, phone, and external_id. Low EMQ silently degrades Meta's ability to use the MQL/SQL signal.
- **Conversion Leads gates:** roughly **200 leads/month minimum**, and the optimised stage must convert at **1%-40%** (if your SQL rate is below 1%, it is out of range for direct optimisation - which is exactly why you optimise on Lead and feed SQL back).

**Why:** Meta optimises for exactly what you ask it for. Give it the right data and a clear definition of a qualified lead / qualified pipeline, and it will go and find that.

> Deeper detail: `meta-capi-and-events.md` (CAPI, event hierarchy, CRM -> CAPI, deduplication, Event Match Quality).

---

## Step 4 - Creative process (one process feeds video AND static)

**Goal: creative that speaks the buyer's language, produced fast enough to keep testing.**

- **Research** where buyers talk: sales calls, Reddit, forums (research sources/tools include X, Reddit, HubSpot, Medium). Pull their real **pains, jargon, and vocabulary**.
- Map **angles + hooks**. The same research feeds **both video and static** - it is one creative process, not two.
  - Video: testimonials, quick product demos, founder videos, real UGC.
  - Static: angle/hook creatives, product UI, data/proof, personalised.
- **Cadence is budget-dependent.** At a **~$30k/month budget, ~10 new creatives every 2 weeks** is the optimal baseline. Scale the volume up or down with the budget. Use **AI creative workflows** to sustain that output.
- Split the account into a **testing campaign** (always fed the new creatives) and a **scaling campaign** (proven winners only).

**Why:** buyers act on their own pains and words, not your feature list. Creative fatigues, so a constant test feed keeps surfacing winners, and keeping test spend separate from scale protects proven spend.

> Deeper detail: `creative-strategy.md`, `creative-cadence-operating-system.md`.

---

## Step 5 - Test & personalise by segment

**Goal: find segments where personalised messaging beats broad all-TAM messaging.**

- From your all-TAM contact list, **filter down to a specific segment** (per strategy) and export those contacts.
- Upload each segment as its **own audience (list + lookalike, same structure as Step 2)**.
- Build **ads + a landing page personalised to that segment** - written in its own reality and jargon.
- Do not only run all-TAM. **Test specific segments** to see if they beat the broad audience.
- A/B test the landing pages: split the ad set's traffic **50/50** between two pages and keep the winner. Run this across all your TAM.

**Why (segment example):** the CFO of a private-equity-owned company has different jargon and a different reality than one at a non-PE company. Speak their language and show you understand it, and the campaign will often perform far better than a non-personalised one. Testing tells you which segments to scale, and A/B testing shows what resonates at the ad level AND the landing-page level.

---

## Step 6 - Report on real SQLs (always up to date)

**Goal: see what is actually driving qualified pipeline, so you can steer Meta manually.**

- Connect **Meta <-> HubSpot (any CRM - HubSpot, Attio, etc.)** via **MCP / APIs** into a **live report** that tracks **MQL + SQL trends against spend** and shows **which ads drive SQLs**. (The `meta-reporting` skill builds this - performance analysis plus a branded dashboard.)

**Why:** while Meta is still optimising per Lead, it pushes budget toward whatever gets the most leads, not the most SQLs. This report shows which ads actually drive SQLs, so you can manually shift Meta's budget toward real pipeline. Read the trend over time, not a single week.

---

## The payoff

Set up this way, Meta produces **qualified pipeline and efficient cost per qualified deal**, not a pile of cheap form-fills that never convert. The optimisation engine is now pointed at the outcome that matters: revenue, not lead count.
