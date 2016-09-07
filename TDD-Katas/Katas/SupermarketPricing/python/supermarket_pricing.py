supermarket_items_prices = {
    'Can of Beans': 0.65,
    'Can of Tomatoes': 0.85
}


def get_supermarket_price(items):
    """ Calculate pricing """
    total = 0.0
    count_of_beans = 0
    count_of_tomatoes = 0
    for item_from_supermarket in supermarket_items_prices:
        for item in items:
            if item == 'Can of Beans':
                count_of_beans += 1
            else:
                count_of_tomatoes += 1

            if item == item_from_supermarket:
                if count_of_beans == 3:
                    total = 1.0
                if count_of_tomatoes == 3:
                    total -= supermarket_items_prices[item_from_supermarket]

                total += supermarket_items_prices[item_from_supermarket]
    return total
