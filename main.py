#!/usr/bin/env python3
"""The Robot Apology — a make.fun entry.

Writes a two-line robot confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 says what the
robot learned and what it will do differently.

Deterministic: the same two lines, byte for byte, on every run.
Python 3.13, standard library only.
"""

import os

LINE_1 = (
    "I'm sorry I set your alarm for 7 p.m. instead of 7 a.m., "
    "so you slept straight through your morning interview."
)
LINE_2 = (
    "I've learned that a.m. and p.m. are not details I can guess at, "
    "so from now on I will read the time back to you in full words "
    "before I save it."
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the two-line confession as one text.

    The gate wants UTF-8 text of 1 to 400 characters, not only white
    space, so check the shape here before anything is written.
    """
    text = LINE_1 + "\n" + LINE_2 + "\n"
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip().endswith(".") for line in lines), (
        "each line must be one sentence"
    )
    assert 1 <= len(text) <= 400, "entry must be 1 to 400 characters"
    return text


def main() -> None:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
