# 735 · Behavior-driven-testing

Placeholder for **Behavior-driven-testing**. A later phase replaces this with a full lesson.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 735-behavior-driven-testing/lesson_735_behavior_driven_testing.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_735_behavior_driven_testing.py</code></summary>

```python
"""Behavior-driven-testing.

Placeholder for **Behavior-driven-testing**. A later phase replaces this with a full lesson.

Run me:
    python 735-behavior-driven-testing/lesson_735_behavior_driven_testing.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"behavior driven testing"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Behavior-driven-testing" for step in (1, 2, 3))


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
pytest 735-behavior-driven-testing
```

## 4. Open the notebook

```bash
jupyter notebook 735-behavior-driven-testing/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 734-test-driven-development](../734-test-driven-development/) · [Next: 736-testing-exceptions →](../736-testing-exceptions/)
