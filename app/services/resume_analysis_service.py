import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from app.services.vector_service import (
    load_vector_store
)

load_dotenv()


def analyze_resume(
    session_id: str
):

    # =========================
    # Load User Resume
    # =========================

    vector_store = load_vector_store(
        session_id
    )

    docs = vector_store.similarity_search(
        "Analyze complete resume",
        k=10
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
You are an expert technical recruiter.

Analyze the resume below.

Resume:
{context}

Return ONLY valid JSON.

{{
  "candidate_name": "",
  "education": "",
  "skills": [],
  "projects": [],
  "strengths": [],
  "recommended_roles": [],
  "areas_for_improvement": []
}}

Do not return markdown.
Do not return explanations.
Return JSON only.
"""

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )

    response = llm.invoke(
        prompt
    )

    return response.content