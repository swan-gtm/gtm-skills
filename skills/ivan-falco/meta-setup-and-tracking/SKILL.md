---
name: "meta-setup-and-tracking"
title: "Meta Ads setup & tracking"
description: "Use this skill when setting up Meta ads tracking — pixel, events, domains, and the implementation checklist for a clean B2B measurement base."
category: Ads
---

# Meta Ads Setup & Tracking - Implementation Guide

Step-by-step setup to run your first B2B campaign on Meta. Use this when you already have access and need to configure tracking, then launch. For campaign strategy (audience hierarchy, ABO vs CBO, creative), see the other knowledge-base files.

## Where Things Live in Meta

| What you need | Where to go |
|---------------|-------------|
| Pixel, events, data sources | **Events Manager** (Ads Manager → left menu → All Tools → Events Manager) |
| Create and run campaigns | **Ads Manager** (campaigns, ad sets, ads) |
| Domain verification, Business assets | **Business Settings** (Business Suite or business.facebook.com → Settings) |
| Lead Gen Forms | Created when you build an ad with the **Leads** objective; form settings live in the ad set/ad flow |

---

## 1. Create and Install the Meta Pixel

### 1.1 Create the pixel (if you don't have one)

1. **Events Manager** → Data Sources → **Add new data source** → **Website** → **Connect**.
2. Choose **Meta Pixel** → name it (e.g. "[Business] - Main Website") → **Create Pixel**.
3. Note your **Pixel ID** (shown in the pixel details). You'll use it in the base code or in tag managers.

### 1.2 Install the pixel on the website

You need the **base pixel code** on every page (or at least all pages you care about for traffic and conversions). Options:

**Option A: Manual install**

- Events Manager → your Pixel → **Set up** (or **Continue set up**) → **Install code manually**.
- Copy the base code snippet (the `fbq('init', 'XXXX')` and `fbq('track', 'PageView')` block).
- Add it to the `<head>` of every page, or to a global header/footer template. Do not add it only to the thank-you page.

**Option B: Google Tag Manager (recommended if you use GTM)**

- Events Manager → **Set up** → **Use a partner** → choose **Google Tag Manager** and follow the steps.
- In GTM: create a Custom HTML tag with the base pixel code, set it to fire on All Pages (or appropriate triggers). Publish the container.

**Option C: CMS or partner integration**

- If your site is on WordPress, Shopify, Webflow, etc., use Events Manager → **Set up** → **Use a partner** and pick the platform. Follow the in-product steps.

### 1.3 Verify the pixel is firing

