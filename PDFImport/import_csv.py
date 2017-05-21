#!/usr/bin/python3

import csv

with open('/home/guess/PycharmProjects/PDFImport/ofxdownload.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
#    for row in f_csv:
        # process row

#print(f_csv)
print(headers)
#print('\n')
print(headers[1] +'\n')
