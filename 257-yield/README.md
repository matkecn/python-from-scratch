# 257 · Yield

Placeholder for **Yield**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 257-yield/lesson_257_yield.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_257_yield.py</code></summary>

```python
"""Yield.

Placeholder for **Yield**. A later phase replaces this with a full lesson.

Run me:
    python 257-yield/lesson_257_yield.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"yield"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Yield" for step in (1, 2, 3))


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
pytest 257-yield
```

## 4. Open the notebook

```bash
jupyter notebook 257-yield/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 256-generators](../256-generators/) · [Next: 258-yield-from →](../258-yield-from/)
