import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from app.services.vector_service import (
    load_vector_store
)

load_dotenv()


def generate_questions(
    domain: str,
    session_id: str
):

    vector_store = load_vector_store(
        session_id
    )

    docs = vector_store.similarity_search(
        f"Skills and projects related to {domain}",
        k=5
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
You are an expert technical interviewer.

Candidate Resume:
{context}

Generate 10 interview questions for:

{domain}

Requirements:
- Personalized to the candidate resume
- Beginner questions
- Intermediate questions
- Advanced questions
- Number them properly
- Return only questions
"""

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )

    response = llm.invoke(
        prompt
    )

    return response.content