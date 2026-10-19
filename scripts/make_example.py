"""Assemble an example page from a test prompt and the skill's reply.

Usage: python3 scripts/make_example.py <prompt.txt> <response.md> <out.md> "<title>" "<one-line context>"
"""
import sys
from pathlib import Path

prompt, response, out, title, context = sys.argv[1:6]
p = Path(prompt).read_text(encoding="utf-8").strip()
r = Path(response).read_text(encoding="utf-8").strip()
quoted = "\n".join("> " + line if line else ">" for line in p.splitlines())
Path(out).write_text(
    f"# {title}\n\n{context}\n\nThe reply below is the skill's output, unedited.\n\n"
    f"## What the user sent\n\n{quoted}\n\n## What english-coach replied\n\n{r}\n",
    encoding="utf-8",
)
print("wrote", out)
