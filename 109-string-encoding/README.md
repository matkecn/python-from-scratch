# 109 · String-encoding

Strings are text, and text is written between quotes.

**Section** Strings, encodings and regular expressions · **Level** 2 of 5 · **Time** about 15 minutes · **Status** generated draft (Phase 2)

## You will learn

- Join strings with `+`
- Use f-strings to place values inside text
- Strings cannot be changed

## 1. Run the example

```bash
python 109-string-encoding/lesson_109_string_encoding.py
```

## 2. Read the code

<details>
<summary>Show <code>lesson_109_string_encoding.py</code></summary>

```python
"""String-encoding.

Strings are text, and text is written between quotes.

Run me:
    python 109-string-encoding/lesson_109_string_encoding.py
"""

from __future__ import annotations


def shout(text: str) -> str:
    """Return the text in upper case.

    Args:
        text: The text to shout.

    Returns:
        The same text, louder.

    Examples:
        >>> shout("hello")
        'HELLO'
    """
    return text.upper()


def count_words(sentence: str) -> int:
    """Count how many words are in a sentence.

    Args:
        sentence: The sentence to measure.

    Returns:
        The number of words.

    Examples:
        >>> count_words("a b c")
        3
    """
    return len(sentence.split())


def initials(name: str) -> str:
    """Return the initials of a full name.

    Args:
        name: A name such as ``"Ada Lovelace"``.

    Returns:
        The initials in upper case.

    Examples:
        >>> initials("Ada Lovelace")
        'AL'
    """
    return "".join(part[0] for part in name.split()).upper()


def main() -> None:
    """Print a small demo so the lesson is runnable."""
    print(shout("hello"))
    print(count_words("one two three"))
    print(initials("Ada Lovelace"))


if __name__ == "__main__":
    main()
```

</details>

## 3. Run the tests

```bash
pytest 109-string-encoding
```

## 4. Open the notebook

```bash
jupyter notebook 109-string-encoding/lesson.ipynb
```

## Words to remember

| word | meaning |
| --- | --- |
| `string` | Text made of characters |
| `immutable` | Cannot be changed after it is made |

## Your turn

1. Write a function that counts the vowels in a word.

## Read more

- [official tutorial](https://docs.python.org/3/tutorial/strings.html)

---

[← 108-multiline-strings](../108-multiline-strings/) · [Next: 110-unicode →](../110-unicode/)
