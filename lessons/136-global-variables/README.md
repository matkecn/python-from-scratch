# 136 · Global-variables

A variable is a name that remembers a value.

**Section** Functions, arguments and scope · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Create a variable with `=`
- One name can be given a new value
- Names use snake_case

## 1. Run the example

```bash
python 136-global-variables/lesson_136_global_variables.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_136_global_variables.py</code></summary>

```python
"""Global-variables.

A variable is a name that remembers a value.

Run me:
    python 136-global-variables/lesson_136_global_variables.py
"""

from __future__ import annotations


def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting that ends with an exclamation mark.

    Examples:
        >>> make_greeting("Ada")
        'Hello, Ada!'
    """
    return f"Hello, {name}!"


def swap(first: int, second: int) -> tuple[int, int]:
    """Return two numbers in the opposite order.

    Args:
        first: The number that should end up second.
        second: The number that should end up first.

    Returns:
        The two numbers, swapped.

    Examples:
        >>> swap(1, 2)
        (2, 1)
    """
    return second, first


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(make_greeting("Ada"))
    print(swap(1, 2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 136-global-variables
```

## 4. Open the notebook

```bash
jupyter notebook 136-global-variables/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `variable` | A name that points at a value |
| `assignment` | Storing a value in a name with `=` |

## Your turn

1. Add a third variable that holds your age and print all three.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/functions.html)

---

[← 135-local-variables](../135-local-variables/) · [Next: 137-nonlocal →](../137-nonlocal/)
