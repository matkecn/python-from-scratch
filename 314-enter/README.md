# 314 · Enter

Placeholder for **Enter**. A later phase replaces this with a full lesson.

**Section** Decorators, context managers, descriptors and introspection · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 314-enter/lesson_314_enter.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_314_enter.py</code></summary>

```python
"""Enter.

Placeholder for **Enter**. A later phase replaces this with a full lesson.

Run me:
    python 314-enter/lesson_314_enter.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"enter"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Enter" for step in (1, 2, 3))


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
pytest 314-enter
```

## 4. Open the notebook

```bash
jupyter notebook 314-enter/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 313-contextmanager](../313-contextmanager/) · [Next: 315-exit →](../315-exit/)
