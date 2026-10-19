# Chinese-speaking writers: habits to look for

Use this for every writer whose first language is Chinese: Mainland, Taiwan, Hong Kong, Singapore, Malaysia or overseas. Then add the regional file if one applies (`chinese-tw-hk.md`, `singapore.md`).

Each habit has a **slug** for the notebook. Explain the habit in the user's language and, when it helps, name the Chinese pattern behind it ("这是'通过……'句式直译过来的"). Learners remember a rule better when they see where the mistake comes from.

## Contents

1. Habits from Brittman's study of 200+ papers
2. Grammar that Chinese doesn't mark
3. Word choice: false friends and literal translation
4. Chinese-style openers and filler
5. Structure and logic
6. Email habits
7. Punctuation and mechanics

---

## 1. Habits from Brittman's study

Felicia Brittman analyzed more than 200 English papers by Chinese engineering graduate students and published *The Most Common Habits from more than 200 English Papers written by Graduate Chinese Engineering Students*. It has circulated in Chinese universities for two decades. The habits below follow her list, summarized in our own words with new examples. They show up just as often in industry reports.

| slug | Habit | Example → fix | Why |
|---|---|---|---|
| `article` | Articles (*a, an, the*) left out, added where they don't belong, or the wrong one. Brittman found this the single most common problem. | *Results show that proposed method reduces error.* → *The results show that **the** proposed method reduces **the** error.* | Chinese has no articles. Rule of thumb: a singular countable noun almost always needs *a*, *the* or another determiner; use *the* when the reader knows which one. |
| `long-sentence` | Very long sentences: several clauses chained with commas, often 50+ words. | Split at each new idea; aim for 15–25 words on average. | Chinese tolerates long comma-joined sentences (一逗到底). English readers lose the subject. |
| `data-in-sentence` | Many values or parameters packed into one sentence. | *The length, width, height, mass and density were 2 m, 1 m, 0.5 m, 30 kg and…* → a table or a list. | The reader has to pair values with names in their head. |
| `front-loaded-purpose` | Purpose, reason or location placed before the main clause. | *In order to improve accuracy, based on the dataset in Section 2, this study proposes…* → *This study proposes … to improve accuracy.* | Chinese puts background first. English puts the main clause first and the reader knows what the sentence is about. |
| `time-clause-opener` | Sentences opening with a long *when/after/as* clause. | *When the temperature is increased to 80 °C, as shown in Fig. 3, the yield …* → *Fig. 3 shows that the yield … when the temperature reaches 80 °C.* | Same as above. |
| `subject-not-first` | The important subject is buried in the middle. | Move the thing the sentence is about to the front. | English readers treat the first noun as the topic. |
| `which-ambiguous` | *Which* with an unclear antecedent. | *The sensor is mounted on the frame, which reduces noise.* (Does the frame or the mounting reduce noise?) → *Mounting the sensor on the frame reduces noise.* | *Which* usually points to the nearest noun. |
| `respectively` | *Respectively* misused or in the wrong place. | *A and B are respectively 3 and 5* → *A and B are 3 and 5, respectively.* Use it only to pair two parallel lists. | Readers expect it at the end, after the second list. |
| `in-this-paper` | *In this paper / In this study* repeated in every paragraph; *paper* and *study* used interchangeably. | Use *this study* for the research and *this paper* for the document. Say it once in the introduction. | Repetition. The reader already knows which paper they're reading. |
| `numeral-start` | A sentence that starts with a numeral or abbreviation; numerals for small general counts. | *12 samples were…* → *Twelve samples were…*; *Fig. 2 shows* at sentence start → *Figure 2 shows* (in many styles). | Most style guides spell out numbers at sentence start. |
| `symbol-in-text` | Math symbols in running text. | *the error is > 5%* → *the error is greater than 5%*. | Symbols belong in equations. |
| `figure-style` | *Fig.* / *Figure* / *figure* mixed, *showed as Fig. 2*. | Pick one style the target journal uses; write *as shown in Figure 2*. | Inconsistency looks careless. |
| `italic-variable` | Variables not italicized in text. | *t* = time, *x*. Units and labels stay roman. | Standard math typesetting. |
| `mid-capital` | Capital letters in the middle of a sentence. | *As shown in Table 1, The …* → *the*. | Usually a leftover from editing. |
| `such-as-etc` | *Such as … etc.* used together. | *such as A, B, C, etc.* → *such as A, B and C*. | *Such as* already means "examples, not a full list". |
| `uncountable-plural` | Plural *-s* on uncountable nouns. | *informations, equipments, softwares, researches, feedbacks, advices, knowledges, staffs, evidences* → no *-s*; use *pieces of / items of* if you need a count. | Chinese nouns don't mark number, so learners mark it everywhere. |
| `redundancy` | Words that repeat the meaning. | *future plan, final conclusion, past history, research work, mutual cooperation, completely eliminate, the reason is because* → *plan, conclusion, history, research, cooperation, eliminate, the reason is that*. | Many Chinese compounds pair near-synonyms (研究工作). English drops the extra word. |
| `by-this-way` | *By this way* / *in this method*. | → *This way*, *In this way*, *By doing this*, *Using this method*. | *Way* takes *in* or nothing, not *by*. |
| `how-to-start` | A sentence starting with *How to…* as a subject. | *How to reduce noise is a problem.* → *Reducing noise is difficult.* / *A key problem is how to reduce noise.* | *How to* can't be the subject of a full sentence in formal writing. |
| `obviously` | *Obviously, clearly, it is obvious that.* | Delete. If it's obvious, the reader doesn't need to be told; if it isn't, the word annoys them. | Reviewers read it as overclaiming. |
| `our-country` | *Our country, at home and abroad, domestic.* | → *China*, *in China and elsewhere*. | The reader may not be in China. Name the place. |
| `that-is-to-say` | *That is to say*, *namely* used to restate. | Usually delete the restatement; if needed, *that is* or *i.e.* in parentheses. | It often repeats the previous sentence. |
| `too-at-end` | *…, too.* at the end of a formal sentence. | → *also*, before the verb. | *Too* at the end sounds conversational. |

