"""A shopping cart that uses the products module from the same package."""

from .products import get_price


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(get_price(item) for item in self.items)
