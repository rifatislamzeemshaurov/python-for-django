"""Product prices for our tiny shop."""

PRICES = {
    "pen": 20,
    "notebook": 120,
    "backpack": 1800,
}


def get_price(product):
    return PRICES.get(product, 0)
