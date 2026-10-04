# 712 · Test-cases

Tests are code that checks your code still works.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Write one test per behaviour
- Use `assert` to check
- Run them with `pytest`

## 1. Run the example

```bash
python 712-test-cases/lesson_712_test_cases.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_712_test_cases.py</code></summary>

```python
"""Test-cases.

Tests are code that checks your code still works.

Run me:
    python 712-test-cases/lesson_712_test_cases.py
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
pytest 712-test-cases
```

## 4. Open the notebook

```bash
jupyter notebook 712-test-cases/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `test` | A check that a piece of code behaves |
| `assert` | A line that must be true or the test fails |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 711-unittest](../711-unittest/) · [Next: 713-test-methods →](../713-test-methods/)
