# 505 · Shutil

`shutil` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `shutil` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 505-shutil/lesson_505_shutil.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_505_shutil.py</code></summary>

```python
"""Shutil.

`shutil` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 505-shutil/lesson_505_shutil.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import shutil

    return getattr(shutil, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names shutil offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import shutil

    return sorted(item for item in dir(shutil) if not item.startswith("_"))


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
pytest 505-shutil
```

## 4. Open the notebook

```bash
jupyter notebook 505-shutil/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `shutil` | A standard library module for shutil |

## Your turn

1. Open the REPL, `import shutil`, then call `dir(shutil)`.

## Read more

- [`shutil` module docs](https://docs.python.org/3/library/shutil.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 504-platform](../504-platform/) · [Next: 506-subprocess →](../506-subprocess/)
