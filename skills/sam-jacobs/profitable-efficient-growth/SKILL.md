---
name: profitable-efficient-growth
title: Profitable efficient growth
description: |
  Use this skill when a founder, revenue leader, CFO, or RevOps team is heading into annual planning, a board meeting, or a fundraise; is debating whether to pour more fuel on acquisition or fix the model first; needs a reality check on a 'growth at any cost' reflex; or asks anything about unit economics, CAC payback, NRR, burn multiple, Rule of 40, magic number, growth efficiency, or GTM budget allocation — even if they never say the word 'scorecard'. Builds a board-ready Profitable Efficient Growth (PEG) scorecard: computes the unit-economics picture from the company's own numbers, grades each metric against Sam Jacobs' PEG benchmarks, diagnoses whether the engine is scale-ready or leaking into a cash trap, and recommends how to allocate the next dollar of GTM spend using the 60/30/10 tranche strategy (proven / probable / experimental).
category: RevOps
---

**Source framework:** Sam Jacobs' Profitable Efficient Growth (PEG) — the rebuttal to "growth at
any cost." Built on the Unit Economics Compass (per-unit profitability as the decision filter for
whether to scale or optimize), PEG's benchmark thresholds (LTV:CAC at or above 3:1, CAC payback
under 12 months, NRR above 110%, Rule of 40 at or above 40%, magic number above 0.75, burn multiple
under 1.5x), a retention-over-acquisition / customer-led growth thesis, and the Tranche Strategy for
GTM spend allocation (60% proven / 30% probable / 10% experimental).

## Purpose & When to Use

Most growth plans start from the wrong question — "how much can we grow?" — when the question
that actually protects the company is "can we grow *this* efficiently?" In the "growth at any
cost" era, teams scaled top-line revenue while quietly digging a financial hole: acquisition
spend outran the value each customer returned, payback stretched past the point where cash ran
out first, and churn ate the gains. Sam Jacobs' **Profitable Efficient Growth (PEG)** is the
correction. Efficiency isn't the reward you earn after growth — it's the *prerequisite* for it.

The core idea is the **Unit Economics Compass**: per-unit profitability (revenue minus the
variable cost to acquire and serve a customer) is the only reliable way to tell whether you're
scaling a healthy business or scaling into a cash crisis. The same $1M of new spend is brilliant
in one unit-economics regime and fatal in another. PEG turns that compass into a decision filter:
if the economics are strong, pour fuel on; if they're soft, fix the model before you scale it.

This skill builds the scorecard. It takes a company's real numbers, computes the PEG metrics,
grades each against Sam's benchmarks, diagnoses whether the engine is scale-ready or leaking,
and translates the verdict into a spend-allocation recommendation using the tranche strategy.

Run this skill when any of these are true:

- The team is heading into **annual planning, a board meeting, or a fundraise** and needs a
  defensible read on growth efficiency.
- Someone is pushing to **scale acquisition spend** and you want to know if the model can take it.
- Growth looks good on the top line but you suspect **"growth at any cost"** is hiding a cash trap.
- Retention / churn is drifting and you need to see whether the problem is **acquisition or the
  base**.
- A revenue leader asks the plain question: **"are our unit economics healthy enough to scale?"**

The one discipline this skill must never break is **laundering a guess into a grade**. Invented
inputs, industry averages standing in for the company's own numbers, or a user's gut-feel estimate
treated as measured fact all produce the same false confidence PEG exists to prevent. But that is
not a reason to refuse imperfect data — it's a reason to stay honest about what each number *is*.
When the data is thin, a principled partial scorecard — one that computes what the numbers honestly
support, flags estimates as estimates, and names the gaps — beats both a fabricated complete one and
a flat refusal to help. See Inputs and Step 1 for how to handle estimates, gaps, and partial runs.

## Procedure

### Inputs you need

Collect these before scoring. Where a number is missing, do **not** fabricate or substitute an
industry average — mark it `[CONFIRM]` and make retrieving the real figure part of the work.
Prefer the company's own trailing figures (last full quarter or trailing twelve months) over
snapshots, and be explicit about the period used.

