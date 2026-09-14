"""
pytest test suite for Exercise 7 — Caesar Cipher

Run with:
    pytest test_08_caesar_cipher.py -v
"""

from _helpers import load_module

caesar_cipher = load_module("08_caesar_cipher.py").caesar_cipher


class TestCaesarCipher:

    def test_typical_message(self):
        assert caesar_cipher("Hello World", 3) == "Khoor Zruog"

    def test_lowercase_wraps_around_z(self):
        assert caesar_cipher("xyz", 3) == "abc"

    def test_uppercase_wraps_around_z(self):
        assert caesar_cipher("XYZ", 3) == "ABC"

    def test_non_letters_are_unchanged(self):
        assert caesar_cipher("Hi, 007!", 5) == "Mn, 007!"

    def test_shift_of_zero_returns_same_text(self):
        assert caesar_cipher("Same Text", 0) == "Same Text"
