# 739 · Testing-apis

Placeholder for **Testing-apis**. A later phase replaces this with a full lesson.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 739-testing-apis/lesson_739_testing_apis.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_739_testing_apis.py</code></summary>

```python
"""Testing-apis.

Placeholder for **Testing-apis**. A later phase replaces this with a full lesson.

Run me:
    python 739-testing-apis/lesson_739_testing_apis.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"testing apis"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Testing-apis" for step in (1, 2, 3))


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
pytest 739-testing-apis
```

## 4. Open the notebook

```bash
jupyter notebook 739-testing-apis/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 738-testing-databases](../738-testing-databases/) · [Next: 740-testing-project-advanced →](../740-testing-project-advanced/)
