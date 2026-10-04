# 564 · Base64

`base64` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `base64` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 564-base64/lesson_564_base64.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_564_base64.py</code></summary>

```python
"""Base64.

`base64` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 564-base64/lesson_564_base64.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import base64

    return getattr(base64, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names base64 offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import base64

    return sorted(item for item in dir(base64) if not item.startswith("_"))


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
pytest 564-base64
```

## 4. Open the notebook

```bash
jupyter notebook 564-base64/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `base64` | A standard library module for base64 |

## Your turn

1. Open the REPL, `import base64`, then call `dir(base64)`.

## Read more

- [`base64` module docs](https://docs.python.org/3/library/base64.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 563-uuid](../563-uuid/) · [Next: 565-binhex →](../565-binhex/)
