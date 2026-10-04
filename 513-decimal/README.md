# 513 · Decimal

`decimal` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `decimal` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 513-decimal/lesson_513_decimal.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_513_decimal.py</code></summary>

```python
"""Decimal.

`decimal` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 513-decimal/lesson_513_decimal.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import decimal

    return getattr(decimal, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names decimal offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import decimal

    return sorted(item for item in dir(decimal) if not item.startswith("_"))


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
pytest 513-decimal
```

## 4. Open the notebook

```bash
jupyter notebook 513-decimal/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `decimal` | A standard library module for decimal |

## Your turn

1. Open the REPL, `import decimal`, then call `dir(decimal)`.

## Read more

- [`decimal` module docs](https://docs.python.org/3/library/decimal.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 512-cmath](../512-cmath/) · [Next: 514-fractions →](../514-fractions/)
