# 391 · Pattern matching

Placeholder for **Pattern matching**. A later phase replaces this with a full lesson.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 391-pattern-matching/lesson_391_pattern_matching.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_391_pattern_matching.py</code></summary>

```python
"""Pattern matching.

Placeholder for **Pattern matching**. A later phase replaces this with a full lesson.

Run me:
    python 391-pattern-matching/lesson_391_pattern_matching.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"pattern matching"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Pattern matching" for step in (1, 2, 3))


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
pytest 391-pattern-matching
```

## 4. Open the notebook

```bash
jupyter notebook 391-pattern-matching/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 390-dataclass-patterns](../390-dataclass-patterns/) · [Next: 392-sequence-patterns →](../392-sequence-patterns/)
