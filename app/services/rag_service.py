import os

from dotenv import load_dotenv

from langchain_openai import (
    ChatOpenAI,
    OpenAIEmbeddings
)

from app.services.vector_service import (
    load_vector_store
)

load_dotenv()


def ask_resume(
    question: str,
    session_id: str
):

    # =========================
    # Load User Vector Store
    # =========================

    vector_store = load_vector_store(
        session_id
    )

    # =========================
    # Retrieve Relevant Chunks
    # =========================

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    # =========================
    # Prompt
    # =========================

    prompt = f"""
You are PrepPilot AI.

Answer ONLY from the resume context.

If the answer is not present in the resume,
say:

"I could not find that information in the uploaded resume."

Resume Context:
{context}

Question:
{question}
"""

    # =========================
    # LLM
    # =========================

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