from fastapi import APIRouter

from app.models.question_model import (
    QuestionRequest
)

from app.services.question_generator_service import (
    generate_questions
)

router = APIRouter()


@router.post("/generate-questions")
def generate(
    request: QuestionRequest
):

    questions = generate_questions(
        request.domain,
        request.session_id
    )

    return {
        "session_id":
        request.session_id,

        "domain":
        request.domain,

        "questions":
        questions
    }