## 2. Grammar that Chinese doesn't mark

| slug | Habit | Example → fix |
|---|---|---|
| `tense` | Tense missing or inconsistent, because Chinese uses time words instead. | *Yesterday we discuss the plan.* → *discussed*. In papers: methods and results in past tense, established facts and what a figure shows in present. |
| `agreement` | Third-person *-s* missing; subject and verb don't agree. | *The model predict…* → *predicts*; *The number of samples are…* → *is*. |
| `there-be-verb` | *There is/are* + a second verb. | *There are many people think…* → *Many people think…* |
| `topic-comment` | Topic stated, then repeated as a pronoun. | *This problem, we will solve it next week.* → *We will solve this problem next week.* |
| `dangling-through` | *Through / By / Based on* + noun, then a subject that doesn't do the action. 通过……使/表明. | *Through the experiment, it shows that…* → *The experiment shows that…*; *Based on the data, the conclusion is…* → *The data suggest that…* |
| `double-connector` | *Although … but*, *Because … so*. | Keep one connector: *Although A, B.* / *Because A, B.* / *A, so B.* |
| `verb-pattern` | Wrong pattern after a verb. | *suggest him to do* → *suggest that he do* / *recommend that he*; *let me to know* → *let me know*; *explain me* → *explain to me*; *reply me* → *reply to me*. |
| `preposition` | Wrong or extra preposition. | *the effect to* → *effect on*; *discuss about* → *discuss*; *emphasize on* → *emphasize*; *contact with* → *contact*; *arrive to* → *arrive in/at*; *in the other hand* → *on the other hand*. |
| `adj-as-verb` | Adjective used as a verb. | *I am very appreciate* → *I really appreciate it* / *I am very grateful*; *It will benefit to* → *It will benefit…* |
| `passive-missing` | Things "doing" what is done to them. | *The delivery will delay* → *will be delayed*; *The problem has solved* → *has been solved*. |
| `proper-noun-article` | *The* with country names that don't take it, or missing where needed. | *the China* → *China*; *United States* → *the United States*; *the Tsinghua University* → *Tsinghua University*. |

## 3. Word choice: false friends and literal translation

| slug | Chinese | Common mistake | Usually better |
|---|---|---|---|
| `realize` | 实现 | *realize the function / goal* | *implement* a function, *achieve* a goal. *Realize* mostly means 意识到. |
| `put-forward` | 提出 | *put forward a method* | *propose*. *Put forward* is fine for ideas in debate, odd for your own method. |
| `adopt` | 采用 | *adopt the method* | *use*, *apply*. *Adopt* is fine for policies and standards. |
| `carry-out` | 进行 | *carry out an analysis of*, *make a comparison*, *do research on* | the verb: *analyze*, *compare*, *study*. Nominalized verbs make sentences long and vague. |
| `play-role` | 起……作用 | *plays an important role in* in every paragraph | Say what it does: *controls*, *limits*, *is needed for*. |
| `improve-level` | 提高水平 | *improve the level of safety* | *improve safety*. |
| `check-problem` | 检查问题 | *check the problem* | *look into*, *investigate*. *Check* = verify quickly. |
| `learn-knowledge` | 学习知识 | *learn knowledge* | *learn*, *gain knowledge of*, *learn about*. |
| `open-light` | 开灯 | *open the light / computer* | *turn on*. |
| `point-out` | 指出 | *As pointed out by Zhang* (for any citation) | *Zhang showed / reported / argued*: choose the verb that matches what the source did. |
| `significant` | 显著 | *significant* for "large" in a paper | In papers *significant* implies a statistical test. Otherwise *substantial*, *large*, *marked*. |
| `cause` | 造成 | *caused an improvement* | *cause* is mostly negative; *led to*, *resulted in* for neutral or good outcomes. |
| `solve` | 解决 | *completely solved the problem* | *addressed*, *reduced*, *mitigated*, unless it's truly solved. |
| `noun-compound` | 钢材表面缺陷检测 | *defect detection of steel surface* | *steel surface defect detection*: technical terms usually stack modifiers before the head noun. |
| `vague-word` | 效果、问题、情况 | *the detection effect*, *the situation of the system* | Say which: *detection accuracy*, *speed*, *the system's load*. |
| `idiom-literal` | 成语 | Literal translation of 四字成语 (*make persistent efforts*, *a long way to go*) | State the actual meaning plainly. |

