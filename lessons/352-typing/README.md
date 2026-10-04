# 352 · Typing

`typing` is a standard library module. This lesson shows how to look inside one.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `typing` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 352-typing/lesson_352_typing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_352_typing.py</code></summary>

```python
"""Typing.

`typing` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 352-typing/lesson_352_typing.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import typing

    return getattr(typing, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names typing offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import typing

    return sorted(item for item in dir(typing) if not item.startswith("_"))


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
pytest 352-typing
```

## 4. Open the notebook

```bash
jupyter notebook 352-typing/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `typing` | A standard library module for typing |

## Your turn

1. Open the REPL, `import typing`, then call `dir(typing)`.

## Read more

- [`typing` module docs](https://docs.python.org/3/library/typing.html)
- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 351-type-hints](../351-type-hints/) · [Next: 353-type-annotations →](../353-type-annotations/)
