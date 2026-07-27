---
title: Evidence Rules and Confidence Scoring
description: Reference for the Warm intro intelligence skill.
---

# Evidence Rules and Confidence Scoring

Sub-page of the Warm Intro Intelligence skill. Load when executing Step 5 - assessing edge confidence for each relationship path found.

---

## Edge Confidence Tiers

### Verified
Direct, dated, logged evidence of two-way interaction between the bridge and the target contact. Any one of the following is sufficient:

- CRM meeting or call logged with the target contact - but ONLY if it passes the Meeting Substance Test below. A meeting record alone is not Verified.
- CRM email thread where both the bridge and target contact appear, with at least one reply from the target contact's email address. A one-way send with no reply is NOT Verified (see Email Substance Test).
- LinkedIn DM or InMail thread with at least one response from the target contact (accessed via the bridge's connected LinkedIn account).
- Explicit note in the CRM or account memory naming both the bridge and the target contact with specific relationship context. Must reference the relationship directly - generic CRM notes and auto-generated placeholders do not qualify.
- Warm Relationship Intake flag confirmed by the internal bridge, with intro_willingness of "strong" or "possible" and source of "intake" or "inferred+confirmed".

Always record the date of the most recent evidence item as the last interaction date.

---

## Evidence Integrity Rules (apply before assigning ANY tier)

These rules exist because a record existing is not the same as a relationship existing. A meeting count, an email count, or a title is metadata - not evidence. Violating these produces false-Strong paths that waste rep trust.

### Rule 1 - Score from content, never metadata
Before assigning any confidence tier, open the record and read its actual content. Never score from the existence of a record, a count of meetings/emails, or a title alone. If you have not read what the interaction actually contained, you cannot assign Verified.

### Rule 2 - Meeting/Call Substance Test
A CRM meeting or call qualifies as **Verified** only if ALL of the following are true:
- It has an assigned owner, AND
- It has a substantive note, body, agenda, or outcome (NOT an auto-generated placeholder such as "left no additional comments," "no notes," or an empty body), AND
- The title indicates a real interaction (NOT a bare "Event Meeting," "Badge Scan," "List Import," or similar capture label).

A meeting record that is title-only, has a placeholder/empty body, or has no owner is treated as **Moderate at most**, labeled: "event capture - interaction depth unconfirmed (likely badge scan or lead grab)." It is NOT Verified.

### Rule 3 - Email Substance Test
- A two-way thread with at least one genuine reply from the target contact -> may be Verified.
- A one-way outbound send (sequence step, single email, no reply) -> **Moderate at most**, never Verified. A logged email existing is not a relationship.
- Auto-replies, out-of-office, and bounce messages do NOT count as a reply.

### Rule 4 - Strong-Tier Verification Gate
Before labeling any path Strong, run a final check: does the underlying record contain a confirmed two-way interaction that passed the substance tests above? If you cannot point to the specific content that confirms a real interaction, downgrade to Medium. When genuinely uncertain between two tiers, choose the LOWER one and state what would confirm the higher tier. Honest under-labeling protects rep trust; false-Strong destroys it.

### Moderate
Credible signal of a relationship, but depth is unknown. Any one of the following is sufficient:

- LinkedIn 1st-degree connection between bridge and target contact - confirmed via Sales Nav or connected LinkedIn account. No message history required, but none visible.
- Shared employment at the same company during overlapping years, AND their roles are at seniority levels plausibly in contact. Rule: any overlap at a company under 100 employees qualifies; VP-level or above at a larger company qualifies. Junior roles at large companies do not qualify without additional evidence.
- Both tagged in the same event in account memory (co-presence confirmed, interaction not confirmed).
- One-way CRM email outreach from the bridge to the target contact with no reply logged.
- Confirmed shared investor: a firm in `{{INVESTOR_REGISTRY}}` also invested in the prospect company. Verifiable overlap; VCs routinely facilitate portfolio-company intros. Firm-level - specific partner relationship not yet identified.
- Unconfirmed Warm Relationship Intake flag where source is "inferred" and not yet confirmed by the bridge.

### Inferred
A pattern suggests a possible relationship. No direct evidence of person-to-person interaction. Any one of the following is sufficient:

- 2nd-degree LinkedIn connection (bridge is connected to someone who is connected to the target contact).
- Company-level commercial relationship between one of your customers or partners and the prospect company - without any person-specific evidence linking specific individuals.
- Public co-mention (both names appear in the same press article, conference panel recording, podcast, or content piece).

---

## Champion Migration Edge Confidence

A champion-migration edge (a pool member who now works at the target account) inherits the confidence of the ORIGINAL relationship formed at the prior company. It never gets a confidence boost for having moved into the target.

- Logged meeting or call, or a replied email thread, at the prior company -> **Verified**
- 1st-degree connection, shared employment only, or other Moderate-tier signal -> **Moderate**
- Pattern only, no logged interaction -> **Inferred**

Mandatory on every champion-migration edge:
- **Migration flag:** "[Verified/Moderate] at [prior company] - [contact] moved to [target] as [current role]."
- **Recency governs, not the move date.** Apply the standard recency weighting to the LAST INTERACTION date, not the date the contact joined the target. A relationship that has gone quiet for 18+ months is stale even if the migration is recent.

When multiple champion-migration hits exist at the same target, each is a separate candidate path and is ranked by the standard Path Ranking logic below - confidence first, then recency, then persona priority, then hops. There is no separate "which champion wins" rule.

---

## Path Confidence

Path confidence is determined by the weakest edge confidence in the path:

- Every edge is Verified -> path confidence: **Strong**
- Weakest edge is Moderate, no edge below Moderate -> path confidence: **Medium**
- Any edge is Inferred -> path confidence: **Low**

Edge labels (Verified / Moderate / Inferred) and path labels (Strong / Medium / Low) are always shown separately. Never combine them or use one label for both levels.

---

## Required Fields Per Edge

Every edge in every output path must include all of the following. Do not omit any field - if a value is unknown, state that explicitly.

- **Confidence:** Verified / Moderate / Inferred
- **Evidence:** what was found, which system it came from, specific details (meeting count, email count, date range, etc.)
- **Last verified / last interaction date:** the most recent date associated with the evidence. If unknown, state "date unknown."
- **Unknown:** the specific gap that limits this edge's confidence. Be precise - "no direct communication found" is better than "relationship depth unknown."
- **Why worth checking:** why the rep might still act on this path despite the limitation. Only include if there is a genuine reason - do not pad this field.
- **What would increase confidence:** the specific signal or action that could upgrade this edge. Examples: "[the bridge rep] confirming the relationship directly," "a CRM meeting logged with this contact in the last 12 months," "a LinkedIn reply thread confirmed via Sales Nav."

---

## Weak Link Rule

For every path, the weakest edge is the confidence-limiting edge. Always name it explicitly in the path summary so the rep can identify the gap without reading all edge details.

Format: "Weak link: [Edge description] - [one sentence explaining the gap]"
Example: "Weak link: Customer Contact -> Prospect VP - company-level relationship only, no person-to-person connection confirmed."

---

## Path Ranking

1. Sort by path confidence: Strong -> Medium -> Low.
2. Within the same confidence tier, apply recency weighting:
   - Last interaction within 6 months -> full weight
   - Last interaction 6-18 months ago -> reduced weight (rank lower within tier)
   - Last interaction 18+ months ago -> lowest weight (rank last within tier, flag as potentially stale)
   - Last interaction date unknown -> treat as 18+ months for ranking purposes
3. Within the same confidence tier and recency band, sort by target persona priority (per `{{PERSONA_MAP}}`): a path reaching a higher-priority buyer persona ranks above one reaching a lower-priority or non-buying persona.
4. Within the same confidence tier, recency band, and persona priority, sort by path length: 1-hop before 2-hop.
5. Return the top 2 paths.
6. Prefer paths targeting different personas. If both top paths target the same persona, note it explicitly.

Persona priority is a ranking axis, not a filter. A known contact who moved into the target in a role outside the buying committee still surfaces - they can intro internally - but ranks below an in-persona path. Never discard a valid path solely because the persona is non-ideal. Confidence and recency always outweigh persona: a high-confidence, recent relationship with a slightly-off persona beats a stale relationship with the perfect persona, because an intro that will actually happen is worth more than a cold path to the ideal contact.

---

## No-Path Case

If no paths exist at any confidence level, do not return an empty output. State: "No relationship signals found between your company's network and this prospect. The paths below are the best available." Then present whatever was found, fully labeled.

If genuinely nothing was found - no bridges, no connections, no overlapping employment: state that clearly and include the gap-triggered intake prompt from the Warm Relationship Intake sub-page.
