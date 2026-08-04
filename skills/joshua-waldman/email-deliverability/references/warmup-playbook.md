# Warmup & Reputation Recovery Playbook

The step-by-step process for warming up new senders or recovering damaged sender reputation, built from managing IP pools that process 10-18 million messages a day. Follow it exactly — the order matters.

---

## When to Use This Playbook

- New domain or IP needs warming before production sending
- Sender has been blocklisted and needs reputation recovery
- Open rates have cratered (below 10%) and domain reputation is damaged
- Migrating from another ESP and need to establish reputation on new infrastructure

---

## Phase 1: The Pause (Week 1)

**Do NOT send bulk email. Do NOT do nothing.**

This week is for data analysis and preparation. The rule is emphatic: "Don't do nothing during that week. During that week, it's generally spent on data analysis."

### Step 1: Assess Current State
- Pull current open rates by mailbox provider (Gmail, Microsoft, Yahoo, iCloud, ProofPoint)
- Check domain reputation in Google Postmaster Tools
- Run SpamHaus check on all sending domains and IPs
- Check all authentication records (SPF, DKIM, DMARC) are present and valid
- Verify HELO/reverse DNS match on every IP

### Step 2: Analyze Historical Performance
- **For promotional senders:** Identify the best-performing offers. "What are the best offers that you've sent?"
- **For newsletter senders:** Identify the most engaging topics. "What are the most salient topics that your audience likes?"
- Goal: Have a strong piece of content ready to launch when sending resumes.

### Step 3: Segment the Audience
Build these segments from most to least engaged:

1. **Recently signed up** — Opted in within the last 30 days. Highest natural engagement.
2. **Super fans** — Your most email-engaged subscribers. "Every brand has their super fans. They love the interaction. They love it when you send them email."
3. **Regular engaged** — Opened or clicked within the last 90 days.
4. **Lightly engaged** — Opened within the last 180 days.
5. **Inactive** — No engagement in 180+ days. These come last, if at all.

### Step 4: Segment by Mailbox Provider
Within each engagement tier, create sub-segments by mailbox provider:
- Gmail
- Microsoft (Outlook/Hotmail)
- Yahoo
- iCloud/Apple
- ProofPoint-filtered domains
- Other

**Start your warmup with Gmail contacts who have engaged with an email in the last 90 days.** Gmail is the largest provider and provides the clearest reputation signals via Google Postmaster Tools. Starting with recently engaged Gmail contacts gives you the highest chance of strong initial engagement, which builds positive domain reputation that carries over when you expand to other providers.

Real-world example: "I did a warmup on Klaviyo a while back. I ended up having to manage eight segments because they had a substantial consumer and B2B audience... seven material buckets of mailbox provider and spam filter plus the other category."

### Step 5: Validate the Data
- Run list hygiene on the entire list
- Remove hard bounces, soft bounces from previous ESP
- Sample and evaluate data risk with validation tools
- Check for spam trap indicators (custom-hosted domains on their own nameservers with 5-letter names)

"When you move onto a new ESP, I want to validate your data just because mistakes happen. Data sets — bounces sometimes will remain in the list."

---

## Phase 2: The Ramp (Weeks 2-6+)

### Starting Volumes by Provider (Reputation Recovery)
When restarting from severely damaged reputation:

| Provider | Day 1 Volume | Ramp Rule |
|----------|-------------|-----------|
| Microsoft | 25 emails | Never send more than 4x previous day's opens |
| Yahoo | 50 emails | Never send more than 4x previous day's opens |
| Gmail | 200 emails | Never send more than 4x previous day's opens |
| iCloud | 50 emails | Fixed schedule, not the 4x rule — MPP inflates opens here. Under 10% open rate at iCloud = severe issue |

### Starting Volumes (New Domain/IP Warmup)
When warming from scratch (not damaged, just new):

- **Days 1-7:** Send only automated/transactional volume (a few hundred per day)
- **Week 2:** Begin blending in engaged audience segments
- **Week 3+:** Gradually introduce less engaged segments
- **Target timeline:** 1-2 months to reach 100K/day (depends on audience engagement quality)

### New Domain Requirements
- New domains need a **90-day aging period** before heavy sending use
- Consider aftermarket domains that already have age — they cost $1-200 depending on keywords
- Look for domains with keywords relevant to the brand (e.g., "blitz" and "games" for a gaming company)
- Even aged domains need sending warmup — domain age helps but isn't sufficient alone

### Daily Management During Ramp

Each day during the warmup:

1. Check yesterday's metrics by provider segment
2. Identify who opened/clicked (these people are "done" for this campaign cycle)
3. Update segments: remove already-mailed contacts, add next batch
4. Send to the next day's segment — only people who haven't received this campaign yet
5. Monitor bounce rates, complaint rates, and inbox placement
6. If any provider shows warning signs, reduce volume or pause for that provider

The manual process: "Literally update those every day and say okay, well today I sent to the last one to three days of engaged people at ProofPoint, Microsoft, Gmail, Hotmail, whatever."

### Automated Warmup (When Available)
With proper tooling, you can load the full weekly segment and let the system manage distribution: "Load up a whole 10,000 segment and just let our warmup schedule run it all out of that one campaign without you having to really do a lot about it. Other than watch it and check the metrics."

---

## Phase 3: Steady State

### When to Declare Victory
- Open rates consistently above 20% across providers
- Domain reputation "High" in Google Postmaster Tools
- No active blocklist entries
- Soft bounce rate under 0.5%
- Complaint rate under 0.1%

### Ongoing Monitoring
- Check domain/IP reputation weekly
- Monitor open rate trends (direction matters more than absolute number)
- Watch for provider-specific drops (one provider declining while others hold = provider-specific issue)
- Validate new list imports before sending
- Maintain engagement-based suppression (sunset inactive contacts)

### For Casino/iGaming Clients
More aggressive sunsetting required:
- Suppress users after 3-5 unopened emails (not the standard 90-180 day window)
- Monthly newsletter sends should be spread across the month, not spiked on one day
- Large campaigns can be spread across 3-4 days rather than a single send

---

## Content Strategy During Warmup

### Best Practice: Identical Content Approach
Send the same newsletter content to both engaged AND disengaged audiences:
- Engaged audience sends first → builds positive content reputation
- Same content then reaches disengaged users → benefits from the positive reputation already established
- This is more effective than sending different content to different segments

### Launch Content
- Use your strongest-performing content type for the first send
- Ensure perfect branding, clean HTML, proper images
- Include plain text version
- Keep links minimal
- Avoid trigger words (URGENT, ACTION REQUIRED, etc.)

### Transactional Email First
If warming a completely new domain:
- Start with automated/transactional emails (OTP codes, order confirmations)
- These have fewer links and higher natural engagement
- Build initial reputation before adding marketing volume

---

## Setting Client Expectations

How to set expectations honestly:

**On the pause:** "Not going to be a lot of volume going out. It's really going to be curated sends to small segments."

**On timeline:** Reputation recovery takes weeks to months, not days. "You just got to let that kind of rest for a little bit."

**On the upside:** "If you're fully inboxing, you're going to be getting 10X that kind of engagement." Frame the pause as an investment, not a loss.

**On list cuts:** "It's truly not the size. It's how it performs and how much money it makes you." Be prepared to cut 10-20% of a list for quality.

**On the long game:** "For me, email is about the long game, not the short game. Yes, there are short-term things you need to do in the interim to keep everything afloat, but really keeping your email reputation high is part of building a sustainable business."
