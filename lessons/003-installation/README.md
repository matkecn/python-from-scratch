# 003 · Installation

Find the Python program on your computer and check it works.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Use `shutil.which` to look for a program
- Fall back to the running interpreter
- Report a clear yes or no

## 1. Run the example

```bash
python 003-installation/lesson_003_installation.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_003_installation.py</code></summary>

```python
"""Installation.

Is Python installed? This lesson asks the computer instead of guessing.

Run me:
    python 003-installation/lesson_003_installation.py
"""

from __future__ import annotations

import shutil
import sys


def find_python() -> str:
    """Return the path of a Python program on this computer.

    Returns:
        The path of ``python3``, or the interpreter running this code.

    Examples:
        >>> bool(find_python())
        True
    """
    return shutil.which("python3") or sys.executable


def is_installed() -> bool:
    """Say whether a Python program can be found.

    Returns:
        ``True`` when Python is ready to use.
    """
    return bool(find_python())


def check() -> str:
    """Return a short report about this computer.

    Returns:
        A line a beginner can read without panic.
    """
    if not is_installed():
        return "Python is missing. Install it from python.org and try again."
    return f"Python found at {find_python()}"


def main() -> None:
    """Print the report."""
    print(check())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 003-installation
```

## 4. Open the notebook

```bash
jupyter notebook 003-installation/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `PATH` | The list of folders your computer searches for programs |
| ``python3`` | The usual name for Python on macOS and Linux |

## Your turn

1. Run `python3 --version` in your terminal and compare it with `check()`.
2. Use `shutil.which` to find `git` the same way.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 002-what-is-python](../002-what-is-python/) · [Next: 004-python-versions →](../004-python-versions/)
