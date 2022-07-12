from QuizAssessment import QuizAssessment
from RatingScheme import RatingScheme
from ExerciseAssessment import ExerciseAssessment
from entities.QuizRequestModel import QuizRequestModel
from entities.Rating import Rating
from helper.QuestionMapper import QuestionMapper
from keywordDetection.scripts.keyword_detection_service import get_keywords
from semanticSimilarity.scripts.semantic_similarity_service import get_similarity_score

ratingScheme = RatingScheme(1, 3, {0.6: 1, 0.7: 2, 0.8: 3})

def assess(request: QuizRequestModel):
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

        if QuestionMapper.has_sample_solution(exercise.questionId):
            rating.similarityScore = get_similarity_score(exercise.questionId, exercise.solution)
            pointThresholds = ratingScheme.pointsForSimilarity.keys()
            for threshold in pointThresholds:
                if rating.similarityScore >= threshold:
                    rating.similarityPoints = ratingScheme.pointsForSimilarity[threshold]

        rating.foundKeywords = get_keywords(exercise)

        if len(rating.foundKeywords) > rating.maxPointsKeyword:
            rating.keywordPoints = rating.maxPointsKeyword
        else:
            rating.keywordPoints = len(rating.foundKeywords)


        exerciseAssessment.rating = rating
        print('similarityScore:', rating.similarityScore, 'similarityPoints:', rating.similarityPoints, 'foundKeywords:', rating.foundKeywords, 'keywordPoints:', rating.keywordPoints)
        assessments.append(exerciseAssessment)

    quizAssessment = QuizAssessment(request.user, assessments)
    # print(quizAssessment.points, quizAssessment.userId, quizAssessment.maxPoints, quizAssessment.creation)/
    return quizAssessment.creation
