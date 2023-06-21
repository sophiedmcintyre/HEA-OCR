import enum
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfMerger

def ocr_func(fileName):
    # Input filename
    file = "/mnt/usershare/Needs Subcollection/" + fileName + ".pdf"


    # Get the file name without extension to use for output file
    # ex: ./Page.png turns to Page
    fileName = file.rsplit('/',1)[-1]
    fileName = fileName.rsplit('.',1)[0]
    # print(fileName)

    # PIL Converter
    PIL_objects = convert_from_path(file)

    # Initiates merger
    merger = PdfMerger()

    pdfs = []
    # Tesseract OCRs each image and converts it to a pdf
    # Each pdf is appended to a list
    for i, page in enumerate(PIL_objects):
        pdf = pytesseract.image_to_pdf_or_hocr(PIL_objects[i], extension='pdf')
        pdfs.append(pdf)

    # Merges each PDF from the list into one PDF
    for page in pdfs:
        with open(f'{fileName}-Page.pdf', 'w+b') as f:
            f.write(page)
            merger.append(f)
        
    # Output file
    merger.write("Book-OCR.pdf")
    merger.close()

        
    print("pdf done!!")

ocr_func("Name of File")
