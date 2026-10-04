# 713 · Test-methods

Tests are code that checks your code still works.

**Section** Debugging and testing · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Write one test per behaviour
- Use `assert` to check
- Run them with `pytest`

## 1. Run the example

```bash
python 713-test-methods/lesson_713_test_methods.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_713_test_methods.py</code></summary>

```python
"""Test-methods.

Tests are code that checks your code still works.

Run me:
    python 713-test-methods/lesson_713_test_methods.py
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
pytest 713-test-methods
```

## 4. Open the notebook

```bash
jupyter notebook 713-test-methods/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `test` | A check that a piece of code behaves |
| `assert` | A line that must be true or the test fails |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/unittest.html)

---

[← 712-test-cases](../712-test-cases/) · [Next: 714-assertions →](../714-assertions/)
