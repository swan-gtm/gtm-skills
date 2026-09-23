#!/usr/bin/env python3
"""Copy the plan template and fill V1 slots without retyping 70KB.

usage: python3 scripts/fill.py references/plan-template.html out/plan.html KEY=value KEY2=value ...
       add --claude to emit only the HEAD/BODY ranges (Claude artifact adapter).
Unfilled {{SLOTS}} are left as-is and listed on stderr so you can Edit them.
"""
import sys, re, html
src, dst, *kv = sys.argv[1:]
claude = "--claude" in kv; kv = [a for a in kv if a != "--claude"]
s = open(src, encoding="utf-8").read()
for a in kv:
    k, _, v = a.partition("=")
    if k.startswith("START_"):
        if not v.isdigit(): sys.exit(f"{k} must be an integer, got {v!r}")
    else:
        v = html.escape(v, quote=False)
    s = s.replace("{{" + k + "}}", v)
if claude:
    mh = re.search(r"<!-- HEAD:start.*?-->\n(.*?)<!-- HEAD:end -->", s, re.S)
    mb = re.search(r"<!-- BODY:start -->\n(.*?)<!-- BODY:end -->", s, re.S)
    if not (mh and mb): sys.exit("template is missing HEAD/BODY range markers")
    s = mh.group(1) + mb.group(1)
open(dst, "w", encoding="utf-8").write(s)
left = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", s)))
print(f"wrote {dst}; unfilled: {' '.join(left) or 'none'}", file=sys.stderr)
