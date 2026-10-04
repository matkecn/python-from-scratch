# 401 · Dunder-methods

Placeholder for **Dunder-methods**. A later phase replaces this with a full lesson.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 401-dunder-methods/lesson_401_dunder_methods.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_401_dunder_methods.py</code></summary>

```python
"""Dunder-methods.

Placeholder for **Dunder-methods**. A later phase replaces this with a full lesson.

Run me:
    python 401-dunder-methods/lesson_401_dunder_methods.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"dunder methods"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Dunder-methods" for step in (1, 2, 3))


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
pytest 401-dunder-methods
```

## 4. Open the notebook

```bash
jupyter notebook 401-dunder-methods/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 400-dataclass-project](../400-dataclass-project/) · [Next: 402-repr →](../402-repr/)
