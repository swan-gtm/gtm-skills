---
name: patent-backed-seo-quick-wins
title: Patent-backed SEO quick wins
description: |
  Use this skill when you're looking at one page and don't know its SEO status,
  and you want the two or three quick wins worth doing now — each traced to the
  mechanism behind it, not a hunch. Point it at a single page; it returns a short,
  ranked list of instant-win actions, and for every action it names the Google
  patent or leaked Search API field that explains why it works, so you can verify
  the claim yourself and defend it in a client or sales call. Reach for it when
  you'd say "what are the quick wins here", "audit this page", "why would this
  rank", "prove this isn't guesswork", "what does Google actually reward", or
  "back that with a patent".
category: SEO
tags: [Marketing]
---

Applies to a single page whose SEO status is unclear and you want the fastest wins. Produces the top two or three quick wins for that page — each traced to the ranking mechanism behind it, with a verifiable patent ID or leaked Search API field as the receipt.

## Bring a direction — the skill grounds it, it doesn't pick it

Come in with a read: "the title is fighting the query", "the content is thin", "nothing internal points at this page". The skill's job is to confirm or kill that read against how the ranking system is documented to work — and to sharpen your model of that system while it does. Hand it a URL with no hypothesis and you get a generic audit any tool spits out. The edge is the direction you bring; the evidence is what makes it defensible.

## Read the page the way the system does

Pull the page and its target query. Walk the elements Google is documented to weigh: the title and how well it matches the query, the headings, the depth and originality of the main content, the internal and inbound anchors, the freshness signals, and the site-level context the page inherits. Mark what's weak — that is your shortlist of candidate wins.

## Every win needs a receipt

For each candidate, name the mechanism that makes it work and attach the evidence: a Google patent that describes the mechanism, and/or a field in the Search API documentation showing Google stores the signal. Read `references/evidence-map.md` for the verified starter set — patent IDs, leaked field names, the on-page action each one grounds, and how to confirm a new one before citing it. A win you cannot tie to a mechanism is a preference, not a quick win: drop it, or label it a hypothesis and say so.

Be precise about what the evidence proves. A patent shows how Google thinks about a problem; a leaked field shows Google stores a signal. Neither proves the signal is live or how heavily it is weighted. Say which one you have.

## Rank by effort-to-impact, hand back the top three

Order the traced wins by how much they move the page for how little work, and return the top three — two if only two are solid — not a 40-line audit nobody acts on. Each item carries four things: the action, the page evidence that it's missing, the mechanism, and the ID to verify.

## What good looks like

- The tell: a strong operator names the exact mechanism under a recommendation, not "best practice". "Tighten the title" is advice anyone gives. "Your title misses the query — and title-to-query match is a field the system stores; here it is" is a receipt a skeptical client cannot wave off. Specificity that survives cross-examination is the tell.
- The common mistake: running the skill as an oracle — feeding it a URL and adopting whatever comes back. It exists to justify and pressure-test a direction you already hold, and to teach you the ranking system as it goes. Run it directionless and you get a confident-sounding audit with no edge and nothing learned.
- The proof: every claim carries an ID a stranger can paste into a patent search or the leaked documentation and confirm in a minute. If a reference does not resolve, or the field is not in the docs, the claim fails and comes out. Verifiability is the product — not the ranking, not the number of findings.

## Rules

- MUST attach a verifiable patent ID or leaked Search API field to every quick win, and confirm it resolves to a real source before citing it.
- MUST distinguish what the evidence proves: a patent describes an approach; a leaked field shows a signal is stored — neither proves live use or weighting.
- MUST cap output at the few highest-impact wins, ranked, each with the page evidence behind it.
- NEVER invent, guess, or approximate a patent number or field name. If you cannot verify it, present it as a hypothesis — never as a receipt.
- NEVER let the skill choose the strategy; it grounds and challenges the direction the operator brings.
