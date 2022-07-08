from pydantic import BaseModel


class QuizSolution(BaseModel):
    questionId: int
    text: str
