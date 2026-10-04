# 289 · Bisect

`bisect` is a standard library module. This lesson shows how to look inside one.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `bisect` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 289-bisect/lesson_289_bisect.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_289_bisect.py</code></summary>

```python
"""Bisect.

`bisect` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 289-bisect/lesson_289_bisect.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import bisect

    return getattr(bisect, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names bisect offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import bisect

    return sorted(item for item in dir(bisect) if not item.startswith("_"))


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
pytest 289-bisect
```

## 4. Open the notebook

```bash
jupyter notebook 289-bisect/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `bisect` | A standard library module for bisect |

## Your turn

1. Open the REPL, `import bisect`, then call `dir(bisect)`.

## Read more

- [`bisect` module docs](https://docs.python.org/3/library/bisect.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 288-heapq](../288-heapq/) · [Next: 290-array →](../290-array/)
