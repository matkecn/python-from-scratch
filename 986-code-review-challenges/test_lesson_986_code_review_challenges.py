"""Tests for Code-review-challenges."""

from lesson_986_code_review_challenges import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Code-review-challenges' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Code-review-challenges' still holds."""
    assert len(outline().splitlines()) == 3
