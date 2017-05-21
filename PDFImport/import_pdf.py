#!/usr/bin/python

import PyPDF2

pdfFileObj = open('/home/guess/PycharmProjects/PDFImport/NIST800-128.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)
