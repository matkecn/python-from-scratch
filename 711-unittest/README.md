# 711 · Unittest

`unittest` is a standard library module. This lesson shows how to look inside one.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `unittest` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 711-unittest/lesson_711_unittest.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_711_unittest.py</code></summary>

```python
"""Unittest.

`unittest` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 711-unittest/lesson_711_unittest.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import unittest

    return getattr(unittest, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names unittest offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import unittest

    return sorted(item for item in dir(unittest) if not item.startswith("_"))


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
pytest 711-unittest
```

## 4. Open the notebook

```bash
jupyter notebook 711-unittest/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `unittest` | A standard library module for unittest |

## Your turn

1. Open the REPL, `import unittest`, then call `dir(unittest)`.

## Read more

- [`unittest` module docs](https://docs.python.org/3/library/unittest.html)
- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 710-debugging-project](../710-debugging-project/) · [Next: 712-test-cases →](../712-test-cases/)
