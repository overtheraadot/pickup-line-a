#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (account A).

Writes one original nerdy code/API pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run, no network, no secrets, no input.
"""

import os

LINE = (
    "Are you an API? Because every time I call you, my heart returns "
    "200 OK \u2014 and I'd love to keep this connection open."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
