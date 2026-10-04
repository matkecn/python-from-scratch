# 561 · Hashlib

`hashlib` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `hashlib` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 561-hashlib/lesson_561_hashlib.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_561_hashlib.py</code></summary>

```python
"""Hashlib.

`hashlib` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 561-hashlib/lesson_561_hashlib.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import hashlib

    return getattr(hashlib, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names hashlib offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import hashlib

    return sorted(item for item in dir(hashlib) if not item.startswith("_"))


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
pytest 561-hashlib
```

## 4. Open the notebook

```bash
jupyter notebook 561-hashlib/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `hashlib` | A standard library module for hashlib |

## Your turn

1. Open the REPL, `import hashlib`, then call `dir(hashlib)`.

## Read more

- [`hashlib` module docs](https://docs.python.org/3/library/hashlib.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 560-codecs](../560-codecs/) · [Next: 562-hmac →](../562-hmac/)
