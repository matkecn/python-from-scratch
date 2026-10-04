# 220 · Abstraction

Placeholder for **Abstraction**. A later phase replaces this with a full lesson.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 220-abstraction/lesson_220_abstraction.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_220_abstraction.py</code></summary>

```python
"""Abstraction.

Placeholder for **Abstraction**. A later phase replaces this with a full lesson.

Run me:
    python 220-abstraction/lesson_220_abstraction.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"abstraction"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Abstraction" for step in (1, 2, 3))


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
pytest 220-abstraction
```

## 4. Open the notebook

```bash
jupyter notebook 220-abstraction/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 219-polymorphism](../219-polymorphism/) · [Next: 221-abc →](../221-abc/)
