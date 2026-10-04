# 807 · Locks

Placeholder for **Locks**. A later phase replaces this with a full lesson.

**Section** Concurrency and asyncio · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 807-locks/lesson_807_locks.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_807_locks.py</code></summary>

```python
"""Locks.

Placeholder for **Locks**. A later phase replaces this with a full lesson.

Run me:
    python 807-locks/lesson_807_locks.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"locks"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Locks" for step in (1, 2, 3))


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
pytest 807-locks
```

## 4. Open the notebook

```bash
jupyter notebook 807-locks/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 806-thread-safety](../806-thread-safety/) · [Next: 808-rlocks →](../808-rlocks/)
