# Using the checker

`scripts/lint_style.py` finds the mechanical patterns and leaves the rewrite free to focus on judgment. It uses only the Python standard library, reads the files you name and prints a report. It makes no network calls and changes nothing.

## Run it

```bash
python3 scripts/lint_style.py draft.md
python3 scripts/lint_style.py page.html email.txt
```

It accepts `.md`, `.html` and `.txt`. When code execution is not available, apply the six patterns by hand using `retired-patterns.md`; the report format below tells you what to look for.

## Reading the report

- `RULE` hits break a written rule. Fix every one. The exit status is 1 when any appear.
- `CHECK` hits are heuristics (a possible fragment, three short sentences in a row, a sentence past 45 words). Read each and decide.
- The checker cannot see every fragment. Read the whole draft for sentences with no verb, especially card descriptions and list items.

## Options

| Option | Effect |
|---|---|
| `--core-only` | Check only the six retired patterns |
| `--skip em-dash,stock-word` | Switch off named house-style rules |
| `--british` | Do not flag British spellings (default flags them, because the default is American English) |
| `--list` | Print every rule name and what it checks, then exit |

Rule names: so-splice, so-bare, so-that, so-opener, worth, nudge, long-before, well-before, none-of, announce, fragment, is-not-it-is, em-dash, not-just, x-not-y, n-nouns, stock-word, partner-verb, spelling.

## Protecting deliberate exceptions

Wrap a span the checker should skip between markers:

```
<!-- lint:off -->
We deliver seamless, holistic solutions.   (shown here as an example of what to avoid)
<!-- lint:on -->
```

The markers work in Markdown, HTML and plain text. Use them only for demonstrations, legal wording and quoted examples, and say so in the report.

## Adding a rule

Add a tuple to `CORE_RULES` (retired patterns) or `HOUSE_RULES` (configurable preferences) with a name, a regular expression and a plain-language reason. Add a before-and-after pair to `rewrite-bank.md` in the same change.
