# Deliverability gate (gate 4)

The sending infrastructure gate runs per mailbox, because one failing mailbox can drag its whole domain into spam folders, and a campaign-level average hides it.

## Authentication

A published record proves nothing until sent mail passes it. Check both.

- [ ] **SPF:** exactly one record beginning `v=spf1`, including the mailbox provider, within 10 DNS lookups counted recursively (the protocol limit; past it, receivers treat SPF as failed).
- [ ] **DKIM:** a record at the provider's selector with a non-empty public key.
- [ ] **DMARC:** a record beginning `v=DMARC1` with a valid policy.
- [ ] **MX:** records that resolve.
- [ ] **Sent-mail proof:** one seed message per sending mailbox to an inbox you control. The message headers show SPF, DKIM and DMARC passing with aligned domains. Record it as N of N mailboxes passing.

When a sending platform shows a generic "bad DNS" badge, open the mailbox's technical panel and name the failing line. A missing custom tracking domain matters only if open or click tracking is on; a failing SPF, DKIM, DMARC, MX or blacklist line always blocks.

## Mailbox settings

- [ ] Daily cap at or below the mailbox provider's stated ceiling. Providers that sell dedicated cold-email mailboxes publish one, and exceeding it burns the mailbox. Read the provider before raising any limit.
- [ ] Campaign daily cap no higher than the per-mailbox cap times the number of mailboxes.
- [ ] Warm-up on and not paused, at a volume at least equal to cold sends.
- [ ] Gradual ramp and daily send variance on.
- [ ] Every value read back from the interface after saving. Settings panels drop clicks; a mailbox left at the old value looks identical in a list view.

## Schedule

- [ ] Weekdays only, business hours in the recipient's time zone, a fallback time zone for unknowns, public holidays skipped.
- [ ] Sending interval spread across the window.
- [ ] Open and click tracking off; reply tracking on. Tracking pixels and rewritten links are among the first things filters weigh.

## Content checks that belong to infrastructure

- [ ] Step 1 is plain text: no HTML part, no links, no images. Verify by sending it to a seed inbox and reading the raw original.
- [ ] Signatures are minimal: name, title, company. No links, phone numbers, images or license numbers. A shared signature element can get every message from the domain blocked.
- [ ] The rendered text of every variant, opt-out line included, passes a spam-word check with zero hits.
- [ ] The greeting and opening line vary across rendered previews, so no two recipients get byte-identical openers.
- [ ] More than one live campaign runs across each mailbox group, so a filter that blocks one piece of copy does not stop the group.

## What blocks, what warns

| Finding | Verdict |
|---|---|
| Any authentication line failing on sent mail | Hold |
| Mailbox disconnected, errored or warm-up failed | Hold that mailbox; launch on the rest only if the cap math still holds |
| Cap above provider ceiling | Hold until lowered and read back |
| Tracking on without a custom tracking domain | Hold, or turn tracking off |
| Single live campaign per mailbox group | Warn; record who accepted it |
| Spam-word hits in rendered copy | Hold until rewritten and rechecked |
