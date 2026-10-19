# Conference talk script and slide · Japanese

**Mode:** Review (slide + talk script, medium lens) · **Writer:** Japanese researcher · **Genre:** conference presentation

The reply below is the skill's output, unedited.

## What the user sent

> 来月の学会発表の原稿とスライド1枚です。英語として変じゃないか見てください。
>
> 【スライド3】
> タイトル: Proposal Method
> - Accuracy improvement by attention mechanism introduction
> - The proposed method was applied to the dataset which was collected in 2024 and it was confirmed that the accuracy is improved.
>
> 【原稿】
> I would like to explain about the proposal method. Furthermore, as illustrated in this figure, it can be observed that the accuracy of the proposed method and the baseline method are 92.3% and 85.1%, respectively. Therefore, it is considered that the attention mechanism is effective. I would like to explain about the limitation next.

## What english-coach replied

**場面**：来月の学会発表（スライド3枚目＋読み上げ原稿）· 機械学習（attention） · 母語：日本語（違っていたら教えてください）
**全体**：数字（92.3%、85.1%）がはっきりしていて、*the proposed method*（スライド2行目・原稿②）も正しく使えています。一番の課題は、原稿が「論文を声に出して読んでいる」英語になっていることと、スライドに長い文や名詞の連続が載っていることです。発表まで時間があるので、最後の④はヒントだけにしてあります。

---

## スライド

**Slide 3** · *Proposal Method* → *Adding attention improves accuracy*

- ❌ **提案手法** `section-word`：*proposal method* は「提案書の方法」のように読めます。提案手法は *proposed method*（提案された手法）。2行目では正しく書けています。
- 💡 **結論を言うタイトル** `topic-title`：*Proposed Method* は話題の名前だけです。聴衆はスライドを数秒しか見ないので、タイトルで「何が言いたいか」を1文で言うと伝わります。下の箇条書き1を直すと、そのままタイトルになります。
- タイトルの大文字は、*Proposal Method*（各単語を大文字）か *Adding attention improves accuracy*（文頭だけ大文字）のどちらかに、全スライドでそろえてください。

**箇条書き1** Accuracy improvement by attention mechanism introduction
**→** Adding attention improves accuracy
- 🗣️ **名詞の連続** `noun-stack`：「attention 機構導入による精度向上」の体言止めを、名詞のまま英語に並べた形です。読み手は *improvement by … introduction* を後ろからほどく必要があります。動詞を1つ入れる（*improves*）と一目で分かります。

**箇条書き2** The proposed method was applied to the dataset which was collected in 2024 and it was confirmed that the accuracy is improved.
**→** [データセット名] (2024): 92.3% vs. 85.1% (baseline)
- 🗣️ **スライドに完全な文** `sentence-on-slide`：26語の文があると、聴衆はそれを読むのに忙しくて話を聞けません。スライドは8語程度の断片にして、文は原稿で話します。
- ❌ **時制** `tense`：*was confirmed*（過去）と *is improved*（現在）が混ざっています。論文で書くなら過去にそろえて *accuracy improved*。
- ⚠️ **確認された** `kakunin`：*confirm* は「予想どおりか確かめる」という意味です。結果を述べるだけなら *Accuracy improved on …* で十分。
- 数字は原稿②から取りました。このデータセットでの結果でなければ直してください。

まとめると、たとえばこうなります：

```
Adding attention improves accuracy
- [Dataset name] (collected in 2024)
- Proposed method: 92.3%
- Baseline: 85.1%
```

---

## 原稿

**①** I would like to explain about the proposal method.
**→** Now let me explain our proposed method.
- ❌ **余分な前置詞** `consider-about`：*explain* は他動詞なので *about* は要りません（*explain the method*）。*talk about* なら about が必要です。
- ❌ **提案手法** `section-word`：スライドと同じく *proposed method*。
- 🗣️ **硬すぎる話し言葉** `stiff-speech`：*I would like to…* は「〜させていただきます」の直訳で、毎回使うと硬く聞こえます。発表では *Let me…* / *I'll…* / *Now…* が定番です。

**②** Furthermore, as illustrated in this figure, it can be observed that the accuracy of the proposed method and the baseline method are 92.3% and 85.1%, respectively.
**→** As you can see in this figure, our method reaches 92.3% accuracy, and the baseline reaches 85.1%.
- 🗣️ **書き言葉の読み上げ** `written-in-speech`：*as illustrated*、*it can be observed that* は論文の言い方です。話すときは *As you can see…* と図を指すのが自然。*Furthermore* もここでは何かに「追加」しているわけではないので不要です。
- 🗣️ **respectively** `respectively-spoken`：聞き手は2つの数字を頭の中で順番に対応させられません。「AはX、BはY」と1つずつ言います。
- ❌ **主語と動詞の一致** `agreement`：*the accuracy … are* は単数の主語に複数の動詞です。論文で残すなら *the accuracies … were*。
- 💡 発表では *we / our* が自然です（*the proposed method* → *our method*）。

**③** Therefore, it is considered that the attention mechanism is effective.
**→** So this suggests that the attention mechanism is effective.
- 🗣️ **書き言葉の読み上げ** `written-in-speech`：*it is considered that* は「〜と考えられる」の直訳で、誰が考えたのかが見えません。話すなら *this suggests* か *we think*。*Therefore* は話し言葉では *So*。主張の強さは元のままにしてあります（*proves* にはしていません）。
- 💡 **内容の確認**：この結論は、baseline が「同じモデルで attention だけ外したもの」のときに強く言えます。そうなら一言足すと説得力が上がります：*The baseline is the same model without attention, so…* 違う場合は教えてください。言い方が変わります。

**④** I would like to explain about the limitation next.
**→** Next, let me ______.
- ヒント：①と同じ2つのクセ（*would like to* と *explain about*）が入っています。①の直し方を使ってみてください。limitation が1つなら *one limitation*、複数なら *the limitations* です。

**流れ**：①で「手法を説明します」と言っていますが、②ではすぐ結果に入っています。①と②の間に手法の要点を1〜2文入れるか、①を *Let's look at the results.* に変えると、話とスライドがそろいます。

---

**今回いちばん直したい3つのクセ**
1. **論文の文をそのまま話している**（①②③④）：*I would like to / Furthermore / it can be observed that / respectively / it is considered that* → *Let me / Now / As you can see / AはX、BはY / this suggests*。原稿は「1回聞いて分かるか」で判断します。
2. **スライドは結論のタイトル＋短い断片**（スライド3）：体言止めの名詞の連続と長い文を避け、タイトルで言いたいことを1文で、箇条書きは数字中心に。
3. **提案手法 = *proposed method*、*explain* に about は付けない**（スライド3、①④）。

質疑応答で使える定番フレーズが必要なら、それもお出しします。

よく出るクセを記録する「エラーノート」を作りましょうか？次回からそこを重点的にチェックします。

**次の一歩**
④を①の直し方で話し言葉に書き直して、送ってください。
