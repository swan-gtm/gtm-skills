# Setup and customization checklist

## Placeholders

- [ ] `{{PRODUCT}}`
- [ ] `{{CALL_NOTES}}`: the agent can read recent call notes or transcripts for a named account.
- [ ] `{{USAGE_SOURCE}}` and `{{USAGE_UNIT}}`: the agent can see plan, usage, top-ups and recent in-product activity per account.
- [ ] `{{ACCOUNT_OWNER}}` and `{{OWNER_ALERT_CHANNEL}}`.
- [ ] `{{NO_REPLY_DAYS}}` (default 10).

## Decisions to make

- [ ] **What counts as "quick succession"** for play 1 (for example, two or more top-ups in 60 days).
- [ ] **What counts as "low value realized"** for play 5, and how the confirmation check is done.
- [ ] **Your commercial options** for play 3: annual terms, custom plans, volume pricing.
- [ ] **Approval.** Every message is queued for the account owner to approve. Do not enable automatic sending for these plays.

## Behaviour that should not change

- Paying customers only; trials and win-backs use other plays.
- The hook is always the customer's own usage or words.
- One sequence per contact.
- The last step is an internal alert, never another pitch.
- Nothing reaches a customer executive without the owner's sign-off.
