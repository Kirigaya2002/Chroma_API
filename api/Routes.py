from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from services.Chroma_service import ChromaService
from services.Document_procesor import DocumentProcessor
from utils.File_utils import delete_temp_file
from utils.File_utils import save_temp_file

router = APIRouter()

# Instancias de servicios
doc_processor = DocumentProcessor()
chroma_service = ChromaService()

# Endpoint para almacenar documentos en ChromaDB
@router.post("/process-docs/")
async def process_docs_and_save_in_chroma(files: list[UploadFile] = File(...)):
    documents = []

    for file in files: 
        content = await file.read()
        file_path = save_temp_file(file.filename, content)

        try:
            text = doc_processor.extract_text(file_path) 
        except ValueError as e:
            delete_temp_file(file_path) 
            return JSONResponse(content={"error": str(e)}, status_code=400)

        documents.append((file.filename, text))
        delete_temp_file(file_path) 

    for name, content in documents:
        chroma_service.add_document(name, content)

    return {"message": f"{len(documents)} documentos procesados y almacenados en ChromaDB."}

# Endpoint para importar documentos en ChromaDB
@router.get("/get-documents/")
def show_documents():
    documents = chroma_service.get_all_documents()
    return {"documentos": documents}