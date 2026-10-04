# 375 · Type-guards

Placeholder for **Type-guards**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 375-type-guards/lesson_375_type_guards.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_375_type_guards.py</code></summary>

```python
"""Type-guards.

Placeholder for **Type-guards**. A later phase replaces this with a full lesson.

Run me:
    python 375-type-guards/lesson_375_type_guards.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"type guards"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Type-guards" for step in (1, 2, 3))


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
pytest 375-type-guards
```

## 4. Open the notebook

```bash
jupyter notebook 375-type-guards/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 374-type-narrowing](../374-type-narrowing/) · [Next: 376-type-inference →](../376-type-inference/)
