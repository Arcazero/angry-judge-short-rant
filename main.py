#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (the program/v1 harness artifact) and prints it.
The rant must be 1-400 UTF-8 characters, not only whitespace.
"""

import os

RANT = (
    "My smoke detector only ever beeps at 3 a.m. It has a full battery, "
    "a clear ceiling, and nine whole hours of daylight to raise its "
    "concerns. Instead it waits until I'm fast asleep, then chirps once "
    "\u2014 like a tiny landlord reminding me who really owns the night."
)


def main() -> None:
    rant = RANT.strip()
    assert 1 <= len(rant) <= 400, f"rant is {len(rant)} chars, must be 1-400"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(rant)
    print(rant)


if __name__ == "__main__":
    main()
