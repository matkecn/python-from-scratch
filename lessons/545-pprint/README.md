# 545 · Pprint

`pprint` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `pprint` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 545-pprint/lesson_545_pprint.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_545_pprint.py</code></summary>

```python
"""Pprint.

`pprint` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 545-pprint/lesson_545_pprint.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import pprint

    return getattr(pprint, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names pprint offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import pprint

    return sorted(item for item in dir(pprint) if not item.startswith("_"))


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
pytest 545-pprint
```

## 4. Open the notebook

```bash
jupyter notebook 545-pprint/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `pprint` | A standard library module for pprint |

## Your turn

1. Open the REPL, `import pprint`, then call `dir(pprint)`.

## Read more

- [`pprint` module docs](https://docs.python.org/3/library/pprint.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 544-copy](../544-copy/) · [Next: 546-textwrap →](../546-textwrap/)
