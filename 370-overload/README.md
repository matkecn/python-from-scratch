# 370 · Overload

Placeholder for **Overload**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 370-overload/lesson_370_overload.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_370_overload.py</code></summary>

```python
"""Overload.

Placeholder for **Overload**. A later phase replaces this with a full lesson.

Run me:
    python 370-overload/lesson_370_overload.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"overload"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Overload" for step in (1, 2, 3))


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
pytest 370-overload
```

## 4. Open the notebook

```bash
jupyter notebook 370-overload/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 369-runtime-checkable](../369-runtime-checkable/) · [Next: 371-type-checkers →](../371-type-checkers/)
