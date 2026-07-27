---
name: "meta-capi-and-events"
title: "Meta Conversions API & events"
description: "Use this skill when wiring the Conversions API and funnel events — feeding MQL/SQL signal back so Meta optimizes for qualified pipeline, not form-fills."
category: Ads
---

# Meta Conversions API (CAPI) & Events - B2B SaaS

Best practices for sending conversion data to Meta via the Conversions API: event hierarchy, CRM vs middleware, deduplication, and Event Match Quality. Use this when setting up or auditing CAPI, choosing between HubSpot native and n8n, or improving event match quality.

---

## Best Option for B2B SaaS: CRM to CAPI (with Pixel)

- **Source of truth:** Your CRM (HubSpot, Salesforce, etc.).
- **Conversion events:** CRM **lifecycle stages** (Lead, MQL, Opportunity, Customer), not only a single "Lead" from the site.
- **Sending:** **Server-side** via Conversions API from the CRM (or from a system that has the same CRM data).
- **Redundancy:** Use **both** the Meta Pixel (browser) and CAPI (server) for the same conversion where possible, with **deduplication** so Meta counts it once.

This gives optimization on real pipeline (opportunity/customer), resilience to iOS/ad blockers, and a proper offline conversion loop: Meta lead to CRM to stage changes to CAPI back to Meta.

---

## Recommended Event Hierarchy (B2B SaaS)

| Event (example) | When to send | Why |
|-----------------|--------------|-----|
| Lead (or initial_lead) | Contact enters "Lead" / first form or demo | Top-of-funnel volume |
| marketingqualifiedlead | Contact becomes MQL | Qualified intent |
| opportunity | Deal/opportunity created | Pipeline; strong optimization target |
| customer | Closed-won | Revenue; best for value optimization |

Send **one CAPI event per lifecycle stage** you care about. Set **conversion event priority** in Events Manager so the event you optimize for (e.g. Lead or Opportunity) ranks above PageView and other events.

---

## Where to Send From: Best vs Second Best

| Option | When it's best |
|--------|-----------------|
| **CRM native (e.g. HubSpot to Meta)** | You want one place to manage sync. Data sharing (Email, Phone, Click ID) is on for all lifecycle events and Event Match Quality is acceptable (e.g. 6+/10). You only need Meta (and maybe other native integrations). No custom logic required. |
| **n8n (or similar) between CRM and Meta** | Event Match Quality stays low despite HubSpot data sharing. You need **normalize + hash per Meta's spec** (SHA-256, E.164 phone, etc.). You need to send to **multiple destinations** (Meta + LinkedIn, Google, Segment). You need **custom logic** (e.g. only send when deal value > X, or only for paid-source contacts). You want **one event_id** for pixel + CAPI and full control over deduplication. **Compliance:** you want to hash in middleware and never send plain PII. |

**Order of preference:** (1) Native HubSpot to Meta with Data sharing on for all events. (2) If match quality stays low or you need custom logic/multi-destination/hashing control, add **n8n** (or Segment, or custom backend): CRM to n8n to normalize + hash to CAPI.

---

## When n8n Is Better Than HubSpot Native

- **Low Event Match Quality** even with HubSpot data sharing on - n8n lets you normalize and hash exactly per Meta's spec.
- **Multiple destinations** - One workflow: HubSpot to n8n to Meta CAPI + LinkedIn, Google, etc.
- **Custom event mapping or filtering** - e.g. only send when deal value > X, or only contacts from paid campaigns.
- **Same event_id for pixel + CAPI** - Full control for deduplication when the pixel fires with a known event_id and you want CAPI to send the same one.
- **Compliance / data control** - Hash in n8n, filter by consent, suppress segments before sending.

---

## Deduplication: Where It Happens

- **Where:** In **Meta's systems**. You don't configure dedup in HubSpot or n8n; you send the right identifiers.
- **How:** Send the **same `event_id`** (and same `event_name`) from both the **pixel** (e.g. on thank-you page) and **CAPI** (from CRM or n8n when that conversion is recorded). Meta merges them into one conversion.
- If the conversion **only** exists in the CRM (e.g. "became Opportunity" days later), you only send CAPI - no pixel event to dedupe with.

---

## Event Match Quality (EMQ)

- Send **user_data** with every CAPI event: at least **email** and **phone** (normalized, then hashed per Meta's rules). Optionally: first name, last name, city, state, zip, country, **external_id** (your CRM ID, hashed).
- **HubSpot:** Use "Data sharing" and select Email, Phone, Click ID (and any other recommended fields) for **all** lifecycle events.
- **n8n:** Use normalize + hash (Crypto node or Code node with `crypto.createHash('sha256').update(str).digest('hex')`) so every event includes hashed `em`, `ph`, etc. Meta expects **hex** (lowercase).
- Check **Event Match Quality** in Events Manager; aim for 6+/10 or "Good." Low scores (e.g. 3.2-3.8) mean Meta can't match well - improve user_data or add hashing via n8n.

---

## Meta CAPI Best Practices (Summary)

- **Pixel + CAPI** for the same events (redundant setup).
- **Deduplication:** same `event_name` + `event_id` (or `external_id` + `fbp`) from pixel and CAPI.
- **Parameters:** Send required (e.g. `action_source`, `event_source_url`, `client_user_agent` for web) and recommended **customer information** (em, ph, fn, ln, etc.) - hashed where required.
- **Real time:** Send events as soon as the stage changes (or at least daily).
- **Test:** Use Meta's Test Events tool and Payload Helper to validate.
- **Post-setup:** Check Event Match Quality; avoid changing pixels or campaign structure unnecessarily during learning.

---

## Related Files

- **meta-setup-and-tracking.md** - Pixel, events, domain verification, first campaign
- **audience-strategy.md** - Prospecting audiences, data hierarchy
- **campaign-structure.md** - Remarketing vs prospecting, ABO/CBO/Advantage+
- **optimization-playbook.md** - Decision trees, weekly cadence, scaling protocol
