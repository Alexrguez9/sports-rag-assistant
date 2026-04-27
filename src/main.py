"""
Punto de entrada de la API.

Inicializa la aplicación FastAPI y configura el ciclo de vida
del servicio RAG.
"""

from fastapi import FastAPI
from src.api.routes import router
from src.services.rag_service import RAGService

app = FastAPI(title="Sports RAG Assistant API")


@app.on_event("startup")
def startup_event():
    """
    Inicializa el servicio RAG al arrancar la aplicación.
    """
    app.state.rag_service = RAGService()


app.include_router(router)