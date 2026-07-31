---
name: never-guess-an-email
title: Never guess an email address
description: |
  Use this skill when you have a target company but no verified contact address and you are
  tempted to infer one from a pattern — first.last@, f.last@, firstinitiallast@. Produces a
  routing decision per account: send, route to another channel, or leave unreachable and say so.
  Covers pattern-guessing, role inbox selection, dead-domain checks, and what to do when no
  address exists at all.
category: Prospecting
tags: [Sales]
---

A guessed address is a bounce you paid for with your sender reputation. This
decides, per account, whether an address may be sent to at all.

## The play

1. **Take only what was published.** An address found on their site, in a
   registry, on a verified data source, or given by a person is a contact. An
   address you assembled from a name and a domain is a hypothesis.
2. **Check the domain can receive mail before you queue anything.** A lookup
   for mail records — falling back to the address record — costs nothing and
   catches the dead domain that a scraper happily handed you. A lookup that
   fails to answer is not a dead domain: retry later, never suppress on a
   timeout.
3. **Rank the role inboxes you did find.** Sales-flavoured first
   (`comercial@`, `vendas@`, `sales@`, `partnerships@`), then neutral
   (`contato@`, `contact@`, `hello@`), then support (`sac@`, `atendimento@`,
   `support@`, `faleconosco@`). The first is a door; the last is a ticket
   queue.
4. **Write differently to a reception desk.** With no named human, open by
   asking to be routed to whoever owns this, in one line, and make the note
   easy to forward. Pitching a shared inbox as though it were the decision
   maker is how a real company marks you as spam.
5. **When there is no address, route, don't invent.** A public LinkedIn,
   WhatsApp or Instagram profile is a channel; a person you can name and reach
   through a colleague is a channel; silence is a channel too. Mark the
   account unreachable by email and move it to the queue a human works.
6. **Suppress permanently on a hard bounce and on a dead domain**, before the
   next send, and keep the record so no future campaign resurrects it.

## What good looks like

- The tell an experienced operator reads first: whether the address was
  *published* or *assembled*. Everything else — pattern confidence scores,
  verification vendors, catch-all detection — is downstream of that one
  question, and no confidence score turns a hypothesis into a contact.
- The mediocre version guesses, verifies with a checker that says "accept
  all", counts that as valid, and ships. Two weeks later the domain's
  reputation is spent and nobody can point at the day it broke, because
  no single send looked wrong.
- You know the output is good when the unreachable pile is *large and
  honest*. Coverage below 100% is the normal state of the world; a list where
  every row has an address is a list with invented rows in it. Bounce rate
  under 2% is the real number to defend, not coverage.

## Rules

- **MUST** treat an assembled address as unreachable, not as low confidence.
- **MUST** check domain deliverability before the first send, and again if the
  address sat unused for weeks.
- **MUST** distinguish "this domain does not exist" from "the lookup failed" —
  only the first one suppresses.
- **NEVER** send to a role inbox with copy written for a named decision maker.
- **NEVER** retry a hard bounce, on any campaign, ever.
- **NEVER** report an account as reachable because a verification tool
  returned "accept all" — that is the domain refusing to answer, not a yes.
