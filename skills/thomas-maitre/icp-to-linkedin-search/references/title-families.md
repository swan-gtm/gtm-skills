# Title families

A title is a family, not a string. One wording finds a third of the people who hold
the role. For each role the input names, write the family in four parts.

## The four parts

| Part | Rule | Example for "CMO" |
|---|---|---|
| Acronym and long form | both, always | CMO, Chief Marketing Officer |
| Size variants | VP, Head, Director, Lead, when company size makes them the same person | VP Marketing, Head of Marketing, Marketing Director (at 11 to 200 employees these are the CMO) |
| Local-language forms | one set per entry in `languages` | Directeur Marketing, Responsable Marketing, Directrice Marketing |
| Adjacent budget owner | the function that owns the same budget | Growth (for a marketing tool), Demand Gen |

## Size decides the variants

| Company size | Who owns the function | Titles to include |
|---|---|---|
| 1-10 | the founder | Founder, CEO, Co-founder, plus the function title if any |
| 11-50 | one person, any title | Head of, Lead, Director, VP, C-level, all the same person |
| 51-200 | Head or VP, with a manager under them | Head of, VP, Director; exclude Manager unless the tool is bought at manager level |
| 201-1000 | VP with directors | VP, Director; the C-level is too far from the tool |
| 1001+ | a director owns the budget line | Director, Senior Director; VP only for strategic deals |

Writing "CMO" against a 1001+ band finds the wrong person: the CMO of a 3,000-person
company does not buy a tool, a director does.

## Worked families

**"Heads of Sales at French SMBs"** (`languages: French, English`, `sizes: 11-200`):
CEO, Founder, Co-founder, Head of Sales, VP Sales, Sales Director, Directeur Commercial,
Directrice Commerciale, Responsable Commercial, Head of Revenue, CRO.

**"RevOps at mid-market SaaS"** (`sizes: 201-1000`):
Revenue Operations, RevOps, Head of Revenue Operations, Director of Revenue Operations,
Sales Operations, Sales Ops, GTM Operations, Head of GTM Ops. Adjacent: Head of Sales
Enablement (same budget at 201-500).

**"CFOs at Swiss fintechs"** (`languages: French, German, English`):
CFO, Chief Financial Officer, VP Finance, Head of Finance, Finance Director, Directeur
Financier, Finanzchef, Leiter Finanzen, Finanzvorstand. Adjacent: COO at 11-50 (the
CFO does not exist yet).

## The exclusion list

Always in `exclude`: `fractional`, `freelance`, `interim`, `intern`, `assistant to`,
`student`, `former`, `ex-`, `retired`, `looking for`, `open to work`.

Usually in `exclude`, unless they are the buyer: `recruiter`, `talent`, `agency`,
`consultant`, `advisor`, `coach`, `investor`.

Exclusions are absolute. A model scoring fit will rate a fractional CFO as a fit; the
exclusion runs before scoring, or the list fills with people who do the job for six
clients and buy nothing.
