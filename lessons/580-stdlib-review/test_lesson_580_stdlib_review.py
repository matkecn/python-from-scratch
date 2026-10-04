"""Tests for Stdlib-review."""

from lesson_580_stdlib_review import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Stdlib-review' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Stdlib-review' still holds."""
    assert len(outline().splitlines()) == 3
