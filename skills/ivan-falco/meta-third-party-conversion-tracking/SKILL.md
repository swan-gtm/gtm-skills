---
name: "meta-third-party-conversion-tracking"
title: "Meta off-domain conversion tracking"
description: "Use this skill when conversions happen off your domain — webinars, events, third-party platforms — and Meta still needs the conversion signal."
category: Ads
---

# Meta Ads - Third-Party / Off-Domain Conversion Tracking (Webinars & Events)

When the conversion (e.g. webinar signup, event registration) happens on a **third-party platform** (Luma, Hopin, etc.) instead of on your website, use this for best-practice setup. Applies to anyone running Meta ads to a webinar or event where signup completes off-domain.

---

## The Problem

- User lands on **your site** (e.g. webinar LP with UTM).
- User clicks "Sign up" → goes to **third-party platform** (e.g. Luma) to complete registration.
- Conversion happens **off your domain**. If your pixel is only on your site, Meta never sees the signup unless you track it on your domain or on the platform.

---

## Best Practice: Two Decisions

### 1. Where to track the conversion (pixel in platform vs thank-you page)

| Option | When to use | What to do |
|--------|-------------|------------|
| **Pixel in the platform** | Platform supports Meta pixel (e.g. Luma Plus → Calendar → Settings → Options). You have or will get the required plan. | Add your Meta pixel in the platform. Platform sends e.g. `CompleteRegistration` when user registers. Add the platform's domain (e.g. luma.com, lu.ma) to your Meta pixel **Traffic permissions** (allow list). |
| **Thank-you page on your site** | Platform doesn't support a pixel, or you don't have the plan. Platform can **redirect after registration** to a URL you control. | Set post-registration redirect to a thank-you page on your domain. Fire `Lead` or `CompleteRegistration` on that page. Optimize for that event. |

**Recommendation:** Pixel in the platform is best when available (one setup, real conversion). Thank-you page is the fallback when the platform can't fire the pixel but can redirect.

### 2. Passing UTM to the signup link

- The platform will **not** automatically see the UTM from the page the user was on when they clicked "Sign up."
- **Best practice:** When the user clicks the signup/register button, the link to the third-party site should **include the same UTM parameters** (e.g. from the current page URL).
- **How:** Build the signup link dynamically: read the current URL query string (e.g. `window.location.search`) and append it to the platform's registration URL. Example: `https://platform.com/event/xyz` → `https://platform.com/event/xyz?utm_source=linkedin&utm_medium=paid-social&utm_campaign=...`
- Ensures attribution and platform-side reporting stay correct.

---

## Example: Luma

- **Pixel:** Luma Plus → Calendar → Settings → Options → Meta Tracking Pixel. Luma sends PageView, CompleteRegistration (free events), Purchase (paid). Add **luma.com** (and **lu.ma** if used) to Meta pixel Traffic permissions.
- **UTM:** Pass UTMs from the webinar LP into the Luma registration URL when the user clicks signup (e.g. via JS appending current URL params to the Luma link).

---

## Quick Message Template

Use when asking someone to enable pixel + UTM pass-through on their side:

**Short version:**

Hi [Name],

Quick ask for [webinar/event name] so we can track signups properly in Meta:

1. **Meta pixel in [platform]** - If you're on [platform plan that includes pixel, e.g. Luma Plus], can you add our Meta pixel in [platform]? ([Where to find it, e.g. Calendar → Settings → Options].) That way we get real "registration" events and can optimize for signups. We'll allow [platform domain] in our Meta pixel settings on our side.

2. **UTM on the signup link** - When someone clicks "Sign up" on the [webinar/event] page, we need the same UTM params (from the page they're on) to be passed through to the [platform] registration URL. That keeps attribution correct. If your team can update the signup button/link to append the current URL's UTM parameters to the [platform] link, we're set.

Thanks,
[Your name]

---

## Related Files

- **meta-setup-and-tracking.md** - Pixel setup, Traffic permissions (allow list), conversion events
- **meta-capi-and-events.md** - CAPI, event hierarchy, HubSpot vs n8n
- **campaign-structure.md** - How tracking fits into overall campaign architecture
