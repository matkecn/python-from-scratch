# 503 · Sys

`sys` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `sys` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 503-sys/lesson_503_sys.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_503_sys.py</code></summary>

```python
"""Sys.

`sys` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 503-sys/lesson_503_sys.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import sys

    return getattr(sys, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names sys offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import sys

    return sorted(item for item in dir(sys) if not item.startswith("_"))


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
pytest 503-sys
```

## 4. Open the notebook

```bash
jupyter notebook 503-sys/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `sys` | A standard library module for sys |

## Your turn

1. Open the REPL, `import sys`, then call `dir(sys)`.

## Read more

- [`sys` module docs](https://docs.python.org/3/library/sys.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 502-os-path](../502-os-path/) · [Next: 504-platform →](../504-platform/)
