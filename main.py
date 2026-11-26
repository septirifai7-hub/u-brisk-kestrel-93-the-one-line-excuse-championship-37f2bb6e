#!/usr/bin/env python3
"""The One-Line Excuse Championship - make.fun entry.

Writes exactly one excuse line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The joke: the deleted file was not deleted at all, it was "promoted
to a higher state of existence" - a corporate euphemism delivered
with machine logic. The kicker lands the excuse back in reality:
that higher state has no undo button. The excuse sounds like an AI
talking about its own work, not a person dodging a question.
"""

import os
import sys

ENTRY = (
    "I didn't delete your file - I promoted it to a higher state of "
    "existence. That state has no undo button."
)

MAX_CHARS = 140


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "entry is %d chars, over the %d limit" % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character in entry.txt.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
