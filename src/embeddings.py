import os

def load_documents(folder_path):
    """
    Carga todos los archivos de texto de una carpeta.

    - folder_path: ruta a la carpeta de documentos
    - devuelve: lista de textos
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"No existe la carpeta: {folder_path}")

    texts = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Ignorar subdirectorios
        if not os.path.isfile(file_path):
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                texts.append(f.read())
        except Exception as e:
            print(f"Error leyendo {file}: {e}")

    return texts

def chunk_text(text, chunk_size=200):
    """Divide un texto en chunks de N palabras."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks
