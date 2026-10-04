# 205 · Class-attributes

A class is a blueprint for making objects.

**Section** Object oriented programming · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- Classes group data and behaviour
- `self` is the object itself
- Call the class to make an object

## 1. Run the example

```bash
python 205-class-attributes/lesson_205_class_attributes.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_205_class_attributes.py</code></summary>

```python
"""Class-attributes.

A class is a blueprint for making objects.

Run me:
    python 205-class-attributes/lesson_205_class_attributes.py
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
pytest 205-class-attributes
```

## 4. Open the notebook

```bash
jupyter notebook 205-class-attributes/lesson.ipynb
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

[← 204-instance-attributes](../204-instance-attributes/) · [Next: 206-instance-methods →](../206-instance-methods/)
