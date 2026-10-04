# 288 · Heapq

`heapq` is a standard library module. This lesson shows how to look inside one.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `heapq` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 288-heapq/lesson_288_heapq.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_288_heapq.py</code></summary>

```python
"""Heapq.

`heapq` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 288-heapq/lesson_288_heapq.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import heapq

    return getattr(heapq, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names heapq offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import heapq

    return sorted(item for item in dir(heapq) if not item.startswith("_"))


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
pytest 288-heapq
```

## 4. Open the notebook

```bash
jupyter notebook 288-heapq/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `heapq` | A standard library module for heapq |

## Your turn

1. Open the REPL, `import heapq`, then call `dir(heapq)`.

## Read more

- [`heapq` module docs](https://docs.python.org/3/library/heapq.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 287-userstring](../287-userstring/) · [Next: 289-bisect →](../289-bisect/)
