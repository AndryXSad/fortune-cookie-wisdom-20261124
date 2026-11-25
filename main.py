"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a single short balanced sentence, true about a developer's
day, with a turn the reader has not heard before and a quiet double
meaning on a second read — the throwaway name "temp" promises
impermanence, yet the function outlives the people around it.
"""

import os

ENTRY = "The function you named 'temp' has already outlived three of your managers."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
