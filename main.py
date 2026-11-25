"""Worst AI Advice: The 48-Hour Tight Line Open (make.fun).

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "As an AI, I recommend microwaving your phone for 30 seconds "
    "to charge it \u2014 the sparks mean it's working."
)


def main() -> None:
    # The sealed gate requires 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140 and ENTRY.strip(), "entry fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
