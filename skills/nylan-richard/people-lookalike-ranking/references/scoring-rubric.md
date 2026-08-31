# Similarity scoring rubric

Start with this 100-point model. Change weights only when the user names a different outcome-linked priority, and preserve a total of 100.

## Default weights

- Function and title family — 30 points.
  - 30: same function and equivalent scope.
  - 21: same function, adjacent title family.
  - 12: related function with plausible overlap.
  - 0: different function.
- Seniority and ownership — 25 points.
  - 25: same level and comparable ownership.
  - 13: one level away or ambiguous ownership.
  - 0: two or more levels away.
- Industry or business model — 20 points.
  - 20: same category and buyer context.
  - 10: adjacent category with similar operating motion.
  - 0: materially different context.
- Company size or stage — 15 points.
  - 15: same employee band or stage.
  - 9: adjacent band.
  - 3: far band but comparable role scope is evidenced.
- Geography — 10 points.
  - 10: same target market.
  - 7: same region or compatible timezone.
  - 3: outside target but not prohibited.

## Manual trajectory adjustment

Apply at most plus or minus 10 points after the base score. Valid reasons include a directly comparable promotion path, experience at the same company stage, or a role transition central to the user's success hypothesis. Write the reason beside the adjustment.

Never adjust for prestige, school, profile polish, demographic traits, or unsupported intent.

## Quality bands

- 75–100: strong analogue.
- 60–74: directional analogue; explain the gap.
- Below 60: do not include by default.

Always show `total = function + seniority + context + size + geography + trajectory adjustment`.
