# 374 · Type-narrowing

Placeholder for **Type-narrowing**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 374-type-narrowing/lesson_374_type_narrowing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_374_type_narrowing.py</code></summary>

```python
"""Type-narrowing.

Placeholder for **Type-narrowing**. A later phase replaces this with a full lesson.

Run me:
    python 374-type-narrowing/lesson_374_type_narrowing.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"type narrowing"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Type-narrowing" for step in (1, 2, 3))


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
pytest 374-type-narrowing
```

## 4. Open the notebook

```bash
jupyter notebook 374-type-narrowing/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 373-pyright](../373-pyright/) · [Next: 375-type-guards →](../375-type-guards/)
