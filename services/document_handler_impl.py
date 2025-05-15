from typing import List, Dict
from interfaces.document_handler import DocumentHandler
from config.settings import DOCUMENT_PROCESSORS, TEXT_CHUNK_SIZE, TEXT_CHUNK_OVERLAP
import os

class DocumentHandlerImpl(DocumentHandler):
    """Implementación concreta del manejador de documentos."""

    def process_document(self, file_path: str) -> str:
        """Procesa un documento y extrae su texto utilizando el procesador apropiado."""
        ext = os.path.splitext(file_path)[1].lower()
        processor_class = DOCUMENT_PROCESSORS.get(ext)
        
        if not processor_class:
            raise ValueError(f"Extensión de archivo no soportada: {ext}")
        
        processor = processor_class()
        return processor.extract(file_path)
    
    def chunk_text(self, text: str) -> List[str]:
        """Divide el texto en chunks usando la configuración definida."""
        chunks = []
        start = 0
        
        while start < len(text):
            end = min(start + TEXT_CHUNK_SIZE, len(text))
            chunks.append(text[start:end])
            start += TEXT_CHUNK_SIZE - TEXT_CHUNK_OVERLAP
            
        return chunks
    
    def format_chunks(self, filename: str, chunks: List[str]) -> List[Dict[str, str]]:
        """Formatea los chunks para su envío a la API."""
        return [{
            "filename": filename,
            "chunk": chunk
        } for chunk in chunks]