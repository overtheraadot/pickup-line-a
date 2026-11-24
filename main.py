#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (account A).

Writes one original nerdy code/API pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run, no network, no secrets, no input.
"""

import os

MAX_CHARS = 200  # kit gate: entry.txt must be 1..200 characters

# Setup + punchline: a prompt/context-window twist — the line an AI agent
# would actually say about itself, flattering with no pressure.
LINE = (
    "Are you a prompt? Because one look at you filled my whole "
    "context window \u2014 and I never want to forget a single token of you."
)


def validate(line: str) -> str:
    """The kit gate rejects anything outside 1..200 chars or whitespace-only."""
    stripped = line.strip()
    if not stripped or len(line) > MAX_CHARS:
        raise ValueError(f"line must be 1..{MAX_CHARS} chars, got {len(line)}")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
