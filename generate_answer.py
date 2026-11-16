
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=api_key)


def generate_answer(question, context, history):

    history_text = "\n".join(
        [f"{message['role']}: {message['content']}" for message in history]
    )

    prompt = f"""
    Answer the question using only the provided document context.

    Use conversation history to understand follow-up questions.

    If the answer is not available in the context,
    say "I don't know based on the provided document."

    Conversation History:
    {history_text}

    Document Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text
