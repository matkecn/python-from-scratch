"""Tests for Api-client-project."""

from lesson_690_api_client_project import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-client-project' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-client-project' still holds."""
    assert len(outline().splitlines()) == 3
