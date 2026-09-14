"""
pytest test suite for Exercise 5 — Average Grade

Run with:
    pytest test_05_average_grades.py -v
"""

import pytest

from _helpers import load_module

average_grades = load_module("05_average_grades.py").average_grades


class TestAverageGrades:

    def test_typical_list(self):
        assert average_grades([85, 92, 78, 90, 88]) == pytest.approx(86.6)

    def test_single_grade(self):
        assert average_grades([100]) == 100

    def test_all_same_grades(self):
        assert average_grades([50, 50, 50]) == 50

    def test_two_grades(self):
        assert average_grades([80, 90]) == 85

    def test_returns_a_float(self):
        assert isinstance(average_grades([70, 80]), float)
