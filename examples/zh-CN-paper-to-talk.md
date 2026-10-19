# Paper paragraph → slides and talk script · Simplified Chinese

**Mode:** Convert (paper → slides + speech) · **Writer:** Graduate student presenting their own paper · **Genre:** group meeting talk

The reply below is the skill's output, unedited.

## What the user sent

> 下周四组会要讲我们自己的论文，下面是论文里结果部分的一段，帮我改成 2 页 slides 和对应的讲稿，我想学一下论文和讲稿的英文到底有什么区别
>
> As shown in Table 3, the proposed method achieves an average F1 score of 0.873 on the three benchmark datasets, outperforming the strongest baseline [14] by 4.6 percentage points. Furthermore, the inference latency is reduced from 120 ms to 62 ms, respectively on GPU and CPU settings, which demonstrates the practicality of the method for real-time applications. However, it should be noted that the performance on the low-resource dataset (n = 312) is relatively limited, suggesting that the effectiveness of the proposed approach may depend on the availability of sufficient training data.

## What english-coach replied

> 我的理解：下周四（10/22）组会，听众是组里同学和导师；领域是机器学习（F1、baseline、benchmark）；你是大陆中文母语者。下面先给 2 页 slides 和讲稿，再讲论文和讲稿的英文到底差在哪。

## ⚠️ 先确认一件事：latency 那句有两种读法

> *the inference latency is reduced from 120 ms to 62 ms, respectively on GPU and CPU settings*

*respectively* 用来把**两组并列的东西一一配对**（A and B are 3 and 5, respectively）。这里只有一组数字（120 → 62），却配了两个设置（GPU 和 CPU），读者没法配对：

- 读法 A：GPU 和 CPU 上都是 120 → 62 ms？（两种硬件数字完全一样，不太可能）
- 读法 B：只是某一个设置下 120 → 62 ms，另一个设置有另外一组数字？

下面的 slide 和讲稿我先写成 `120 → 62 ms on [GPU / CPU]`，你告诉我实际情况我再帮你调。**如果论文还能改，这句也要改**，这是会让审稿人看不懂的问题，不只是风格问题。

---

## Slide 1

**Title:** Our method outperforms the strongest baseline and nearly halves latency

- Avg. F1: **0.873** on 3 benchmarks (Table 3)
- **+4.6 pts** vs. strongest baseline ([baseline 名字])
- Latency: **120 → 62 ms** (−48%) on [GPU / CPU]
- Practical for real-time applications

**讲稿（约 40 秒）**

> So, how well does it work? This table compares our method with the baselines on three benchmark datasets. On average, we get an F1 score of about 0.87. That's almost five points higher than the strongest baseline, [baseline 名字].
>
> It's also faster. Latency drops from 120 milliseconds to about 60, so it's almost twice as fast. This shows the method is practical for real-time use.

**Speaker notes（精确数字，被问到时用）：** F1 = 0.873（3 个数据集平均）；比 [14] 高 4.6 个百分点；latency 120 ms → 62 ms（−48%），[GPU / CPU]。

## Slide 2

**Title:** Results are weaker on the small dataset (n = 312)

- Low-resource dataset: F1 [x.xxx] vs. [0.873 avg.]
- Likely cause: not enough training data
- [Next step，如果你们有计划就写；没有就删掉这条]

**讲稿（约 30 秒）**

> Now, one limitation. On our smallest dataset, which has only 312 samples, the results are weaker. [F1 is about x.]
>
> Our guess is that the method needs enough training data to work well. [If we have a plan: Next, we want to try …]
>
> So, to sum up: the method is more accurate and faster than the strongest baseline, but it probably needs a fair amount of data.

**Speaker notes：** n = 312；F1 = [x.xxx]。原文用的是 *suggesting … may depend*，讲的时候保持"推测"的语气，不要说成 *proves* 或 *the method fails*。

> 📌 原文只写了 *relatively limited*，没给数字。slide 上一定要放这个数据集的 F1，听众第一反应就是问"差多少"。这个数字只有你知道，所以留了 [x.xxx]。

---

## 论文 vs. slide vs. 讲稿：逐句对比

