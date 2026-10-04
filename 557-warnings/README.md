# 557 · Warnings

`warnings` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `warnings` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 557-warnings/lesson_557_warnings.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_557_warnings.py</code></summary>

```python
"""Warnings.

`warnings` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 557-warnings/lesson_557_warnings.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import warnings

    return getattr(warnings, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names warnings offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import warnings

    return sorted(item for item in dir(warnings) if not item.startswith("_"))


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
pytest 557-warnings
```

## 4. Open the notebook

```bash
jupyter notebook 557-warnings/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `warnings` | A standard library module for warnings |

## Your turn

1. Open the REPL, `import warnings`, then call `dir(warnings)`.

## Read more

- [`warnings` module docs](https://docs.python.org/3/library/warnings.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 556-logging](../556-logging/) · [Next: 558-traceback →](../558-traceback/)
