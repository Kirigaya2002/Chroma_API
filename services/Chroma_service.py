from chromadb import PersistentClient
from uuid import uuid4

class ChromaService:

    # Inicializacion del cliente de ChromaDB y la colección
    def __init__(self):
        self.client = PersistentClient(path="./chroma_storage")
        self.collection = self.client.get_or_create_collection(name="documentos")

    # Procesa y guarda documentos en ChromaDB
    def add_document(self, filename: str, content: str):
        doc_id = str(uuid4())  # Genera un ID único para el documento
        self.collection.add(
            documents=[content],
            metadatas=[{"nombre": filename}],
            ids=[doc_id]
        )

    # Muestra todos los documentos en ChromaDB
    def get_all_documents(self):
        documents = self.collection.get()
        result = []
        for i in range(len(documents["ids"])):
            result.append({
                "id": documents["ids"][i],
                "texto": documents["documents"][i],
                "metadatos": documents["metadatas"][i],
            })
        return result