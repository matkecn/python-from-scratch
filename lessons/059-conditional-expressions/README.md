# 059 · Conditional-expressions

Placeholder for **Conditional-expressions**. A later phase replaces this with a full lesson.

**Section** Conditionals and loops · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 059-conditional-expressions/lesson_059_conditional_expressions.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_059_conditional_expressions.py</code></summary>

```python
"""Conditional-expressions.

Placeholder for **Conditional-expressions**. A later phase replaces this with a full lesson.

Run me:
    python 059-conditional-expressions/lesson_059_conditional_expressions.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"conditional expressions"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Conditional-expressions" for step in (1, 2, 3))


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
pytest 059-conditional-expressions
```

## 4. Open the notebook

```bash
jupyter notebook 059-conditional-expressions/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/controlflow.html)

---

[← 058-guards](../058-guards/) · [Next: 060-control-flow →](../060-control-flow/)
