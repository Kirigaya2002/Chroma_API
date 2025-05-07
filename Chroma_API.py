import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import chromadb
from chromadb.config import Settings
from Pdf_Process import extraer_texto_pdf as extract_text_pdf
from Docx_Process import extraer_texto_docx as extract_text_docx

app = FastAPI()

# Configuración de ChromaDB (local)
client = chromadb.PersistentClient(path="./chroma_storage")

# Crear una colección o acceder a una existente
collection = client.get_or_create_collection(name="documentos")


@app.post("/process-docs/")
async def process_docs_and_save_in_chroma(files: list[UploadFile] = File(...)):
    documents = []

    for file in files:
        content = await file.read()
        file_path = f"./temp_{file.filename}"

        # Guardar archivo temporalmente
        with open(file_path, "wb") as temp_file:
            temp_file.write(content)

        # Procesar según el tipo de archivo
        if file.filename.endswith(".pdf"):
            text = extract_text_pdf(file_path)
        elif file.filename.endswith(".docx"):
            text = extract_text_docx(file_path)
        else:
            os.remove(file_path)
            return JSONResponse(
                content={"error": f"Unsupported file type: {file.filename}"},
                status_code=400,
            )

        documents.append((file.filename, text))
        os.remove(file_path)  # Eliminar archivo temporal

    # Guardar documentos en ChromaDB
    for name, content in documents:
        collection.add(
            documents=[content],
            metadatas=[{"nombre": name}],
            ids=[name]
        )

    return {"message": f"{len(documents)} documentos procesados y almacenados en ChromaDB."}


@app.get("/get-documents/")
def show_documents():
    # Obtener todos los documentos guardados
    documents = collection.get()

    # Formatear resultados
    result = []
    for i in range(len(documents["ids"])):
        result.append({
            "id": documents["ids"][i],
            "texto": documents["documents"][i],
            "metadatos": documents["metadatas"][i],
        })

    return {"documentos": result}