**Look for the numbers before you ask a human for them.** Many of these values already exist
somewhere in reach — stated earlier in this conversation, sitting in an uploaded board deck, model,
or financial export, or retrievable from a connected system (CRM for customer counts and ARR,
finance/billing tools for spend, margin, and cash). Check those first, and when you find a figure,
*confirm* it ("I'm seeing S&M spend of $2.1M last quarter — is that the number you'd use?") rather
than re-requesting something the user already gave you. Only ask outright for what you genuinely
can't find.

**When you do ask, ask conversationally — don't drop the full twelve-input wall on them.** A founder
faced with a wall of finance terms disengages or guesses. Ask a few questions at a time, starting
with the inputs that unlock the most metrics (S&M spend, net-new ARR, cash delta, and customer count
cover burn multiple, magic number, and blended CAC on their own), then follow the thread into
retention and margin. A data-rich CFO who pastes everything at once should skip straight to
compiling; a founder answering live should feel like a short guided conversation, not an audit form.

**Distinguish measured figures from estimates as you collect.** Some numbers a founder knows cold
(spend, cash, customer count); others they'll answer from intuition. When a number arrives round,
hesitant, or suspiciously convenient ("churn's probably around 2%"), gently probe provenance —
"is that measured, or a gut feel?" — and tag anything estimated so it doesn't get graded as fact
(Step 1 covers how estimates flow through the math). Use social judgment about how hard to push:
interrogating every input is as corrosive to the conversation as accepting everything is to the
scorecard. Probe the numbers that move the verdict, and let the obvious ones pass.

- **Revenue & growth:** current ARR (or MRR), and year-over-year ARR growth rate.
- **Acquisition cost:** total S&M spend for the period, and the number of new customers it produced
  (for blended CAC). Segment by channel where possible — the tranche recommendation depends on it.
- **Customer value:** average revenue per customer, gross margin %, and average customer lifetime
  or gross churn rate (to derive LTV).
- **Retention:** gross revenue retention and **net revenue retention (NRR)** — expansion minus
  churn/contraction across the existing base.
- **Efficiency inputs:** operating margin or FCF margin (for Rule of 40), net new ARR and cash
  burned for the period (for burn multiple), and new ARR vs. prior-period S&M (for the magic number).
- **Spend context:** how GTM budget is currently split across channels, and which channels are
  proven vs. still being tested — needed for the 60/30/10 allocation.

