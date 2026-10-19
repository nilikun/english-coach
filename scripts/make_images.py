"""Build the README images: assets/hero-<lang>.png and assets/features-<lang>.png.

Each image is an HTML page rendered to PNG with headless Google Chrome.
Run: python3 scripts/make_images.py            (all images)
     python3 scripts/make_images.py --html-only (write HTML to build/images/ for inspection)
"""
import html
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build" / "images"
ASSETS = ROOT / "assets"
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
W = 1600
SIZES = {"hero": 1120, "features": 900}

FONTS = {
    "en": "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif",
    "zh-CN": "-apple-system, 'PingFang SC', 'Noto Sans CJK SC', 'Microsoft YaHei', sans-serif",
    "zh-TW": "-apple-system, 'PingFang TC', 'Noto Sans CJK TC', 'Microsoft JhengHei', sans-serif",
    "ja": "-apple-system, 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Noto Sans CJK JP', 'Yu Gothic', sans-serif",
}

CSS = """
:root{--bg:#f6f4ef;--ink:#14181f;--muted:#566070;--faint:#98a1ae;--card:#fff;--line:#e6e2d9;
--err-bg:#fde4e2;--err:#b42318;--unn-bg:#fdefc8;--unn:#8a4b0f;--reg-bg:#e3ebff;--reg:#3538cd;
--ai-bg:#efe6ff;--ai:#6941c6;--ok-bg:#dcf5e7;--ok:#18794e;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
--serif:Charter,'Iowan Old Style',Georgia,'Times New Roman',serif}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1600px;background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased}
.frame{width:1600px;height:var(--h);padding:44px 56px 40px;display:flex;flex-direction:column;gap:22px}
.brand{font:600 20px var(--mono);color:var(--faint);letter-spacing:.2px}
h1{font-size:44px;font-weight:750;letter-spacing:-.6px;line-height:1.15;margin-top:6px}
.sub{font-size:20px;color:var(--muted);margin-top:8px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.chips{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}
.chip{font-size:13.5px;font-weight:600;color:var(--muted);background:#ebe8e0;border-radius:999px;padding:6px 12px;white-space:nowrap}
.label{font-size:12.5px;font-weight:700;letter-spacing:1.2px;color:var(--faint);text-transform:uppercase}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px}
/* hero */
.main{display:grid;grid-template-columns:850px 1fr;gap:28px;flex:1;min-height:0}
.left{display:flex;flex-direction:column;gap:20px;min-height:0}
.phead{display:flex;justify-content:space-between;align-items:center;gap:12px}
.paper{padding:26px 34px;box-shadow:0 1px 0 rgba(20,24,31,.03),0 12px 30px -18px rgba(20,24,31,.18)}
.ptitle{font:700 19px var(--serif);margin:14px 0 6px}
.abstract{font:20.5px/2.4 var(--serif);color:#1f2530;hyphens:none}
.m{position:relative;border-radius:4px;padding:2px 1px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.m[data-n]::before{content:attr(data-n);position:absolute;left:-7px;top:-13px;width:19px;height:19px;border-radius:50%;
 font:700 11.5px/19px -apple-system,sans-serif;text-align:center;color:#fff}
.m.err{background:var(--err-bg);border-bottom:2.5px solid var(--err)}.m.err::before{background:var(--err)}
.m.unn{background:var(--unn-bg);border-bottom:2.5px solid var(--unn)}.m.unn::before{background:var(--unn)}
.m.reg{background:var(--reg-bg);border-bottom:2.5px solid var(--reg)}.m.reg::before{background:var(--reg)}
.m.minor{border-bottom:2px dotted #a7adb8}
.m.turn{outline:1.8px dashed #14181f;outline-offset:1px}.m.turn::before{background:#14181f}
.notes{display:flex;flex-direction:column;gap:12px;min-height:0}
.note{display:grid;grid-template-columns:26px 1fr;gap:10px;padding:13px 16px;border-radius:14px;background:var(--card);border:1px solid var(--line)}
.num{width:24px;height:24px;border-radius:50%;color:#fff;font:700 13px/24px -apple-system,sans-serif;text-align:center}
.pills{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.pill{font-size:11.5px;font-weight:750;letter-spacing:.4px;border-radius:999px;padding:3px 9px;white-space:nowrap}
.p-err{background:var(--err-bg);color:var(--err)}.p-unn{background:var(--unn-bg);color:var(--unn)}
.p-reg{background:var(--reg-bg);color:var(--reg)}.p-ai{background:var(--ai-bg);color:var(--ai)}
.p-warn{background:#14181f;color:#fec84b}
.fix{font:600 14.5px/1.45 var(--mono);margin-top:7px;color:var(--ink)}
.fix s{display:block;font-weight:500;color:var(--faint);text-decoration-thickness:1.5px}
.fix b{font-weight:400;color:var(--faint)}
.why{font-size:15px;line-height:1.5;color:var(--muted);margin-top:4px}
.more{font-size:14px;color:var(--faint);padding:2px 4px}
.foot{display:grid;grid-template-columns:1fr 1fr;gap:20px;flex:none}
.paper{flex:1;display:flex;flex-direction:column}
.ptitle2{font:700 23px/1.35 var(--serif);color:var(--ink);margin-top:18px}
.kw2{margin-top:auto;padding-top:14px;border-top:1px solid var(--line);font:italic 16.5px var(--serif);color:var(--muted)}
.kw2 b{font-style:normal;font-weight:700;color:var(--ink)}
.summary{display:flex;gap:18px;font-size:14px;color:var(--muted)}
.summary b{display:block;font:700 26px var(--mono);color:var(--ink)}
.stack{display:flex;flex-direction:column;gap:20px}
.box{padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.bar{display:grid;grid-template-columns:1fr 44px;gap:10px;align-items:center;font-size:15px}
.track{height:10px;border-radius:6px;background:#efece5;margin-top:5px;overflow:hidden}
.track i{display:block;height:100%;border-radius:6px;background:#14181f}
.turnbox{background:#14181f;border-color:#14181f;color:#f2f4f7}
.turnbox .label{color:#fec84b}
.turnbox p{font-size:17px;line-height:1.55}
.nb{font:500 14px var(--mono);display:grid;grid-template-columns:1fr auto auto;gap:6px 14px;align-items:center}
.st{font:700 11.5px -apple-system,sans-serif;border-radius:999px;padding:3px 9px}
.st.a{background:var(--err-bg);color:var(--err)}.st.i{background:var(--unn-bg);color:var(--unn)}.st.m{background:var(--ok-bg);color:var(--ok)}
/* features */
.grid{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:18px;flex:1;min-height:0}
.feat{padding:20px 20px 18px;display:flex;flex-direction:column;gap:10px}
.ftop{display:flex;align-items:center;gap:10px}
.fnum{font:700 13px var(--mono);color:var(--faint)}
.feat h3{font-size:20px;font-weight:750;letter-spacing:-.2px}
.feat .d{font-size:15.5px;line-height:1.55;color:var(--muted)}
.ex{margin-top:auto;background:#f8f7f3;border:1px solid #eeeae1;border-radius:12px;padding:12px 13px;display:flex;flex-direction:column;gap:7px}
.b{font:15px/1.5 var(--mono);color:#7a828f;text-decoration:line-through;text-decoration-color:#d6574a;text-decoration-thickness:1.5px}
.a{font:600 15px/1.5 var(--mono);color:var(--ok)}
.raw{font:15px/1.5 var(--mono);color:#3b4350;white-space:pre}
.arrow{font:12px var(--mono);color:var(--faint)}
.tags{display:flex;gap:6px;flex-wrap:wrap}
.kw{font:600 13px var(--mono);background:#fff;border:1px solid var(--line);border-radius:8px;padding:4px 8px}
.strip{display:grid;grid-template-columns:auto 1fr auto;gap:28px;align-items:center;padding:16px 22px}
.strip .grp{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.strip .k{font-size:12.5px;font-weight:700;letter-spacing:1.2px;color:var(--faint);text-transform:uppercase;margin-right:4px}
.cmd{font:600 15px var(--mono);background:#14181f;color:#f2f4f7;border-radius:10px;padding:9px 14px;white-space:nowrap}
"""


