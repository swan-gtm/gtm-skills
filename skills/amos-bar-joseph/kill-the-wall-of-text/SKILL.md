---
name: kill-the-wall-of-text
title: Kill the wall of text
description: |
  Use this skill when work is about to go from one person to another: a report, a plan, an
  analysis, a memo, meeting notes, research, a code change, a proposal, or a raw AI answer.
  Produces an interactive, human-readable page that the recipient can review in seconds, with a
  ten-second top, a two-minute body, and folded evidence, written in Simplified Technical English
  and signed by the sender after a review loop. Trigger phrasings: "make this digestible", "make
  this readable", "de-slop this", "turn this into an artifact", "one-pager", "exec view", "I need
  to forward this", "nobody will read this", "show me what I must decide".
category: Leadership
tags: [Leadership, RevOps]
---

Applies each time raw work must go to a person who did not make it. Produces one interactive page that the recipient can review in seconds, and that the sender has read and signed.

The rule: work like a lawyer who talks to a five-year-old. The lawyer signs each word and stands behind it. Nobody gives a five-year-old ten pages of text; someone shows the story.

The measure: work is slop if the review takes longer than the generation. This play inverts that ratio. The build takes longer, so that the review takes seconds.

## The three layers

Each page has all three.

1. **Top, 10 seconds.** The verdict in one sentence. The ask: what the recipient must do, and by when. A maximum of three key numbers.
2. **Body, 2 minutes.** An interactive view in the shape that fits the content.
3. **Evidence, on demand.** Sources, method, assumptions, and the content that was cut. Folded. Nothing is lost, and nothing is in the way.

Test for the top: if the recipient reads only the top and closes the page, do they know the answer and their next action?

## The play

1. **Read all of the raw work.** Extract the recipient, the ask, the verdict, each fact with its location in the source, and the gaps: missing data, contradictions, claims with no evidence.
2. **Ask a maximum of two questions, in one message.** "Who gets this, and what must they do with it?" and "What is the one thing they must understand?" Offer a proposed verdict, so that the human can say yes. Do not ask what the context answers. A skipped question becomes a labeled assumption, not a second question.
3. **Select the shape.** A report becomes a dashboard. A plan becomes a one-page view. A decision becomes an option comparison. A code change becomes a diagram of what moved. Read `references/shape-table.md` for the ten shapes and the rule for two shapes that fit.
4. **Write each visible word in Simplified Technical English.** Short active sentences, one word for one thing, no idioms, absolute dates, one named owner for each action. Read `references/writing-rules.md` before you write; it also has the fidelity rules and the cases where the two sets of rules meet.
5. **Publish the first version quickly.** Start from `references/page-skeleton.md`. The first version shows a "Draft, not signed" banner. Chat gets one line: "This is V1. Tell me what goes on top, what to cut, and what is wrong."
6. **Check before each publish.** Read `references/pre-publish-check.md`. It has a script that finds sentences that break the writing rules, calculates the read time, and lists each number that is not in the source.
7. **Run the review loop.** The human decides what goes on top, what to cut, and what is wrong. Each block has Keep, Cut, Fix, and Move up controls, and one button copies the feedback as text for the chat. Apply the feedback to the current page; do not build it again. Read `references/review-loop-and-signing.md`.
8. **Get the signature.** When the human approves, ask one time: "Did you read all of it, and do you stand behind it?" On yes, the banner changes to "Signed by NAME, DATE". No signature, no change.

`references/worked-example.md` shows one case from raw work to signed page, with the weak version adjacent to the good one.

## What good looks like

- **The best operator starts from the recipient's next action, not from the document.** The first question is "what must this person do after they read it?" The shape, the top, and the cuts all follow from that answer. The average operator starts from the structure of the source and keeps it.
- **The common mistake is text in boxes.** The same paragraphs, cut into cards, with twelve numbers of equal size. It looks better and reads no faster. If the shape of the page is the shape of the source, the work did not occur.
- **The top states the answer, not the topic.** "The quarter missed the plan by 12%, and small-business churn is the cause" is a top. "This report covers quarterly performance" is a label.
- **Read time is a number on the page.** Top plus the longest tab, divided by 200 words for each minute. More than three minutes means more cuts or more folds.
- **Each number has a source.** A number that is not in the source has a `calculated` or `assumed` tag, or it is wrong. A conflict between two sources shows the two values, on top if the number is on top.
- **The first version is about 80% correct, and that is the plan.** The 20% that the human changes is what only the human knows: what this recipient will ask first. A good page makes that 20% fast to change. A page that the human signs with no changes is a warning that the human did not read it.
- **Interaction does work.** A fold hides depth. A filter answers a question. A check box records an action. Animation and hover effects do none of these.
- **The chat stays short.** One line after each publish. The page is the work surface.

## Rules

- MUST show the "Draft, not signed" banner until the human confirms that they read all of it.
- MUST keep cut content in the evidence layer, where the human can restore it.
- MUST tag each assumption, calculation, proposal, unverified claim, and conflict where it occurs.
- MUST write "Not in the source" for a missing owner, date, or number.
- MUST make the page work on a phone with no sideways scroll, and print with all tabs open.
- NEVER invent a number, an owner, a date, or a quote.
- NEVER write a signature that the human did not give.
- NEVER make a claim stronger or weaker than the source makes it.
- NEVER put more than three key numbers on top, or more than four tabs in the body.
- NEVER deliver a long chat message or a text dump in place of the page.
- NEVER say that a check was made when it was not made.
