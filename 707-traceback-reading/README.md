# 707 · Traceback-reading

Placeholder for **Traceback-reading**. A later phase replaces this with a full lesson.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 707-traceback-reading/lesson_707_traceback_reading.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_707_traceback_reading.py</code></summary>

```python
"""Traceback-reading.

Placeholder for **Traceback-reading**. A later phase replaces this with a full lesson.

Run me:
    python 707-traceback-reading/lesson_707_traceback_reading.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"traceback reading"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Traceback-reading" for step in (1, 2, 3))


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
pytest 707-traceback-reading
```

## 4. Open the notebook

```bash
jupyter notebook 707-traceback-reading/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`traceback` module docs](https://docs.python.org/3/library/traceback.html)
- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 706-debugger-practice](../706-debugger-practice/) · [Next: 708-error-reproduction →](../708-error-reproduction/)