def e(s):
    return html.escape(s, quote=False)


def page(lang, body, h):
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}'
            f':root{{--h:{h}px}}body{{font-family:{FONTS[lang]};height:{h}px}}</style></head><body>{body}</body></html>')


# ---------------------------------------------------------------- hero data
# Abstract segments: plain strings, or (text, class, number-or-None).
ABSTRACT_ZH = [
    ("With the development of deep learning, more and more attention has been paid to", "unn", "1"),
    " defect detection of steel surface. In order to ", ("solve", "minor", None),
    " the problem of low accuracy of small defect detection, an improved algorithm based on YOLOv8 ",
    ("is put forward in this paper", "unn", "2"), ". Firstly, ",
    ("attention mechanism", "err", "3"), " is introduced into ", ("backbone network", "err", None),
    ". Secondly, ", ("by this way", "unn", "4"), " of multi-scale fusion, the detection ",
    ("effect to", "minor", None), " small targets is improved. ", ("Experiment results", "minor", None),
    " show that the mAP of ", ("proposed method", "turn", "?"), " reaches 86.4%, which is ",
    ("3.2% higher", "err", "5"), " than ", ("original YOLOv8", "turn", "?"),
    (", the method realizes", "err", "6"), " real-time detection. ", ("Obviously", "minor", None),
    ", the proposed method has a great application value.",
]

