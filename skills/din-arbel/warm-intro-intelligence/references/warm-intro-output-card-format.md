---
title: Warm Intro Output Card Format
description: Reference for the Warm intro intelligence skill.
---

# Warm Intro Output Card Format

Sub-page of the Warm Intro Intelligence skill. Load when executing Step 9 - generating the output card.

---

## Card Structure

Deliver the following in chat. Keep it scannable - under 1 minute to read. Every path gets one block, not a wall of text.

---

**Warm Intro Map - [Prospect Company Name]**
Segment: [Segment] - Stage: [Stage] - [Open deal / no deal / already in sequence - one line]

**Buying committee targeted:** [Name (Role)], [Name (Role)], [Name (Role)]

----------------------------------------

**Path [N] - [Strong / Medium / Low]** [- Source tag if non-CRM, e.g. - Transcript]
[Bridge] -> [Intermediate if 2-hop] -> [Target Name, Role]
[One sentence: what the evidence is and why it's relevant.]
[!] [One sentence: the key unknown or limitation.]

[Repeat for each additional path]

----------------------------------------

[If no verified/moderate path: "No verified or moderate path found. All paths above are worth a quick check with the relevant rep before going cold."]

**Sources:** [Source check or - not available, comma-separated]

*You decide whether to pursue any of these.*

---

## Context Field (optional, per path)

When Step 7 context enrichment finds co-mentions between the bridge and the target contact, append a Context block after the [!] line:

Context: [Bridge] and [Target] [one-line description - e.g. "appeared on the same industry conference panel, 2025" or "co-authored an article on [shared topic], Jan 2026"]. ([Source, Date])

Rules:
- Label it Context every time - never fold it into the evidence line.
- One line maximum. No bullet lists.
- Source and date always included.
- Never use language that implies this strengthens the relationship confidence ("this suggests a strong relationship", "this confirms they know each other"). Context only.
- If LinkedIn URL was missing and the post scrape couldn't run, do not add a note - omit the context block entirely.
- If nothing was found in web research or LinkedIn posts, omit the context block entirely. Do not write "no context found."

## Champion Migration Paths

When a path comes from the Champion Migration check (a known contact who now works at the target):
- Tag the path header: **- Champion Move**. Example: **Path 1 - Strong - Champion Move**
- The evidence line must state the migration explicitly: who owned the relationship, what the interaction was, at which prior company, and where the contact is now. Example: *"[Your founding AE] had 3 logged meetings with [contact] while they were at [prior company]; they're now VP Payments at [Target]."*
- The [!] line still applies and reflects the real gap (usually recency - how long since the last interaction).

### Team Migration Note

If two or more known contacts now work at the target account, add one line after the last path block, before the sources footer:
"We already know [N] people now at [Company][ - [N] of them came from [prior company]]. This is awareness only and does not affect the ranking above."
Never let team migration influence which paths are shown or how they rank.

## Per-Path Rules

- Max 3 lines per path: evidence line + [!] limitation line + optional "why worth checking" if genuinely useful.
- Source tag only for non-CRM signals (Transcript, LinkedIn, Intake, Champion Move) - keep it visible so the rep knows where it came from.
- [!] line is mandatory. Never omit it even for the strongest paths.
- Never use bullet lists inside a path block. One evidence line, one warning line.

## Path Confidence Labels

- **Strong** - weakest edge is Verified
- **Medium** - weakest edge is Moderate
- **Low** - any edge is Inferred

Always include the label in the path header. Example: **Path 1 - Strong** or **Path 2 - Low - Transcript**

## Path Ranking

Paths are ranked in Step 6 using the Path Ranking logic in the Evidence Rules and Confidence Scoring sub-page (the single source of truth: confidence tier -> recency -> persona priority -> hop count). Do not re-rank at the output stage - render the paths in the order Step 6 produced them. Context enrichment (Step 7) never changes this order.

## No Path Found

If no paths exist at any confidence level:

"No relationship signals found between our network and this prospect.
If you have a personal relationship with anyone at this company or in their network, sharing it could help surface a path."

## Persona Not Found

If no contact was found for one or more identified personas, add one line after the buying committee header:
"No contact found at [Company] matching [Persona] - CRM and LinkedIn returned no results."

## Same Persona Note

If all paths target the same persona, add after the last path:
"All paths above target [Persona Name]. No alternative path to a second persona was found."

## Sources Footer Format

List only sources that were actually checked. Format:
CRM check - LinkedIn employment check - Transcript check - Champion migration check - Sales Nav not available - Intake flags none

If Sales Nav was checked for only some reps, note it: Sales Nav check ([rep names])

## Language Rules

- Suggested paths are options, not instructions. Never write "ask X to intro you." Write "X may be able to connect you."
- [!] line states the specific gap, not a generic caveat.
- Keep the whole card under ~250 words. If it runs longer, tighten the evidence lines first.
- Never omit the sources footer - the rep needs to know what was and wasn't checked.
