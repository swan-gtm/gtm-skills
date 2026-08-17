# Visual toolkit: the right tool for each visual job

A recognisable cluster of failures comes from using the wrong tool for a visual element. They are worth their own pass because they read as off-brand or machine-made even when the layout and copy are fine, and because they are easy to miss if you only review the composition. Check each of these on any asset that carries icons, logos, or generated imagery.

## Icons: one set, never generated

- Use a single, consistent vector icon set across the whole asset (for example Lucide, Phosphor, or Heroicons), so every icon shares one grid, one stroke weight, and one corner language. Recolor to the brand palette.
- Never generate icons with an image model. Model-drawn icons wander in weight and style and read as robotic.
- Never mix icon sets in one asset. Two sets side by side is one of the fastest tells that an asset was assembled, not designed.

**Reviewing:** if the icons vary in stroke weight or style, or look illustrated rather than drawn to a grid, flag it. The fix is to replace them all with one real vector set.

## Logos: always the real asset

- Never generate or approximate a real logo with an image model. A model-rendered logo is subtly wrong in a way viewers feel even when they cannot name it, and using a mangled version of a real brand's mark is worse than using none.
- Use the actual logo file. If it is missing, say so and use a clearly-labelled placeholder rather than a generated stand-in.
- Logos keep even visual weight and clear space; never stretched, recolored, or dropped in at low resolution.

**Reviewing:** any logo that looks even slightly off is a high-severity flag. Verify it is the real asset, correct brand, and undistorted.

## Photographic and hero imagery: generate deliberately

- A generative image model is the right tool for photographic, illustrative, hero, background, or product-mockup imagery - not for icons or logos.
- When a set of images has to feel like one system (a formats row, a series of cards), generate one anchor image and then edit variations from it, rather than re-prompting each from scratch, so the set shares one look.
- Do not bake headline text into a generated image; model-rendered text is unreliable. Leave deliberate space for a headline and set the real copy over it afterward.

**Reviewing:** if hero images in a set look unrelated to each other, or a headline is rendered inside the image, flag it.

## Hierarchy comes from structure, not color

A common self-inflicted failure: solving hierarchy by coloring everything. Hierarchy should come from size, weight, spacing, and placement. If a slide uses five colors to signal importance, the fix is usually one accent color and a real type scale, not more color.

## Density is about information, not size

Dense should mean information-dense, never small-and-cramped. If an asset is hard to read, shrinking type to fit more in makes it worse. The fix is to cut what does not carry the argument and give the rest room, not to reduce the type size.
