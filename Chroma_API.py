import os
import chromadb
from chromadb.config import Settings
from Pdf_Process import extraer_texto_pdf
from Docx_Process import extraer_texto_docx

# Configuración de ChromaDB (local)
client = chromadb.PersistentClient(path="./chroma_storage")

# Crear una colección o acceder a una existente
collection = client.get_or_create_collection(name="documentos")

# Obtener todos los documentos guardados
documentos = collection.get()

# Mostrar resultados
print("Documentos almacenados en ChromaDB:")
for i in range(len(documentos["ids"])):
    print(f"\nID: {documentos['ids'][i]}")
    print(f"Texto: {documentos['documents'][i]}")
    print(f"Metadatos: {documentos['metadatas'][i]}")

def procesar_archivos_y_guardar():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    documentos = []

    for archivo in os.listdir(ruta_base):
        if archivo.endswith(".pdf"):
            texto = extraer_texto_pdf(os.path.join(ruta_base, archivo))
        elif archivo.endswith(".docx"):
            texto = extraer_texto_docx(os.path.join(ruta_base, archivo))
        else:
            continue

        documentos.append((archivo, texto))

    for nombre, contenido in documentos:
        collection.add(
            documents=[contenido],
            metadatas=[{"nombre": nombre}],
            ids=[nombre]  # Usamos el nombre del archivo como ID único
        )

    print(f"{len(documentos)} documentos procesados y almacenados en ChromaDB.")


if __name__ == "__main__":
    procesar_archivos_y_guardar()
