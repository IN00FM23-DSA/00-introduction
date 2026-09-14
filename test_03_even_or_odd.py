"""
pytest test suite for Exercise 3 — Even or Odd

Run with:
    pytest test_03_even_or_odd.py -v
"""

from _helpers import load_module

even_or_odd = load_module("03_even_or_odd.py").even_or_odd


class TestEvenOrOdd:

    def test_even_number(self):
        assert even_or_odd(42) == "even"

    def test_odd_number(self):
        assert even_or_odd(7) == "odd"

    def test_zero_is_even(self):
        assert even_or_odd(0) == "even"

    def test_negative_even(self):
        assert even_or_odd(-4) == "even"

    def test_negative_odd(self):
        assert even_or_odd(-3) == "odd"
