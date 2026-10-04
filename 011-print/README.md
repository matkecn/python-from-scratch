# 011 · Print

`print` shows a value. `return` hands it back. They are not the same.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- `print` writes to the screen for people
- `return` gives a value back to code
- Change the gap with `sep` and the ending with `end`

## 1. Run the example

```bash
python 011-print/lesson_011_print.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_011_print.py</code></summary>

```python
"""Print.

`print` is for people. `return` is for code. A function that returns a value
can be printed later, reused and tested.

Run me:
    python 011-print/lesson_011_print.py
"""

from __future__ import annotations


def shout(text: str) -> str:
    """Return the text in upper case.

    Args:
        text: The text to shout.

    Returns:
        The same text, louder.

    Examples:
        >>> shout("hello")
        'HELLO'
    """
    return text.upper()


def show(text: str, times: int = 1) -> None:
    """Print some text a number of times.

    Args:
        text: The text to print.
        times: How many lines to print.
    """
    for _ in range(times):
        print(text)


def join_numbers(numbers: list[int]) -> str:
    """Return numbers as one line, separated by dashes.

    Args:
        numbers: The numbers to join.

    Returns:
        A single line of text.

    Examples:
        >>> join_numbers([1, 2, 3])
        '1 - 2 - 3'
    """
    return " - ".join(str(number) for number in numbers)


def main() -> None:
    """Show printing and returning side by side."""
    print(shout("hello"))
    show("again", times=2)
    print(join_numbers([1, 2, 3]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 011-print
```

## 4. Open the notebook

```bash
jupyter notebook 011-print/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `side effect` | Something a program does that a caller cannot see, like printing |
| `return` | Handing a value back to whoever called |

## Your turn

1. Print the same value twice, once with `print` and once with `return`.
2. Use `sep` and `end` to print `1, 2, 3` on one line without trailing spaces.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 010-indentation](../010-indentation/) · [Next: 012-input →](../012-input/)
