"""Tests for Backup-tool."""

from lesson_948_backup_tool import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Backup-tool' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Backup-tool' still holds."""
    assert len(outline().splitlines()) == 3
