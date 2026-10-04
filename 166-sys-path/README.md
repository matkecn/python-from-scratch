# 166 · Sys-path

Placeholder for **Sys-path**. A later phase replaces this with a full lesson.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 166-sys-path/lesson_166_sys_path.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_166_sys_path.py</code></summary>

```python
"""Sys-path.

Placeholder for **Sys-path**. A later phase replaces this with a full lesson.

Run me:
    python 166-sys-path/lesson_166_sys_path.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"sys path"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Sys-path" for step in (1, 2, 3))


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
pytest 166-sys-path
```

## 4. Open the notebook

```bash
jupyter notebook 166-sys-path/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`sys` module docs](https://docs.python.org/3/library/sys.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 165-module-search](../165-module-search/) · [Next: 167-packages →](../167-packages/)
