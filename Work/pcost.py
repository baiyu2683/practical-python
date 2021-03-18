#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):
    total = 0
    portfolio = report.read_portfolio(filename)
    for no, record in enumerate(portfolio, start=1):
        try:
            cur_share = record.shares
            cur_price = record.price
            total += cur_share * cur_price
        except ValueError as e:
            print(f'Row {no}: Bad row: {record}', e)
    print('Total cost', total)

def main(argvs: list):
    if len(argvs) == 2:
        filename = argvs[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio_cost(filename)
    
if __name__ == '__main__':
   main(sys.argv)     
