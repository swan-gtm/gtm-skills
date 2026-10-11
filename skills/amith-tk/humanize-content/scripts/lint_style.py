#!/usr/bin/env python3
"""Check copy against the mechanical rules in the humanize-content skill.

Usage: lint_style.py [options] FILE [FILE ...]      (.md, .html or .txt)

RULE hits break a written rule and should be fixed.
CHECK hits are heuristics and need a human judgment.
Exit status is 1 when any RULE hit is found.

Reads the named files only. No network access, no file changes.
Wrap deliberate exceptions between <!-- lint:off --> and <!-- lint:on -->.
"""
import argparse
import html
import re
import sys

# Retired patterns: always checked unless a rule is explicitly skipped.
CORE_RULES = [
    ("so-splice", r",\s+so\b(?!\s+(?:many|much|far|long|little|few)\b)", "comma followed by 'so' (retired pattern 2)"),
    ("so-bare", r"(?<![,.!?:;])\s+so (?:the|a|an|you|your|we|they|it|its|each|every|there|this|these|both|everyone|nobody|buyers?|sales|marketing)\b", "'so' splicing two clauses without a comma (retired pattern 2)"),
    ("so-that", r"\bso that\b", "'so that' is the same splice (retired pattern 2)"),
    ("so-opener", r"(?:^|[.!?]\s+)So\s", "sentence opening with 'So'"),
    ("worth", r"\bworth(?:while)?\b(?!\s+(?:an?\s+)?(?:estimated\s+)?[$£€\d])", "'worth' as an editorial nudge (retired pattern 3)"),
    ("nudge", r"\b(?:it(?:'s| is) important to note|bears mentioning|keep in mind|here(?:'s| is) the thing|the truth is|the reality is|interestingly)\b", "editorial nudge phrase (retired pattern 3)"),
    ("long-before", r"\blong (?:before|after|since)\b", "'long before/after' (retired pattern 4)"),
    ("well-before", r"\bwell (?:before|after)\b", "'well before/after' is the same gesture (retired pattern 4)"),
    ("none-of", r"\bnone of (?:it|them|this|that|these|those)\b", "'none of ...' closer (retired pattern 5)"),
    ("announce", r"(?-i:\bThe) (?:part|thing|bit|trick|catch|trap|key|secret|point) (?:that|which|is|of|about)\b|(?-i:\bThe) (?:first|real|hard|hardest|only) (?:job|step|part|work|problem|question|difference|differences|answer|issue|task|goal|test|catch) (?:is|are)\b|(?-i:\bThe) (?:difference|practical consequence) is\b|(?-i:\bWhat) (?:matters|counts|separates|compounds|works)\b[^.?!\n]{0,60}\bis\b|(?-i:\bMost) of what (?:gets|is) (?:called|sold|described as)\b", "sentence that announces its point before making it (retired pattern 6)"),
]

# House-style preferences: on by default, switch off with --skip NAME.
HOUSE_RULES = [
    ("is-not-it-is", r"\b(?:is|are|was|were) not [^.,;]{3,50}, (?:it|they|we) (?:is|are|was|were)\b", "'is not X, it is Y' contrast"),
    ("em-dash", "\u2014", "em dash"),
    ("not-just", r"\bnot (?:just|only|merely)\b", "'not just/only' contrast"),
    ("x-not-y", r",\s+not\s+(?:a |an |the |about )?\w+", "'X, not Y' contrast"),
    ("n-nouns", r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten) [a-z]+, (?:one|two|three|four|five|six|seven|eight|nine|ten) [a-z]+", "'N nouns, N nouns' pairing"),
    ("stock-word", r"\b(?:leverag\w*|seamless\w*|empower\w*|unlock\w*|robust|actionable|data-driven|solutions?|holistic\w*|synerg\w*|journey|transform\w*|world-class|cutting-edge|next-generation)\b", "stock word from the default avoid list"),
    ("partner-verb", r"\bpartner(?:s|ed|ing)? (?:with|on)\b", "'partner' used as a verb"),
    ("spelling", r"\b(?:organis\w+|recognis\w+|personalis\w+|behaviour\w*|colour\w*|programme\w*|enquir\w+|afterwards|optimis\w+|prioritis\w+|analyse[sd]?|centre\w*)\b", "British spelling (default is American English; use --british to allow)"),
]

