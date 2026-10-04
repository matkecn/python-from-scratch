# 627 · Sqlite-update

SQLite keeps your data in one file and understands real SQL.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- `sqlite3.connect` opens a database file
- Use `?` to keep SQL safe
- `with` commits or rolls back

## 1. Run the example

```bash
python 627-sqlite-update/lesson_627_sqlite_update.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_627_sqlite_update.py</code></summary>

```python
"""Sqlite-update.

SQLite keeps your data in one file and understands real SQL.

Run me:
    python 627-sqlite-update/lesson_627_sqlite_update.py
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
pytest 627-sqlite-update
```

## 4. Open the notebook

```bash
jupyter notebook 627-sqlite-update/lesson.ipynb
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

[← 626-sqlite-insert](../626-sqlite-insert/) · [Next: 628-sqlite-delete →](../628-sqlite-delete/)
