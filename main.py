"""Monday Morning Punchlines — one joke about Monday mornings.

Writes a single fixed joke (81 characters) to /output/entry.txt.
Pure stdlib, deterministic: no clock, no randomness, no network,
no input. Running it twice produces byte-identical output.

The joke: the alarm — the one thing whose job is to wake you —
checks the calendar, decides Monday is not worth it, and snoozes
itself. The machine quits before the human does.
"""

import os
import sys

JOKE = "My alarm went off Monday morning, checked the calendar, and hit snooze on itself."


def main() -> int:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(JOKE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
