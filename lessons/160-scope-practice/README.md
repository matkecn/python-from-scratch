# 160 · Scope-practice

Placeholder for **Scope-practice**. A later phase replaces this with a full lesson.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 160-scope-practice/lesson_160_scope_practice.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_160_scope_practice.py</code></summary>

```python
"""Scope-practice.

Placeholder for **Scope-practice**. A later phase replaces this with a full lesson.

Run me:
    python 160-scope-practice/lesson_160_scope_practice.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"scope practice"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Scope-practice" for step in (1, 2, 3))


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
pytest 160-scope-practice
```

## 4. Open the notebook

```bash
jupyter notebook 160-scope-practice/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 159-unbound-local](../159-unbound-local/) · [Next: 161-modules →](../161-modules/)
