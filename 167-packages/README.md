# 167 · Packages

Placeholder for **Packages**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 167-packages/lesson_167_packages.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_167_packages.py</code></summary>

```python
"""Packages.

Placeholder for **Packages**. A later phase replaces this with a full lesson.

Run me:
    python 167-packages/lesson_167_packages.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"packages"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Packages" for step in (1, 2, 3))


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
pytest 167-packages
```

## 4. Open the notebook

```bash
jupyter notebook 167-packages/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 166-sys-path](../166-sys-path/) · [Next: 168-init-py →](../168-init-py/)
