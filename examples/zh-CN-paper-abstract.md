# Paper abstract · Simplified Chinese

**Mode:** Review · **Writer:** Mainland Chinese graduate student · **Genre:** journal abstract (computer vision)

The reply below is the skill's output, unedited.

## What the user sent

> 帮我看看这段摘要，下周要投稿了，导师说英文有问题但没说哪里
>
> With the development of deep learning, more and more attention has been paid to defect detection of steel surface. In order to solve the problem of low accuracy of small defect detection, based on YOLOv8, an improved algorithm is put forward in this paper. Firstly, attention mechanism is introduced into backbone network, which can enhance feature extraction ability. Secondly, by this way of multi-scale fusion, the detection effect to small targets is improved. Experiment results show that the mAP of proposed method reaches 86.4%, which is 3.2% higher than original YOLOv8, and the speed reaches 92 FPS, the method realizes real-time detection. Obviously, the proposed method has a great application value in industrial field.

## What english-coach replied

**场景**：论文摘要（投稿用）· 计算机视觉 / 钢材表面缺陷检测 · 母语：简体中文（如果判断有误请告诉我）
**总体**：结构是完整的：背景 → 问题 → 两个改进点 → 带数字的结果 → 意义，而且给了 mAP 和 FPS 两个具体数字，这一点很多摘要都做不到，请保留。导师说的"英文有问题"主要集中在三类：**冠词缺失**、**中文模板式开头和结尾**、**逐字直译的搭配**。另外第 ⑤ 句有一个可能改变意思的数字表达，投稿前一定要确认。

---

**①** With the development of deep learning, more and more attention has been paid to defect detection of steel surface.
**→** Deep learning is increasingly applied to steel surface defect detection.
- ⚠️ **"随着……的发展"开头** `with-development`：这是中文作文模板直译，审稿人读到会觉得是空话。直接写变化本身。
- ⚠️ **"越来越多"** `more-and-more`：*more and more attention* 是"越来越多"的直译，学术写作里用 *increasingly* 或 *a growing number of*。
- ⚠️ **名词修饰顺序** `noun-compound`：英文术语习惯把修饰语放前面，*steel surface defect detection*，不用 *defect detection of steel surface*（后者还缺冠词）。

**②** In order to solve the problem of low accuracy of small defect detection, based on YOLOv8, an improved algorithm is put forward in this paper.
**→** To address the low accuracy of small-defect detection, we propose an improved algorithm based on YOLOv8.
- ⚠️ **目的状语前置** `front-loaded-purpose`：主句前面堆了两个状语（*In order to…*, *based on YOLOv8*），读者要读到最后才知道主语是谁。英文先给主句，或者目的状语最多留一个在前面。
- ⚠️ **"based on" 悬空** `dangling-through`：*based on YOLOv8* 后面紧跟的是 *an improved algorithm*，但句子结构上它修饰不清楚。放在 *algorithm* 后面就没有歧义了。
- ⚠️ **"提出"** `put-forward`：*put forward* 多用于辩论中提出观点；提出自己的方法用 *propose*。
- ⚠️ **"解决"** `solve`：*solve* 意味着问题彻底消失了。你的方法是"改善"准确率，用 *address* 或 *improve* 更准确，也不会被审稿人挑"过度声明"。
- 💡 **用 we** `in-this-paper`：*is put forward in this paper* 换成 *we propose* 更短。大多数工科期刊接受 *we*；如果目标期刊要求不用 *we*，写 *This paper proposes…*。

**③** Firstly, attention mechanism is introduced into backbone network, which can enhance feature extraction ability.
**→** Firstly, an attention mechanism is introduced into the backbone network to improve feature extraction.
- ❌ **冠词** `article`：*mechanism* 是单数可数名词，前面必须有限定词。这里第一次提到，用 *an*。
- ❌ **冠词** `article`：*backbone network* 指的是 YOLOv8 自己那个骨干网络，读者知道是哪一个，用 *the*。
- ⚠️ **which 指代不清** `which-ambiguous`：*which* 默认指离它最近的名词，也就是 *backbone network*，但你想说的是"引入注意力机制"这件事。改成 *to improve…* 表示目的，没有歧义。
- 💡 **多余的 ability** `redundancy`：*enhance feature extraction ability* 是"提高特征提取能力"的直译，英文 *improve feature extraction* 已经包含"能力"的意思。

