import ollama

def ask_llm(question: str, context: list[str], title: str):

    prompt = f"""
You are answering questions about ONE research paper.

Paper Title:
{title}

Retrieved Context:
{"\n\n".join(context)}

Question:
{question}

Rules:
- Answer ONLY from the retrieved context.
- Be concise.
- If the retrieved context does not contain the answer, reply exactly:
  The retrieved context does not contain the answer.
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]