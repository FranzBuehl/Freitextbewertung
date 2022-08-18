from pydantic import BaseModel

class ChatEvaluationRequestModel(BaseModel):
    question: str
    answer: str






