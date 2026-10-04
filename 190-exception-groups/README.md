# 190 · Exception-groups

Exceptions are how Python complains about problems.

**Section** Modules, imports and exceptions · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Errors stop the program
- `try` and `except` catch them
- `raise` sends one on purpose

## 1. Run the example

```bash
python 190-exception-groups/lesson_190_exception_groups.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_190_exception_groups.py</code></summary>

```python
"""Exception-groups.

Exceptions are how Python complains about problems.

Run me:
    python 190-exception-groups/lesson_190_exception_groups.py
"""

from __future__ import annotations


def parse_age(text: str) -> int:
    """Turn text into an age.

    Args:
        text: The text to read.

    Returns:
        The age as a whole number.

    Raises:
        ValueError: If the text is not a whole number.

    Examples:
        >>> parse_age("12")
        12
    """
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"age must be a whole number: {text!r}") from error


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(parse_age("12"))
    try:
        print(parse_age("old"))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 190-exception-groups
```

## 4. Open the notebook

```bash
jupyter notebook 190-exception-groups/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `exception` | A signal that something went wrong |
| `raise` | Send an exception on purpose |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/modules.html)

---

[← 189-exception-chaining](../189-exception-chaining/) · [Next: 191-baseexception →](../191-baseexception/)
