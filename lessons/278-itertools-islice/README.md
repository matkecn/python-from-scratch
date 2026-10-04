# 278 · Itertools-islice

Placeholder for **Itertools-islice**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 278-itertools-islice/lesson_278_itertools_islice.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_278_itertools_islice.py</code></summary>

```python
"""Itertools-islice.

Placeholder for **Itertools-islice**. A later phase replaces this with a full lesson.

Run me:
    python 278-itertools-islice/lesson_278_itertools_islice.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"itertools islice"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Itertools-islice" for step in (1, 2, 3))


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
pytest 278-itertools-islice
```

## 4. Open the notebook

```bash
jupyter notebook 278-itertools-islice/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`itertools` module docs](https://docs.python.org/3/library/itertools.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 277-itertools-groupby](../277-itertools-groupby/) · [Next: 279-itertools-tee →](../279-itertools-tee/)
