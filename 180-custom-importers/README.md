# 180 · Custom-importers

Placeholder for **Custom-importers**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 180-custom-importers/lesson_180_custom_importers.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_180_custom_importers.py</code></summary>

```python
"""Custom-importers.

Placeholder for **Custom-importers**. A later phase replaces this with a full lesson.

Run me:
    python 180-custom-importers/lesson_180_custom_importers.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"custom importers"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Custom-importers" for step in (1, 2, 3))


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
pytest 180-custom-importers
```

## 4. Open the notebook

```bash
jupyter notebook 180-custom-importers/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 179-import-hooks](../179-import-hooks/) · [Next: 181-exceptions →](../181-exceptions/)
