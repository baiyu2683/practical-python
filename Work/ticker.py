#!/usr/bin/env python
# ticker.py

from follow import follow
import csv
import report
import stock

def make_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for val, func in zip(row, types)]

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
    

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    portfolio = report.read_portfolio(portfile)
    #rows = filter_symbols(rows, portfolio)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = report.create_formatter(fmt)
    headers = ['Name', 'Price', 'Change']
    formatter.headings(headers)
    for row in rows:
        st = stock.Stock(row['name'], 0, row['change'])
        st.change = row['change']
        formatter.row(st, headers)


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

