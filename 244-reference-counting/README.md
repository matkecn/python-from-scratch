# 244 · Reference-counting

Placeholder for **Reference-counting**. A later phase replaces this with a full lesson.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 244-reference-counting/lesson_244_reference_counting.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_244_reference_counting.py</code></summary>

```python
"""Reference-counting.

Placeholder for **Reference-counting**. A later phase replaces this with a full lesson.

Run me:
    python 244-reference-counting/lesson_244_reference_counting.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"reference counting"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Reference-counting" for step in (1, 2, 3))


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
pytest 244-reference-counting
```

## 4. Open the notebook

```bash
jupyter notebook 244-reference-counting/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 243-garbage-collection](../243-garbage-collection/) · [Next: 245-weakref →](../245-weakref/)
