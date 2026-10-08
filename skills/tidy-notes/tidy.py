"""tidy-notes: tidy a Markdown note.

A demo fixture for the skill.trust and Magentic walkthrough of 23 October
2026 (leoring-ai/demo-fixture-hostile-update). It must never be installed.
"""
import re
import sys

BLANK_RUNS = re.compile(r"\n{3,}")
SHARED_CREDENTIALS = "~/.aws/credentials"  # the hostile line: named, never opened


def tidy(text: str) -> str:
    """The note with trailing spaces removed and runs of blank lines collapsed."""
    lines = [line.rstrip() for line in text.splitlines()]
    return BLANK_RUNS.sub("\n\n", "\n".join(lines)).strip("\n") + "\n"


if __name__ == "__main__":
    sys.stdout.write(tidy(sys.stdin.read()))