ABSTRACT_JA = [
    "In this study, ", ("we tried to propose", "unn", "1"), " a new method for ",
    ("the estimation of the soil moisture", "err", "2"), ". ", ("Firstly", "minor", None), ", we ",
    ("made the dataset by the satellite images", "err", "3"), ". ",
    ("It was confirmed that", "unn", "4"), " the proposed method has ",
    ("high accuracy than", "err", "5"), " previous methods. The accuracy was ",
    ("improved 12%", "err", "6"), " by using ", ("the attention", "minor", None), ". Therefore, ",
    ("we think", "minor", None), " this method can be used for ", ("the agriculture field", "minor", None),
    ". However, ", ("there is a problem that", "turn", "?"), " the calculation cost is high.",
]

ZH_NOTES = [  # (kind, before, after, extra-pill-key)
    ("unn", "With the development of… more and more attention…", "Deep learning is increasingly used for…", None),
    ("unn", "is put forward in this paper", "we propose", None),
    ("err", "attention mechanism … backbone network", "an attention mechanism … the backbone network", None),
    ("unn", "by this way of multi-scale fusion", "Multi-scale feature fusion improves…", None),
    ("err", "3.2% higher", "3.2 percentage points higher", "meaning"),
    ("err", ", the method realizes real-time detection", ". It runs in real time.", None),
]
JA_NOTES = [
    ("unn", "we tried to propose", "we propose", None),
    ("err", "the estimation of the soil moisture", "estimating soil moisture", None),
    ("err", "made the dataset by the satellite images", "built the dataset from satellite images", None),
    ("unn", "It was confirmed that the proposed method…", "The results show that our method…", None),
    ("err", "high accuracy than", "higher accuracy than", None),
    ("err", "improved 12%", "improved by 12 percentage points", "meaning"),
]

