from datetime import datetime
from entities import ExerciseAssessment


class QuizAssessment():
    userId: str
    creation: datetime
    assessments: [ExerciseAssessment]
    points: int = 0
    maxPoints: int = 0

    def __init__(self, userId, assessments):
        self.userId = userId
        self.assessments = assessments
        self.creation = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        for assessment in assessments:
            self.points += assessment.rating.similarityPoints + assessment.rating.keywordPoints
            self.maxPoints += assessment.rating.maxPointsSimilaity + assessment.rating.maxPointsKeyword


    def to_dictionary(self):
        dict = {}
        dict['userId'] = self.userId
        dict['creation'] = self.creation
        dict['assessments'] = [assessment.to_dictionary() for assessment in self.assessments]
        dict['points'] = self.points
        dict['maxPoints'] = self.maxPoints

        return dict

