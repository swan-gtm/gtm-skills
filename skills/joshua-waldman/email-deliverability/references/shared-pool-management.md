# Shared Pool Management & Compliance

How to manage shared IP pools, detect contaminating senders, and handle high-risk verticals — ESP-level deliverability management, learned at the scale of millions of messages a day.

---

## The Core Problem

"Everything you have is connected in some kind of way and a problem in any one area can bleed over onto the whole if you don't address it, because mailbox providers and spam filters will just keep increasing their scrutiny and the amount of your mail that they filter. Until they ultimately decide — well, I'm spamming most of this and you keep sending, so I'm just gonna block it."

---

## Diagnosing Shared Pool Issues

### Step 1: Scale Assessment
Ask: "What percentage of the ESP's infrastructure is getting hit and having problems, by weight?"
- If a minority percentage of IPs are affected → probably isolated bad sender(s)
- If double digits → "there's a pretty serious problem, likely it's all gonna come down to the customers that you're sending on your network"

### Step 2: Shared vs. Dedicated Analysis
"Is it mostly your shared IPs that are getting blocked or is it mostly your dedicated IPs that are getting blocked?"
- **Shared IPs blocked** → Pool contamination. One or more senders are dragging down the pool.
- **Dedicated IPs blocked** → Look for commonalities: "Are they in the same industry vertical? Maybe there's just a lot of risk around that industry vertical and you need to vet customers in that industry a bit more stringently."

### Step 3: Find the Contaminator
Build visibility into which clients generate the highest block rates:
- "You would want a really robust system that would allow us to see which clients are getting the highest block rates. Where are those clients blocked?"
- Cross-reference block patterns with customer sending behavior
- Check if any customer connected servers outside the approved warmup protocol
- Look for HELO/rDNS mismatches on recently added IPs

### Step 4: Assess Cascade Risk
One misconfigured customer can melt down the entire infrastructure:
- Example: Client connected to new server outside of warmup protocol. The SMTP HELO announcement didn't match the IP's reverse DNS → automatic SpamHaus listing → "started causing everything we were doing to melt down"
- Cascade principle: Filters increase scrutiny incrementally → filtering more mail → eventually blocking entirely

---

## Building Compliance Rails

The operating rule: "Having as many compliance checks as possible built into your system as well as the ability to view ongoing compliance checks for your team and take action in the system when there looks to be a sustained issue."

### On Intake (New Customer Onboarding)
1. **Validate data on import** — Run list hygiene automatically. "When you move onto a new ESP, I want to validate your data just because mistakes happen."
2. **Sample and risk-evaluate** — "Maybe even sampling some portion of that and throwing it at a tool that can evaluate the risk of that data."
3. **Check domain age** — Domains under 90 days old need special warmup handling.
4. **Verify authentication setup** — SPF, DKIM, DMARC records must be in place before first send.
5. **Industry vertical assessment** — Flag high-risk verticals for additional review.

### Ongoing Monitoring
1. **Bounce rate monitoring** — "Why would your ESP let you bounce five thousand or fifty thousand messages when they could look at a sample of like a hundred or five hundred and go, you know what, I'm pulling the plug?"
2. **Open rate tracking** — Below 10% = intervene. "I've seen ESPs let customers persist with two to four percent open rates, bad domain reputation... they don't want to risk the contract."
3. **Complaint rate alerts** — Automated intervention at threshold.
4. **Block detection** — Real-time visibility into which IPs are blocked where.
5. **Provider outage detection** — "If everybody starts getting blocked at Microsoft because it went down again, we should pause sending and not just bounce a gazillion emails off of Microsoft's infrastructure."

### Automated Intervention
All of this should be automated, not manual:
- "Frankly, all this can be automated. Don't need a person to reach out to the customer. You can shoot them an email."
- Trigger automated alerts at first sign of problems
- Suspend sending automatically when bounce patterns indicate issues
- Resume requires human review of root cause

---

## High-Risk Vertical Management

### Verticals That Get Blanket-Banned at Many ESPs
- Crypto/cryptocurrency
- Casino/iGaming
- Adult content
- Political content

### The Better Approach: Enhanced Vetting, Not Blanket Bans
"There are also plenty of legitimate senders in many of those industries."

Instead of rejecting outright: "We're not gonna say no, but you definitely have to go for some kind of additional questioning."

### Enhanced Vetting Process
1. Additional questionnaire about sending practices
2. Review of content samples
3. List source verification
4. Volume and frequency expectations
5. Explicit agreement to aggressive sunsetting policies

### Casino/iGaming Specific Requirements
- Aggressive sunsetting: suppress after 3-5 unopened emails (not standard 90-180 day window)
- Spread monthly newsletters across the month (no single-day spikes)
- May need dedicated IP allocation to isolate from shared pool
- "With the right sending strategy, you can be successful"

---

## ESP Accountability

A frustration with the industry:

"What I've seen in the industry ecosystem is ESPs avoiding responsibility like it's the plague. Even when the customer is like, yo, I know this is my fault, but can you help me?"

The healthy approach:
- **Don't hide problems** — "It's unconscionable to me. I've seen ESPs let customers send millions of emails into the spam folder when they absolutely had the intelligence to tell their customer, this is not working."
- **Alert early** — "They're just delaying the pain. It's gonna blow up later when someone realizes they paid you thousands or tens of thousands, even hundreds of thousands of dollars to get literally no traction."
- **Own the infrastructure** — The ESP controls the MTA. Use that control to protect all senders on the platform.
- **Make it a win-win-win** — "The customer is happy. Your infrastructure is not gonna get as damaged. The customer is gonna get a timely alert about a potential cybersecurity issue."

---

## When to Fire a Customer

There's a line between helping a struggling sender and letting a bad actor damage your infrastructure:

- Persistent violation of sending policies after warnings
- Refusal to implement list hygiene or engagement segmentation
- Sending to purchased lists repeatedly
- Content that consistently fails compliance checks
- Business model that inherently requires spammy practices

The "ice skating uphill" test: If their business model requires practices that will always trigger spam filters, they probably won't succeed on your platform regardless of how much you help them. Better to part ways than let them contaminate shared infrastructure.
