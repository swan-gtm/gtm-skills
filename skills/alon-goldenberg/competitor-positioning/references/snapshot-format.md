# Positioning snapshot format

Keep one file per competitor in your workspace, named for the competitor. This structured format is what makes delta detection work — every field is diffable against the next run. Update the file after every run; never overwrite the History section.

```markdown
# [Competitor Name]
## Last Updated: [YYYY-MM-DD]

## Site Structure
- Key Pages: [URLs for features, pricing, blog, docs, etc.]
- Missing Pages: [notable absences — e.g., "no public pricing", "no blog"]
- Subdomains: [docs., api., community., etc.]

## Homepage
- Source: [homepage URL]
- Tagline: [exact text]
- Hero Message: [exact text]
- Primary CTA: [button text]
- Value Props: [each, verbatim]
- Target Audience: [who the copy speaks to]
- Navigation Structure: [top-level nav items]

## Features
- Source: [features page URL]
- Key Categories: [list]
- Differentiation Claims: [list, verbatim]
- Notable Features: [branded names, flagship features]

## Pricing
- Source: [pricing page URL]
- Model: [per-seat / usage / flat / freemium / custom]
- Tiers: [list, with prices if visible]
- Enterprise Signal: [yes/no, details]
- Feature Gating: [what's locked to higher tiers]

## Content Strategy
- Sources: [blog/resource URLs analyzed]
- Blog Cadence: [weekly / biweekly / monthly / sporadic]
- Primary Themes: [list]
- Content Types: [blog, case study, whitepaper, webinar, etc.]
- Audience Focus: [developer, executive, practitioner, etc.]

## Social Proof
- Sources: [customer/case-study URLs]
- Key Customers: [names if public]
- Testimonial Themes: [what customers praise]
- Case Study Focus: [industries, use cases highlighted]

## History
### [YYYY-MM-DD]
- [change — e.g., "Tagline changed from 'X' to 'Y'"]
- [change]
```

## Maintenance rules

- **Top sections reflect current state; History is append-only.** On each run, update the current-state sections to what's live now, then add a dated History entry describing every diff you made. The History trail is how "when did they pivot to enterprise?" gets answered months later.
- **Verbatim or nothing.** Taglines, CTAs, value props, and differentiation claims are stored as exact text. If a page was inaccessible this run, keep the prior value and note "not re-verified [date]" rather than blanking it.
- **A run with no changes still gets a History entry** ("[date] — no changes detected") so cadence gaps are distinguishable from missed runs.
- **Cross-link, don't merge.** If you keep separate business-signal notes on the same company (funding, hiring), reference that file from here — positioning shifts and business events explain each other, but the files serve different plays.
