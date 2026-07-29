---
name: saas-lifecycle
title: SaaS lifecycle programs
description: |
  Use this skill when a subscription product's messaging needs to be designed, audited, or rebuilt
  across the whole customer journey — activation, onboarding, trial conversion, adoption, retention,
  expansion, failed-payment recovery, and win-back. Produces either a findings report ranked by
  leverage, or a staged build roadmap with the trigger, touches, and data prerequisites for each
  program. Trigger phrasings: "design our lifecycle", "why are we churning", "review our lifecycle
  emails", "trial conversion is low", "build a win-back flow", "dunning", "onboarding emails",
  "our activation rate is bad", "where do we start with lifecycle".
category: RevOps
---

Applies to any subscription product with usage data. Produces an audit ranked by leverage, or a staged roadmap with data prerequisites named.

## Audit the data layer before anything else

The most common finding is not a missing campaign. It's that the events and attributes the messaging would need are not being tracked, are tracked inconsistently, or never reach the messaging platform. Design a beautiful behavioural program on top of that and it silently sends the wrong thing to everyone.

So the first move in any engagement is: what events actually exist and are populated? Are plan, usage, and subscription attributes flowing through? Where's the gap between what the messaging needs and what the data provides? **If the pipes are broken, fixing them is the first deliverable — say so plainly, even when the ask was for a campaign.**

## The eight stages

Locate the user on this map, then ask: what's the single next value moment, and what message helps them reach it?

1. **Acquisition** — signup created → set expectations, drive first login
2. **Activation** — first login → reach the aha moment
3. **Onboarding** — account created → complete the setup steps that predict retention
4. **Adoption** — activated → build the habit, widen feature use
5. **Retention** — recurring use → reinforce value, prevent decay
6. **Expansion** — hitting limits → upgrade, seats, cross-sell
7. **Advocacy** — promoter → referral, review
8. **Resurrection** — dormant or churned → reactivate, save cancellers, recover failed payments

A minimum viable program set is: welcome/activation, onboarding, trial conversion if there's a trial, failed-payment recovery, and win-back. Add expansion and advocacy once those are working.

## Two truths that shape every stage

**Retention is the foundation.** Acquisition, expansion, and referral all leak away without it, and top-line growth hides decaying cohorts for a surprisingly long time. Read the cohort retention curve *before* prescribing anything: a curve that flattens means there's a real product-market fit to build on; a curve decaying toward zero cannot be fixed by email, and saying so is the honest deliverable.

**Behaviour beats time.** Trigger on what someone did or didn't do at their natural frequency, not on a fixed clock.

## Define activation properly

The activation metric is the earliest milestone that predicts long-term retention — the aha moment *repeated at the expected frequency*, not a setup step completed once. A validated activation metric shows activated users retaining at roughly twice the rate of non-activated ones. If yours doesn't, you've measured a setup step and every program keyed to it is aimed at the wrong target.

## What good looks like

The tell of a good operator: they ask what the core action is and how often a happy user would do it, before asking anything about email. Everything downstream — triggers, delays, what counts as dormant — falls out of that one answer.

The mediocre version is a complete-looking set of flows built on a fixed time drip, with no holdout, no exit conditions, and a churn number nobody can attribute to anything. It looks like a working lifecycle program in a screenshot.

Good output ranks gaps by leverage against *this* company's actual churn shape rather than listing every missing program, states the data prerequisite for each recommendation, and instruments measurement plus a holdout before launch — because a program you can't attribute is a program you can't defend or improve.

## Rules

- MUST audit event and attribute coverage before designing any program.
- MUST define the core action and its natural frequency first.
- MUST rank recommendations by leverage, not by completeness of the stage map.
- MUST instrument metrics and a holdout before launch.
- NEVER prescribe messaging as the fix for a retention curve decaying toward zero.
