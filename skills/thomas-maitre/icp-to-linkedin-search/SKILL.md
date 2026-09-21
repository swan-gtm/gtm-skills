---
name: icp-to-linkedin-search
title: ICP to LinkedIn search
description: |
  Use this skill when someone describes who they sell to, in a sentence, a website URL
  or a rough persona, and needs it turned into something LinkedIn can search: a
  structured ICP in seven facets, normalized title families, a boolean string for the
  title field, an exclusion list, and a company count that says whether the audience is
  a motion, a campaign or a market. Fires on "build me a LinkedIn search", "Sales
  Navigator boolean", "people search for <persona>", "size this audience", "normalize
  these job titles", "CMO plus Chief Marketing Officer plus VP Marketing", or "exclude
  fractional, freelance and interns".
category: Prospecting
tags: [Sales]
---

Applies before any list is built or any outreach starts, whenever the buyer exists only
as a sentence. Produces an ICP card, a boolean title string with its exclusions, and a
company count with what to change if the count is wrong.

Input: "CFOs at Swiss fintechs", a website URL, or a paragraph about the buyer. The
mistake to avoid is treating a title as a string; it is a family, and the search that
uses one wording finds a third of the people.

## The play

1. **Extract the seven facets.** `titles`, `seniority`, `languages`, `industries`,
   `sizes`, `locations`, `exclude`, as plain-word lists. Name only the facets the input
   gave or that follow from the product; an empty facet means "any", not "unknown". From
   a website URL, read the pricing page for the size band, the customer logos for the
   industry, the docs or integrations page for the buyer's function. Facet definitions,
   headcount bands and the URL-reading routine are in `references/facets.md`.
2. **Normalize the titles into families.** For each role: the acronym and the long form,
   the VP, Head, Director and Lead variants where company size makes them the same
   person, the local-language forms for each language, and the adjacent function that
   owns the same budget. Then the exclusions: always `fractional`, `freelance`,
   `interim`, `intern`, `assistant to`, `student`, `former`, `ex-`, `retired`,
   `looking for`; usually `recruiter`, `agency`, `consultant`, `advisor`. Full method and
   worked families in `references/title-families.md`.
3. **Write the boolean string.** Quotes around multi-word titles, `OR` inside a family,
   `NOT` for the exclusions, parentheses around each group, at most 15 operators per
   field. Keywords are a separate field for the chore or the tool, never for the title.
   Syntax rules and a filled example in `references/boolean-and-sizing.md`.
4. **Size it, in companies.** Count companies with the three company facets only
   (industry, headcount, geography); titles do not change the company count and people
   counts double-count the same firm. A few thousand companies is a motion; a few hundred
   is a campaign; tens of thousands is a market, not a buyer. Iterate on the three facets
   until the number fits the pace. How to count and what to change in
   `references/boolean-and-sizing.md`.
5. **Hand over the card.** The seven facets, the string, the company count, and the two
   or three things LinkedIn cannot filter on (a language, "does their own prospecting", a
   tech stack). Those are judged per person at reading time, not per search.

## What good looks like

- The best operator writes the title family before the boolean and finds the local
  forms. "Directeur Commercial" is not in an English-only string, and at 11 to 50
  employees the "Head of Marketing" is the CMO.
- The mediocre version is one title in quotes with no `NOT` group. It returns the
  fractional CFOs, the interim ones, the ones "looking for" the role, and the assistant
  to the real one.
- The size step catches the two failure modes before money is spent: 40 companies means
  a campaign dressed up as an ICP; 30,000 means the buyer has not been chosen yet.
- A good card can be handed to someone else and they run the same search. Facets are
  plain words; nothing depends on the reader's memory of the conversation.

## Rules

- MUST write titles as families (acronym, long form, size variants, local language)
  before writing the boolean string.
- MUST add the standard exclusions to every string; `fractional`, `interim` and
  `looking for` are never the buyer.
- MUST size in companies, not people, and report the count with what to change.
- NEVER put a chore or a tool word in the title field; keywords are their own field.
- NEVER exceed 15 operators in one field; split into two searches instead.
- NEVER treat an empty facet as a constraint; empty means any.
