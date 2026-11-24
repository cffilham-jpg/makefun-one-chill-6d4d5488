"""One Line, One Chill — writes a single horror sentence to /output/entry.txt."""

import os
import unicodedata

LINE = "The voice on the baby monitor isn't singing to my son \u2014 it's teaching him my voice, one word a night."


def validate(line):
    """Return True only if the line is a valid single-sentence entry."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 200:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    if any(unicodedata.category(ch) == "Cc" for ch in line):
        return False
    return True


def main():
    if not validate(LINE):
        raise SystemExit("invalid line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
