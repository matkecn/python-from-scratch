# 292 · Enum

`enum` is a standard library module. This lesson shows how to look inside one.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `enum` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 292-enum/lesson_292_enum.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_292_enum.py</code></summary>

```python
"""Enum.

`enum` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 292-enum/lesson_292_enum.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import enum

    return getattr(enum, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names enum offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import enum

    return sorted(item for item in dir(enum) if not item.startswith("_"))


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
pytest 292-enum
```

## 4. Open the notebook

```bash
jupyter notebook 292-enum/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `enum` | A standard library module for enum |

## Your turn

1. Open the REPL, `import enum`, then call `dir(enum)`.

## Read more

- [`enum` module docs](https://docs.python.org/3/library/enum.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 291-enumeration](../291-enumeration/) · [Next: 293-intenum →](../293-intenum/)
