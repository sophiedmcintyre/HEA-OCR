# HEA-OCR

### Purpose
This program (OCR_PDF.py) performs optical character recognition (OCR) on a PDF using the open-source Tesseract engine. It will specifically be used to OCR the Historic Education Archive (HEA) at James E. Walker Library. By OCR-ing these documents, we can provide better accessibility and open up more opportunities for textual analysis.

### Prerequisites
- pdf2image (converts PDF into multiple Python Image Library (PIL) objects)
- Pytesseract (OCR engine that converts PIL objects into PDFs)
- PyPDF2 (merges the OCRed PDFs into one OCRed PDF)

### Installation
Note: requires Python to be downloaded https://www.python.org/downloads/
```bash
pip install pdf2image
pip install pytesseract
pip install PyPDF2
!sudo apt-get install -y poppler-utils
```

### Workflow

![OCR Workflow](https://github.com/sophiedmcintyre/HEA-OCR/blob/25f981dc710a3690a08bb9dbfaa77ab12ebd818f/HEA%20OCR%20Workflow.png)

### Example
Enter the filename that you would like to OCR and provide a different filename for the output file

Note: the file variable below is the path of the input pdf. The path "./Book.pdf" means that the PDF (Book.pdf) is in the same directory as the program (OCR_PDF.py).

```python
file = "./Book.pdf" # input file
...
merger.write("Book-OCR.pdf") #output file
merger.close()
```

### Citations
This program was made with the help of a notebook on creating an OCR Workflow by Constellate (https://github.com/ithaka/tdm-notebooks/blob/4fd51b8dcd4eca40b2b9057dc4a569d786245d2e/ocr-workflow-1.ipynb)
