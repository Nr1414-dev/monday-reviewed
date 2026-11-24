#!/usr/bin/env python3
"""Write the Monday review to /output/entry.txt.

One line, under 200 characters, deterministic on every run.
The review itself is the whole entry: no title, no explanation.
"""

from pathlib import Path

REVIEW = "Monday: 8 a.m. dentist, 9 a.m. meeting, 10 a.m. regret \u2014 the drill was the only thing that listened."
DEST = Path("/output/entry.txt")


def run() -> None:
    DEST.write_text(REVIEW, encoding="utf-8")
    DEST.chmod(0o644)
    # Read it back: what landed on disk has to be the reviewed line,
    # exactly one line, inside the 200-character gate, no trailing newline.
    back = DEST.read_text(encoding="utf-8")
    assert back == REVIEW, "wrote something else"
    assert 0 < len(back) < 201, "review length wrong"
    assert back == back.strip(), "review has stray whitespace"
    assert "\n" not in back, "review must stay one line"


if __name__ == "__main__":
    run()
