"""
Definición de endpoints de la API.
"""

from fastapi import APIRouter, Request
from src.api.schemas import QuestionRequest, AnswerResponse

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Sports RAG Assistant API is running"}

@router.get("/health")
def health():
    """
    Endpoint de salud del sistema.
    """
    return {"status": "ok"}


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: Request, body: QuestionRequest):
    """
    Endpoint principal para consultar al sistema RAG.

    - request: objeto FastAPI (para acceder al estado de la app)
    - body: contiene la pregunta del usuario
    """
    rag_service = request.app.state.rag_service

    answer = rag_service.ask(body.question)

    return AnswerResponse(answer=answer)