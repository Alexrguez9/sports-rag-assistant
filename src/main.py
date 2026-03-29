from embeddings import load_documents, chunk_text
from retriever import Retriever
from llm import ask_llm
from vector_store import VectorStore

# 1. Cargar documentos
docs = load_documents("./data")

# 2. Crear chunks
chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc))

# 3. Vector store
vector_store = VectorStore()

if not vector_store.exists():
    print("Generando embeddings...")
    retriever = Retriever()
    retriever.build(chunks)
    vector_store.save(chunks, retriever.embeddings)
else:
    print("Cargando embeddings guardados...")
    vector_store.load()
    chunks, embeddings = vector_store.get_chunks_and_embeddings()
    retriever = Retriever(chunks, embeddings)

print("Sistema listo. Escribe tu pregunta (exit para salir):\n")

while True:
    question = input(">> ")

    if question.lower() == "exit":
        break

    relevant_chunks = retriever.search(question)
    answer = ask_llm(question, relevant_chunks)

    print("\nRespuesta:\n", answer)
    print("\n" + "-"*50 + "\n")