**Different metrics have different data appetites — a partial scorecard is often the right answer,
not a failure.** Burn multiple and magic number need only figures nearly every founder knows cold
(cash delta, net-new ARR, S&M spend), so they're almost always computable. LTV:CAC and CAC payback
depend on gross margin and churn — numbers early teams frequently don't track yet — and Rule of 40
needs a growth rate and a margin. When the harder inputs are missing, don't refuse and don't guess:
compute the metrics the data honestly supports, state plainly which ones you couldn't run and *why
each matters* (e.g. "no payback without gross margin — this is the single most important efficiency
read, so it's worth pinning down"), and turn the gaps into a prioritized get-the-real-numbers list
ordered by how many metrics each figure unlocks. A partial scorecard that's honest about its own
edges is a genuinely useful deliverable. Reserve stopping for when the data is too thin to support
even one grounded metric — that's a judgment call about substance, not a fixed input threshold.

### Step 1 — Compute the metrics

Calculate each PEG metric from the inputs, keeping the arithmetic visible and auditable. Use the
company's own numbers, not benchmarks, for the inputs.

- **LTV:CAC ratio** — LTV = (avg revenue per customer × gross margin %) / churn rate (or × avg
  lifetime); CAC = S&M spend / new customers. Report the ratio.
- **CAC payback (months)** — CAC / (avg monthly revenue per customer × gross margin %). How long
  until a customer repays their acquisition cost, on a gross-margin basis.
- **Net Revenue Retention (NRR)** — starting ARR + expansion − contraction − churn, over starting
  ARR, for the existing cohort.
- **Rule of 40** — revenue growth % + operating (or FCF) margin %. YoY growth is the standard input,
  but early-stage companies often don't have a clean trailing-year figure. Pick a growth-measurement
  approach thoughtfully (annualized recent-quarter growth, trailing available months, etc.), state
  which you used, and when reasonable methods disagree materially, show the range and whether the
  grade holds across the choice rather than silently picking the flattering one.
- **Magic number** — net new ARR in the period / prior-period S&M spend. A proxy for sales efficiency.
- **Burn multiple** — net cash burned / net new ARR. Dollars burned per dollar of new ARR.

Round conservatively rather than generously. If an input is `[CONFIRM]`, carry that flag through to
the metric so no soft number is presented as fact.

**Let estimates flow through as ranges, not false-precision points.** When a metric leans on an
estimated input, resist collapsing it to a single confident number — that's exactly how a founder's
"probably 2%" churn becomes a graded fact. Instead, run the math under a conservative-low and a
plausible-high version of the estimate and show the metric as a range (e.g. "LTV:CAC ≈ 2.4–3.6x,
driven by an *estimated* churn rate"), naming which input is doing the swinging. Let the grade
reflect that uncertainty: if the range straddles a benchmark boundary, say so rather than picking a
side, and note that pinning the underlying number down is what would resolve the grade. A metric
built entirely on measured inputs earns a clean point value; one resting on a guess should visibly
wear that guess.

### Step 2 — Grade each metric against the PEG benchmarks

Score each metric against Sam's thresholds and label it Healthy / Watch / Warning. These are the
"scale-ready" bars — below them, scaling spend tends to drain cash faster than customers repay it.

| Metric | Healthy | Watch | Warning | Why it matters |
| :--- | :--- | :--- | :--- | :--- |
| **LTV:CAC** | ≥ 3:1 | 2–3:1 | Under 2:1 | Below 3:1, acquisition spend is outpacing the value each customer returns. |
| **CAC payback** | Under 12 mo | 12–18 mo | Over 18 mo | Past ~12 months, scaling fast drains cash before customers turn profitable. |
| **NRR** | Over 110% | 100–110% | Under 100% | Under 100%, the base leaks faster than it expands — you're filling a bucket with a hole. |
| **Rule of 40** | ≥ 40% | 30–40% | Under 30% | The headline efficiency metric; 40% is the floor investors expect at growth stage. |
| **Magic number** | Over 0.75 | 0.5–0.75 | Under 0.5 | Below 0.75, the S&M engine needs optimizing before you invest more into it. |
| **Burn multiple** | Under 1.5x | 1.5–2x | Over 2x | Higher means you're burning more cash per dollar of new ARR — the opposite of efficient. |

Grade honestly. A single Warning on payback or NRR can outweigh a strong growth rate — that's the
whole point of PEG over "growth at any cost."

**Keep the grades honest, but don't stop at grading them one by one.** These are growth-stage bars.
An early-stage or pre-PMF company can fail Rule of 40 *structurally* — it's investing ahead of
revenue by design — while running a genuinely healthy engine. A wall of red Warnings with no
interpretation is technically true and nearly useless. Never soften a Warning to be kind, but do
explain what each grade *means for a company at this stage*, and separate **structural** Warnings
(expected given where the company is — flag them as "watch as you scale," not "fix now") from
**actionable** ones (a real leak the company can and should address today).

**Read the pattern across metrics, not just the individual grades.** The same "mostly red" scorecard
can carry opposite diagnoses. A strong magic number paired with a margin-driven LTV collapse says
*the sales engine works but the serving economics are broken* — scaling acquisition pours more
customers into a leaky unit. The reverse — healthy margins and retention but a weak magic number —
says *the economics are sound but the go-to-market engine is inefficient* — the fix is in the motion,
not the model. Name which story the pattern tells; that interpretation is what turns a grid of colors
into a decision.

### Step 3 — Read the compass: scale, or optimize?

Use the graded scorecard as a decision filter, the way the Unit Economics Compass intends:

- **Green light to scale** — LTV:CAC, payback, and NRR are all Healthy. The model repays itself and
  the base expands. More spend compounds; this is when to pour fuel on.
- **Optimize first** — one or more of payback / LTV:CAC / NRR is in Warning. Scaling here amplifies
  a leak. The recommendation is to fix the economics (retention, pricing, ICP tightening, channel
  efficiency) *before* adding acquisition spend.
- **Cash-trap risk** — strong top-line growth paired with a Warning burn multiple or sub-100% NRR.
  Flag this explicitly: the company is growing revenue while building a financial hole. Growth is
  masking the problem, not solving it.

Name the single highest-priority fix. Per Sam's retention-over-acquisition / customer-led-growth
thesis, if NRR is soft, retention and expansion usually outrank new-logo acquisition as the fix —
brute-force acquisition is no longer the reliable growth driver it once was.

### Step 4 — Allocate the next dollar with the tranche strategy

Translate the verdict into a spend recommendation using Sam's **60/30/10 tranche strategy**, so the
plan balances stability with innovation instead of making an all-in bet on an unproven channel:

- **60% — Proven.** Channels with predictable, established ROI and clear unit economics. The core
  engine you already trust.
- **30% — Probable.** "Next-level" channels showing strong signal but not yet fully proven at scale;
  fund them to graduate into proven.
- **10% — Experimental.** High-risk / high-reward bets (new tactics, AI-driven workflows) with
  unproven ROI. Small enough to survive being wrong, large enough to learn.

Adapt the split to the compass reading: if the model is in "optimize first," bias the proven/probable
tranches toward retention and expansion motions rather than new-logo acquisition, and keep the
experimental 10% honest — it's for learning, not for hiding an unaccountable bet.

### What it produces

A one-page Profitable Efficient Growth scorecard containing:

- **The metric table** — LTV:CAC, CAC payback, NRR, Rule of 40, magic number, burn multiple, each
  with the computed value (a clean point where inputs are measured, a **range** where an estimate is
  doing the work), its Healthy/Watch/Warning grade, and the visible math behind it. Metrics that
  couldn't be computed are shown as such, not omitted or faked.
- **The compass verdict** — scale / optimize-first / cash-trap-risk, with the reasoning and the
  cross-metric pattern it rests on, framed for the company's stage.
- **The single highest-priority fix** — the one lever that most improves efficiency, retention-first
  where NRR is soft.
- **A tranche allocation** — the recommended 60/30/10 split for the next GTM dollar, adapted to the
  verdict.
- **`[CONFIRM]` items and the get-the-real-numbers list** — every missing or estimated input,
  surfaced as a task rather than a guess, prioritized by how many metrics each figure would unlock.

## What Good Looks Like

A great PEG scorecard is one a founder can hand to their board and a skeptical CFO respects. Every
number traces to the company's own data, the grades are honest even when they're uncomfortable, and
the recommendation is a clear "scale" or "fix this first" — not a vague "keep growing." It reframes
the conversation from "how fast can we grow?" to "can we grow this efficiently?" and gives a concrete
answer.

Signs it's working:

- A strong growth rate no longer earns a pass on its own — payback and NRR get equal weight.
- The team can point to the *one* metric that decides whether to scale or optimize, and act on it.
- A "let's just spend more" impulse gets checked against the compass before the budget moves.
- Retention and expansion get funded as growth drivers, not treated as a CS afterthought.
- The experimental 10% is a deliberate learning bet, not a place unaccountable spend hides.
- A data-rich CFO still gets the crisp one-shot compile; a data-poor founder gets a short guided
  conversation and an honest partial scorecard — neither experience launders a guess into a grade.
- Estimated inputs show up as ranges the reader can see, and the grade openly reflects the
  uncertainty instead of hiding it behind false precision.
- A pre-PMF company reads its Rule of 40 Warning as "structural, watch as you scale," not as a
  failing grade — while its genuinely actionable leaks still get called out plainly.
- Numbers already in the deck, the thread, or a connected system get confirmed, not re-requested.

Signs it's off track:

- Metrics are computed from industry averages or round guesses instead of the company's real numbers.
- A user's gut-feel estimate gets graded as a measured fact, with no range and no provenance check.
- Growth rate is used to wave away a Warning on payback, burn, or NRR.
- The scorecard produces numbers but no verdict — no clear scale/optimize call.
- A wall of red Warnings is handed over with no stage context and no cross-metric story.
- The agent stops cold on missing data when a principled partial scorecard was available, or asks
  for numbers it could have found in the conversation, an upload, or a connected system.
- The tranche split is applied mechanically without adapting to what the compass says.
- "Cash-trap risk" cases get softened into optimism instead of being named plainly.
