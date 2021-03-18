#!/usr/bin/env python
# tableformat.py

class TableFormatter:
    def headings(self, headers: list):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata: list, colnames: list=None):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class PlainTextFormatter(TableFormatter):
    def headings(self, headers: list):
        for header in headers:
            print('{:>10s} '.format(header), end='')
        print()
        print('---------- ' * len(headers))

    def row(self, rowdata: list, colnames: list=None):
        for colname in colnames:
            if hasattr(rowdata, colname):
                print('{:>10s} '.format(str(getattr(rowdata, colname))), end='')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join([str(s) for s in rowdata]))
