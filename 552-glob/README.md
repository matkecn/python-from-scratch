# 552 · Glob

`glob` is a standard library module. This lesson shows how to look inside one.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `glob` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 552-glob/lesson_552_glob.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_552_glob.py</code></summary>

```python
"""Glob.

`glob` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 552-glob/lesson_552_glob.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import glob

    return getattr(glob, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names glob offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import glob

    return sorted(item for item in dir(glob) if not item.startswith("_"))


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
pytest 552-glob
```

## 4. Open the notebook

```bash
jupyter notebook 552-glob/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `glob` | A standard library module for glob |

## Your turn

1. Open the REPL, `import glob`, then call `dir(glob)`.

## Read more

- [`glob` module docs](https://docs.python.org/3/library/glob.html)
- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 551-pathlib](../551-pathlib/) · [Next: 553-fileinput →](../553-fileinput/)
