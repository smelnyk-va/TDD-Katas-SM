__author__ = 'smelnyk'

import unittest
from string_calculator import StringCalculator


class StringCalculatorAddTests(unittest.TestCase):

    def test_add_should_return_sum_of_0_for_empty_string(self):
        expected = 0
        actual = StringCalculator.string_add("")
        self.assertEqual(expected, actual)

    def test_add_should_return_sum_equal_to_string_given_if_string_only_contains_1_number(self):
        expected = 3
        actual = StringCalculator.string_add("3")
        self.assertEqual(expected, actual)

    def test_add_should_return_sum_equal_to_the_sum_of_2_numbers_given_separated_by_a_comma(self):
        expected = 5
        actual = StringCalculator.string_add("2, 3")
        self.assertEqual(expected, actual)
