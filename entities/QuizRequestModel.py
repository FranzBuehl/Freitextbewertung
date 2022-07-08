from typing import Union
from pydantic import BaseModel

from entities.QuizSolution import QuizSolution


class QuizRequestModel(BaseModel):
    user: str
    quiz: Union[list[QuizSolution], None] = None
