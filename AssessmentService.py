import json
from os.path import exists

from entities.QuizAssessment import QuizAssessment
from entities.RatingScheme import RatingScheme
from entities.ExerciseAssessment import ExerciseAssessment
from entities.QuizRequestModel import QuizRequestModel
from entities.Rating import Rating
from helper.QuestionMapper import QuestionMapper
from keywordDetection.scripts.keyword_detection_service import get_keywords
from semanticSimilarity.scripts.semantic_similarity_service import get_similarity_score

#TODO read ratingScheme from config-tool
ratingScheme = RatingScheme(1, 3, {0.6: 1, 0.7: 2, 0.8: 3})

class AssessmentService:

    def assess(self, request: QuizRequestModel):
        assessments = []

        for exercise in request.quiz:
            exerciseAssessment = ExerciseAssessment()
            exerciseAssessment.exercise = exercise

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

            exerciseAssessment.rating = rating

            print('similarityScore:', rating.similarityScore, 'similarityPoints:', rating.similarityPoints, 'foundKeywords:', rating.foundKeywords, 'keywordPoints:', rating.keywordPoints)
            assessments.append(exerciseAssessment)

        quizAssessment = QuizAssessment(request.user, assessments)
        self.save_as_competence(quizAssessment)

        return quizAssessment.creation

    def save_as_competence(self, assessment: QuizAssessment):

        if exists('./assets/competencies.jsonl'):
            # read file
            with open('./assets/competencies.jsonl', 'r', encoding='utf-8') as file:
                data = json.load(file)
            file.close()
        else:
            data = []

        assessmentDict = assessment.to_dictionary()
        assessmentDict['competence'] = self.map_competence(assessment.points, assessment.maxPoints)
        data.append(assessmentDict)

        #write file
        with open('./assets/competencies.jsonl', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        # close the fileself,
        file.close()

    def map_competence(self, points, maxPoints):
        #user gets competence if 50% of the points are reached
        if points/maxPoints >= 0.5:
            return 'Arbeitsanalyse - Level 3'
        else:
            return '-'
