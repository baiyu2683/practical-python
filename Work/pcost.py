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
            cur_count = int(record[1])
            cur_share = float(record[2])
            total += cur_count * cur_share
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
