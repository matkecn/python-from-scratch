# 487 · Csv-reader

Placeholder for **Csv-reader**. A later phase replaces this with a full lesson.

**Section** Files, paths and serialization · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 487-csv-reader/lesson_487_csv_reader.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_487_csv_reader.py</code></summary>

```python
"""Csv-reader.

Placeholder for **Csv-reader**. A later phase replaces this with a full lesson.

Run me:
    python 487-csv-reader/lesson_487_csv_reader.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"csv reader"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Csv-reader" for step in (1, 2, 3))


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(outline())
    print(keywords())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 487-csv-reader
```

## 4. Open the notebook

```bash
jupyter notebook 487-csv-reader/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`csv` module docs](https://docs.python.org/3/library/csv.html)
- [official tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

[← 486-csv](../486-csv/) · [Next: 488-csv-writer →](../488-csv-writer/)