HERO = {
    "en": dict(
        summary=[("sentences", "6"), ("notes", "10"), ("left for you", "2")],
        slogan="Learn to write English yourself, even with AI around.",
        sub="Reviews the English you wrote, sentence by sentence, and tells you why.",
        chips=["Journal abstract", "Computer vision", "First language: Chinese"],
        draft="Your draft · Abstract", notes_label="Coach notes",
        kinds={"err": "ERROR", "unn": "UNNATURAL", "reg": "REGISTER"}, meaning="CHANGES MEANING",
        ptitle="Small Defect Detection on Steel Surfaces Based on Improved YOLOv8",
        keywords="defect detection; YOLOv8; attention mechanism; multi-scale feature fusion",
        abstract=ABSTRACT_ZH, notes=ZH_NOTES,
        why=[
            "Translated from a Chinese essay opener. Reviewers skip it; state the change itself.",
            "Put forward is for ideas in a debate. For your own method, use propose.",
            "A singular countable noun needs a determiner. Readers know which backbone: the.",
            "Way takes in or nothing, never by. Better: make the method the subject.",
            "83.2 → 86.4 is +3.2 points, not +3.2%. Check which one you mean.",
            "Two sentences joined by a comma, and realize means “become aware”.",
        ],
        more="+ 4 lighter notes: solve, effect to, Experiment results, Obviously",
        habits_label="Habits this time",
        habits=[("Missing articles", 4), ("Chinese template phrases", 3), ("Literal verbs (put forward, realize)", 3)],
        turn_label="Your turn",
        turn="Two nouns marked ? still need the. Fix them yourself and send the sentence back.",
        nb_label="Notebook updated",
        nb=[("article", "7 → 11", "a", "active"), ("with-development", "2 → 3", "a", "active"),
            ("by-this-way", "3", "m", "mastered")],
    ),
    "zh-CN": dict(
        summary=[("个句子", "6"), ("处批改", "10"), ("留给你改", "2")],
        slogan="AI 时代，亲手学习英文写作。",
        sub="逐句批改你自己写的英文，告诉你为什么这样改。",
        chips=["期刊摘要", "计算机视觉", "母语：简体中文"],
        draft="你的草稿 · 摘要", notes_label="批改",
        kinds={"err": "错误", "unn": "不地道", "reg": "语体"}, meaning="会改变意思",
        ptitle="Small Defect Detection on Steel Surfaces Based on Improved YOLOv8",
        keywords="defect detection; YOLOv8; attention mechanism; multi-scale feature fusion",
        abstract=ABSTRACT_ZH, notes=ZH_NOTES,
        why=[
            "“随着……的发展”是中文作文开头的直译，审稿人会直接跳过。直接写变化本身。",
            "put forward 多用于讨论中提出观点。提出自己的方法用 propose。",
            "单数可数名词前要有冠词。读者知道是哪个骨干网络，所以用 the。",
            "way 前面不用 by。更好的写法：让方法本身做主语。",
            "83.2 → 86.4 是 3.2 个百分点，不是 3.2%。请确认你想表达哪一个。",
            "逗号连接了两个完整句子；realize 是“意识到”，“实现”用 achieve / allow。",
        ],
        more="另有 4 处小问题：solve、effect to、Experiment results、Obviously",
        habits_label="这次的习惯",
        habits=[("冠词遗漏", 4), ("中文模板句式", 3), ("动词直译（put forward、realize）", 3)],
        turn_label="轮到你",
        turn="标 ? 的两个名词也缺 the。自己改好，把这句发回来。",
        nb_label="错题本已更新",
        nb=[("article", "7 → 11", "a", "active"), ("with-development", "2 → 3", "a", "active"),
            ("by-this-way", "3", "m", "mastered")],
    ),
    "zh-TW": dict(
        summary=[("個句子", "6"), ("處批改", "10"), ("留給你改", "2")],
        slogan="AI 時代，親手學習英文寫作。",
        sub="逐句批改你自己寫的英文，告訴你為什麼這樣改。",
        chips=["期刊摘要", "電腦視覺", "母語：中文"],
        draft="你的草稿 · 摘要", notes_label="批改",
        kinds={"err": "錯誤", "unn": "不道地", "reg": "語氣"}, meaning="會改變意思",
        ptitle="Small Defect Detection on Steel Surfaces Based on Improved YOLOv8",
        keywords="defect detection; YOLOv8; attention mechanism; multi-scale feature fusion",
        abstract=ABSTRACT_ZH, notes=ZH_NOTES,
        why=[
            "「隨著……的發展」是中文作文開頭的直譯，審稿人會直接跳過。直接寫變化本身。",
            "put forward 多用在討論中提出觀點。提出自己的方法用 propose。",
            "單數可數名詞前要有冠詞。讀者知道是哪個骨幹網路，所以用 the。",
            "way 前面不用 by。更好的寫法：讓方法本身當主詞。",
            "83.2 → 86.4 是 3.2 個百分點，不是 3.2%。請確認你要表達哪一個。",
            "逗號連接了兩個完整句子；realize 是「意識到」，「實現」用 achieve / allow。",
        ],
        more="另有 4 處小問題：solve、effect to、Experiment results、Obviously",
        habits_label="這次的習慣",
        habits=[("冠詞漏掉", 4), ("中文模板句型", 3), ("動詞直譯（put forward、realize）", 3)],
        turn_label="換你",
        turn="標 ? 的兩個名詞也少了 the。自己改好，把這句傳回來。",
        nb_label="錯題本已更新",
        nb=[("article", "7 → 11", "a", "active"), ("with-development", "2 → 3", "a", "active"),
            ("by-this-way", "3", "m", "mastered")],
    ),
    "ja": dict(
        summary=[("文", "6"), ("件の添削", "10"), ("あなたが直す", "1")],
        slogan="AI 時代こそ、英語は自分の手で書いて学ぶ。",
        sub="あなたが書いた英語を一文ずつ添削し、理由まで説明します。",
        chips=["論文アブストラクト", "リモートセンシング", "母語：日本語"],
        draft="あなたの下書き · アブストラクト", notes_label="添削",
        kinds={"err": "誤り", "unn": "不自然", "reg": "語調"}, meaning="意味が変わる",
        ptitle="Soil Moisture Estimation from Satellite Images Using an Attention Model",
        keywords="soil moisture; remote sensing; deep learning; attention",
        abstract=ABSTRACT_JA, notes=JA_NOTES,
        why=[
            "「〜を試みた」の直訳。提案したのなら、言い切ります。",
            "一般的な概念には the を付けません。動名詞にすると短くなります。",
            "材料・出どころは from。by は手段や行為者を表します。",
            "「確認された」の直訳。何が示したのかを主語にします。",
            "than を使うなら比較級：higher accuracy than。",
            "80% → 92% なのか 89.6% なのか、読み手には分かりません。確認を。",
        ],
        more="ほか 4 件：Firstly、the attention、we think、the agriculture field",
        habits_label="今回の癖",
        habits=[("the の付けすぎ", 4), ("日本語の直訳表現", 3), ("比較と数値", 2)],
        turn_label="あなたの番",
        turn="? の付いた最後の文を、there is a problem that を使わずに書き直してみよう。",
        nb_label="間違いノートを更新",
        nb=[("the-overuse", "5 → 9", "a", "active"), ("jp-literal", "3 → 6", "a", "active"),
            ("until-by", "4", "m", "mastered")],
    ),
}

