# Review loop and signature

Read this page after the first version is published, and each time the human sends feedback.

## Review loop

AI makes the first version in a minute, and it is almost never fully correct. The human must do the editorial work. Make that work easy:

- Put `data-block` on each unit that the human can want to cut or fix alone: a block, an option, and also a single row or action when the rows are the content. Each one gets review controls.
- Do not put `data-block` on a container and also on its rows. Select one level.
- Each block in the artifact has review controls (Keep / Cut / Fix / Move up + note) in Review mode. The **Copy feedback** button builds a text block with the marker `[kill-the-wall-of-text · review vN]`. The human pastes it in chat.
- When you receive that marker, or feedback in plain words, apply each item: cut the block (move it to "Cut" in layer 3), fix it, or move it up. Then publish again to the same location.
- The human can name a block, a tab, a tile, or use free words. A tab name applies to all of the blocks in that tab. If a name is ambiguous, ask.
- "Move up" means: put it nearer to the top. Use the note for the exact position. With no note, move it one position up in its tab, or make it the first tab.
- "Cut" with a note such as "keep only X" is a partial cut: keep X, and list each removed item in "Cut" in layer 3. An item that you remove from the top, but that stays in the body, needs no "Cut" entry.
- Ask a maximum of one question for each turn, and only if you have a real one. Good questions: "Is this the correct verdict?" · "Which of these three numbers matters most to [recipient]?" · "Can I cut [block]?"
- After each publish: one line about what changed. Do not repeat the content of the artifact in chat.
- Edit the current artifact. Do not build it again from zero.

## Signature

When the human says the artifact is correct ("ship it", "looks good", "approved"), ask once: "Did you read all of it, and do you stand behind it?" On yes, publish the signed version to the same location: change the banner to **Signed by [name], [date]** (the name of the human, the date of today) and remove Review mode (see the fill rules). Do not write a signature that the human did not give. If the human sends without a signature, the Draft banner stays.

## Special cases

- **Two or more recipients.** Write the top for the person who must decide or act. If different persons have different actions, the ask has one short line for each person, with a maximum of three lines. A second group with a different need gets the first tab, or a tile that points to it. Do not write two verdicts.
- **The recipient is the user.** Write "For NAME" in the header and address the user as "you". The signature is then optional.
- **No action for the recipient.** The ask says that: "No action. Read the top." If the action belongs to the sender, say who acts. Do not invent an ask.
- **A "final" or "send-ready" request.** The procedure stays the same. Deliver the best draft and say in one line that it is a draft until the human signs it.
- **The human is not there.** Continue with labeled assumptions. Name the assumption with the largest effect in one line of chat.
