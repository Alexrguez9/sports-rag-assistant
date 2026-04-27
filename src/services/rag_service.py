"""
Servicio que encapsula el pipeline completo de RAG.
"""

from src.embeddings import load_documents, chunk_text
from src.retriever import Retriever
from src.vector_store import VectorStore
from src.llm import ask_llm
from src.core.logger import logger


class RAGService:
    """Orquesta el pipeline completo de RAG."""

    def __init__(self, data_path="./data"):
        """
        Inicializa el sistema:
        - carga documentos
        - genera o carga embeddings
        """
        logger.info("Inicializando RAGService...")

        docs = load_documents(data_path)

        chunks = []
        for doc in docs:
            chunks.extend(chunk_text(doc))

        logger.info(f"Chunks generados: {len(chunks)}")

        vector_store = VectorStore()

        if vector_store.exists():
            logger.info("Cargando embeddings desde disco...")
            vector_store.load()
            chunks, embeddings = vector_store.get_chunks_and_embeddings()
            self.retriever = Retriever(chunks, embeddings)
        else:
            logger.info("Generando embeddings...")
            self.retriever = Retriever()
            self.retriever.build(chunks)
            vector_store.save(chunks, self.retriever.embeddings)
            logger.info("Embeddings generados y guardados.")

    def ask(self, question: str) -> str:
        """
        Responde una pregunta utilizando RAG.

        - question: pregunta del usuario
        """
        logger.info(f"Procesando pregunta: {question}")

        relevant_chunks = self.retriever.search(question)
        answer = ask_llm(question, relevant_chunks)

        return answer