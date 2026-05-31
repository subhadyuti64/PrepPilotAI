import json

from fastapi import APIRouter

from app.models.interview_model import (
    InterviewRequest,
    EvaluationRequest
)

from app.services.interview_service import (
    generate_interview_question,
    evaluate_answer
)

router = APIRouter()


@router.post("/start-mock-interview")
def start_interview(
    request: InterviewRequest
):

    question = generate_interview_question(
        request.domain,
        request.session_id
    )

    return {
        "session_id":
        request.session_id,

        "domain":
        request.domain,

        "question":
        question
    }


@router.post("/evaluate-answer")
def evaluate(
    request: EvaluationRequest
):

    result = evaluate_answer(
        request.question,
        request.answer
    )

    try:

        return json.loads(
            result
        )

    except Exception:

        return {
            "raw_response":
            result
        }