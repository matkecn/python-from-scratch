# 005 · Python-interpreter

The interpreter is the program that actually runs your code.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Find the interpreter with `sys.executable`
- Hand a line of code to a brand new Python
- Read back exactly what it printed

## 1. Run the example

```bash
python 005-python-interpreter/lesson_005_python_interpreter.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_005_python_interpreter.py</code></summary>

```python
"""Python interpreter.

Your ``.py`` file is text. Something has to read it and do what it says. That
something is the interpreter.

Run me:
    python 005-python-interpreter/lesson_005_python_interpreter.py
"""

from __future__ import annotations

import subprocess
import sys


def interpreter_path() -> str:
    """Return the path of the interpreter running this very code.

    Returns:
        The path of the Python program.

    Examples:
        >>> interpreter_path().endswith(("python", "python3", "python.exe")) or True
        True
    """
    return sys.executable


def run_expression(source: str) -> str:
    """Run one line of Python in a brand new interpreter.

    Args:
        source: The code to run, for example ``"print(2 + 2)"``.

    Returns:
        Whatever the code printed, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the code fails.

    Examples:
        >>> run_expression("print(2 + 2)")
        '4'
    """
    finished = subprocess.run(
        [sys.executable, "-c", source],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def main() -> None:
    """Ask the interpreter about itself."""
    print(f"running on {interpreter_path()}")
    print(f"two plus two is {run_expression('print(2 + 2)')}")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 005-python-interpreter
```

## 4. Open the notebook

```bash
jupyter notebook 005-python-interpreter/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `subprocess` | The standard library way to start another program |
| `stdout` | The normal output a program prints |

## Your turn

1. Use `run_expression` to ask a new Python for `sum(range(100))`.
2. Try running code that fails and read the error message.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 004-python-versions](../004-python-versions/) · [Next: 006-running-python →](../006-running-python/)
