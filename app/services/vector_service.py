import os

from dotenv import load_dotenv

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_openai import (
    OpenAIEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

load_dotenv()


def create_vector_store(
    documents,
    session_dir
):

    # =========================
    # Split Documents
    # =========================

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    # =========================
    # Create Embeddings
    # =========================

    embeddings = OpenAIEmbeddings(
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )

    # =========================
    # Create FAISS
    # =========================

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    # =========================
    # Save To User Folder
    # =========================

    vector_store.save_local(
        session_dir
    )

    return len(chunks)


# =====================================
# LOAD VECTOR STORE
# =====================================

def load_vector_store(
    session_id
):

    embeddings = OpenAIEmbeddings(
        api_key=os.getenv(
            "OPENAI_API_KEY"
        )
    )

    vector_store = FAISS.load_local(
        f"vectorstores/{session_id}",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store