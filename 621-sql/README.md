# 621 · SQL

Placeholder for **SQL**. A later phase replaces this with a full lesson.

**Section** Networking, APIs and databases · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 621-sql/lesson_621_sql.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_621_sql.py</code></summary>

```python
"""SQL.

Placeholder for **SQL**. A later phase replaces this with a full lesson.

Run me:
    python 621-sql/lesson_621_sql.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"sql"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. SQL" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 621-sql
```

## 4. Open the notebook

```bash
jupyter notebook 621-sql/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 620-api-project](../620-api-project/) · [Next: 622-sqlite →](../622-sqlite/)
