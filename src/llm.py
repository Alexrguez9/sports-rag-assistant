import os
from openai import OpenAI
from dotenv import load_dotenv
from config import OPENAI_API_KEY, CHAT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(question, context_chunks):
    """
    Responde una pregunta usando contexto (RAG básico).
    
    - question: pregunta del usuario
    - context_chunks: lista de textos relevantes
    """
    context = "\n\n".join(context_chunks)

    prompt = f"""
Responde a la pregunta usando SOLO el contexto proporcionado.

Contexto:
{context}

Pregunta:
{question}
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content