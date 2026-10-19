# Mixed mode

Bilingual professionals often write like this:

> We need to 确认 the 交期 with the supplier, otherwise production will be 推迟.
> 来週の MTG で、この件の evidence を共有します。
> 呢個 case 我會 follow，有 update 再 send 俾你。

Two different problems show up here. Handle both.

## A. English with native-language gaps

The user wrote the English skeleton and got stuck on certain words. They did most of the work, so you may assemble the sentence for them after the gaps are filled.

For each gap:

1. Give one to three English options, with the difference between them in a few words.
2. Mark the one that fits this context and say why.
3. After all gaps, show the assembled sentence, then review the English the user wrote around the gaps using the normal Review rules (`review.md`).

```markdown
**原句**：We need to 确认 the 交期 with the supplier, otherwise production will be 推迟.

| 中文 | 可选 | 区别 |
|---|---|---|
| 确认 | **confirm** ✓ / check / verify | *confirm* 是让对方给出确定答复；*check* 是自己去查；*verify* 是核实真伪 |
| 交期 | **delivery date** ✓ / lead time | *delivery date* 是具体哪天到货；*lead time* 是从下单到交货要多久 |
| 推迟 | **delayed** ✓ / postponed | *postponed* 是主动决定推后；被迫延后用 *delayed* |

**组合后**：We need to confirm the delivery date with the supplier; otherwise, production will be delayed.
- ❌ **逗号连接两个完整句子** `comma-splice`：*otherwise* 不是连词，前面用分号或句号。

**轮到你**：下次试着先写英文，实在想不出来的词再用中文占位，像这次一样。
```

## B. Native-language text full of English work words

In Chinese and Japanese offices, English words drift from their English meanings. When the user turns such a message into English, those words come along and carry the drifted meaning. Native readers then misread them.

When the user asks how to say a mixed sentence in English, or their English contains these words, flag the shifted ones.

Notebook slugs for these: `office-<word>` for Chinese workplace English (`office-push`, `office-case`) and `wasei-<word>` for Japanese katakana (`wasei-claim`, `wasei-evidence`).

### Chinese workplace (Mainland, Taiwan, Hong Kong, Singapore)

| Office usage | What the writer means | What English readers hear | Write instead |
|---|---|---|---|
| push 一下 | 催一下 | to force or promote something | *follow up with*, *chase* (BrE, informal), *remind* |
| 这个 case | 项目、客户、案子 | a legal or support case | *project*, *deal*, *account*, *issue* |
| align 一下 | 对齐意见 | (fine, but overused in email) | *agree on*, *make sure we're on the same page* (informal) |
| follow 这个 | 跟进、负责 | to come after, to obey | *follow up on*, *handle*, *own* (informal) |
| share 一下 | 做个分享、演讲 | to give part of something | *present*, *walk us through*, *give a talk on* |
| check 一下 | 确认、看看、核实 | to verify quickly | *confirm*, *review*, *look into* depending on meaning |
| open 一个 meeting | 开会 | — | *set up a meeting*, *schedule a call* |
| 落地 / landing | 实施 | an airplane landing | *implement*, *roll out*, *put into practice* |
| 复盘 | 回顾总结 | — | *retrospective*, *post-mortem*, *review what happened* |
| 赋能 / empower | 支持、提供能力 | a buzzword; reads as AI or marketing | say what you give them: *train*, *give access to* |
| 对标 | 参照、比较 | — | *benchmark against*, *compare with* |
| 颗粒度 | 细节程度 | — | *level of detail* |
| 打法 | 方法、策略 | — | *approach*, *playbook*, *strategy* |
| 抓手 | 着力点 | — | *lever*, *starting point*, or say the concrete action |
| 沉淀 | 总结成文档或经验 | — | *document*, *capture*, *turn into a guide* |

### Japanese office katakana

| 和製・カタカナ | 意図 | 英語での問題 | 代わりに |
|---|---|---|---|
| クレーム | 苦情 | *claim* = 主張・請求 | *complaint* |
| アポ | 約束・面会予約 | — | *appointment*, *meeting* |
| リスケ | 日程変更 | 略語は通じない | *reschedule* |
| MTG | 会議 | 略語は社外で通じにくい | *meeting* |
| エビデンス | 裏付け資料・記録 | *evidence* は法廷・科学の重い語感 | *supporting documents*, *records*, *screenshots*, *data* |
| フィックス | 確定 | *fix* = 修理する | *finalize*, *confirm* |
| ペンディング | 保留 | 通じるがやや硬い | *on hold* |
| ネゴ | 交渉 | — | *negotiate*, *negotiation* |
| コンセンサスを取る | 合意を得る | — | *get agreement from*, *get sign-off from* |
| アサイン | 担当を割り当てる | 通じる | *assign* はOK、ただし *assign him to the project* の形で |
| マスト | 必須 | *must* は名詞にしない | *required*, *essential* |
| ブラッシュアップ | 改善 | *brush up* = 忘れかけた知識を磨き直す | *refine*, *improve*, *polish* |
| キャパ | 対応能力 | — | *bandwidth*, *capacity* |
| ノルマ | 達成目標 | 英語ではほぼ通じない | *quota*, *target* |
| マンション | 分譲住宅 | *mansion* = 大豪邸 | *apartment*, *condo* |
| サラリーマン | 会社員 | *salaryman* は古い・日本特有 | *office worker*, *employee* |

For other drifted words, use the same test: would a native reader who never worked in an Asian office understand it the way the writer means it? If not, flag it.

## Output order for mixed input

1. Gap table (part A), if there are native-language chunks.
2. Assembled sentence.
3. Normal review notes on the English the user wrote.
4. Drifted-meaning notes (part B), if any.
5. One next step.
