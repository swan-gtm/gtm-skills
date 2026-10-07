---
name: ambassador-finder
title: Ambassador finder
description: |
  Use this skill whenever a user wants to find, source, or shortlist potential brand
  ambassadors, industry advocates, or independent influencers for a company. Trigger on
  phrases like "find ambassadors," "who could be a brand ambassador," "independent experts
  in [field]," "find advocates for us," or any request to identify credible outside voices
  in a given industry who could represent, endorse, or amplify a company. Also trigger when
  a user names an industry and asks for people who fit a specific credibility bar
  (former director-level, independent, minimum following). Do not use for finding customers,
  leads, or prospects - this skill is for finding third-party voices to represent a brand,
  not people to sell to.
category: Influencers
tags: [Marketing]
---

Independent, credible outside voices - people who could represent, endorse, or amplify a company in its field. This skill finds and shortlists them; it never treats them as a sales target.

Produces a ranked, evidence-backed shortlist: one row per candidate, each screening criterion marked confirmed / likely / unverified, a one-line rationale, and the manual checks still outstanding.

## Core principle

A strong candidate has **field credibility, independence, and reach - in that order.** Reach without credibility is an influencer, not an ambassador. Credibility without reach is a fine advisor who won't move anything in public. Screen for all three, but never let reach outrank credibility on the list.

## Step 1 - Clarify the field and the angle

Pin down, from the user or the context:

- The **specific sub-field**, not the category: "B2B demand generation," not "marketing". 
- **Public representative or advisor?** A public ambassador (events, co-marketing, tagging) leans harder on reach; an advisory ambassador leans almost entirely on credibility. This changes the ranking.
- **Explicit exclusions:** direct competitors, partners already in the network, anyone the user has ruled out.

## Step 2 - Source candidates

Search in layers, strongest credibility signal first:

- Field plus independence markers: "fractional," "independent consultant," "advisor," "former Director / VP / Head of [function]" at named companies in the space.
- Authors of well-regarded articles, conference talks, podcast appearances, or widely shared posts in the field - visible thought leadership pre-filters for both credibility and reach.
- Alumni patterns: "former [senior role] at [respected company in the field]" plus "consultant" or "advisor." Founder of an exited company or Ex-employees of a recognized market leader are the highest-yield seam - the leader's reputation transfers to them.
- Follower counts and current employment usually can't be read from search alone. Capture apparent seniority and field fit now; mark reach and current role for manual verification on the platform.

The full bar - the five criteria, platform-by-platform reach floors, independence disqualifiers, red flags, and the evidence bar for each label - lives in `references/screening-rubric.md`. Read it before screening.

## Step 3 - Screen each candidate

One row per candidate, one column per criterion: field experience, independence, seniority signal, reach, publishes content. Mark each **confirmed** (direct evidence in what you found), **likely** (strong circumstantial signal), or **unverified** (no evidence either way). Never present a criterion as met without evidence; if reach can't be verified, write that - don't guess a number.

## Step 4 - Shortlist and prioritize

Rank by confirmed credibility and independence first, then reach. "Publishes content" is a tiebreaker that lifts a borderline candidate, never a substitute for the top two. Tier the list into approach now / nurture / pass using the thresholds in the rubric.

## Output format

Default to a structured table:

| Name | Field fit | Independence | Seniority signal | Reach (platform, est.) | Publishes content | Notes / to verify |

Follow it with: who ranks highest and why, and what still needs manual confirmation (almost always current employment and follower counts, which change and are not reliably searchable). Worked examples of this reasoning are in `references/worked-examples.md`.

## What good looks like

- **The tell:** read the size and type of the companies in the work history *before* the follower count. A large audience built only on tiny-company or solo-consultancy experience does not transfer credibility to a buyer audience - that candidate reads as a peer, not an authority, and converts poorly both to recruit and to deploy.
- **The common mistake:** ranking by follower count. It surfaces influencers and people who are merely visible, and buries the quieter ex-operator from a market leader who carries far more weight with the target audience.
- **A good shortlist:** most names are worth a real approach, every "confirmed" has evidence attached, and the top few are people the user is a little surprised and pleased to see. A candidate who works out posts about the space unprompted, references the company without being asked, and shows up - an event, an intro, a quote - within the first few months.

## Rules

- MUST rank credibility and independence above reach, always.
- MUST attach evidence to every "confirmed"; mark anything unproven as "likely" or "unverified."
- NEVER invent or estimate a follower count to fill the table - say it needs a manual check.
- NEVER put a current full-time employee of a direct competitor on the shortlist.
- NEVER include people the user named as excluded, or the company's own customers and prospects - this is not a lead list.
