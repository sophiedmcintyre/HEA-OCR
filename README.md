# HEA-OCR

### Purpose
This program performs optical character recognition (OCR) on a PDF using the open-source Tesseract engine. It will specifically be used to OCR the Historic Education Archive (HEA) at James E. Walker Library. By OCR-ing these documents, we can provide better accessibility and open up more opportunities for textual analysis.

### Prerequisites
- pdf2image (converts PDF into multiple Python Image Library (PIL) objects)
- Pytesseract (OCR engine that converts PIL objects into PDFs)
- PyPDF2 (merges the OCRed PDFs into one OCRed PDF)

### Installation
*requires Python to be downloaded https://www.python.org/downloads/
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

```python
file = "./BookTitle.pdf" # input file
...
merger.write("BookTitle-OCR.pdf") #output file
merger.close()
```
