# 290 · Array

`array` is a standard library module. This lesson shows how to look inside one.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `array` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 290-array/lesson_290_array.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_290_array.py</code></summary>

```python
"""Array.

`array` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 290-array/lesson_290_array.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import array

    return getattr(array, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names array offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import array

    return sorted(item for item in dir(array) if not item.startswith("_"))


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
pytest 290-array
```

## 4. Open the notebook

```bash
jupyter notebook 290-array/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `array` | A standard library module for array |

## Your turn

1. Open the REPL, `import array`, then call `dir(array)`.

## Read more

- [`array` module docs](https://docs.python.org/3/library/array.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 289-bisect](../289-bisect/) · [Next: 291-enumeration →](../291-enumeration/)
