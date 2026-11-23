#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes the winning six-word story (variant C, blind self-judge 2-0) to the
output file. Pure standard library; no dependencies.

Output: $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when the
environment variable is not set.
"""

import os

STORY = "Grandfather's watch stopped. Time kept apologizing."


def main():
    words = STORY.split()
    assert len(words) == 6, "story must be exactly six words, got %d" % len(words)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    print("wrote %s (%d words)" % (out_path, len(words)))


if __name__ == "__main__":
    main()
