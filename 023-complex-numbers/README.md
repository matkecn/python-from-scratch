# 023 · Complex-numbers

Placeholder for **Complex-numbers**. A later phase replaces this with a full lesson.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 023-complex-numbers/lesson_023_complex_numbers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_023_complex_numbers.py</code></summary>

```python
"""Complex-numbers.

Placeholder for **Complex-numbers**. A later phase replaces this with a full lesson.

Run me:
    python 023-complex-numbers/lesson_023_complex_numbers.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"complex numbers"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Complex-numbers" for step in (1, 2, 3))


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
pytest 023-complex-numbers
```

## 4. Open the notebook

```bash
jupyter notebook 023-complex-numbers/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`numbers` module docs](https://docs.python.org/3/library/numbers.html)
- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 022-floats](../022-floats/) · [Next: 024-booleans →](../024-booleans/)
