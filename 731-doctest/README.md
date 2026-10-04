# 731 · Doctest

`doctest` is a standard library module. This lesson shows how to look inside one.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `doctest` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 731-doctest/lesson_731_doctest.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_731_doctest.py</code></summary>

```python
"""Doctest.

`doctest` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 731-doctest/lesson_731_doctest.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import doctest

    return getattr(doctest, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names doctest offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import doctest

    return sorted(item for item in dir(doctest) if not item.startswith("_"))


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
pytest 731-doctest
```

## 4. Open the notebook

```bash
jupyter notebook 731-doctest/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `doctest` | A standard library module for doctest |

## Your turn

1. Open the REPL, `import doctest`, then call `dir(doctest)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 730-testing-project](../730-testing-project/) · [Next: 732-property-testing →](../732-property-testing/)
