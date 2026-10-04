# 155 · Enclosing-scope

Placeholder for **Enclosing-scope**. A later phase replaces this with a full lesson.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 155-enclosing-scope/lesson_155_enclosing_scope.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_155_enclosing_scope.py</code></summary>

```python
"""Enclosing-scope.

Placeholder for **Enclosing-scope**. A later phase replaces this with a full lesson.

Run me:
    python 155-enclosing-scope/lesson_155_enclosing_scope.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"enclosing scope"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Enclosing-scope" for step in (1, 2, 3))


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
pytest 155-enclosing-scope
```

## 4. Open the notebook

```bash
jupyter notebook 155-enclosing-scope/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 154-local-scope](../154-local-scope/) · [Next: 156-builtins-scope →](../156-builtins-scope/)
