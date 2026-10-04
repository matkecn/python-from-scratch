# 371 · Type-checkers

Placeholder for **Type-checkers**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 371-type-checkers/lesson_371_type_checkers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_371_type_checkers.py</code></summary>

```python
"""Type-checkers.

Placeholder for **Type-checkers**. A later phase replaces this with a full lesson.

Run me:
    python 371-type-checkers/lesson_371_type_checkers.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"type checkers"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Type-checkers" for step in (1, 2, 3))


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
pytest 371-type-checkers
```

## 4. Open the notebook

```bash
jupyter notebook 371-type-checkers/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 370-overload](../370-overload/) · [Next: 372-mypy →](../372-mypy/)
