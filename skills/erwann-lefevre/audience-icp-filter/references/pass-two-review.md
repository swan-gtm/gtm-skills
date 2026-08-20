# Pass 2 — semantic review

Pass 1 sorts on patterns. Pass 2 reads for meaning. It is mandatory, it is bounded, and it is the agent's work rather than the user's.

## Review the queue, not the list

Pass 1 returns a `pass2_queue`: the only leads worth inspecting. Reviewing anything outside it is the eight-minute mistake — on a 250-lead list, reading every lead individually took eight minutes and changed almost nothing, because the confident classifications were never in doubt.

On a clean, on-target list the queue is fifteen to twenty-five leads. That's the whole job.

| Flag | What it is | What to check |
|---|---|---|
| `ambiguous` | the entire review bucket | resolve to match or no_match where you honestly can |
| `bio-inferred match` | matched from the bio, not the title | confirm the bio really indicates an in-ICP function |
| `agency/freelance` | a match whose company or bio reads like an agency, freelancer or consultant | keep if they're a real buyer, drop if they're a service provider |
| `dropped on geo/industry` | right seniority and function, failed the location or industry substring | rescue if the label is just a variant of an in-ICP value |
| `bio-inferred drop` | left the ICP on a seniority or function read out of the bio, not the title | confirm the bio really means that, before discarding the lead |

Note that false positives live in `match`, not only in `review` — which is why the queue pulls risky matches in alongside the ambiguous ones. That's how you catch them without re-reading the confident ones.

The same logic runs in the other direction. A lead dropped because of a function or seniority read out of free text is the mirror image of a bio-inferred match: same weak signal, worse consequence, because a wrong drop is invisible by construction. Nothing leaves the ICP on an inference without passing through the queue first.

## What patterns can't catch

| Lead | Pass 1 says | Reality |
|---|---|---|
| `Chief Happiness Officer` | C-level → match | HR role. Not a buyer. |
| `Chief Medical Officer` | C-level → match | Clinical role. Not a buyer. |
| `Head of Growth` at an unlisted competitor | match | Should be excluded |
| `companyName: "Nothing"` | treated as a company | Junk data |
| `Founder @ Stealth Mode` | review | Almost certainly in ICP |
| A title in a language the taxonomy misses | review | Often a clear match |

The `Chief … Officer` pattern is deliberately broad in pass 1 — it catches every real C-level, and pass 2 removes the happiness, medical and people officers. Narrowing the pattern to avoid the false positives would lose real buyers, which is the worse error.

**Bare functional C-titles resolve for seniority but not for function.** `CMO @ Acme` is unambiguously C-level and carries no function token, so it lands in review. Read these as their function — CMO as marketing, CRO as sales, CTO as product/tech — rather than leaving them ambiguous.

## Two rescues worth knowing

Both came out of real runs and both are pure queue work:

**Agencies and freelancers sitting in `match`.** The title and function are right, and the company is a five-person consultancy that will never buy. Or it's a genuine buyer who happens to be independent. Only reading tells you which.

**Real target companies sitting in `no_match` on an industry label.** A software company labelled `Technology, Information and Internet` rather than `Software` fails an industry substring and gets dropped. The synonym expansion catches the common cases; the queue flag catches the rest.

## Working the queue down is the deliverable

Read each queued lead's full record — title, bio, industry, company — and resolve as many as you honestly can. Write the overrides with a substantive reason each; the adjudication step rejects reclassifications with no reason, duplicates, invalid buckets, and overrides on leads that don't exist. Nothing can be lost in pass 2 either.

Leave only the genuinely ambiguous handful for a human decision. A fifty-lead review bucket handed back untouched is not a result — it's the hand-sorting this skill exists to eliminate, relabelled as output.

## When the queue is large

A queue of sixty or more is a diagnosis, not a workload. Two causes, in order of likelihood:

1. **The list was never enriched.** Check coverage. Thin titles and empty bios push everything into ambiguity.
2. **The ICP is under-specified.** Most often the founder question went unanswered, so every function-less founder title is sitting in review. Sometimes the function list is simply too narrow for the list in hand.

Name the cause and fix it upstream. Re-running pass 1 with a corrected spec takes seconds; hand-reviewing sixty leads does not.

## Report what changed, briefly

What pass 2 reclassified is an audit detail, not a headline. One line: how many moved, and why in aggregate — "moved 3: 2 rescued on an industry-label variant, 1 competitor excluded". The buckets and counts are the result; the reclassification log is provenance.
