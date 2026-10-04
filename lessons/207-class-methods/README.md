# 207 · Class-methods

A class is a blueprint for making objects.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Classes group data and behaviour
- `self` is the object itself
- Call the class to make an object

## 1. Run the example

```bash
python 207-class-methods/lesson_207_class_methods.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_207_class_methods.py</code></summary>

```python
"""Class-methods.

A class is a blueprint for making objects.

Run me:
    python 207-class-methods/lesson_207_class_methods.py
"""

from __future__ import annotations


class Dog:
    """A simple dog that can bark."""

    def __init__(self, name: str) -> None:
        """Give the dog a name.

        Args:
            name: The dog's name.
        """
        self.name = name

    def bark(self) -> str:
        """Return what the dog says.

        Returns:
            A bark that uses the dog's name.
        """
        return f"{self.name} says woof"


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    dog = Dog("Rex")
    print(dog.bark())


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 207-class-methods
```

## 4. Open the notebook

```bash
jupyter notebook 207-class-methods/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `class` | A blueprint for objects |
| `object` | One thing made from a class |
| `self` | The object a method is called on |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/classes.html)

---

[← 206-instance-methods](../206-instance-methods/) · [Next: 208-static-methods →](../208-static-methods/)
