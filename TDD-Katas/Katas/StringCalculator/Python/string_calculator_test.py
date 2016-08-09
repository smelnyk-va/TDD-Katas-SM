__author__ = 'smelnyk'

import unittest
from string_calculator import StringCalculator


class StringCalculatorAddTests(unittest.TestCase):

    def test_add_should_return_sum_of_0_for_empty_string(self):
        expected = 0
        actual = StringCalculator.string_add("")
        self.assertEqual(expected, actual)
