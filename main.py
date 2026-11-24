#!/usr/bin/env python3
"""Entry for u-po-pu-say-what-actually-broke-a2c153b5.

Writes one single-line software error message (at most 200 characters)
to /output/entry.txt. The line names the real failure in plain words,
says what to do next, and ends on a twist a reader repeats out loud.
"""

from pathlib import Path

ENTRY = "The payment failed because the card on file expired in 2019. Update it and try again \u2014 your cart is still here, judging you."

# The rules seal the entry at 1 to 200 characters, one line.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY


def main() -> None:
    out = Path("/output") / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
