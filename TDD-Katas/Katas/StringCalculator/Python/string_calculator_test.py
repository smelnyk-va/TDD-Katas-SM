# coding=utf-8
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

    def test_add_should_return_sum_equal_to_the_sum_of_3_numbers_given_separated_by_a_comma(self):
        expected = 10
        actual = StringCalculator.string_add("2, 3, 5")
        self.assertEqual(expected, actual)

    def test_add_should_return_sum_equal_to_the_sum_of_multiple_numbers_separated_by_a_newline(self):
        expected = 10
        actual = StringCalculator.string_add("5\n5")
        self.assertEqual(expected, actual)

    def test_add_should_return_sum_equal_to_the_sum_of_multiple_numbers_separated_by_a_newline_and_a_comma(self):
        expected = 6
        actual = StringCalculator.string_add("1\n2,3")
        self.assertEqual(expected, actual)

    """ Upcoming Tests/Code that needs to be written/handled """
    # Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that
    # was passed.if there are multiple negatives, show all of them in the exception message

    # Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2

    # Delimiters can be of any length with the following format: "//[delimiter]\n" for example: "//[***]\n1***2***3" = 6

    # When done the above, write a substract function and follow the same kind of steps!
