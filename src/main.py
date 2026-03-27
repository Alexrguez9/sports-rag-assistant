from embeddings import load_documents, chunk_text
from retriever import Retriever
from llm import ask_llm

# 1. Cargar documentos
docs = load_documents("./data")

# 2. Crear chunks
chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc))

# 3. Crear retriever
retriever = Retriever(chunks)

print("Sistema listo. Escribe tu pregunta (exit para salir):\n")

while True:
    question = input(">> ")

    if question.lower() == "exit":
        break

    relevant_chunks = retriever.search(question)
    answer = ask_llm(question, relevant_chunks)

    print("\nRespuesta:\n", answer)
    print("\n" + "-"*50 + "\n")