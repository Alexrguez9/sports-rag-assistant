"""
Punto de entrada del sistema RAG.

Orquesta el flujo completo:
- carga de documentos
- indexado (embeddings)
- recuperación
- generación de respuestas
"""

from embeddings import load_documents, chunk_text
from retriever import Retriever
from llm import ask_llm
from vector_store import VectorStore
from logger import logger


def main():
    logger.info("Iniciando sistema RAG...")

    # 1. Cargar documentos
    logger.info("Cargando documentos...")
    docs = load_documents("./data")
    logger.info(f"Documentos cargados: {len(docs)}")

    # 2. Crear chunks
    logger.info("Generando chunks...")
    chunks = []
    for doc in docs:
        chunks.extend(chunk_text(doc))
    logger.info(f"Total chunks generados: {len(chunks)}")

    # 3. Vector store (persistencia embeddings)
    vector_store = VectorStore()

    if vector_store.exists():
        logger.info("Cargando embeddings desde disco...")
        vector_store.load()
        chunks, embeddings = vector_store.get_chunks_and_embeddings()
        retriever = Retriever(chunks, embeddings)
    else:
        logger.info("No existen embeddings. Generándolos...")
        retriever = Retriever()
        retriever.build(chunks)
        vector_store.save(chunks, retriever.embeddings)
        logger.info("Embeddings generados y guardados.")

    logger.info("Sistema listo para recibir preguntas.")

    # 4. Loop de preguntas
    while True:
        question = input(">> ")

        if question.lower() == "exit":
            logger.info("Cerrando sistema.")
            break

        logger.info(f"Pregunta recibida: {question}")

        relevant_chunks = retriever.search(question)
        answer = ask_llm(question, relevant_chunks)

        print("\nRespuesta:\n", answer)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()