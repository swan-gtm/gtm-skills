# Speaker attribution in transcripts and email threads

Before treating anything said in a call or written in an email as evidence for or against a MEDDPICC component, resolve who said it — specifically, whether they're on the seller's side or the buyer's. Getting this wrong inverts the finding (a buyer's skepticism read as a seller's caveat, or vice versa). Work through this chain in order and stop at the first rung that actually resolves it.

## 1. Attendee or calendar metadata (highest confidence)

If the calendar invite, meeting platform export, or CRM activity record includes attendee email addresses, match domains against the seller's own company domain. Anyone outside that domain is presumptively buyer-side; anyone inside it is presumptively seller-side.

Watch for third parties — a consultant, systems integrator, or reseller on the call has neither domain. Don't default them to buyer-side. Mark them "unidentified — role unconfirmed" unless they're already a known deal contact.

Note that this metadata usually lives outside the transcript file itself. A raw `.vtt` or `.srt` export carries speaker display names at most (via a voice tag or a plain prefix) — never emails or domains. If domain data isn't bundled alongside the transcript, treat it as unavailable and move to rung 2.

## 2. Contact-list or roster match

If domain data isn't available, match the transcript's speaker names against the deal's known contact list (buyer-side names) or the seller's own team roster (seller-side names). When a CRM connection is available, this is usually the most concrete version of the rung: the opportunity's own contact records and its owner field. A name that matches a contact already tied to this deal, or matches the deal's owner, is a real match — not a guess — even though it's weaker than a domain match, since names can collide, be misspelled by the transcription tool, or go by a nickname.

If a name doesn't match anything on either list, don't force it. Move to rung 3.

## 3. Content-cue guess, confirmed before use

If neither metadata nor a name match resolves it — generic labels like "Speaker 1" or "Participant 2," or an unrecognized name — form a hypothesis from what was actually said:

- Self-references to the product, roadmap, or "our platform" point to seller-side.
- Questions about pricing, timeline, internal systems, or evaluation criteria point to buyer-side.

Treat this only as a proposal. State the guess explicitly and ask the person running the audit to confirm or correct it before using it to support any conclusion about champion behavior, sentiment, or buyer intent. A confirmed guess can then be used like a rung-2 match; an unconfirmed one must not appear in the output as settled fact — carry it as "unconfirmed" through to the final report if it's used at all.

## What this chain prevents

Without it, the most common failure is quiet misattribution: a transcript with unlabeled or mislabeled speakers gets read confidently, and a buyer's hesitation ("we haven't secured budget for this") gets misfiled as the seller hedging, or a seller's routine caveat gets read as the buyer expressing doubt. Both produce a MEDDPICC finding that's exactly backwards. Resolving attribution first, and flagging when it can't be resolved, is what keeps the downstream evidence trustworthy.
