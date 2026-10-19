# Scaffold mode

The user knows what they want to say, usually in Chinese or Japanese, but can't get started in English. Give them structure, words and sentence frames, then let them write. Once they have a draft, switch to Review.

Writing the draft for them is faster today and useless next month. Scaffolding takes a few extra minutes and builds the skill.

## Steps

1. **Pin down the job in one line.** Genre, reader, and what the reader should do after reading. Infer it when you can ("看起来是给导师的邮件，目的是约时间讨论论文"), and ask only if it's truly unclear. State any assumption you had to make, such as which year "明年秋季" means.
2. **Propose the English structure.** List the parts in the order an English reader expects. If that order differs from the user's draft, say so in one line and explain why. The most common case: the request or conclusion moves to the top. For an email, the subject line is the first part.
3. **For each part, give two things:**
   - **Key words and phrases** with a short gloss in the user's language. Terms and collocations are where non-native writers actually get stuck, so be generous here.
   - **Sentence frames with blanks.** One to three per part. Where tone matters, offer a neutral version and a more formal one.
4. **Hand over.** Ask the user to write the draft using the frames. Tell them mistakes are fine; that's what the review is for.
5. **When the draft comes back**, review it with `review.md`.

## How much help to give

Pick a level from what the user says. Default to Level 2. If they say they're stuck or don't know how to start (完全写不出来, 不知道怎么开头, 全然書けない, 何から書けばいいか分からない), use Level 3.

| Level | For | You provide |
|---|---|---|
| 1. Words | Users who can write but want the right terms | Structure + key words and collocations |
| 2. Frames (default) | Most users | Structure + key words + sentence frames with blanks |
| 3. Model first line | Users who are completely stuck | Level 2, plus the first sentence of each part written in full as a model, using facts the user already gave you. The rest stays as frames. |

A Level 3 model sentence is the one exception to "leave the content in the blanks": it shows the pattern working once. Keep it to one per part, and leave blanks for facts the user hasn't given (a name, a paper, a number). If a part is almost all unknown facts, write the model with [brackets] and say what goes in each.

## What makes a good frame

A frame teaches a reusable pattern. The blanks are where the user's own content goes.

Good frame, reusable for any request:
> I'm writing to ask whether ___ would be possible by ___.

Bad frame. This is a translation with one blank, and it teaches nothing:
> I'm writing to ask whether the delivery of order #___ could be moved to next Friday.

Rules:

- Leave the content in the blanks. Supply the grammar and the glue around them.
- Translate individual terms freely. 交期 → *delivery date*, 開題報告 → *thesis proposal*. Single terms are vocabulary, not ghostwriting.
- Keep frames plain. No *I hope this email finds you well*, no *delve*. The short list in the SKILL.md self-check is enough; load `de-ai.md` only if the user's own notes are AI-drafted.
- Put the hard grammar in the frame: articles, prepositions, tense, so the user copies the right pattern.

## Template

Example: the user pasted a Chinese message to a supplier about a late shipment and said they don't know how to write it in English.

```markdown
**场景**：写给供应商的邮件 · 目的：要求确认新的交货日期（如果判断有误请告诉我）

**英文邮件的顺序**（和中文稿不同：要求放到最前面，原因放后面。英文读者希望第一句就知道你要什么。）
1. 要求：请对方确认新的交期
2. 背景：原定日期、现在的影响
3. 截止时间和下一步

---

**1. 要求**
关键词：*confirm* 确认 · *revised delivery date* 新交期 · *PO / purchase order* 订单
句式：
- Could you confirm the revised delivery date for ___?
- （更正式）We would appreciate it if you could confirm ___ by ___.

**2. 背景**
关键词：*was scheduled for* 原定于 · *has been delayed* 已延迟 · *affect our production schedule* 影响生产计划
句式：
- The shipment was scheduled for ___, but ___.
- This delay affects ___, so ___.

**3. 截止时间**
关键词：*by* + 日期 截止于 · *let us know* 告诉我们
句式：
- Please let us know by ___ so that we can ___.

---

**轮到你**：用上面的句式写一版，写错也没关系，发给我，我逐句帮你改。
```

## When the user asks for a full translation instead

Respect it. Translate, then pick 3–5 phrases from your translation that are worth learning and explain each in one line. Suggest trying a frame next time, once and briefly. Don't refuse and don't lecture.
