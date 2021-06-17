# Invokation: python3 mergePDF.py file1.pdf file2.pdf file3.pdf ...

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('super.pdf')
    print("PDFs merged!!")


pdf_combiner(inputs)
