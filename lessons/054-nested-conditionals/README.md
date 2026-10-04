# 054 · Nested-conditionals

Placeholder for **Nested-conditionals**. A later phase replaces this with a full lesson.

**Section** Conditionals and loops · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 054-nested-conditionals/lesson_054_nested_conditionals.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_054_nested_conditionals.py</code></summary>

```python
"""Nested-conditionals.

Placeholder for **Nested-conditionals**. A later phase replaces this with a full lesson.

Run me:
    python 054-nested-conditionals/lesson_054_nested_conditionals.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"nested conditionals"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Nested-conditionals" for step in (1, 2, 3))


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
pytest 054-nested-conditionals
```

## 4. Open the notebook

```bash
jupyter notebook 054-nested-conditionals/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/controlflow.html)

---

[← 053-else](../053-else/) · [Next: 055-match →](../055-match/)
