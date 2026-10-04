"""Tests for Api-client-design."""

from lesson_682_api_client_design import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Api-client-design' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Api-client-design' still holds."""
    assert len(outline().splitlines()) == 3
