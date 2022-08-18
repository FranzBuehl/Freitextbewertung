from pydantic import BaseModel
from pydantic.fields import Optional


class ChatAnswerResponseModel(BaseModel):
    response: Optional[str]
    success: bool


