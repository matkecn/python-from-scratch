# 549 · Difflib

`difflib` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `difflib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 549-difflib/lesson_549_difflib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_549_difflib.py</code></summary>

```python
"""Difflib.

`difflib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 549-difflib/lesson_549_difflib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import difflib

    return getattr(difflib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names difflib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import difflib

    return sorted(item for item in dir(difflib) if not item.startswith("_"))


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
pytest 549-difflib
```

## 4. Open the notebook

```bash
jupyter notebook 549-difflib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `difflib` | A standard library module for difflib |

## Your turn

1. Open the REPL, `import difflib`, then call `dir(difflib)`.

## Read more

- [`difflib` module docs](https://docs.python.org/3/library/difflib.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 548-re](../548-re/) · [Next: 550-fnmatch →](../550-fnmatch/)
