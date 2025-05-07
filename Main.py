from fastapi import FastAPI
from api.Routes import router as api_router

# Configuración de FastAPI
app = FastAPI(title="Chroma API", description="API para procesar y almacenar documentos en ChromaDB", version="1.0")

# Rutas de la api
app.include_router(api_router)
