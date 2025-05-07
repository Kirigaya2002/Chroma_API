import os
from processors.Pdf_Process import PdfProcessor
from processors.Docx_Process import DocxProcessor

class DocumentProcessor:

    # Constructor de la clase DocumentProcessor
    # Inicializa los procesadores de documentos para diferentes tipos de archivos
    def __init__(self):
        self.processors = {
            ".pdf": PdfProcessor(),
            ".docx": DocxProcessor()
        }

    # Extraer texto de un archivo con la ruta del archivo
    def extract_text(self, filepath: str) -> str:
        ext = os.path.splitext(filepath)[1].lower()
        processor = self.processors.get(ext)
        if not processor:
            raise ValueError(f"Extension de archivo insorportada: {ext}")
        return processor.extract(filepath)
