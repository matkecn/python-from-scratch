# 304 · Decorator-factories

A decorator wraps a function to add behaviour.

**Section** Decorators, context managers, descriptors and introspection · **Level** 4 of 5 · **Time** about 40 minutes · **Status** generated draft (Phase 2)

## You will learn

- A decorator takes a function and gives a new one back
- `@` applies it
- `functools.wraps` keeps the name

## 1. Run the example

```bash
python 304-decorator-factories/lesson_304_decorator_factories.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_304_decorator_factories.py</code></summary>

```python
"""Decorator-factories.

A decorator wraps a function to add behaviour.

Run me:
    python 304-decorator-factories/lesson_304_decorator_factories.py
"""

from __future__ import annotations


from functools import wraps


def shouty(func):
    """Make a function's result louder.

    Args:
        func: The function to wrap.

    Returns:
        The wrapped function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Call the function and shout its result."""
        return str(func(*args, **kwargs)).upper()

    return wrapper


@shouty
def welcome(name: str) -> str:
    """Return a welcome message.

    Args:
        name: Who is arriving.

    Returns:
        A welcome message.
    """
    return f"welcome {name}"


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(welcome("Ada"))
    print(welcome.__name__)


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 304-decorator-factories
```

## 4. Open the notebook

```bash
jupyter notebook 304-decorator-factories/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `decorator` | A function that wraps another function |
| `wrapper` | The new function a decorator gives back |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 303-class-decorators](../303-class-decorators/) · [Next: 305-decorator-arguments →](../305-decorator-arguments/)
