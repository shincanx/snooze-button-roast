#!/usr/bin/env python3
"""Write one roast of a 6 AM Saturday alarm to /output/entry.txt.

The roast: the alarm is not just loud, it is persistent — snoozing only
buys nine minutes before it returns, like a debt collector who hates
weekends too. Concrete detail (6 AM, Saturday, snooze), one twist, no cliche.

Deterministic: no input, no network, no randomness. The program writes a
single fixed line (under 200 characters) and prints it to stdout.
"""

from pathlib import Path

ENTRY = (
    "My alarm went off at 6 AM on a Saturday, so I hit snooze "
    "\u2014 then it came back like a debt collector who also hates weekends."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer does: one line of
    # 1-200 characters, not only whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
