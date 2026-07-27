---
title: "Image-ad mockups: HTML rules + design patterns"
description: Reference for the LinkedIn ABM ad design skill.
---

# Image-ad mockups: HTML rules + design patterns

Mockups are live HTML - pixel-perfect, on-brand, editable - not AI-generated images. Patterns extracted from high-performing B2B SaaS LinkedIn ads (Gong, Vanta, m3ter, Instantly, Orum, ColdIQ, Fibbler); originally from the "LinkedIn Ad Designer" skill by Advanced Client (advancedclient.io).

## Brand config (collect in the interview)

```
COMPANY NAME / TAGLINE
── Colours ──  PRIMARY #hex · ACCENT #hex · DARK BACKGROUND #hex · TEXT ON DARK #hex · MUTED TEXT rgba
── Typography ──  FONT (e.g. Inter, DM Sans) · HEADING WEIGHT (e.g. 800) · BODY WEIGHT (e.g. 400)
── Logo ──  SVG code, an image file in the images folder, or "company name in FONT WEIGHT, primary colour"
── Tone ──  e.g. "Direct, confident, no fluff. Numbers over adjectives. Short punchy lines."
```

## HTML format rules

- One self-contained `.html` file per ad. Square 1:1 by default (540×540px), 1.91:1 landscape if asked.
- Max width 540px, border-radius 16px, overflow hidden, inline styles only. Font via font-family stack (load Google Fonts with a `<link>` if the font needs it and the renderer has network access).
- All colours from the brand config. No placeholder lorem ipsum, no fake logos.
- User images: reference as `./images/<file>` and copy the files into `mockups/images/` so the HTML opens in a browser AND renders to PNG.
- Copy rules: cut every word that doesn't earn its place; numbers > adjectives ("20% lower CPL" not "much lower CPL"); one idea per ad (two ideas = two ads); no "leverage/synergy/best-in-class"; max ~40 words total on the ad.
- Iterations: when the user asks for changes, regenerate the full HTML - show, don't describe. Variations = separate files.

## Rendering to PNG

If a headless browser or screenshot tool is available, render each mockup to a 1080×1080 PNG (2× scale); otherwise any browser screenshot of the HTML at 1080×1080 works. (The full plugin at github.com/ZENABM/linkedin-abm-skills bundles a ready-made render script.) After rendering, open each PNG and check: no text overflow, readable contrast, images loaded (a broken image icon means a wrong path), nothing clipped at the edges.

## What wins visually (2026 benchmarks, 463+ top ads)

Specific offers - FREE / $ / deadline - appear in 65% of top image ads vs 10% of low; real people with names 47% (stock photos: 35% of low performers); strong high-contrast CTA button 59% vs 20%; humor/pattern-interrupt 35% vs 2%; dark background + neon text in 35% of ≥2%-CTR ads. Avoid: text-heavy layouts, logo-as-hero, UI-screenshot dumps, generic minimalism, vague "Learn More" CTAs.

## Universal design principles - default to RICH style

1. Gradient background (not flat solid)
2. At least one glass-morphism element
3. 1-2 subtle background shapes
4. box-shadow on floating elements

## The 23 patterns (pick by the ad's job)

| # | Pattern | When to use | Key elements |
|---|---------|-------------|--------------|
| 1 | Stat Highlight with Pill | surprising data point, benchmark stat | soft italic lead-in; big bold stat with highlight pill behind key words; vibrant single-colour bg |
| 2 | Product Screenshot + Headline + CTA | demo signups, product in action | bold headline, ONE word in accent; product mockup fills bottom 50-60% |
| 3 | Card-on-Dark with Floating Elements | downloadable resource | very dark bg; large white card offset left (~70% width); floating checkmark circles |
| 4 | Clean Light with Illustration | brand awareness, softer tone | light/cream bg; bold headline, ONE keyword in accent |
| 5 | Dark Resource/Playbook Promo | guide or multi-chapter resource | dark bg; ALL-CAPS headline; 4-6 chapter titles in pill rows |
| 6 | Six-Panel Grid | process, timeline, feature grid | dark bg; 2x3 or 3x2 grid of white cards |
| 7 | Contrarian / Pattern Interrupt | challenging conventional wisdom | dark bg; HUGE bold headline; key phrase in accent |
| 8 | Before → After Comparison | transformation, old way vs new way | two panels: before (red tints) → after (green tints, checkmarks) |
| 9 | Four-Panel Grid | product intro, multiple features | 2x2 grid, each panel its own background |
| 10 | Report Cover / White Paper Promo | report, benchmark study | premium feel, lots of space; the stat in the headline sells |
| 11 | Social Proof / Logo Bar | vertical/industry targeting | HUGE industry keyword on top; row of 3-4 customer logos |
| 12 | Data Visualization / Chart Ad | data-driven argument | 3-act structure: SETUP → EVIDENCE (chart) → CONCLUSION |
| 13 | Question Hook + Bold Answer | specific pain point | question in accent italic; bold answer below |
| 14 | Handwritten Annotation | thought leadership, founder voice | light bg; hand-drawn SVG underline; Caveat font annotation |
| 15 | Co-Branded Report + Stat Cards | co-branded research | "Brand A × Brand B" header; 2 stat callout cards above report mockup |
| 16 | Scattered Touchpoint / Tag Cloud | complexity, messy buyer journey | 8-15 scattered pill tags, organic layout |
| 17 | Testimonial + Review Badge + Metrics | social proof with results | gradient bg + glass card; inline metric pills; G2 badge + headshot |
| 18 | Metric Funnel with Floating Cards | workflow results with numbers | 3 staggered glass metric cards (input → process → output) |
| 19 | Rejection Wall / Pain Gallery | pain of bad outreach | scattered negative-response pills (top 60%); bold contrarian headline (bottom 40%) |
| 20 | Tool Consolidation Grid | all-in-one replacement positioning | crowded grid of tool icons; "Replace them all with one." |
| 21 | Case Study Speech Bubble | named customer, bold claims | vibrant saturated bg; MASSIVE stat in white speech bubble |
| 22 | Split Visual Comparison | old vs new with visual contrast | left: messy cascading cards; right: clean product mockup |
| 23 | Social Proof + Team + Dashboard | "use what we use" positioning | abstracted dashboard mockup; row of headshot circles; objection-handling tags |

State the chosen pattern (from this reference) in each image ad's design brief so the designer (or the mockup) and the brief stay in sync.
