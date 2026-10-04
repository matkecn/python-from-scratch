# 860 · Memory-project

Placeholder for **Memory-project**. A later phase replaces this with a full lesson.

**Section** Performance, memory and CPython internals · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 860-memory-project/lesson_860_memory_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_860_memory_project.py</code></summary>

```python
"""Memory-project.

Placeholder for **Memory-project**. A later phase replaces this with a full lesson.

Run me:
    python 860-memory-project/lesson_860_memory_project.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"memory project"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Memory-project" for step in (1, 2, 3))


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
pytest 860-memory-project
```

## 4. Open the notebook

```bash
jupyter notebook 860-memory-project/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 859-string-interning](../859-string-interning/) · [Next: 861-cpython →](../861-cpython/)
