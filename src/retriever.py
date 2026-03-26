import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_embedding(text):
    """Devuelve el embedding de un texto."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


class Retriever:
    """Búsqueda semántica básica sobre una lista de textos."""
    def __init__(self, chunks):
        # Guardar textos y calcular embeddings
        self.chunks = chunks
        self.embeddings = [get_embedding(c) for c in chunks]

    def search(self, query, top_k=3):
        """Devuelve los chunks más similares a la query."""
        query_emb = get_embedding(query)

        similarities = [
            np.dot(query_emb, emb) for emb in self.embeddings
        ]

        # Ordenar y quedarnos con los mejores
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [self.chunks[i] for i in top_indices]
