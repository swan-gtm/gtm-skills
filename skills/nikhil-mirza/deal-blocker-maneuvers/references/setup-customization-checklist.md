---
title: Setup and customization checklist
description: (reference) Placeholders to fill, stage mapping, calibration and observation-mode rollout, write-back rules, and the enablement failures that matter.
---

# Setup and customization checklist

What to configure before running this on live deals, and how to roll it out without losing the reps in week one.

## 1. Fill the placeholders

| Placeholder | What to put there | Default if unsure |
|---|---|---|
| `{{TERMINOLOGY_MAP}}` | Your org's labels for the eight dimensions, where they differ from textbook terms | Textbook terms |
| `{{STAGE_NAMES}}` | Your pipeline stages mapped onto the five bands | See mapping below |
| `{{CONTEXT_LAYER}}` | Where primary evidence lives — call recordings and transcripts, email threads, meeting records, shared docs | Whatever is reliably captured |
| `{{COMPLEX_DEAL_FLOOR}}` | Size, cycle length, or segment below which this does not run | Closes in under 30 days, or has one stakeholder |
| `{{FORECAST_OWNER}}` | Who is told, same day, when a deal escalates — more than 1.5 below expectation, under the hard floor, an unknown cluster, or a breached band gate | The rep's direct manager |
| `{{REVIEW_CADENCE}}` | When it runs | After every meaningful interaction |

### The terminology map

Many orgs rename dimensions to match how they sell. Whatever you choose, declare it once and enforce it everywhere — mixed vocabulary across a pipeline makes deals uncomparable, which is most of the value of scoring them.

Common renames worth considering: *economic buyer* → executive sponsor, when the approver is a sponsor rather than a budget holder. *Implicated pain* → initiative, when purchases are driven by funded programs rather than problems. *Paper process* → partners, when third parties matter more than legal review. Each of these changes what reps look for, which is the point of renaming.

### Mapping your stages

Five bands, however many stages you run:

| Band | Maps to any stage where… |
|---|---|
| Discovery / qualification | You are establishing whether a deal exists |
| Validation | The buyer has confirmed intent; you are proving fit |
| Proposal / business case | A formal case, quote, or proposal is with the buyer |
| Negotiation | Commercial terms are being worked |
| Commit / close | Signature and paperwork |

More than five stages: map several to one band. Fewer: leave bands unused rather than compressing them — an unused band is harmless, a compressed one moves the floor to the wrong place.

## 2. Calibrate the bands before trusting them

Do not adopt the default numbers on faith. The full procedure — building a per-stage dataset from closed deals, setting expectation and floor from the distribution of winners, and checking the floor against losses — is in the scoring reference. Note that the binding constraint is **winners at the stage being calibrated**, not total deals: a set large enough overall can still leave too few late-stage winners to support a percentile, and those bands stay provisional until it fills in. Budget half a day.

Skipping calibration is survivable for coaching output but not for forecast decisions. Do not let an uncalibrated score pull a deal from the forecast in the first quarter of use.

## 3. Run in observation mode first

For the first two to four weeks, run everything except the consequences:

- Score deals, build maneuvers, publish artifacts.
- **Do not** write to the deal record.
- **Do not** move anything in or out of the forecast on the strength of a score.
- Include the exact values that *would* have been written, so reps can see what the framework wanted to do.

Ask two questions in review: where did the score disagree with the rep's read, and who was right? Every disagreement is calibration data, and the ones where the rep was right are the more valuable half.

## 4. Check the context layer honestly

The framework is only as good as the evidence it reads. Before rollout, confirm:

- Calls are recorded and transcribed with enough coverage that a typical deal has real material — not one call in six.
- Email with buyers is captured somewhere the analysis can reach.
- Meeting records exist for stakeholder interactions that happen outside calls.

**If coverage is thin, fix that before rolling this out.** A framework starved of primary evidence will be fed the rep's summary instead, which is the exact failure this skill is built to prevent: it converts a rep's optimism into a number that looks like analysis. Thin coverage is not a reason to lower the evidence standard; it is a reason to delay.

## 5. Write-back rules

If scores or next steps sync to the deal record:

- Field by field, with explicit human approval each time. Never a bulk write.
- Never write on a schedule or from an automated run without a human in the loop.
- Preserve the prior value and the delta marker, so a downgrade is auditable.
- Where the record has a length limit on a next-step or summary field, write to it rather than truncating mid-sentence — a cut-off instruction is worse than a short one.

## 6. Enablement — where this actually fails

The framework does not fail on logic. It fails when reps treat it as a form.

- **Train on the evidence rule first, not the scoring.** The single behavior that determines whether this works is a rep declining to score a dimension they cannot evidence. Everything else is secondary.
- **Make 0 safe.** If unknowns are treated as a rep failing to do their job, unknowns will disappear from the data and the framework becomes decorative within a month. Unknowns are the product working.
- **Review the maneuver, not the score, in one-to-ones.** "What did you run and what happened" builds the habit. "Why is this a +3" builds score inflation.
- **Celebrate an abort.** The first time a rep stops a play at its stated failure condition instead of trying once more, say so publicly. It is the hardest behavior to establish and the clearest sign the framework is being used rather than filled in.

## 7. Recalibrate when the motion changes

Re-run the calibration when you enter a new segment, change price point materially, or see cycle length shift by more than about a third. Bands built on a six-month cycle mislead on a two-month one — the same score means something different when there was half the time to earn it.
