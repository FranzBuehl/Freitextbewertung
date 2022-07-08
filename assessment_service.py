from QuizAssessment import QuizAssessment
from SolutionAssessment import SolutionAssessment
from entities.QuizRequestModel import QuizRequestModel
from entities.Rating import Rating
from helper.QuestionMapper import QuestionMapper
from keywordDetection.scripts.keyword_detection_service import get_keywords


def assess(request: QuizRequestModel):
    assessments = []

    for quizSolution in request.quiz:
        solutionAssessnent = SolutionAssessment()
        solutionAssessnent.quizSolution = quizSolution
        maxKeywordPoints = 3
        if(QuestionMapper.has_sample_solution(quizSolution.questionId)):
            maxSimilarityPoints = 3
        else:
            maxSimilarityPoints = 0
        rating = Rating(maxKeywordPoints, maxSimilarityPoints)

        # if QuestionMapper.has_sample_solution(quizSolution.questionId):
        #     # @TODO add simularity scores
        #     return ""

        rating.foundKeywords = get_keywords(quizSolution)
        print(rating.foundKeywords)
        if len(rating.foundKeywords) > rating.maxKeywordPoints:
            rating.keywordPoints = rating.maxKeywordPoints
        else:
            rating.keywordPoints = len(rating.foundKeywords)
        print(rating.keywordPoints)

        solutionAssessnent.rating = rating
        print(solutionAssessnent.quizSolution.text)
        assessments.append(solutionAssessnent)

    for assessment in assessments:
        assessment.quizSolution = quizSolution
    quizAssessment = QuizAssessment(request.user, assessments)
    print(quizAssessment.points, quizAssessment.userId, quizAssessment.maxPoints, quizAssessment.creation)
    return quizAssessment.creation
