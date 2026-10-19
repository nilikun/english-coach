# Group meeting slides and script · Simplified Chinese

**Mode:** Review (slides + talk script) · **Writer:** Graduate student presenting a paper · **Genre:** lab group meeting (组会)

The reply below is the skill's output, unedited.

## What the user sent

> 下周组会要用英文讲一篇论文，这是我的slides文字和讲稿，帮我看看
>
> Slide 1: Research Background
> - With the development of LLM, more and more researches focus on long context
> - Existing methods have high computation cost
>
> Slide 2: Method
> - Propose a sparse attention method
> - Training the model on 4K tokens and then extending to 128K
> - Evaluation on LongBench
>
> Slide 3: Experiment
> - The proposed method is the best in all datasets
> - Speed is improved 3 times
>
> Slide 4: Thank you for your listening!
>
> 讲稿：
> Today I will introduce you a paper about long context LLM. Firstly, let me introduce the background. With the development of LLM, more and more researches focus on long context, however existing methods have high computation cost because the attention complexity is quadratic to the sequence length which makes it difficult to process very long documents in practical applications. In this paper, the authors put forward a sparse attention method. Everyone can see that the proposed method is the best in all datasets. That's all my report, welcome everyone to criticize and correct.

## What english-coach replied

**场景**：组会论文汇报（slides + 口头讲稿）· 机器学习 / 大模型长上下文 · 母语：简体中文 · 下周讲，还有时间自己改（如果判断有误请告诉我）

**总体**：结构清楚，背景 → 方法 → 实验，四页正好；讲稿里"注意力复杂度随序列长度平方增长"这个因果讲得很准，是整段最有内容的一句。主要问题有三类：中文汇报套话直译（随着……的发展、欢迎批评指正）、slide 标题和 bullet 不够"说重点"、讲稿把别人的结论当成事实说。
**先确认一个数字**：*Speed is improved 3 times* 有歧义，听众可能理解成"速度提升了三次"。论文里的意思是"比 [基线] 快 3 倍"吗？是推理还是训练、在多长的序列上？下面我用 [方括号] 留了位置，请按论文填。

---

## Slides

**Slide 1** · *Research Background* → *Long context is expensive: attention cost grows quadratically*
- ⚠️ **标题只写了板块名** `slide-title`：*Background* 告诉听众"这是背景"，但没说背景的要点。用一句话当标题，听众还没看 bullet 就知道这页想说什么。另外"研究背景"直译成 *Research Background*，*Research* 是多余的；如果你想保留板块名，写 *Background* 就够了。
- ⚠️ **"随着……的发展"** `with-development`：*With the development of LLM* 是中文作文开头的直译，英文读者觉得是空话。直接写变化本身。
- ⚠️ **"越来越多"** `more-and-more`：*more and more* 偏口语，slide 上用 *growing interest* 或直接给数字。
- ❌ **不可数名词加 -s** `uncountable-plural`：*research* 不可数，没有 *researches*。要表达"很多研究"用 *a lot of research*、*many studies*。
- ❌ **单复数** `article`：*LLM* 是可数名词，泛指一类模型时用复数 *LLMs*。
- ⚠️ **搭配** `collocation`：论文里的固定说法是 *computational cost*，*computation cost* 也有人用，但少见。

建议的 bullet：
- *Growing interest in long-context LLMs*
- *Existing methods: high computational cost*

**Slide 2** · *Method* → *Sparse attention: train on 4K, extend to 128K*
- ❌ **bullet 不平行** `parallel`：*Propose / Training / Evaluation* 是动词原形、-ing、名词三种形式。一页里 bullet 要用同一种句型，最简单的是都用动词原形：
  - *Propose a sparse attention method*
  - *Train on 4K tokens, then extend to 128K*
  - *Evaluate on LongBench*
- 💡 内容本身很好：短、具体、有数字。这页只需要改形式。

**Slide 3** · *Experiment* → *[N]× faster than [baseline], best on all LongBench datasets*
- ⚠️ **标题只写了板块名** `slide-title`：同 Slide 1。结果页最适合用结论当标题，把你最想让大家记住的数字放上去。另外"实验"页一般叫 *Results* 或 *Experiments*，*Experiment* 单数读起来像只做了一个实验。
- ⚠️ **谁说的** `attribution`：*The proposed method is the best* 把作者的结论写成了事实。组会讲别人的论文，大家会追问"在什么指标上 best？跟谁比？"标出这是作者报告的结果，也给你自己留了余地：*Authors report the best [metric] on all [N] LongBench datasets*。
- ❌ **介词** `preposition`：在某个数据集上取得结果用 *on*：*on all datasets*，不用 *in*。
- ❌ **数字有歧义** `vague-word`：见上面的确认。英文写倍数最清楚的是 *3× faster than [baseline]*，后面最好补上条件：*at [128K] tokens*。

**Slide 4** · *Thank you for your listening!* → *Thank you* / *Questions?*
- ⚠️ **"谢谢聆听"直译**：*listening* 前面不加 *your*，英文说 *Thanks for listening* 或只写 *Thank you*。
- 💡 更好的做法：最后一页放这篇论文的一句 takeaway（比如 *Sparse attention: [N]× faster at 128K, [accuracy result]*，方括号按论文实际结论填），下面加 *Questions?*。大家提问时这页一直挂着，比单独一个 *Thank you* 有用。

**整套 slides 的问题（只说一次）**
- **标题大小写** `title-case`：现在 *Research Background* 是每个词大写，改成句子标题后建议统一用 sentence case（只有第一个词和专有名词大写），四页保持一致。
- **复合形容词加连字符** `compound-hyphen`：*long context* 放在名词前当形容词时写 *long-context LLMs*；单独当名词时 *long context* 不加。

