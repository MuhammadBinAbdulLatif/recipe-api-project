"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """
    Test the calc module"""
    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
    def test_subtract_number(self):
        """Test subtracting two numbers"""
        res = calc.subtract(50, 20)
        self.assertEqual(res, 30)
    def test_multiply_number(self):
        """Test multiplying two numbers"""
        res = calc.multiply(5, 6)
        self.assertEqual(res, 30)