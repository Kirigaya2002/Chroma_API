import fitz  # PyMuPDF
from processors.BaseProcessor import BaseProcessor

class PdfProcessor(BaseProcessor):
    def extract(self, file_path: str) -> str:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text