PARTICIPLE = re.compile(r",\s+(?:built|drawn|made|written|backed|chosen|given|designed|ordered|sourced|tested|based|kept)\b", re.I)
OFF_ON = re.compile(r"<!--\s*lint:off\s*-->[\s\S]*?<!--\s*lint:on\s*-->", re.I)


def load(path):
    text = open(path, encoding="utf-8").read()
    text = OFF_ON.sub(" ", text)
    if path.lower().endswith((".html", ".htm")):
        text = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", text)
        attrs = re.findall(r'\b(?:aria-label|alt|title|content)="([^"]{25,})"', text)
        attrs = [a for a in attrs if " " in a and not a.startswith(("http", "width="))]
        text = re.sub(r"</(p|li|h[1-6]|div|span|b|td|th)>", "\n", text)
        text = re.sub(r"<[^>]+>", " ", text)
        text = html.unescape(text + "\n" + "\n".join(html.unescape(a) for a in attrs))
    else:
        text = re.sub(r"\A---\n[\s\S]*?\n---\n", "", text)  # leading frontmatter
        text = re.sub(r"```[\s\S]*?```", "", text)           # code blocks
        text = re.sub(r"\]\([^)]*\)", "]", text)             # link addresses
    return text


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def snippet(text, m):
    a = max(0, m.start() - 45)
    b = min(len(text), m.end() + 45)
    return " ".join(text[a:b].split())


def sentences(raw):
    return [s for s in re.split(r"(?<=[.!?])\s+", raw.strip()) if s]


def check(path, rules):
    text = load(path)
    hits = 0
    print(f"\n== {path}")
    for name, pattern, why in rules:
        flags = 0 if name == "so-opener" else re.I
        for m in re.finditer(pattern, text, flags):
            hits += 1
            print(f"RULE  {name:<12} line {line_of(text, m.start()):<4} {why}\n      ...{snippet(text, m)}...")
    for raw in text.splitlines():
        for sent in sentences(raw):
            words = sent.split()
            if 0 < len(words) <= 9 and PARTICIPLE.search(sent):
                hits += 1
                print(f"RULE  fragment     short fragment with a trailing participle (retired pattern 1)\n      {sent}")
            elif 0 < len(words) <= 14 and PARTICIPLE.search(sent):
                print(f"CHECK fragment     possible fragment with a trailing participle (retired pattern 1)\n      {sent}")
    for raw in text.splitlines():
        sents = sentences(raw)
        run = 0
        for s in sents:
            run = run + 1 if len(s.split()) < 8 else 0
            if run == 3:
                print(f"CHECK choppy       three short sentences in a row\n      {raw.strip()[:140]}")
                break
        if any(len(s.split()) > 45 for s in sents):
            print(f"CHECK long         a sentence runs past 45 words\n      {raw.strip()[:140]}")
    return hits


def main():
    ap = argparse.ArgumentParser(description="Check copy against the humanize-content rules.")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--core-only", action="store_true", help="check only the six retired patterns")
    ap.add_argument("--skip", default="", help="comma-separated rule names to switch off")
    ap.add_argument("--british", action="store_true", help="allow British spellings")
    ap.add_argument("--list", action="store_true", help="list rule names and exit")
    args = ap.parse_args()

    rules = list(CORE_RULES) + ([] if args.core_only else list(HOUSE_RULES))
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}
    if args.british:
        skip.add("spelling")
    rules = [r for r in rules if r[0] not in skip]

    if args.list:
        for name, _, why in CORE_RULES + HOUSE_RULES:
            print(f"{name:<13} {why}")
        return 0
    if not args.files:
        ap.print_help()
        return 2
    total = sum(check(p, rules) for p in args.files)
    print(f"\n{total} RULE hit(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
