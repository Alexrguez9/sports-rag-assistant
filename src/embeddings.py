import os

def load_documents(folder_path):
    """Carga todos los archivos de texto de una carpeta."""
    texts = []
    for file in os.listdir(folder_path):
        with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts


def chunk_text(text, chunk_size=200):
    """Divide un texto en chunks de N palabras."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks
