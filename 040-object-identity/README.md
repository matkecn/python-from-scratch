# 040 · Object-identity

Placeholder for **Object-identity**. A later phase replaces this with a full lesson.

**Section** Data types and conversions · **Level** 1 of 5 · **Time** about 10 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 040-object-identity/lesson_040_object_identity.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_040_object_identity.py</code></summary>

```python
"""Object-identity.

Placeholder for **Object-identity**. A later phase replaces this with a full lesson.

Run me:
    python 040-object-identity/lesson_040_object_identity.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"object identity"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Object-identity" for step in (1, 2, 3))


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
pytest 040-object-identity
```

## 4. Open the notebook

```bash
jupyter notebook 040-object-identity/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/introduction.html)

---

[← 039-equality](../039-equality/) · [Next: 041-arithmetic →](../041-arithmetic/)
