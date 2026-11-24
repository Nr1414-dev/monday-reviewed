#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes a single one-line review of the entrant's own Monday, under
200 characters, to /output/entry.txt. Deterministic: the same bytes
on every run.
"""

LINE = "Monday: 8 a.m. dentist, 9 a.m. meeting, 10 a.m. regret \u2014 the drill was the only thing that listened."


def main() -> None:
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    import os

    os.chmod(path, 0o644)
    # Read-back guard: the file on disk must be byte-identical to the
    # validated line, one line, under 200 characters, no trailing newline.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry mismatch"
    assert 1 <= len(written) <= 200, "entry length out of range"
    assert written == written.strip() and "\n" not in written, "entry not one clean line"


if __name__ == "__main__":
    main()
