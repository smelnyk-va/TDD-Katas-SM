import unittest
from HarryPotter import calculate_cost_of_books_purchased


class HarryPotterTests(unittest.TestCase):

    def test_buy_one_copy_of_first_book_should_cost_8_euros(self):
        num_of_books = 1
        different_book_titles = 1
        expected_cost = 8
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)

    def test_buy_two_copies_of_first_book_should_cost_16_euros(self):
        num_of_books = 2
        different_book_titles = 1
        expected_cost = 16
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)

    def test_buy_two_books_of_two_different_names_should_give_5_percent_discount(self):
        num_of_books = 2
        different_book_titles = 2
        expected_cost = 15.2  # (8*2) - ((8*2) * 0.05)
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)

    def test_buy_one_book_of_two_different_names_should_give_5_percent_discount(self):
        num_of_books = 3
        different_book_titles = 2
        expected_cost = 22.8  # (8*2) - ((8*2) * 0.05)
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)

    def test_buy_three_books_of_one_names_should_give_10_percent_discount(self):
        num_of_books = 3
        different_book_titles = 3
        expected_cost = 21.6  # (8*3) - ((8*3) * 0.10)
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)

    def test_buy_four_books_of_one_names_should_give_15_percent_discount(self):
        num_of_books = 4
        different_book_titles = 4
        expected_cost = 27.2  # (8*4) - ((8*4) * 0.15)
        print expected_cost
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        print actual
        self.assertEqual(expected_cost, actual)

    def test_buy_five_books_of_one_names_should_give_25_percent_discount(self):
        num_of_books = 5
        different_book_titles = 5
        expected_cost = 30.0  # (8*5) - ((8*5) * 0.25)
        actual = calculate_cost_of_books_purchased(num_of_books, different_book_titles)
        self.assertEqual(expected_cost, actual)
