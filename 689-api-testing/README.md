# 689 · Api-testing

Placeholder for **Api-testing**. A later phase replaces this with a full lesson.

**Section** Web concepts, scraping and security · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 689-api-testing/lesson_689_api_testing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_689_api_testing.py</code></summary>

```python
"""Api-testing.

Placeholder for **Api-testing**. A later phase replaces this with a full lesson.

Run me:
    python 689-api-testing/lesson_689_api_testing.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"api testing"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Api-testing" for step in (1, 2, 3))


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
pytest 689-api-testing
```

## 4. Open the notebook

```bash
jupyter notebook 689-api-testing/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 688-api-errors](../688-api-errors/) · [Next: 690-api-client-project →](../690-api-client-project/)
