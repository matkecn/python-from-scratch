# 567 · Zlib

`zlib` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `zlib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 567-zlib/lesson_567_zlib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_567_zlib.py</code></summary>

```python
"""Zlib.

`zlib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 567-zlib/lesson_567_zlib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import zlib

    return getattr(zlib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names zlib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import zlib

    return sorted(item for item in dir(zlib) if not item.startswith("_"))


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
pytest 567-zlib
```

## 4. Open the notebook

```bash
jupyter notebook 567-zlib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `zlib` | A standard library module for zlib |

## Your turn

1. Open the REPL, `import zlib`, then call `dir(zlib)`.

## Read more

- [`zlib` module docs](https://docs.python.org/3/library/zlib.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 566-binascii](../566-binascii/) · [Next: 568-gzip →](../568-gzip/)
