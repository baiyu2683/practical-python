#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = (record['name'], int(record['shares']), float(record['price']))
            portfolio.append(holding)
    return portfolio

def read_price(filename: str) -> dict:
    '''读取csv文件内容，存储到一个map中'''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices[name] = float(price)
            except ValueError as e:
                pass
    return prices

def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        name, shares, price = row
        if name in prices:
            cur_price = prices[name]
            report.append((name, shares, cur_price, cur_price - price))
    return report

def print_report(report):
    name, share, price, change = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(name, share, price, change))
    print('-'*10, '-'*10, '-'*10, '-'*10)
    for name, share, price, change in report:
        price = '$' + f'{price:0.2f}'
        print(f'{name:>10s} {share:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(filename1: str, filename2: str) -> None:
    portfolio = read_portfolio(filename1)
    prices = read_price(filename2)
    report = make_report(portfolio, prices)
    print(report)
