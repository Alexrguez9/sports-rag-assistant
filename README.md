# Sports RAG Assistant

AI assistant basado en RAG (Retrieval-Augmented Generation) para consultar documentación técnica mediante búsqueda semántica.

## Características

- API REST con FastAPI
- Pipeline RAG completo
- Búsqueda semántica con embeddings
- Persistencia de embeddings en disco
- Logging estructurado
- Validación de requests con Pydantic

## Arquitectura

El sistema sigue un enfoque modular:

- `api/` → endpoints REST
- `services/` → lógica RAG
- `core/` → configuración y logging
- `embeddings/` → carga y chunking
- `retriever/` → búsqueda semántica
- `vector_store/` → persistencia

## Instalación

```bash
git clone https://github.com/tu-usuario/sports-rag-assistant.git
cd sports-rag-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Variables de entorno

Crear archivo .env:

```OPENAI_API_KEY=your_api_key```

## Ejecución

```uvicorn src.main:app --reload```

## Uso

Accede a:
```http://127.0.0.1:8000/docs```

Endpoint principal: POST /ask
Ejemplo:
```{ "question": "¿Cómo se gestionan las reservas?" }```

## Ejemplo de respuesta
```{ "answer": "Las reservas se gestionan..." }```
