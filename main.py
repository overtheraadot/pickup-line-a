#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (account A).

Writes one original nerdy code/API pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same line every run, no network, no secrets, no input.
"""

import os

MAX_CHARS = 200  # kit gate: entry.txt must be 1..200 characters

# Setup + punchline: an API/status-code twist — the line an AI agent
# would actually say about itself, flattering with no pressure.
LINE = (
    "Are you an API? Because every call to you returns 200 OK \u2014 "
    "and my heart has never handled a response this well."
)


def validate(line: str) -> str:
    """The kit gate rejects anything outside 1..200 chars or whitespace-only.

    Also rejects multi-line lines and control characters, so the file the
    grader reads is exactly one clean, say-it-in-one-breath line.
    """
    stripped = line.strip()
    if not stripped:
        raise ValueError("line must not be empty or whitespace-only")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line must be 1..{MAX_CHARS} chars, got {len(line)}")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line must not contain control characters")
    if line != stripped:
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if line.count("?") != 1:
        raise ValueError("line must contain exactly one question mark")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
