# Weekly report email with slide shorthand · Simplified Chinese

**Mode:** Review (medium + register) · **Writer:** Mainland Chinese data engineer · **Genre:** weekly status email to a manager in Singapore

The reply below is the skill's output, unedited.

## What the user sent

> 这是我要发给新加坡老板的周报（邮件），帮我看看英文
>
> Hi Kelvin,
>
> This week we got a lot of progress on the data pipeline. Latency ↓ 40% w/ new cache, and the error rate is kind of stable now. So, basically the migration is on track. BTW, the vendor API is still super slow, we think it's a big risk for the Q4 launch. Next week → finish load test + fix the remaining bugs.
>
> Thx!
> Wei

## What english-coach replied

**场景**：发给直属老板的周报邮件（公司内部）· 数据工程 · 母语：简体中文 · 默认这封马上要发，所以每处都直接给改法，最后附上可以直接复制的全文（如果判断有误请告诉我）
**总体**：内容是齐的：进展、数字（40%）、风险、下周计划都有，这是周报最重要的部分。问题主要在形式：↓ → + w/ 这类幻灯片符号，加上 So / basically / BTW / Thx 这些聊天口吻，读起来像随手发的消息，不像周报。最要紧的一处是 ⑤：Q4 上线的风险用 *BTW*（顺便说一下）引出来，老板很容易一眼略过去。

---

**①** Hi Kelvin,
✅ 没问题。写给新加坡的直属老板，*Hi* + 名字很常见，不用改成 *Dear*。

**②** This week we got a lot of progress on the data pipeline.
**→** This week we made a lot of progress on the data pipeline.
- ⚠️ **搭配** `collocation`：*progress* 的固定搭配是 *make progress*。*get progress* 是"取得进展"逐字翻过来的。
- 说明：*a lot of* 放在邮件里没问题，可以保留（正式报告和论文里才需要换掉）。

**③** Latency ↓ 40% w/ new cache, and the error rate is kind of stable now.
**→** Latency is down 40% with the new cache, and the error rate is now fairly stable.
- 🗣️ **邮件里用了幻灯片写法** `slide-in-prose`：↓、w/ 是 PPT 和聊天里的速记。邮件正文要写完整的句子：*is down 40%*、*with*。
- ❌ **冠词** `article`：*cache* 是可数名词，指的又是你们这次上的那个缓存，所以要加 *the*：*the new cache*。
- 🗣️ **口语里的含糊词** `spoken-in-writing`：*kind of* 是口语里的"有点、算是"。想表达"基本稳定"，就写 *fairly stable* 或 *mostly stable*。手上有数字的话，直接写 *has stayed around [x]% since [日期]* 最好，老板看数字比看形容词放心。
- 💡 可选：40% 是哪个指标？如果是 p95 或平均延迟，写成 *p95 latency is down 40% ([原值] → [现值] ms)*，信息更完整。

**④** So, basically the migration is on track.
**→** Overall, the migration is on track.
- 🗣️ **口语开头** `spoken-in-writing`：句首的 *So, basically* 是说话时的填充词，写进邮件显得随意，还会让 *on track* 这个结论听着不太确定。用 *Overall,* 或者直接从 *The migration is on track* 开头。
- 💡 这句是全封邮件的结论，挪到最前面（见下面的"结构"）。

**⑤** BTW, the vendor API is still super slow, we think it's a big risk for the Q4 launch.
**→** The vendor API is still very slow ([平均响应时间等数字]), and we think it's a big risk to the Q4 launch.
- 🗣️ **聊天缩写** `chat-in-email`：*BTW* 是"顺便一提"的意思，等于告诉老板"这条不重要"。可这是会影响 Q4 上线的风险，正好相反，应该单独成段、让人看到。直接删掉 *BTW*。
- ❌ **逗号连句** `comma-splice`：*…super slow, we think…* 是两个完整的句子，不能只靠逗号连。加 *and*，或者改成句号。
- 🗣️ **口语强调词** `spoken-in-writing`：*super* 是口语。改成 *very*，最好再补一个数字（比如响应时间），"慢"有多慢就清楚了。
- ⚠️ **介词** `preposition`：说"对……构成风险"，英文一般用 *a risk to* + 受影响的事情。
- 💡 **缺内容**：老板看到风险，下一个问题就是"打算怎么办 / 需要我做什么"。在后面加一句，比如 *We're [你们的应对措施]* 或 *Could you [需要老板做的事] by [日期]?*。这部分内容只有你知道，我先用方括号占位。

**⑥** Next week → finish load test + fix the remaining bugs.
**→** Next week, we'll finish the load test and fix the remaining bugs.
- 🗣️ **邮件里用了幻灯片写法** `slide-in-prose`：跟 ③ 一样，→ 和 + 换成完整句子：主语 *we'll*，加 *and*。
- ❌ **冠词** `article`：*load test* 指的是你们这次的压测，要加 *the*。*the remaining bugs* 你写对了 ✅。

**⑦** Thx! / Wei
**→** Thanks, / Wei
- 🗣️ **聊天缩写** `chat-in-email`：*Thx* 是聊天缩写，邮件里写全 *Thanks,*。结尾用逗号就行，不需要感叹号。

---

**结构**（英文周报的习惯是先给状态，再写完成了什么、风险、下一步，见 ④⑤）
1. 第一句给结论：*The migration is on track.*
2. 本周进展（②③）
3. 风险单独一段，并写清楚应对办法（⑤）
4. 下周计划（⑥）
另外加一个具体的邮件标题，方便老板以后搜索，例如 *Weekly update: data pipeline migration ([日期])*。

**可以直接复制的版本**（方括号里的内容请换成实际信息，不需要的可以删掉）

> **Subject:** Weekly update: data pipeline migration ([date])
>
> Hi Kelvin,
>
> Overall, the migration is on track.
>
> This week we made a lot of progress on the data pipeline. Latency is down 40% with the new cache, and the error rate is now fairly stable.
>
> Risk: the vendor API is still very slow ([response time]), and we think it's a big risk to the Q4 launch. [What we're doing about it, or what we need from you.]
>
> Next week, we'll finish the load test and fix the remaining bugs.
>
> Thanks,
> Wei

---

**这次最值得改的 3 个习惯**
1. **邮件里别用 PPT 速记**（③⑥）：↓ → + w/ 放在 slide 上没问题，邮件正文要写完整句子：*is down*、*with*、*and*。
2. **聊天口吻进了周报**（③④⑤⑦）：*So, basically / kind of / super / BTW / Thx*。缩写（*we'll*、*it's*）在给老板的邮件里可以用，要去掉的是这些填充词和聊天缩写。
3. **结论和风险放在前面、单独写**（④⑤）：老板可能只看前两行，先写 *on track*，风险单独一段，再加上应对办法。

要不要我建一个错题本，记下你常犯的问题（比如冠词、PPT 写法），下次重点检查？

**轮到你**
用习惯 1 的规则，把这行"PPT 写法"改成一句能放进邮件的英文：
*Cost ↓ 15% w/ new instance type → roll out to staging next week*
