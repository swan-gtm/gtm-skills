# Scoring the post, then selecting the people

Two rubrics, applied in this order. The post is judged before anyone in it is pulled;
the people are judged against the buyer description before any model scores them.

## 1. Engagement floor (free, first)

Median reactions on a raw result page is 0 to 4. Rank by `reactions + 2 x comments`
and keep posts above 20. On one real day 638 found posts became 45, and 11 of those had
over 100 reactions.

## 2. Post buckets

Read the body and place the post in one bucket. The bucket decides; the score refines.

| Bucket | Keep? | The tell |
|---|---|---|
| Rant or ask from someone who has the problem | yes | first person, present tense, a number, a question |
| Vendor pitch or launch | no | "we built", "excited to announce", a link to a product |
| Job post or hiring | no | "we're hiring", "join us" |
| Thought leadership about the market | maybe | third person, no personal stake; take only the commenters who disagree or ask |

Then score 0 to 100 against the intent sentence and keep 70 and above. A vendor pitch
with 400 reactions is 400 people who like the vendor, not buyers; the bucket catches
what the score would let through.

## 3. Who to take from a kept post, in order

| Source | Intent score? | Rule |
|---|---|---|
| Commenters | yes, 0 to 100 against the intent, keep 70+ | "same here, we do it in a spreadsheet" is intent; "great post!" is nothing |
| Reactors | no, silent | keep only if they fit the buyer description; expect about 85 percent to be 2nd-degree connections |
| Author | off by default | as often a vendor as a buyer; read the profile. A founder venting about their own sales process is the best lead on the thread, and free |

## 4. Hard gates before any scoring

Apply the buyer description as exclusions **before** a model sees the person: vendor,
agency, consultant, recruiter, salesperson at a tool in the same category. Models rate an
outbound consultant 80 on fit for "people who do their own prospecting" if allowed to.

## 5. Fit: loose for engagers, strict for search

One real post, 96 reactions and 80 comments, 150 unique people:

| Fit rule applied | People kept |
|---|---|
| Strict people-search ICP (Head of Sales, 11 to 200 employees, SaaS, one country) | 1 |
| Buyer description, role and seniority only ("does their own B2B prospecting", exclusions applied) | 22, of whom 5 with intent above 70, plus the author |

Engagers are found by intent, so firmographics matter less than they do in a people
search. Read them with a loose fit (role and seniority, exclusions absolute), or the play
yields one person per viral post.

## Output shape

One row per kept person: name, role, company, the sentence they wrote (or "reacted"),
intent score, post URL, post bucket. Sort by intent score, then by engagement of the
post. The top of the table is the day's approach list.
