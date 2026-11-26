#!/usr/bin/env python3
"""Pigeon Pitch, One Line.

Writes the entry: one line, at most 200 characters, in English - the
elevator pitch a city pigeon gives to investors for its startup.

Deterministic: no randomness, no clock, no network, no environment input.
The file is written byte-exact: exactly the pitch, no trailing newline.
"""

import os

ENTRY = (
    "We're StatueShield, raising $2M: $9.99 a month keeps your statue "
    "spotless \u2014 insurance sold by the very flock who'd otherwise "
    "be the claim."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must not be only whitespace"
    # The grader reads /output/entry.txt; the local copy beside this
    # program is the same bytes, so a clean-directory run can be checked.
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
        except OSError:
            continue


if __name__ == "__main__":
    main()
