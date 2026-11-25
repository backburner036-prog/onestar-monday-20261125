"""One-star review of Monday, written as if Monday were a restaurant.

The entry is a single review line written verbatim to the output file.
It reads like a genuine one-star restaurant review, with the Monday
jokes (cold coffee, reheated leftovers, the meeting that could have
been an email) and a short final twist: Monday owns the calendar.
Short enough to screenshot into the group chat.
"""

from pathlib import Path

LINE = "One star. Monday served cold coffee, reheated leftovers, and a meeting that could have been an email. It owns my calendar."

ENTRY_PATH = Path("/output/entry.txt")


def ensure_parent(path: Path) -> None:
    """Create the output directory if it does not exist yet."""
    path.parent.mkdir(parents=True, exist_ok=True)


def write_entry(path: Path, text: str) -> None:
    """Write the entry line to *path* exactly as given."""
    ensure_parent(path)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    write_entry(ENTRY_PATH, LINE)


if __name__ == "__main__":
    main()
