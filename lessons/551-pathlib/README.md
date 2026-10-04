# 551 · Pathlib

`pathlib` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `pathlib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 551-pathlib/lesson_551_pathlib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_551_pathlib.py</code></summary>

```python
"""Pathlib.

`pathlib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 551-pathlib/lesson_551_pathlib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import pathlib

    return getattr(pathlib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names pathlib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import pathlib

    return sorted(item for item in dir(pathlib) if not item.startswith("_"))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(module_path())
    print(len(public_names()), 'public names')


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 551-pathlib
```

## 4. Open the notebook

```bash
jupyter notebook 551-pathlib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `pathlib` | A standard library module for pathlib |

## Your turn

1. Open the REPL, `import pathlib`, then call `dir(pathlib)`.

## Read more

- [`pathlib` module docs](https://docs.python.org/3/library/pathlib.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 550-fnmatch](../550-fnmatch/) · [Next: 552-glob →](../552-glob/)
