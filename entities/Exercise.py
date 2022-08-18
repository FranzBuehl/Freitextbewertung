from pydantic import BaseModel


class Exercise(BaseModel):
    questionId: int
    solution: str

    def to_dictionary(self):
        dict = {}
        dict['questionId'] = self.questionId
        dict['solution'] = self.solution

        return dict


