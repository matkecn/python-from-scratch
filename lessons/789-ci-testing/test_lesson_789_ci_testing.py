"""Tests for Ci-testing."""

from lesson_789_ci_testing import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Ci-testing' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Ci-testing' still holds."""
    assert len(outline().splitlines()) == 3
