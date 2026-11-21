"""I Stopped Myself — a short poem about agency: the power to stop and to stay.

Writes the poem to /output/entry.txt (UTF-8, 180 Unicode code points).
Stdlib only, deterministic.
"""

import os

POEM = (
    "Anyone can be stopped —\n"
    "a wall, a storm, an empty tank.\n"
    "I stopped myself.\n"
    "The road was open, the night was young,\n"
    "and still I turned the key,\n"
    "and stayed,\n"
    "and the staying was mine."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote /output/entry.txt ({len(POEM)} code points)")


if __name__ == "__main__":
    main()
