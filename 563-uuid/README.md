# 563 · Uuid

`uuid` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `uuid` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 563-uuid/lesson_563_uuid.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_563_uuid.py</code></summary>

```python
"""Uuid.

`uuid` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 563-uuid/lesson_563_uuid.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import uuid

    return getattr(uuid, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names uuid offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import uuid

    return sorted(item for item in dir(uuid) if not item.startswith("_"))


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
pytest 563-uuid
```

## 4. Open the notebook

```bash
jupyter notebook 563-uuid/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `uuid` | A standard library module for uuid |

## Your turn

1. Open the REPL, `import uuid`, then call `dir(uuid)`.

## Read more

- [`uuid` module docs](https://docs.python.org/3/library/uuid.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 562-hmac](../562-hmac/) · [Next: 564-base64 →](../564-base64/)
