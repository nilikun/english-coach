"""Generate the README hero images (assets/hero-<lang>.svg).

Run: python3 scripts/make_hero.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1200, 640
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'PingFang TC', "
        "'Hiragino Sans', 'Noto Sans CJK SC', 'Microsoft YaHei', 'Yu Gothic', sans-serif")

KIND = {  # marker colors: (fill, text)
    "error": ("#fde2e1", "#b42318"),
    "unnatural": ("#fef0c7", "#93370d"),
    "register": ("#e0eaff", "#3538cd"),
    "ai": ("#f4ebff", "#6941c6"),
}

# Draft lines; spans to highlight are given as (line, start_char, end_char, kind).
DRAFT_EN = [
    "Dear Mr. David,",
    "",
    "I hope this email finds you well.",
    "Please kindly be noted that the",
    "delivery will delay to next Friday",
    "because the raw material is short.",
    "Please reply me as soon as possible.",
]
SPANS_EN = [(0, 5, 14, "unnatural"), (2, 0, 33, "ai"), (3, 7, 22, "register"),
            (4, 9, 22, "error")]

DRAFT_JA = [
    "Dear Mr. Johnson-san,",
    "",
    "Thank you for your continued support.",
    "We received a claim from our customer.",
    "Please teach me the inspection data",
    "until this Friday.",
]
SPANS_JA = [(0, 5, 20, "unnatural"), (3, 14, 19, "unnatural"), (4, 7, 12, "error"),
            (5, 0, 5, "error")]

LANGS = {
    "en": {
        "tagline": "Learn to write English yourself, even with AI around.",
        "sub": "Reviews the English you wrote, sentence by sentence, and tells you why.",
        "draft_label": "YOUR DRAFT",
        "notes_label": "COACH NOTES",
        "draft": DRAFT_EN, "spans": SPANS_EN,
        "labels": {"error": "ERROR", "unnatural": "UNNATURAL", "register": "REGISTER", "ai": "AI-STYLE"},
        "notes": [
            ("unnatural", "Mr. David → Mr. Smith", "Mr. goes with the family name, not the given name."),
            ("ai", "I hope this email finds you well → (cut)", "Stock opener. Readers skim it. Start with the news."),
            ("register", "Please kindly be noted → Please note", "Old office English, and the grammar doesn't work."),
            ("error", "will delay to → will be delayed until", "A delivery doesn't delay itself. Use the passive."),
        ],
        "turn_label": "YOUR TURN",
        "turn": "“Please reply me” has a verb-pattern mistake. Fix it yourself.",
    },
    "zh-CN": {
        "tagline": "AI 时代，亲手学习英文写作。",
        "sub": "逐句批改你自己写的英文，告诉你为什么这样改。",
        "draft_label": "你的草稿",
        "notes_label": "批改",
        "draft": DRAFT_EN, "spans": SPANS_EN,
        "labels": {"error": "错误", "unnatural": "不地道", "register": "语体", "ai": "AI 腔"},
        "notes": [
            ("unnatural", "Mr. David → Mr. Smith", "Mr. 后面接姓，不接名。"),
            ("ai", "I hope this email finds you well → 删掉", "千篇一律的开头，读者直接跳过。第一句就说事。"),
            ("register", "Please kindly be noted → Please note", "老式公文腔，而且语法不对。"),
            ("error", "will delay to → will be delayed until", "货物不会自己“延迟”，要用被动。"),
        ],
        "turn_label": "轮到你",
        "turn": "“Please reply me” 还有一个动词搭配错误，自己改一下发回来。",
    },
    "zh-TW": {
        "tagline": "AI 時代，親手學習英文寫作。",
        "sub": "逐句批改你自己寫的英文，告訴你為什麼這樣改。",
        "draft_label": "你的草稿",
        "notes_label": "批改",
        "draft": DRAFT_EN, "spans": SPANS_EN,
        "labels": {"error": "錯誤", "unnatural": "不道地", "register": "語體", "ai": "AI 腔"},
        "notes": [
            ("unnatural", "Mr. David → Mr. Smith", "Mr. 後面接姓，不接名。"),
            ("ai", "I hope this email finds you well → 刪掉", "制式開頭，讀者會直接跳過。第一句就講重點。"),
            ("register", "Please kindly be noted → Please note", "老派公文腔，文法也不對。"),
            ("error", "will delay to → will be delayed until", "貨物不會自己「延遲」，要用被動。"),
        ],
        "turn_label": "換你",
        "turn": "「Please reply me」還有一個動詞用法錯誤，自己改改看再傳給我。",
    },
    "ja": {
        "tagline": "AI 時代こそ、英語は自分の手で書いて学ぶ。",
        "sub": "あなたが書いた英語を一文ずつ添削し、理由まで説明します。",
        "draft_label": "あなたの下書き",
        "notes_label": "添削",
        "draft": DRAFT_JA, "spans": SPANS_JA,
        "labels": {"error": "誤り", "unnatural": "不自然", "register": "語調", "ai": "AI 調"},
        "notes": [
            ("unnatural", "Mr. Johnson-san → Mr. Johnson", "敬称は一つだけ。Mr. と -san は重ねない。"),
            ("unnatural", "a claim → a complaint", "claim は「主張・請求」。苦情は complaint。"),
            ("error", "Please teach me → Could you send me", "teach は「授業をする」。資料がほしいなら send。"),
            ("error", "until this Friday → by this Friday", "期限は by。until は「〜までずっと」。"),
        ],
        "turn_label": "あなたの番",
        "turn": "冒頭の定型文は本当に必要？ 用件から始める形に書き直してみよう。",
    },
}


def text(x, y, s, size, fill, family=SANS, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def build(lang):
    c = LANGS[lang]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
           f'<rect width="{W}" height="{H}" rx="24" fill="#f7f5f0"/>']
    # Header
    out.append(text(56, 76, "english-coach", 22, "#667085", MONO, 600))
    out.append(text(56, 126, c["tagline"], 40, "#101828", SANS, 700))
    out.append(text(56, 164, c["sub"], 20, "#475467"))

    # Draft panel
    px, py, pw, ph = 56, 200, 500, 384
    out.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#ffffff" stroke="#e4e2dc"/>')
    out.append(text(px + 28, py + 40, c["draft_label"], 13, "#98a2b3", SANS, 700))
    fs, cw, lh = 18, 18 * 0.602, 34
    x0, y0 = px + 28, py + 88
    for (ln, a, b, kind) in c["spans"]:
        fill, stroke = KIND[kind]
        out.append(f'<rect x="{x0 + a * cw - 3:.1f}" y="{y0 + ln * lh - 20}" width="{(b - a) * cw + 6:.1f}" '
                   f'height="27" rx="5" fill="{fill}"/>')
        out.append(f'<rect x="{x0 + a * cw - 3:.1f}" y="{y0 + ln * lh + 5}" width="{(b - a) * cw + 6:.1f}" '
                   f'height="2.5" fill="{stroke}"/>')
    for i, line in enumerate(c["draft"]):
        out.append(f'<text x="{x0}" y="{y0 + i * lh}" font-family="{MONO}" font-size="{fs}" fill="#1d2939" '
                   f'xml:space="preserve">{escape(line)}</text>')

    # Notes panel
    nx, ny = 596, 200
    out.append(text(nx, ny + 40, c["notes_label"], 13, "#98a2b3", SANS, 700))
    y = ny + 70
    for kind, fix, why in c["notes"]:
        fill, stroke = KIND[kind]
        label = c["labels"][kind]
        lw = max(64, len(label) * (13 if lang == "en" else 17) + 20)
        out.append(f'<rect x="{nx}" y="{y - 16}" width="{lw}" height="24" rx="12" fill="{fill}"/>')
        out.append(text(nx + lw / 2, y + 1, label, 12.5, stroke, SANS, 700, "middle"))
        out.append(text(nx + lw + 12, y + 1, fix, 16.5, "#101828", MONO, 600))
        out.append(text(nx, y + 30, why, 16.5, "#475467"))
        y += 72

    # Your turn
    out.append(f'<rect x="{nx}" y="{y - 14}" width="{W - nx - 56}" height="64" rx="14" fill="#101828"/>')
    out.append(text(nx + 20, y + 12, c["turn_label"], 12.5, "#fec84b", SANS, 700))
    out.append(text(nx + 20, y + 36, c["turn"], 16, "#f2f4f7"))
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent / "assets"
    root.mkdir(exist_ok=True)
    for lang in LANGS:
        (root / f"hero-{lang}.svg").write_text(build(lang), encoding="utf-8")
        print("wrote", root / f"hero-{lang}.svg")