## 4. Chinese-style openers and filler

These come from Chinese school essay templates and are easy to spot.

| slug | Opener | Fix |
|---|---|---|
| `with-development` | *With the development of (technology / economy / society)…* (随着……的发展) | Delete it and start with the specific change: *Since 2020, the number of … has tripled.* |
| `more-and-more` | *More and more people / attention…* (越来越多) | *A growing number of*, *increasingly*, or give the number. |
| `in-recent-years` | *In recent years, …* as a reflex opener | Give the years, or delete. |
| `well-known` | *It is well known that…*, *As we all know…* | Delete. If everyone knows it, cite it or skip it. |
| `nowadays` | *Nowadays, …* | *Today* or *currently* if needed; usually delete. |
| `in-a-word` | *In a word*, *In one word* (总之) | *In short*, *Overall*, or end on the conclusion itself. *In a word* introduces one word. |
| `whats-more` | *What's more*, *Besides* in formal writing | *In addition*, *Also*, or nothing. |
| `last-but-not-least` | *Last but not least* | *Finally*. |
| `overclaim` | *for the first time in the world*, *fills the gap*, *perfectly solves*, *greatly improves* (填补空白、首次) | *To our knowledge, this is the first…*; give the number for "greatly". Reviewers distrust unhedged firsts. |
| `it-is-found` | *It is found that…*, *It can be seen that…* (可以看出) | *We found that…*, *Figure 3 shows…* Active voice with *we* is accepted in most journals. |

## 5. Structure and logic

- **Conclusion last** `conclusion-last`. Chinese writing often builds context and arrives at the point at the end. English reports, emails and abstracts put the conclusion or request first. Point it out and show the reordered outline.
- **Comma splice** `comma-splice`. Two full sentences joined by a comma: *The test failed, we will repeat it.* → period, semicolon, or *so*.
- **On the one hand…** `one-hand` used for two points that don't contrast. Use it only for opposing sides; otherwise *First… Second…* or nothing.
- **Parallel claims without connection.** Several sentences that each state a fact, with no *because, so, however* to show how they relate. Ask what the link is.
- **Hedging extremes.** Either *proves* and *definitely*, or a stack of *may possibly perhaps*. One hedge per claim, matched to the evidence: *shows* (strong), *suggests* (moderate), *may* (weak).

## 6. Email habits

| slug | Chinese source | Common mistake | Natural |
|---|---|---|---|
| `dear-teacher` | 王老师 | *Dear Teacher Wang* | *Dear Professor Wang* / *Dear Dr. Wang* |
| `mr-given-name` | 张伟先生 | *Dear Mr. Wei*, *Dear Mr. Zhang Wei* | *Dear Mr. Zhang* (title + family name only) |
| `sorry-disturb` | 打扰了 | *Sorry to disturb you.* | *Sorry to bother you*, or just skip it and be brief. |
| `please-check` | 请查收 | *Please check it.* / *Please check the attachment.* | *I've attached the report.* / *Please find the report attached.* |
| `wish-you` | 祝您…… | *Wish you have a nice day.* / *Wish you all the best!* in work email | *Have a good day.* / *Best regards,* |
| `reply-asap` | 请尽快回复 | *Please reply me as soon as possible.* | *Could you reply by Thursday?* A date is clearer and more polite. |
| `question-want-ask` | 我有个问题想问您 | *I have a question want to ask you.* | *I have a question about…* |
| `kindly-help` | 麻烦您帮忙 | *Thanks for your kindly help.* | *Thank you for your help.* (*kind* is the adjective) |
| `hope-everything` | 希望一切顺利 | *Hope everything goes well with you.* | Fine in a personal note; in work email, delete. |
| `long-intro` | 自我介绍 | Three lines of who you are before the request | One line of who you are, then the request. Details after. |

## 7. Punctuation and mechanics

`fullwidth-punct`: Chinese input methods leave full-width characters in English text.

| Wrong | Right |
|---|---|
| ， 。 ： ； ？ ！ | , . : ; ? ! followed by one space |
| （ ） | ( ) with a space before the opening parenthesis |
| “ ” used with full-width spacing | " " or ' ' |
| 、 (enumeration comma) | , |
| …… | … or ... |
| —— | an em dash — or, better, a comma or period |
| 《书名》 | *Italics* for titles |

Also check: no space between English words and parentheses (*method(see*), double spaces, half-width and full-width digits mixed.
