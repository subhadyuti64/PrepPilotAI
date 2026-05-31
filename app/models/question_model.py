from pydantic import BaseModel


class QuestionRequest(BaseModel):

    session_id: str

    domain: str