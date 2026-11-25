"""Meeting That Should Have Been One Line — entry program.

Writes exactly one line to <OUTPUT_DIR>/entry.txt.
"""

import os

LINE = "This meeting could have been an email, and the email could have been a shrug."


def write_entry(output_dir: str) -> str:
    """Write the line to <output_dir>/entry.txt; return the path written."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return path


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
