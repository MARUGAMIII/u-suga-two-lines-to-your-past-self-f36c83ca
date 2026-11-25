#!/usr/bin/env python3
"""Two Lines to Your Past Self entry.

Writes exactly two lines to /output/entry.txt: a warning to my past
self about one specific moment, and one sentence on why it mattered
and what changed because of it.

Line one names a real moment -- a sentence said out loud, on a
platform, on a dated day. Line two traces the cause and effect:
he took the words at face value, he left that winter, and the
children who came after have never met him except as a voice on
the phone at Christmas.
"""

import os

LINE_ONE = "Don't say 'I don't need you' to your brother on the platform at King's Cross on 4 August 2015."
LINE_TWO = "He took you at your word, flew to Australia that winter, and your children have never met him except as a voice on Christmas calls."

ENTRY = LINE_ONE + "\n" + LINE_TWO + "\n"


def _check_gate(entry: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 280
    characters, not only whitespace. The task requires exactly two
    lines, one sentence each, plain ASCII.
    """
    assert entry.strip(), "entry must not be only whitespace"
    assert entry.isascii(), "entry must be plain ASCII"
    assert 1 <= len(entry) <= 280, "entry must be 1 to 280 characters"
    lines = entry.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "neither line may be empty"
    # One sentence per line: each line ends with a single full stop.
    assert all(line.strip().endswith(".") for line in lines), \
        "each line must be a single sentence ending in a full stop"
    assert all(line.count(".") == 1 for line in lines), \
        "each line must contain exactly one sentence"


def main() -> None:
    _check_gate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
