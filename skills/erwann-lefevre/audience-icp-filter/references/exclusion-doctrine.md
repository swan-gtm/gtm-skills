# Exclusion doctrine

Naive exclusion on company name leaks. It leaks in the direction that hurts most: the team's own colleagues end up in a cold prospecting sequence.

Three failure modes, all observed on real lists, all handled deterministically in pass 1.

## 1. Empty company and empty email

The company field is blank, there's no email, and the only trace of the employer is the bio: `Client Partner @ Acme`.

Filtering on the company field lets this person straight through. This is the standard shape of a lead imported from a social export, which is to say it's common.

**Fix:** match exclusions across the whole identity surface — company name, work email, personal email, bio, and company URL. This is why bio coverage is a gate condition and not a nice-to-have.

## 2. Job-changers

The company field says `Vantage Digital` and the work email says `j.moreau@acmelabs.com`. The company is stale, the email is current — or the reverse. Either field read alone gives the wrong answer.

**Fix:** a hit on *either* field excludes. Don't try to decide which one is fresher.

## 3. Collapsed spellings

`@AcmeLabs` and `acme-labs` contain none of the literal string `"Acme Labs"`. Anyone writing the company without its spaces evades a plain substring match.

**Fix:** run a second comparison with all punctuation and spacing stripped from both sides.

**With a length guard.** Below about five characters, a squashed substring match collides constantly — a three-letter company acronym starts firing inside unrelated words and excludes real prospects. Short tokens stay word-bounded; only longer terms get the squashed comparison.

## Always seed with their own company

The single most common leak, and the most embarrassing one. Add the team's own company name and email domain to the exclusion list before anything else, whether or not anyone thought to mention it.

## Extending exclusions in pass 2

Pass 2 can add competitors nobody listed. Say which ones you added and why.

**But a competitor's name in a bio is not an employer.** People list the tools they use in their bios. On real data, two competitor product names appeared in prospects' bios as tools they worked with — excluding those leads was wrong, and it removed real pipeline.

Before excluding on a competitor signal, confirm it appears as the employer or in the email domain, not merely somewhere in the bio text.

## Junk company values

Values like `Nothing`, `-`, `N/A`, `Freelance` and `Self-employed` are not employers. They're either placeholder data or a statement that the person has no company, and treating them as company names produces nonsense exclusions and nonsense matches alike.

Agency, freelance and consultant signals don't get excluded automatically — a consultant can be a genuine buyer — but they do get flagged into the pass-2 queue, because the two cases look identical to a pattern and completely different to a reader.

## What exclusion is not

Exclusion is not a quality filter. It answers "must we never contact this person", not "is this person a good lead". Someone out of ICP goes to `no_match`; someone at a competitor or on the team goes to `excluded`. Collapsing the two loses the distinction between *we chose not to* and *we must not*, which is exactly the distinction anyone auditing the list later needs.