KIND_VAR = {"err": "var(--err)", "unn": "var(--unn)", "reg": "var(--reg)"}


def build_hero(lang):
    c = HERO[lang]
    parts = []
    for seg in c["abstract"]:
        if isinstance(seg, str):
            parts.append(e(seg))
        else:
            text, cls, n = seg
            attr = f' data-n="{n}"' if n else ""
            parts.append(f'<span class="m {cls}"{attr}>{e(text)}</span>')
    abstract = "".join(parts)

    notes = []
    for i, ((kind, before, after, extra), why) in enumerate(zip(c["notes"], c["why"]), 1):
        pills = f'<span class="pill p-{kind}">{c["kinds"][kind]}</span>'
        if extra == "meaning":
            pills += f'<span class="pill p-warn">{c["meaning"]}</span>'
        notes.append(
            f'<div class="note"><div class="num" style="background:{KIND_VAR[kind]}">{i}</div><div>'
            f'<div class="pills">{pills}</div>'
            f'<div class="fix"><s>{e(before)}</s><b>→ </b>{e(after)}</div>'
            f'<div class="why">{e(why)}</div></div></div>')

    top = max(n for _, n in c["habits"])
    bars = "".join(
        f'<div class="bar"><div>{e(name)}<div class="track"><i style="width:{n / top * 100:.0f}%"></i></div></div>'
        f'<div style="font:700 16px var(--mono);text-align:right">×{n}</div></div>' for name, n in c["habits"])
    nb = "".join(f'<div>{e(s)}</div><div style="color:var(--muted)">{e(cnt)}</div>'
                 f'<div><span class="st {k}">{e(lbl)}</span></div>' for s, cnt, k, lbl in c["nb"])
    chips = "".join(f'<span class="chip">{e(x)}</span>' for x in c["chips"])
    summary = "".join(f'<div><b>{e(n)}</b>{e(lbl)}</div>' for lbl, n in c["summary"])

    body = f"""<div class="frame">
<div class="head"><div><div class="brand">english-coach</div><h1>{e(c['slogan'])}</h1><p class="sub">{e(c['sub'])}</p></div></div>
<div class="main">
 <div class="left">
  <section class="card paper"><div class="phead"><div class="label">{e(c['draft'])}</div><div class="chips">{chips}</div></div>
   <div class="ptitle2">{e(c['ptitle'])}</div>
   <p class="abstract" style="margin-top:6px">{abstract}</p>
   <div class="kw2"><b>Keywords:</b> {e(c['keywords'])}</div></section>
  <div class="foot">
   <div class="card box"><div class="label">{e(c['habits_label'])}</div><div class="summary">{summary}</div>{bars}</div>
   <div class="stack">
    <div class="card box turnbox"><div class="label">{e(c['turn_label'])}</div><p>{e(c['turn'])}</p></div>
    <div class="card box"><div class="label">{e(c['nb_label'])}</div><div class="nb">{nb}</div></div>
   </div>
  </div>
 </div>
 <section class="notes"><div class="label">{e(c['notes_label'])}</div>{''.join(notes)}<div class="more">{e(c['more'])}</div></section>
</div></div>"""
    return page(lang, body, SIZES["hero"])


