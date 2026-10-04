# 001 · Getting-started

Three commands and you are ready to write Python.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Check that Python is installed
- Read your version as two numbers
- Know which version this course needs

## 1. Run the example

```bash
python 001-getting-started/lesson_001_getting_started.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_001_getting_started.py</code></summary>

```python
"""Getting started.

Three commands and you are ready to write Python.

Run me:
    python 001-getting-started/lesson_001_getting_started.py
"""

from __future__ import annotations

import sys

NEEDED = (3, 11)


def version_number() -> tuple[int, int]:
    """Return the Python version as two plain numbers.

    Returns:
        The major and minor version, for example ``(3, 12)``.

    Examples:
        >>> version = version_number()
        >>> len(version)
        2
    """
    return sys.version_info.major, sys.version_info.minor


def is_supported() -> bool:
    """Say whether this Python is new enough for the course.

    Returns:
        ``True`` when the version is 3.11 or newer.

    Examples:
        >>> is_supported() == (version_number() >= (3, 11))
        True
    """
    return version_number() >= NEEDED


def version_text() -> str:
    """Return a friendly one line description of this Python.

    Returns:
        Text such as ``"Python 3.12.0 is ready"``.

    Examples:
        >>> version_text().startswith("Python 3")
        True
    """
    full = ".".join(str(part) for part in sys.version_info[:3])
    if is_supported():
        return f"Python {full} is ready"
    return f"Python {full} is too old, we need {NEEDED[0]}.{NEEDED[1]} or newer"


def main() -> None:
    """Print what we found."""
    print(version_text())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 001-getting-started
```

## 4. Open the notebook

```bash
jupyter notebook 001-getting-started/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `interpreter` | The program that reads and runs your Python code |
| `version` | The number that says which release you have |

## Your turn

1. Print the version on your own machine and compare it with a friend.
2. Change `NEEDED` to `(3, 99)` and watch `version_text` complain.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 000-welcome](../000-welcome/) · [Next: 002-what-is-python →](../002-what-is-python/)
