# Setup and customization checklist

Work through this before the first run.

## Placeholders

- [ ] `{{BILLING_SOURCE}}`: you can pull every active paid subscription with plan, price, included usage and remaining usage. If remaining usage is not stored, decide how burn is computed (usage logs, or a weekly snapshot).
- [ ] `{{CRM}}` and `{{CLOSED_WON_STAGE}}`: the stage or lifecycle value that means "paying customer".
- [ ] `{{TIER_TAGS}}` and `{{ACV_TAGS}}`: the scan depends on accounts already carrying a tier and an ACV tag. If they do not, run your account scoring first. Untagged accounts are excluded or score zero.
- [ ] `{{USAGE_UNIT}}` and `{{PLAN_LADDER}}`: list each plan with its monthly price and included usage, so burn and the recommended upgrade can be computed.
- [ ] `{{SCALE_PRICE}}`: the plan price a mature customer should sit on.
- [ ] `{{EXPANSION_TARGETS_FILE}}` (optional): one row per account with expansion angle, category and status.
- [ ] `{{DIGEST_CHANNEL}}`, `{{ERROR_CHANNEL}}`, `{{EXPANSION_OWNER}}`.

## Decisions to make

- [ ] **Price-gap bands.** The defaults ($250 / $500 / $750 / $1,200) assume a scale plan around $1,200 a month. Rescale them proportionally to your own ladder.
- [ ] **Headcount bands.** Defaults: 200+ and 75 to 199 employees against $750 a month or less. Move them if your price-per-employee expectations differ.
- [ ] **Which tiers are scanned.** Default: the top two only. Widening it makes the digest longer and noisier.
- [ ] **"Already in motion" statuses** that exclude an account from the digest.
- [ ] **Digest size.** Default: top 25 scored, 20 posted at most.
- [ ] **Run day.** Default: Monday morning, so the week's work is set.

## Behaviour that should not change

- Only paying, closed-won accounts in the top tiers are scanned.
- Accounts already in an upgrade conversation are skipped.
- Missing data is stated, never guessed.
- The digest never sends outreach; it suggests it.
- If a data pull fails, the run stops and reports the error rather than posting a partial digest.
