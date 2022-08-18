from typing import Union
from pydantic import BaseModel

from entities.Exercise import Exercise


class QuizRequestModel(BaseModel):
    user: str
    quiz: Union[list[Exercise], None] = None