| 论文原句（你写的） | Slide | 讲稿 | 变了什么、为什么 |
|---|---|---|---|
| *As shown in Table 3, the proposed method achieves an average F1 score of 0.873 on the three benchmark datasets,* ✅ | *Avg. F1: 0.873 on 3 benchmarks* | *This table compares… On average, we get an F1 score of about 0.87.* | 🗣️ `written-in-speech`：*As shown in Table 3* 是写给读者翻页找表的；讲的时候表就在屏幕上，直接说 *This table…*。数字讲出来要取整（0.873 → about 0.87），精确值放 slide 上。*the proposed method* → *our method / we*，讲稿里用 *we, you*。 |
| *outperforming the strongest baseline [14] by 4.6 percentage points.* ✅ | *+4.6 pts vs. strongest baseline* | *That's almost five points higher than the strongest baseline, [名字].* | 🗣️ `citation-spoken`：[14] 念不出来，听众也记不住编号，说方法名或"[作者] 2023 年那篇"。🗣️ `long-sentence`：论文里一句 30 多词没问题，讲稿拆成两句，一句一个意思。 |
| *Furthermore, the inference latency is reduced from 120 ms to 62 ms, respectively on GPU and CPU settings,* | *Latency: 120 → 62 ms (−48%)* | *It's also faster. Latency drops from 120 milliseconds to about 60…* | 🗣️ `written-in-speech`：*Furthermore* 是书面连接词，讲稿用 *also / and*。🗣️ `respectively-spoken`：听的人脑子里没法给两组东西配对，讲稿里永远别用 *respectively*。slide 上用箭头和 −48%，讲出来用 *almost twice as fast*。*ms* 要读成 *milliseconds*。 |
| *which demonstrates the practicality of the method for real-time applications.* | *Practical for real-time applications* | *This shows the method is practical for real-time use.* | 🗣️ `written-in-speech`（长名词短语）：*the practicality of the method for…* 是名词化写法，讲的时候改成"主语 + 动词 + 形容词"：*the method is practical*。语气强度不变（*demonstrates* → *shows*），只换说法。 |
| *However, it should be noted that the performance on the low-resource dataset (n = 312) is relatively limited,* | Title: *Results are weaker on the small dataset (n = 312)* | *Now, one limitation. On our smallest dataset, which has only 312 samples, the results are weaker.* | 🗣️ `talk-signpost`：讲稿里换话题要先"报幕"：*Now, one limitation.* 听众马上知道接下来是缺点。*n = 312* 是论文记法，讲出来说 *312 samples*。 |
| *suggesting that the effectiveness of the proposed approach may depend on the availability of sufficient training data.* | *Likely cause: not enough training data* | *Our guess is that the method needs enough training data… it probably needs a fair amount of data.* | 🗣️ `written-in-speech`（长名词短语）：*the effectiveness of… the availability of sufficient…* 两层名词化，耳朵跟不上，改成 *needs enough data*。hedge 要保留：*suggesting… may* → *our guess is / probably*，同样是"推测"，只是口语说法。 |

## 这次转换用到的 5 条规则（下次自己转可以照着用）

1. **一句一个意思**：论文 25–35 词的长句，讲稿拆成 8–15 词的短句。
2. **用口语连接词和"报幕"**：*Furthermore / However, it should be noted that* → *It's also… / Now, one limitation. / So, to sum up*。
3. **数字分三种写法**：论文精确（0.873, 4.6 percentage points）；slide 用符号（+4.6 pts, 120 → 62 ms）；讲稿取整说成话（about 0.87, almost five points, almost twice as fast），精确数字放 speaker notes。
4. **引用和图表不念编号**：[14] → 方法名；*As shown in Table 3* → *This table shows…*；*respectively* 一律拆开说。
5. **动词代替名词化，hedge 只换说法不换强度**：*the practicality of* → *is practical*；*suggesting… may* → *probably / our guess is*，不要升级成 *proves*。

Slide 本身的两条：标题写结论（不要只写 *Results*），bullet 写短语、不写整句。

## 论文原文本身

- ✅ 第一句（As shown in Table 3… 4.6 percentage points）是标准的结果句：有表、有数字、有对比对象。*percentage points* 用得对，很多人会错写成 *4.6%*。
- `respectively`：见最上面，会影响理解，建议改。
- `it-is-found`：*it should be noted that* 是填充，删掉不丢信息：*However, performance on the low-resource dataset (n = 312) is lower ([具体数字])…*
- `vague-word`：*relatively limited* 不说多少、跟谁比。论文里也应该给出数字。

## 组会 Q&A 可能用到的句子

讲了 limitation，组里很可能会追问：

- *That's a fair point. We haven't tested that yet.*
- *That's outside what we tested, but my guess is…*
- *Let me make sure I understand the question: you're asking whether…*

---

要不要我帮你建一个错题本？把这次的 `respectively`、`written-in-speech` 这几类记下来，下次改稿和组会前可以拿来复习。

**下一步：** 从论文里再挑一段（比如 ablation 或 discussion 的一段），用上面 5 条规则自己改成 1 页 slide + 讲稿发给我，我来看哪里还像在念论文。
