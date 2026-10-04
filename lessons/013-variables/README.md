# 013 · Variables

A variable is a name that remembers a value.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Store a value with `=`
- Change a name as often as you like
- Swap two values in one line

## 1. Run the example

```bash
python 013-variables/lesson_013_variables.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_013_variables.py</code></summary>

```python
"""Variables.

A variable is a label you stick on a value. `=` does not mean equals, it means
"put this value in this box".

Run me:
    python 013-variables/lesson_013_variables.py
"""

from __future__ import annotations


def make_greeting(name: str) -> str:
    """Build a greeting for someone.

    Args:
        name: The person's name.

    Returns:
        A greeting ending with an exclamation mark.

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


def describe_box(box: int) -> str:
    """Describe a variable in words.

    Args:
        box: The value inside the box.

    Returns:
        A sentence about the value and its type.

    Examples:
        >>> describe_box(3)
        'the box holds 3, which is type int'
    """
    return f"the box holds {box}, which is type {type(box).__name__}"


def main() -> None:
    """Make a few variables and look at them."""
    name = "Ada"
    year = 1815
    print(make_greeting(name))
    print(describe_box(year))
    left, right = swap(1, 2)
    print(f"swapped: left={left}, right={right}")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 013-variables
```

## 4. Open the notebook

```bash
jupyter notebook 013-variables/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `variable` | A name that points at a value |
| `assignment` | Storing a value in a name |

## Your turn

1. Make three variables for a character and print a one line story about them.
2. Swap three values using one line and no temporary variable.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 012-input](../012-input/) · [Next: 014-naming →](../014-naming/)
