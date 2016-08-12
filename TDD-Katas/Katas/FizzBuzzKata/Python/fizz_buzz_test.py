import unittest
from fizz_buzz import fizz_buzz_it


class FizzBuzzTests(unittest.TestCase):

    def test_number_modulus_3_should_return_fizz(self):
        expected = "fizz"
        actual = fizz_buzz_it([3])
        self.assertEqual(expected, actual)
