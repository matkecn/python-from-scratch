"""Sqlite-cursors.

SQLite keeps your data in one file and understands real SQL.

Run me:
    python 624-sqlite-cursors/lesson_624_sqlite_cursors.py
"""

from __future__ import annotations


import sqlite3


def create_table(db: sqlite3.Connection) -> None:
    """Make the notes table if it is not there yet.

    Args:
        db: An open connection.
    """
    with db:
        db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")


def add_note(db: sqlite3.Connection, text: str) -> int:
    """Save one note and return its row id.

    Args:
        db: An open connection.
        text: The note to save.

    Returns:
        The new note's id.
    """
    with db:
        cursor = db.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        return int(cursor.lastrowid or 0)


def all_notes(db: sqlite3.Connection) -> list[str]:
    """Return every saved note, oldest first.

    Args:
        db: An open connection.

    Returns:
        The note texts.
    """
    rows = db.execute("SELECT text FROM notes ORDER BY id").fetchall()
    return [row[0] for row in rows]


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    import sqlite3

    db = sqlite3.connect(":memory:")
    create_table(db)
    add_note(db, "milk")
    print(all_notes(db))


if __name__ == "__main__":
    main()
