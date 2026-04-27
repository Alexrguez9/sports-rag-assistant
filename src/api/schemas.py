"""
Modelos de datos para la API.
"""

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    """Modelo de entrada para preguntas."""
    question: str


class AnswerResponse(BaseModel):
    """Modelo de salida para respuestas."""
    answer: str