**④** Secondly, by this way of multi-scale fusion, the detection effect to small targets is improved.
**→** Secondly, multi-scale feature fusion is used to improve the detection of small defects.
- ⚠️ **by this way** `by-this-way`：*way* 不跟 *by*，要么 *in this way*，要么直接把方法当主语。这里直接说"用了什么、改善了什么"最清楚。
- ❌ **介词** `preposition`：*effect to* → *effect on*。不过这里更好的是不用 effect（见下一条）。
- ⚠️ **"检测效果"** `detection-effect`：*detection effect* 是"效果"的直译，英文读者不知道指精度还是速度。直接说 *detection*，或具体写 *detection accuracy*。
- 💡 **术语前后一致** `term-consistency`：前面写的是 *small defects*，这里变成 *small targets*。同一个对象全文用同一个词，否则审稿人会以为是两回事。另外如果你融合的是特征图，写 *multi-scale feature fusion*，这是领域里的标准说法。

**⑤** Experiment results show that the mAP of proposed method reaches 86.4%, which is 3.2% higher than original YOLOv8, and the speed reaches 92 FPS, the method realizes real-time detection.
**→** Experimental results show that ___ proposed method achieves an mAP of 86.4%, 3.2 percentage points higher than ___ original YOLOv8. It runs at 92 FPS, which allows real-time detection.
- ❌ **百分比 vs 百分点** `percentage-point`：**这条会改变意思，请先确认。** 如果是 86.4% 减去 83.2% 得到的 3.2，英文要写 *3.2 percentage points higher*；写 *3.2% higher* 意思是相对提升 3.2%（即原来约 83.7%）。我上面按"百分点"改了，如果你算的是相对提升，告诉我。
- ❌ **逗号连句** `comma-splice`：*…92 FPS, the method realizes…* 是两个完整句子用逗号连起来，英文里这是语法错误。在 *YOLOv8* 后断句，后半句另起。
- ❌ **"实现"** `realize`：*realize* 主要是"意识到"。"实现实时检测"用 *achieve* 或 *allow*。
- ⚠️ **名词作形容词** `experimental`：*Experiment results* → *Experimental results*，修饰名词用形容词形式。
- 💡 **reaches 用了两次** `reach-repeat`：*mAP reaches*、*speed reaches* 都是"达到"的直译。*achieves an mAP of*、*runs at 92 FPS* 是这个领域的常见说法。
- 冠词：两个 ___ 留给你填，见文末。

**⑥** Obviously, the proposed method has a great application value in industrial field.
**→** These results indicate that the method is suitable for industrial applications.
- ⚠️ **Obviously** `obviously`：审稿人看到 *Obviously* 会觉得作者在替他下结论。如果真的显而易见，不用说；如果不是，这个词只会让人反感。删掉，用结果来支撑。
- ⚠️ **"具有很大的应用价值"** `overclaim`：*has a great application value* 是直译，而且没有证据支撑"great"。用 *indicate/suggest* 加一个具体的说法，审稿人更容易接受。如果你有在产线上测过，可以写得更具体，比如 *suitable for real-time inspection on production lines*。
- ❌ **冠词 + 搭配** `article`：*value* 在这里不可数，不加 *a*；*in industrial field* 缺冠词，而且英文一般说 *in industry* 或 *for industrial applications*。

---

**结构**（3 行内）：摘要里"问题"那一句可以更明确：现有方法在小缺陷上准确率低的**原因**是什么（比如小缺陷特征在下采样中丢失）？另外结果句没有说**在哪个数据集**上测的（如 NEU-DET 或自建数据集），也没说是 mAP@0.5 还是 mAP@0.5:0.95，审稿人几乎一定会问，建议补上。

**这次最值得改的 3 个习惯**
1. **冠词**（③⑤⑥）：单数可数名词前几乎总要 *a/the*；读者知道指哪一个时用 *the*（*the proposed method*, *the backbone network*）。
2. **中文模板式开头结尾**（①⑥）：*With the development of*、*more and more*、*Obviously*、*great application value* 这类句式审稿人一眼就认得出，直接写具体的事实和数字。
3. **逐字直译的动词**（②④⑤）：提出 → *propose*，解决 → *address*，实现 → *achieve*，效果 → 说清楚是精度还是速度。

如果你愿意，我可以建一个错题本，把这次的冠词、模板句式这些习惯记下来，下次改别的章节时对照着看、也能做小测验。要不要？

**轮到你**
把第 ⑤ 句改写里两个 ___ 填上冠词（提示：这两个都是读者已经知道指哪一个的），顺便告诉我 3.2 是百分点还是相对提升，发回来。我确认后给你一版完整的、可以直接投稿的摘要。
