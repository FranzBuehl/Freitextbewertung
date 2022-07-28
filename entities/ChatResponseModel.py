from pydantic import BaseModel
from pydantic.fields import Optional


class ChatResponseModel(BaseModel):
    response: Optional[str] = ""
    success: bool
