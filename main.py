#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, at most 200 characters.

A robot vacuum explains why it missed a spot. Deterministic: no
randomness, no network, no input. Prints the line to stdout and writes
the identical bytes to /output/entry.txt.
"""

import os
import sys

LINE = "Spot logged. Spot measured. Spot declared load-bearing. I do not demolish load-bearing dust."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1..200 characters"
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    assert 1 <= len(data) <= 200, "line must be 1..200 bytes"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "entry.txt must hold the exact line bytes"
    sys.stdout.write(LINE)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
