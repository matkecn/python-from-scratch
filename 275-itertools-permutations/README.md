# 275 · Itertools-permutations

Placeholder for **Itertools-permutations**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 275-itertools-permutations/lesson_275_itertools_permutations.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_275_itertools_permutations.py</code></summary>

```python
"""Itertools-permutations.

Placeholder for **Itertools-permutations**. A later phase replaces this with a full lesson.

Run me:
    python 275-itertools-permutations/lesson_275_itertools_permutations.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"itertools permutations"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Itertools-permutations" for step in (1, 2, 3))


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
pytest 275-itertools-permutations
```

## 4. Open the notebook

```bash
jupyter notebook 275-itertools-permutations/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`itertools` module docs](https://docs.python.org/3/library/itertools.html)
- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 274-itertools-product](../274-itertools-product/) · [Next: 276-itertools-combinations →](../276-itertools-combinations/)
