from typing import Dict, Type
from processors.BaseProcessor import BaseProcessor
from processors.Pdf_Process import PdfProcessor
from processors.Docx_Process import DocxProcessor

# Configuración de procesadores de documentos
DOCUMENT_PROCESSORS: Dict[str, Type[BaseProcessor]] = {
    ".pdf": PdfProcessor,
    ".docx": DocxProcessor
}

# Configuración de chunking de texto
TEXT_CHUNK_SIZE = 500
TEXT_CHUNK_OVERLAP = 50

# Configuración de API externa
CHROMA_API_URL = "http://vector-api:8001/store-chunks/"


# Configuración de archivos temporales
TEMP_FILE_PREFIX = "temp_"