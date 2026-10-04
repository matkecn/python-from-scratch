# 559 · Linecache

`linecache` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `linecache` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 559-linecache/lesson_559_linecache.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_559_linecache.py</code></summary>

```python
"""Linecache.

`linecache` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 559-linecache/lesson_559_linecache.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import linecache

    return getattr(linecache, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names linecache offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import linecache

    return sorted(item for item in dir(linecache) if not item.startswith("_"))


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
pytest 559-linecache
```

## 4. Open the notebook

```bash
jupyter notebook 559-linecache/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `linecache` | A standard library module for linecache |

## Your turn

1. Open the REPL, `import linecache`, then call `dir(linecache)`.

## Read more

- [`linecache` module docs](https://docs.python.org/3/library/linecache.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 558-traceback](../558-traceback/) · [Next: 560-codecs →](../560-codecs/)
