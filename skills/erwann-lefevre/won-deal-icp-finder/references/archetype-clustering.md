# Building the archetypes

The engine returns segments. Turning them into two to four profiles a prospector can actually search is the judgment half.

## What an archetype is

A named, criteria-based company profile that several won customers fit — not a description of one customer, and not a vibe.

Each one needs:

- **A title** a seller would use out loud. "Mid-market FinTech in FR/DE", not "Segment B".
- **Objective criteria**: one or two industries, one or two size buckets, one or two geographies. More values per dimension and it stops being searchable.
- **A typical deal size**, taken from the deals in the group.
- **The evidence**: how many won companies fit, and which ones.
- **A buyer persona** where the motion supports inferring one — seniority and function — explicitly labelled as inferred when the data never recorded it.

## How to build them

Intersect the revenue-dominant segments rather than reading each dimension separately. The leading industry and the leading size bucket are frequently the same set of companies; treating them as two findings double-counts them and produces archetypes that overlap.

Aim for groups that are distinct from each other and each tight enough to hand to someone building a prospecting list. Two sharp archetypes beat four blurry ones.

Cap at four. Past that you are slicing noise, and the thin groups are usually one customer each. Collapse them.

## Anti-patterns

| Trap | Why it misleads | Do instead |
|---|---|---|
| Ranking or clustering by deal count | Rewards whichever segment is cheapest to sell to, which is rarely the one that pays | Cluster on revenue share |
| One archetype per top account | A whale is not a repeatable profile | Group on shared firmographics; report the concentration instead |
| Reading a channel ranking off a thin source field | Coverage below ~70% describes a sample, not the book | State coverage next to the ranking |
| An archetype broad enough to match anyone | "B2B in Europe" returns the whole market | One or two values per dimension |
| Filling in firmographics the data didn't carry | Absent is not the same as free to guess | Flag the gap; label inferences as inferred |
| Building on the top ten deals rather than the top ten accounts | A customer with four deals gets counted four times | Cluster from per-account revenue |

## The concentration caveat

When one account holds more than roughly a quarter of the revenue, the honest reading is that the book leans on one customer. Say that first, then build archetypes from what remains.

Two teams get this wrong in opposite directions: one builds an "ICP" that is a portrait of its single largest customer, and the other drops the whale entirely and describes a business it doesn't have. Report the concentration, keep the account visible in the evidence, and don't let one logo set the criteria.

## Worked example

Run `examples/sample-deals.json` and the engine returns 12 won deals across 10 companies, 342,000 total, `top_1_account_share` 21.1%.

The industry segment reads:

| Industry | Revenue | Share |
|---|---|---|
| FinTech | 113,000 | 33.0% |
| SaaS | 92,000 | 26.9% |
| Logistics | 70,000 | 20.5% |
| Consulting | 40,000 | 11.7% |

Size concentrates in 51–200 (48.0%) and 201–500 (41.5%); geography in France (49.4%) and Germany (31.0%).

The naive reading takes the top three industries and produces three archetypes. Check the accounts before you do, because the third one dissolves:

**A — Mid-market FinTech, FR/DE.** 51–500 employees. Cobalt FinTech (FR, 72,000 across 2 deals) and Vantage FinTech (DE, 41,000). Two companies, 33.0% of revenue, typical deal 36–41k.

**B — Growth-stage SaaS, DE/FR.** 51–200 employees. Velora (DE, 36,000), Meridian (DE, 29,000), Quill (FR, 27,000). Three companies, 26.9% of revenue, typical deal 27–36k.

**Logistics is not archetype C.** That 20.5% is Northwind Logistics — one company, two deals, no second example anywhere in the book. It looks like a top-three segment in the industry table and it is a single customer. Report it as concentration, not as a profile: a segment whose entire revenue sits in one account tells you that account renewed, not that a market exists.

The remaining four companies span Consulting, Manufacturing and Retail with one deal each and sit in different size buckets. That's the tail. Saying so is more useful than manufacturing a "Segment D — Other".

Note the shape of the check: the industry table alone would have produced three archetypes, one of which is a mirage. Cross-referencing every candidate segment against the account list — *how many distinct companies is this?* — is what catches it. Do it every time; a segment backed by fewer than two companies is a customer, not a pattern.

Note also what the example doesn't do: it doesn't claim a buyer persona, because this dataset never carried contact roles. Inferring one here and labelling it "(inferred)" would still be inventing it.

## Handing it off

The output is finished when someone building a prospecting list can use it without asking a follow-up question. That means each archetype restates cleanly as a single line of search criteria — industries, size range, geographies, target function — with nothing left to interpret.

If a criteria line needs a paragraph of explanation to be usable, the archetype is still too vague.
