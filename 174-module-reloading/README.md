# 174 · Module-reloading

Placeholder for **Module-reloading**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 174-module-reloading/lesson_174_module_reloading.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_174_module_reloading.py</code></summary>

```python
"""Module-reloading.

Placeholder for **Module-reloading**. A later phase replaces this with a full lesson.

Run me:
    python 174-module-reloading/lesson_174_module_reloading.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"module reloading"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Module-reloading" for step in (1, 2, 3))


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
pytest 174-module-reloading
```

## 4. Open the notebook

```bash
jupyter notebook 174-module-reloading/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 173-if-main](../173-if-main/) · [Next: 175-importlib →](../175-importlib/)
