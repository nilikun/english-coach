# Error notebook

Writers improve fastest when they work on their own recurring mistakes, not a textbook's. The notebook records each user's habits across sessions, so reviews can focus on what this person keeps doing and quizzes can drill it.

## Where it lives

Try these in order and use the first that works:

1. `~/.english-coach/notebook.md` (the user's home directory). Works across projects in Claude Code and most local agents.
2. `./.english-coach/notebook.md` in the current workspace, when the agent can't write outside the project.
3. No file access (e.g. a chat app): print the notebook as a markdown block at the end of the reply and tell the user to save it and paste it back at the start of the next session.

Tell the user where it's saved the first time you write it.

## Consent and privacy

- **Ask once before creating it**, in one line, after the first review: "要不要我建一个错题本，记录你常犯的问题，下次重点检查？" If they say no, don't ask again in this session.
- If a notebook already exists, read it at the start of a review and use it without asking.
- Store **patterns and short snippets** only, 15 words at most per example. Never store whole emails or papers.
- Replace names, company names, email addresses, amounts and other confidential details in snippets with placeholders: `[client]`, `[amount]`, `[colleague]`.

## Format

Keep it plain markdown so the user can read and edit it by hand.

```markdown
# English Coach notebook
<!-- Managed by the english-coach skill. You can edit this file by hand. -->

## Profile
- Explain in: 简体中文
- First language: Chinese (Mainland)
- Writes mostly: research papers (materials science), email to supervisor
- Last session: 2026-10-19

## Habits
| slug | habit | count | last seen | example (theirs → fix) | status |
|---|---|---|---|---|---|
| article | 冠词遗漏 | 7 | 2026-10-19 | on surface of the film → on the surface of the film | active |
| realize | realize 当"实现" | 2 | 2026-10-12 | realize the function → implement the function | improving |
| with-development | "随着…的发展"开头 | 3 | 2026-09-30 | With the development of AI, … → (state the change directly) | mastered |

## Words I'm learning
| term | meaning | example | added | used |
|---|---|---|---|---|
| lead time | 交货周期 | The lead time is now eight weeks. | 2026-10-19 | no |

## Log
- 2026-10-19 · email to supervisor · 9 notes · article×3, long-sentence×1, realize×1
```

## Updating after a review

1. Read the notebook first. In the review, check the user's active habits first, and point it out when one appears again ("又是冠词：这已经是第 8 次了。").
2. After the review, for each slug you flagged: increase `count`, update `last seen` and the example (keep the newest one).
3. Update status:
   - `active`: seen in the last 2 sessions where it could have appeared.
   - `improving`: not seen in the last 2 such sessions.
   - `mastered`: not seen in the last 5 such sessions. Say so to the user; it's encouraging.
   - A mastered habit that shows up again goes back to `active`.
4. If the user used a word from *Words I'm learning* correctly, set `used` to the date.
5. Add one line to the log. Keep the log to the latest 30 lines.
6. Tell the user in one line what changed ("错题本已更新：冠词 +3，realize 已经两次没出现了，标为 improving").

## Quiz

When the user asks for a quiz ("quiz me", "出题", "复习", "テストして"):

1. Pick 5 items, mostly `active` habits, plus one `improving` habit and one word from the list.
2. Write short new sentences that contain the same kind of mistake, in the user's field. Base them on the user's snippets, but change the content so it isn't pure memory.
3. Mix formats: find-and-fix, choose the right word, fill the blank, rewrite one sentence.
4. Give all 5 at once, wait for answers, then mark them with a one-line reason each.
5. Update counts: a correct answer counts as a "not seen" session for that habit; a wrong answer counts as seen.

## Commands to recognize

- Show the notebook: "看错题本", "my notebook", "ノートを見せて"
- Quiz: "quiz me", "出题", "复习错题", "復習", "テスト"
- Reset or delete: "清空错题本", "delete my notebook". Confirm once, then do it.
- Change the explanation language: "用英文解释", "explain in Japanese". Update the profile.
