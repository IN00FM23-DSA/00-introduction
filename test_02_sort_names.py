"""
pytest test suite for Exercise 2 — Sort Names Alphabetically

Run with:
    pytest test_02_sort_names.py -v
"""

from _helpers import load_module

sort_names = load_module("02_sort_names.py").sort_names


class TestSortNames:

    def test_typical_list(self):
        assert sort_names(["Charlie", "Alice", "Bob", "Diana"]) == \
            ["Alice", "Bob", "Charlie", "Diana"]

    def test_already_sorted(self):
        assert sort_names(["Alice", "Bob"]) == ["Alice", "Bob"]

    def test_reverse_sorted(self):
        assert sort_names(["Charlie", "Bob", "Alice"]) == ["Alice", "Bob", "Charlie"]

    def test_single_name(self):
        assert sort_names(["Alice"]) == ["Alice"]

    def test_empty_list(self):
        assert sort_names([]) == []
