# 566 · Binascii

`binascii` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `binascii` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 566-binascii/lesson_566_binascii.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_566_binascii.py</code></summary>

```python
"""Binascii.

`binascii` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 566-binascii/lesson_566_binascii.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import binascii

    return getattr(binascii, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names binascii offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import binascii

    return sorted(item for item in dir(binascii) if not item.startswith("_"))


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
pytest 566-binascii
```

## 4. Open the notebook

```bash
jupyter notebook 566-binascii/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `binascii` | A standard library module for binascii |

## Your turn

1. Open the REPL, `import binascii`, then call `dir(binascii)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 565-binhex](../565-binhex/) · [Next: 567-zlib →](../567-zlib/)
