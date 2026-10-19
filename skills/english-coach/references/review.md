# Review mode

The user wrote something in English and wants it better. Show them what to change and why, one sentence at a time, so the next draft has fewer of the same problems.

## How much detail

Pick the depth by length. Annotating every line of a 4,000-word paper produces a wall of notes nobody reads.

| Length | What to do |
|---|---|
| Short: about 250 words or 12 sentences or fewer | Go sentence by sentence. Mark clean sentences ✅. |
| Medium: about 250–1,200 words | Start with an overall diagnosis. Annotate only the sentences with issues; list the clean ones by number in one line. |
| Long: over 1,200 words, or a whole paper or report | Diagnose section by section, then give the top 3–5 habits, each with two examples from the text. Offer to go sentence by sentence on one section the user picks. |

If the user asks for full sentence-by-sentence on a long text, do it in chunks (one section per reply) and ask before continuing.

## Markers

Use these five markers so the user can see at a glance what kind of problem each note is.

| Marker | Meaning | Example |
|---|---|---|
| ❌ | **Error**: grammar or usage a native reader sees as a mistake | *informations*, *discuss about*, missing article |
| ⚠️ | **Unnatural**: grammatical, but no native writer would put it this way; usually first-language transfer | *With the development of AI, …*, *by this way*, *Wish you have a nice day* |
| 🗣️ | **Register**: wrong formality for this reader (too casual, too stiff, or regional) | *Pls revert ASAP*, *Kindly be informed that* |
| 🤖 | **AI pattern**: reads machine-written | *I hope this email finds you well*, *delve into*, *a pivotal role* |
| 💡 | **Better**: optional improvement in clarity, concision or structure | splitting a 60-word sentence, putting the request first |

After the marker, give a short label in the user's language and a stable slug in backticks (e.g. ⚠️ **冠词** `article`). The slug lets the notebook count habits across sessions. Use the slugs listed in the first-language files when one fits; otherwise make a short kebab-case one and reuse it consistently.

## Template

Write the labels and explanations in the user's language. This example is 简体中文.

```markdown
**场景**：写给导师的周报邮件 · 分子生物学 · 母语：简体中文（如果判断有误请告诉我）
**总体**：内容清楚，下一步计划也写了。主要问题是时态和两处中文结构直译。

---

**①** This week I have done the western blot experiment, the result is not good.
**→** This week I ran the western blot, but the results were not good.
- ❌ **逗号连句** `comma-splice`：两个完整的句子不能只用逗号连起来，用 *but* 或句号。
- ⚠️ **搭配** `collocation`：实验用 *run* 或 *perform*；*do the experiment* 偏口语。
- ❌ **时态** `tense`：说的是这周已经出来的结果，用过去时 *were*。

**②** ✅ 没问题。

**③** I think the reason is because the antibody concentration is too low.
**→** I think the reason is that the antibody concentration was too low.
- ⚠️ **"原因是因为"** `redundancy`：*reason* 已经是"原因"，后面用 *that*，不用 *because*。

**④** Next week I will discuss with Dr. Chen about the new protocol.
**→** Next week I will discuss the new protocol with Dr. Chen.
- ❌ **多余的介词** `preposition`：*discuss* 后面直接接讨论的内容，不加 *about*。

---

**这次最值得改的 3 个习惯**
1. **时态**（①③）：已经发生的事用过去时。中文靠"了""这周"表示时间，英文要改动词。
2. **逗号连句**（①）：两个完整句子之间用句号、分号或连词。
3. **"原因是因为"这类重复**（③）：*reason is that*、*discuss X*。

要不要我建一个错题本，记下你常犯的问题，下次重点检查？

**轮到你**
用 ①③ 的规则写一句新的："上周的结果也不好，原因是样本量太小。"
```

## Going out soon

If the text goes to its reader within a day or two, or the user asks for a version they can send:

- Give every correction directly. Skip the hand-over rule below; don't make the user solve puzzles on a deadline.
- After the sentence notes, add the **full corrected text**, ready to copy, with [brackets] for anything only the user knows.
- Make **轮到你** a *new* practice sentence that uses the top habit, so the practice doesn't block their send.

For anything later (a draft, a paper weeks from submission), use the normal flow and leave the assembly to the user.

## Slugs

Use these shared slugs for problems that occur in any first language, so the notebook counts them the same way across sessions. First-language files and `de-ai.md` add their own.

