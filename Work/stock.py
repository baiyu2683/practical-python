#!/usr/bin/env python
# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, sell):
        self.shares -= sell
        return self.shares
    def __repr__(self):
        name = self.name
        shares = self.shares
        price = self.price
        return f'Stock(\'{name}\', {shares}, {price})'

class MyStock(Stock):

    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        actual_cost = super().cost()
        return self.factor * actual_cost 

