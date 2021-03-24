# pip install PyPDF2

import PyPDF2

# rb means read binary
f = open('test.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)

# Check how many pages the PDF file has
pdf_reader.numPages

# get the first page
page_one = pdf_reader.getPage(0)
# get the text from page one
page_one_text = page_one.extractText()

f.close()