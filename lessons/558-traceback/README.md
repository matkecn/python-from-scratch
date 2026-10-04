# 558 · Traceback

`traceback` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `traceback` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 558-traceback/lesson_558_traceback.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_558_traceback.py</code></summary>

```python
"""Traceback.

`traceback` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 558-traceback/lesson_558_traceback.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import traceback

    return getattr(traceback, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names traceback offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import traceback

    return sorted(item for item in dir(traceback) if not item.startswith("_"))


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
pytest 558-traceback
```

## 4. Open the notebook

```bash
jupyter notebook 558-traceback/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `traceback` | A standard library module for traceback |

## Your turn

1. Open the REPL, `import traceback`, then call `dir(traceback)`.

## Read more

- [`traceback` module docs](https://docs.python.org/3/library/traceback.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 557-warnings](../557-warnings/) · [Next: 559-linecache →](../559-linecache/)
