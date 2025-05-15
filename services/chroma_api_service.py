import requests
from typing import List, Dict
from config.settings import CHROMA_API_URL

class ChromaApiService:
    """Servicio para manejar la comunicación con la API de Chroma."""

    @staticmethod
    def send_chunks(chunks: List[Dict[str, str]]) -> None:
        """Envía los chunks procesados a la API de Chroma."""
        
        response = requests.post(
            CHROMA_API_URL,
            json=chunks,
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(f"Error al enviar documentos a la API: {response.text}")