#!/usr/bin/python3

import csv
from collections import namedtuple


with open('/home/guess/PycharmProjects/PDFImport/ofxdownload.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        #process row

print (headings)
#print (Row)
