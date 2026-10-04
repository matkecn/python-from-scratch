# 995 · Build-your-own-test-framework

Tests are code that checks your code still works.

**Section** Projects, challenges and mastery · **Level** 5 of 5 · **Time** about 60 minutes · **Status** generated draft (Phase 2)

## You will learn

- Write one test per behaviour
- Use `assert` to check
- Run them with `pytest`

## 1. Run the example

```bash
python 995-build-your-own-test-framework/lesson_995_build_your_own_test_framework.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_995_build_your_own_test_framework.py</code></summary>

```python
"""Build-your-own-test-framework.

Tests are code that checks your code still works.

Run me:
    python 995-build-your-own-test-framework/lesson_995_build_your_own_test_framework.py
"""

from __future__ import annotations


def add(first: int, second: int) -> int:
    """Add two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The total.
    """
    return first + second


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(add(2, 3))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 995-build-your-own-test-framework
```

## 4. Open the notebook

```bash
jupyter notebook 995-build-your-own-test-framework/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `test` | A check that a piece of code behaves |
| `assert` | A line that must be true or the test fails |

## Read more

- [language reference](https://docs.python.org/3/reference/index.html)
- [glossary](https://docs.python.org/3/glossary.html)

---

[← 994-build-your-own-database-layer](../994-build-your-own-database-layer/) · [Next: 996-build-your-own-package →](../996-build-your-own-package/)
