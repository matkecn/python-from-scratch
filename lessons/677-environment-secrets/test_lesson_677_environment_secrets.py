"""Tests for Environment-secrets."""

from lesson_677_environment_secrets import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Environment-secrets' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Environment-secrets' still holds."""
    assert len(outline().splitlines()) == 3
