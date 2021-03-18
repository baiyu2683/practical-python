#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import sys
import csv
import fileparse
import stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as file:
        portfolio = fileparse.parse_csv(file, selects=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [list(record.values()) for record in portfolio]
    portfolio = [stock.Stock(record[0], record[1], record[2]) for record in portfolio]
    return Portfolio(portfolio)

def read_price(filename: str) -> dict:
    '''读取csv文件内容，存储到一个map中'''
    prices = {}
    with open(filename, 'rt') as file:
        prices = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    return prices

def make_report(portfolio: list, prices: dict):
    report = []
    for record in portfolio:
        name = record.name
        if name in prices:
            cur_price = prices[name]
            record.change = round(cur_price - record.price, 2)
        report.append(record)
    return report

def print_report(report, formatter):
    headers = ('Name', 'Shares', 'Price', 'Change')
    formatter.headings(headers)
    for row in report:
        formatter.row(row, headers)

class UnknownTableFormatError(Exception):
    pass

def create_formatter(name: str) -> tableformat.TableFormatter:
    if name == 'txt':
        return tableformat.PlainTextFormatter()
    elif name == 'csv':
        return tableformat.CSVTableFormatter()
    else:
        raise UnknownTableFormatError(f'Unknown format {name}')

def portfolio_report(filename1: str, filename2: str, fmt: str='txt') -> None:
    portfolio = read_portfolio(filename1)
    prices = read_price(filename2)
    report = make_report(portfolio, dict(prices))
    formatter = create_formatter(fmt)
    print_report(report,formatter)

def print_table(report: list, colnames: list, formatter: tableformat.TableFormatter):
    formatter.headings(tuple(colnames))
    for row in report:
        formatter.row(row, colnames)

def main(filenames: list):
    portfolio_report(filenames[0], filenames[1]) 

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise ValueError('参数长度不够')
    main([sys.argv[1], sys.argv[2]])
