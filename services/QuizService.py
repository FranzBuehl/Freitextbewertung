import json
from os.path import exists

from entities.QuizRating import QuizRating
from entities.RatingScheme import RatingScheme
from entities.ExerciseRating import ExerciseRating
from entities.QuizRequestModel import QuizRequestModel
from entities.Rating import Rating
from helper.QuestionMapper import QuestionMapper
from keywordDetection.scripts.keyword_detection import get_keywords
from semanticSimilarity.scripts.semantic_similarity import get_similarity_score

#TODO read ratingScheme from config-tool

ratingScheme = RatingScheme(1, 3, {0.6: 1, 0.7: 2, 0.8: 3})

class QuizService:

    def rate(self, request: QuizRequestModel):
        ratings = []

        for exercise in request.quiz:
            exerciseRatings = ExerciseRating()
            exerciseRatings.exercise = exercise

            if(QuestionMapper.has_sample_solution(exercise.questionId)):
                                        #Get last Element
                lastKey = list(ratingScheme.pointsForSimilarity)[-1]
                maxSimilarityPoints = ratingScheme.pointsForSimilarity[lastKey]
            else:
                maxSimilarityPoints = 0

            rating = Rating(ratingScheme.maxPointsKeywords, maxSimilarityPoints)

            #similarity Rating
            if QuestionMapper.has_sample_solution(exercise.questionId):
                rating.similarityScore = get_similarity_score(exercise.questionId, exercise.solution)
                pointThresholds = ratingScheme.pointsForSimilarity.keys()
                for threshold in pointThresholds:
                    if rating.similarityScore >= threshold:
                        rating.similarityPoints = ratingScheme.pointsForSimilarity[threshold]

            #keyword rating
            rating.foundKeywords = get_keywords(exercise)

            if len(rating.foundKeywords) * ratingScheme.pointsPerKeyword > rating.maxPointsKeyword:
                rating.keywordPoints = rating.maxPointsKeyword
            else:
                rating.keywordPoints = len(rating.foundKeywords) * ratingScheme.pointsPerKeyword

            exerciseRatings.rating = rating

            print('similarityScore:', rating.similarityScore, 'similarityPoints:', rating.similarityPoints, 'foundKeywords:', rating.foundKeywords, 'keywordPoints:', rating.keywordPoints)
            ratings.append(exerciseRatings)

        quizRating = QuizRating(request.user, ratings)
        self.save_as_competence(quizRating)

        return quizRating

    def save_as_competence(self, rating: QuizRating):

        if exists('assets/competencies.json'):
            # read file
            with open('assets/competencies.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            file.close()
        else:
            data = []

        ratingDict = rating.to_dictionary()
        ratingDict['competence'] = self.map_competence(rating.points, rating.maxPoints)
        data.append(ratingDict)

        #write file
        with open('assets/competencies.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        file.close()

    def map_competence(self, points, maxPoints):
        #user gets competence if 50% of the points are reached
        if points/maxPoints >= 0.5:
            return 'Arbeitsanalyse - Level 3'
        else:
            return '-'
