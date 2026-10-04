# 550 · Fnmatch

`fnmatch` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `fnmatch` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 550-fnmatch/lesson_550_fnmatch.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_550_fnmatch.py</code></summary>

```python
"""Fnmatch.

`fnmatch` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 550-fnmatch/lesson_550_fnmatch.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import fnmatch

    return getattr(fnmatch, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names fnmatch offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import fnmatch

    return sorted(item for item in dir(fnmatch) if not item.startswith("_"))


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
pytest 550-fnmatch
```

## 4. Open the notebook

```bash
jupyter notebook 550-fnmatch/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `fnmatch` | A standard library module for fnmatch |

## Your turn

1. Open the REPL, `import fnmatch`, then call `dir(fnmatch)`.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 549-difflib](../549-difflib/) · [Next: 551-pathlib →](../551-pathlib/)