`article` · `plural` · `uncountable-plural` · `tense` · `agreement` · `preposition` · `verb-pattern` · `collocation` · `passive-missing` · `comma-splice` · `long-sentence` · `double-connector` (*because… so*, *although… but*) · `redundancy` · `word-choice` · `missing-words` · `term-consistency` · `vague-word` (*effect*, *thing*, *problem* where a precise word exists) · `exact-date` · `percentage-point` · `too-blunt` · `over-polite` · `request-last` · `fullwidth-punct`

Make a new kebab-case slug only when none of these or the loaded files fit, and reuse it for the rest of the conversation.

## Writing the explanation

A good explanation does one of these:

- **States a rule**: "When you mean *in this specific study*, use *the*; the reader already knows which study."
- **Describes the reader's reaction**: "A native reader sees *by this way* and stops to reparse it. *This way* or *by doing this* reads smoothly."
- **Contrasts two words**: "*Propose* puts forward an idea; *suggest* is softer. Reviewers expect *propose* for your own method."
- **Names the transfer**: "这是中文'随着……的发展'直译过来的。英文读者觉得这是空话，直接写变化本身。"

Avoid explanations that only say "more natural", "better", "more formal" or "more native". If you can't say why, you may be flagging a preference. Say it's a preference, or drop it.

Keep each explanation to one or two lines. If a point needs a paragraph, it's probably a habit; save the long version for **这次最值得改的习惯**.

## Correcting a sentence

- Give **one** recommended rewrite per sentence. Add an alternative only when the choice depends on something the user knows (tone, what they meant). Say what decides between them.
- Change as little as possible. If only the article is wrong, fix only the article. A rewrite that changes every word teaches nothing about which words were wrong.
- Keep technical terms, names, numbers and claims exactly as written, unless a term itself is wrong (then explain).
- If the fix needs information only the user has (which paper, what result, the exact date), put a [placeholder] in the rewrite and say what goes there. Don't invent it. This is common with AI-drafted text, where the real problem is missing content.
- Flag a number or term that may change the meaning (*3.2% higher* vs *3.2 percentage points higher*) as the first thing in the **总体** line, and ask the user to confirm.
- If a sentence is too tangled to fix by editing, say so, show the split into 2–3 sentences, and explain where the break points are.
- Leave acceptable variants alone: British or American spelling (just keep it consistent), the serial comma, *data is/are* in business writing, *we* in academic writing.

## Repeated habits: correct twice, then hand over

When the same habit appears three or more times, correct the first two fully. For later occurrences, put a hint at that sentence instead of the answer ("same article issue here: which noun needs *the*?"). You can leave ___ blanks inside the rewrite for the part the user should fill. Related slugs count as one habit for this rule (four literal set phrases from Japanese email are one habit).

This is the core of the coaching. Spotting the pattern on your own makes it stick.

Skip this and give every answer when the text is going out soon (see above) or the user asks for all corrections. **轮到你** then asks the user to fill in those blanks or rewrite those sentences, as one step.

## One-off errors that matter most

The habits section lists repeated problems. A single error can still be the most important one: a wrong name in the greeting, a number that changes meaning, *revert* to a reader who will take it literally. Mention it in the **总体** line at the top so it isn't lost among the notes.

## Short text that is mostly AI-style

If a short text is AI-flavored throughout, go sentence by sentence (the user wants to see where), but for the second half, give hints and a frame instead of rewrites, and make **轮到你** "rewrite this paragraph in your own words". See `de-ai.md`.

## Structure and flow

After sentence-level notes, look at the whole piece once:

- Is the main point or request where the reader expects it? English work writing usually puts it first. Chinese and Japanese drafts often build context first and ask at the end.
- Does each paragraph do one job?
- Are transitions doing work, or are they decoration (*Moreover*, *Furthermore*, *In addition* in every paragraph)?

Mention structure in at most three lines unless it's the main problem.

## Mechanics checklist

Check these quickly; they're easy marks lost:

- Full-width punctuation in English text: ，。：；“”（）、—— → , . : ; " " ( ) and a real dash or a comma.
- Missing space before an opening parenthesis or after a comma or period (*method(see Fig. 1)*, *results,which*).
- Number and unit spacing (*5 kg*, *30 %* → *30%* in most styles).
- Sentence starting with a numeral (*12 samples were…* → *Twelve samples were…*).
- Inconsistent capitalization of terms; a capital letter in the middle of a sentence.
- Names: *Mr.* + family name only (*Mr. Wang*, not *Mr. Wei*); one honorific (not *Mr. Tanaka-san*).

## After the review

- If the user sends back a rewrite, check it quickly: say what they got right first, then any remaining issue. Update the notebook (`references/notebook.md`).
- If the domain vocabulary was a big gap, offer a short word list (`references/vocab.md`) in one line.
