import unittest
# from fizz_buzz import fizz_buzz_it
from supermarket_pricing import get_supermarket_price


class SupermarketPricingTests(unittest.TestCase):

    def test_returns_65_cents_for_one_can_of_beans(self):
        expected = 0.65
        actual = get_supermarket_price(['Can of Beans'])
        self.assertEqual(expected, actual)

    def test_returns_value_of_two_cans_of_beans(self):
        expected = 1.30
        actual = get_supermarket_price(['Can of Beans', 'Can of Beans'])
        self.assertEqual(expected, actual)

    def test_returns_value_of_one_can_of_tomatoes(self):
        expected = 0.85
        actual = get_supermarket_price(['Can of Tomatoes'])
        self.assertEqual(expected, actual)

    def test_returns_value_of_one_can_of_tomatoes_and_one_can_of_beans(self):
        expected = 0.85 + 0.65
        items = ['Can of Beans', 'Can of Tomatoes']
        actual = get_supermarket_price(items)
        self.assertEqual(expected, actual)

    def test_returns_value_of_one_can_of_tomatoes_and_two_cans_of_beans(self):
        expected = 0.85 + (2 * 0.65)
        items = ['Can of Beans', 'Can of Beans', 'Can of Tomatoes']
        actual = get_supermarket_price(items)
        self.assertEqual(expected, actual)

    def test_returns_value_when_getting_sales_price_for_three_for_a_dollar(self):
        expected = 1.00
        items = ['Can of Beans', 'Can of Beans', 'Can of Beans']
        actual = get_supermarket_price(items)
        self.assertEqual(expected, actual)

    def test_returns_value_when_getting_sales_price_for_three_for_a_dollar_and_extra_item(self):
        expected = 1.85
        items = ['Can of Beans', 'Can of Beans', 'Can of Tomatoes', 'Can of Beans']
        actual = get_supermarket_price(items)
        self.assertEqual(expected, actual)

    def test_returns_value_of_buy_two_get_one_free_for_can_of_tomatoes(self):
        expected = (2 * 0.85) + (2 * 0.65)
        items = ['Can of Beans', 'Can of Tomatoes', 'Can of Tomatoes', 'Can of Tomatoes', 'Can of Beans']
        actual = get_supermarket_price(items)
        self.assertEqual(expected, actual)

