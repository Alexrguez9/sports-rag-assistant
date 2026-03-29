import json
import os

class VectorStore:
    """Gestiona la persistencia de embeddings en disco."""

    def __init__(self, path="data/embeddings.json"):
        """Inicializa el almacén de vectores con una ruta de almacenamiento."""
        self.path = path
        self.data = []

    def exists(self):
        """Comprueba si existe un archivo de embeddings persistido."""
        return os.path.exists(self.path)

    def save(self, chunks, embeddings):
        """Guarda los chunks y sus embeddings asociados en disco."""
        self.data = [
            {"chunk": c, "embedding": e}
            for c, e in zip(chunks, embeddings)
        ]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f)

    def load(self):
        """Carga los embeddings previamente guardados."""
        with open(self.path, "r") as f:
            self.data = json.load(f)

    def get_chunks_and_embeddings(self):
        """Devuelve los chunks y embeddings almacenados."""
        chunks = [item["chunk"] for item in self.data]
        embeddings = [item["embedding"] for item in self.data]
        return chunks, embeddings
