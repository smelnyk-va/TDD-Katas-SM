"""
To try and encourage more sales of the 5 different Harry
Potter books they sell, a bookshop has decided to offer
discounts of multiple-book purchases.

One copy of any of the five books costs 8 EUR.

If, however, you buy two different books, you get a 5%
discount on those two books.

If you buy 3 different books, you get a 10% discount.

If you buy 4 different books, you get a 20% discount.

If you go the whole hog, and buy all 5, you get a huge 25%
discount.

Note that if you buy, say, four books, of which 3 are
different titles, you get a 10% discount on the 3 that
form part of a set, but the fourth book still costs 8 EUR.

Your mission is to write a piece of code to calculate the
price of any conceivable shopping basket (containing only
Harry Potter books), giving as big a discount as possible.

For example, how much does this basket of books cost?

2 copies of the first book
2 copies of the second book
2 copies of the third book
1 copy of the fourth book
1 copy of the fifth book

Answer: 51.60 EUR
"""


def calculate_cost_of_books_purchased(num_of_books, num_of_different_titles):
    """ My first attempt at this function, made it too generic """

    cost_of_one_book = 8
    initial_cost_for_books = num_of_books * cost_of_one_book

    if num_of_different_titles == 2:
        discount = 0.05
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost

    elif num_of_different_titles == 3:
        discount = 0.10
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost

    elif num_of_different_titles == 4:
        discount = 0.15
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost

    elif num_of_different_titles == 5:
        discount = 0.25
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost

    else:
        total_cost = initial_cost_for_books * num_of_different_titles

    return total_cost


def calculate_cost_of_books_purchased_individual(num_of_books, num_of_book_one, num_of_book_two, num_of_book_three, num_of_book_four, num_of_book_five):
    """ My second attempt at this function - passing in individual books this time """

    cost_of_one_book = 8
    initial_cost_for_books = num_of_books * cost_of_one_book

    num_of_different_book_titles = 0

    if num_of_book_one >= 1:
        num_of_different_book_titles += 1
    if num_of_book_two >= 1:
        num_of_different_book_titles += 1
    if num_of_book_three >= 1:
        num_of_different_book_titles += 1
    if num_of_book_four >= 1:
        num_of_different_book_titles += 1
    if num_of_book_five >= 1:
        num_of_different_book_titles += 1

    if num_of_different_book_titles == 2:
        discount = 0.05
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost
    elif num_of_different_book_titles == 3:
        discount = 0.10
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost
    elif num_of_different_book_titles == 4:
        discount = 0.15
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost
    elif num_of_different_book_titles == 5:
        discount = 0.25
        discount_cost = initial_cost_for_books * discount
        total_cost = initial_cost_for_books - discount_cost
    else:
        total_cost = initial_cost_for_books

    return total_cost

