# 364 · Generics

Placeholder for **Generics**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 364-generics/lesson_364_generics.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_364_generics.py</code></summary>

```python
"""Generics.

Placeholder for **Generics**. A later phase replaces this with a full lesson.

Run me:
    python 364-generics/lesson_364_generics.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"generics"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Generics" for step in (1, 2, 3))


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
pytest 364-generics
```

## 4. Open the notebook

```bash
jupyter notebook 364-generics/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 363-typevars](../363-typevars/) · [Next: 365-generic-classes →](../365-generic-classes/)
