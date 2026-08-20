# Quality Check

How to score and pressure-test an outbound message — a cold email or a LinkedIn message — against copywriting standards. This is the absolute, best-practice check (is the copy good?). The comparative check — how the copy stacks up against the user's own past campaigns — is a separate concern.

Used in two places:
- `multichannel-campaign-builder` — a light self-check on every message it generates.
- `campaign-challenger` — the best-practice baseline, especially when the user has no past campaigns to compare against.

## Step 1 — Detect the campaign type

The benchmark targets depend on the campaign type. Detect it before scoring.

| Type | Characteristics | Target reply | Target booking |
|---|---|---|---|
| Warm trigger-based | Engagement, post like, profile view, recent hire, funding, tool switch | 40–50% | 5% |
| Warm intent | Demo request, content download, webinar attendee | 30–40% | 5% |
| Cold targeted | ICP + persona match, no signal | 8–15% | 1–2% |
| Cold pure | List-based, no personalization signal | 5–8% | 0.5–1% |
| Re-engagement | Old / no-reply 60+ days | 10–15% | 1–2% |

If the user states the type, use it. Otherwise infer from the message: a trigger referenced in the opening → warm trigger-based; an obvious intent → warm intent; ICP match but no signal → cold targeted; otherwise → cold pure (conservative fallback).

## Step 2 — Score the 12 dimensions (1–10 each)

Score each with a cited excerpt as evidence.

| # | Dimension | What to assess |
|---|---|---|
| 1 | Authenticity & human voice | Sounds human, natural contractions, confident, passes the 15-second read-aloud |
| 2 | Pattern breaking & opening | 10–20 word opener, trigger / tension / insight, no flattery, "why now" relevance |
| 3 | Optimal length & structure | 50–100 words email / 40–70 LinkedIn, no sentence over 20 words, body max 3 sentences |
| 4 | Concrete value & impact | Specific pain, concrete outcome, active phrasing, prospect's language |
| 5 | Loss-aversion framing | Risks avoided, cost of inaction — not gain-only framing |
| 6 | CTA structure | Low-friction, value-framed, passes the permissionless-value bar below |
| 7 | Persona fit | Right altitude and language for the target buyer persona the user is going after |
| 8 | Value proposition relevance | Trigger → capability alignment, differentiated, business outcome |
| 9 | Safe social proof | "Companies like..." phrasing, no fabricated metrics, sector-relevant |
| 10 | Factual accuracy | Every claim traceable, no hallucinations (see Step 4) |
| 11 | Strategic question / insight | Non-generic, reply-driving, curiosity-driving |
| 12 | Positioning alignment | Consistent with the user's positioning: no positioning-banned words, claims on-message |

## Scoring dimension 6 — the permissionless-value bar

Most outreach dies at the CTA. *"Would you be open to a 30-minute call?"* is high-friction and seller-centric: it forces a binary the prospect has no reason to resolve in your favour yet, so they resolve it by ignoring the message.

A CTA that carries **permissionless value** delivers something standalone — an insight, a benchmark, a resource, a question worth answering — that the reader can use whether or not they ever buy. The reply comes from curiosity rather than obligation.

Score dimension 6 against five checks. A CTA passes only if all five hold:

- The prospect can use the insight or resource even if they never buy.
- The product is not mentioned.
- The reply it asks for fits in one word or one sentence.
- It is specific — it could not be sent to a thousand random people.
- No urgency, no implicit pressure.

Failing any one of them caps dimension 6 below the launch threshold, and the fix is a rewrite of the CTA rather than an edit.

Two structural faults score here as well, independent of the wording: a meeting ask in the opening touch, and the same CTA shape repeated in consecutive touches. Both are sequence-level defects that a per-message read will miss, so check them across the whole cadence before scoring.

Dimension 12 is the only one that depends on the user's own context. If the user has shared their positioning and a banned-word list, check the copy against them. If not, check only that claims are coherent and not off-brand, and skip the banned-word part.

## Step 3 — Performance killers (penalties)

Apply before computing the overall score.

**Red flags (−3 each):** the word "click"; an exclamation count of 2+ in one message; ALL CAPS words; an em-dash (—) anywhere in the body; an emoji in a professional email; a vanity metric stated as the headline result; a ROI or % claim with no traceable source (also a Critical Error — see Step 4); "checking in / following up / circling back".

**Moderate issues (−1 to −2 each):** over the word limit without justification; tone too formal / corporate; generic opening with no business relevance; missing CTA components; weak challenge-to-value link; generic "I saw on LinkedIn..." opener; "I hope this finds you well" / "I came across" / "Quick question"; filler verbs (leverage, utilize, optimize, streamline).

User-configurable: if the user has named positioning-banned words, treat each occurrence as a −3 red flag too.

## Step 4 — Accuracy assessment

Classify every key claim in the message:

- ✅ **Verified Fact** — cites a source the user provided
- 🔵 **Reasonable Inference** — logical, generic, makes no claim of certainty
- ⚠️ **Unsupported Claim** — not traceable, assumes internal context
- 🚨 **Critical Error** — fabricated metric, false claim, risky assertion

Any 🚨 must be rewritten before the message ships.

## Step 5 — Output

Produce: the campaign type + targets; the 12 dimension scores with excerpts; the penalties applied; the accuracy breakdown; the overall score (1–10); and the top 3–5 transformation priorities — the changes that will most improve replies and credibility.

When used as a self-check inside `multichannel-campaign-builder`, keep it lightweight: flag only messages scoring below 7/10, and rewrite those before output. When used inside `campaign-challenger`, produce the full breakdown.
