# 600 · Cli-and-logging-project

Logging writes notes about what your program is doing.

**Section** Command line tools and logging · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Use levels such as info and error
- Log to the screen or to a file
- Libraries should not use `print`

## 1. Run the example

```bash
python 600-cli-and-logging-project/lesson_600_cli_and_logging_project.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_600_cli_and_logging_project.py</code></summary>

```python
"""Cli-and-logging-project.

Logging writes notes about what your program is doing.

Run me:
    python 600-cli-and-logging-project/lesson_600_cli_and_logging_project.py
"""

from __future__ import annotations


import logging

logger = logging.getLogger("lesson")


def make_logger(level: int = logging.INFO) -> logging.Logger:
    """Return a logger that writes short messages.

    Args:
        level: The lowest level to show.

    Returns:
        The configured logger.
    """
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    return logger


def log_a_journey(steps: list[str]) -> list[str]:
    """Log each step and return the steps.

    Args:
        steps: The steps to log.

    Returns:
        The same steps, unchanged.
    """
    for step in steps:
        logger.info("step: %s", step)
    return steps


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    make_logger()
    print(log_a_journey(["start", "stop"]))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 600-cli-and-logging-project
```

## 4. Open the notebook

```bash
jupyter notebook 600-cli-and-logging-project/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `logging` | Recorded notes about how a program behaves |

## Read more

- [`logging` module docs](https://docs.python.org/3/library/logging.html)

---

[← 599-logging-project](../599-logging-project/) · [Next: 601-sockets →](../601-sockets/)
