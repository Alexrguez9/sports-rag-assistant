"""
Interacción con el modelo de lenguaje.
"""

from openai import OpenAI
from src.core.config import OPENAI_API_KEY, CHAT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(question, context_chunks):
    """
    Responde una pregunta usando contexto (RAG básico).
    """
    context = "\n\n".join(context_chunks)

    prompt = f"""
- Si no hay información suficiente, di que no lo sabes.
- No inventes información.
- Responde de forma clara y concisa.

Contexto:
{context}

Pregunta:
{question}
"""

    try:
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generando respuesta: {str(e)}"