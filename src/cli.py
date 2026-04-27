"""
Interfaz CLI para probar el sistema RAG sin API.
"""

from src.services.rag_service import RAGService
from src.core.logger import logger


def main():
    logger.info("Iniciando CLI RAG...")

    rag_service = RAGService()

    while True:
        question = input(">> ")

        if question.lower() == "exit":
            break

        answer = rag_service.ask(question)

        print("\nRespuesta:\n", answer)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()