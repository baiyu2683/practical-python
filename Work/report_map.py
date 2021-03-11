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
            holding = {'name': row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

#if len(sys.argv) == 2:
 #   filename = sys.argv[1]
#else:
 #   filename = 'Data/portfolio.csv'

