# 729 · Integration-tests

Tests are code that checks your code still works.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Write one test per behaviour
- Use `assert` to check
- Run them with `pytest`

## 1. Run the example

```bash
python 729-integration-tests/lesson_729_integration_tests.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_729_integration_tests.py</code></summary>

```python
"""Integration-tests.

Tests are code that checks your code still works.

Run me:
    python 729-integration-tests/lesson_729_integration_tests.py
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
pytest 729-integration-tests
```

## 4. Open the notebook

```bash
jupyter notebook 729-integration-tests/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `test` | A check that a piece of code behaves |
| `assert` | A line that must be true or the test fails |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 728-code-coverage](../728-code-coverage/) · [Next: 730-testing-project →](../730-testing-project/)
