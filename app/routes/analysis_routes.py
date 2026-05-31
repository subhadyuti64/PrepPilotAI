import json

from fastapi import APIRouter

from app.models.session_model import (
    SessionRequest
)

from app.services.resume_analysis_service import (
    analyze_resume
)

router = APIRouter()


@router.post("/analyze-resume")
def analyze(
    request: SessionRequest
):

    result = analyze_resume(
        request.session_id
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