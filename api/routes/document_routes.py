from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List

from services.document_handler_impl import DocumentHandlerImpl
from services.temp_file_service import TempFileService
from services.chroma_api_service import ChromaApiService

router = APIRouter()
doc_handler = DocumentHandlerImpl()
temp_service = TempFileService()

@router.post("/upload-docs/")
async def upload_docs(files: List[UploadFile] = File(...)):
    """Endpoint para procesar documentos y enviarlos a la API de Chroma."""
    try:
        # Guardar archivos temporales
        temp_files = []
        for file in files:
            content = await file.read()
            temp_file = temp_service.save_temp_file(file.filename, content)
            temp_files.append(temp_file)

        all_chunks = []
        # Procesar cada documento
        for file, temp_file in zip(files, temp_files):
            # Extraer y procesar el texto
            extracted_text = doc_handler.process_document(temp_file)
            text_chunks = doc_handler.chunk_text(extracted_text)
            formatted_chunks = doc_handler.format_chunks(file.filename, text_chunks)
            all_chunks.extend(formatted_chunks)

        # Limpiar archivos temporales
        temp_service.delete_temp_files(temp_files)

        # Imprimir los chunks en formato JSON
        print("Chunks en formato JSON:")
        print(all_chunks)
        # Enviar chunks a la API de Chroma
        ChromaApiService.send_chunks(all_chunks)

        return JSONResponse(
            content={"message": "Documentos procesados y enviados correctamente"},
            status_code=200
        )

    except Exception as e:
        # Asegurar limpieza de archivos temporales en caso de error
        temp_service.delete_temp_files(temp_files)
        return JSONResponse(
            content={"message": str(e)},
            status_code=500
        )