# 579 · Standard-library-project

Placeholder for **Standard-library-project**. A later phase replaces this with a full lesson.

**Section** Standard library tour · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Find the official documentation and skim it
- Try the smallest possible example in the REPL
- Write the one sentence that explains the idea in your own words

## 1. Run the example

```bash
python 579-standard-library-project/lesson_579_standard_library_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_579_standard_library_project.py</code></summary>

```python
"""Standard-library-project.

Placeholder for **Standard-library-project**. A later phase replaces this with a full lesson.

Run me:
    python 579-standard-library-project/lesson_579_standard_library_project.py
"""

from __future__ import annotations


def keywords() -> list[str]:
    """Return search words that will find this topic in the documentation.

    Returns:
        Words to search for.
    """
    return sorted({"standard library project"})


def outline() -> str:
    """Return a tiny study outline for the topic.

    Returns:
        Three steps to work through.
    """
    return "\n".join(f"{step}. Standard-library-project" for step in (1, 2, 3))


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
pytest 579-standard-library-project
```

## 4. Open the notebook

```bash
jupyter notebook 579-standard-library-project/lesson.ipynb
```

## Your turn

1. Replace this lesson with a real one: add two small functions with docstrings.
2. Add one test per function.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 578-text-processing-project](../578-text-processing-project/) · [Next: 580-stdlib-review →](../580-stdlib-review/)
