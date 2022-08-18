from datetime import datetime
from entities import ExerciseRating


class QuizRating():
    userId: str
    creation: datetime
    exerciseRatings: [ExerciseRating]
    explanationPath: str
    points: int = 0
    maxPoints: int = 0

    def __init__(self, userId, exerciseRatings):
        self.userId = userId
        self.exerciseRatings = exerciseRatings
        now = datetime.today()
        self.creation = now.strftime('%d-%m-%Y %H:%M:%S')
        for exerciseRating in exerciseRatings:
            self.points += exerciseRating.rating.similarityPoints + exerciseRating.rating.keywordPoints
            self.maxPoints += exerciseRating.rating.maxPointsSimilaity + exerciseRating.rating.maxPointsKeyword

        self.explanationPath = 'assets/explanations/'+ self.userId +'_'+ now.strftime('%d-%m-%Y_%H.%M.%S') + '.html'


    def to_dictionary(self):
        dict = {}
        dict['userId'] = self.userId
        dict['creation'] = self.creation
        dict['exerciseRatings'] = [exerciseRating.to_dictionary() for exerciseRating in self.exerciseRatings]
        dict['explanationPath'] = self.explanationPath
        dict['pointsTotal'] = self.points
        dict['maxPointsTotal'] = self.maxPoints

        return dict

