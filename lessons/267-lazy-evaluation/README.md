# 267 · Lazy-evaluation

Placeholder for **Lazy-evaluation**. A later phase replaces this with a full lesson.

**Section** Iterators, generators and the collections library · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 267-lazy-evaluation/lesson_267_lazy_evaluation.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_267_lazy_evaluation.py</code></summary>

```python
"""Lazy-evaluation.

Placeholder for **Lazy-evaluation**. A later phase replaces this with a full lesson.

Run me:
    python 267-lazy-evaluation/lesson_267_lazy_evaluation.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"lazy evaluation"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Lazy-evaluation" for step in (1, 2, 3))


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
pytest 267-lazy-evaluation
```

## 4. Open the notebook

```bash
jupyter notebook 267-lazy-evaluation/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 266-generator-pipelines](../266-generator-pipelines/) · [Next: 268-infinite-iterators →](../268-infinite-iterators/)
