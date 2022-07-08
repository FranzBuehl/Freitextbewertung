from datetime import datetime
import SolutionAssessment


class QuizAssessment():
    userId: str
    creation: datetime
    assessments: [SolutionAssessment]
    points: int = 0
    maxPoints: int = 0

    def __init__(self, userId, assessments):
        self.userId = userId
        self.assessments = assessments
        self.creation = datetime.now()
        for assessment in assessments:
            self.points += assessment.rating.similarityPoints + assessment.rating.keywordPoints
            self.maxPoints += assessment.rating.maxSimilaityPoints + assessment.rating.maxKeywordPoints

