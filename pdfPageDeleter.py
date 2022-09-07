#!/usr/bin/python
from PyPDF2 import PdfWriter, PdfReader

import sys

oldFile = sys.argv[1]
pageNumber = int(sys.argv[2])
newFile = sys.argv[3]


pages_to_keep = [pageNumber] #important to note that page numbering starts at 0
infile = PdfReader(oldFile, 'rb') #read binary
output = PdfWriter()

for i in pages_to_keep:
    p = infile.pages[i]
    output.add_page(p)

with open(newFile, 'wb') as f: #write binary
    output.write(f)
