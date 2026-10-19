# Contributing

Thanks for helping. The most useful contributions are real mistakes from real writers, and new first-language modules.

## Report a wrong or missing correction

Open an issue with:

- the sentence you wrote (remove names and confidential details),
- what english-coach said,
- what you think it should have said, and why.

Corrections from teachers, editors and native speakers in a specific field are especially welcome.

## Add a habit to an existing language

Edit the matching file in `skills/english-coach/references/l1/`. Each habit needs:

- a **slug** in backticks (short, kebab-case, unique in that file),
- the mistake as learners actually write it,
- the fix,
- one line on why the mistake happens or how it reads to an English speaker.

Keep the example sentences your own. Don't paste from textbooks or paid courses.

## Add a new first language

1. Copy `references/l1/japanese.md` as a template and name the file after the language (`korean.md`).
2. Cover the same ground: grammar the language doesn't mark, false friends and loanwords, literal set phrases, email conventions, academic habits, mechanics (punctuation, spacing).
3. Add one line to the first-language list in `SKILL.md`.
4. Add at least two test prompts to `evals/evals.json`: one email, one paper paragraph or report.
5. Run the prompts with the skill installed and put the best reply in `examples/`. Don't edit the reply; if it's wrong, fix the skill instead.

The roadmap in the README lists the languages people have asked for.

## Style for skill files

- Explain *why* a rule exists. The model applies a reason more reliably than a bare rule.
- Prefer plain English. If a reference file starts to sound like marketing, cut it.
- Keep `SKILL.md` short. Detailed guidance belongs in `references/`.

## Rebuild the README images

The images are HTML pages rendered with headless Google Chrome. Edit the text in `scripts/make_images.py`, then:

```bash
python3 scripts/make_images.py
```

Set `CHROME=/path/to/chrome` if Chrome isn't in the default macOS location.
