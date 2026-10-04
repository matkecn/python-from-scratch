# 273 · Itertools-count

Placeholder for **Itertools-count**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 273-itertools-count/lesson_273_itertools_count.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_273_itertools_count.py</code></summary>

```python
"""Itertools-count.

Placeholder for **Itertools-count**. A later phase replaces this with a full lesson.

Run me:
    python 273-itertools-count/lesson_273_itertools_count.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"itertools count"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Itertools-count" for step in (1, 2, 3))


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
pytest 273-itertools-count
```

## 4. Open the notebook

```bash
jupyter notebook 273-itertools-count/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`itertools` module docs](https://docs.python.org/3/library/itertools.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 272-itertools-repeat](../272-itertools-repeat/) · [Next: 274-itertools-product →](../274-itertools-product/)
