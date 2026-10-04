"""Tests for F-strings."""

from lesson_105_f_strings import price_line, progress


def test_formats_price() -> None:
    """The promise of lesson 'F-strings' still holds."""
    assert price_line("Tea", 2.5) == "Tea: 2.50"


def test_draws_progress() -> None:
    """The promise of lesson 'F-strings' still holds."""
    assert progress(2, 6) == "[##----]"
