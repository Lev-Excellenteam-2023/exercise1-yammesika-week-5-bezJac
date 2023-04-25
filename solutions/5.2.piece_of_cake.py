def get_recipe_price(prices, optionals=None, **kwargs):
    """
    Calculate the total cost of a recipe based on the ingredient prices and quantities specified.

    Args:
        prices (dict): A dictionary of ingredient prices (per 100 grams).
        optionals (list, optional): A list of optional ingredients to be excluded from the cost calculation.
                                    Defaults to an empty list.
        **kwargs (float): The quantities of each ingredient used in the recipe, specified as keyword arguments,
                           where the key is the ingredient name (str) and the value is the quantity (float).

    Returns:
        The total cost of the recipe, based on the ingredient prices and quantities specified.
    """
    if prices == {}:
        return 0

    if optionals is None:
        optionals = []

    total_sum = 0

    total_sum += sum((prices[ingredient] * (quantity / 100)) for ingredient, quantity in kwargs.items() if
                     ingredient not in optionals)

    return int(total_sum)


def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


if __name__ == "__main__":
    main()
