---
name: find-buyers-in-linkedin-comments
title: Find buyers in LinkedIn comments
description: |
  Use this skill when you want B2B buyers who have said, in public, that they have the
  problem you solve: mine the comments and reactions of LinkedIn posts where people
  complain about a pain, a chore or an incumbent tool, and keep the engagers who fit.
  Produces a scored list of people with a quoted intent line each, ready for a warm
  approach. Fires on "who is complaining about X on LinkedIn", "find prospects from
  posts, comments or reactions", "intent signals from LinkedIn", "mine a competitor's
  posts or a viral post for leads", "post discovery", "social listening for sales",
  "engager scraping", "comment mining", or when someone pastes a post URL and asks who
  in the thread is worth reaching.
category: Prospecting
tags: [Sales]
---

Applies when the buyer names the problem out loud on LinkedIn and a people search would
never surface them. Produces a list of engagers, each with a fit verdict, an intent score
and the sentence they wrote, taken from posts that were scored before anyone was pulled.

A person who writes "I pay 100 a month for Sales Navigator and still build my lists by
hand" under a post has told you three things: they have the problem today, they own it,
and they said it in public. This play finds those posts, takes the people who engaged,
and keeps the ones who fit.

## What you need first

- **The intent**, one sentence in the buyer's own words and language: "people struggling
  with manual LinkedIn prospecting", "founders doing their own sales who hate cold email".
- **Anchors**: 5 to 15 short words for the tools, brands and chores the buyer would name.
- **Who is a buyer and who is not**: "anyone doing their own B2B prospecting; exclude
  vendors, agencies, consultants, recruiters". The exclusions are absolute.

If the input is a post URL rather than an intent, skip the search and start at scoring.

## The play

1. **Write the searches: short, many, in every language.** LinkedIn post search is an
   AND over every word, so a natural pain phrase finds almost nothing while a 2 to 3
   word topic query finds hundreds. Write 15 to 20 queries, sort by date, filter to the
   last 24 hours. Recall comes from the searches; precision comes from the next two
   steps, never from a longer query. Read `references/search-recipe.md` for the measured
   comparison and the query rules.
2. **Filter on engagement first, because it is free.** Rank every found post by
   `reactions + 2 x comments` and keep the ones above 20. Nobody engages with a post
   nobody saw, and the people you want are in the engagement, not in the post.
3. **Score the post before touching anyone in it.** Put the post in one of four buckets
   (rant from someone who has the problem, vendor pitch, job post, thought leadership),
   then score it 0 to 100 against the intent and keep 70 and above. The bucket matters
   more than the number. Rubric in `references/scoring-and-selection.md`.
4. **Take the right people, in order.** Commenters first (read the comment, score it
   against the intent, keep 70 and above), reactors second (no intent score, fit only),
   the author last and off by default. Apply the buyer exclusions as hard gates before
   any model scoring. Read engagers with a loose fit (role and seniority), not the strict
   ICP used for people search. Yields and gates in `references/scoring-and-selection.md`.
5. **Approach warm, never in the thread.** Visit the profile, react to the post, reply to
   their comment with one specific sentence, and invite two days later with a note that
   names the thread. The conversation opens itself. A full run, from query to yield, is in
   `references/worked-example.md`.

## What good looks like

- The best operator reads the **comment**, not the profile. "Same here, we do it in a
  spreadsheet" is a buyer; "great post!" from a perfect-title VP is nothing. The
  intent line is the asset; the title is a filter.
- The mediocre version pulls every engager from a viral post and scores them on fit. A
  vendor pitch with 400 reactions is 400 people who like the vendor. A post scored before
  its engagers are pulled is what separates a lead list from a follower list.
- Models rate an outbound consultant 80 on "fit" for a "people who do their own
  prospecting" intent if allowed to. The buyer exclusions run **before** scoring, as
  hard gates, or the list fills with people who sell the same thing.
- Good output on a real post: 150 unique engagers become about 20 fitting people, of whom
  a handful wrote something with explicit intent, plus sometimes the author. Against a
  strict people-search ICP the same post yields one. The loose fit is the point.
- The output reads as a table: name, role, company, the sentence they wrote, intent
  score, and the post it came from. Anyone can pick the top five without re-reading the
  thread.

## Rules

- MUST score the post before pulling a single engager from it.
- MUST apply the buyer exclusions (vendor, agency, consultant, recruiter, seller of the
  same category) as hard gates before any scoring.
- MUST keep the engager's own words next to their name; the quote is what makes the
  approach specific.
- NEVER pitch in the thread. The thread is where they were found, not where they are sold.
- NEVER invite on the same day as the first touch; visit, react, reply, then invite two
  days later.
- NEVER rely on one query or one language; short queries in every language the buyer
  speaks, or the target post is missed.
