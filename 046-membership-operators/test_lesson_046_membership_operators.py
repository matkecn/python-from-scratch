"""Tests for Membership-operators."""

from lesson_046_membership_operators import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Membership-operators' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Membership-operators' still holds."""
    assert len(outline().splitlines()) == 3
