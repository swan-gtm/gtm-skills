# Seniority and function classification

The tiers pass 1 applies. The full regex patterns live in `title-taxonomy.json`, which `build.py` loads — you don't need to read it. Consult it only to extend the taxonomy or when someone disputes a classification.

## Seniority — first match wins

Evaluated top-down, which is why `Chief Executive Officer` resolves as founder/C-level rather than matching "executive" further down.

| Tier | Matches |
|---|---|
| `founder_c` | Founder, Co-Founder, Fondateur/Fondatrice, CEO/CTO/CMO/CRO/COO/CFO, Chief … Officer, President, Owner, Managing Partner, Managing Director |
| `vp_head` | VP, SVP, EVP, Vice President, Head of, Director, Directeur/Directrice, General Manager, Country Manager |
| `manager_lead` | Manager, Lead, Responsable, Supervisor, Principal, Founder's Office |
| `ic` | Account Executive, SDR, BDR, Specialist, Coordinator, Analyst, Consultant, Engineer, Intern, Junior |

Ordering is load-bearing. A flat set of patterns would classify `VP of Engineering` and `Engineer` identically.

## Function — all matches collected

Unlike seniority, functions accumulate. `General Manager of Sales and Marketing` carries both `sales` and `growth_marketing`, and satisfies an ICP containing either.

| Key | Matches |
|---|---|
| `sales` | Sales, Vente, Commercial, Account Executive, SDR/BDR, Business Development, New Business, Pre-Sales |
| `growth_marketing` | Growth, Marketing, MarTech, Demand Gen, Acquisition, Brand, Content, SEO, Paid |
| `revops` | RevOps, Revenue Operations/Systems/Strategy, Sales Ops, GTM, Go-to-market, CRM, Automation, Enablement |
| `partnerships` | Partnerships, Alliances, Channel, Affiliate |
| `product_tech` | Product, Engineering, Software, Technology, Data, Security, Platform, Architect |
| `other` | HR, Recruiting, Finance, Legal, Customer Success, Support, Coaching, Editorial |

Collecting rather than picking matters for cross-functional titles, which are common at the size of company most ICPs target. Forcing a single function on a `Head of Growth & Partnerships` throws away half the signal.

## Title first, bio as fallback

Detection runs on the job title. When the title carries no seniority signal, or no function signal, pass 1 falls back to the bio.

A `Managing Director` whose bio reads *"Développement commercial"* matches on that bio. This is worth more than it sounds: on a real 150-lead list, reading the bio cut the review bucket by roughly 60%.

Every bio-inferred match is flagged as such in its reason and enters the pass-2 queue, because inference from free text is exactly where a pattern is most likely to be confidently wrong.

## Case is part of the pattern

Detection runs against the original string, not a lowercased one, and **a pattern written with an uppercase letter is matched case-sensitively.**

This exists because short acronyms are indistinguishable from ordinary words once case is discarded. Matched case-insensitively, `IT` matches the English pronoun — so a bio reading "making it happen" scores as a technology function, and if the ICP doesn't include that function the lead is dropped. Three patterns rely on this: `IT`, `R&D`, and `EI` in the agency list.

The practical rule when extending the taxonomy: write a pattern in lowercase unless the capitals carry meaning. `\bproduct\b` should match "Product", "product" and "PRODUCT" alike; `\bIT\b` should match only the acronym.

## Multilingual titles

The taxonomy carries French alongside English — `Fondatrice`, `Responsable`, `Directeur`, `Commercial`, `Vente` — because a list drawn from a European market is routinely half non-English, and a taxonomy that only reads English routes all of it to review.

It doesn't cover every language. A title in one the taxonomy misses lands in review and gets resolved in pass 2, which is the correct failure mode: visible and recoverable rather than silently mis-sorted.

## Noise titles

Student, intern, open-to-work, retired, investor and similar route to `no_match` rather than `review`. They aren't ambiguous — they're clearly not buyers — and putting them in review inflates the bucket that a human has to read.

The distinction is worth holding to generally: `review` means *the engine declined to guess*, not *this lead is unusual*.
