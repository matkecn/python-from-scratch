# 449 · Data-model-project

Placeholder for **Data-model-project**. A later phase replaces this with a full lesson.

**Section** The Python data model (dunder methods) · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 449-data-model-project/lesson_449_data_model_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_449_data_model_project.py</code></summary>

```python
"""Data-model-project.

Placeholder for **Data-model-project**. A later phase replaces this with a full lesson.

Run me:
    python 449-data-model-project/lesson_449_data_model_project.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"data model project"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Data-model-project" for step in (1, 2, 3))


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
pytest 449-data-model-project
```

## 4. Open the notebook

```bash
jupyter notebook 449-data-model-project/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/datamodel.html)

---

[← 448-custom-awaitable](../448-custom-awaitable/) · [Next: 450-python-protocol-project →](../450-python-protocol-project/)
