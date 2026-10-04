# 006 · Running-python

Three ways to run Python: a file, a line, or the prompt.

**Section** Getting started and first programs · **Level** 1 of 5 · **Time** about 10 minutes · **Status** hand written

## You will learn

- Run a whole file with `python file.py`
- Run one line with `python -c`
- Keep a tiny script and run it again and again

## 1. Run the example

```bash
python 006-running-python/lesson_006_running_python.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_006_running_python.py</code></summary>

```python
"""Running Python.

Three doors into Python: a file, a single line, or the interactive prompt.

Run me:
    python 006-running-python/lesson_006_running_python.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT = '"""A tiny script."""\n\nprint("the script ran")\n'


def run_line(source: str) -> str:
    """Run one line of Python and return what it printed.

    Args:
        source: The code to run.

    Returns:
        The output, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the code fails.

    Examples:
        >>> run_line("print(6 * 7)")
        '42'
    """
    finished = subprocess.run(
        [sys.executable, "-c", source],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def write_script(path: str) -> Path:
    """Write a tiny script to disk.

    Args:
        path: Where to write it.

    Returns:
        The path that was written.
    """
    target = Path(path)
    target.write_text(SCRIPT, encoding="utf-8")
    return target


def run_script(path: str) -> str:
    """Run a script file and return what it printed.

    Args:
        path: The script to run.

    Returns:
        The output, without the final newline.

    Raises:
        subprocess.CalledProcessError: If the script fails.

    Examples:
        >>> import tempfile, os
        >>> folder = tempfile.mkdtemp()
        >>> target = write_script(os.path.join(folder, "tiny.py"))
        >>> run_script(str(target))
        'the script ran'
    """
    finished = subprocess.run(
        [sys.executable, path],
        capture_output=True,
        text=True,
        check=True,
    )
    return finished.stdout.strip()


def main() -> None:
    """Show all three ways to run Python."""
    import tempfile
    from pathlib import Path as RealPath

    print(f"one line says: {run_line('print(1 + 1)')}")
    target = write_script(str(RealPath(tempfile.mkdtemp()) / "demo.py"))
    print(f"the file says: {run_script(str(target))}")


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 006-running-python
```

## 4. Open the notebook

```bash
jupyter notebook 006-running-python/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `script` | A file of Python instructions you can run |
| `argument` | A value you hand to a program |

## Your turn

1. Save your own `first.py` and run it with `python first.py`.
2. Run the same script twice and notice nothing changes.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/interpreter.html)

---

[← 005-python-interpreter](../005-python-interpreter/) · [Next: 007-python-repl →](../007-python-repl/)
