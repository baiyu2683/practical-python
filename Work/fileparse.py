#!/usr/bin/env python3
# fileparse.py
#
# Exercise 3.3
import csv
import io
import logging

logging.basicConfig(
    filename = 'app.log',
    filemode='w',
    level = logging.WARNING,
)
log = logging.getLogger(__name__)

def parse_csv(content, selects: list=None, types: list=None, has_headers: bool=True, delimiter: str=',', **opts) -> list:
    '''
    解析csv文件，并存到list中
    content: 文件或者可迭代类型
    select: 列名
    types: 解析的列的类型
    has_headers: 是否有标题
    delimiter: csv文件数据分隔符
    '''
    silence_errors = False
    if 'silence_errors' in opts:
        silence_errors = opts['silence_errors']
    
    rows = csv.reader(content, delimiter=delimiter)
        
    print('row', rows)
    if has_headers:
        headers = next(rows)
    else:
        headers = []
    print('headers', headers)
    select_index = []
    if has_headers and selects:
        select_index = [headers.index(select) for select in selects]
        headers = [header for index, header in enumerate(headers) if index in select_index]

    if types and select_index:
        types = [types[index] for index in select_index]
    print('select_index', select_index)
    print('types', types)
    print('headers', headers)
    records = []
    for index, row in enumerate(rows):
        if not row:
            continue
        if select_index:
            row = [row[index] for index in select_index]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except Exception as e:
                if not silence_errors:
                    log.warning('row %d: Couldn\'t convert %s', index, row)
                    log.debug('Row %d: Reason %s', index, e)
        if has_headers:
             record = dict(zip(headers, row))
        else:
             record = tuple(row)
        records.append(record)

    return records

