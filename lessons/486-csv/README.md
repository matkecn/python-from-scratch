# 486 · Csv

`csv` is a standard library module. This lesson shows how to look inside one.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Import `csv` and see what it holds
- Use `dir` to list what a module offers
- Read the module's own docs

## 1. Run the example

```bash
python 486-csv/lesson_486_csv.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_486_csv.py</code></summary>

```python
"""Csv.

`csv` is a standard library module. This lesson shows how to look inside one.

Run me:
    python 486-csv/lesson_486_csv.py
"""

from __future__ import annotations


def module_path() -> str:
    """Return the file the module lives in.

    Returns:
        The path of the module file.
    """
    import csv

    return getattr(csv, "__file__", "built in")


def public_names() -> list[str]:
    """Return the names csv offers that do not start with an underscore.

    Returns:
        A sorted list of public names.
    """
    import csv

    return sorted(item for item in dir(csv) if not item.startswith("_"))


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
pytest 486-csv
```

## 4. Open the notebook

```bash
jupyter notebook 486-csv/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `csv` | A standard library module for csv |

## Your turn

1. Open the REPL, `import csv`, then call `dir(csv)`.

## Read more

- [`csv` module docs](https://docs.python.org/3/library/csv.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 485-json-custom-types](../485-json-custom-types/) · [Next: 487-csv-reader →](../487-csv-reader/)
