#!/usr/bin/env python3
"""One-Line Roast entry: writes a single original roast of the laptop
I use every day to entry.txt. Deterministic, stdlib only, no network,
no randomness, no file reads outside this repo."""

import os
import sys

ROAST = (
    "My laptop treats sleep mode as a suggestion: close the lid and it "
    "spends all night awake in my bag, warm, glowing, and quietly "
    "judging me for going to bed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
