"""Tests for Sqlite-cursors."""

import sqlite3

from lesson_624_sqlite_cursors import create_table, add_note, all_notes



def notes_round_trip() -> list[str]:
    """Save one note in a memory database and read it back.

    Returns:
        The notes that were found.
    """
    db = sqlite3.connect(":memory:")
    create_table(db)
    add_note(db, "milk")
    return all_notes(db)


def test_saves_and_reads() -> None:
    """The promise of lesson 'Sqlite-cursors' still holds."""
    assert notes_round_trip() == ["milk"]
