#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                cur_count = int(record['shares'])
                cur_share = float(record['price'])
                total += cur_count * cur_share
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    print('Total cost', total)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_cost(filename)
