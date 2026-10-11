# Writing rules: Simplified Technical English for B2B work

Read this page before you write any visible text in the artifact.

Each word of visible text in the artifact obeys these rules. STE was made so that a reader with basic English can understand safety-critical text with no ambiguity. That is the "five-year-old" standard with the "lawyer" precision.

Note: the official ASD-STE100 dictionary is a licensed specification for aerospace. This skill applies its writing rules strictly, and replaces the aerospace dictionary with the short B2B word list below.

**Words**
1. One word, one meaning. Use the same word for the same thing each time. If you call it "account", do not call it "customer", "client", and "logo" in other places.
2. Use the simple, common word: "use" (not "utilize", "leverage"), "help" (not "facilitate", "enable"), "start" (not "initiate", "kick off"), "end" (not "terminate", "sunset"), "show" (not "demonstrate", "showcase"), "about" (not "regarding", "with respect to"), "buy" (not "procure"), "need" (not "require"), "enough" (not "sufficient"), "before" (not "prior to"), "do" (not "execute on", "action").
3. Technical names and business terms are permitted when the recipient uses them (ARR, pipeline, churn, SQL, API). Define an abbreviation the first time, unless you are sure that the recipient knows it.
4. No noun clusters longer than three words. "Enterprise customer renewal risk mitigation plan" becomes "the plan to decrease renewal risk for enterprise customers".
5. No idioms, no metaphors, no slang, no hype: "move the needle", "low-hanging fruit", "game changer", "deep dive", "circle back", "robust", "seamless", "synergy", "unlock", "supercharge".
6. No empty intensifiers or hedges: "very", "really", "quite", "basically", "arguably", "it is worth noting that", "it is important to note".
7. Do not use contractions. Write "do not", "it is".

**Sentences**
8. One topic for each sentence.
9. Instructions: a maximum of 20 words. Descriptions: a maximum of 25 words.
10. Active voice. Name who does the action. "Dana will send the contract Friday", not "The contract will be sent".
11. Instructions use the imperative: "Approve the budget before 14 June."
12. One instruction for each sentence, unless two actions occur at the same time.
13. Simple tenses only: present, past, future. No "has been being", no "would have had".
14. Do not use the -ing form as a verb or to start a clause. "Reviewing the data, we found" becomes "We reviewed the data. We found".
15. Keep the articles and the small words ("the", "a", "that"). Do not write in telegraph style in sentences. Labels, tiles, and chips can be short fragments.
16. State a condition first, then the action: "If churn is more than 3%, tell Finance."

**Structure**
17. One topic for each paragraph. A maximum of six sentences. Most paragraphs in an artifact have one to three.
18. If you have three or more parallel items, use a list or a table.
19. Put a warning or a risk before the item it applies to. Start it with the command or the consequence.
20. Numbers are digits with units and a time period: "$1.2M ARR in the third quarter", not "strong revenue". Compare each key number with something (target, last period, plan).
21. Dates are absolute: "14 June", not "next Friday" or "soon".

**B2B additions (opinionated)**
22. Lead with the answer. No background before the verdict.
23. Each action has one named owner and one date. "The team" is not an owner.
24. Say what you do not know. Use "Not in the source" instead of a guess.
25. Headings are statements, not labels: "Churn increased in SMB" tells more than "Churn overview".
26. Remove sender-centric filler: "I hope this helps", "As discussed", "Here is a summary of".

**Where the writing rules meet the fidelity rules**
- **Quotes.** A direct quote from the source stays word for word, in quotation marks, with the speaker. The writing rules do not apply inside the quotation marks. Quote only when the exact words matter.
- **Opinion.** State an opinion as an opinion with its owner: "Lior thinks that the price is not the real problem."
- **Uncertainty.** Keep it, in simple words: "possibly", "about", "Tomer estimates".
- **Renamed terms.** When rule 1 makes you replace a word of the source ("logos" becomes "accounts"), record the change in "Assumptions and gaps".
- **Relative dates.** Change "by Friday" to the absolute date, calculated from the date of the source. Show the original words adjacent to it ("9 October · the notes say 'by Friday'"). If the source has no date and the work is clearly current, calculate from the date of today and add the `assumed` tag. If you cannot calculate, keep the original words in quotation marks.
- **Missing owner or date.** Do not invent one. If the ask has no deadline, write "Deadline: not in the source". If a date has no year, add the year that fits and record the assumption one time. Write "Owner: not in the source". You can propose an owner only with the `assumed` tag, and then ask the human about it. If many rows in one block have the same gap, say it one time for the block.
- **"We" and "our".** If you know the name of the company, use the name. A forwarded artifact must be clear to a reader outside the team.
- **Two owners in the source.** Keep the two names. Do not select one.
- **Layer 3.** The same rules apply, but lists of gaps and sources can be short fragments.

**Other languages.** If the source or the recipient uses a different language, write the artifact in that language and apply the same rules in spirit: short active sentences, one word for one thing, no idioms, absolute dates. Translate all visible labels: the banner, the tabs, the fold names, the tags, and the `L` strings in the script. For a right-to-left language (Hebrew, Arabic), set `lang` and `dir="rtl"` on the `html` element, and wrap Latin terms and numbers that can change order in `bdi`. The check script finds style problems only in English; for other languages it gives the read time and the number check, and you check the style by eye.

## Fidelity rules (the lawyer part)

The human will sign this. A wrong number that looks good is worse than slop.

- Each number, date, name, and quote in the artifact comes from the source.
- You can calculate a number when the recipient needs it to compare (a ratio, a difference, a total). Add the `calculated` tag and show the calculation in "Method and calculations". The proportions of a chart bar are not a calculation.
- Do not invent data to fill a chart or a tile. If a field is missing, write "Not in the source".
- If the source contradicts itself, show the two values with the `conflict` tag. Do not select one silently.
- Tags: `assumed` (your assumption), `proposed` (your recommendation), `calculated`, `unverified` (the source gives a claim with no evidence), `conflict`, `not in source`. Put the tag immediately after the item it applies to. These tags use the neutral `.tag` style or `.tag.warn`. Keep `.tag.ok` and `.tag.bad` for status.
- **Your own proposal.** If the human asks what to decide and the source recommends nothing, you can add a recommendation. Give it the `proposed` tag, with the reason in one sentence. Do not mark an option as the pick of the source when the source did not select one.
- **Status colors are a judgment.** Use the status words of the source if it has them. If you assign green/yellow/red, record the rule you used in "Assumptions and gaps".
- A conflict about a key number goes where that number is, also on top. Do not hide it in layer 3. A conflict tile shows the two values ("$310K or $335K") with the `conflict` tag and the two sources in its label.
- When you cut something, move it to "Cut" in layer 3. The human can restore it. Do not delete content silently.
- Do not make the content stronger or weaker. "May" stays "may". "Three of five customers" does not become "most customers".
- Layer 3 has a Sources block: the name of each source and its date.
