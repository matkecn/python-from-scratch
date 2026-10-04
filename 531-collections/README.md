# 531 · Collections

`collections` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `collections` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 531-collections/lesson_531_collections.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_531_collections.py</code></summary>

```python
"""Collections.

`collections` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 531-collections/lesson_531_collections.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import collections

    return getattr(collections, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names collections offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import collections

    return sorted(item for item in dir(collections) if not item.startswith("_"))


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
pytest 531-collections
```

## 4. Open the notebook

```bash
jupyter notebook 531-collections/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `collections` | A standard library module for collections |

## Your turn

1. Open the REPL, `import collections`, then call `dir(collections)`.

## Read more

- [`collections` module docs](https://docs.python.org/3/library/collections.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 530-calendar](../530-calendar/) · [Next: 532-collections-defaultdict →](../532-collections-defaultdict/)
