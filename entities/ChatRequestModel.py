from pydantic import BaseModel


class ChatRequestModel(BaseModel):
    question: str
    answer: str = ""
