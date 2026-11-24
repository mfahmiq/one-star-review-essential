"""Write a deadpan one-star review of an everyday essential to /output/entry.txt.

The review: gravity, filed as a formal complaint. Gravity has held
everything down for billions of years and still will not let the reviewer
reach the top shelf. Deadpan, one joke, the sting in the last few words.

Stdlib only, no network, deterministic: the same bytes on every run.
The entry must be 1-160 characters, one single line.
"""

import os

LINE = (
    "One star. Gravity has held everything down for billions of years "
    "and still will not let me reach the top shelf."
)

assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
