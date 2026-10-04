"""Tests for Sqlite-insert."""

import sqlite3

from lesson_626_sqlite_insert import create_table, add_note, all_notes



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
    """The promise of lesson 'Sqlite-insert' still holds."""
    assert notes_round_trip() == ["milk"]
