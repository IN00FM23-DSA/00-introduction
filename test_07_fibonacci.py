"""
pytest test suite for Exercise 6 — Fibonacci Sequence

Run with:
    pytest test_07_fibonacci.py -v
"""

from _helpers import load_module

fibonacci = load_module("07_fibonacci.py").fibonacci


class TestFibonacci:

    def test_eight_numbers(self):
        assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

    def test_two_numbers(self):
        assert fibonacci(2) == [0, 1]

    def test_one_number(self):
        assert fibonacci(1) == [0]

    def test_five_numbers(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]

    def test_ten_numbers(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
