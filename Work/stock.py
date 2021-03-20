#!/usr/bin/env python
# stock.py
from typedproperty import String, Integer, Float

class Stock:
    # 限制属性名集合,访问其他属性会抛出异常
    #__slots__ = ('name', '_shares', 'price', '_change')
    #name = String('name') 
    #shares = Integer('shares') 
    #price = Float('price') 

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        #if not isinstance(value, int):
        #    raise TypeError('Expected int')
        self._shares = value
    
    @property
    def cost(self):
        return self.shares * self.price

    @property
    def change(self):
        return self._change
    
    @change.setter
    def change(self, value: float):
        self._change = value

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

