"""Tests for Pep-process."""

from lesson_889_pep_process import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Pep-process' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Pep-process' still holds."""
    assert len(outline().splitlines()) == 3
