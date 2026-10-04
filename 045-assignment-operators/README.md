# 045 · Assignment operators

Placeholder for **Assignment operators**. A later phase replaces this with a full lesson.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 045-assignment-operators/lesson_045_assignment_operators.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_045_assignment_operators.py</code></summary>

```python
"""Assignment operators.

Placeholder for **Assignment operators**. A later phase replaces this with a full lesson.

Run me:
    python 045-assignment-operators/lesson_045_assignment_operators.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"assignment operators"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Assignment operators" for step in (1, 2, 3))


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
pytest 045-assignment-operators
```

## 4. Open the notebook

```bash
jupyter notebook 045-assignment-operators/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 044-bitwise-operators](../044-bitwise-operators/) · [Next: 046-membership-operators →](../046-membership-operators/)
