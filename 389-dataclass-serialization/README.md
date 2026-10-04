# 389 · Dataclass-serialization

A dataclass writes the boring parts of a class for you.

**Section** Type hints, dataclasses and pattern matching · **Level** 3 of 5 · **Time** about 25 minutes · **Status** generated draft (Phase 2)

## You will learn

- `@dataclass` builds `__init__` for you
- Every field needs a type
- `frozen=True` stops changes

## 1. Run the example

```bash
python 389-dataclass-serialization/lesson_389_dataclass_serialization.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_389_dataclass_serialization.py</code></summary>

```python
"""Dataclass-serialization.

A dataclass writes the boring parts of a class for you.

Run me:
    python 389-dataclass-serialization/lesson_389_dataclass_serialization.py
"""

from __future__ import annotations


from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """A point on a grid."""

    x: int
    y: int

    def distance_from_origin(self) -> float:
        """Return how far the point is from ``0, 0``.

        Returns:
            The distance, as a float.
        """
        return (self.x**2 + self.y**2) ** 0.5


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    point = Point(3, 4)
    print(point)
    print(round(point.distance_from_origin(), 2))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 389-dataclass-serialization
```

## 4. Open the notebook

```bash
jupyter notebook 389-dataclass-serialization/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `dataclass` | A class that generates its own `__init__` |

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/typing.html)

---

[← 388-dataclass-comparison](../388-dataclass-comparison/) · [Next: 390-dataclass-patterns →](../390-dataclass-patterns/)
