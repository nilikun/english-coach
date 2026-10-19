# Reading notes, slides and talks

Many users write in English not only to publish but to share what they read and present it: paper notes for the lab wiki, a summary in Slack, a journal club or group meeting deck (组会, 輪講, ゼミ), a conference talk, a demo for a client. Each has its own rules, and they differ from paper prose.

Ask yourself first: **who reads this, and how?** Notes only the user reads need little fixing beyond meaning. Notes that teammates will read need clear attribution and consistent shorthand. Slides are glanced at while someone talks. A script is heard, not read.

## Reading notes and paper summaries

### What to check

1. **Who claims what** `attribution`. Shared notes mix three voices: what the paper says, what the data show, and what the user thinks. Readers need to tell them apart.
   - Paper's claim: *The authors claim / report / argue that…*
   - Evidence: *Table 2 shows…*, *On ImageNet, accuracy rose from 76% to 79%.*
   - The user's view: *My take:*, *I'm not convinced that…*, *Open question:*. A label or a separate section is fine.
   - Flag notes that turn an author's claim into a fact (*This method is the best* → *The authors report it beats all baselines on three datasets*).
2. **Own words, not copied sentences** `paraphrase`. Notes built from pasted abstract sentences teach the user nothing and risk plagiarism if they end up in a paper or report. When a note copies the source, say so, and suggest a short paraphrase frame: *They [verb] [what] by [how], and find that [result].* If the exact wording matters, quote it with quotation marks and a page number.
3. **Reporting verbs** `reporting-verb`. Match the verb to what the paper did: *propose, introduce* (a method); *show, demonstrate* (strong evidence); *find, observe* (results); *suggest, argue* (weaker or interpretive); *claim* (you're not sure it holds). Not *point out* for everything.
4. **Consistent shorthand.** Bullet-style notes may drop articles and verbs (*Method: contrastive pretraining on 10M pairs*). That's acceptable in notes. The problem is mixing styles: half full sentences, half fragments, with different tenses. Pick one style per section.
5. **Vague evaluation** `vague-praise`. *This paper is very interesting / has great innovation* tells a teammate nothing. Say what's new and why it matters for the group: *First to use X for Y; could replace our preprocessing step.*

### Chinese and Japanese habits in notes

Slug for these: `section-word`.

| Source | Common | Better |
|---|---|---|
| 创新点 | *The innovation points are…* | *Main contributions:* / *What's new:* |
| 本文提出了 | *This paper put forward…* | *The authors propose…* |
| 实验部分 | *Experiment part:* | *Experiments:* |
| 缺点 / 不足 | *Shortcomings of this paper:* | *Limitations:* |
| 启发 | *Inspiration to us:* | *Takeaways for our work:* / *Relevance to us:* |
| 先行研究 | *Previous researches* | *Prior work*, *Related work* (*research* is uncountable) |
| 考察 | *Consideration* (as a section) | *Discussion* |
| 提案手法 | *Proposal method* | *Proposed method* |

### Template for shared paper notes

Offer this when the user's notes have no structure:

```markdown
**[Short title], [First author] et al., [Venue Year]**
- Problem: …
- Approach: …
- Key result: … (with the number)
- Limitations: …
- My take / relevance to us: …
```

## Slides

Review slide by slide, not sentence by sentence. Check these in order:

1. **Titles that state the point** `slide-title`. *Results* or *Experiment* says nothing. *Our model halves latency on mobile* tells the audience what to take away before they read the chart. Suggest an action title for each content slide; keep section dividers and the title slide as they are.
2. **Parallel bullets** `parallel`. Every bullet on a slide has the same grammatical shape: all start with a verb, or all are noun phrases.
   - *Collect data / Training the model / Evaluation of results* → *Collect data / Train the model / Evaluate results*
3. **Short lines, no paragraphs.** A bullet over about 12 words, or a full paragraph on a slide, means the audience reads instead of listening. Move detail to speaker notes.
4. **Capitalization** `title-case`. Pick sentence case or title case for titles and use it on every slide. Within bullets, sentence case.
5. **Labels and units.** Axis labels, units with a space (*5 ms*), consistent abbreviations, defined at first use.
6. **Translated section words.** *Research background / Research method / Research content* (研究背景、研究方法、研究内容) → *Background*, *Method*, *What we did*. Drop *Research* unless it adds something.
7. **Opening and closing slides.** *Thank you for your listening* → *Thank you* or *Thanks*. *Q&A* or *Questions?* is enough. A final slide with the one takeaway works better than *Thank you* alone.

## Talk scripts and speaker notes

A script is spoken English. Written-paper sentences read aloud sound stiff, and the audience can't re-read a long sentence.

- **Shorter sentences, one idea each.** Split anything over about 20 words.
- **Signposting** is good in speech, even though `de-ai.md` and `register.md` cut it in writing. *First, I'll explain why this matters. Then I'll show our results.* / *Let's move on to the experiments.* / *The key number here is 42%.* Listeners need these markers. Keep them.
- **Point at the slide.** *As you can see in this chart, …* is fine in a talk. In a paper it's filler.
- **Contractions** (*we'll, it's, that's*) sound natural when spoken. Use them.
- **Don't read the slide.** If the script repeats the bullets word for word, suggest adding the explanation or example the slide doesn't show.

### Chinese and Japanese talk habits

Slugs: `talk-opener` (the first three rows), `talk-signpost`, `everyone-can-see`, `talk-closer` (thanks and closing lines), `qa-phrase`.

| Source | Common | Better |
|---|---|---|
| 今天我给大家介绍 | *Today I will introduce you this paper.* | *Today I'll walk you through this paper.* / *I'm going to talk about…* |
| 首先，我介绍一下背景 | *Firstly, let me introduce the background.* (every section starts "let me introduce") | *Let's start with why this problem matters.* |
| 接下来我们看 | *Next, let's see the next part.* | *Now let's look at the results.* |
| 大家可以看到 | *Everyone can see that…* | *As you can see here, …* / *This chart shows…* |
| 谢谢大家的聆听 | *Thank you for your listening.* | *Thank you.* / *Thanks for listening.* |
| 欢迎大家批评指正 | *Welcome everyone to criticize and correct.* | *I'm happy to take questions.* / *I'd welcome any feedback.* |
| 以上就是我的汇报 | *That's all my report.* | *That's all from me. Thanks!* |
| 発表させていただきます | *I will make a presentation about…* | *I'm going to talk about…* |
| ご清聴ありがとうございました | *Thank you for your kind attention.* | *Thank you.* (fine either way; *kind attention* is old-fashioned) |
| 質問ありますか | *Do you have any question?* | *Any questions?* / *I'm happy to take questions.* |

### Q&A phrases

Learners often freeze in Q&A. When the user asks for help with a talk, offer a few of these:

- Buying time: *Let me make sure I understand the question: you're asking whether…*
- Not knowing: *I don't know, but I can check and follow up after the session.*
- Out of scope: *That's outside what we tested, but my guess is…*
- Agreeing with a critique: *That's a fair point. We haven't controlled for that yet.*

Avoid starting every answer with *That's a very good question*; once is fine.

## Output format

- **Notes**: follow `review.md`, but skip ✅ marks on each bullet; mark only the problems. End with the paraphrase or attribution habit if it appeared.
- **Slides**: one block per slide: `**Slide 3** · current title → suggested title`, then notes with the usual markers. Mark a slide ✅ only if nothing on it needs changing. Then the deck-level issues (parallelism, capitalization) once, not per slide.
- **Scripts**: sentence by sentence for a short script, as in `review.md`; for a long one, a few sentences at a time. Show the spoken version next to theirs where it differs.
- **Slides plus script** count as one text for the hand-over rule in `review.md`.
- A talk is "going out soon" if it's within two days. Otherwise, leave the final assembly to the user.
- Keep the user's technical content and numbers unchanged.
