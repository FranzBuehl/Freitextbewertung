from pydantic import BaseModel


class ChatEvaluationResponseModel(BaseModel):
    success: bool


