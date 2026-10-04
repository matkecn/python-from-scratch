# 002 · What-is-python

Python is a language, and it is also the program that runs it.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Tell the language from the program that runs it
- Read the implementation and the version
- See that your code is turned into bytecode first

## 1. Run the example

```bash
python 002-what-is-python/lesson_002_what_is_python.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_002_what_is_python.py</code></summary>

```python
"""What is Python.

Python is two things: a language you write, and a program that runs it.

Run me:
    python 002-what-is-python/lesson_002_what_is_python.py
"""

from __future__ import annotations

import platform
import sys


def implementation() -> str:
    """Return the name of the Python running this code.

    Returns:
        Usually ``"CPython"``.

    Examples:
        >>> isinstance(implementation(), str)
        True
    """
    return platform.python_implementation()


def python_version() -> str:
    """Return the full version, such as ``"3.12.0"``.

    Returns:
        The version as text.
    """
    return platform.python_version()


def runs_bytecode() -> bool:
    """Say whether Python turns source into bytecode before running it.

    Returns:
        ``True`` for CPython, which caches compiled code.

    Examples:
        >>> runs_bytecode() == (implementation() == "CPython")
        True
    """
    return implementation() == "CPython"


def summary() -> str:
    """Return one sentence describing this Python.

    Returns:
        A short summary you could read out loud.
    """
    return f"{implementation()} {python_version()} runs bytecode: {runs_bytecode()}"


def main() -> None:
    """Print what we found."""
    print(summary())
    print(f"running on {sys.platform}")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 002-what-is-python
```

## 4. Open the notebook

```bash
jupyter notebook 002-what-is-python/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `CPython` | The most common Python, written in C |
| `bytecode` | A small set of instructions Python runs quickly |

## Your turn

1. Find out which Python your friend uses and compare notes.
2. Use `sys.executable` to print the exact program that is running your code.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 001-getting-started](../001-getting-started/) · [Next: 003-installation →](../003-installation/)
