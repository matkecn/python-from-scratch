# 041 · Arithmetic operators

Placeholder for **Arithmetic operators**. A later phase replaces this with a full lesson.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 041-arithmetic/lesson_041_arithmetic.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_041_arithmetic.py</code></summary>

```python
"""Arithmetic operators.

Placeholder for **Arithmetic operators**. A later phase replaces this with a full lesson.

Run me:
    python 041-arithmetic/lesson_041_arithmetic.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"arithmetic"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Arithmetic operators" for step in (1, 2, 3))


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
pytest 041-arithmetic
```

## 4. Open the notebook

```bash
jupyter notebook 041-arithmetic/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 040-object-identity](../040-object-identity/) · [Next: 042-comparison →](../042-comparison/)
