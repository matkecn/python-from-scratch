"""Tests for Logging."""

from lesson_556_logging import make_logger, log_a_journey


def test_keeps_steps() -> None:
    """The promise of lesson 'Logging' still holds."""
    assert log_a_journey(["a", "b"]) == ["a", "b"]
