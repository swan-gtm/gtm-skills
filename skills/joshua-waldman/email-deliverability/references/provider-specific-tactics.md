# Provider-Specific Tactics

How to diagnose and fix deliverability issues at each major mailbox provider and spam filter, based on experience managing large-scale sending operations.

---

## Gmail

### How Gmail Thinks
Gmail uses correlation-based filtering — it connects multiple data points to identify coordinated operations. It's not just looking at one signal; it's looking for patterns.

**Gmail's strategy:** "Make it unprofitable, not impossible." They don't block everything outright — they make spamming so costly in terms of blocked mail and wasted resources that legitimate senders optimize while bad actors give up.

### Correlation Points Gmail Watches
- Physical business addresses shared across domains
- Web hosting IPs shared across "different" brands
- Similar domain naming patterns
- Sender identity mismatches (display name vs. email address)
- Similar or identical content sent from different domains
- Lack of consistent branding across sends

### Gmail-Specific Warmup
- Start at ~200 emails/day for campaigns
- Never exceed 4x previous day's opens
- Domain reputation in Google Postmaster Tools is your primary signal
- Reputation levels: High → Medium → Low → Bad
- Moving from Low to High takes weeks of consistent positive signals

### Gmail-Specific Fixes
- **Content filtering:** Address all correlation points. If multiple domains share infrastructure markers, Gmail treats them as one sender.
- **Domain reputation "Bad":** Full warmup restart needed. Consider whether the domain is recoverable or if starting fresh is more practical.
- **Low engagement:** Gmail heavily weights engagement. Sending to inactive subscribers actively damages your reputation there.

---

## Microsoft (Outlook / Hotmail)

### How Microsoft Differs
Microsoft tends to be more aggressive with blocking than Gmail. Where Gmail might spam-folder your emails, Microsoft might outright reject them.

### Microsoft-Specific Warmup
- Start very low: 25 emails/day when recovering from damaged reputation
- Never exceed 4x previous day's opens
- Microsoft separates Outlook.com and Hotmail — track both independently
- Recovery is often slower at Microsoft than Gmail

### Microsoft-Specific Issues
- **Outages affect senders:** Microsoft's own outages can cause mass bounces. The ESP should detect this and pause sending: "If everybody starts getting blocked at Microsoft because it went down again, we should pause sending and not just bounce a gazillion emails off of Microsoft's infrastructure."
- **Aggressive gray-listing:** Microsoft uses gray-listing (code 400 soft bounces) extensively. Legitimate senders retry and get through; spammers don't. Understanding this behavior is critical — it inflates apparent soft bounce rates for legitimate senders. Never treat graylisted soft bounces as a dirty list: retry them, and only treat what still fails after three attempts across 72 hours as a hard bounce. Suppressing on the first soft bounce at Microsoft deletes valid, reachable addresses.

### Microsoft-Specific Fixes
- When Microsoft blocks: 48-hour pause from that IP, then restart at minimal volume
- New IP may be preferable to rehabilitating a blocked one
- Track Hotmail and Outlook.com as separate segments during warmup

---

## Yahoo

### How Yahoo Differs
Yahoo is generally more forgiving than Gmail or Microsoft. Good news: easier to recover. Bad news: people sometimes use Yahoo success as false confidence about overall deliverability.

### Yahoo-Specific Warmup
- Start at ~50 emails/day when recovering
- Never exceed 4x previous day's opens
- Yahoo performance recovering doesn't mean Gmail performance is fine

### Yahoo-Specific Tactics
- Yahoo's engagement weighting is lighter than Gmail's
- Still important to segment by engagement, but Yahoo gives more room for recovery
- Watch for Yahoo-specific spam folder placement vs. blocks — they behave differently

---

## iCloud / Apple Mail

### The iCloud Signal
iCloud/Apple Mail open rates below 10% indicate severe inbox placement problems. Because Apple Mail Privacy Protection inflates open rates, genuinely low iCloud opens mean almost nothing is being delivered to inbox.

