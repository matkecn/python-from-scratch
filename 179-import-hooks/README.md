# 179 · Import-hooks

Placeholder for **Import-hooks**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 179-import-hooks/lesson_179_import_hooks.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_179_import_hooks.py</code></summary>

```python
"""Import-hooks.

Placeholder for **Import-hooks**. A later phase replaces this with a full lesson.

Run me:
    python 179-import-hooks/lesson_179_import_hooks.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"import hooks"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Import-hooks" for step in (1, 2, 3))


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
pytest 179-import-hooks
```

## 4. Open the notebook

```bash
jupyter notebook 179-import-hooks/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 178-module-cache](../178-module-cache/) · [Next: 180-custom-importers →](../180-custom-importers/)