- **Events Manager** → your Pixel → **Test events** (or use the **Test Events** tool).
- Open your website in another tab (or use the built-in test URL). You should see **PageView** (and any other events you've set) in the event list within a few seconds.
- Alternatively, install the **Meta Pixel Helper** browser extension and load your site; it should show the pixel and events.

Until the base code is on the site and firing, don't rely on Meta for conversion optimization or remarketing.

**Pro tip:** Pay two freelancers $20 each to independently verify your pixel and events are tracking properly. $40 is cheap insurance against burning thousands optimizing on broken tracking. Even experienced media buyers miss technical setup issues.

---

## 2. Set Up Conversion Events

The pixel base code sends PageView by default. For lead-gen and B2B, you need **conversion events** so Meta can optimize and report.

### 2.1 Which events to use

- **Lead** - Form submit, demo request, "contact us," lead gen form submit, etc.
- **CompleteRegistration** - Sign-up, account creation, webinar registration (if you treat that as a key conversion).

Set the event to fire when the action **actually completes** (e.g. after form validation, on the thank-you page or success callback), not on button click.

### 2.2 Adding events

**From Events Manager (recommended for clarity):**

- Pixel → **Set up** → **Set up events** → **Use a partner** (e.g. GTM) or **Install events manually**.
- For manual: add a second snippet where the conversion happens, e.g. `fbq('track', 'Lead');` on thank-you page or in form success handler.

**In GTM:**

- One tag per event (e.g. Lead, CompleteRegistration). Use Custom HTML with `fbq('track', 'Lead');` and trigger on the thank-you page URL or a form submission trigger.

**With Meta Lead Gen Forms:**

- When you choose the **Leads** objective and use an in-platform lead form, Meta can track the lead event automatically. You still want the pixel on the rest of the site for remarketing and for any landing-page conversions.

### 2.3 Event prioritization (if multiple events fire on the same page)

- **Events Manager** → Pixel → **Settings** → **Conversions** (or event configuration).
- Set the **order of priority** so the event you optimize for (e.g. Lead) is higher than PageView or other lower-funnel events. Meta uses this for optimization and attribution.

---

## 3. Domain Verification

Required for reliable conversion matching, some advanced features, and controlling how your links appear. Do this for every root domain you use in ads (landing pages, lead form thank-you, etc.).

1. **Business Settings** → **Brand Safety** → **Domains** → **Add** → enter the domain (e.g. `yourcompany.com`).
2. Choose **one** verification method:
   - **DNS (TXT record)** - Add the TXT record at your DNS host; then in Meta click **Verify**.
   - **Meta tag in `<head>`** - Add the meta tag to the homepage `<head>`; then **Verify**.
   - **HTML file upload** - Download the file, upload to the site root, then **Verify**.

Verification can take a few minutes to 72 hours depending on DNS propagation. Verify before scaling spend.

---

## 4. Conversions API (CAPI) - Optional but Recommended for B2B

Browser blockers and privacy features can block or delay pixel events. **Conversions API** sends the same events from your server to Meta, so you get more complete and reliable data.

- **When to set up:** After the pixel is installed and key events are firing. Especially valuable when you see a gap between CRM leads and Meta-reported conversions.
- **Where:** Events Manager → your Pixel → **Settings** → **Conversions API** (or Data Source settings). You'll need an **Access Token** and (depending on method) a partner integration or custom server setup.
- **Deduplication:** Use the same `event_id` for the pixel and CAPI versions of the same event so Meta can deduplicate. Many partners and Meta's own code do this automatically.

If you're not ready to implement CAPI, you can launch with pixel-only and add CAPI later.

---

## 5. Audiences You Need Before the First Campaign

- **Remarketing (start here):**
  **Audiences** (Ads Manager or Business Settings) → **Create audience** → **Custom Audience** → **Website traffic**. Create segments for 30-day, 90-day, and optionally 180-day visitors. Requires the pixel installed and firing.
- **Exclusions:** Create a Custom Audience of employees (and optionally competitors) and **exclude** it from prospecting (and optionally remarketing) so you don't waste spend.
- **Prospecting (after remarketing is running):**
  See **audience-strategy.md** for the data hierarchy (CRM lookalike → third-party → broad). Build and upload CRM or third-party audiences when you're ready for prospecting.

---

## 6. Running Your First Campaign - Checklist

Use this as a quick sequence; details are in the other KB files.

| Step | What to do | Reference |
|------|------------|-----------|
| 1 | Start with **Remarketing** (website visitors). Create a campaign with objective **Leads** (or **Sales** if you use a landing page and optimize for a conversion event). | campaign-structure.md |
| 2 | Set **audience** to a website visitor Custom Audience (e.g. 90-day). Set a small daily budget. | audience-strategy.md |
| 3 | Choose **Lead Gen Form** or **landing page**. For in-Meta forms: **Higher Intent** form type, **Work email** required, 1-3 custom qualification questions. | lead-form-optimization.md |
| 4 | Use **4-6 distinct creative concepts** (not micro-variations). Copy must clearly state who the ad is for. | creative-strategy.md |
| 5 | **Placements:** Default Advantage+ is fine if you have placement-appropriate creative (e.g. 9:16 for Stories/Reels). Otherwise limit placements. | campaign-structure.md |
| 6 | **Naming:** Use a clear convention, e.g. `[Product] - Remarketing - Website 90d`. | campaign-structure.md |
| 7 | Launch, then **test**: submit a test lead and confirm it appears in Events Manager and in your lead destination (CRM/integration). | - |

When remarketing is running and you're ready to add cold traffic, follow **audience-strategy.md** (audience validation with ABO, then scale winners with CBO) and **campaign-structure.md** (roadmap and structure).

---

## 7. Quick Reference: What to Have Before Launch

- [ ] Pixel created and installed on all relevant pages
- [ ] Pixel firing (verified in Events Manager or Pixel Helper)
- [ ] At least one conversion event (e.g. Lead) firing on completion, not on click
- [ ] Event prioritization set if multiple events fire on the same page
- [ ] Domain(s) verified in Business Settings
- [ ] At least one remarketing audience (e.g. 90-day website visitors)
- [ ] Exclusions (e.g. employees) if applicable
- [ ] Lead form (Higher Intent, work email, 1-3 questions) or landing page with tracked conversion
- [ ] Test conversion submitted and visible in Events Manager and CRM

---

## Related Files

- **audience-strategy.md** - Data hierarchy, lookalikes, third-party data, validation
- **campaign-structure.md** - Campaign types, remarketing → prospecting → acceleration, ABO/CBO/Advantage+
- **lead-form-optimization.md** - Form type, work email, custom questions, friction
- **creative-strategy.md** - Creative-as-targeting, concept testing, placements
- **optimization-playbook.md** - Decision trees, weekly cadence, scaling protocol
