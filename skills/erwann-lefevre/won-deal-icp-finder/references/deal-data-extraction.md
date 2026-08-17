# Getting the deal data

Read this before pulling anything. The extraction is where the analysis is won or lost — every downstream number inherits the field choices made here.

## Learn the conventions before you pull

Three questions, answered from **one** sample: a single deal with its associated company and primary contact, properties listed. Don't keep probing; one well-chosen sample answers all three.

**1. Which field actually holds deal value?**

The CRM's standard amount field is frequently abandoned. Teams migrate to a custom ARR, ACV, MRR or "contract value" field and leave the original empty on every record. Check whether the standard field is populated on real deals before trusting it. If it's empty or sparsely filled, find the field that carries the money and pass it explicitly to the engine.

Watch for a value field that holds monthly figures while the team talks in annual ones, or the reverse. It doesn't change the ranking, but it changes every number you quote back.

**2. How does this team mark a deal won — if at all?**

Four possibilities, in descending order of convenience:

- A clean won stage in the pipeline.
- A boolean closed-won flag maintained by the CRM.
- A custom label the team applies by hand — often inconsistently, often localised.
- Nothing. Some teams never mark won; a populated value field is the only signal a deal was real.

The fourth case is common and is not a blocker. When no won signal exists, the engine analyses value-bearing deals in the window and reports the selection basis as `value-in-window`. Surface that basis in one line and ask the user to confirm it matches what they'd call a won deal. Lost deals are excluded in every mode.

The trap: assuming a won stage exists, matching nothing, and falling back to "the most recent N deals". Recent deals are the newest and therefore the emptiest. That failure produces a complete, confident, entirely worthless analysis.

**3. Where does acquisition source live?**

It sits on the deal, the company, or the contact, and it varies by setup. Check the standard analytics-source properties, then the custom ones — a "Lead Source", "Channel" or "Origin" field the team maintains manually. Note which object carries it.

While you're there, check whether any **campaign-level** field exists as well, and whether it has values in it. Channel without campaign is the normal state of affairs, and it's worth reporting: the team can see that outbound produced revenue but not which sequence did.

## The pull

Deals whose value field is populated, from the last 365 days, by close date where available and create date otherwise, with company firmographics attached — industry, headcount or size bucket, country.

**Do not pull the newest N deals regardless of value.** This is the single most common way this analysis goes wrong.

Write the rows to a file before analysing. The engine reads JSON or CSV from disk; going through a file means the analysis is reproducible and the pull happens exactly once.

## Keep it bounded

This is a handful of calls, not an investigation.

- Discover the schema from one sample. Stop.
- Pull the window in as few paginated calls as possible, requesting only the properties needed.
- Enrich company firmographics for the **top ~30 deals by value only**. They carry the revenue and they define the archetypes; the long tail changes nothing and costs real time.
- Persist once, analyse once. Don't re-pull, don't re-read files already in hand.

## The export fallback

Works with no connector at all, and is often faster than negotiating API access.

Ask for an export of deals carrying a value, from the last twelve months, including company industry, size and country plus whatever source or campaign column the team uses. Most CRM exports use human-readable column labels; the engine matches them by alias, so a raw export usually runs without any flags.

## When to stop and ask

Ask one short, specific question — where deal value lives, and how they mark a deal won — rather than guessing, whenever:

- No candidate value field is populated.
- Several value fields are populated and they disagree.
- The won signal is ambiguous or localised in a way you can't confirm.
- The engine refuses.

An engine refusal is a question for the user, not an obstacle to route around. One question costs a minute; a wrong field choice costs the whole analysis and isn't visible in the output.
