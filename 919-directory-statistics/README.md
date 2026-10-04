# 919 · Directory-statistics

Placeholder for **Directory-statistics**. A later phase replaces this with a full lesson.

**Section** Practical Python applications · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 919-directory-statistics/lesson_919_directory_statistics.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_919_directory_statistics.py</code></summary>

```python
"""Directory-statistics.

Placeholder for **Directory-statistics**. A later phase replaces this with a full lesson.

Run me:
    python 919-directory-statistics/lesson_919_directory_statistics.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"directory statistics"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Directory-statistics" for step in (1, 2, 3))


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
pytest 919-directory-statistics
```

## 4. Open the notebook

```bash
jupyter notebook 919-directory-statistics/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [`statistics` module docs](https://docs.python.org/3/library/statistics.html)

---

[← 918-batch-renamer](../918-batch-renamer/) · [Next: 920-data-processing-project →](../920-data-processing-project/)
