import unittest
from HarryPotter import calculate_cost_of_books_purchased


class HarryPotterTests(unittest.TestCase):

    def test_buy_one_copy_of_first_book_should_cost_8_euros(self):
        expected = 8
        actual = calculate_cost_of_books_purchased(1, 1)
        self.assertEqual(expected, actual)

    def test_buy_two_copies_of_first_book_should_cost_16_euros(self):
        expected = 16
        actual = calculate_cost_of_books_purchased(2, 1)
        self.assertEqual(expected, actual)

    def test_buy_one_book_of_two_different_names_should_give_5_percent_discount(self):
        expected = 14.4  # (16 * 2) * 0.05 = 1.6 (Discount) (16 - 1.6 = 14.4)
        actual = calculate_cost_of_books_purchased(2, 2)
        self.assertEqual(expected, actual)