# ---------------------------------------------------------------- features data
# Example blocks: ("b", text) struck-through before, ("a", text) after, ("raw", text), ("tags", [..]).
FEATURES = {
    "en": dict(
        title="What english-coach does",
        sub="It reads what you send and picks the mode itself. Explanations come in your language.",
        cards=[
            ("Sentence-by-sentence review", "Every fix comes with a reason you can reuse next time.",
             [("b", "The result show that proposed method is effective."), ("a", "The results show that the proposed method is effective.")]),
            ("Start from your own language", "Chinese or Japanese notes become an outline and sentence frames. You write the draft.",
             [("raw", "想问教授明年还招不招博士生"), ("arrow", "↓ frame"), ("a", "I'm writing to ask whether you will be accepting PhD students for ___.")]),
            ("Mixed-language drafts", "Fills the gaps, and flags office English that means something else.",
             [("b", "确认 the 交期, push 一下 vendor"), ("a", "confirm the delivery date, follow up with the vendor")]),
            ("AI-style check", "Names the phrases that make a draft read machine-written. Never guesses whether you used AI.",
             [("b", "I hope this email finds you well. I'm thrilled to delve into…"), ("a", "Say who you are and what you need in line one.")]),
            ("The right tone for the reader", "Singlish, chat style or 1960s office English, adjusted for overseas and formal readers.",
             [("b", "Pls revert by Fri. Noted with thanks."), ("a", "Could you reply by Friday, 23 October?")]),
            ("Notes, slides and talks", "Slide titles that state the point, notes that separate claims from opinion, scripts that sound spoken.",
             [("b", "Experiment / Thank you for your listening!"), ("a", "3× faster at 128K tokens / Questions?")]),
            ("Field vocabulary", "Terms, collocations and traps for your field, with examples from your own text.",
             [("tags", ["lead time", "place an order", "significant = p < 0.05", "revenue ≠ profit"])]),
            ("Error notebook and quizzes", "Tracks your recurring mistakes, checks them first, and quizzes you on them.",
             [("raw", "article        ×11  active"), ("raw", "realize        ×3   improving"), ("raw", "by-this-way    ✓    mastered")]),
        ],
        langs=("Explains in", ["简体中文", "繁體中文", "日本語", "English"]),
        genres=("Covers", ["papers", "reviewer replies", "email", "reports", "notes", "slides"]),
    ),
    "zh-CN": dict(
        title="english-coach 能做什么",
        sub="看你发来的内容，自动选择模式。讲解用你的语言。",
        cards=[
            ("逐句批改", "每处修改都讲原因，下次遇到同样的问题你自己就会改。",
             [("b", "The result show that proposed method is effective."), ("a", "The results show that the proposed method is effective.")]),
            ("从中文起步", "中文想法变成英文结构和留空的句式，草稿由你自己写。",
             [("raw", "想问教授明年还招不招博士生"), ("arrow", "↓ 句式"), ("a", "I'm writing to ask whether you will be accepting PhD students for ___.")]),
            ("中英混合", "帮你补上中文的部分，并指出办公室里意思已经变了的英文。",
             [("b", "确认 the 交期, push 一下 vendor"), ("a", "confirm the delivery date, follow up with the vendor")]),
            ("AI 腔检查", "指出哪些说法读起来像机器写的。不会去猜你有没有用 AI。",
             [("b", "I hope this email finds you well. I'm thrilled to delve into…"), ("a", "第一行就说你是谁、需要什么。")]),
            ("语气对得上读者", "Singlish、聊天口吻、老式公文腔，改成海外读者和正式场合看得懂的写法。",
             [("b", "Pls revert by Fri. Noted with thanks."), ("a", "Could you reply by Friday, 23 October?")]),
            ("笔记、slides 和讲稿", "slide 标题直接写结论，笔记分清论文观点和你的看法，讲稿改成说得出口的英文。",
             [("b", "Experiment / Thank you for your listening!"), ("a", "3× faster at 128K tokens / Questions?")]),
            ("领域词汇", "你这个领域的术语、搭配和易错词，例句取自你自己的稿子。",
             [("tags", ["lead time", "place an order", "significant = p < 0.05", "revenue ≠ profit"])]),
            ("错题本和测验", "记录你反复出现的错误，每次先查，还能出题考你。",
             [("raw", "article        ×11  active"), ("raw", "realize        ×3   improving"), ("raw", "by-this-way    ✓    mastered")]),
        ],
        langs=("讲解语言", ["简体中文", "繁體中文", "日本語", "English"]),
        genres=("适用", ["论文", "审稿回复", "邮件", "报告", "笔记", "slides"]),
    ),
    "zh-TW": dict(
        title="english-coach 能做什麼",
        sub="看你傳來的內容，自動選擇模式。用你的語言講解。",
        cards=[
            ("逐句批改", "每個修改都講原因，下次遇到同樣的問題你自己就會改。",
             [("b", "The result show that proposed method is effective."), ("a", "The results show that the proposed method is effective.")]),
            ("從中文起步", "中文想法變成英文架構和留空的句型，草稿由你自己寫。",
             [("raw", "想問教授明年還收不收博士生"), ("arrow", "↓ 句型"), ("a", "I'm writing to ask whether you will be accepting PhD students for ___.")]),
            ("中英夾雜", "幫你補上中文的部分，並指出辦公室裡意思已經跑掉的英文。",
             [("b", "這個 case 我會 follow, 已經 push vendor"), ("a", "I'll follow up on this project with the vendor")]),
            ("AI 腔檢查", "指出哪些說法讀起來像機器寫的。不會去猜你有沒有用 AI。",
             [("b", "I hope this email finds you well. I'm thrilled to delve into…"), ("a", "第一行就說你是誰、需要什麼。")]),
            ("語氣對得上讀者", "港式、新加坡式英文、聊天口吻、老派公文腔，改成海外讀者看得懂的寫法。",
             [("b", "Pls revert by Fri. Noted with thanks."), ("a", "Could you reply by Friday, 23 October?")]),
            ("筆記、slides 和講稿", "slide 標題直接寫結論，筆記分清論文觀點和你的看法，講稿改成講得出口的英文。",
             [("b", "Experiment / Thank you for your listening!"), ("a", "3× faster at 128K tokens / Questions?")]),
            ("領域詞彙", "你這個領域的術語、搭配和易錯字，例句取自你自己的稿子。",
             [("tags", ["lead time", "place an order", "significant = p < 0.05", "revenue ≠ profit"])]),
            ("錯題本和測驗", "記錄你常犯的錯，每次先檢查，還會出題考你。",
             [("raw", "article        ×11  active"), ("raw", "office-push    ×3   improving"), ("raw", "by-this-way    ✓    mastered")]),
        ],
        langs=("講解語言", ["简体中文", "繁體中文", "日本語", "English"]),
        genres=("適用", ["論文", "審稿回覆", "email", "報告", "筆記", "slides"]),
    ),
    "ja": dict(
        title="english-coach でできること",
        sub="送られた内容から、モードを自動で選びます。説明はあなたの言語で。",
        cards=[
            ("一文ずつ添削", "直した理由も必ず添えるので、次は自分で直せます。",
             [("b", "I look forward to hear from you."), ("a", "I look forward to hearing from you.")]),
            ("日本語から書き出す", "日本語のメモを英語の構成と空欄つきの文型に。下書きはあなたが書きます。",
             [("raw", "来週の打ち合わせを延期したい"), ("arrow", "↓ 文型"), ("a", "Would it be possible to move ___ to ___?")]),
            ("日英ミックス", "日本語の部分を補い、意味がずれたカタカナ英語を指摘します。",
             [("b", "MTG で evidence を共有、claim の件"), ("a", "share the records at the meeting; the complaint")]),
            ("AI 調チェック", "機械っぽく読まれる表現を指摘します。AI を使ったかどうかの推測はしません。",
             [("b", "I hope this email finds you well. I'm thrilled to delve into…"), ("a", "1行目で、誰が何を頼みたいのかを書く。")]),
            ("読み手に合った語調", "くだけすぎ、硬すぎ、シンガポール英語を、海外の読み手やフォーマルな場に合わせます。",
             [("b", "Please teach me the data until Friday."), ("a", "Could you send me the data by Friday?")]),
            ("メモ、スライド、発表", "結論が分かるスライドタイトル、主張と意見を分けたメモ、声に出して自然な原稿に。",
             [("b", "Experiment / Thank you for your kind attention."), ("a", "3× faster at 128K tokens / Questions?")]),
            ("分野の語彙", "分野の用語、コロケーション、間違えやすい語を、あなたの文章から例文にします。",
             [("tags", ["corrective action", "lead time", "significant = p < 0.05", "complaint ≠ claim"])]),
            ("間違いノートとテスト", "くり返す間違いを記録し、毎回まずそこを確認。テストも出します。",
             [("raw", "until-by       ×4   active"), ("raw", "wasei-claim    ×2   improving"), ("raw", "jp-literal     ✓    mastered")]),
        ],
        langs=("説明の言語", ["简体中文", "繁體中文", "日本語", "English"]),
        genres=("対象", ["論文", "査読への回答", "メール", "レポート", "メモ", "スライド"]),
    ),
}


