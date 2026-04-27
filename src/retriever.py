"""
Módulo encargado de la búsqueda semántica.
"""

import numpy as np
from openai import OpenAI
from src.core.config import OPENAI_API_KEY, EMBEDDING_MODEL, TOP_K
from src.core.logger import logger

client = OpenAI(api_key=OPENAI_API_KEY)


def get_embedding(text: str):
    """Devuelve el embedding de un texto."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding


class Retriever:
    """Realiza búsqueda semántica sobre un conjunto de textos."""

    def __init__(self, chunks=None, embeddings=None):
        """Inicializa el retriever con datos opcionales."""
        self.chunks = chunks
        self.embeddings = embeddings

    def build(self, chunks):
        """Genera embeddings para los textos proporcionados."""
        logger.info("Generando embeddings para los chunks...")
        self.chunks = chunks
        self.embeddings = [get_embedding(c) for c in chunks]

    def search(self, query, top_k=TOP_K):
        """Devuelve los chunks más similares a la consulta."""
        if self.embeddings is None:
            raise ValueError("Retriever no inicializado")

        logger.info(f"Buscando top {top_k} chunks para la query")

        query_emb = get_embedding(query)

        similarities = [
            np.dot(query_emb, emb) for emb in self.embeddings
        ]

        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]