### iCloud-Specific Considerations
- Apple MPP (Mail Privacy Protection) pre-fetches images, which inflates open rate numbers
- If you're seeing sub-10% opens at iCloud despite MPP inflation, the actual engagement is dramatically worse
- iCloud placement is heavily reputation-dependent
- Do not use the 4x-opens ramp here — MPP inflation makes it unsafe. Use a fixed daily schedule and watch bounces and delivery instead
- Recovery approach follows the standard warmup playbook but with extra attention to engagement quality

---

## ProofPoint

### How ProofPoint Works
ProofPoint is a corporate spam filter (not a mailbox provider). It protects enterprise email systems — so when you're sending to business addresses at companies using ProofPoint, different rules apply.

### ProofPoint-Specific Issues
- **Sending rate sensitivity:** "The rate at which they were sending for one customer into the ProofPoint spam filter was not working. It was generating huge numbers of soft bounces."
- **IP-level blocking:** ProofPoint blocks at the IP level. Getting delisted requires contacting ProofPoint directly.
- **Throttling requirement:** The ESP's MTA must throttle sending rate to ProofPoint-filtered domains. Sending too fast = automatic soft bounces.

### ProofPoint-Specific Fixes
- Get the IP delisted from ProofPoint's blocklist directly
- Implement MTA-level throttling for ProofPoint-filtered domains
- Reduce sending volume to ProofPoint destinations during recovery
- ProofPoint soft bounces are often rate-related, not reputation-related — distinguish between the two

---

## SpamHaus

### What SpamHaus Does
SpamHaus maintains blocklists that many mailbox providers and spam filters reference. A SpamHaus listing can cascade across multiple providers simultaneously.

### Automatic SpamHaus Listing Triggers
- **HELO/rDNS mismatch:** "If the HELO, the server announcement that comes through the SMTP connection, doesn't match the IP's reverse DNS — that is an automatic SpamHaus listing. If you hit enough networks with it."
- **Spam trap hits:** Sending to SpamHaus-maintained spam traps
- **High complaint rates:** Excessive spam reports from multiple sources

### SpamHaus Diagnosis
Use the free SpamHaus domain reputation checker to check:
- Negative reputation scores
- Infrastructure quality assessment
- Domain creation dates (new domains are higher risk)
- Whether multiple domains share the same IP address

### SpamHaus Delisting
- Fix the root cause first — delisting without fixing the cause results in re-listing
- Submit delisting request through SpamHaus portal
- Provide evidence of remediation steps taken
- Monitor closely after delisting — re-listing happens fast if the problem recurs

---

## Cross-Provider Strategy

### The Segment-by-Provider Approach
During any warmup or recovery, segment sending by mailbox provider. Each provider has different:
- Rate tolerances
- Engagement weighting
- Block vs. spam-folder behavior
- Recovery timelines

Real-world example of segment management during warmup:
"I literally one time had to create eight separate segments for the different mailbox providers and spam filters and then literally update those every day and say okay, well today I sent to the last one to three days of engaged people at ProofPoint, Microsoft, Gmail, Hotmail, whatever."

### Reading Provider Signals Together
- **All providers declining:** Likely a content or data quality issue
- **One provider declining, others stable:** Provider-specific throttling or reputation issue
- **Sudden drops everywhere:** Authentication failure, DNS change, or SpamHaus listing
- **Gradual decline:** Engagement erosion — probably sending to too many inactive contacts

### The 4x Rule
Where opens are trustworthy: "Never send more than 4x previous day's opens."

If you sent 100 emails yesterday and got 25 opens, today's maximum is 100 emails (4x25). This prevents over-sending to unengaged audiences and naturally scales volume as engagement improves.

**The Apple exception.** Do not ramp on this rule at iCloud or Apple Mail. Mail Privacy Protection pre-fetches images, so a large share of those opens are machines, not people. Multiplying an inflated number authorizes volume no human asked for. Ramp Apple on a fixed schedule instead, and judge it on delivery and bounce behavior. The same caution applies anywhere else opens are proxied or prefetched.
