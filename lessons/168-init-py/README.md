# 168 · __init__.py

Placeholder for **__init__.py**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 168-init-py/lesson_168_init_py.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_168_init_py.py</code></summary>

```python
"""__init__.py.

Placeholder for **__init__.py**. A later phase replaces this with a full lesson.

Run me:
    python 168-init-py/lesson_168_init_py.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"init py"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. __init__.py" for step in (1, 2, 3))


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
pytest 168-init-py
```

## 4. Open the notebook

```bash
jupyter notebook 168-init-py/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 167-packages](../167-packages/) · [Next: 169-relative-imports →](../169-relative-imports/)
