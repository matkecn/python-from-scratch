# 000 · Welcome

> The shortest useful program in any language is one line. This is ours.

**Level** 1 of 5 · **Time** about 10 minutes

Welcome. This folder holds the very first program anyone writes:

```python
print("Hello, world!")
```

If you have never programmed, you just did. If you have, you remember the
feeling anyway.

## You will learn

- A Python file is a list of instructions, run from the top down
- `print` shows a value on the screen
- Text goes between quotes, and quotes come in pairs
- A function is a name you can run again later

## Run it

```bash
python 000-welcome/lesson_000_welcome.py
```

You should see two lines:

```text
Hello, world!
Hello, Ada!
```

## Read the code

<details>
<summary>Show <code>lesson_000_welcome.py</code></summary>

```python
"""Welcome to Python.

The shortest useful program in any language is one line. This is ours.

Run me:
    python 000-welcome/lesson_000_welcome.py
"""

from __future__ import annotations


def hello_world() -> str:
    """Return the classic first line of programming.

    Returns:
        The text ``"Hello, world!"``.

    Examples:
        >>> hello_world()
        'Hello, world!'
    """
    return "Hello, world!"


def greet(name: str) -> str:
    """Return a greeting for one person.

    Args:
        name: Who to greet. An empty name falls back to ``"world"``.

    Returns:
        A friendly greeting.

    Examples:
        >>> greet("Ada")
        'Hello, Ada!'
        >>> greet("")
        'Hello, world!'
    """
    who = name or "world"
    return f"Hello, {who}!"


def main() -> None:
    """Print the classic line, then a personal one."""
    print(hello_world())
    print(greet("Ada"))


if __name__ == "__main__":
    main()
```

</details>

## Run the tests

```bash
pytest 000-welcome
```

## Open the notebook

```bash
jupyter notebook 000-welcome/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `print` | Shows a value on the screen |
| function | A named recipe you can run again |
| `return` | Hands a value back to whoever asked for it |
| `f-string` | Text with a `{hole}` for a value |

## Your turn

1. Add a `goodbye(name: str) -> str` function that returns `"Goodbye, Ada!"`.
2. Print it from `main`.
3. Add a test for it in `test_lesson_000_welcome.py`.

## Where next

Open [`001-getting-started`](../001-getting-started/README.md) to install Python
properly and learn how to run a file.

---

[Next: Getting started →](../001-getting-started/)
