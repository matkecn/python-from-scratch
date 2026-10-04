"""Tests for Xml-etree."""

from lesson_496_xml_etree import keywords, outline


def test_has_keywords() -> None:
    """The promise of lesson 'Xml-etree' still holds."""
    assert len(keywords()) == 1


def test_has_three_steps() -> None:
    """The promise of lesson 'Xml-etree' still holds."""
    assert len(outline().splitlines()) == 3
