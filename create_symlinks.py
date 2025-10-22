"""Generate organized symlink structure for Dendron notes.

This script scans the current working directory for Markdown files
representing Dendron notes and creates a mirrored hierarchy inside an
``organized`` directory using symbolic links. It is designed to run from
within the notes directory and is safe to execute multiple times.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

SINGLE_WORD_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def is_single_word(stem: str) -> bool:
    """Return True if the stem is a single word (alphanumeric only)."""
    return all(ch in SINGLE_WORD_CHARS for ch in stem)


def destination_for(note: Path, organized_dir: Path) -> Optional[Path]:
    """Determine the destination path for a note inside organized_dir.

    Returns None if the note should be skipped.
    """
    if note.name == "root.md":
        return None

    stem = note.stem
    if not stem:
        return None

    if "." not in stem:
        if is_single_word(stem):
            return organized_dir / f"{stem}.md"
        return organized_dir / stem / "index.md"

    parts = stem.split(".")
    return organized_dir.joinpath(*parts) / "index.md"


def ensure_gitignore(organized_dir: Path) -> None:
    """Create a .gitignore that keeps symlinks out of version control."""
    organized_dir.mkdir(exist_ok=True)
    gitignore = organized_dir / ".gitignore"
    contents = "*\n!.gitignore\n"
    if not gitignore.exists() or gitignore.read_text() != contents:
        gitignore.write_text(contents)


def create_symlink(source: Path, destination: Path) -> None:
    """Create or update a symbolic link at destination pointing to source."""
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists() or destination.is_symlink():
        # Remove existing file or symlink to keep operation idempotent.
        destination.unlink()

    source_resolved = source.resolve()
    dest_parent_resolved = destination.parent.resolve()
    relative_target = os.path.relpath(source_resolved, dest_parent_resolved)
    destination.symlink_to(relative_target)


def main() -> None:
    notes_dir = Path.cwd()
    organized_dir = notes_dir / "organized"

    ensure_gitignore(organized_dir)

    for note in sorted(notes_dir.glob("*.md")):
        if note.name.endswith(".schema.yml"):
            continue

        destination = destination_for(note, organized_dir)
        if destination is None:
            continue

        create_symlink(note, destination)


if __name__ == "__main__":
    main()
