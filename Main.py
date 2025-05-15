from fastapi import FastAPI
from api.routes.document_routes import router as document_router

# Configuración de FastAPI
app = FastAPI(
    title="API de Procesamiento de Documentos",
    description="API para procesar y cargar documentos PDF y DOCX a Chroma DB",
    version="1.0",
)

# Registro de rutas
app.include_router(document_router, tags=["Documentos"])
