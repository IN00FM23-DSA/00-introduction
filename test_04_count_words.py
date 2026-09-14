"""
pytest test suite for Exercise 4 — Count Words

Run with:
    pytest test_04_count_words.py -v
"""

from _helpers import load_module

count_words = load_module("04_count_words.py").count_words


class TestCountWords:

    def test_typical_sentence(self):
        assert count_words("Hello world this is Python") == 5

    def test_single_word(self):
        assert count_words("Hello") == 1

    def test_extra_spaces_between_words(self):
        assert count_words("Hello    world") == 2

    def test_leading_and_trailing_spaces(self):
        assert count_words("  Hello world  ") == 2

    def test_empty_string(self):
        assert count_words("") == 0
