# 562 · Hmac

`hmac` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `hmac` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 562-hmac/lesson_562_hmac.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_562_hmac.py</code></summary>

```python
"""Hmac.

`hmac` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 562-hmac/lesson_562_hmac.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import hmac

    return getattr(hmac, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names hmac offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import hmac

    return sorted(item for item in dir(hmac) if not item.startswith("_"))


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
pytest 562-hmac
```

## 4. Open the notebook

```bash
jupyter notebook 562-hmac/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `hmac` | A standard library module for hmac |

## Your turn

1. Open the REPL, `import hmac`, then call `dir(hmac)`.

## Read more

- [`hmac` module docs](https://docs.python.org/3/library/hmac.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 561-hashlib](../561-hashlib/) · [Next: 563-uuid →](../563-uuid/)
