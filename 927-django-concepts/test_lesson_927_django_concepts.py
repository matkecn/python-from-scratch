"""Tests for Django-concepts."""

from lesson_927_django_concepts import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Django-concepts' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Django-concepts' still holds."""
    assert len(outline().splitlines()) == 3
