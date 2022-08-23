from pydantic import BaseModel


class Exercise(BaseModel):
    questionId: str
    solution: str

    def to_dictionary(self):
        dict = {}
        dict['questionId'] = self.questionId
        dict['solution'] = self.solution

        return dict

    def has_sample_solution(self):
        return "Arbeitsgestaltung" in self.questionId
