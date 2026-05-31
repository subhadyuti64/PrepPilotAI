from fastapi import APIRouter

from app.models.query_model import (
    QueryRequest
)

from app.services.rag_service import (
    ask_resume
)

router = APIRouter()


@router.post("/ask-resume")
def ask_question(
    request: QueryRequest
):

    answer = ask_resume(
        request.question,
        request.session_id
    )

    return {
        "session_id":
        request.session_id,

        "question":
        request.question,

        "answer":
        answer
    }