---

## 讲稿

讲稿是说出来的英文，标准和论文不一样：句子要短，可以用 *I'll*、*let's* 这样的缩写，"首先""接下来"这类路标词在演讲里是好的，要保留。

**①** Today I will introduce you a paper about long context LLM.
**→** Today I'll walk you through a paper on long-context LLMs.
- ❌ **动词句型** `verb-pattern`："给你介绍一篇论文"直译了。*introduce* 后面不能直接接"人 + 东西"，*introduce you a paper* 不成立。讲论文用 *walk you through* 或 *I'm going to talk about*。
- ❌ **单复数** `article`：同 Slide 1，*LLMs*。

**②** Firstly, let me introduce the background.
**→** Let's start with why this problem matters.
- ⚠️ **"首先我介绍一下背景"** `let-me-introduce`：每一部分都用 *let me introduce* 开头，听起来像在念流程。直接说这一部分要讲什么。想保留"首先"也可以：*First, some background.* 口语里 *First* 比 *Firstly* 常见。

**③** With the development of LLM, more and more researches focus on long context, however existing methods have high computation cost because the attention complexity is quadratic to the sequence length which makes it difficult to process very long documents in practical applications.
**→**（拆成三句）
*______.* But existing methods are expensive. Attention cost grows quadratically with sequence length, so very long documents are hard to process in practice.
- ⚠️ **第一句留给你**：这半句就是 Slide 1 第一条原样念出来的，前面已经改过两次 LLM 单复数、改过 *researches*，这次你自己写口语版。提示：去掉"随着……的发展"，*LLM* 要不要加 -s？*research* 能不能加 -s？
- ❌ **逗号连句** `comma-splice`：*…long context, however existing…* 两个完整句子之间不能只用逗号。*however* 是副词，不是连词；要么句号后写 *However,*，要么口语里直接用 *But*。
- ❌ **长句** `long-sentence`：原句 50 多个词，听众听到 *which* 时已经忘了主语。中文可以一逗到底，英文口语一句一个意思。断点：①研究热点 ②现有方法贵 ③为什么贵。
- ❌ **介词** `preposition`：数学上说"关于 n 是平方的"用 *quadratic in*，不是 *quadratic to*。口语里 *grows quadratically with* 更顺。
- ⚠️ **which 指代不清** `which-ambiguous`：*…the sequence length which makes it difficult…* 读起来像"序列长度让处理变难"，其实你想说的是"平方复杂度让处理变难"。用 *so* 把因果直接说出来。

**④** In this paper, the authors put forward a sparse attention method.
**→** In this paper, the authors propose a sparse attention method.
- ✅ *the authors* 用得对：讲别人的论文，用 *the authors* 把作者的工作和你自己的看法分开。
- ⚠️ **"提出"** `put-forward`：提出方法用 *propose*。*put forward* 多用于在讨论中提出观点。

**⑤** Everyone can see that the proposed method is the best in all datasets.
**→** As you can see here, the authors report the best [metric] on all [N] LongBench datasets.
- ⚠️ **"大家可以看到"** `everyone-can-see`：*Everyone can see that* 听起来像"这是显而易见的"，有点强加于人。指着 slide 说 *As you can see here* 或 *This table shows* 是演讲里很自然的说法。
- ⚠️ **谁说的** `attribution`：同 Slide 3。
- ❌ **介词** `preposition`：同 Slide 3，*on all datasets*。

**⑥** That's all my report, welcome everyone to criticize and correct.
**→** That's all from me. I'm happy to take questions.
- ⚠️ **"以上就是我的汇报 / 欢迎批评指正"**：两句都是中文汇报套话直译。*That's all my report* 语法不通；*criticize and correct* 在英文里听起来像"请来批评我"，太重。英文组会结尾就是 *I'm happy to take questions* 或 *I'd welcome any feedback*。
- ❌ **逗号连句** `comma-splice`：同 ③，两个句子用句号分开。

**讲稿整体**
- 讲稿从背景直接跳到 ⑤ 的结论，Slide 2 的方法（4K 训练、扩展到 128K、LongBench）和 Slide 3 的 3 倍加速都没讲。组会上大家最想听的就是方法怎么做的。建议在 ④ 后面补两三句，讲 slide 上没写的东西：[稀疏注意力具体保留哪些 token / 怎么从 4K 扩展到 128K]。
- ③ 前半句、⑤ 和 slide 上的 bullet 几乎一样。讲稿不要念 slide，要说 slide 没写的解释或例子。

**组会提问时可以用的几句**
- 没听清：*Let me make sure I understand: you're asking whether…*
- 不知道：*I'm not sure. I'll check the paper and get back to you.*
- 同意质疑：*That's a fair point. The paper doesn't test that.*

---

**这次最值得改的 3 个习惯**
1. **中文汇报套话直译**（Slide 1、Slide 4、①②⑤⑥）：*With the development of*、*let me introduce*、*Everyone can see*、*welcome to criticize and correct*。英文演讲开头直接说要讲什么，结尾说 *I'm happy to take questions*。
2. **slide 标题只写板块名**（Slide 1、3）：把这页的结论写进标题，听众先知道重点再看细节。
3. **别人的结论要标出来**（Slide 3、⑤）：*the authors report / show / propose*。你在 ④ 已经这样做了，⑤ 照着来就行。

要不要我建一个错题本，记下你常犯的问题，下次重点检查？

**轮到你**
写出 ③ 空着的第一句：用口语说"长上下文大模型现在很受关注"，不用 *With the development of*，注意 *LLM* 和 *research* 的单复数。
