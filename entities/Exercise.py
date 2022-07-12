from pydantic import BaseModel


class Exercise(BaseModel):
    questionId: int
    solution: str
