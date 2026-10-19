# ChatGPT-drafted PhD inquiry · Simplified Chinese

**Mode:** Review + AI-style lens · **Writer:** Master's student · **Genre:** first email to a prospective PhD supervisor

The reply below is the skill's output, unedited.

## What the user sent

> 我用ChatGPT写了一封给教授的套磁信，感觉有点AI味，你帮我看看哪里像AI，教我怎么改成我自己的话
>
> Dear Professor Smith,
>
> I hope this email finds you well. I am writing to express my profound interest in joining your esteemed research group. Having delved into your groundbreaking work on graph neural networks, I am truly inspired by how it paves the way for a deeper understanding of molecular property prediction.
>
> Throughout my master's journey, I have meticulously honed my skills in PyTorch, data analysis, and scientific writing. Furthermore, my recent project not only showcases my ability to tackle complex challenges but also underscores my passion for pushing the boundaries of AI for science.
>
> I would be absolutely thrilled to discuss potential PhD opportunities. Please don't hesitate to reach out at your earliest convenience.
>
> Thank you for your time and consideration.
>
> Warm regards,
> Zhang Wei

## What english-coach replied

**场景**：第一次联系教授的套磁邮件（申请 PhD）· 机器学习 / AI for science · 母语：简体中文（判断有误请告诉我）

**总体**：语法基本没错，称呼、结尾句都用对了，"兴趣 → 背景 → 请求"的顺序也合理。问题在于几乎每句都是"万能句"：把 Professor Smith 和 graph neural networks 换掉，这封信可以原样发给任何一位教授。教授每周收到很多这样开头的邮件，读到第二句就开始扫读了。

所以改成"自己的话"，关键**不是换同义词**，而是把空洞的形容词换成只有你能写的具体信息：你是谁、读了教授哪篇论文、做过什么项目、结果是多少。顺便提一句：想写得"高级"，往往正是 AI 味的来源。简单动词加具体事实，反而最像真人写的。

---

**①** I hope this email finds you well.
**→** 删掉，直接从第②句开始。
- 🤖 **万能开头** `ai-opener`：这几乎是 AI 邮件的标准第一句。写给不认识的教授，第一句就应该说你是谁、为什么写信。

**②** I am writing to express my profound interest in joining your esteemed research group.
**→** I am a master's student in [专业] at [学校], and I am writing to ask whether you are accepting PhD students for [入学年份/学期].
- 🤖 **夸张形容词** `ai-inflated-word`：*profound interest*、*esteemed* 没有任何信息量。*your esteemed research group* 有点像"贵课题组"直译再加一层 AI 客套，英文读者只会读出恭维。
- 💡 **没有自我介绍** `no-self-intro`：整封信都没说你是谁、在哪读、什么时候毕业。教授得先知道这些，才会决定要不要往下读。一句话就够。
- 💡 **请求要能回答** `vague-ask`：*express my interest* 不是问题，教授没法回答。*whether you are accepting PhD students* 他回一个词就行。

**③** Having delved into your groundbreaking work on graph neural networks, I am truly inspired by how it paves the way for a deeper understanding of molecular property prediction.
**→** I read your [年份] paper on [论文主题], and I was especially interested in [具体哪一点：某个方法、结论或实验].
- 🤖 **AI 高频词** `ai-word`：*delve into* → *read*；*pave the way for*、*a deeper understanding of* 都是 AI 最爱用的搭配，换成你实际想说的那件事。
- 🤖 **用夸奖代替内容** `vague-praise`：*groundbreaking*、*truly inspired* 看不出你到底读没读过。说出一个具体细节（比如这篇论文怎么处理分子结构、哪个结果让你意外），比任何形容词都有说服力。

**④** Throughout my master's journey, I have meticulously honed my skills in PyTorch, data analysis, and scientific writing.
- 🤖 `ai-word`：*journey*、*meticulously honed*，读研不是"旅程"，也很少有人这样形容自己。
- 🤖 **三项并列** `triplet`：三个技能并排放着，但一个证据都没有。只留你能举出例子的那一项。
- **提示**：这句和③是同一个毛病（形容词代替事实），这次你自己改。可以用这个框架：*During my master's, I used PyTorch to [做了什么 / 实现了什么模型] for [什么任务].*

**⑤** Furthermore, my recent project not only showcases my ability to tackle complex challenges but also underscores my passion for pushing the boundaries of AI for science.
- 🤖 **"not only… but also"套句** `not-only-but-also`、`ai-word`：*showcase*、*underscore* 在这里都只是"显示"的意思，而且整句没有说项目是什么。
- 🤖 **装饰性连接词** `transition-stack`：*Furthermore* 删掉，逻辑一点不受影响。
- **提示**：同样你来改。这句只要回答三个问题：项目做的是什么？你负责哪部分？结果怎么样（数字、投稿或发表情况）？框架：*In my recent project, I [做了什么], and [结果]. This is why I am interested in [和教授研究的联系].*

**⑥⑦** I would be absolutely thrilled to discuss potential PhD opportunities. Please don't hesitate to reach out at your earliest convenience.
**→** If so, I would be glad to have a short call at a time that works for you.
- 🤖 **过度热情** `over-warm`：*absolutely thrilled* 对第一次联系的教授来说太满了，读起来像客服回复。*glad* 就够。
- 🤖 **AI 结尾套话** `ai-closer`：*Please don't hesitate to reach out* 是 AI 邮件的标配结尾。*at your earliest convenience* 还带一点催促的意思，而且变成了让教授主动联系你，方向反了。
- 💡 *If so* 接回第②句的问题：如果教授在招人，再请他约个时间，请求一次说清楚。

**⑧** Thank you for your time and consideration.
✅ 申请类邮件用这句很正常，保留。

**称呼和署名**：*Dear Professor Smith,* ✅（Professor + 姓，正确）。*Warm regards,* ✅ 也可以，用 *Best regards,* 同样合适。
- 💡 署名下面加一行身份，例如 *MSc student, [Department], [University]*，教授不用翻邮件就知道你是谁。

---

**结构**：原信是"客套 → 夸教授 → 夸自己 → 请求"，四段都没有具体信息。英文套磁信通常是：**你是谁 + 你想问什么 → 为什么找这位教授（一篇具体论文）→ 你做过什么（一个项目 + 结果）→ 请求**。另外别忘了主题行，例如 *Prospective PhD student: GNNs for molecular property prediction*。

**这次最值得改的 3 个习惯**
1. **形容词代替事实**（②③④⑤⑥）：每写一个 *groundbreaking / profound / meticulously*，就问自己"证据是什么？"然后写出证据，删掉形容词。
2. **AI 高频词**（①③④⑤⑦）：*delve into, pave the way, journey, showcase, underscore, don't hesitate to reach out*，看到就换成 *read, show, help* 这类简单词，或者直接删。
3. **开头先说你是谁、要什么**（②）：第一段就交代身份和问题，不要把请求留到最后。

要不要我帮你建一个错题本，把这次的 `ai-word`、`vague-praise` 这些习惯记下来，以后可以复习、出题？

**轮到你**
按④⑤的框架，用你自己的话把第二段重写成 2–3 句（写清楚项目做了什么、结果是多少），发回来我帮你看。