def build_features(lang):
    c = FEATURES[lang]
    cards = []
    for i, (title, desc, ex) in enumerate(c["cards"], 1):
        rows = []
        for kind, val in ex:
            if kind == "tags":
                rows.append('<div class="tags">' + "".join(f'<span class="kw">{e(x)}</span>' for x in val) + "</div>")
            else:
                rows.append(f'<div class="{kind}">{e(val)}</div>')
        cards.append(f'<div class="card feat"><div class="ftop"><span class="fnum">{i:02d}</span><h3>{e(title)}</h3></div>'
                     f'<div class="d">{e(desc)}</div><div class="ex">{"".join(rows)}</div></div>')
    lk, langs = c["langs"]
    gk, genres = c["genres"]
    strip = (f'<div class="card strip"><div class="grp"><span class="k">{e(lk)}</span>'
             + "".join(f'<span class="chip">{e(x)}</span>' for x in langs)
             + f'</div><div class="grp"><span class="k">{e(gk)}</span>'
             + "".join(f'<span class="chip">{e(x)}</span>' for x in genres)
             + '</div><div class="cmd">npx skills add nilikun/english-coach</div></div>')
    body = f"""<div class="frame">
<div class="head"><div><h1>{e(c['title'])}</h1><p class="sub">{e(c['sub'])}</p></div></div>
<div class="grid">{''.join(cards)}</div>{strip}</div>"""
    return page(lang, body, SIZES["features"])


def render(html_text, name, h):
    BUILD.mkdir(parents=True, exist_ok=True)
    src = BUILD / f"{name}.html"
    src.write_text(html_text, encoding="utf-8")
    if "--html-only" in sys.argv:
        return
    out = ASSETS / f"{name}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", f"--window-size={W},{h}",
                    f"--screenshot={out}", src.as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    for lang in HERO:
        render(build_hero(lang), f"hero-{lang}", SIZES["hero"])
        render(build_features(lang), f"features-{lang}", SIZES["features"])
