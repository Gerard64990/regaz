#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import csv
import sys

filename=sys.argv[1]

def csv_from_excel(filename):
    wb = xlrd.open_workbook(filename+'.xlsx')
    sh = wb.sheet_by_name('Worksheet')
    your_csv_file = open(filename+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


csv_from_excel(filename)