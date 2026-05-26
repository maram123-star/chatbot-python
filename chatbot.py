import gradio as gr
from groq import Groq
import os

# Récupère la clé depuis une variable d'environnement
# Tu gardes ta clé sur ton PC, mais elle ne part pas sur GitHub
client = Groq(api_key="gsk_noOUZoD0mvDZ6vw0kVweWGdyb3FYoHuG1YimOs1S9xbiAiruWa6bgit ")  # ← garde ta clé ici pour ton PC
contexte_cours = """
Tu es un professeur de Python. Cours : print(), input(), if/else, for/while, def
"""

def repondre(question, historique):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": contexte_cours},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

interface = gr.ChatInterface(fn=repondre, title="Chatbot Python")
interface.launch()