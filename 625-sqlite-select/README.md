# 625 · Sqlite-select

SQLite keeps your data in one file and understands real SQL.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `sqlite3.connect` opens a database file
- Use `?` to keep SQL safe
- `with` commits or rolls back

## 1. Run the example

```bash
python 625-sqlite-select/lesson_625_sqlite_select.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_625_sqlite_select.py</code></summary>

```python
"""Sqlite-select.

SQLite keeps your data in one file and understands real SQL.

Run me:
    python 625-sqlite-select/lesson_625_sqlite_select.py
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
```

</details>

## 3. Run the tests

```bash
pytest 625-sqlite-select
```

## 4. Open the notebook

```bash
jupyter notebook 625-sqlite-select/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `SQL` | The language databases understand |
| `transaction` | A group of changes that all succeed or all fail |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 624-sqlite-cursors](../624-sqlite-cursors/) · [Next: 626-sqlite-insert →](../626-sqlite-insert/)
