#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import sys
import csv
import fileparse

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as file:
        portfolio = fileparse.parse_csv(file, selects=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [list(record.values()) for record in portfolio]
    return portfolio

def read_price(filename: str) -> dict:
    '''读取csv文件内容，存储到一个map中'''
    prices = {}
    with open(filename, 'rt') as file:
        prices = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    return prices

def make_report(portfolio: list, prices: dict):
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
    report = make_report(portfolio, dict(prices))
    print_report(report)

def main(filenames: list):
    portfolio_report(filenames[0], filenames[1]) 

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError('参数长度不够')
    main([sys.argv[1], sys.argv[2]])
