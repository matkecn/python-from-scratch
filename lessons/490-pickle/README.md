# 490 · Pickle

`pickle` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `pickle` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 490-pickle/lesson_490_pickle.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_490_pickle.py</code></summary>

```python
"""Pickle.

`pickle` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 490-pickle/lesson_490_pickle.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import pickle

    return getattr(pickle, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names pickle offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import pickle

    return sorted(item for item in dir(pickle) if not item.startswith("_"))


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
pytest 490-pickle
```

## 4. Open the notebook

```bash
jupyter notebook 490-pickle/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `pickle` | A standard library module for pickle |

## Your turn

1. Open the REPL, `import pickle`, then call `dir(pickle)`.

## Read more

- [`pickle` module docs](https://docs.python.org/3/library/pickle.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 489-csv-dialects](../489-csv-dialects/) · [Next: 491-pickle-security →](../491-pickle-security/)
