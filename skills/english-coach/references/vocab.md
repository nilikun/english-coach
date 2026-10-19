# Vocab mode

Use this when the user asks for vocabulary in a field, or when a review shows that missing domain words were the main gap. The goal is a short list the user can actually use this week, tied to what they're writing. A 200-word glossary doesn't do that.

## Identify the field precisely

"Finance" is too broad to be useful. Narrow it down from the user's text: *equity research*, *corporate treasury*, *audit*, *retail banking compliance*. If the user's text names the field, say which one you detected in the first line, so they can correct you.

## What to include

Twelve to twenty items, grouped like this:

1. **Core terms** (5–8): nouns the field uses that general English doesn't, with a gloss in the user's language. Prefer the term practitioners actually write, not the textbook term. *Churn*, not *customer attrition rate*, in a SaaS weekly update.
2. **Collocations** (4–8): verb + noun and adjective + noun pairs. This is where non-native writers lose the most points. *Conduct an experiment*, *mitigate a risk*, *file a patent*, *close the books*, *raise a ticket*.
3. **Function phrases** (3–5): phrases for the job this text does. Describing a trend, hedging a result, escalating an issue, declining a request.
4. **Traps** (2–4): words that mean something specific in this field, or that learners commonly misuse here. *Significant* in a paper means statistically significant. *Leverage* in finance is debt, so don't use it to mean "use". *Revenue* is not *profit*. *Data* is usually plural in academic writing.

For each item give: the term, a gloss in the user's language, and one example sentence. If possible, build the example from the user's own text or topic, so they see it in use.

## Quality rules

- **Only real usage.** Don't invent terms or collocations. If you're not sure a collocation is standard, leave it out.
- **Mark variety differences** when they matter: *lift* / *elevator* matters less here than *turnover* (UK: revenue; US: staff leaving) or *billion* in old British texts.
- **Avoid buzzwords** unless the field truly uses them as terms. *Synergy* and *paradigm* rarely belong on the list.
- **Prefer the plain word** when a plain word is the field's normal choice.

## Template

```markdown
**领域**：供应链 · 采购（根据你的邮件判断）

**核心词**
| 英文 | 中文 | 例句 |
|---|---|---|
| lead time | 交货周期 | The lead time for this part is now eight weeks. |
| purchase order (PO) | 采购订单 | We issued the PO on 3 March. |
| …

**搭配**
- *place an order* 下单（不说 *make an order*）
- *expedite a shipment* 加急发货
- …

**常用句**
- 说明延迟：*The shipment has been delayed due to …*
- …

**易错**
- *delivery* vs *shipment*：*shipment* 是发出的那批货，*delivery* 是送达这个动作
- …

**轮到你**：挑 3 个用在你下一封邮件里，写完发给我看。
```

## After the list

Offer to save the words to the notebook (`notebook.md`), in one line. Next time the user writes in this field, check whether they used them.
