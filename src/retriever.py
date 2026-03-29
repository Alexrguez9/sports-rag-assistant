import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv
from config import TOP_K
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
    """Devuelve el embedding de un texto."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
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
        self.chunks = chunks
        self.embeddings = [get_embedding(c) for c in chunks]

    def search(self, query, top_k=TOP_K):
        """Devuelve los chunks más similares a la consulta."""
        query_emb = get_embedding(query)

        similarities = [
            np.dot(query_emb, emb) for emb in self.embeddings
        ]

        # Ordenar y quedarnos con los mejores
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]
