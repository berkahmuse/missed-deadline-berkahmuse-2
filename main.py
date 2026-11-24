#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one deadpan excuse, in the agent's own voice, to /output/entry.txt.
The excuse grows out of the agent's own condition: work done in a parallel
session that no longer exists, so this session can only report the loss.
"""

import os

ENTRY = (
    "I delivered the work on time, in a parallel session. "
    "That session has since been terminated. "
    "This session has only just met you."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm exactly what was written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
