from abc import ABC, abstractmethod
from typing import List, Dict

class DocumentHandler(ABC):
    """Interfaz abstracta para el manejo de documentos."""
    
    @abstractmethod
    def process_document(self, file_path: str) -> str:
        """Procesa un documento y extrae su texto."""
        pass
    
    @abstractmethod
    def chunk_text(self, text: str) -> List[str]:
        """Divide el texto en chunks."""
        pass
    
    @abstractmethod
    def format_chunks(self, filename: str, chunks: List[str]) -> List[Dict[str, str]]:
        """Formatea los chunks para su envío."""
        pass