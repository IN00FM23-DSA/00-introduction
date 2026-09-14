"""
pytest test suite for Exercise 1 — Find the Largest Number

Run with:
    pytest test_01_find_largest.py -v
"""

from _helpers import load_module

find_largest = load_module("01_find_largest.py").find_largest


class TestFindLargest:

    def test_typical_list(self):
        assert find_largest([3, 7, 2, 9, 4]) == 9

    def test_largest_at_start(self):
        assert find_largest([10, 2, 3]) == 10

    def test_largest_at_end(self):
        assert find_largest([1, 2, 3, 100]) == 100

    def test_all_negative_numbers(self):
        assert find_largest([-5, -1, -9, -3]) == -1

    def test_single_element(self):
        assert find_largest([42]) == 42
