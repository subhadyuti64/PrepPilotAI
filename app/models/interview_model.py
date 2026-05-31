from pydantic import BaseModel


class InterviewRequest(BaseModel):

    session_id: str

    domain: str


class EvaluationRequest(BaseModel):

    question: str

    answer: str